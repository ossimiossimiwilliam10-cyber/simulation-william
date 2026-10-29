"""
Génération des pièces officielles du dimanche 18 août 2041, 16h30 (Tour n° 103) :
1. Compte-rendu d'enquête de terrain et analyse économique : Réalité de la facturation CIE, délestages et étude d'opportunité micro-retail / B2C à Abidjan
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_compte_rendu_enquete_terrain():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Enquête de Terrain : Facturation CIE, Délestages & Analyse du Segment Micro-Retail",
        auteur="Monsieur William Ossimi, Associé Unique Fondateur",
        pied="Étude Terrain Micro-Retail & Réseau CIE — SOLEIL B2B CI — 18/08/2041"
    )

    pdf.meta("Auteur de l'observation", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Date de l'immersion", "Dimanche 18 août 2041 (09h30 - 15h30)")
    pdf.meta("Périmètre géographique", "Abidjan : Cocody Deux-Plateaux, Village urbain d'Anono, Boulevard des Martyrs / Vallons")
    pdf.meta("Objet", "Sondage qualitatif exploratoire sur la gestion de l'électricité, les délestages et l'appétence au solaire")
    pdf.ln(3)

    pdf.titre1("1. Démarche exploratoire et protocole d'observation")
    pdf.para(
        "Dans le cadre de l'évaluation globale du marché énergétique ivoirien, une immersion de terrain a été menée ce dimanche 18 août "
        "à travers plusieurs quartiers représentatifs d'Abidjan. L'objectif consistait à confronter les hypothèses théoriques de marché "
        "à la réalité économique vécue par les petits commerçants de proximité (épiceries, maquis, artisans) et les résidents urbains."
    )
    pdf.para(
        "L'approche a été conduite sous un angle d'observation discret et informel, afin de capter des réactions authentiques et non biaisées "
        "face aux contraintes d'approvisionnement de la Compagnie Ivoirienne d'Électricité (CIE) et à l'alternative solaire."
    )

    pdf.titre1("2. Données qualitatives et réactions de terrain")
    pdf.para(
        "A. Commerce de proximité / Alimentation générale (Deux-Plateaux) :\n"
        "- Gestion énergétique : Utilisation prédominante de compteurs à prépaiement, générant une dépense mensuelle de 35 000 à 45 000 FCFA "
        "pour faire tourner deux vitrines réfrigérées et l'éclairage de base.\n"
        "- Réaction et posture (Wilfried Yéo, 49 ans) : Méfiance immédiate et recul face aux questions relatives aux factures et aux raccordements. "
        "Peur viscérale d'un contrôle inopiné de la CIE ou d'une inspection fiscale déguisée. Volonté d'indépendance, mais rejet catégorique "
        "de toute contractualisation rigide ou de tout engagement financier pluriannuel."
    )
    pdf.para(
        "B. Restauration populaire et maquis (Village d'Anono) :\n"
        "- Impact critique des délestages (Safiatou Camara, 44 ans, gérante de maquis) : Facture CIE oscillant entre 85 000 et 110 000 FCFA/mois. "
        "Les coupures intempestives constituent une menace directe de faillite : perte de stocks périssables (viandes, poissons) et départ immédiat "
        "de la clientèle exigeant des boissons fraîches. Recours obligé à des petits groupes électrogènes à essence, extrêmement coûteux en carburant (3 000 à 5 000 FCFA par coupure) et bruyants.\n"
        "- Perception du solaire : Lucidité totale sur l'inadéquation des petits kits solaires d'entrée de gamme face aux compresseurs de froid industriel. "
        "Rejet explicite des offres tarifaires progressives ('tarifs d'appel' bas coût qui augmentent par la suite), perçues comme des pièges de surendettement."
    )
    pdf.para(
        "C. Habitat résidentiel et cours urbaines (Kader Bamba, 32 ans, Deux-Plateaux) :\n"
        "- Obstacles structurels : Prédominance du statut de locataire interdisant toute pose unilatérale de panneaux sur les toitures collectives sans accord des bailleurs.\n"
        "- Verrou réglementaire : Monopole légal de la CIE sur la distribution d'électricité et crainte de sanctions en cas de modifications d'installations perçues comme frauduleuses."
    )

    pdf.titre1("3. Enseignements stratégiques et confirmation du modèle B2B")
    pdf.para(
        "Les observations de terrain recueillies corroborent point par point la stratégie retenue pour SOLEIL B2B CÔTE D'IVOIRE :\n"
        "1. Impasse du segment Retail / B2C : Bien que le besoin d'autonomie soit criant face aux délestages, le recouvrement auprès des micro-acteurs "
        "informels présente un taux de sinistralité rédhibitoire (défaut de paiement prévisible > 40 % dès les premiers mois creux).\n"
        "2. Sanctuarisation de la cible Industrielle : Seules les moyennes et grandes entreprises (usines, entrepôts logistiques, cliniques, hypermarchés) "
        "disposent de la solvabilité, de toitures propriétaires solides et de flux de trésorerie bancarisés permettant la mise en place de cautions bancaires "
        "et de contrats PPA de 50 à 500 kWc rentables et sécurisés."
    )

    fichier = chemin("documents_william", "2041-08-18_Compte_Rendu_Enquete_Terrain_Micro_Commerces_et_Reseau_CIE.pdf")
    pdf.sauver(fichier)
    print(f"Généré : {fichier}")


if __name__ == "__main__":
    generer_compte_rendu_enquete_terrain()
