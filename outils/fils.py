"""FILS OUVERTS (`etat/fils-ouverts.md`) en une commande (créé le 14/10/2026 : fini les remplacements de texte écrits à la main).
Les lignes des tableaux portent un numéro en première colonne (« | 4 | … », « | I4 | … ») ; rien ne s'efface : une note s'ajoute
à la fin de la case « Contexte », une clôture barre le sujet et garde tout.

    python outils/fils.py noter 4 "Kiara confirme samedi 15h"          # ajoute « ; *(20/07 14h46) Kiara confirme samedi 15h* »
    python outils/fils.py clore 5 "réglé : Clément a pris bien le refus"
    python outils/fils.py ajouter --sujet "Grab installé" --contexte "…" [--echeance "—"]
    python outils/fils.py horodater                                       # en-tête « au … » réglé sur l'horloge
    python outils/fils.py liste
"""
import argparse
import re
import sys

from commun import ETAT, OUTILS, date_fr, ecrire_texte, heure_fr, lire_texte, utf8

sys.path.insert(0, str(OUTILS))
FICHIER = ETAT / "fils-ouverts.md"
LIGNE = re.compile(r"^\| ([A-Z]?\d+) \| (.*) \| (.*) \| (.*) \|\s*$")


def maintenant():
    import horloge
    h = horloge.lire()
    return h


def etiquette_courte(h):
    t = h["instant"]
    return f"{t:%d/%m} {t:%H}h{t:%M}"


def horodater():
    h = maintenant()
    t = lire_texte(FICHIER)
    suffixe = "" if h["fuseau"] == "luxembourg" else f", heure de {h['fuseau'].capitalize()}"
    nouveau = re.sub(r"\(univers 2 ; au [^)]*\)", f"(univers 2 ; au {date_fr(h['instant'])}, {heure_fr(h['instant'])}{suffixe})", t, count=1)
    ecrire_texte(FICHIER, nouveau)


def _modifier(ident, fonction):
    lignes = lire_texte(FICHIER).split("\n")
    for i, l in enumerate(lignes):
        m = LIGNE.match(l.rstrip("\r"))
        if m and m.group(1) == ident:
            lignes[i] = fonction(m)
            ecrire_texte(FICHIER, "\n".join(lignes))
            horodater()
            return lignes[i]
    sys.exit(f"Fil introuvable : {ident}")


def noter(ident, texte):
    h = maintenant()
    note = f" ; *({etiquette_courte(h)}) {texte.replace('|', '/')}*"
    return _modifier(ident, lambda m: f"| {m.group(1)} | {m.group(2)} | {m.group(3)}{note} | {m.group(4)} |")


def clore(ident, texte):
    h = maintenant()
    def f(m):
        sujet = m.group(2) if m.group(2).startswith("~~") else f"~~{m.group(2)}~~"
        return f"| {m.group(1)} | {sujet} **CLOS le {etiquette_courte(h)}** : {texte.replace('|', '/')} | {m.group(3)} | {m.group(4)} |"
    return _modifier(ident, f)


def ajouter(sujet, contexte, echeance="—"):
    lignes = lire_texte(FICHIER).split("\n")
    dernier, nums = None, []
    for i, l in enumerate(lignes):
        m = LIGNE.match(l.rstrip("\r"))
        if m and m.group(1).isdigit():
            dernier, nums = i, nums + [int(m.group(1))]
    if dernier is None:
        sys.exit("Tableau A introuvable dans etat/fils-ouverts.md")
    n = max(nums) + 1
    h = maintenant()
    lignes.insert(dernier + 1, f"| {n} | **{sujet.replace('|', '/')}** ({etiquette_courte(h)}) | {contexte.replace('|', '/')} | {echeance} |")
    ecrire_texte(FICHIER, "\n".join(lignes))
    horodater()
    return n


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("noter")
    p.add_argument("id")
    p.add_argument("texte")
    p = sp.add_parser("clore")
    p.add_argument("id")
    p.add_argument("texte")
    p = sp.add_parser("ajouter")
    p.add_argument("--sujet", required=True)
    p.add_argument("--contexte", required=True)
    p.add_argument("--echeance", default="—")
    sp.add_parser("horodater")
    sp.add_parser("liste")
    args = ap.parse_args()
    if args.cmd == "noter":
        noter(args.id, args.texte)
        print(f"Fil {args.id} : note ajoutée")
    elif args.cmd == "clore":
        clore(args.id, args.texte)
        print(f"Fil {args.id} : clos")
    elif args.cmd == "ajouter":
        print(f"Fil {ajouter(args.sujet, args.contexte, args.echeance)} ajouté")
    elif args.cmd == "horodater":
        horodater()
        print("En-tête réglé sur l'horloge")
    else:
        for l in lire_texte(FICHIER).split("\n"):
            m = LIGNE.match(l.rstrip("\r"))
            if m:
                print(f"{m.group(1):>3} | {re.sub(r'[*~]', '', m.group(2))[:110]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
