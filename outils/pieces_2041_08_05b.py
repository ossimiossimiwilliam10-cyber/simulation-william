"""
Génération du Rapport quotidien n° 17 du Directeur Général virtuel
Lundi 5 août 2041 — Tour n° 69
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from pdf_base import DocPDF

def chemin(*parties):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, *parties)


def generer_rapport_quotidien_17():
    pdf = DocPDF(
        "Rapport Quotidien du Directeur Général Virtuel (n° 17)",
        "Semaine W32 : ouverture et agenda de la dernière semaine avant mission — Lundi 5 août 2041",
        auteur="Directeur Général virtuel",
        pied="Rapport n° 17 — Opérations Côte d'Ivoire & Luxembourg — 05/08/2041"
    )

    pdf.meta("Période", "Lundi 5 août 2041, 06h00 – 20h00")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Président Fondateur")
    pdf.meta("Statut global", "Nominal — Mission Abidjan J-7 — Dernière séance MCC effectuée")
    pdf.ln(3)

    pdf.titre1("1. Pôle Ressources Humaines & Recrutement")
    pdf.puces([
        "Direction Technique (Éric Koffi Yao, 84/100) : Contrat cadre Niveau 2 à 1 600 000 FCFA net/mois"
        " en cours de finalisation par Mohamed Coulibaly. Présence confirmée à Abidjan du 13 au 25 août "
        "pour les réunions de cadrage et visites de toitures industrielles ;",
        "Direction Commerciale : Sourcing actif relancé via le réseau professionnel de Mohamed Coulibaly"
        " et le cabinet de chasse spécialisé abidjanais. Aucun nouveau profil reçu à ce stade ; "
        "exigence maintenue : note > 80/100 avant toute transmission à la Présidence ;",
        "Direction Administrative et Financière (Mariam Brou) : Dossier stabilisé. Confirmation de poste"
        " et signature du contrat liées à la séance notariale du mardi 13 août à 10h00 au Plateau."
    ])

    pdf.titre1("2. Pôle Logistique & Mission Abidjan (J-7)")
    pdf.puces([
        "Vol Air France : Départ Luxembourg-Findel le lundi 12 août 2041 à 06h50 (AF1233 LUX→CDG),"
        " correspondance CDG→ABJ AF702 à 10h30, arrivée FHB prévue 18h10 heure locale ;",
        "Formalités d'entrée : Attestation SNEDAI e-visa biométrique (réf. CI-2041-88419B) vérifiée,"
        " QR Code imprimé à conserver en format physique ;",
        "Hébergement : Résidence hôtelière sécurisée Cocody Deux-Plateaux confirmée, groupe électrogène"
        " permanent, check-in prévu lundi 12 août en soirée ;",
        "Agenda Abidjan (13-25 août) : Séance de signature notariale Cabinet Gnamien (13/08, 10h00),"
        " réunions de cadrage DT (14-15/08), premières visites terrain, points DG quotidiens."
    ])

    pdf.titre1("3. Pôle Finances & Comptabilité")
    pdf.puces([
        "Compte courant Spuerkeess : 10 098,59 EUR au 05/08/2041 après exécution des prélèvements"
        " du 5 du mois (PR1 : 949,28 EUR ; assurance habitation : 45,00 EUR ; assurance véhicule : 107,00 EUR) ;",
        "Échéances imminentes : Débit Visa Premier 1 358,00 EUR le 07/08 (relevé clos au 30/07) ;"
        " électricité 132,00 EUR et gaz 253,00 EUR le 12/08 ;",
        "Trésorerie disponible après Visa Premier (estimation au 08/08) : 8 740,59 EUR ;"
        " réserve mission Abidjan provisionnée sur compte courant ;",
        "Livret épargne projet : 75 982,00 EUR (stable) ; ETF Monde : 676 135,00 EUR (valeur de marché)."
    ])

    pdf.titre1("4. Pôle Juridique & Conformité")
    pdf.puces([
        "Cabinet Maître Ismaël Niamien : Documents de constitution SASU et convention de mandat DG"
        " transmis et validés. Séance de signature planifiée le mardi 13 août à 10h00 au Plateau, Abidjan ;",
        "Ministère de l'Éducation Nationale Luxembourg (MENJE) : Note formelle et dossier en 4 points"
        " préparés par le pôle juridique virtuel pour transmission à la rentrée de septembre ;",
        "Conformité article 14 du statut des fonctionnaires luxembourgeois : Structure SASU retenue"
        " (rôle d'associé non-gérant pour William) ; aucun conflit d'intérêts identifié."
    ])

    pdf.titre1("5. Surveillance des risques & sécurité opérationnelle")
    pdf.puces([
        "Contrôles dominicaux (04/08) : Aucun signalement de fuite externe ni d'escalade administrative"
        " (T4 et T5 négatifs) ; intégrité du secret absolu sur l'automatisation du segment virtuel préservée ;",
        "Affaires ouvertes : Projet CI — annonce : 13 personnes informées hors William (fuite interne 39 %,"
        " externe 13 %) ; Projet CI — article 14 : 1 personne informée (fuite interne 3 %, externe 1 %).",
        "Aucun incident sécurité ni signalement dans les 24 dernières heures."
    ])

    pdf.titre1("6. Consommation API du segment virtuel")
    pdf.para(
        "Consommation API du jour : 0,40 EUR (synthèse hebdomadaire, mise à jour des pôles et "
        "préparation du rapport n° 17). Cumul mensuel août 2041 : 1,40 EUR sur plafond autorisé de 50,00 EUR."
    )

    cible = chemin("documents_william", "2041-08-05_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_rapport_quotidien_17()
