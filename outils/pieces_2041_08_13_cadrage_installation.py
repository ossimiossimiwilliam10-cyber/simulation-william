"""
Génération de l'Étude de Cadrage Budgétaire : Installation du Siège (QG), Équipements et Prêt d'Associé
Mardi 13 août 2041 — Tour n° 82
Document de contre-expertise financière préparé par le Pôle Financier Virtuel
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_cadrage_installation():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Pôle Financier Virtuel",
        "Étude de Cadrage Budgétaire : Implantation du Siège (QG), Équipements et Financement en Compte Courant",
        auteur="Pôle Financier & Stratégie Virtuel",
        pied="Cadrage Budgétaire Installation & Compte Courant — SOLEIL B2B CI — 13/08/2041"
    )

    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Rédacteur", "Pôle Financier Virtuel — Application Gestion")
    pdf.meta("Date d'établissement", "Mardi 13 août 2041, 15h00 (heure d'Abidjan)")
    pdf.meta("Objet", "Chiffrage prévisionnel CAPEX d'installation, intendance/cantine, et doctrine de remboursement du compte courant d'associé")
    pdf.ln(3)

    pdf.titre1("1. Synthèse des orientations stratégiques de l'Associé Unique")
    pdf.para(
        "Lors de la séance de cadrage tenue ce 13 août 2041 au Plateau avec le Directeur Général Mohamed Coulibaly et "
        "la Directrice Administrative et Financière Mariam Brou, l'Associé Unique a arrêté les directives fondatrices "
        "relatives à l'installation matérielle et humaine de SOLEIL B2B CÔTE D'IVOIRE :"
    )
    pdf.puces([
        "Espaces de travail par direction : Bureaux distincts et spacieux pour chaque pôle (Direction Générale, Commerciale, Technique, DAF), dimensionnés pour accueillir les équipiers de niveaux 3 et 4 ;",
        "Climatisation intégrale et ergonomie : Climatisation performante obligatoire dans l'ensemble des locaux pour garantir des conditions de travail optimales face aux chaleurs équatoriales ;",
        "Renonciation à un bureau actionnaire : Pas d'espace privatif dédié à l'Associé Unique, présent par intermittence à Abidjan, optimisant ainsi les mètres carrés opérationnels ;",
        "Volet social et cantine d'entreprise : Aménagement d'un réfectoire commun servant de cantine le midi pour les salariés (prioritairement les jeunes recrues de niveau 4), approvisionné en repas équilibrés et boissons saines ;",
        "Personnel d'intendance et sécurité : Recrutement direct d'une employée d'entretien polyvalente (ménage et intendance cantine) et d'un gardien de site à temps plein ;",
        "Pharmacie de premiers secours : Mise à disposition d'une armoire médicale approvisionnée en antalgiques de base (paracétamol, ibuprofène) et soins d'urgence ;",
        "Flotte automobile : Acquisition prioritaire d'un véhicule technique tout-terrain / utilitaire pour les chantiers et l'outillage de la Direction Technique ; budget déplacement au réel pour les autres pôles ;",
        "Parc informatique et mobilier : Dotation complète en mobilier ergonomique et postes informatiques (PC portables et fixes selon la criticité des postes), négociés en volume ;",
        "Compte bancaire d'entreprise et avance remboursable : Ouverture immédiate du compte institutionnel et injection des capitaux sous forme de prêt en compte courant d'associé bloqué/conventionné, remboursé en priorité absolue sur les dividendes."
    ])

    pdf.titre1("2. Grille budgétaire prévisionnelle des investissements d'installation (CAPEX)")
    pdf.para(
        "Pour permettre à l'Associé Unique d'analyser les futurs devis de Mohamed Coulibaly et Mariam Brou avec des repères objectifs, "
        "le pôle financier virtuel a modélisé l'enveloppe d'installation initiale à Abidjan :"
    )

    entetes = ["Poste d'investissement", "Détail opérationnel", "Montant estimé (FCFA)", "Équivalent (EUR)"]
    lignes = [
        ["Bail villa QG (Garantie & avance)", "Caution 3 mois + 2 mois d'avance (loyer 1,8 M FCFA)", "9 000 000 FCFA", "13 720 €"],
        ["Climatisation & aménagement", "8 climatiseurs split Inverter, cloisons, câblage", "6 500 000 FCFA", "9 910 €"],
        ["Mobilier de bureau & cantine", "Bureaux, sièges ergonomiques, rangements, tables", "4 800 000 FCFA", "7 320 €"],
        ["Parc informatique & réseau", "10 PC portables pros, 4 PC fixes, NAS, switches, 2 fibres", "8 500 000 FCFA", "12 960 €"],
        ["Mobilité technique (Véhicule)", "Pickup utilitaire d'occasion récente révisé (Direction Technique)", "11 000 000 FCFA", "16 770 €"],
        ["Outillage & pharmacie", "Mesure solaire, pyranomètre, outillage atelier, armoire soins", "3 200 000 FCFA", "4 880 €"],
        ["Total CAPEX d'installation", "Enveloppe globale prévisionnelle d'amorçage matériel", "43 000 000 FCFA", "65 560 €"]
    ]
    pdf.tableau(entetes, lignes, [45, 70, 42, 33])

    pdf.titre1("3. Budget récurrent d'intendance, cantine et sécurité (OPEX mensuel)")
    pdf.para(
        "L'engagement social de fournir un cadre de travail soigné et un repas méridien équilibré génère une charge fixe mensuelle "
        "particulièrement rentable en termes d'engagement, de ponctualité et de rétention des talents :"
    )
    pdf.puces([
        "Employée polyvalente intendance & entretien : Salaire net de 180 000 FCFA/mois (environ 274 €) + charges sociales CNPS ;",
        "Gardiennage du site : Salaire net de 150 000 FCFA/mois (environ 229 €) + charges ;",
        "Ravitaillement cantine d'entreprise : Budget vivres et boissons saines pour 12 à 15 personnes (déjeuners ouvrés) estimé à 450 000 FCFA/mois (environ 686 €), soit environ 1 500 FCFA par repas par collaborateur ;",
        "Total mensuel charges sociales d'accueil : Environ 900 000 à 950 000 FCFA/mois (1 370 à 1 450 €/mois)."
    ])

    pdf.titre1("4. Mécanisme juridique et financier du Compte Courant d'Associé (CCA)")
    pdf.para(
        "Le choix de l'Associé Unique de financer ces investissements par une avance personnelle remboursable plutôt que par une augmentation "
        "de capital social présente des avantages financiers et juridiques déterminants en droit OHADA :"
    )
    pdf.puces([
        "Souplesse et étanchéité : L'apport en compte courant d'associé est constaté par une convention d'avance passée entre William Ossimi et la société, approuvée dans les décisions souveraines. Le capital social de 1 000 000 FCFA reste inchangé ;",
        "Priorité absolue de remboursement : La convention prévoira expressément que 100 % des flux de trésorerie disponible nets d'impôt seront affectés au remboursement du principal du compte courant jusqu'à apurement complet, avant toute mise en distribution de dividendes ;",
        "Avantage fiscal majeur : Le remboursement du compte courant constitue un remboursement de créance personnelle. Il est donc totalement exonéré de l'Impôt sur le Revenu des Valeurs Mobilières (IRVM au taux de 15 %), contrairement aux dividendes."
    ])

    pdf.titre1("5. Architecture de régulation souveraine des futurs dividendes")
    pdf.para(
        "Pour préserver la société de tout risque de décapitalisation, l'équipe virtuelle propose de paramétrer dans l'application Gestion "
        "un algorithme de distribution sous condition, activable dès la phase de rentabilité :"
    )
    pdf.puces([
        "Verrou 1 (Apurement de la dette) : Zéro dividende tant que le compte courant d'associé d'installation n'est pas soldé à 100 % ;",
        "Verrou 2 (Matelas de sécurité opérationnelle) : Maintien obligatoire d'une trésorerie résiduelle équivalente à au moins 6 mois de charges fixes d'exploitation (salaires, loyer villa, assurances) ;",
        "Verrou 3 (Ratio d'autonomie financière) : Dette financière nette inférieure à 2 fois l'excédent brut d'exploitation (EBE)."
    ])

    fichier_pdf = RACINE / "documents_william" / "2041-08-13_Cadrage_Budgetaire_Investissement_Installation_QG_et_Equipements.pdf"
    pdf.output(str(fichier_pdf))
    print(f"PDF généré : {fichier_pdf}")


if __name__ == "__main__":
    generer_cadrage_installation()
