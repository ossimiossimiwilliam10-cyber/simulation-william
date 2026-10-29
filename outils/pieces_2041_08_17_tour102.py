"""
Génération des pièces officielles du samedi 17 août 2041, 22h30 (Tour n° 102) :
1. Directive de Gouvernance de William Ossimi : Arbitrage et Validation du Format de Reporting Journalier par Indicateurs Clés (KPIs)
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_validation_reporting_kpis():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Directive de Gouvernance : Arbitrage et Validation du Format de Reporting par KPIs",
        auteur="Monsieur William Ossimi, Associé Unique Fondateur",
        pied="Arbitrage Reporting Agile KPIs — SOLEIL B2B CI — 17/08/2041"
    )

    pdf.meta("Émetteur", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur Mohamed Coulibaly, Directeur Général (dg@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Samedi 17 août 2041, 18h45 (heure d'Abidjan)")
    pdf.meta("Objet", "Validation définitive du compromis pragmatique sur le format de reporting opérationnel agile")
    pdf.ln(3)

    pdf.titre1("1. Arbitrage de l'Associé Unique et adhésion au compromis opérationnel")
    pdf.para(
        "Faisant suite à la note d'analyse et aux propositions transmises le 17 août 2041 à 17h15 par la Direction Générale, "
        "l'Associé Unique valide sans réserve le diagnostic posé par Monsieur Mohamed Coulibaly :"
    )
    pdf.para(
        "- Préservation de la disponibilité opérationnelle : Les directeurs de terrain (Monsieur Éric Koffi Yao pour la Technique "
        "et Madame Viviane Tanoh pour le Développement Commercial) doivent consacrer l'essentiel de leur énergie aux déploiements industriels "
        "et à la négociation de haut niveau. Une charge bureaucratique littéraire en fin de journée serait contre-productive."
    )
    pdf.para(
        "- Primauté de la donnée factuelle : L'objectif de la gouvernance à distance n'est pas d'accumuler des écrits de complaisance, "
        "mais de capter une métrique rigoureuse, standardisée et exploitable immédiatement par les outils d'analyse et d'audit."
    )

    pdf.titre1("2. Matrice standardisée des indicateurs clés (KPIs) par pôle")
    pdf.para(
        "En conséquence, le reporting journalier de chaque pôle sera constitué exclusivement d'une matrice standardisée "
        "de 5 indicateurs clés chiffrés, complétée par 3 à 5 puces factuelles (temps de remplissage n'excédant pas 10 minutes) :"
    )
    pdf.para(
        "A. Direction Technique (Monsieur Éric Koffi Yao) :\n"
        "1. Nombre d'audits techniques et relevés de toiture réalisés dans la journée.\n"
        "2. Nombre de chantiers de pose ou de raccordement actifs.\n"
        "3. Puissance crête cumulée installée et raccordée (en kWc).\n"
        "4. Avaries, incidents techniques ou alertes approvisionnement matériel (oui/non et résumé).\n"
        "5. Taux de respect du planning contractuel d'exécution (%).\n"
        "+ 3 à 5 puces synthétiques sur les événements techniques marquants."
    )
    pdf.para(
        "B. Direction Commerciale (Madame Viviane Tanoh) :\n"
        "1. Nombre de rendez-vous de prospection B2B industriels qualifiés menés.\n"
        "2. Nombre d'études de faisabilité et d'offres contractuelles PPA remises.\n"
        "3. Nombre de contrats PPA ou de baux solaires signés dans la journée.\n"
        "4. Volume de chiffre d'affaires prévisionnel récurrent contractualisé.\n"
        "5. Blocages commerciaux, retards de closing ou objections tarifaires rencontrées.\n"
        "+ 3 à 5 puces synthétiques sur la dynamique du pipe commercial."
    )
    pdf.para(
        "C. Direction Administrative et Financière (Madame Mariam Brou) :\n"
        "1. Solde disponible en fin de journée sur les comptes bancaires de la société (SGCI).\n"
        "2. Montant total des décaissements opérationnels exécutés.\n"
        "3. Encaissements constatés sur facturation PPA ou redevances.\n"
        "4. Alertes sur dérives budgétaires, créances échues ou retards de paiement client.\n"
        "5. Statut des déclarations fiscales, sociales et conformité administrative.\n"
        "+ 3 à 5 puces synthétiques sur la gestion financière et administrative."
    )

    pdf.titre1("3. Consolidation, traitement automatisé et filtre d'alerte rouge")
    pdf.para(
        "- Consolidation journalière : Monsieur Mohamed Coulibaly assure la compilation quotidienne de ces trois fiches sous format "
        "standardisé et l'expédie chaque soir ouvrable à l'adresse de direction (direction@soleil-b2b.ci)."
    )
    pdf.para(
        "- Traitement et revue de fond : L'équipe d'audit virtuelle assure l'archivage, la compilation statistique et le recoupement "
        "bancaire. L'Associé Unique consacrera sa séance de travail de fin de semaine à l'examen de cette trajectoire consolidée."
    )
    pdf.para(
        "- Alerte rouge immédiate : Le dispositif d'escalade immédiate par notification prioritaire reste sanctuarisé pour tout impayé > 15 jours, "
        "tout arrêt critique d'installation ou tout risque réglementaire ou judiciaire imminent."
    )

    fichier = chemin("documents_william", "2041-08-17_Validation_Format_Reporting_Agile_KPIs.pdf")
    pdf.sauver(fichier)
    print(f"Généré : {fichier}")


if __name__ == "__main__":
    generer_validation_reporting_kpis()
