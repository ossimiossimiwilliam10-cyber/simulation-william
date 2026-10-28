"""
Génération du Rapport quotidien n° 18 du Directeur Général virtuel
Mardi 6 août 2041 — Tour n° 70
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from pdf_base import DocPDF

def chemin(*parties):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, *parties)


def generer_rapport_quotidien_18():
    pdf = DocPDF(
        "Rapport Quotidien du Directeur Général Virtuel (n° 18)",
        "Gouvernance SASU et conformité article 14 — Mardi 6 août 2041",
        auteur="Directeur Général virtuel",
        pied="Rapport n° 18 — Opérations Côte d'Ivoire & Luxembourg — 06/08/2041"
    )

    pdf.meta("Période", "Mardi 6 août 2041, 00h00 – 20h00")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Statut global", "Nominal — Analyse de gouvernance statutaire — Mission Abidjan J-6")
    pdf.ln(3)

    pdf.titre1("1. Pôle Juridique : Analyse de la gouvernance et de l'article 14")
    pdf.para(
        "À la suite de la demande de réexamen de la gouvernance, le pôle juridique virtuel a conduit une "
        "analyse croisée entre le droit des sociétés OHADA (AUSCGIE) et l'article 14 du statut des "
        "fonctionnaires de l'État luxembourgeois."
    )
    pdf.puces([
        "Risque identifié : En droit OHADA (art. 853-1 de l'AUSCGIE), le « Président » est légalement investi "
        "des pouvoirs de représentation et d'engagement de la société vis-à-vis des tiers. Si William assume "
        "le titre de Président dans les statuts, l'administration luxembourgeoise (MENJE) est susceptible de "
        "considérer qu'il s'agit d'un mandat de direction ou d'administration exécutive, en contradiction formelle "
        "avec les restrictions de l'article 14 ;",
        "Principe de conformité : L'article 14 admet sans restriction la détention patrimoniale passive de titres "
        "sociaux (associé non-gérant / actionnaire unique) sans fonction d'administration ou de gestion courante ;",
        "Recommandation opérationnelle : Ajuster la rédaction des statuts définitifs chez Maître Gnamien pour la signature "
        "du 13 août : attribuer le mandat social de Président (ou Président-Directeur Général) à Mohamed Coulibaly, "
        "tandis que William conserve la qualité exclusive d'Associé Unique Fondateur ;",
        "Maintien du contrôle souverain : En qualité d'Associé Unique, William conserve statutairement l'intégralité "
        "du pouvoir décisionnel : approbation des comptes, affectation des résultats, nomination/révocation des dirigeants, "
        "et droit de veto préalable obligatoire pour tout engagement supérieur à 10 000 000 FCFA."
    ])

    pdf.titre1("2. Pôle Ressources Humaines & Recrutement")
    pdf.puces([
        "Direction Commerciale (DC) : Mohamed Coulibaly poursuit ses prospections à Abidjan via son réseau "
        "professionnel et un cabinet de chasse local. Aucun profil n'ayant franchi le seuil d'exigence (note > 80/100) "
        "n'a été soumis ce jour ;",
        "Direction Technique (DT) : Éric Koffi Yao confirme ses disponibilités pour les réunions de cadrage et "
        "visites techniques de toitures du 13 au 25 août à Abidjan ;",
        "Direction Administrative et Financière (DAF) : Dossier de Mariam Brou en ordre pour finalisation "
        "lors de la mission d'août."
    ])

    pdf.titre1("3. Pôle Logistique & Mission Abidjan (J-6)")
    pdf.puces([
        "Vol Air France : Départ confirmé le lundi 12 août à 06h50 (Findel, vol AF1233 puis AF702 via Paris CDG) ;",
        "Formalités et hébergement : Attestation e-visa biométrique SNEDAI, carnet vaccinal et réservation à "
        "Cocody Deux-Plateaux entièrement vérifiés ;",
        "Signature notariale : Séance confirmée le mardi 13 août à 10h00 au Cabinet de Maître Gnamien au Plateau."
    ])

    pdf.titre1("4. Pôle Finances & Gestion personnelle")
    pdf.puces([
        "Compte courant Spuerkeess : 10 098,59 EUR au 06/08/2041 ;",
        "Échéance imminente : Débit automatique du solde de la carte Visa Premier (1 358,00 EUR) programmé "
        "pour demain mercredi 7 août à 06h00 (relevé arrêté au 30/07/2041) ;",
        "Trésorerie prévisionnelle après débit carte : 8 740,59 EUR sur le compte courant ;",
        "Comptes d'épargne : Livret projet à 75 982,00 EUR ; portefeuille ETF Monde à 676 135,00 EUR."
    ])

    pdf.titre1("5. Surveillance des risques et consommation API")
    pdf.para(
        "Consommation API du jour : 0,35 EUR (analyse juridique et rapport quotidien n° 18). "
        "Cumul mensuel août 2041 : 1,75 EUR sur plafond autorisé de 50,00 EUR. "
        "Aucune anomalie ni incident de sécurité à signaler."
    )

    cible = chemin("documents_william", "2041-08-06_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_rapport_quotidien_18()

