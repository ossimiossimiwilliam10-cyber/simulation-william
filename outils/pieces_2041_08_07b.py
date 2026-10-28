"""
Génération du courriel de Mohamed Coulibaly sur le seuil d'exigence (80/100)
Mercredi 7 août 2041 — Tour n° 72
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_coulibaly_seuil():
    pdf = DocPDF(
        "Messagerie Institutionnelle SOLEIL B2B CÔTE D'IVOIRE",
        "Courriel de Mohamed Coulibaly — Consultation sur le seuil de sélection de l'équipe de direction",
        auteur="Mohamed Coulibaly",
        pied="Courriel Mohamed Coulibaly — SOLEIL B2B CI — 07/08/2041"
    )

    pdf.meta("De", "Mohamed Coulibaly <m.coulibaly@soleilb2b.ci>")
    pdf.meta("À", "Direction Générale / Associé Unique <direction@soleilb2b.ci>")
    pdf.meta("Date et heure", "Mercredi 7 août 2041, 18h30 (heure d'Abidjan / 20h30 Luxembourg)")
    pdf.meta("Objet", "Avis stratégique : Évaluation du seuil d'exigence (80/100) pour l'équipe de direction")
    pdf.ln(3)

    pdf.titre1("Texte du courriel")
    pdf.para(
        "Monsieur Ossimi,\n\n"
        "J'accuse bonne réception de votre interrogation concernant le seuil de notation de 80 sur 100 actuellement "
        "fixé pour le recrutement de notre équipe de direction. C'est une question légitime et déterminante pour "
        "l'avenir de SOLEIL B2B."
    )
    pdf.para(
        "Permettez-moi de vous apporter mon retour d'expérience de banquier d'affaires et ma lecture du marché abidjanais :"
    )

    pdf.titre1("1. La réalité sélective du filtre 80/100")
    pdf.para(
        "Une note de 80/100 sur notre grille d'évaluation n'a rien d'un standard moyen. Notre grille est pondérée sur des "
        "critères particulièrement stricts : expérience démontrée sur le photovoltaïque en toiture, maîtrise contractuelle "
        "des modèles d'autoproduction, solidité du carnet d'adresses industriel et rigueur de gestion. "
        "Dans la pratique locale, un seuil à 80/100 élimine d'emblée plus de 80 % des candidatures. L'exemple récent de Stéphane "
        "Bamba (74/100), qui affichait pourtant une solide réputation dans les réseaux d'énergie conventionnelle, prouve que "
        "notre filtre actuel joue pleinement son rôle de rempart contre la complaisance et l'approximation."
    )

    pdf.titre1("2. Les contraintes d'un seuil relevé (85 ou 90/100)")
    pdf.para(
        "Relever le seuil général à 85 ou 90/100 présenterait deux obstacles majeurs pour notre phase de lancement :"
    )
    pdf.puces([
        "Raréfaction critique du vivier : Le solaire B2B industriel est une filière technique pointue en Côte d'Ivoire. Les profils à 85+ sont très rares et déjà installés à des postes d'associés dans des filiales de multinationales. Exiger 85+ sur la Direction Commerciale risque de paralyser nos prospections pendant six à neuf mois ;",
        "Pression salariale immédiate : Un candidat évalué à 85+ (comme Mariam Brou à 88 ou moi-même à 91) n'accepte pas la grille Niveau 2 fixée à 1 600 000 FCFA net. Il prétendra légitimement à des émoluments de Niveau 1 (plus de 2,5 à 3 millions FCFA net par mois), ce qui alourdirait sensiblement notre point mort avant le premier kilowatt raccordé."
    ])

    pdf.titre1("3. Ma préconisation pour bâtir une véritable équipe de champions")
    pdf.para(
        "Pour concilier l'ambition d'excellence et la réalité du terrain, je vous propose la doctrine suivante :"
    )
    pdf.puces([
        "Maintenir le plancher de 80/100 comme seuil éliminatoire absolu : aucun recrutement en dessous de 80, sans exception ni compromis de complaisance ;",
        "Instaurer une note éliminatoire sur le cœur de métier (85/100) : pour le Directeur Commercial, exiger au moins 85/100 spécifiquement sur le critère de closing des contrats PPA industriels, même si sa moyenne générale se situe entre 80 et 84 ;",
        "Valider le niveau d'élite à l'exécution : une équipe de champions ne se décrète pas uniquement sur dossier. C'est l'épreuve des trois mois d'essai et l'obligation d'atteindre les objectifs contractuels (les deux premiers contrats au 1er trimestre) qui validera définitivement le maintien de chaque directeur."
    ])
    pdf.para(
        "Je reste naturellement à votre disposition pour en échanger dès votre arrivée à Abidjan le 12 août.\n\n"
        "Bien à vous,\n\n"
        "Mohamed Coulibaly\n"
        "Président-Directeur Général désigné\n"
        "SOLEIL B2B CÔTE D'IVOIRE SASU"
    )

    cible = chemin("courriels", "2041-08-07_Courriel_Mohamed_Coulibaly_Avis_Seuil_Exigence_80_Recrutement_Elite.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_courriel_coulibaly_seuil()
