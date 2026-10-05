"""Contrôle qualité des PDF de `serveur/` et de `courriels/` (pièces reçues par William hors serveur) — À LANCER après chaque génération de livrable.

    python outils/verifier_pdf.py

Vérifie pour chaque PDF : texte extractible (pas de PDF vide, cf. incident des contrats
vierges du 20/07) et absence de mots français courants écrits SANS accent (William a recadré
Mariette et Grace pour ça le 18/07). Code de sortie 1 s'il y a un avertissement.
Les noms de dossiers cités avec une barre oblique (conformite/, rh/) ne sont pas contrôlés : les
dossiers n'ont pas d'accent.
"""
import re
import sys
from pathlib import Path

from pypdf import PdfReader

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent

# forme fautive -> forme correcte (insensible à la casse, mots entiers)
SANS_ACCENT = {
    "synthese": "synthèse", "equipe": "équipe", "equipes": "équipes", "evaluation": "évaluation",
    "gerant": "gérant", "gerante": "gérante", "pole": "pôle", "poles": "pôles", "energies": "énergies",
    "tracabilite": "traçabilité", "reglement": "règlement", "interieur": "intérieur", "duree": "durée",
    "determinee": "déterminée", "redigee": "rédigée", "detaillee": "détaillée", "bareme": "barème",
    "assiduite": "assiduité", "execution": "exécution", "hierarchie": "hiérarchie", "numerise": "numérisé",
    "numerisee": "numérisée", "societe": "société", "remuneration": "rémunération", "generale": "générale",
    "aicha": "Aïcha", "diomande": "Diomandé", "toure": "Touré",
    "conformite": "conformité", "budgetisation": "budgétisation", "prevu": "prévu", "creation": "création",
    "reference": "référence", "periode": "période", "modifie": "modifié", "verifie": "vérifié",
}

# un mot immédiatement suivi d'une barre oblique est un nom de dossier (pas de contrôle d'accent)
MOTIF_DOSSIER = re.compile(r"[A-Za-z_]+" + "/")
MOTIF_MOT = re.compile(r"[A-Za-zÀ-ÿ']+")


def main():
    pdfs = sorted((RACINE / "serveur").rglob("*.pdf")) + sorted((RACINE / "courriels").rglob("*.pdf"))
    if not pdfs:
        print("Aucun PDF dans serveur/ ni courriels/.")
        return 0
    erreurs = 0
    for p in pdfs:
        texte = "\n".join((pg.extract_text() or "") for pg in PdfReader(str(p)).pages)
        rel = p.relative_to(RACINE)
        if len(texte.strip()) < 80:
            print(f"[VIDE ] {rel} : texte quasi absent ({len(texte.strip())} caractères)")
            erreurs += 1
            continue
        sans_dossiers = MOTIF_DOSSIER.sub(" ", texte)
        mots = {m.lower() for m in MOTIF_MOT.findall(sans_dossiers)}
        fautes = sorted(f"{k}->{v}" for k, v in SANS_ACCENT.items() if k in mots)
        if fautes:
            print(f"[ACCENT] {rel} : {', '.join(fautes)}")
            erreurs += 1
        else:
            print(f"[ OK  ] {rel}")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
