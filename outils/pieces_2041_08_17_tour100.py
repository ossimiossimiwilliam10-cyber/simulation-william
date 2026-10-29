"""
Génération des pièces officielles du samedi 17 août 2041, 12h30 (Tour n° 100) :
1. Courriel officiel de Mohamed Coulibaly (16/08 22h50) : Validation des 3 verrous contractuels anti-défaut client et confirmation du rendez-vous
2. Rapport officiel d'inspection technique et d'agencement du siège social des Vallons rédigé par William Ossimi
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_coulibaly_verrous():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Accusé de Réception & Validation des Directives de Recouvrement",
        auteur="Mohamed Coulibaly",
        pied="Directives de Recouvrement B2B — SOLEIL B2B CI — 16/08/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly, Directeur Général (m.coulibaly@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Vendredi 16 août 2041, 22h50 (heure d'Abidjan)")
    pdf.meta("Objet", "Validation des 3 verrous de sécurisation financière des contrats B2B et confirmation rendez-vous Vallons")
    pdf.ln(3)

    pdf.titre1("1. Intégration impérative des verrous anti-défaut dans les contrats commerciaux")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "J'accuse réception avec la plus grande attention de vos directives stratégiques relatives à la gestion du risque de contrepartie client. "
        "Votre analyse est d'une remarquable lucidité : dans l'écosystème industriel ouest-africain, le risque létal pour un producteur d'énergie "
        "décentralisée ne réside pas dans la technologie photovoltaïque, mais dans la défaillance ou l'inertie de paiement des acheteurs d'électricité."
    )
    pdf.para(
        "Je valide sans la moindre réserve les trois instruments de protection que vous formulez, et je vous confirme qu'ils sont d'ores et déjà "
        "érigés en règles d'or non négociables pour la Direction Commerciale et la DAF :"
    )
    pdf.para(
        "1. Caution bancaire ou dépôt de garantie obligatoire de trois (3) mois de redevances estimées, exigible dès la signature avant tout approvisionnement de matériel."
    )
    pdf.para(
        "2. Clause de réserve de propriété stricte et opposable aux tiers, sanctuarisant la propriété juridique inaliénable des modules solaires, onduleurs et batteries au profit de SOLEIL B2B CI jusqu'au terme complet du contrat PPA."
    )
    pdf.para(
        "3. Système de télécoupure et de bridage à distance par automate connecté GSM/satellite : en cas de retard de paiement supérieur à quinze (15) jours après mise en demeure, bascule automatique de la centrale solaire en mode veille technique, forçant l'industriel à repasser sur le tarif prohibitif du réseau conventionnel."
    )
    pdf.para(
        "Je brieferai formellement Viviane Tanoh et Mariam Brou dès lundi matin afin que ces clauses soient intégrées dans notre trame contractuelle standard."
    )

    pdf.titre1("2. Confirmation du rendez-vous à la Villa des Vallons")
    pdf.para(
        "Je serai présent devant le portail de la villa dès 09h50 demain matin, samedi 17 août. Les clés, l'état des lieux d'entrée et les plans cadastraux "
        "seront à votre disposition. Prenez tout le temps nécessaire pour votre inspection : je me plierai scrupuleusement à votre rythme."
    )

    sortie = chemin("courriels", "2041-08-16_Courriel_Mohamed_Coulibaly_Validation_Verrous_Contractuels_et_Rendez_Vous_Vallons.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


def generer_rapport_inspection_villa():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Rapport d'Inspection Technique, Sécurité & Schéma d'Agencement du Siège Social",
        auteur="Monsieur William Ossimi, Associé Unique Fondateur",
        pied="Inspection Siège Social Villa Vallons — 17/08/2041"
    )

    pdf.meta("Site inspecté", "Villa Duplex 7 Pièces — Cocody Deux-Plateaux Vallons, Abidjan")
    pdf.meta("Date de la visite", "Samedi 17 août 2041, de 10h00 à 12h30")
    pdf.meta("Participants", "William Ossimi (Fondateur) ; Mohamed Coulibaly (Directeur Général, de 10h00 à 11h45)")
    pdf.meta("Objectif", "Audit technique exhaustif, diagnostic des infrastructures et affectation spatiale des pôles")
    pdf.ln(3)

    pdf.titre1("1. Diagnostic des infrastructures techniques & énergie de secours")
    pdf.para(
        "L'inspection minutieuse des installations techniques a permis de valider la conformité générale du site :"
    )
    pdf.para(
        "- Groupe électrogène de secours : Marque SDMO / Perkins, puissance nominale 45 kVA insonorisé. Démarrage à sec et bascule automatique "
        "opérés avec succès lors du test de 10h25. Cuve de carburant sécurisée de 500 litres en parfait état, garantissant 48 heures d'autonomie continue."
    )
    pdf.para(
        "- Tableau Général Basse Tension (TGBT) : Câblage propre, disjoncteurs différentiels conformes. Nécessité d'installer un coffret parafoudre dédié "
        "pour protéger les futurs équipements informatiques et onduleurs face aux surtensions orageuses abidjanaises."
    )
    pdf.para(
        "- Toiture et gisement solaire propre : Toiture en bac acier à double pente, orientée sud-sud-est, dégagée de tout ombrage majeur. "
        "Surface utile estimée à 140 m², permettant d'implanter une centrale photovoltaïque témoin de 15 kWc couplée à 20 kWh de batteries LiFePO4. "
        "Cette installation assurera l'autoconsommation complète du siège social et constituera un showroom grandeur nature pour les prospects industriels."
    )

    pdf.titre1("2. Schéma d'affectation spatiale des sept pièces")
    entetes_pieces = ["Espace / Pièce", "Niveau", "Affectation opérationnelle", "Équipements requis"]
    lignes_pieces = [
        ["Grand Salon", "RDC", "Espace Commercial B2B & Accueil Showroom", "Bureaux modulaires, écrans de monitoring, canapés accueil"],
        ["Salle à Manger", "RDC", "Salle du Conseil de Direction & Visioconférence", "Grande table de conférence 10 places, visioconférence 4K"],
        ["Pièce Est (RDC)", "RDC", "Direction Administrative & Financière (DAF)", "Bureaux Brou + Comptable + Risk Analyst, coffre-fort scellé"],
        ["Cuisine / Office", "RDC", "Espace Détente, Cafétéria & Tisanerie", "Réfrigérateur, micro-ondes, distributeur d'eau, rangements"],
        ["Suite Parentale", "Étage", "Bureau du Directeur Général (DG Coulibaly)", "Bureau direction bois massif, salon privé, salle d'eau"],
        ["Pièce Nord (Étage)", "Étage", "Direction Technique (DT Éric Yao & Études)", "Stations de travail DAO/PVsyst, banc d'essai matériel"],
        ["Pièce Ouest (Étage)", "Étage", "Salle Serveurs Sécurisée & Baie de Brassage", "Baie rack 42U, clim dédiée 24/7, onduleurs online, fibre"],
        ["Pièce Sud (Étage)", "Étage", "Salle d'Archives Sécurisées & Documentation", "Rayonnages métalliques ignifuges, documentation RCCM"]
    ]
    pdf.tableau(entetes_pieces, lignes_pieces, [35, 20, 75, 60])

    pdf.ln(3)
    pdf.titre1("3. Sécurité du périmètre & Réseau")
    pdf.para(
        "- Périmètre extérieur : Clôture maçonnée de 2,60 mètres de haut surmontée d'une herse de concertina. Guérite de sécurité à l'entrée. "
        "Recommandation : pose de 4 caméras IP infrarouges couvrant les angles morts de la cour et le portail motorisé."
    )
    pdf.para(
        "- Réseau télécom : Présence d'un regard fibre optique en bordure de propriété (Orange CI). Lancement immédiat de la demande de raccordement "
        "Fibre Pro avec adresse IP fixe et routeur double WAN."
    )

    pdf.titre1("4. Décision de l'Associé Unique")
    pdf.para(
        "Le site de la Villa des Vallons est validé sans réserve. Mohamed Coulibaly est autorisé à lancer les consultations d'artisans "
        "pour la peinture intérieure (blanc satiné / gris perle institutionnel), la révision des climatiseurs et le câblage réseau Cat 6A, "
        "dans la limite du budget d'aménagement préliminaire alloué."
    )

    sortie = chemin("documents_william", "2041-08-17_Rapport_Inspection_Technique_et_Agencement_QG_Vallons.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_courriel_coulibaly_verrous()
    generer_rapport_inspection_villa()

