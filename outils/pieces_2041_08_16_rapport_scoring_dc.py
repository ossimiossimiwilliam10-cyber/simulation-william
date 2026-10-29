"""
Génération du rapport officiel d'évaluation et de scoring de la Direction Commerciale
Vendredi 16 août 2041, 13h00 — Tour n° 95
Préparé par le Pôle RH & Commercial Virtuel pour William Ossimi
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_rapport_scoring_dc():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Pôle RH & Commercial Virtuel",
        "Rapport d'Évaluation Stratégique & Scoring Comparatif : Direction Commerciale",
        auteur="Pôle RH & Commercial Virtuel — Application Gestion",
        pied="Scoring Direction Commerciale — SOLEIL B2B CI — 16/08/2041"
    )

    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Rédacteur", "Pôle RH & Commercial Virtuel — Application Gestion v0.3")
    pdf.meta("Date d'établissement", "Vendredi 16 août 2041, 13h00 (heure d'Abidjan)")
    pdf.meta("Objet", "Analyse objective et scoring multicritère des candidatures de M. Marc-Antoine Kouadio et Mme Viviane Tanoh")
    pdf.ln(3)

    pdf.titre1("1. Doctrine de recrutement et rappel du cadre d'arbitrage")
    pdf.para(
        "Conformément aux directives souveraines de l'Associé Unique et aux règles de gouvernance établies dans l'application Gestion, "
        "la sélection du Directeur Commercial de SOLEIL B2B CÔTE D'IVOIRE est soumise à un seuil éliminatoire strict supérieur à 80 sur 100 (> 80/100), "
        "avec une exigence minimale de 85/100 sur les composantes clés du cœur de métier commercial (portefeuille et vélocité de closing)."
    )
    pdf.para(
        "L'évaluation a été menée par le pôle d'intelligence commerciale virtuel sur la base des dossiers complets, des références professionnelles, "
        "des cartographies de prospects et des propositions d'actions opérationnelles remises le 16 août 2041 à 12h00."
    )

    pdf.titre1("2. Évaluation détaillée de Monsieur Marc-Antoine Kouadio (Note : 84,7 / 100)")
    pdf.para(
        "Monsieur Marc-Antoine Kouadio (38 ans), ingénieur d'affaires grands comptes dans l'énergie, présente un profil de haute technicité "
        "et de rigueur institutionnelle."
    )
    pdf.puces([
        "Axe 1 — Accès au Portefeuille Clients (pondération 25 %) : Note 88 / 100. Cartographie solide de 14 comptes industriels majeurs à Vridi et San Pedro (cimenteries, agro-industrie, minoteries). Accès direct attesté auprès de 9 décideurs. Potentiel de puissance élevé (250 kWc à 1 MWc par site).",
        "Axe 2 — Offre Anti-Délestage CIE (pondération 25 %) : Note 90 / 100. Excellente modélisation financière du coût complet du kWh thermique comparé au solaire avec stockage batteries LFP, avec un temps d'amortissement documenté de 4,2 ans. Argumentaire financier d'une efficacité redoutable face aux directions financières.",
        "Axe 3 — Vélocité du Cycle de Vente (pondération 20 %) : Note 72 / 100. Point de vigilance majeur. Le cycle moyen annoncé (75 à 90 jours) excède l'objectif cible de 60 jours en raison de la lourdeur décisionnelle des comités d'investissement industriels.",
        "Axe 4 — Management Équipe Terrain (pondération 15 %) : Note 78 / 100. Management directif et très analytique axé sur le reporting CRM. Risque de rigidité face à de jeunes commerciaux de terrain nécessitant un accompagnement de proximité.",
        "Axe 5 — Conformité & Zéro Bakchich (pondération 15 %) : Note 94 / 100. Intégrité exemplaire. Refus absolu de tout intermédiaire informel, audits bilatéraux et clauses éthiques strictes conformes aux standards internationaux."
    ])

    pdf.titre1("3. Évaluation détaillée de Madame Viviane Tanoh (Note : 86,4 / 100)")
    pdf.para(
        "Madame Viviane Tanoh (36 ans), directrice des ventes en distribution industrielle, incarne un profil commercial offensif, "
        "extrêmement dynamique et orienté résultats rapides."
    )
    pdf.puces([
        "Axe 1 — Accès au Portefeuille Clients (pondération 25 %) : Note 86 / 100. Liste de 18 PME/PMI à Yopougon et Treichville (chambres froides, conserveries, imprimeries) souffrant directement des délestages. Accès direct aux patrons propriétaires, circuits de décision très courts.",
        "Axe 2 — Offre Anti-Délestage CIE (pondération 25 %) : Note 80 / 100. Argumentaire économique très percutant centré sur la sauvegarde des stocks et la continuité de service, mais dépendance forte vis-à-vis du bureau d'études technique pour les calculs d'ingénierie.",
        "Axe 3 — Vélocité du Cycle de Vente (pondération 20 %) : Note 94 / 100. Performance exceptionnelle. Plan de closing en 45 jours soutenu par un accord de principe de leasing bancaire à 100 % sur 5 ans avec deux banques locales, annulant le frein de l'apport initial.",
        "Axe 4 — Management Équipe Terrain (pondération 15 %) : Note 92 / 100. Leadership commercial terrain remarquable : coaching hebdomadaire, débriefings quotidiens, tournées en clientèle et intéressement stimulant aux paliers de vente.",
        "Axe 5 — Conformité & Zéro Bakchich (pondération 15 %) : Note 82 / 100. Respect strict du cadre légal. Préconise le recours à des conventions d'apport d'affaires formelles facturées par des entités déclarées, nécessitant un suivi vigilant de conformité."
    ])

    pdf.titre1("4. Matrice de Synthèse et Comparatif des Scores")
    entetes_matrice = ["Axe d'évaluation", "Pondération", "M.-A. Kouadio", "Score K.", "V. Tanoh", "Score T."]
    lignes_matrice = [
        ["1. Portefeuille Clients", "25 %", "88 / 100", "22,00", "86 / 100", "21,50"],
        ["2. Offre Anti-Délestage", "25 %", "90 / 100", "22,50", "80 / 100", "20,00"],
        ["3. Vélocité Cycle Vente", "20 %", "72 / 100", "14,40", "94 / 100", "18,80"],
        ["4. Management Terrain", "15 %", "78 / 100", "11,70", "92 / 100", "13,80"],
        ["5. Conformité Éthique", "15 %", "94 / 100", "14,10", "82 / 100", "12,30"],
        ["TOTAL PONDÉRÉ", "100 %", "84,7 / 100", "84,70", "86,4 / 100", "86,40"]
    ]
    pdf.tableau(entetes_matrice, lignes_matrice, [45, 25, 30, 25, 30, 25])

    pdf.ln(3)
    pdf.titre1("5. Analyse Stratégique et Recommandation Arbitrale")
    pdf.para(
        "Constat d'éligibilité : Les deux candidatures franchissent le seuil éliminatoire de 80/100 imposé par l'entreprise "
        "(84,7/100 pour Kouadio ; 86,4/100 pour Tanoh). Tous deux satisfont également à l'exigence d'excellence sur le cœur de métier commercial (> 85/100)."
    )
    pdf.para(
        "Arbitrage stratégique soumis à l'Associé Unique :\n"
        "• Option Kouadio : Privilégie la sécurité technique, la crédibilité institutionnelle et des contrats industriels de grande envergure (250 kWc à 1 MWc), mais au prix d'un délai d'encaissement plus long (3 mois) et d'un management moins entraînant pour les juniors.\n"
        "• Option Tanoh : Privilégie la vélocité commerciale immédiate (closing sous 45 jours via leasing), des rentrées de trésorerie rapides sur le segment des PME/PMI et un encadrement terrain très énergique, avec une rémunération fixe légèrement plus modérée (1,4 M FCFA vs 1,5 M FCFA).\n\n"
        "Le choix définitif relève de la décision discrétionnaire de Monsieur William Ossimi, avant notification officielle au Directeur Général Mohamed Coulibaly."
    )

    sortie = chemin("documents_william", "2041-08-16_Rapport_Evaluation_et_Scoring_Direction_Commerciale.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_rapport_scoring_dc()

