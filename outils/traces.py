"""DOSSIER DES TRACES DE WILLIAM (`etat/traces.md`) en une commande (créé le 14/10/2026 : moins d'écriture à la main pour l'IA).
Chaque écrit, signature, message ou paiement de William qui peut ressortir s'ajoute ici ; `rencontres.py` et `whatsapp.py` le font
d'eux-mêmes pour les messages de William.

    python outils/traces.py ajouter --quand "AAAA-MM-JJ HH:MM" --trace "…" --support "…" --qui "…" [--exposition faible|moyenne|forte]
"""
import argparse
import re
import sys

from commun import ETAT, ajouter_texte, lire_texte, ecrire_texte, utf8

FICHIER = ETAT / "traces.md"


def horodater(etiquette):
    t = lire_texte(FICHIER)
    nouveau = re.sub(r"à jour au [^)]*\)", f"à jour au {etiquette})", t, count=1)
    if nouveau != t:
        ecrire_texte(FICHIER, nouveau)


def ajouter(quand_txt, trace, support, qui, exposition="faible", etiquette=None):
    nettoie = lambda s: s.replace("|", "/").replace("\n", " ").strip()  # noqa: E731
    ajouter_texte(FICHIER, f"| {nettoie(quand_txt)} | {nettoie(trace)} | {nettoie(support)} | {nettoie(qui)} | {exposition} |\n")
    if etiquette:
        horodater(etiquette)


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("ajouter")
    p.add_argument("--quand", required=True)
    p.add_argument("--trace", required=True)
    p.add_argument("--support", required=True)
    p.add_argument("--qui", required=True)
    p.add_argument("--exposition", default="faible", choices=("faible", "moyenne", "forte"))
    args = ap.parse_args()
    ajouter(args.quand, args.trace, args.support, args.qui, args.exposition)
    print("Trace ajoutée")
    return 0


if __name__ == "__main__":
    sys.exit(main())
