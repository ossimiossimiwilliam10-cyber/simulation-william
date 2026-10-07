"""Évaluation d'Aïcha Diomandé par William (26/07/2040) -> serveur/rh/evaluations/evaluation_aicha_2607.pdf (déplacé de direction/ par Mariette le 26/07 à 14h59, sur ordre de William)

Évaluation menée en questions-réponses entre William et le moteur (26/07/2040, 14h08-14h26), critère par critère, selon la matrice
d'évaluation détaillée v1.0 (`serveur/rh/matrice_evaluation.pdf`). Notes de William : 5, 7, 5, 24, 18, 15 ; ajustement discrétionnaire : 0
-> total 74 / 100, tranche « de 61 à 85 : performance standard (maintien) ». William n'a donné aucune observation écrite : le document ne
contient que les notes (le moteur n'ajoute ni commentaire ni motif). William l'uploade dans `direction/` à 14h28 (dossier non précisé :
lu comme celui qu'il cite pour les autres évaluations).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Évaluation d'Aïcha Diomandé",
              "OSIA Énergies — évaluation du 26/07/2040 selon la matrice d'évaluation détaillée v1.0 (20/07/2040)")
pdf.meta("Évaluée", "Aïcha Diomandé, gérante et directrice générale (pôle Direction / gestion)")
pdf.meta("Évaluateur", "William Ossimi, Direction générale (associé unique)")
pdf.meta("Date", "26 juillet 2040")
pdf.meta("Barème", "Matrice v1.0 : tronc commun (30 points), direction / gestion (70 points), ajustement discrétionnaire")

pdf.titre1("Notes")
lignes = [
    ["Tronc commun", "1. Assiduité et ponctualité", "5", "10"],
    ["", "2. Respect des directives et de la hiérarchie", "7", "10"],
    ["", "3. Usage du serveur et traçabilité", "5", "10"],
    ["", "Sous-total tronc commun", "17", "30"],
    ["Direction / gestion", "4. Rentabilité globale", "24", "30"],
    ["", "5. Coordination des pôles", "18", "20"],
    ["", "6. Reporting", "15", "20"],
    ["", "Sous-total direction / gestion", "57", "70"],
    ["Ajustement", "7. Ajustement discrétionnaire de la Direction générale (bonus / malus)", "0", "—"],
    ["Total", "", "74", "100"],
]
pdf.tableau(["Bloc", "Critère", "Note", "Maximum"], lignes, (32, 88, 25, 25))

pdf.titre1("Résultat")
pdf.para("Score : 74 / 100.")
pdf.para("Tranche de la matrice : de 61 à 85 / 100 — performance standard (maintien).")

pdf.sauver(serveur("rh", "evaluations", "evaluation_aicha_2607.pdf"))
