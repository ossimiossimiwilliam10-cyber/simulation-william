"""
Génération de l'Étude de Cadrage : Analyse Quantitative des Risques, Modélisation Financière et Protection Patrimoniale
Vendredi 9 août 2041 — Tour n° 75
Document préparatoire confidentiel destiné à l'Associé Unique Fondateur
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_etude_risques_quantitatifs():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Direction Financière & Stratégie",
        "Étude de Cadrage : Intégration d'un Analyste Quantitatif, Modélisation du Risque et Alerte Trésorerie",
        auteur="Pôle Finance & Stratégie Virtuel",
        pied="Cadrage Analyse Risques & Alerte Trésorerie — SOLEIL B2B CI — 09/08/2041"
    )

    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Rédacteur", "Pôle Financier & Stratégie Virtuel — Application Gestion")
    pdf.meta("Date d'établissement", "Vendredi 9 août 2041, 09h30 (heure de Luxembourg)")
    pdf.meta("Objet", "Architecture de maîtrise du risque d'insolvabilité, recrutement d'un analyste quantitatif et surveillance patrimoniale")
    pdf.ln(3)

    pdf.titre1("1. Préambule : L'enjeu de la survie financière à long terme")
    pdf.para(
        "L'interrogation soulevée par l'Associé Unique touche au cœur de la pérennité d'un développeur solaire : "
        "dans un modèle d'autoproduction industrielle (contrats PPA sur 10 à 15 ans), le risque principal n'est pas "
        "technologique, mais financier et structurel. L'entreprise supporte les coûts d'investissement initiaux lourds (CAPEX) "
        "et ne recouvre ses capitaux que progressivement sous forme de redevances mensuelles. Si les coûts dérapent, si les "
        "clients industriels font défaut ou si les dépenses fixes excèdent le rythme des raccordements, l'entreprise s'expose "
        "à une crise de liquidité aiguë."
    )

    pdf.titre1("2. Rôle, profil et rattachement de l'Analyste Quantitatif (Risk Analyst)")
    pdf.para(
        "Pour mesurer scientifiquement le risque, le recrutement d'un Analyste Quantitatif (Quantitative Risk Analyst) "
        "est une décision stratégique à intégrer dans la trajectoire de croissance :"
    )
    pdf.puces([
        "Rattachement organisationnel impératif : L'analyste quantitatif doit obligatoirement être rattaché au Pôle Finance & Comptabilité (sous l'autorité de la DAF Mariam Brou), avec un canal de reporting direct vers le PDG. Le positionner au commercial créerait un conflit d'intérêts structurel : le commercial est incité au volume, tandis que l'analyste du risque a pour mandat d'évaluer objectivement la solidité des contreparties ;",
        "Missions principales :",
        "  • Modélisation du risque de contrepartie : scoring financier et probabilité de défaut sur 10 ans des entreprises industrielles clientes avant tout engagement de travaux ;",
        "  • Modélisation du risque de change et d'inflation : simulation des fluctuations EUR/USD/FCFA impactant l'achat des panneaux solaires Tier-1 importés ;",
        "  • Analyse de sensibilité des flux de trésorerie : calcul du taux de rentabilité interne (TRI), de la valeur actuelle nette (VAN) et du coût moyen actualisé du kWh produit (LCOE) par toiture ;",
        "  • Suivi hebdomadaire du 'Burn Rate' : mesure de la vitesse d'épuisement des liquidités par rapport au calendrier d'encaissement prévisionnel."
    ])

    pdf.titre1("3. Le double niveau de défense : Contre-expertise par le pôle virtuel")
    pdf.para(
        "Pour garantir que l'Associé Unique ne soit jamais dépendant d'un rapport interne biaisé ou complaisant, "
        "un dispositif de double contrôle automatisé est institué :"
    )
    pdf.puces([
        "Premier niveau (Local — Abidjan) : L'analyste quantitatif produit mensuellement la matrice des risques de l'entreprise et la soumet au PDG et à la DAF ;",
        "Second niveau (Souverain — Pôle Virtuel) : Le pôle financier virtuel de William reçoit directement les données sources brutes et applique son propre modèle de stress-test indépendant. À chaque apport en compte courant ou appel de fonds demandé par Abidjan, l'équipe virtuelle calcule le 'Runway' résiduel (nombre de mois de trésorerie disponible avant rupture) et émet un diagnostic binaire clair : Trajectoire soutenable / Risque de dérive / Alerte critique de faillite."
    ])

    pdf.titre1("4. Connexion bancaire de William (Open Banking) et étanchéité patrimoniale")
    pdf.para(
        "La proposition de connecter l'application bancaire personnelle de William à son système de gestion virtuelle "
        "renforce la sécurité patrimoniale de l'investisseur :"
    )
    pdf.puces([
        "Agrégation sécurisée en lecture seule : Via les protocoles Open Banking européens (norme DSP2 / API bancaire Spuerkeess), l'équipe virtuelle suit en temps réel les soldes du compte courant et du livret projet sans aucun risque d'opération non sollicitée ;",
        "Simulation d'impact patrimonial : Avant tout décaissement vers Abidjan, le simulateur mesure l'impact sur le patrimoine net de William (858 862 €), garantissant qu'aucun apport ne vienne menacer sa sécurité financière personnelle ni son épargne de précaution ;",
        "Principe fondamental d'étanchéité juridique : En qualité d'Associé Unique d'une SASU, la responsabilité financière de William est strictement plafonnée au montant de son apport au capital social (10 000 000 FCFA, soit environ 15 245 €). Tant que William ne souscrit aucun cautionnement personnel ni garantie solidaire sur les emprunts de la société, une défaillance éventuelle de l'entreprise ne peut en aucun cas impacter son patrimoine personnel (maison, portefeuille d'ETF Monde, comptes luxembourgeois)."
    ])

    pdf.titre1("5. Recommandation opérationnelle pour la mission d'Abidjan")
    pdf.para(
        "Le pôle virtuel préconise d'inscrire le principe du poste d'analyste quantitatif dans l'organigramme cible "
        "de phase 2 (dès que le portefeuille de projets dépasse 3 centrales en étude), et d'intégrer formellement dans les "
        "discussions avec Mohamed Coulibaly l'obligation d'un modèle d'évaluation des risques validé par l'Associé Unique."
    )

    cible = chemin("documents_william", "2041-08-09_Etude_Cadrage_Analyse_Risques_Financiers_et_Modele_Quantitatif.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_etude_risques_quantitatifs()

