"""
Génération de la Grille d'Évaluation Stratégique pour la Direction Commerciale
Jeudi 15 août 2041 — Tour n° 88
Préparée par le Pôle Commercial & RH Virtuel pour William Ossimi et Mohamed Coulibaly
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_grille_evaluation_dc():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Pôle RH & Commercial Virtuel",
        "Grille d'Évaluation Stratégique & Grille d'Arbitrage : Direction Commerciale",
        auteur="Pôle RH & Commercial Virtuel — Application Gestion",
        pied="Grille d'Évaluation Direction Commerciale — SOLEIL B2B CI — 15/08/2041"
    )

    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Copie pour arbitrage", "Monsieur Mohamed Coulibaly, Directeur Général")
    pdf.meta("Rédacteur", "Pôle RH & Commercial Virtuel — Application Gestion")
    pdf.meta("Date d'établissement", "Jeudi 15 août 2041, 09h00 (heure d'Abidjan)")
    pdf.meta("Objet", "Cadre d'évaluation et critères d'arbitrage pour les candidatures de Marc-Antoine Kouadio et Viviane Tanoh (dossiers attendus vendredi 16/08 à 12h00)")
    pdf.ln(3)

    pdf.titre1("1. Contexte du recrutement et doctrine de sélection (Seuil > 80/100)")
    pdf.para(
        "Dans le cadre de la constitution de l'équipe de direction de SOLEIL B2B CÔTE D'IVOIRE, la Direction Commerciale "
        "constitue le moteur de génération du chiffre d'affaires et de sécurisation du carnet de commandes. Conformément aux directives "
        "de l'Associé Unique et aux recommandations du Directeur Général, la doctrine de recrutement impose un score éliminatoire "
        "strict supérieur ou égal à 80/100, avec une exigence minimale de 85/100 sur le cœur de compétence commerciale."
    )
    pdf.para(
        "Les deux candidats présélectionnés lors des entretiens préliminaires sont convoqués pour remettre leur dossier complet et "
        "leur proposition stratégique vendredi 16 août à 12h00 : Monsieur Marc-Antoine Kouadio (ingénieur d'affaires grands comptes énergie) "
        "et Madame Viviane Tanoh (directrice des ventes B2B distribution industrielle)."
    )

    pdf.titre1("2. Les 5 Questions Clés d'Arbitrage Stratégique")
    pdf.para(
        "Pour structurer l'analyse comparative des deux dossiers et guider la décision finale de l'Associé Unique et du Directeur Général, "
        "cinq questions déterminantes ont été formalisées par le pôle d'intelligence commerciale :"
    )

    entetes_questions = ["Axe d'évaluation", "Question clé posée aux candidats", "Livrable attendu dans le dossier", "Pondération"]
    lignes_questions = [
        [
            "1. Accès au Portefeuille Clients",
            "Quelle est la cartographie exacte de vos 15 premiers contacts décideurs (Directeurs d'usines, DG de PME) activables sous 30 jours à Vridi et Yopougon ?",
            "Liste anonymisée avec secteur, puissance souscrite estimée et historique relationnel.",
            "25 %"
        ],
        [
            "2. Offre Anti-Délestage CIE",
            "Face aux micro-coupures récurrentes signalées par les industriels, comment articulez-vous l'argumentaire de vente d'un système hybride solaire + stockage ?",
            "Simulateur de ROI / temps d'amortissement comparé aux coûts de carburant des groupes électrogènes.",
            "25 %"
        ],
        [
            "3. Vélocité du Cycle de Vente",
            "Quel est votre plan d'action opérationnel pour ramener le cycle de vente moyen d'une installation solaire B2B de 6 mois à moins de 60 jours ?",
            "Processus en 4 étapes : qualification, audit technique préliminaire, offre ferme, closing bancaire.",
            "20 %"
        ],
        [
            "4. Management Équipe Terrain",
            "Comment comptez-vous encadrer, coacher et objectiver les technico-commerciaux de Niveau 3 et les prospecteurs juniors de Niveau 4 ?",
            "Grille de KPI hebdomadaires, plan d'intéressement à la marge brute et gestion de la discipline.",
            "15 %"
        ],
        [
            "5. Conformité & Zéro Bakchich",
            "Dans un environnement concurrentiel où l'intermédiation informelle est fréquente, quelle est votre méthode pour remporter des contrats en stricte conformité ?",
            "Engagement écrit de conformité éthique, audit de transparence et refus formel de rétro-commissions.",
            "15 %"
        ],
    ]
    pdf.tableau(entetes_questions, lignes_questions, [40, 65, 60, 25])

    pdf.ln(3)
    pdf.titre1("3. Calendrier d'Arbitrage et Modalités de Décision")
    pdf.para(
        "Le déroulement de la séquence de décision est programmé comme suit :\n"
        "• Vendredi 16 août, 12h00 : Réception formelle des dossiers et notes d'orientations stratégiques des deux candidats.\n"
        "• Vendredi 16 août, 12h00-13h30 : Dépouillement, scoring indépendant par le pôle RH virtuel et analyse financière du plan de vente.\n"
        "• Vendredi 16 août, 14h00 : Point d'arbitrage conjoint entre William Ossimi et Mohamed Coulibaly pour désignation du titulaire.\n"
        "• Lundi 19 août : Notification de sélection officielle et contractualisation sous contrat de travail de direction Niveau 2."
    )

    sortie = chemin("documents_william", "2041-08-15_Grille_Evaluation_Direction_Commerciale.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_grille_evaluation_dc()
