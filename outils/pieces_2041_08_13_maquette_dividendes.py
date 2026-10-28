"""
Génération de la Maquette de Politique de Distribution des Dividendes et Réinvestissement ETF Monde
Mardi 13 août 2041 — Tour n° 83
Document stratégique préparé par le Pôle Financier Virtuel pour William Ossimi et Mohamed Coulibaly
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_maquette_dividendes():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Pôle Financier Virtuel",
        "Maquette Stratégique : Politique de Distribution des Dividendes & Boucle de Réinvestissement ETF Monde",
        auteur="Pôle Financier & Stratégie Virtuel",
        pied="Politique de Distribution Dividendes & Réinvestissement ETF — SOLEIL B2B CI — 13/08/2041"
    )

    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Copie pour information", "Monsieur Mohamed Coulibaly, Président-Directeur Général")
    pdf.meta("Rédacteur", "Pôle Financier Virtuel — Application Gestion")
    pdf.meta("Date d'établissement", "Mardi 13 août 2041, 15h30 (heure d'Abidjan)")
    pdf.meta("Objet", "Arbitrage de financement du prêt d'associé (65 560 €), cadencement des dividendes et réinvestissement indiciel")
    pdf.ln(3)

    pdf.titre1("1. Analyse financière de l'arbitrage d'apport : Compte Épargne vs ETF Monde")
    pdf.para(
        "Pour couvrir l'enveloppe d'installation et d'équipement initial chiffrée à 43 000 000 FCFA (soit 65 560 €), "
        "l'Associé Unique William Ossimi envisage un apport mixte réparti à 50 % sur son compte épargne projet et 50 % "
        "sur son compte-titres ETF Monde Spuerkeess. Le pôle financier virtuel a procédé à l'analyse comparative des impacts :"
    )

    entetes_arbitrage = ["Source de financement", "Montant prélevé", "Solde résiduel", "Impact patrimonial & fiscal"]
    lignes_arbitrage = [
        ["Compte Épargne Projet", "32 780 € (50 %)", "43 202 €", "Liquidité immédiate préservée au-delà du matelas d'urgence (25 250 €) ; aucun frottement fiscal."],
        ["Compte-Titres ETF Monde", "32 780 € (50 %)", "643 355 €", "Prélèvement de 4,8 % du portefeuille ; exonération fiscale luxembourgeoise (> 6 mois, art. 99ter LIR) ; frais d'ordre 25 €."],
        ["Total Apport d'Associé", "65 560 € (100 %)", "694 912 € (Total)", "Structure financière saine. Alternative à 100 % épargne possible pour préserver les intérêts composés."]
    ]
    pdf.tableau(entetes_arbitrage, lignes_arbitrage, [45, 35, 30, 80])

    pdf.para(
        "Recommandation du Pôle Financier : La formule 50/50 est pleinement validée. Elle conserve une marge de sécurité liquide "
        "confortable tout en réduisant l'exposition au compte d'épargne. L'ordre de rachat ETF sera calibré pour minimiser les frais de transaction."
    )

    pdf.titre1("2. Cadre juridique et fiscal de la distribution sous droit OHADA")
    pdf.para(
        "La politique de rémunération de l'actionnaire unique de SOLEIL B2B CÔTE D'IVOIRE obéit à une hiérarchie stricte des flux financiers :"
    )
    pdf.puces([
        "Priorité absolue à l'apurement du Compte Courant d'Associé (CCA) : Avant tout dividende, 100 % de la capacité d'autofinancement excédentaire est affectée au remboursement du prêt de 65 560 €. Ce remboursement est fiscalement neutre (exonéré d'IRVM) ;",
        "Dotation de la réserve légale : Selon l'Acte Uniforme OHADA sur les sociétés commerciales, un prélèvement obligatoire de 10 % est opéré sur le bénéfice net jusqu'à ce que la réserve légale atteigne 20 % du capital (soit 200 000 FCFA, atteinte dès la première clôture bénéficiaire) ;",
        "Fiscalité de distribution : Les dividendes réguliers sont assujettis à l'Impôt sur le Revenu des Valeurs Mobilières (IRVM) au taux de 15 %, retenu à la source par l'État ivoirien, le solde net de 85 % étant librement transférable."
    ])

    pdf.titre1("3. Taux de distribution cible (Payout Ratio) et périodicité")
    pdf.para(
        "Afin de garantir à la fois l'autonomie d'investissement de la société et un retour sur capital substantiel pour William Ossimi, "
        "la grille de distribution est arrêtée comme suit :"
    )

    entetes_distribution = ["Régime de distribution", "Part du résultat net", "Périodicité", "Conditions préalables"]
    lignes_distribution = [
        ["Phase d'apurement CCA", "0 % dividendes / 100 % CCA", "Trimestrielle au réel", "Résultat net positif et trésorerie minimale de 6 mois d'OPEX."],
        ["Régime de croisière", "40 % à 50 % du résultat net", "Annuelle (après AG)", "Compte courant soldé ; réserve légale dotée ; trésorerie saine."],
        ["Option Acomptes", "Acomptes semestriels", "Semestrielle (octobre)", "Bilan intermédiaire certifié par la DAF attestant d'un bénéfice net."],
        ["Réserves de croissance", "50 % à 60 % réinvestis", "Permanent", "Autofinancement des recrutements et du BFR sans dette bancaire."]
    ]
    pdf.tableau(entetes_distribution, lignes_distribution, [45, 45, 40, 60])

    pdf.titre1("4. Boucle souveraine de réinvestissement indiciel ETF Monde")
    pdf.para(
        "L'ensemble des liquidités perçues par William Ossimi sous forme de remboursement de prêt ou de dividendes nets est immédiatement "
        "réinjecté dans l'architecture patrimoniale d'accumulation :"
    )
    pdf.puces([
        "Rapatriement international automatisé : Virement direct des dividendes nets d'IRVM depuis le compte d'entreprise d'Abidjan vers le compte Spuerkeess Luxembourg de William Ossimi ;",
        "Ordre d'achat ETF MSCI World : Allocation à 100 % des montants rapatriés en parts d'ETF Monde à réplication physique et capitalisante (dividendes réinvestis sans friction fiscale locale) ;",
        "Effet cliquet et reconstitution patrimoniale : Le capital initialement injecté dans SOLEIL B2B CI retourne intégralement dynamiser le portefeuille boursier de long terme, amplifiant les intérêts composés."
    ])

    pdf.titre1("5. Feuille de route opérationnelle pour Mohamed Coulibaly")
    pdf.para(
        "Ce document sera formellement transmis à Mohamed Coulibaly et Mariam Brou pour intégration dans les statuts et le manuel "
        "de procédures administratives et financières dès l'obtention du RCCM au CEPICI."
    )

    fichier_pdf = RACINE / "documents_william" / "2041-08-13_Maquette_Politique_Distribution_Dividendes_et_Reinvestissement_ETF.pdf"
    pdf.sauver(str(fichier_pdf))
    print(f"Document généré : {fichier_pdf}")


if __name__ == "__main__":
    generer_maquette_dividendes()

