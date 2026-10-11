"""Synthèse des équipes par pôle (DRH, 18/07/2040) -> serveur/rh/synthese_equipe_1807.pdf

Version corrigée le 21/07/2040 : accents rétablis, salaires en BRUT (comme dans
osia/equipe.md), colonnes début/fin de contrat demandées par William le 18/07.
Version corrigée le 26/07/2040 (corrections n° 34) : CDI avec période d'essai (avant : CDD de 24 mois).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Synthèse des équipes par pôle", "OSIA Énergies — document à mettre à jour à chaque évolution",
              orientation="L")
pdf.meta("Date", "18/07/2040")
pdf.meta("Auteur", "Mariette Kouadio (DRH)")
pdf.meta("Destinataire", "William Ossimi (Gérant)")
pdf.ln(4)

entetes = ["Pôle", "Nom", "Poste", "Salaire brut mensuel (FCFA)", "Contrat (début)", "Fin de l'essai", "Évaluation"]
lignes = [
    ["Direction", "Aïcha Diomandé", "Directrice générale (gérante par procuration)", "750 000", "CDI (22/05/2040)", "21/11/2040", ""],
    ["Direction", "Mariette Kouadio", "DRH", "650 000 (+ 10 000 de forfait internet)", "CDI (01/06/2040)", "30/11/2040", ""],
    ["Commercial", "Grace Adjoua-Mensah", "Directrice commerciale", "850 000 + 2 % du CA + bonus trimestriel", "CDI (16/07/2040)", "15/01/2041", ""],
    ["Technique", "Abdoul Karim Touré", "Directeur technique", "900 000", "CDI (16/07/2040)", "15/01/2041", ""],
    ["Technique", "Yves Kanga", "Responsable SAV / relation client", "600 000", "CDI (16/07/2040)", "15/10/2040", ""],
    ["Conformité", "Esther N'Guessan", "Conformité et risques", "1 000 000", "CDI (01/09/2040*)", "28/02/2041*", ""],
]
pdf.tableau(entetes, lignes, [26, 42, 50, 55, 26, 26, 36])

pdf.para("* Prévisionnel : arrivée d'Esther N'Guessan fin août ou en septembre, selon la fin de son préavis "
         "bancaire de trois mois. Essai : six mois pour les cadres supérieurs, trois mois pour Yves (cadre), renouvelable une fois par écrit.", italique=True)
pdf.para("Note de la DRH : ce tableau ne comprend pour l'instant que les cadres de l'équipe de direction. "
         "Les recrutements des sous-équipes (techniciens SAV, ouvriers poseurs) sont en cours de "
         "budgétisation par les responsables respectifs (livrables attendus pour le 31/07/2040). "
         "La colonne « Évaluation » reste vide jusqu'à la première évaluation trimestrielle.", italique=True)

pdf.sauver(serveur("rh", "synthese_equipe_1807.pdf"))
