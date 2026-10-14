"""CONVERSATIONS WHATSAPP DE WILLIAM (`whatsapp/<nom>.md`) en une commande (créé le 14/10/2026). Le format est celui que lisent la base
et le téléphone : « **[JJ/MM/AAAA - HH:MM (Lieu)] Auteur :** texte ». Un message de William ajoute aussi sa trace (`traces.py`) ;
un message d'un contact peut être programmé d'avance par `reactions.py` (puis joué par `reactions.py jouer`).

    python outils/whatsapp.py message --avec "Clément Grandjean" --auteur william|contact --texte "…" [--quand "AAAA-MM-JJ HH:MM"]
    python outils/whatsapp.py voir "Clément Grandjean"

L'heure est celle de l'horloge (son fuseau) ; le lieu affiché suit le fuseau (Luxembourg, Manille…).
"""
import argparse
import sys

from commun import OUTILS, RACINE, ajouter_texte, ecrire_texte, lire_texte, slug, utf8

sys.path.insert(0, str(OUTILS))
DOSSIER = RACINE / "whatsapp"
LIEUX = {"luxembourg": "Luxembourg", "manille": "Manille", "paris": "Paris", "abidjan": "Abidjan", "lisbonne": "Lisbonne"}


def fichier(nom):
    return DOSSIER / f"{slug(nom)}.md"


def message(avec, auteur, texte, quand_txt=None):
    import horloge
    import jet
    h = horloge.lire()
    p = jet.fiche_personnage(avec)
    nom = p["nom"] if p else avec
    quand_txt = quand_txt or f"{h['instant']:%Y-%m-%d %H:%M}"
    d, hh = quand_txt.split()
    a, m, j = d.split("-")
    f = fichier(nom)
    if not f.exists():
        ecrire_texte(f, f"# Conversation WhatsApp : William / {nom}\n\n")
    qui = "William" if auteur == "william" else nom
    lieu = LIEUX.get(h["fuseau"], h["fuseau"].capitalize())
    ajouter_texte(f, f"**[{j}/{m}/{a} - {hh} ({lieu})] {qui} :** {texte.strip()}\n")
    if auteur == "william":
        import traces
        traces.ajouter(f"{j}/{m}/{a} {hh.replace(':', 'h')}" + ("" if lieu == "Luxembourg" else f" ({lieu})"),
                       f"Message WhatsApp à {nom} : « {texte.strip()[:160]} »", "conversation WhatsApp", f"{nom} (captures possibles)",
                       "faible", etiquette=f"{j}/{m}/{a}, {hh.replace(':', 'h')}")
    return f


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("message")
    p.add_argument("--avec", required=True)
    p.add_argument("--auteur", choices=("william", "contact"), required=True)
    p.add_argument("--texte", required=True)
    p.add_argument("--quand")
    p = sp.add_parser("voir")
    p.add_argument("nom")
    args = ap.parse_args()
    if args.cmd == "message":
        f = message(args.avec, args.auteur, args.texte, args.quand)
        print(f"Message enregistré dans {f.relative_to(RACINE).as_posix()}")
        return 0
    print(lire_texte(fichier(args.nom)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
