"""
Génération des pièces officielles du dimanche 18 août 2041, 21h30 (Tour n° 104) :
1. Courriel officiel de Mohamed Coulibaly : Réponse à l'enquête de terrain, cadrage de la vision prospective micro-retail à moyen/long terme et préparation du lancement des devis Vallons
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_reponse_coulibaly_micro_retail():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE",
        "Courriel : Retour sur Enquête Terrain & Prospective Micro-Retail",
        auteur="Monsieur Mohamed Coulibaly, Directeur Général",
        pied="Correspondance Direction Générale — SOLEIL B2B CI — 18/08/2041"
    )

    pdf.meta("De", "Mohamed Coulibaly, Directeur Général (dg@soleil-b2b.ci)")
    pdf.meta("À", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Dimanche 18 août 2041, 19h15 (heure d'Abidjan)")
    pdf.meta("Objet", "RE : Compte-rendu d'enquête terrain & Réflexion prospective segment micro-commerces")
    pdf.ln(3)

    pdf.titre1("1. Salutations et appréciation de la démarche de terrain")
    pdf.para(
        "Monsieur le Président et Associé Unique,"
    )
    pdf.para(
        "J'ai pris connaissance avec un vif intérêt du compte-rendu exhaustif de votre prospection dominicale dans les quartiers "
        "des Deux-Plateaux et d'Anono. Permettez-moi de saluer cette initiative personnelle : aller au contact direct des gérants "
        "d'alimentation générale et de maquis pour éprouver la réalité de leurs factures CIE et de leurs contraintes de délestage "
        "démontre une acuité managériale remarquable."
    )
    pdf.para(
        "Votre diagnostic recoupe trait pour trait la réalité sociologique et financière d'Abidjan : une appétence immense pour la continuité "
        "électrique, mais un risque de sinistralité et d'impayé rédhibitoire pour quiconque s'aventurerait aujourd'hui à financer "
        "ces acteurs informels sur ses fonds propres."
    )

    pdf.titre1("2. Orientations pour une solution optimale à moyen et long terme (Phase 2)")
    pdf.para(
        "Votre volonté de ne pas fermer la porte à ce marché gigantesque est visionnaire. Si nous parvenons à terme à craquer l'équation "
        "de solvabilité du micro-commerce, le potentiel de volume en Côte d'Ivoire et dans la sous-région se chiffrera en dizaines de milliers "
        "de points de vente. Comme vous le soulignez avec beaucoup de sagesse, il ne s'agit pas de chercher des miracles, mais d'élaborer "
        "une ingénierie rigoureuse. Voici les trois piliers qu'il conviendra de structurer le moment venu :"
    )
    pdf.para(
        "- Verrou technologique du prépaiement strict (PAYG) : Le modèle ne pourra reposer sur aucune facturation différée. "
        "Il exigera des onduleurs communicants de 1,5 à 3 kVA équipés de puces GSM et de relais de coupure à distance, activés exclusivement "
        "à la recharge quotidienne ou hebdomadaire par Mobile Money (Wave, Orange Money). Pas de paiement = coupure automatique instantanée."
    )
    pdf.para(
        "- Externalisation intégrale du risque de crédit : SOLEIL B2B CI ne doit pas jouer le rôle de banquier de l'informel. "
        "La solution pérenne consistera à nouer un partenariat stratégique avec des institutions de microfinance implantées (type Advans CI, "
        "Baobab CI ou COFINA). L'institution de microfinance portera le risque financier et le crédit-bail en s'appuyant sur des cautions solidaires "
        "(tontines, associations de commerçants), tandis que SOLEIL B2B CI interviendra comme équipementier exclusif, installateur certifié "
        "et mainteneur sous contrat de service récurrent."
    )
    pdf.para(
        "- Calendrier et sanctuarisation de la rentrée : Afin de ne pas disperser nos forces, je préconise de maintenir 100 % de nos ressources "
        "sur le lancement du B2B industriel et tertiaire (usines, entrepôts, cliniques) dès le 1er septembre avec Viviane Tanoh et Éric Yao. "
        "Une fois le runway sécurisé et les premiers flux de trésorerie encaissés, nous pourrons ouvrir au premier trimestre 2042 une cellule "
        "R&D et prospective pour modéliser cette offre micro-retail en toute sécurité."
    )

    pdf.titre1("3. Préparatifs opérationnels pour l'ouverture de la semaine (lundi 19 août)")
    pdf.para(
        "Pour information, les préparatifs pour le lancement des devis d'aménagement de la villa des Vallons sont finalisés. "
        "Dès demain matin à 08h00, le cahier des charges sera transmis aux trois entreprises générales retenues pour les lots climatisation, "
        "câblage réseau sécurisé, cloisons amovibles et révision générale du groupe électrogène 45 kVA. Les retours de devis sont calés "
        "pour mercredi 21 août en vue d'une attribution rapide."
    )
    pdf.para(
        "Je reste à votre entière disposition et vous souhaite une excellente fin de week-end."
    )
    pdf.para(
        "Bien respectueusement,\n"
        "Mohamed Coulibaly\n"
        "Directeur Général, SOLEIL B2B CÔTE D'IVOIRE"
    )

    sortie = chemin("courriels", "2041-08-18_Courriel_Mohamed_Coulibaly_Orientation_Prospective_Micro_Retail_et_Lancement_Devis_Vallons.pdf")
    pdf.sauver(sortie)
    print(f"Généré : {sortie}")


if __name__ == "__main__":
    generer_courriel_reponse_coulibaly_micro_retail()

