"""Charte interne et système d'évaluation (réunion du 19/07/2040) -> serveur/direction/charte_et_evaluation_1907.pdf

Contenu inchangé (version relue par William le 19/07 ; il a refusé la section 2, jugée trop vague,
remplacée par la matrice détaillée du 20/07). Seul le moteur de génération a changé.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Charte interne et système d'évaluation — OSIA Énergies")
pdf.meta("Date", "19/07/2040")
pdf.meta("Auteurs", "Aïcha Diomandé, Mariette Kouadio, Grace Adjoua-Mensah, Abdoul Touré, Yves Kanga")

pdf.titre1("1. Règlement intérieur (charte)")
pdf.puces([
    "Horaires de travail : 08h00 - 17h00 (pause de 12h30 à 13h30).",
    "Confidentialité : interdiction stricte de divulguer les informations financières, les salaires et les données clients.",
    "Pôle technique : port obligatoire des EPI (équipements de protection individuelle) sur les chantiers. Entretien rigoureux du matériel.",
    "Pôle commercial et direction : tenue professionnelle exigée au QG et en rendez-vous.",
    "Congés (futurs contrats) : 2,2 jours ouvrables par mois de présence effective, conformément au code du travail ivoirien.",
])
pdf.titre1("2. Barème d'évaluation trimestrielle (sur 100 points)")
pdf.puces([
    "Objectifs quantitatifs (40 pts) : CA généré (commercial), délais respectés (technique), rigueur budgétaire (direction).",
    "Qualité et satisfaction (30 pts) : taux de SAV, retours clients, absence d'erreurs administratives.",
    "Comportement et esprit d'équipe (20 pts) : ponctualité, entraide, respect de la charte interne.",
    "Initiative et leadership (10 pts) : force de proposition, résolution de problèmes.",
])
pdf.titre1("3. Primes, sanctions et conséquences")
pdf.puces([
    "Score ≥ 85/100 : prime trimestrielle de 150 000 FCFA (cadres) / 50 000 FCFA (employés).",
    "Score de 50 à 84/100 : performance standard, maintien du poste sans prime.",
    "Score < 50/100 : avertissement écrit, plan d'amélioration sur 1 mois.",
    "Score < 30/100 (ou récidive < 50) : faute grave. Convocation pour licenciement avec indemnités minimales légales.",
])
pdf.ln(2)
pdf.para("Note de l'équipe : nous, soussignés, validons ce système et considérons la période actuelle comme une "
         "« période de grâce » pour l'ajuster. Le présent document servira de base au règlement intérieur officiel, "
         "déposable à l'Inspection du travail.", italique=True)

pdf.sauver(serveur("direction", "charte_et_evaluation_1907.pdf"))
