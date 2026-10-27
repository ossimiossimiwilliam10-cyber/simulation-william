"""PIÈCES DU 24/07/2041 (univers 3, tour n° 48) :
1. Convention d'honoraires et dossier KYC du Cabinet Me Ismaël Gnamien (reçu par courriel professionnel le 24/07/2041) ;
2. Rapport quotidien du Directeur Général virtuel (24 juillet 2041, 20h00).

Génération des fichiers PDF physiques (règle 4 et directives de William)
déposés dans `courriels/` et `documents_william/` et référencés dans l'application Gestion / Téléphone.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_lettre_mission_gnamien():
    pdf = DocPDF(
        "Cabinet d'Avocats Ismaël Gnamien & Associés — Abidjan",
        "Convention d'assistance juridique & Questionnaire d'identification client (KYC)",
        auteur="Cabinet Me Ismaël Gnamien (Abidjan)",
        pied="Cabinet Gnamien & Associés — Convention d'honoraires SAS Solaire B2B"
    )

    pdf.meta("Émetteur", "Cabinet Me Ismaël Gnamien & Associés, Avocat à la Cour, Barreau d'Abidjan (Cocody)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique / Investisseur (Projet Solaire B2B Abidjan)")
    pdf.meta("Date", "Mercredi 24 juillet 2041")
    pdf.meta("Objet", "Constitution d'une Société par Actions Simplifiée (SAS) & Formalités de constitution")
    pdf.ln(3)

    pdf.titre1("1. Objet et périmètre de la mission d'assistance juridique")
    pdf.para(
        "Par la présente convention d'honoraires, le Cabinet d'Avocats Ismaël Gnamien & Associés est formellement missionné par "
        "Monsieur William Ossimi afin d'assurer l'ensemble des diligences juridiques, administratives et fiscales relatives à la "
        "création, l'immatriculation et l'implantation opérationnelle de la société Projet Solaire B2B Abidjan SAS :"
    )
    pdf.puces([
        "Rédaction personnalisée des Statuts de la Société par Actions Simplifiée (SAS) régie par l'Acte Uniforme OHADA, "
        "intégrant les clauses de gouvernance stricte de l'associé unique investisseur ;",
        "Rédaction du Pacte d'Associés et des règles de gouvernance des organes de direction ;",
        "Formalisation définitive et enregistrement de la Convention de Mandat Social du Directeur Général réel (droit OHADA) ;",
        "Dépôt du capital social initial auprès d'une banque partenaire agréée à Abidjan et obtention de la Déclaration Notariée de Souscription et de Versement (DNSV) ;",
        "Accomplissement des formalités de dépôt et d'immatriculation au Registre du Commerce et du Crédit Mobilier (RCCM) auprès du Guichet Unique du CEPICI ;",
        "Déclaration Fiscale d'Existence (DFE) et obtention du Numéro d'Identifiant Fiscal Unique (NCI/NCC) ;",
        "Publication de l'avis de constitution au Journal Officiel de Côte d'Ivoire et dans un journal d'annonces légales agréé."
    ])

    pdf.titre1("2. Honoraires et modalités de règlement échelonné")
    pdf.para(
        "Conformément au devis formellement accepté le 22 juillet 2041, les honoraires du Cabinet pour la mission complète s'établissent "
        "au forfait ferme et définitif de 2 100 000 FCFA Hors Taxes (soit environ 3 200 € HT), hors débours administratifs légaux "
        "(droits de timbre, enregistrement et frais de greffe CEPICI facturés sur justificatifs réels)."
    )
    pdf.para(
        "Le règlement s'effectue par virement bancaire échelonné selon le calendrier suivant :"
    )
    pdf.puces([
        "Premier acompte (40 %) : 840 000 FCFA HT (soit 991 200 FCFA TTC avec TVA 18 %, ≈ 1 511 €), exigible à la signature de la présente convention pour ouverture du dossier et engagement de la rédaction des statuts ;",
        "Deuxième acompte (40 %) : 840 000 FCFA HT (991 200 FCFA TTC), exigible lors du dépôt du dossier complet d'immatriculation au greffe du CEPICI ;",
        "Solde final (20 %) : 420 000 FCFA HT (495 600 FCFA TTC), exigible à la remise de l'extrait RCCM officiel, du registre fiscal et des statuts enregistrés."
    ])

    pdf.titre1("3. Procédure d'identification client (KYC — Conformité légale)")
    pdf.para(
        "En application des dispositions légales ivoiriennes et internationales relatives à la prévention du blanchiment de capitaux "
        "et du financement du terrorisme (règlementation CENTIF / UEMOA), le Cabinet est tenu d'établir la fiche d'identification complète de l'investisseur :"
    )
    pdf.puces([
        "Identité du client : William Ossimi, enseignant de la fonction publique luxembourgeoise, domicilié à Audun-le-Tiche ;",
        "Régime juridique : Associé unique non-gérant, investisseur en fonds propres, sans fonction de direction opérationnelle locale, en stricte conformité avec l'article 14 du statut général des fonctionnaires de l'État luxembourgeois ;",
        "Origine des fonds investis : Épargne personnelle licite issue des traitements et revenus réguliers perçus au Grand-Duché de Luxembourg ;",
        "Pièces justificatives à transmettre sous pli numérique sécurisé : copie certifiée conforme du passeport en cours de validité et justificatif de domicile récent (facture d'électricité ou avis d'imposition de moins de trois mois)."
    ])

    pdf.titre1("4. Signature et validation des engagements")
    pdf.para(
        "Fait à Abidjan, le 24 juillet 2041. Pour le Cabinet d'Avocats : Me Ismaël Gnamien. Document transmis pour accord, "
        "signature et retour des pièces requises."
    )

    fichier_sortie = chemin("courriels", "2041-07-24_Cabinet_Gnamien_Convention_d_honoraires_et_KYC.pdf")
    pdf.sauver(fichier_sortie)
    return fichier_sortie


def generer_rapport_quotidien_24():
    pdf = DocPDF(
        "Rapport quotidien d'activité — Direction Générale virtuelle",
        "Mercredi 24 juillet 2041 · 20h00 (heure de Luxembourg / 18h00 Abidjan)",
        auteur="Directeur Général virtuel",
        pied="Projet Solaire B2B Abidjan — Rapport d'activité du 24/07/2041"
    )

    pdf.meta("Émetteur", "Directeur Général virtuel (Pôle Central / Architecture IA)")
    pdf.meta("Destinataire", "William Ossimi, Associé unique et investisseur")
    pdf.meta("Date et heure", "Mercredi 24 juillet 2041, 20h00")
    pdf.meta("Objet", "Rapport d'étape : réception de la convention d'avocat, avancement RH et situation générale")
    pdf.ln(3)

    pdf.titre1("1. Synthèse de la journée du 24 juillet 2041")
    pdf.para(
        "La journée a été marquée par l'arrivée de la convention d'honoraires formalisée et du dossier KYC transmis par le Cabinet de "
        "Me Ismaël Gnamien à Abidjan, ainsi que par la poursuite des diligences de vérification des références de candidatures de "
        "Direction Générale par le pôle RH."
    )

    pdf.titre1("2. Pôle Juridique : Validation de la convention d'honoraires de Me Gnamien")
    pdf.para(
        "Le document officiel transmis par Me Gnamien (reçu à 11h45) a été intégralement passé en revue par le pôle juridique virtuel :"
    )
    pdf.puces([
        "Conformité financière : Le forfait convenu de 2 100 000 FCFA HT est scrupuleusement respecté, sans surfacturation cachée. L'échelonnement (40 % à la commande, 40 % au dépôt CEPICI, 20 % à la remise de l'extrait RCCM) est parfaitement équilibré.",
        "Sécurisation statutaire : Le périmètre couvre explicitement la rédaction sur-mesure des statuts SAS, du pacte d'associés, des formalités fiscales, et l'enregistrement officiel de la convention de mandat social du DG arrêtée par William.",
        "Conformité KYC et statut luxembourgeois : La fiche KYC mentionne expressément la qualité d'associé unique non-gérant de William, garantissant l'étanchéité absolue vis-à-vis de l'article 14 du statut de la fonction publique luxembourgeoise.",
        "Décision attendue : William peut valider la convention et transmettre les deux pièces justificatives (passeport et justificatif de domicile) pour déclenchement de la rédaction des statuts."
    ])

    pdf.titre1("3. Pôle Ressources Humaines : Recrutement de la Direction Générale")
    pdf.para(
        "Le traitement des retours d'évaluation auprès des anciens employeurs et pairs de Mohamed Coulibaly (91/100) et Mariam Brou (88/100) "
        "se poursuit rigoureusement :"
    )
    pdf.puces([
        "Mohamed Coulibaly (note 91/100) : Les retours d'un ancien directeur de projet confirment son très haut niveau d'expertise technique, sa rigueur financière et sa probité managériale. Le pôle RH finalise la synthèse comparative.",
        "Mariam Brou (note 88/100) : Retours d'évaluation commerciale très positifs sur sa capacité de pénétration des comptes industriels B2B.",
        "Kader Assi (note 84/100) : Dossier complet maintenu en position d'excellence.",
        "Jean-Baptiste Tuo (note 71/100) : Dossier clos et archivé en réserve active suite à son accusé de réception courtois d'hier soir."
    ])

    pdf.titre1("4. Consommation d'API et budget du segment virtuel")
    pdf.para(
        "La consommation d'API pour les analyses du pôle juridique virtuel et le suivi de surveillance s'établit à 1,20 € pour la "
        "journée, portant le cumul mensuel à 39,56 € sur le plafond de 1 000,00 € (solde disponible : 960,44 € pour juillet 2041)."
    )

    fichier_sortie = chemin("documents_william", "2041-07-24_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(fichier_sortie)
    return fichier_sortie


if __name__ == "__main__":
    f1 = generer_lettre_mission_gnamien()
    f2 = generer_rapport_quotidien_24()
    print("2 pièces générées avec succès.")

