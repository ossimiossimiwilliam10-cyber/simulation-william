"""Rapport de prospection (Grace, 18/07/2040) -> serveur/commercial/rapport_prospects_1807.pdf

Contenu inchangé (version avec accents remise à William le 18/07 à 17h45). Seul le moteur a changé.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de prospection commerciale")
pdf.meta("Date", "18/07/2040")
pdf.meta("Auteur", "Grace Adjoua-Mensah (directrice commerciale)")

pdf.titre1("1. Clinique privée (Marcory)")
pdf.puces([
    "Besoin identifié : sécurisation des blocs opératoires et des réfrigérateurs à vaccins contre les délestages et micro-coupures.",
    "Budget estimé : élevé. Le client recherche une solution premium et hautement fiable.",
    "Statut actuel : prospect chaud.",
    "Prochaine étape : le directeur de la clinique attend une visite de notre directeur technique (Abdoul) "
    "pour un relevé de puissance et l'établissement d'un devis précis.",
])
pdf.titre1("2. Grande villa (Riviera)")
pdf.puces([
    "Besoin identifié : autonomie totale hors réseau électrique national (le client est excédé par les coupures répétitives).",
    "Budget estimé : à définir lors de l'étude technique, mais capacité financière importante.",
    "Statut actuel : prospect tiède.",
    "Prochaine étape : le client dispose déjà de deux autres devis concurrents. Nous devons proposer une offre "
    "très agressive sur les garanties et le service après-vente (SAV) pour remporter le marché.",
])
pdf.ln(2)
pdf.para("Conclusion : je recommande une intervention rapide d'Abdoul sur la clinique de Marcory. "
         "C'est une belle opportunité pour signer notre premier gros contrat B2B.", italique=True)

pdf.sauver(serveur("commercial", "rapport_prospects_1807.pdf"))
