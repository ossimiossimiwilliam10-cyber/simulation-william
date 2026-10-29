"""
Génération des pièces officielles du vendredi 16 août 2041, 15h30 (Tour n° 97) :
1. Avis d'opéré bancaire Spuerkeess S-Net : Virement prêt d'associé CCA de 8 000 EUR
2. Courriel officiel de Mohamed Coulibaly : Confirmation signature bail Vallons, remise des clés et recadrage Analyste Quantitatif
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_avis_virement_spuerkeess():
    pdf = DocPDF(
        "BANQUE ET CAISSE D'ÉPARGNE DE L'ÉTAT, LUXEMBOURG (SPUERKEESS)",
        "Avis d'Opéré — Virement International Sortant (S-Net Pro / Particulier)",
        auteur="Spuerkeess — Service des Opérations Internationales",
        pied="Avis d'Opéré Virement CCA — Spuerkeess S-Net — 16/08/2041"
    )

    pdf.meta("Émetteur", "Banque et Caisse d'Épargne de l'État, Luxembourg (BCEE / Spuerkeess)")
    pdf.meta("Donneur d'ordre", "Monsieur William Ossimi")
    pdf.meta("Compte débité", "Compte Courant Zebra Premium — LU28 0019 4006 4472 0000")
    pdf.meta("Date et heure d'exécution", "Vendredi 16 août 2041, 13h55 (heure Luxembourg / 11h55 UTC)")
    pdf.meta("Référence transaction", "TRANS-BCEE-20410816-CCA-08000")
    pdf.meta("Canal d'authentification", "S-Net Mobile — LuxTrust Mobile 2FA (Validé)")
    pdf.ln(3)

    pdf.titre1("1. Détail de l'opération de transfert international")
    pdf.para(
        "Nous vous confirmons l'exécution irrévocable de l'ordre de virement international transmis par vos soins "
        "via votre application bancaire sécurisée S-Net, selon les caractéristiques ci-dessous :"
    )

    entetes_op = ["Paramètre de l'ordre", "Valeur enregistrée"]
    lignes_op = [
        ["Montant débité", "8 000,00 EUR"],
        ["Frais de transfert international", "0,00 EUR (Package Zebra Premium inclus)"],
        ["Date de valeur débit", "16 août 2041"],
        ["Taux de change appliqué", "1 EUR = 655,957 XOF (parité fixe légale UEMOA)"],
        ["Contrevaleur brute créditée", "5 247 656 FCFA (arrondi d'usage : 5 250 000 FCFA)"],
        ["Bénéficiaire", "SOLEIL B2B CÔTE D'IVOIRE SASU"],
        ["Établissement destinataire", "Société Générale Côte d'Ivoire (SGCI) — Agence Plateau, Abidjan"],
        ["IBAN du bénéficiaire", "CI93 CI00 8010 0501 2045 8971 0283"],
        ["Code BIC / SWIFT destinataire", "SGCB CI AB"],
        ["Motif économique déclaré", "Apport en compte courant d'associé (CCA) — Démarrage trésorerie exploitation"],
        ["Référence interne de l'associé", "CCA-20410816-OSSIMI-01"]
    ]
    pdf.tableau(entetes_op, lignes_op, [70, 120])

    pdf.ln(3)
    pdf.titre1("2. Certificat de conformité et traçabilité réglementaire")
    pdf.para(
        "La présente opération a été exécutée sous le protocole de transfert SWIFT GPI (Global Payments Innovation). "
        "Les fonds sont acheminés directement vers la banque correspondante en Côte d'Ivoire. Conformément aux dispositions "
        "de la convention de compte courant d'associé de SOLEIL B2B CÔTE D'IVOIRE SASU, cette créance financière constitue un prêt "
        "d'associé remboursable prioritairement sur les flux de trésorerie disponibles de l'entreprise avant toute distribution de dividende."
    )

    sortie = chemin("documents_william", "2041-08-16_Ordre_Virement_Spuerkeess_CCA_Soleil_B2B_CI.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


def generer_courriel_signature_bail_coulibaly():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Compte-Rendu Signature Bail Vallons & Confirmation Analyste Quantitatif",
        auteur="Mohamed Coulibaly",
        pied="Signature Bail Vallons & Analyste Quantitatif — SOLEIL B2B CI — 16/08/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly, Directeur Général (m.coulibaly@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Vendredi 16 août 2041, 15h35 (heure d'Abidjan)")
    pdf.meta("Objet", "Compte-rendu de la signature du bail commercial de la villa des Vallons, remise des clés et recadrage Analyste Quantitatif")
    pdf.ln(3)

    pdf.titre1("1. Recadrage immédiat : Intégration de l'Analyste Quantitatif (Risk Analyst)")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "J'ai bien reçu votre message d'observation concernant l'absence de mention explicite de l'Analyste Quantitatif dans ma précédente note. "
        "Vous avez parfaitement raison de me rappeler à cette exigence cardinale, et je vous prie d'excuser cette omission dans ma synthèse rapide. "
        "L'intégration de l'Analyste Quantitatif (Risk Analyst Niveau 3/4 rattaché à la DAF Mariam Brou avec double ligne de reporting vers vous) "
        "demeure gravée dans le marbre de notre doctrine de gouvernance validée le 9 août."
    )
    pdf.para(
        "J'ai immédiatement rectifié le plan de cadrage de Mariam Brou : elle a pour instruction formelle de lancer dès la rentrée de septembre "
        "le sourcing d'un profil d'excellence en modélisation financière et analyse de risque (ingénieur ou master en statistiques/finance quantitative, "
        "idéalement issu de la filière Data/Finances de l'INP-HB Yamoussoukro). Ce collaborateur aura la charge exclusive de modéliser les risques de contrepartie, "
        "d'auditer la rentabilité des offres solaires et d'assurer le calcul en temps réel de notre burn rate."
    )

    pdf.titre1("2. Signature officielle du bail commercial de la Villa des Vallons")
    pdf.para(
        "J'ai l'immense honneur de vous confirmer que la séance de signature du bail commercial s'est tenue ce jour entre 14h00 et 15h20 "
        "en présence du représentant du propriétaire bailleur et du gestionnaire de patrimoine de l'agence immobilière des Vallons."
    )
    pdf.para(
        "Les termes arrêtés sont rigoureusement conformes à nos négociations préalables :\n"
        "• Objet du bail : Villa duplex de standing (7 pièces, jardin clos, garage sécurisé 4 véhicules) sise à Cocody Deux-Plateaux Vallons ;\n"
        "• Destination des lieux : Siège social, bureaux de direction, salle de téléprésence et base technique opérationnelle ;\n"
        "• Loyer mensuel : 1 750 000 FCFA net de charges ;\n"
        "• Franchise gracieuse d'aménagement : 15 jours accordés sans facturation (prise d'effet locative au 1er septembre 2041) ;\n"
        "• Dépôt de garantie et premier loyer : Règlement différé convenu en début de semaine prochaine, dès compensation de votre virement d'associé sur notre compte SGCI."
    )

    pdf.titre1("3. État des lieux contradictoire et remise effective des clés")
    pdf.para(
        "L'état des lieux d'entrée a été conduit minutieusement pièce par pièce. Les points névralgiques ont été validés sans réserve :\n"
        "• Groupe électrogène de secours de 45 kVA en état de fonctionnement nominal (test de démarrage concluant) ;\n"
        "• Système de climatisation centralisé et splits individuels testés et révisés ;\n"
        "• Compteur électrique CIE triphasé haute puissance opérationnel ;\n"
        "• Toiture-terrasse parfaitement saine et dégagée, confirmée apte à recevoir notre installation photovoltaïque pilote de 10 kWc."
    )
    pdf.para(
        "Le trousseau complet des clés de la villa ainsi que les télécommandes du portail motorisé m'ont été officiellement remis à 15h25. "
        "Le siège de SOLEIL B2B CÔTE D'IVOIRE est désormais une réalité physique à Abidjan."
    )

    sortie = chemin("courriels", "2041-08-16_Courriel_Mohamed_Coulibaly_Compte_Rendu_Signature_Bail_Vallons_et_Remise_Cles.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_avis_virement_spuerkeess()
    generer_courriel_signature_bail_coulibaly()
