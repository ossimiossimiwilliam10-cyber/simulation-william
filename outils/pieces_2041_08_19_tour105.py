"""
Génération des pièces officielles du lundi 19 août 2041, 09h00 (Tour n° 105) :
1. Courriel officiel de Mohamed Coulibaly : Notification de lancement de la consultation des entreprises pour les travaux d'aménagement du QG des Vallons
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_lancement_amenagement():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE",
        "Courriel : Lancement de la Consultation Aménagement Siège Vallons",
        auteur="Monsieur Mohamed Coulibaly, Directeur Général",
        pied="Consultation Travaux QG Vallons — SOLEIL B2B CI — 19/08/2041"
    )

    pdf.meta("De", "Mohamed Coulibaly, Directeur Général (dg@soleil-b2b.ci)")
    pdf.meta("À", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Lundi 19 août 2041, 08h15 (heure d'Abidjan)")
    pdf.meta("Objet", "Notification d'envoi des DCE — Travaux de réhabilitation et aménagement du siège des Deux-Plateaux Vallons")
    pdf.ln(3)

    pdf.titre1("1. Envoi formel des dossiers de consultation des entreprises (DCE)")
    pdf.para(
        "Monsieur le Président et Associé Unique,"
    )
    pdf.para(
        "Conformément à nos arbitrages et suite à la validation de la grille d'agencement spatial intervenue ce week-end, "
        "j'ai le plaisir de vous notifier que les dossiers de consultation technique ont été formellement transmis ce matin à 08h00 "
        "aux trois entreprises générales de second œuvre sélectionnées pour leur fiabilité et leurs références professionnelles à Abidjan :"
    )
    pdf.para(
        "- BTP & Climatisation Ivoire (Cocody / Plateau)\n"
        "- Bâtir Pro CI (Deux-Plateaux Vallons)\n"
        "- Ivoire Réseaux & Énergie (Marcory Zone 4)"
    )

    pdf.titre1("2. Périmètre des 4 lots soumis à adjudication")
    pdf.para(
        "La consultation est articulée autour des quatre lots techniques prioritaires définis dans notre rapport d'inspection :"
    )
    pdf.para(
        "1. Lot Climatisation : Installation de 6 climatiseurs muraux Inverter basse consommation (bureaux individuels et réfectoire) "
        "et d'une console plafonnière 24 000 BTU pour la salle de réunion et de conseil."
    )
    pdf.para(
        "2. Lot Réseau & Courants Faibles : Déploiement d'un câblage blindé RJ45 Catégorie 6A (2 prises par poste de travail), "
        "installation d'une baie de brassage sécurisée 24 ports dans la réserve informatique, raccordement fibre optique et double onduleur centralisé."
    )
    pdf.para(
        "3. Lot Cloisonnement & Menuiserie : Pose de cloisons amovibles semi-vitrées acoustiques pour isoler les bureaux de direction "
        "(Technique / Yao, Commercial / Tanoh, DAF / Brou) et sécurisation du bureau réservé à l'Associé Unique."
    )
    pdf.para(
        "4. Lot Énergie de Secours & Sécurité : Révision intégrale, vidange et tests en charge du groupe électrogène 45 kVA existant, "
        "remplacement de la batterie de démarrage 12V et pose d'un inverseur de source automatique triphasé normal/secours."
    )

    pdf.titre1("3. Calendrier d'exécution et sourcing opérationnel")
    pdf.para(
        "- Remise des offres chiffrées : Mercredi 21 août 2041 à 16h00 au plus tard.\n"
        "- Dépouillement et choix du titulaire : Jeudi 22 août 2041.\n"
        "- Démarrage des travaux sur site : Vendredi 23 août 2041, pour une livraison clé en main le samedi 31 août 2041."
    )
    pdf.para(
        "En parallèle, Madame Viviane Tanoh et Monsieur Éric Koffi Yao ont démarré ce matin les démarches d'approche discrète "
        "pour le vivier de techniciens et de commerciaux juniors (Niveaux 3 et 4) conformément au barème d'exigence validé."
    )
    pdf.para(
        "Je vous tiendrai informé de tout retour significatif et reste à votre écoute pour vos orientations hebdomadaires."
    )
    pdf.para(
        "Bien respectueusement,\n"
        "Mohamed Coulibaly\n"
        "Directeur Général, SOLEIL B2B CÔTE D'IVOIRE"
    )

    sortie = chemin("courriels", "2041-08-19_Courriel_Mohamed_Coulibaly_Lancement_Appel_Offres_Amenagement_QG_Vallons.pdf")
    pdf.sauver(sortie)
    print(f"Généré : {sortie}")


if __name__ == "__main__":
    generer_courriel_lancement_amenagement()

