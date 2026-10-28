"""
Génération du Rapport de Projection Financière à 5 Ans (2041-2046)
Jeudi 15 août 2041 — Tour n° 90
Préparé par le Pôle d'Analyse Financière & Modélisation Patrimoniale (Application Gestion)
pour William Ossimi, Associé Unique Fondateur
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_projection_financiere_5ans():
    pdf = DocPDF(
        "GESTION PATRIMONIALE & SOLEIL B2B CI — Pôle Modélisation Financière",
        "Rapport de Projection Patrimoniale à 5 Ans (2041 — 2046)",
        auteur="Pôle Modélisation Financière — Application Gestion",
        pied="Projection Patrimoniale 5 Ans — William Ossimi — 15/08/2041"
    )

    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Émetteur", "Pôle d'Analyse Financière & Modélisation Patrimoniale — Application Gestion")
    pdf.meta("Date d'arrêté", "Jeudi 15 août 2041, 18h30 (heure d'Abidjan)")
    pdf.meta("Horizon temporel", "5 ans (Août 2041 — Août 2046)")
    pdf.meta("Objet", "Modélisation de la valeur terminale du compte-titres ETF Monde selon 3 scénarios de développement de SOLEIL B2B CI")
    pdf.ln(3)

    pdf.titre1("1. Paramètres de Départ et Hypothèses Fondamentales")
    pdf.para(
        "L'analyse repose sur le réinvestissement systématique à 100 % de l'ensemble des dividendes futurs issus de SOLEIL B2B CÔTE D'IVOIRE "
        "vers le compte-titres ETF Monde de William Ossimi, en complément de son effort d'épargne programmé régulier (DCA luxembourgeois)."
    )

    entetes_base = ["Paramètre d'entrée", "Valeur au 15/08/2041", "Hypothèse de modélisation (2041-2046)"]
    lignes_base = [
        ["Solde initial ETF Monde", "676 135,00 €", "Point d'ancrage réel certifié au Grand Livre."],
        ["DCA Personnel Mensuel", "5 755,00 € / mois", "69 060 € / an issus du traitement net d'État luxembourgeois."],
        ["Cumul DCA personnel sur 5 ans", "345 300,00 €", "60 versements mensuels ininterrompus."],
        ["Rendement moyen ETF Monde", "7,00 % / an", "Performance annualisée nominale de l'indice MSCI World."],
        ["Amortissement du Prêt Associé (CCA)", "65 560,00 €", "Remboursement prioritaire avant toute distribution de dividende."],
        ["Gouvernance et supervision", "Score élevé (> 85)", "Maintien de la rigueur de gestion et recrutement sélectif."]
    ]
    pdf.tableau(entetes_base, lignes_base, [55, 45, 90])

    pdf.ln(3)
    pdf.titre1("2. Les Trois Scénarios de Développement de SOLEIL B2B CI")
    pdf.para(
        "Trois trajectoires d'exploitation ont été simulées, intégrant les charges de structure de la villa des Vallons, "
        "une masse salariale de 10 collaborateurs (Direction, ingénieurs d'études, technico-commerciaux, monteurs) et la politique "
        "de dividende (distribution de 60 % du résultat net après apurement complet du compte courant d'associé dès fin Année 2)."
    )

    entetes_scenarios = ["Indicateur Clé (à 5 ans)", "Scénario Pessimiste", "Scénario Probable (Médian)", "Scénario Optimiste"]
    lignes_scenarios = [
        [
            "Chiffre d'Affaires annuel (2046)",
            "520 M FCFA (≈ 793 k€)",
            "1,85 Md FCFA (≈ 2,82 M€)",
            "3,60 Md FCFA (≈ 5,49 M€)"
        ],
        [
            "Marge Nette d'Exploitation",
            "11,5 % (pression prix)",
            "19,2 % (modèle nominal)",
            "23,5 % (économies d'échelle)"
        ],
        [
            "Résultat Net annuel moyen",
            "65 000 € / an",
            "380 000 € / an",
            "890 000 € / an"
        ],
        [
            "Dividendes cumulés perçus (5 ans)",
            "92 000 €",
            "395 000 €",
            "880 000 €"
        ],
        [
            "Remboursement CCA (Capital + int.)",
            "Intégral (Année 3)",
            "Intégral (Année 2)",
            "Intégral (Fin Année 1)"
        ],
    ]
    pdf.tableau(entetes_scenarios, lignes_scenarios, [50, 45, 48, 47])

    pdf.ln(3)
    pdf.titre1("3. Projection de la Valeur Terminale du Compte ETF Monde en Août 2046")
    pdf.para(
        "La capitalisation composée (intérêts composés à 7 % l'an) appliquée au stock initial, aux flux mensuels de DCA "
        "et aux flux annuels de dividendes réinvestis produit les soldes de portefeuille suivants à horizon 5 ans :"
    )

    entetes_solde = ["Composante du Portefeuille", "Pessimiste", "Probable (Médian)", "Optimiste"]
    lignes_solde = [
        [
            "Capitalisation stock initial (676 k€)",
            "948 300 €",
            "948 300 €",
            "948 300 €"
        ],
        [
            "Capitalisation versements DCA (Luxembourg)",
            "412 150 €",
            "412 150 €",
            "412 150 €"
        ],
        [
            "Sous-total ETF (hors activité SOLEIL)",
            "1 360 450 €",
            "1 360 450 €",
            "1 360 450 €"
        ],
        [
            "Dividendes réinvestis capitalisés",
            "108 500 €",
            "462 000 €",
            "1 035 000 €"
        ],
        [
            "TOTAL COMPTE ETF MONDE (Août 2046)",
            "1 468 950 €",
            "1 822 450 €",
            "2 395 450 €"
        ],
        [
            "Valorisation estimée des parts SOLEIL B2B",
            "350 000 €",
            "1 900 000 €",
            "4 200 000 €"
        ],
        [
            "PATRIMOINE PROFESSIONNEL + ETF CUMULÉ",
            "1 818 950 €",
            "3 722 450 €",
            "6 595 450 €"
        ],
    ]
    pdf.tableau(entetes_solde, lignes_solde, [60, 42, 44, 44])

    pdf.ln(3)
    pdf.titre1("4. Enseignements Stratégiques pour l'Actionnaire")
    pdf.para(
        "1. L'effet socle du DCA luxembourgeois garantit à lui seul un portefeuille ETF supérieur à 1,36 M€ en 2046, "
        "indépendamment des aléas de l'entreprise ivoirienne.\n"
        "2. Dans le scénario probable, SOLEIL B2B CI propulse le portefeuille ETF à plus de 1,82 M€ liquides et confère à William Ossimi "
        "un patrimoine global consolidé approchant les 4 millions d'euros à 41 ans.\n"
        "3. La clé de voûte de cette trajectoire réside dans la sélection rigoureuse de la Direction Commerciale (seuil > 80/100) et "
        "la discipline d'exécution sans déviation sur les coûts fixes."
    )

    sortie = chemin("documents_william", "2041-08-15_Projection_Financiere_5_Ans_ETF_Soleil_B2B.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_projection_financiere_5ans()

