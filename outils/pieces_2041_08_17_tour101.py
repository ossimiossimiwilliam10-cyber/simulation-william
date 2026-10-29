"""
Génération des pièces officielles du samedi 17 août 2041, 18h30 (Tour n° 101) :
1. Note de cadrage de William Ossimi : Protocole officiel de reporting opérationnel quotidien, traitement automatisé et filtre d'escalade critique
2. Courriel officiel de Mohamed Coulibaly : Accusé de réception avec exécution à contre-coeur, mise en garde respectueuse sur la lourdeur bureaucratique et proposition d'un canevas standardisé par KPIs
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_note_protocole_reporting():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Directive de Gouvernance : Protocole de Reporting Journalier & Dispositif d'Alerte Critique",
        auteur="Monsieur William Ossimi, Associé Unique Fondateur",
        pied="Protocole Reporting & Escalade Critique — SOLEIL B2B CI — 17/08/2041"
    )

    pdf.meta("Émetteur", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur Mohamed Coulibaly, Directeur Général")
    pdf.meta("Date et heure", "Samedi 17 août 2041, 15h30 (heure d'Abidjan)")
    pdf.meta("Objet", "Mise en place de la doctrine de remontee d'information en regime de croisiere (rentree de septembre)")
    pdf.ln(3)

    pdf.titre1("1. Architecture du flux d'information journalier")
    pdf.para(
        "Dès l'entrée en fonction opérationnelle de l'ensemble du comité de direction et des équipes (Niveaux 2, 3 et 4) "
        "au 1er septembre 2041, la société appliquera une doctrine rigoureuse de traçabilité opérationnelle et d'évaluation continue :"
    )
    pdf.para(
        "- Remontée interne par pôle : Chaque directeur opérationnel (Direction Technique / Yao, Direction Commerciale / Tanoh, "
        "Direction Administrative et Financière / Brou) adressera en fin de journée ouvrée son compte-rendu d'activité détaillé au Directeur Général."
    )
    pdf.para(
        "- Consolidation par la Direction Générale : Mohamed Coulibaly consolidera ces éléments au sein d'un Rapport Journalier d'Exploitation "
        "exhaustif, ventilé par pôle, transmis chaque soir ouvrable à l'adresse électronique institutionnelle de la direction (direction@soleil-b2b.ci)."
    )

    pdf.titre1("2. Circuit d'analyse et régime de revue hebdomadaire")
    pdf.para(
        "- Rôle du segment d'analyse : L'ensemble des rapports journaliers reçus sera automatiquement intégré, recoupé et audité "
        "face aux flux bancaires et aux contrats par le pôle d'analyse interne."
    )
    pdf.para(
        "- Rythme de travail du Fondateur : Afin de préserver la hauteur de vue stratégique et d'éviter toute micro-gestion parasite, "
        "l'Associé Unique consacrera une session de travail hebdomadaire (le vendredi soir ou le week-end) à l'examen consolidé des rapports "
        "et adressera en retour ses orientations synthétiques au Directeur Général."
    )

    pdf.titre1("3. Dispositif d'escalade d'urgence (Alerte Rouge)")
    pdf.para(
        "Par dérogation expresse au rythme hebdomadaire, tout événement critique, alarmant ou présentant un risque juridique, "
        "financier ou technique majeur déclenchera une notification prioritaire immédiate à l'attention de William Ossimi :"
    )
    pdf.para(
        "1. Tout retard de paiement ou impayé client excédant quinze (15) jours calendaires."
    )
    pdf.para(
        "2. Tout incident technique sérieux sur une installation (défaut d'onduleur non résolu sous 24h, avarie toiture, rupture approvisionnement)."
    )
    pdf.para(
        "3. Toute anomalie comptable, écart de caisse, tentative de contournement des procédures ou conflit réglementaire avec une administration ivoirienne."
    )

    sortie = chemin("documents_william", "2041-08-17_Cadrage_Protocole_Reporting_Quotidien_et_Escalade_Critique.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


def generer_courriel_reponse_coulibaly_reporting():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Accusé de Réception sur le Reporting & Suggestions Opérationnelles",
        auteur="Mohamed Coulibaly",
        pied="Avis Reporting Journalier — SOLEIL B2B CI — 17/08/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly, Directeur Général (m.coulibaly@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Samedi 17 août 2041, 17h15 (heure d'Abidjan)")
    pdf.meta("Objet", "Accusé de réception des directives de reporting quotidien et observations de terrain")
    pdf.ln(3)

    pdf.titre1("1. Prise en compte scrupuleuse de vos instructions")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "J'accuse bonne réception de votre directive fixant le protocole de reporting journalier par pôle et le dispositif d'escalade critique. "
        "Soyez assuré que ces dispositions seront appliquées avec toute la rigueur et le sérieux que vous me connaissez dès la rentrée de septembre. "
        "Le mécanisme d'alerte rouge immédiate pour les impayés de plus de 15 jours ou les incidents critiques est une excellente mesure de gouvernance."
    )

    pdf.titre1("2. Observations respectueuses sur la charge administrative des équipes")
    pdf.para(
        "Permettez-moi toutefois, dans le cadre de ma mission de conseil et de préservation du climat de travail, de vous faire part "
        "d'une précaution bienveillante concernant le format quotidien. Dans le contexte abidjanais, nos directeurs technique et commercial "
        "(Éric Yao et Viviane Tanoh) passeront l'essentiel de leurs journées sur le terrain : toitures industrielles, chantiers, négociation "
        "avec les directions d'usines à Vridi et Yopougon, et embouteillages d'Abidjan. Rentrer au bureau à 18h30 pour rédiger un rapport littéraire "
        "exhaustif risque de peser lourdement sur leur moral et d'induire une lassitude bureaucratique rapide."
    )
    pdf.para(
        "Afin de concilier votre exigence absolue de contrôle et la productivité commerciale/technique des équipes, je me permets "
        "de vous proposer un compromis agile : nous formaliserons une matrice standardisée de 5 indicateurs clés par pôle (KPIs chiffrés : "
        "leads contactés, offres remises, chantiers audités, trésorerie disponible) complétée par 3 à 5 puces concrètes sur les faits marquants. "
        "Ce format prendra moins de 10 minutes à remplir pour les directeurs, tout en me permettant de vous compiler chaque soir une synthèse nette, "
        "percutante et immédiatement exploitable par vos systèmes d'audit."
    )
    pdf.para(
        "Sauf contrordre de votre part, je préparerai ce canevas type pour le soumettre à votre validation avant le 1er septembre."
    )

    sortie = chemin("courriels", "2041-08-17_Courriel_Mohamed_Coulibaly_Accuse_Protocole_Reporting_et_Propositions_Format.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_note_protocole_reporting()
    generer_courriel_reponse_coulibaly_reporting()
