"""COURRIEL REÇU (créé le 13/10/2026) : toute pièce reçue par William par courriel devient un vrai PDF dans `courriels/`
(règle 4 du fichier maître), lu par l'application Courriels du téléphone. Un seul outil pour tous les courriels du monde
(administrations, hôtel, banque, tentatives d'arnaque…), au lieu d'un script par pièce.

    python outils/courriel.py --de "Nom <adresse>" --objet "…" --texte fichier.txt --quand "2040-07-16 20:14" [--nom-fichier "…"]

Le texte est écrit tel que William le reçoit (langue de l'expéditeur comprise) ; une ligne vide sépare les paragraphes.
"""
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

from commun import OUTILS, slug, utf8

sys.path.insert(0, str(OUTILS))


def ecrire(de, objet, texte, quand, nom_fichier=None):
    from pdf_base import DocPDF, chemin
    pdf = DocPDF(objet, f"Reçu le {quand:%d/%m/%Y} à {quand:%H:%M}", auteur=de, pied="Courriel reçu")
    pdf.meta("De", de)
    pdf.meta("À", "William Ossimi")
    pdf.meta("Objet", objet)
    for para in re.split(r"\n\s*\n", texte.strip()):
        pdf.para(" ".join(l.strip() for l in para.splitlines()))
    nom = nom_fichier or f"{quand:%Y-%m-%d}_{slug(objet)[:60]}.pdf"
    cible = chemin("courriels", nom)
    pdf.sauver(cible)
    return cible


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--de", required=True)
    ap.add_argument("--objet", required=True)
    ap.add_argument("--texte", required=True, help="fichier texte (UTF-8) du corps du courriel")
    ap.add_argument("--quand", required=True, help="AAAA-MM-JJ HH:MM (heure de réception, fuseau de William)")
    ap.add_argument("--nom-fichier")
    args = ap.parse_args()
    cible = ecrire(args.de, args.objet, Path(args.texte).read_text(encoding="utf-8"), dt.datetime.fromisoformat(args.quand), args.nom_fichier)
    print(f"Courriel écrit : {cible}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
