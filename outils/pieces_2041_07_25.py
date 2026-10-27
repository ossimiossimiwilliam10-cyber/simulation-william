"""PIÈCES DU 25/07/2041 MATIN (univers 3, tour n° 51) :
1. Courriel du Cabinet d'Avocats Ismaël Gnamien & Associés : accusé de réception formel du dossier KYC
   et transmission du RIB bancaire officiel pour le virement du premier acompte (991 200 FCFA TTC / 1 511 €) ;
2. Document du Pôle RH : dossier d'évaluation de Mariam Brou (88/100) et trame d'entretien en visioconférence
   pour Mohamed Coulibaly (91/100).

Génération des fichiers PDF physiques (règle 4 et directives de William)
déposés dans `courriels/` et `documents_william/` et référencés dans l'application Gestion / Téléphone.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_gnamien_rib():
    pdf = DocPDF(
        "Cabinet d'Avocats Ismaël Gnamien & Associés — Abidjan",
        "Accusé de réception KYC & Relevé d'Identité Bancaire officiel (RIB)",
        auteur="Cabinet Me Ismaël Gnamien (Abidjan)",
        pied="Cabinet Gnamien & Associés — Transmission RIB & Accusé KYC SAS"
    )

    pdf.meta("Émetteur", "Cabinet Me Ismaël Gnamien & Associés, Avocat à la Cour, Barreau d'Abidjan")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique / Investisseur (Audun-le-Tiche / Luxembourg)")
    pdf.meta("Date et heure", "Jeudi 25 juillet 2041, 10h15 (heure d'Abidjan / 12h15 Luxembourg)")
    pdf.meta("Objet", "Dossier CI-2041-0722 : Accusé de réception KYC et coordonnées bancaires officielles du Cabinet")
    pdf.ln(3)

    pdf.titre1("1. Accusé de réception et validation de conformité du dossier KYC")
    pdf.para(
        "Monsieur,"
    )
    pdf.para(
        "Nous accusons formellement réception de votre courriel en date du 24 juillet 2041 nous notifiant votre acceptation ferme "
        "des termes de notre convention d'assistance juridique pour la constitution de la société Projet Solaire B2B Abidjan SAS, "
        "ainsi que des pièces justificatives transmises au titre de l'identification client (dossier KYC)."
    )
    pdf.para(
        "Après vérification par notre cellule de conformité réglementaire, nous vous confirmons que les pièces fournies (copie de votre passeport "
        "en cours de validité et justificatif de domicile en Moselle) sont complètes et conformes aux exigences de l'Acte Uniforme OHADA "
        "et de la réglementation bancaire UEMOA en vigueur. Le dossier permanent d'immatriculation est ouvert sous la référence "
        "d'archive interne : DOSSIER CI-2041-0722 / SAS SOLAIRE B2B."
    )
    pdf.para(
        "Nous prenons bonne note de votre qualité exclusive d'associé unique investisseur non-gérant, garantissant une étanchéité juridique "
        "rigoureuse avec votre statut professionnel au Luxembourg conformément aux dispositions de l'article 14 de la loi luxembourgeoise."
    )

    pdf.titre1("2. Coordonnées bancaires officielles pour le règlement du premier acompte")
    pdf.para(
        "Afin de procéder au règlement du premier acompte de démarrage de 40 %, soit la somme de 840 000 FCFA Hors Taxes majorée de la TVA (18 %), "
        "représentant un montant total de 991 200 FCFA TTC (contrevaleur en euros : 1 511,00 €), veuillez trouver ci-après les coordonnées "
        "bancaires officielles de notre compte séquestre professionnel :"
    )

    pdf.tableau(
        ["Élément d'identification", "Détail bancaire officiel"],
        [
            ["Établissement bancaire", "Banque Internationale pour le Commerce et l'Industrie de la Côte d'Ivoire (BICICI)"],
            ["Agence bancaire", "Agence Principale du Plateau, Avenue Delafosse, Abidjan (Côte d'Ivoire)"],
            ["Titulaire du compte", "SELAS Cabinet d'Avocats Ismaël Gnamien & Associés — Compte CARPA / Débours"],
            ["Code Banque / Guichet", "Banque : CI006  |  Guichet : 01001"],
            ["Numéro de compte", "012345678901  (Clé RIB : 45)"],
            ["Numéro IBAN (norme UEMOA)", "CI93 CI00 6010 0101 2345 6789 0145"],
            ["Code BIC / SWIFT", "BICI CI AB"],
            ["Montant à virer", "991 200 FCFA TTC  (soit 1 511,00 EUR au taux fixe légal UEMOA)"],
            ["Référence obligatoire de virement", "HONO-CI-2041-0722-OSSIMI"],
        ],
        largeurs=[65, 125]
    )

    pdf.titre1("3. Calendrier des diligences juridiques et formalités de création")
    pdf.para(
        "Dès l'émission de votre virement bancaire et la communication de l'avis d'opéré SWIFT correspondant, notre cabinet "
        "engagera sans délai la rédaction définitive des projets d'actes :"
    )
    pdf.puces([
        "Finalisation du projet des Statuts de la SASU selon les stipulations de l'Acte Uniforme OHADA révisé ;",
        "Rédaction du projet de Procès-Verbal des décisions de l'associé unique et de la Convention de Mandat Social du Directeur Général ;",
        "Transmission de ces projets pour relecture et approbation formelle sous 48 heures ouvrées (au plus tard lundi 29 juillet 2041) ;",
        "Réservation du certificat d'indisponibilité du capital social auprès de la banque partenaire BICICI en vue du dépôt des fonds."
    ])
    pdf.para(
        "Restant à votre entière disposition pour tout renseignement complémentaire, nous vous prions d'agréer, Monsieur, l'expression de nos sentiments distingués."
    )
    pdf.para(
        "Pour le Cabinet Gnamien & Associés,\nMaître Ismaël Gnamien, Avocat à la Cour"
    )

    cible = chemin("courriels", "2041-07-25_Cabinet_Gnamien_Transmission_RIB_officiel.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")


def generer_dossier_rh_candidats():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Pôle Ressources Humaines & Direction",
        "Dossier comparatif Mariam Brou (88/100) & Trame d'entretien Mohamed Coulibaly (91/100)",
        auteur="Pôle RH & Direction Générale virtuelle",
        pied="Projet Solaire B2B Abidjan — Processus de recrutement Dirigeant"
    )

    pdf.meta("Émetteur", "Pôle Ressources Humaines & Direction Générale virtuelle")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique et Investisseur")
    pdf.meta("Date et heure", "Jeudi 25 juillet 2041, 11h30 (heure de Luxembourg)")
    pdf.meta("Objet", "Finalisation du dossier Mariam Brou et guide de préparation d'entretien Mohamed Coulibaly")
    pdf.ln(3)

    pdf.titre1("1. Dossier d'évaluation approfondie : Madame Mariam Brou (C020, Note 88/100)")
    pdf.para(
        "Le Pôle RH a achevé la vérification approfondie du profil et des références professionnelles de Madame Mariam Brou, "
        "dont le dossier a été soumis le 19 juillet 2041 via le sourcing d'Abidjan :"
    )
    pdf.tableau(
        ["Critère d'analyse", "Évaluation détaillée du Pôle RH"],
        [
            ["Identité et situation", "43 ans, de nationalité ivoirienne, résidente permanente à Abidjan (Cocody)."],
            ["Formation académique", "Diplôme d'Études Supérieures Comptables et Financières (INP-HB Yamoussoukro)."],
            ["Expérience métier", "16 ans d'expérience en gestion comptable, administrative et financière de PME à Abidjan."],
            ["Réseau d'affaires local", "Réseau établi de 15 directeurs généraux et chefs d'entreprises industrielles (Vridi, Yopougon)."],
            ["Points forts majeurs", "Maîtrise absolue du droit SYSCOHADA, rigueur administrative, fiabilité de gestion avérée."],
            ["Limites opérationnelles", "Absence de compétences techniques en ingénierie photovoltaïque ; profil plus gestionnaire que commercial B2B."],
            ["Recommandation du Pôle RH", "Profil de très haute valeur à orienter prioritairement vers la Direction Administrative et Financière (DAF)."],
        ],
        largeurs=[60, 130]
    )

    pdf.titre1("2. Cadrage de l'entretien de sélection : Monsieur Mohamed Coulibaly (C011, Note 91/100)")
    pdf.para(
        "Conformément à votre arbitrage désignant Monsieur Mohamed Coulibaly comme candidat prioritaire numéro un pour le poste de "
        "Directeur Général, le Pôle RH a préparé la prise de contact pour caler l'entretien officiel en visioconférence. "
        "Trois créneaux horaires sont proposés au candidat :"
    )
    pdf.puces([
        "Option A : Vendredi 26 juillet 2041 à 18h30 (heure de Bruxelles/Luxembourg, soit 16h30 à Abidjan) ;",
        "Option B : Samedi 27 juillet 2041 à 10h00 (heure de Bruxelles/Luxembourg, soit 08h00 à Abidjan) ;",
        "Option C : Lundi 29 juillet 2041 à 19h00 (heure de Bruxelles/Luxembourg, soit 17h00 à Abidjan)."
    ])

    pdf.titre1("3. Trame d'entretien et grille d'évaluation structurée (durée prévisionnelle : 45 minutes)")
    pdf.para(
        "Pour structurer cet entretien décisif, le Pôle RH vous soumet la trame opérationnelle suivante :"
    )
    pdf.tableau(
        ["Séquence", "Objectif et points clés à sonder"],
        [
            ["1. Parcours & retour (10 min)", "Motivation du retour en Côte d'Ivoire, calendrier d'installation à Abidjan, disponibilité."],
            ["2. Déploiement B2B (15 min)", "Plan de prospection des toitures industrielles, activation des 40 contacts dirigeants, approche commerciale."],
            ["3. Gouvernance OHADA (10 min)", "Adhésion au mandat social pur révocable ad nutum, respect du reporting mensuel, clause de non-concurrence."],
            ["4. Rémunération & clôture (10 min)", "Échanges sur le fixe d'amorçage et le variable sur marge nette encaissée, questions du candidat."],
        ],
        largeurs=[65, 125]
    )

    pdf.titre1("4. Consommation du budget informatique du segment virtuel")
    pdf.para(
        "Le coût informatique de génération du présent dossier et des vérifications de références s'élève à 1,20 € HT, "
        "portant la consommation cumulée du mois de juillet 2041 à 40,76 € sur le plafond alloué de 1 000,00 € (solde disponible : 959,24 €)."
    )

    cible = chemin("documents_william", "2041-07-25_Dossier_comparatif_Mariam_Brou_et_Trame_entretien_Mohamed_Coulibaly.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")


if __name__ == "__main__":
    generer_courriel_gnamien_rib()
    generer_dossier_rh_candidats()
