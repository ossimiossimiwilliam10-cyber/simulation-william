"""Génération de la grille d'audit solaire et préparation de visio de William (18/07/2041)."""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer():
    pdf = DocPDF(
        titre="GRILLE D'AUDIT & PRÉPARATION VISIO",
        sous_titre="Projets Solaires Geração Distribuída (Brésil) — Entretien Thiago Rocha du 19/07/2041",
        auteur="William Ossimi",
        pied="William Ossimi · Dossier d'investissement personnel"
    )

    pdf.meta("Date", "18 juillet 2041 (Audun-le-Tiche)")
    pdf.meta("Auteur", "William Ossimi (36 ans)")
    pdf.meta("Objet", "Grille de Due Diligence et questions préalables pour entretien visio avec Thiago Rocha")
    pdf.ln(3)

    pdf.titre1("1. Cadrage Réglementaire & Modèle Économique (Minas Gerais)")
    pdf.para(
        "L'investissement ciblé s'inscrit dans le cadre de la loi brésilienne n° 14.300 (Marco Legal da Geração Distribuída). "
        "Le modèle d'exploitation repose sur la location de parcs photovoltaïques au sol (75 kW à 300 kW) à des entreprises "
        "commerciales ou industrielles locales, permettant à ces dernières d'effacer une partie de leur facture d'électricité "
        "via le mécanisme de compensation de crédits énergétiques de la concessionnaire Cemig (Companhia Energética de Minas Gerais)."
    )
    pdf.para(
        "Le Minas Gerais présente un atout déterminant : un niveau d'irradiation solaire exceptionnel (> 2 100 kWh/m²/an) "
        "et un régime fiscal favorable (exonération d'ICMS sur l'énergie compensée). Les rendements bruts anticipés oscillent "
        "entre 13 % et 17 % par an, avant provision pour dépréciation et impôt sur les sociétés (Lucro Presumido)."
    )

    pdf.titre1("2. Sécurité Statutaire de l'Investisseur (Article 14)")
    pdf.para(
        "En tant qu'enseignant fonctionnaire d'État au Luxembourg, la préservation intégrale du statut et du traitement "
        "mensuel net de 9 320 € constitue une contrainte non négociable. Le montage juridique impératif est le suivant :"
    )
    pdf.puces([
        "Forme sociétaire brésilienne : Sociedade de Propósito Específico (SPE) sous statut de Sociedade Limitada (Ltda).",
        "Qualité de William : Associé détenteur de quotas de capital (investisseur passif/commanditaire), sans mandat social.",
        "Administration opérationnelle : Gérance et représentation légale confiées intégralement à un administrateur résident brésilien.",
        "Conformité statutaire : Aucune démarche commerciale active exercée par William, 100 % de conformité avec l'Article 14."
    ])

    pdf.titre1("3. Tableau d'Évaluation des Risques de Due Diligence")

    entetes = ["Pilier d'audit", "Point critique de contrôle", "Risque identifié", "Parade exigée"]
    lignes = [
        ["1. Raccordement", "Parecer de Acesso Cemig", "Retard ou refus de connexion", "Exiger le document final signé Cemig"],
        ["2. Foncier", "Bail notarié (Arrendamento)", "Litige de propriété / servitudes", "Bail de 20 ans + servitude enregistrée"],
        ["3. Matériel EPC", "Panneaux TIER-1 / Onduleurs", "Sous-performance / pannes", "Garantie matériel 12 ans + perf. 25 ans"],
        ["4. Off-taker", "Solvabilité du preneur", "Défaut de paiement de la location", "Caution bancaire ou dépôt de 3 mois"],
        ["5. Change (BRL)", "Volatilité du Real brésilien", "Baisse de rendement en Euro", "Couverture partielle ou réinvestissement"]
    ]
    pdf.tableau(entetes, lignes, [35, 45, 48, 51], taille=8.0)

    pdf.titre1("4. Grille des 12 Questions Clés pour Thiago Rocha (Entretien du 19/07)")
    pdf.puces([
        "1. Quel est le statut exact d'approbation du Parecer de Acesso de la Cemig pour les centrales de 150 kW et 300 kW ?",
        "2. Le foncier est-il loué ou acheté par la SPE ? Quelle est la durée exacte et le montant indexé du bail notarié ?",
        "3. Quelles marques et fabricants (modules TIER-1, onduleurs Huawei ou Sungrow) sont spécifiés dans le devis EPC ?",
        "4. L'installateur offre-t-il un contrat d'exploitation et maintenance (O&M) avec engagement de disponibilité (au moins 98 %) ?",
        "5. Quel est le modèle contractuel avec le client final (locataire de l'actif ou adhérent à un consortium de consommation) ?",
        "6. Quelle est la durée du contrat de location d'énergie (5 ans, 10 ans) et quel est le préavis de résiliation ?",
        "7. Quel est le profil financier et la solvabilité de l'off-taker pressenti ?",
        "8. Quel est le montant global de l'investissement (CAPEX) requis par kWc installé (ratio R$/kWc) ?",
        "9. Quelle est la part de fonds propres (equity) demandée à l'investisseur et quel est le montant d'éventuelle dette bancaire ?",
        "10. Quel est le taux de rendement interne (TRI / TIR) projeté en Real brésilien (BRL) sur 15 ans et 20 ans ?",
        "11. Comment est structurée la rémunération du développeur (honoraires au succès, part dans la SPE, marge EPC) ?",
        "12. La structure de gouvernance permet-elle formellement la détention passive sans engagement de gestion pour un non-résident ?"
    ])

    cible = RACINE / "documents_william" / "2041-07-18_Grille_Audit_Solaire_Bresil_Thiago_Rocha.pdf"
    cible.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(cible))
    print(f"PDF écrit : {chemin(cible)}")


if __name__ == "__main__":
    generer()
