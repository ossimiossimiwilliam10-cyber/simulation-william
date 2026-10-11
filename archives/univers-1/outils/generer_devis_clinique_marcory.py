"""Devis de la clinique de Marcory (Grace et Abdoul) -> serveur/commercial/devis_clinique_marcory_2707.pdf

Demandé par le Dr Yapi le 23/07 (visite technique) : devis en trois lignes (matériel, pose, garantie) + plan de maintenance, au plus tard
le vendredi 27/07 ; conseil d'administration de la clinique le mardi 31/07. Relevé d'Abdoul : « dix-huit à vingt-quatre, je dirais vingt-et-un ».
Plancher de marge validé par William : 25 % (récap de Grace du 23/07) ; marge interne ≈ 26 % (coût ≈ 15,8 M FCFA), non portée sur le devis.
Batteries lithium fer phosphate (recommandation du plan technique d'Abdoul du 26/07). Remis par Grace à Aïcha le 27/07 à 09h05
(jet « avant 09h30 » 50 % : OUI) ; validé par Aïcha après lecture (11h15) ; envoyé au Dr Yapi par Grace à 11h32.
Repères de prix 2025-2026 (Côte d'Ivoire, Sénégal) projetés en 2040 (+35 %) ; PV ≈ 300 FCFA/Wc, LFP ≈ 175 000 FCFA/kWh au prix d'achat.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Devis — continuité électrique solaire",
              "OSIA Énergies — Clinique de Marcory — référence CM-01 — 27/07/2040 — validité 30 jours")
pdf.meta("Client", "Clinique de Marcory, à l'attention du Dr Yapi, directeur")
pdf.meta("Interlocuteurs", "Grace Adjoua-Mensah (commerciale), Abdoul Karim Touré (technique)")
pdf.meta("Objet", "Continuité de l'alimentation des deux blocs opératoires et du local des réfrigérateurs à vaccins pendant les coupures, "
                  "avec relais du groupe électrogène existant")

pdf.titre1("Solution proposée (relevé du 23/07/2040)")
pdf.puces([
    "Champ photovoltaïque de 16 kWc en toiture.",
    "Deux onduleurs hybrides de 10 kW en parallèle.",
    "Stockage de 30 kWh en batteries lithium fer phosphate (sans entretien, nombreux cycles).",
    "Tableau de circuits prioritaires : blocs opératoires, froid des vaccins, éclairage de secours.",
    "Inverseur de source automatique avec le groupe électrogène existant : les circuits prioritaires restent alimentés pendant le démarrage du groupe.",
])

pdf.titre1("Prix")
pdf.tableau(["Ligne", "Contenu", "Prix hors taxes (FCFA)"], [
    ["1. Matériel", "Champ photovoltaïque, onduleurs, batteries, protections, tableau prioritaire, inverseur de source", "15 600 000"],
    ["2. Pose", "Pose, câblage, mise en service, essais, formation du personnel technique de la clinique", "3 900 000"],
    ["3. Garantie", "Extension à cinq ans, pièces et main-d'œuvre", "1 900 000"],
    ["Total", "", "21 400 000"],
], (28, 104, 38))
pdf.para("TVA en sus selon le régime applicable au matériel solaire (exonération éventuelle à confirmer).")

pdf.titre1("Plan de maintenance (en option)")
pdf.puces([
    "Deux visites préventives par an, avec rapport écrit.",
    "Intervention sous 24 heures ouvrées sur les circuits prioritaires.",
    "Prix : 650 000 FCFA hors taxes par an.",
])

pdf.titre1("Conditions")
pdf.puces([
    "Paiement : 40 % à la commande, 50 % à la livraison du matériel, 10 % à la réception.",
    "Délai : quatre à six semaines après la commande, selon la disponibilité du matériel.",
    "Visite de confirmation avant la commande, sans frais.",
])
pdf.para("Grace Adjoua-Mensah — Abdoul Karim Touré — OSIA Énergies", italique=True)

pdf.sauver(serveur("commercial", "devis_clinique_marcory_2707.pdf"))
