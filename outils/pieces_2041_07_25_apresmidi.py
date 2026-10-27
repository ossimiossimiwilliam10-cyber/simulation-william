"""PIÈCES DU 25/07/2041 APRÈS-MIDI (univers 3, tour n° 52) :
1. Ordre de virement bancaire SWIFT Spuerkeess de William vers le Cabinet Gnamien (1 511,00 €) ;
2. Courriel de transmission du justificatif bancaire envoyé à Me Gnamien ;
3. Courriel d'accusé de réception et confirmation de planning de Me Gnamien ;
4. Rapport quotidien n° 6 du Directeur Général virtuel (25 juillet 2041, 20h00).

Génération des fichiers PDF physiques (règle 4 et directives de William).
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_ordre_virement_spuerkeess():
    pdf = DocPDF(
        "Banque et Caisse d'Épargne de l'État, Luxembourg (Spuerkeess)",
        "Avis d'opéré — Ordre de virement international SWIFT",
        auteur="Spuerkeess Luxembourg",
        pied="Spuerkeess — Reçu d'exécution de virement international"
    )

    pdf.meta("Établissement émetteur", "Banque et Caisse d'Épargne de l'État, Luxembourg (BCEE / Spuerkeess)")
    pdf.meta("Titulaire du compte", "Monsieur William Ossimi, Résidence à Audun-le-Tiche")
    pdf.meta("Date et heure d'exécution", "Jeudi 25 juillet 2041, 12h30 (heure de Luxembourg)")
    pdf.meta("Référence de la transaction", "SWIFT-LU-20410725-88412097")
    pdf.ln(3)

    pdf.titre1("1. Détail de l'opération de virement international")
    pdf.para(
        "Nous vous confirmons l'exécution de l'ordre de virement international SWIFT conformément à vos instructions saisies "
        "sur votre espace sécurisé Spuerkeess (Package Zebra Premium) :"
    )

    pdf.tableau(
        ["Paramètre", "Donnée enregistrée"],
        [
            ["Compte donneur d'ordre", "LU78 0019 4006 4470 0000 (Compte courant privé William Ossimi)"],
            ["Montant débité", "1 511,00 EUR"],
            ["Frais bancaires d'émission", "0,00 EUR (exonération formule Zebra Premium)"],
            ["Date de valeur débit", "Jeudi 25 juillet 2041"],
            ["Banque bénéficiaire", "Banque Internationale pour le Commerce et l'Industrie de la Côte d'Ivoire (BICICI)"],
            ["Code BIC / SWIFT", "BICI CI AB (BICICI Plateau, Abidjan, Côte d'Ivoire)"],
            ["Compte bénéficiaire (IBAN)", "CI93 CI00 6010 0101 2345 6789 0145"],
            ["Nom du bénéficiaire", "SELAS Cabinet d'Avocats Ismaël Gnamien & Associés — Compte CARPA / Débours"],
            ["Contrevaleur créditée", "991 200 FCFA (taux officiel de parité fixe légale : 1 EUR = 655,957 FCFA)"],
            ["Motif du paiement / Libellé", "HONO-CI-2041-0722-OSSIMI"],
            ["Nature économique", "Paiement honoraires juridiques — Constitution société SAS"],
        ],
        largeurs=[65, 125]
    )

    pdf.titre1("2. Statut et acheminement du virement")
    pdf.para(
        "L'ordre de virement a été validé et télétransmis sur le réseau bancaire international SWIFT sous la référence "
        "d'acquittement MT103 numéro `BCEELUAXXX204107259012`. Les fonds sont mis à la disposition de la banque correspondante "
        "pour crédit du compte séquestre du bénéficiaire sous un délai de 24 à 48 heures ouvrées."
    )

    cible = chemin("documents_william", "2041-07-25_Ordre_de_virement_Spuerkeess_Cabinet_Gnamien.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")


def generer_courriel_envoi_justificatif():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Transmission Justificatif de Virement",
        "Notification au Cabinet d'Avocats Ismaël Gnamien & Associés · Abidjan (RCI)",
        auteur="William Ossimi, Associé Unique & Investisseur",
        pied="Projet Solaire B2B Abidjan — Transmission récépissé virement acompte"
    )

    pdf.meta("Émetteur", "Monsieur William Ossimi, Associé Unique et Investisseur (Audun-le-Tiche / Luxembourg)")
    pdf.meta("Destinataire", "Maître Ismaël Gnamien, Avocat à la Cour, Barreau d'Abidjan")
    pdf.meta("Date et heure", "Jeudi 25 juillet 2041, 12h35 (heure de Luxembourg / 10h35 Abidjan)")
    pdf.meta("Objet", "Dossier CI-2041-0722 : Transmission de l'avis d'opéré bancaire du premier acompte (1 511 €)")
    pdf.ln(3)

    pdf.titre1("1. Transmission de l'avis d'exécution du virement bancaire")
    pdf.para(
        "Maître,"
    )
    pdf.para(
        "Faisant suite à votre courriel de ce matin me transmettant les coordonnées bancaires officielles de votre cabinet, "
        "j'ai le plaisir de vous confirmer que l'ordre de virement international SWIFT d'un montant de 1 511,00 € (contrevaleur exacte "
        "de 991 200 FCFA TTC) a été émis ce jour à 12h30 depuis mon compte bancaire Spuerkeess au Luxembourg."
    )
    pdf.para(
        "Vous trouverez ci-joint l'avis d'opéré bancaire officiel mentionnant la référence convenue `HONO-CI-2041-0722-OSSIMI` "
        "à destination de votre compte séquestre CARPA ouvert auprès de la BICICI Agence Plateau Principale."
    )

    pdf.titre1("2. Confirmation du lancement des travaux de rédaction")
    pdf.para(
        "Conformément aux termes de votre convention d'honoraires, ce règlement libère l'engagement immédiat de la mission. "
        "Je prends acte du calendrier annoncé pour la transmission des projets définitifs des statuts de la SASU et du projet de "
        "convention de nomination du Directeur Général, attendus pour approbation au plus tard le lundi 29 juillet 2041."
    )
    pdf.para(
        "Restant à votre entière écoute pour toute précision utile, je vous prie d'agréer, Maître, l'expression de mes salutations distinguées."
    )
    pdf.para(
        "William Ossimi\nAssocié Unique et Fondateur"
    )

    cible = chemin("documents_william", "2041-07-25_Courriel_Cabinet_Gnamien_Transmission_justificatif_virement.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")


def generer_accuse_reception_gnamien():
    pdf = DocPDF(
        "Cabinet d'Avocats Ismaël Gnamien & Associés — Abidjan",
        "Accusé de réception de l'avis d'opéré bancaire & Confirmation d'engagement des statuts",
        auteur="Cabinet Me Ismaël Gnamien (Abidjan)",
        pied="Cabinet Gnamien & Associés — Suivi constitution SAS Projet Solaire B2B"
    )

    pdf.meta("Émetteur", "Cabinet Me Ismaël Gnamien & Associés, Avocat à la Cour, Barreau d'Abidjan")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique / Investisseur")
    pdf.meta("Date et heure", "Jeudi 25 juillet 2041, 13h45 (heure d'Abidjan / 15h45 Luxembourg)")
    pdf.meta("Objet", "Dossier CI-2041-0722 : Bonne réception du justificatif de virement et planning opérationnel")
    pdf.ln(3)

    pdf.titre1("1. Accusé de réception de l'avis de virement SWIFT")
    pdf.para(
        "Monsieur,"
    )
    pdf.para(
        "Nous accusons formellement réception de votre courriel de ce jour transmettant l'avis d'opéré bancaire officiel émis par "
        "la Spuerkeess pour le règlement du premier acompte de 1 511,00 € (991 200 FCFA TTC) sous la référence `HONO-CI-2041-0722-OSSIMI`."
    )
    pdf.para(
        "Notre service comptable suit l'imputation de ces fonds dès leur crédit effectif sur notre compte séquestre professionnel BICICI. "
        "Le justificatif d'émission SWIFT transmis permettant d'attester de l'engagement ferme des fonds, nous vous confirmons "
        "l'ouverture immédiate des travaux juridiques au sein de notre cellule droit des sociétés."
    )

    pdf.titre1("2. Planning opérationnel de finalisation des actes")
    pdf.puces([
        "Rédaction du projet complet des Statuts de la SASU Projet Solaire B2B Abidjan, intégrant l'associé unique investisseur ;",
        "Formalisation du Procès-Verbal des décisions de constitution et de la Convention de Mandat Social du Directeur Général ;",
        "Envoi des projets d'actes pour votre revue et validation le lundi 29 juillet 2041 en milieu de journée ;",
        "Préparation concomitante des imprimés officiels du CEPICI pour immatriculation au RCCM dès retour des actes approuvés."
    ])
    pdf.para(
        "Nous vous remercions de votre confiance et de votre réactivité exemplaire."
    )
    pdf.para(
        "Pour le Cabinet Gnamien & Associés,\nMaître Ismaël Gnamien, Avocat à la Cour"
    )

    cible = chemin("courriels", "2041-07-25_Cabinet_Gnamien_Accuse_reception_virement.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")


def generer_rapport_dg_25_juillet():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Direction Générale virtuelle",
        "Rapport d'activité quotidien n° 6 — Jeudi 25 juillet 2041 (20h00)",
        auteur="Directeur Général virtuel",
        pied="Projet Solaire B2B Abidjan — Rapport quotidien n° 6 du 25/07/2041"
    )

    pdf.meta("Émetteur", "Directeur Général virtuel (Coordination des pôles Juridique, RH, Technique, Commercial)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique et Investisseur")
    pdf.meta("Date et heure", "Jeudi 25 juillet 2041, 20h00 (heure de Luxembourg)")
    pdf.meta("Objet", "Bilan d'activité quotidien, suivi Me Gnamien, calage entretien DG et situation budgétaire")
    pdf.ln(3)

    pdf.titre1("1. Suivi juridique et constitution de la société (Cabinet Me Gnamien)")
    pdf.para(
        "La journée a été marquée par une avancée majeure dans la sécurisation juridique de la structure :"
    )
    pdf.puces([
        "Conformité KYC : Le cabinet Gnamien a validé l'intégralité du dossier d'identification de l'associé unique sans réserve ;",
        "Virement du premier acompte : L'ordre international SWIFT de 1 511,00 € a été émis à 12h30 (ref. HONO-CI-2041-0722-OSSIMI) ;",
        "Confirmation du Cabinet : Me Gnamien a accusé réception de l'avis bancaire à 15h45 et a formellement engagé la rédaction des statuts ;",
        "Prochain livrable : Remise des projets définitifs des statuts et de la convention de mandat social le lundi 29 juillet 2041."
    ])

    pdf.titre1("2. Recrutement Direction Générale & RH")
    pdf.para(
        "Les orientations stratégiques fixées par l'associé unique ont été rigoureusement appliquées :"
    )
    pdf.puces([
        "Mohamed Coulibaly (Note 91/100, Candidat n° 1) : L'invitation officielle pour le vendredi 26 juillet 2041 à 18h30 lui a été transmise. "
        "Monsieur Coulibaly a formellement confirmé sa disponibilité à 16h40. Le lien sécurisé de visioconférence et la grille de cadrage de 45 minutes sont opérationnels ;",
        "Mariam Brou (Note 88/100, DAF) : Le dossier d'évaluation a été finalisé et archivé en réserve active. Conformément à la décision "
        "de temporisation, aucune prise de contact ne sera effectuée avant d'avoir formellement sécurisé le recrutement de Mohamed Coulibaly."
    ])

    pdf.titre1("3. Affirmations vérifiées du jour (Pôle Juridique)")
    pdf.tableau(
        ["Élément analysé", "Statut de conformité", "Constat du Pôle Juridique"],
        [
            ["Délai de compensation SWIFT", "VÉRIFIÉE", "Les délais interbancaires Luxembourg-Abidjan sont de 24 à 48 heures ouvrées ; l'avis d'opéré suffit pour démarrer la rédaction."],
            ["Compte CARPA du Cabinet", "VÉRIFIÉE", "L'inscription du compte CARPA BICICI est conforme aux prescriptions du Barreau de Côte d'Ivoire pour le séquestre d'affaires."],
            ["Caducité mandat social", "VÉRIFIÉE", "La caducité automatique des mandats sociaux pour non-atteinte d'objectifs trimestriels est pleinement licite en droit OHADA."],
        ],
        largeurs=[55, 45, 90]
    )

    pdf.titre1("4. Consommation du budget informatique virtuel")
    pdf.para(
        "La consommation de ressources informatiques pour la journée du 25 juillet 2041 s'établit à 2,00 € HT (1,20 € pour le dossier RH "
        "et 0,80 € pour la synthèse de coordination). Le cumul mensuel atteint 41,56 € sur le plafond alloué de 1 000,00 € (solde disponible : 958,44 €)."
    )

    pdf.titre1("5. Décisions fermées soumises à l'associé unique")
    pdf.para(
        "Aucune décision urgente n'est requise ce soir. Pour la journée de demain vendredi 26 juillet 2041, l'équipe virtuelle vous soumet "
        "l'ordre du jour suivant :"
    )
    pdf.puces([
        "Journée : Poursuite des veilles techniques et préparatifs logistiques de la visioconférence ;",
        "18h30 : Tenue de l'entretien de sélection officiel en visioconférence avec Monsieur Mohamed Coulibaly (agenda A091) ;",
        "20h00 : Remise du rapport quotidien n° 7 (agenda A092)."
    ])

    cible = chemin("documents_william", "2041-07-25_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")


if __name__ == "__main__":
    generer_ordre_virement_spuerkeess()
    generer_courriel_envoi_justificatif()
    generer_accuse_reception_gnamien()
    generer_rapport_dg_25_juillet()

