"""Devis comparatif de la villa Riviera (Grace) -> serveur/commercial/devis_villa_riviera_2607.pdf

Demandé par le propriétaire le 21/07 (comparaison avec une marque d'onduleur « qu'il connaît ») ; trame de Grace le 23/07 : 15 à 20 M FCFA,
plancher de marge 20 % ; remis à Aïcha le jeudi 26/07/2040 à 16h30 (jets : aujourd'hui 65 % OUI ; avant 16h 50 % NON).
Version client : les marges ne figurent pas dans le document (option A ≈ 21 %, option B ≈ 20 %, note interne transmise à Aïcha).
Repères de prix : villa consommant 150 000 FCFA/mois → hybride dès 8,5 M FCFA (2025) ; toit du QG 10 kWc + 20 kWh ≈ 9,8 M FCFA (2040).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Devis comparatif — installation solaire hybride",
              "OSIA Énergies — villa Riviera — référence VR-01 — 26/07/2040 — validité 30 jours")
pdf.meta("Client", "Propriétaire de la villa (Riviera, Cocody)")
pdf.meta("Interlocutrice", "Grace Adjoua-Mensah, directrice commerciale")
pdf.meta("Besoin", "Autonomie de la villa pendant les coupures et réduction de la facture CIE, groupe électrogène en secours")

pdf.titre1("Dimensionnement commun aux deux options")
pdf.puces(["Champ photovoltaïque de 15 kWc (panneaux monocristallins, structure aluminium en toiture).",
           "Onduleur hybride de 12 kW, couplage avec le réseau CIE et le groupe existant.",
           "Stockage de 30 kWh.",
           "Protections, câblage, mise à la terre, mise en service et formation du personnel de maison."])

pdf.titre1("Comparaison")
pdf.tableau(["", "Option A — gamme OSIA", "Option B — marque demandée par le client"], [
    ["Onduleur hybride 12 kW", "Gamme de notre fournisseur", "Marque demandée par le client"],
    ["Batteries 30 kWh", "Gel", "Lithium fer phosphate"],
    ["Garantie du matériel", "2 ans", "5 ans (onduleur), 10 ans (batteries)"],
    ["Garantie de pose", "1 an", "1 an"],
    ["Durée de vie attendue des batteries", "5 à 7 ans", "12 à 15 ans"],
    ["Prix hors taxes", "15 900 000 FCFA", "19 600 000 FCFA"],
], (50, 55, 65))
pdf.para("TVA en sus selon le régime applicable au matériel solaire (exonération éventuelle à confirmer).")

pdf.titre1("Conditions")
pdf.puces(["Paiement : 50 % à la commande, 40 % à la livraison du matériel, 10 % à la réception.",
           "Délai : trois à cinq semaines après la commande, selon la disponibilité du matériel.",
           "Visite technique de confirmation avant la commande, sans frais."])
pdf.para("Grace Adjoua-Mensah — OSIA Énergies", italique=True)

pdf.sauver(serveur("commercial", "devis_villa_riviera_2607.pdf"))
