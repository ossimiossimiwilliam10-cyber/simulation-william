"""
Génération des pièces du 9 et 10 août 2041 :
1. Courriel d'envoi officiel des 3 maquettes de gouvernance à Mohamed Coulibaly (09/08/2041)
2. Courriel de réponse et d'avis circonstancié de Mohamed Coulibaly (10/08/2041)
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_envoi_maquettes():
    pdf = DocPDF(
        "PROJET SOLAIRE B2B CÔTE D'IVOIRE — Direction Générale & Associé Unique",
        "Transmission Officielle des 3 Maquettes de Gouvernance et Cadrage Organisationnel",
        auteur="Direction Générale Virtuelle — Pour William Ossimi",
        pied="Transmission Maquettes de Gouvernance — 09/08/2041"
    )

    pdf.meta("De", "William Ossimi, Associé Unique Fondateur (via direction@projet-solaire.ci)")
    pdf.meta("À", "Monsieur Mohamed Coulibaly, Président-Directeur Général désigné (m.coulibaly@projet-solaire.ci)")
    pdf.meta("Date d'envoi", "Vendredi 9 août 2041, 16h45 (heure de Luxembourg) / 14h45 (heure d'Abidjan)")
    pdf.meta("Objet", "Transmission préparatoire : Maquettes de missions, contrôle interne et équipes opérationnelles")
    pdf.meta("Pièces jointes (3)", "1. Missions_Continues_Pôles.pdf ; 2. Dispositif_Contrôle_Anti_Détournement.pdf ; 3. Équipes_Opérationnelles_Niveaux_3_4.pdf")
    pdf.ln(3)

    pdf.titre1("Texte du message")
    pdf.para("Monsieur le Président-Directeur Général, cher Mohamed,")
    pdf.para(
        "À l'approche de mon arrivée à Abidjan pour la signature notariale et le lancement opérationnel de SOLEIL B2B "
        "CÔTE D'IVOIRE SASU, je vous transmets par la présente trois documents de cadrage stratégique et organisationnel "
        "afin de vous permettre d'en prendre connaissance avant notre première séance de travail en tête-à-tête :"
    )
    pdf.puces([
        "1. Maquette des missions continues et objectifs récurrents par pôle : définition des routines hebdomadaires de direction et des seuils quantitatifs minimaux ;",
        "2. Maquette du système de contrôle interne, conformité et sécurité financière : sanctuarisation du principe zéro espèces, double signature bancaire sur flux supérieurs à 10 millions FCFA, séparation stricte des fonctions et protection du secret d'affaires ;",
        "3. Maquette organisationnelle des équipes opérationnelles : dimensionnement agile des pôles, critères d'évaluation stricts (Niveau 3 >= 80/100, Niveau 4 juniors < 30 ans avec fort potentiel entre 75 et 85/100), et typologie des missions (continues, direction, spéciales)."
    ])
    pdf.para(
        "Concernant la Direction Générale, je souhaiterais recueillir votre appréciation sur l'opportunité d'une assistance "
        "de direction dédiée dès la phase d'amorçage ou son report en phase 2 de croissance."
    )
    pdf.para(
        "Si ces cadres organisationnels recueillent votre accord, vous pourrez d'ores et déjà engager les démarches de sourcing "
        "et de pré-sélection des équipes opérationnelles sur ces bases. J'attends votre retour avant mon départ."
    )
    pdf.ln(2)
    pdf.para("Bien cordialement,\n\n**William Ossimi**\nAssocié Unique Fondateur")

    cible = chemin("documents_william", "2041-08-09_Courriel_Mohamed_Coulibaly_Transmission_3_Maquettes_Gouvernance.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_courriel_reponse_coulibaly():
    pdf = DocPDF(
        "CABINET DE LA PRÉSIDENCE DE DIRECTION GÉNÉRALE — SOLEIL B2B CI",
        "Avis Favorable Circonstancié sur les 3 Maquettes et Recommandation d'Amorçage",
        auteur="Mohamed Coulibaly, Président-Directeur Général",
        pied="Réponse & Avis 3 Maquettes — Mohamed Coulibaly — 10/08/2041"
    )

    pdf.meta("De", "Mohamed Coulibaly, Président-Directeur Général désigné (m.coulibaly@projet-solaire.ci)")
    pdf.meta("À", "Monsieur William Ossimi, Associé Unique Fondateur (direction@projet-solaire.ci)")
    pdf.meta("Date de réception", "Samedi 10 août 2041, 11h18 (heure d'Abidjan) / 13h18 (heure de Luxembourg)")
    pdf.meta("Objet", "Re: Transmission préparatoire : Maquettes de missions, contrôle interne et équipes opérationnelles")
    pdf.ln(3)

    pdf.titre1("Texte du message")
    pdf.para("Monsieur l'Associé Unique, cher William,")
    pdf.para(
        "J'accuse bonne réception de votre courriel et des trois maquettes d'organisation transmises hier après-midi. "
        "Après une étude approfondie de ces documents au cours de la matinée, je vous confirme mon accord plein et entier "
        "sur l'ensemble des orientations proposées, qui témoignent d'une vision managériale d'une grande maturité :"
    )
    pdf.puces([
        "1. Contrôle interne et zéro espèces : Je souscris sans réserve à la dématérialisation intégrale des flux financiers et à la double signature électronique pour tout décaissement supérieur à dix millions de FCFA. Ce cadre protège l'entreprise autant qu'il sécurise ma propre responsabilité de mandataire social vis-à-vis des tiers ;",
        "2. Calibrage des équipes opérationnelles (Niveaux 3 et 4) : Les exigences de recrutement sont parfaitement équilibrées. Le seuil de 80/100 (avec 85 sur le métier) pour le chef de chantier technique garantit la sécurité industrielle. La priorité donnée aux jeunes de moins de 30 ans à fort potentiel (75-85/100) pour les postes d'installateurs et de commerciaux B2B permettra de constituer une équipe dynamique, adaptable et fidèle à la culture d'entreprise ;",
        "3. Pôle Finance : L'intégration d'un analyste quantitatif dédié à l'évaluation des contreparties industrielles et au suivi du burn rate sous l'autorité de Mariam Brou est une excellente initiative qui renforcera notre crédibilité auprès des bailleurs de fonds ;",
        "4. Assistance de Direction Générale : En réponse directe à votre interrogation, je préconise très nettement de reporter ce recrutement à la Phase 2. Durant la phase d'amorçage, mon assistanat direct alourdirait les charges fixes sans justification de volume. Mariam Brou et moi-même absorberons aisément les formalités de gestion courante, avec l'appui des services du centre d'affaires."
    ])
    pdf.para(
        "Sur ces bases désormais arrêtées, je prépare le cadrage des fiches de poste pour engager le sourcing dès la semaine "
        "prochaine. Je me réjouis de vous accueillir à Abidjan ce mardi 13 août pour la signature solennelle chez Maître Gnamien "
        "et notre déjeuner de cadrage."
    )
    pdf.ln(2)
    pdf.para("Très respectueusement,\n\n**Mohamed Coulibaly**\nPrésident-Directeur Général désigné")

    cible = chemin("courriels", "2041-08-10_Courriel_Mohamed_Coulibaly_Accuse_et_Avis_3_Maquettes_Gouvernance.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_courriel_envoi_maquettes()
    generer_courriel_reponse_coulibaly()