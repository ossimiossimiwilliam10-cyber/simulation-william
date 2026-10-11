"""Récapitulatif de Grace (23/07/2040) -> serveur/commercial/recap_grace_2307.pdf

Promis à William le 21/07 : objectifs sur la clinique de Marcory et la villa Riviera, calendrier,
marge plancher proposée. Une page, ton direct et chiffré.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Récapitulatif commercial : clinique de Marcory et villa Riviera",
              "À valider ou corriger par William Ossimi")
pdf.meta("Date", "23/07/2040")
pdf.meta("Auteur", "Grace Adjoua-Mensah (directrice commerciale)")
pdf.meta("Destinataire", "William Ossimi")

pdf.titre1("1. Objectifs")
pdf.puces([
    "Clinique de Marcory (Dr Yapi) : visite technique avec Abdoul ce lundi 23/07 à 14h ; devis chiffré remis sous cinq jours "
    "ouvrés ; objectif : signer notre premier contrat B2B avant la fin août.",
    "Villa Riviera : devis comparatif prêt jeudi 26/07, établi sur la fiche d'onduleur de référence fournie par Abdoul "
    "(comparaison à armes égales avec les deux offres concurrentes).",
    "Autres pistes à relancer : école privée, hôtel, deux villas de Bingerville dont celle de M. Tanoh (propriétaire du QG). "
    "Objectif : trois devis envoyés d'ici le 10/08.",
])

pdf.titre1("2. Calendrier")
pdf.tableau(["Date", "Action", "Avec"], [
    ["Lun. 23/07, 14h", "Visite technique clinique de Marcory", "Abdoul, Dr Yapi"],
    ["Jeu. 26/07", "Devis comparatif villa Riviera", "Abdoul (fiche onduleur)"],
    ["Mar. 31/07", "Devis clinique et rapport complet d'organisation commerciale", "Abdoul, William"],
    ["Avant le 10/08", "Trois devis envoyés (école, hôtel, Bingerville)", "Yves (suivi SAV)"],
], [38, 96, 40])

pdf.titre1("3. Marge plancher proposée")
pdf.puces([
    "Clinique (premium) : marge brute plancher de 25 %.",
    "Villa Riviera (marché concurrentiel) : marge brute plancher de 20 %.",
    "Toute offre sous ces planchers vous est soumise avant envoi ; je ne négocie seule aucune remise supérieure à 5 %.",
    "La marge nette est notée dans la matrice (20 points) : je ne brade pas pour signer.",
])

pdf.titre1("4. Besoins")
pdf.puces([
    "Abdoul disponible pour deux relevés techniques d'ici le 31/07.",
    "Accès aux prix d'achat du fournisseur libanais pour chiffrer au plus juste.",
    "Votre validation des planchers sous 24 heures.",
])
pdf.para("Rappel : mon contrat exclut les marchés publics et toute commission ; je m'y tiendrai.", italique=True)

pdf.sauver(serveur("commercial", "recap_grace_2307.pdf"))
