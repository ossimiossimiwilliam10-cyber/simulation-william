"""Génération du rapport d'étude prospective IA de William (16/07/2041)."""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer():
    pdf = DocPDF(
        titre="ÉTUDE PROSPECTIVE & CADRAGE JURIDIQUE",
        sous_titre="Opportunités d'Investissement International & Article 14 du Statut Général — 16 Juillet 2041",
        auteur="William Ossimi",
        pied="William Ossimi · Dossier d'analyse personnelle"
    )

    pdf.meta("Date", "16 juillet 2041 (Audun-le-Tiche)")
    pdf.meta("Auteur", "William Ossimi (36 ans)")
    pdf.meta("Objet", "Analyse sectorielle (CI, BR, PH) et véhicule d'investissement pour fonctionnaire")
    pdf.ln(3)

    pdf.titre1("1. Synthèse Décisionnelle & Véhicule Juridique (Article 14)")
    pdf.para(
        "En tant que professeur fonctionnaire d'État au Luxembourg (traitement net mensuel lissé de 9 320 €), "
        "toute prise de participation doit strictement respecter l'article 14 du statut général des fonctionnaires. "
        "L'article 14 interdit formellement d'exercer une profession commerciale ou industrielle à titre principal."
    )
    pdf.para(
        "Le montage retenu est celui d'ASSOCIÉ OU INVESTISSEUR PASSIF NON-GÉRANT : la simple détention de parts de capital, "
        "d'actions ou de titres financiers ne constitue pas une activité commerciale ou industrielle prohibée, dès lors "
        "qu'aucun mandat social de gestion (gérant, administrateur délégué, directeur général) n'est exercé. "
        "La direction opérationnelle est confiée à un partenaire opérateur local sur le terrain. "
        "Cette formule garantit un risque zéro pour le statut de fonctionnaire et protège intégralement le traitement d'État."
    )

    pdf.titre1("2. Analyse Comparative des Marchés Cibles")

    entetes = ["Critère", "Côte d'Ivoire", "Brésil", "Philippines"]
    lignes = [
        ["Secteurs clés", "Agro-industrie, Immo/Logistique", "Agritech, Énergies vertes", "BPO/KPO, Immo bureaux"],
        ["Ticket type", "25 000 € à 75 000 €", "30 000 € à 100 000 €", "20 000 € à 60 000 €"],
        ["Risque de change", "Nul (Parité fixe EUR/FCFA)", "Modéré à fort (BRL)", "Modéré (PHP / USD)"],
        ["Pilotage à distance", "Besoin d'un gérant local", "Complexité fiscale (Custo)", "Écosystème BPO anglophone"],
        ["Potentiel rendement", "12 % à 18 % brut annuel", "10 % à 15 % brut annuel", "11 % à 16 % brut annuel"]
    ]
    pdf.tableau(entetes, lignes, [35, 48, 48, 48], taille=8.5)

    pdf.titre1("3. Détail par Pays")

    pdf.para("A. Côte d'Ivoire (Zone Franc CFA / UEMOA) :", italique=True)
    pdf.puces([
        "Transformation agro-alimentaire locale : fort soutien gouvernemental pour passer de l'exportation brute à la valeur ajoutée locale (cacao, cajou, fruits séchés).",
        "Logistique et immobilier d'entreprise : déficit structurel à Abidjan et San Pedro en entrepôts sécurisés et immobilier d'activités.",
        "Atout majeur pour William : 1 € = 655,957 FCFA (parité fixe), garantissant une absence totale de perte de change lors des rapatriements de dividendes."
    ])

    pdf.para("B. Brésil :", italique=True)
    pdf.puces([
        "Agritech et intrants durables : marché gigantesque où les exploitations adoptent massivement les technologies d'agriculture de précision et bio-fertilisants.",
        "Énergies renouvelables : modèle de génération distribuée solaire dans le Nordeste offrant des contrats d'achat d'électricité stables.",
        "Contrainte : fiscalité brésilienne complexe et nécessité absolue d'un conseil juridique bilingue sur place."
    ])

    pdf.para("C. Philippines :", italique=True)
    pdf.puces([
        "IT-BPM & KPO de niche : externalisation de processus de connaissances (comptabilité analytique, développement tech, IA appliquée, support haut de gamme) facturés en USD/EUR.",
        "Immobilier de standing : forte demande de bureaux et résidences pour cadres à Bonifacio Global City (BGC) et Makati.",
        "Atout : main-d'œuvre anglophone à 100 % et cadre incitatif PEZA très protecteur pour les investisseurs étrangers."
    ])

    pdf.titre1("4. Prochaines Étapes Recommandées")
    pdf.puces([
        "Sélectionner le marché prioritaire selon l'appétence (Côte d'Ivoire pour la stabilité monétaire, Philippines pour le digital/BPO).",
        "Calibrer l'enveloppe de départ (ex: 25 000 € à 40 000 € issus de l'épargne liquide de sécurité de 75 250 €).",
        "Identifier et auditer un opérateur local fiable avant tout engagement de fonds."
    ])

    cible = chemin("documents_william", "2041-07-16_Etude_IA_Opportunites_Investissement.pdf")
    pdf.sauver(cible)


if __name__ == "__main__":
    generer()
