"""Matrice d'évaluation détaillée v1.0 (Aïcha + Mariette, 20/07/2040) -> serveur/rh/matrice_evaluation.pdf

Version corrigée le 21/07/2040 : accents rétablis ; trou de barème comblé
(avant : « 86 à 94 » puis « > 95 » -> un score de 95 exact n'était couvert par aucune
règle ; maintenant : « 86 à 95 » puis « 96 et plus », conformément à « au-dessus de 95 »).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Matrice d'évaluation détaillée — OSIA Énergies",
              "Version 1.0 — rédigée par Aïcha Diomandé et Mariette Kouadio (20/07/2040)")

pdf.titre1("Barème commun (tronc commun — 30 points)")
pdf.para("1. Assiduité et ponctualité (10 pts)")
pdf.puces(["Aucun retard : 10 pts", "1 à 2 retards justifiés : 5 pts", "Retard non justifié ou absence : 0 pt"])
pdf.para("2. Respect des directives et de la hiérarchie (10 pts)")
pdf.puces(["Exécution immédiate et sans faille : 10 pts", "Exécution avec rappel : 5 pts",
           "Insubordination / refus : 0 pt (alerte licenciement)"])
pdf.para("3. Usage du serveur et traçabilité (10 pts)")
pdf.puces(["100 % des documents numérisés et classés sur le serveur : 10 pts", "Un oubli mineur : 5 pts",
           "Fichier perdu ou gardé en local : 0 pt"])

pdf.titre1("Critères spécifiques par pôle (70 points)")
poles = [
    ("Pôle commercial (Grace Adjoua-Mensah)", [
        "Acquisition client (30 pts) : atteinte de l'objectif mensuel de contrats signés.",
        "Qualité du pipeline (20 pts) : suivi CRM à jour, devis précis, relances effectuées.",
        "Marge nette (20 pts) : maintien d'une marge bénéficiaire élevée sans brader les prix."]),
    ("Pôle technique / installation (Abdoul Touré et Yves Kanga)", [
        "Qualité d'installation (30 pts) : aucun défaut technique, conformité électrique parfaite.",
        "Respect des délais (20 pts) : chantier terminé dans le temps imparti.",
        "Satisfaction client SAV (20 pts) : zéro plainte post-installation, interventions rapides."]),
    ("Pôle RH et administration (Mariette Kouadio)", [
        "Conformité juridique (30 pts) : aucune faille dans les contrats, respect du code du travail.",
        "Gestion de la paie (20 pts) : fiches de paie exactes, versées en temps et en heure.",
        "Climat social / discipline (20 pts) : maintien de la rigueur sans baisse de productivité."]),
    ("Direction / gestion (Aïcha Diomandé)", [
        "Rentabilité globale (30 pts) : suivi de la trésorerie et respect du budget.",
        "Coordination des pôles (20 pts) : fluidité de l'information entre commercial et technique.",
        "Reporting (20 pts) : transparence totale envers le Gérant (William)."]),
]
for titre, items in poles:
    pdf.para(titre)
    pdf.puces(items)

pdf.titre1("Règle de sanction et de promotion")
pdf.puces([
    "Moins de 30/100 : licenciement pour incompétence notoire + « naming and shaming » (signalement externe).",
    "De 30 à 60/100 : avertissement formel.",
    "De 61 à 85/100 : performance standard (maintien).",
    "De 86 à 95/100 : prime d'excellence de 150 000 FCFA.",
    "96/100 et plus (au-dessus de 95) : prime d'excellence + éligibilité immédiate à une promotion (directeur ou PDG).",
])
pdf.titre1("Ajustement discrétionnaire (bonus / malus)")
pdf.para("La Direction générale (W. Ossimi) se réserve le droit exclusif d'ajouter ou de retirer des points à tout employé.")

pdf.sauver(serveur("rh", "matrice_evaluation.pdf"))
