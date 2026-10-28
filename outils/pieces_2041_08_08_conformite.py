"""
Génération de la Maquette du Système de Contrôle Interne, Conformité et Sécurité Anti-Détournement
Jeudi 8 août 2041 — Tour n° 74
Document préparatoire confidentiel destiné exclusivement à l'Associé Unique Fondateur
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_maquette_conformite_securite():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Dispositif de Sécurité & Conformité",
        "Maquette du Système de Contrôle Interne, Prévention des Détournements et Protection Anti-Fraude",
        auteur="Pôle Juridique & Audit Virtuel",
        pied="Dispositif Contrôle Interne & Anti-Détournement — SOLEIL B2B CI — 08/08/2041"
    )

    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (usage strictement confidentiel)")
    pdf.meta("Rédacteur", "Pôle Juridique, Financier & Audit Virtuel — Application Gestion")
    pdf.meta("Date d'établissement", "Jeudi 8 août 2041, 18h00 (heure de Luxembourg)")
    pdf.meta("Objet", "Architecture du système de verrouillage financier, gouvernance anti-coup d'État et surveillance")
    pdf.ln(3)

    pdf.titre1("1. Préambule et doctrine de sécurité")
    pdf.para(
        "Ce document établit l'architecture de contrôle interne destinée à immuniser SOLEIL B2B CÔTE D'IVOIRE SASU "
        "contre tout risque de détournement d'actifs, de malversation financière, de manipulation de rapports ou de "
        "tentative de captation hostile de la clientèle par les dirigeants locaux. La doctrine repose sur un principe "
        "cardinal : la confiance n'exclut pas le contrôle systématique et automatisé par des canaux indépendants."
    )

    pdf.titre1("2. Verrouillage financier et règle du 'Zéro Espèces'")
    pdf.para(
        "L'ensemble des flux financiers de l'entreprise est intégralement bancarisé sans aucune exception :"
    )
    pdf.puces([
        "Proscription absolue des espèces : Interdiction formelle de détenir une caisse physique, d'encaisser des règlements clients en liquide ou d'effectuer des paiements en espèces. Tout règlement s'opère par virement bancaire interbancaire ou chèque de banque barré ;",
        "Règle de la double signature bancaire électronique : Les conventions de compte auprès des banques partenaires à Abidjan (BICICI, Société Générale CI) instaurent un double niveau d'autorisation. Le Président-Directeur Général initie les ordres de virement, mais tout mouvement unitaire supérieur au seuil statutaire de 10 000 000 FCFA (environ 15 245 €) requiert obligatoirement la co-validation électronique (clé token sécurisée) de l'Associé Unique ;",
        "Accès bancaire direct en consultation 24/7 : L'Associé Unique dispose d'un identifiant bancaire administrateur autonome permettant la consultation en direct et l'exportation quotidienne des relevés de compte officiels, sans dépendre des extraits fournis par l'équipe locale ;",
        "Facturation et justification intégrale : Aucun décaissement n'est autorisé sans l'adossement d'une facture pro-forma validée, d'un bon de commande signé et d'un procès-verbal de réception technique."
    ])

    pdf.titre1("3. Séparation fonctionnelle des tâches (Règle des 3 Tiers)")
    pdf.para(
        "Pour empêcher toute collusion interne, les processus opérationnels sont strictement compartimentés :"
    )
    pdf.puces([
        "Tiers 1 — Engagement commercial : Le pôle commercial et le PDG négocient les offres et signent les devis clients ;",
        "Tiers 2 — Constat du service fait : La Direction Technique (DT) valide la conformité des livraisons de panneaux, l'inventaire physique des stocks et la réalité des travaux sur chantier via un procès-verbal d'inspection signé ;",
        "Tiers 3 — Règlement et comptabilisation : La Directrice Administrative et Financière (DAF) ordonnance le paiement uniquement après rapprochement strict entre la facture fournisseur et le PV technique. La DAF n'a pas le pouvoir d'engager des chantiers, et la DT n'a pas accès aux comptes bancaires."
    ])

    pdf.titre1("4. Protection contre la concurrence déloyale et le détournement de clientèle")
    pdf.para(
        "Afin d'éviter qu'un dirigeant ne capte l'activité à son profit ou ne crée une structure parallèle concurrente :"
    )
    pdf.puces([
        "Propriété exclusive des actifs immatériels : L'intégralité des études techniques, dimensionnements PVsyst, marques, supports commerciaux et contrats types sont déposés au nom exclusif de la SASU avec protection OAPI ;",
        "Centralisation souveraine de la base clients : Le fichier clients et les opportunités commerciales sont hébergés sur un CRM sécurisé dont les accès administrateurs racine (root) sont détenus par l'Associé Unique. Toute extraction massive de données déclenche une alerte de sécurité immédiate ;",
        "Clauses de non-concurrence et pénalités dissuasives : La convention de mandat du PDG verrouille une interdiction de concurrence de 12 mois post-mandat sur tout le District d'Abidjan, assortie d'une clause pénale immédiate de 24 000 000 FCFA (environ 36 500 €) et de poursuites pénales pour abus de confiance en cas de manquement."
    ])

    pdf.titre1("5. Détection des faux rapports et surveillance croisée")
    pdf.para(
        "Pour neutraliser tout risque de falsification de données d'activité par le management local, un triple canal "
        "de vérification croisée est institué :"
    )
    pdf.puces([
        "Croisement bancaire et fiscal : Les chiffres de vente déclarés dans les rapports du PDG sont systématiquement confrontés aux encaissements bancaires réels et aux déclarations de TVA déposées auprès de la Direction Générale des Impôts (DGI) ;",
        "Télémonitoring direct des centrales : Les compteurs électriques communicants installés sur chaque toiture industrielle transmettent leurs données de production en direct sur un serveur de supervision indépendant, certifiant le raccordement effectif et la puissance réelle délivrée sans intermédiaire ;",
        "Audit légal externe indépendant : Nomination d'un Commissaire aux comptes / cabinet d'expertise comptable indépendant inscrit à l'Ordre national des experts-comptables de Côte d'Ivoire (ONECCA), mandaté pour réaliser un audit semestriel inopiné des écritures et un inventaire physique annuel."
    ])

    pdf.titre1("6. Gouvernance et pilotage du système de contrôle")
    pdf.para(
        "Qui pilote ce dispositif ? La supervision du système est déléguée au Pôle Audit & Conformité Virtuel de William "
        "(intégré dans l'application Gestion). Ce pôle indépendant de la direction locale assure la réconciliation hebdomadaire "
        "automatisée des flux, émet des alertes d'anomalies en temps réel et transmet une note de synthèse confidentielle à "
        "l'Associé Unique. En cas de dérive caractérisée, l'Associé Unique conserve la faculté statutaire de révoquer ad nutum "
        "le mandataire social et de bloquer instantanément les procurations bancaires."
    )

    cible = chemin("documents_william", "2041-08-08_Maquette_Systeme_Controle_Conformite_Anti_Detournement.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_maquette_conformite_securite()
