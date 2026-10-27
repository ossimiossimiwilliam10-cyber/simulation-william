"""Génération des pièces du lundi 29 juillet 2041 après-midi et soir (tour n° 65) :
- D030 : Courriel officiel de William à Me Gnamien portant validation définitive des statuts SASU et du mandat DG (11h45)
- D031 : Dossier officiel MENJE Article 14 préparé pour la transmission hiérarchique au Directeur du Lycée (12h15)
- D032 : Rapport d'activité quotidien n° 10 du Directeur Général virtuel (20h00)
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_validation_gnamien():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Approbation Définitive des Actes",
        "Transmission au Cabinet d'Avocats Ismaël Gnamien & Associés à Abidjan",
        auteur="William Ossimi",
        pied="Projet Solaire B2B Abidjan — Validation Statuts & Mandat DG — 29/07/2041"
    )

    pdf.meta("Émetteur", "Monsieur William Ossimi, Associé Unique Fondateur (Audun-le-Tiche / Luxembourg)")
    pdf.meta("Destinataire", "Maître Ismaël Gnamien, Avocat à la Cour, Barreau d'Abidjan")
    pdf.meta("Date et heure", "Lundi 29 juillet 2041, 11h45 (heure de Luxembourg / 09h45 Abidjan)")
    pdf.meta("Objet", "Dossier CI-2041-0722 : Approbation définitive des projets de Statuts SASU et Mandat Social DG")
    pdf.ln(3)

    pdf.titre1("1. Approbation intégrale des projets d'actes")
    pdf.para(
        "Maître,"
    )
    pdf.para(
        "J'accuse formellement réception de votre courriel de ce jour transmettant le projet des statuts constitutifs de la société "
        "par actions simplifiée unipersonnelle (SASU) dénommée « SOLEIL B2B CÔTE D'IVOIRE » ainsi que le projet de convention de "
        "mandat social de Directeur Général liant la structure à Monsieur Mohamed Coulibaly."
    )
    pdf.para(
        "Après examen approfondi des stipulations contractuelles et vérification de conformité par mon pôle juridique, j'ai l'honneur "
        "de vous notifier mon approbation pleine, entière et sans réserve de ces deux projets d'actes."
    )

    pdf.titre1("2. Confirmation des paramètres clés")
    pdf.puces([
        "Forme et capital : SASU de droit OHADA, au capital initial de 10 000 000 FCFA (1 000 actions de 10 000 FCFA), intégralement souscrit par William Ossimi ;",
        "Direction Générale : Nomination de Monsieur Mohamed Coulibaly en qualité de Directeur Général mandataire social pur prenant effet au 1er octobre 2041, avec présence à Abidjan lors de la mission du 12 au 25 août 2041 ;",
        "Encadrement des pouvoirs : Plafond d'autorisation préalable écrite du Président fixé à 10 000 000 FCFA HT pour tout engagement unitaire, emprunt ou cautionnement ;",
        "Clause de non-concurrence : Durée de 12 mois post-mandat sur le Grand Abidjan, assortie d'une indemnité compensatrice de 50 % du traitement fixe (1 000 000 FCFA/mois) strictement due en cas de révocation discrétionnaire sans faute de gestion ;",
        "Transparence financière : Droit d'audit permanent et transmission directe de tous les états comptables et bancaires par la Direction Administrative et Financière."
    ])

    pdf.titre1("3. Calendrier de signature physique et immatriculation CEPICI")
    pdf.para(
        "Je vous confirme ma présence à Abidjan pour la séance solennelle de signature des actes authentiques en votre étude, "
        "arrêtée au mardi 13 août 2041 à 10h00, conjointement avec Monsieur Mohamed Coulibaly. "
        "Je vous remercie de préparer l'ensemble des originaux sur papier officiel ainsi que le dossier de dépôt auprès du CEPICI "
        "afin d'amorcer sans délai les formalités d'immatriculation au RCCM."
    )

    cible = chemin("documents_william", "2041-07-29_Courriel_Cabinet_Gnamien_Validation_definitive_statuts_et_mandat_DG.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


def generer_dossier_menje():
    pdf = DocPDF(
        "Ministère de l'Éducation nationale, de l'Enfance et de la Jeunesse (Luxembourg)",
        "Dossier de Déclaration au Titre de l'Article 14 du Statut des Fonctionnaires",
        auteur="William Ossimi",
        pied="Dossier Article 14 Statut Général — William Ossimi — Lycée de Luxembourg — 29/07/2041"
    )

    pdf.meta("Demandeur", "Monsieur William Ossimi, Professeur de mathématiques et physique (Carrière A1, Grade 14)")
    pdf.meta("Destinataire hiérarchique", "Monsieur le Directeur du Lycée d'affectation (Luxembourg-Ville)")
    pdf.meta("Autorité de tutelle", "Ministère de l'Éducation nationale, de l'Enfance et de la Jeunesse (MENJE)")
    pdf.meta("Date de constitution", "Lundi 29 juillet 2041 (préparé pour transmission formelle)")
    pdf.meta("Objet", "Demande d'autorisation d'activité accessoire / détention de capital non exécutif (Article 14)")
    pdf.ln(3)

    pdf.titre1("Lettre de saisine par la voie hiérarchique")
    pdf.para(
        "Monsieur le Directeur,"
    )
    pdf.para(
        "Faisant suite aux orientations transmises par la Direction générale du personnel enseignant du MENJE en date du 29 juillet 2041, "
        "j'ai l'honneur de vous soumettre, par la voie hiérarchique réglementaire, ma demande formelle d'autorisation relative à une participation "
        "financière non exécutive dans une entreprise de transition énergétique en Côte d'Ivoire, en application de l'article 14 de la loi "
        "modifiée du 16 avril 1979 fixant le statut général des fonctionnaires de l'État."
    )
    pdf.para(
        "Vous trouverez ci-joint le dossier complet comportant l'ensemble des éléments justificatifs requis par l'administration centrale "
        "afin de vous permettre d'émettre un avis motivé à destination de Madame la Ministre."
    )

    pdf.titre1("Pièce 1 — Note descriptive de l'activité économique projetée")
    pdf.para(
        "L'entité concernée est la société « SOLEIL B2B CÔTE D'IVOIRE » (SASU de droit OHADA), dont le siège social est situé à Abidjan (Cocody). "
        "Son activité est strictement circonscrite à l'ingénierie, la conception technique, la fourniture et la pose de panneaux solaires photovoltaïques "
        "en toiture pour des clients exclusivement professionnels (usines, entrepôts, bâtiments commerciaux tertiaires du secteur privé ivoirien)."
    )
    pdf.para(
        "Cette société n'a aucun lien contractuel, commercial ou institutionnel, direct ou indirect, avec l'État luxembourgeois, le système scolaire "
        "ou des entreprises de la Grande Région."
    )

    pdf.titre1("Pièce 2 — Justification documentaire de la qualité d'associé non exécutif")
    pdf.para(
        "Conformément aux statuts constitutifs déposés au dossier :"
    )
    pdf.puces([
        "Monsieur William Ossimi a la qualité exclusive d'associé unique fondateur et investisseur au capital (10 000 000 FCFA) ;",
        "La société est dotée d'une gouvernance séparée : la direction générale opérationnelle, technique, juridique et sociale est intégralement déléguée à un mandataire social tiers, Monsieur Mohamed Coulibaly, cadre supérieur bancaire et ingénieur ;",
        "Monsieur William Ossimi n'exerce aucun mandat de gérance, aucune fonction salariée, aucune représentation quotidienne et ne dispose d'aucun pouvoir de signature sur les comptes bancaires opérationnels de la société."
    ])

    pdf.titre1("Pièce 3 — Déclaration sur l'honneur d'absence d'incidence sur la tâche d'enseignement")
    pdf.para(
        "Je soussigné, William Ossimi, professeur de mathématiques et de physique, déclare sur l'honneur :"
    )
    pdf.puces([
        "Que l'intégralité de ma tâche réglementaire d'enseignement (22 leçons hebdomadaires normales et 3 leçons supplémentaires, soit 25 leçons au total), ainsi que l'ensemble des devoirs de préparation, de correction et de présence pédagogique demeurent ma priorité absolue et inconditionnelle ;",
        "Qu'aucun temps de service, aucune heure de cours et aucune disponibilité due aux élèves ou à l'établissement ne sera distrait au profit de cette entité ;",
        "Que mes prérogatives d'actionnaire (examen des comptes annuels et assemblée générale d'approbation) s'exerceront exclusivement en dehors des périodes scolaires et durant les congés légaux."
    ])

    pdf.titre1("Pièce 4 — Déclaration sur la nature exclusive des flux financiers perçus")
    pdf.para(
        "Je certifie sur l'honneur que la rémunération issue de cette participation se limitera strictement, le cas échéant, aux dividendes "
        "distribués au titre de la détention du capital social après approbation des comptes annuels par l'assemblée générale. "
        "Aucun salaire, traitement, honoraire de conseil, vacation, jeton de présence ou avantage en nature ne me sera alloué par la société."
    )

    cible = chemin("documents_william", "2041-07-29_Dossier_MENJE_Article_14_Transmission_hierarchique_Lycee.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


def generer_rapport_dg_29_juillet():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Direction Générale virtuelle",
        "Rapport d'activité quotidien n° 10 — Lundi 29 juillet 2041 (20h00)",
        auteur="Directeur Général virtuel",
        pied="Projet Solaire B2B Abidjan — Rapport quotidien n° 10 du 29/07/2041"
    )

    pdf.meta("Émetteur", "Directeur Général virtuel (Coordination des pôles Juridique, RH, Technique, Commercial)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique et Investisseur")
    pdf.meta("Date et heure", "Lundi 29 juillet 2041, 20h00 (heure de Luxembourg)")
    pdf.meta("Objet", "Bilan d'activité quotidien, consolidation des statuts constitutifs et gestion administrative MENJE")
    pdf.ln(3)

    pdf.titre1("1. Synthèse juridique : Statuts et Mandat DG validés")
    pdf.para(
        "La journée a marqué une avancée historique dans la concrétisation institutionnelle du projet :"
    )
    pdf.puces([
        "Réception des projets d'actes : Les projets complets de statuts constitutifs de la SASU SOLEIL B2B CÔTE D'IVOIRE (D028) et de la convention de mandat social de DG (D029) ont été livrés à 11h00 par le Cabinet Gnamien ;",
        "Approbation définitive de l'associé unique : Notification d'accord ferme transmise par courriel à 11h45 (D030) sans réserve ;",
        "Accusé de réception et rendez-vous officiel : Le Cabinet Gnamien a accusé réception à 12h05 et confirmé l'impression des originaux reliés sous chemise notariale en vue de la signature physique à Abidjan le mardi 13 août 2041 à 10h00 avec Mohamed Coulibaly, avant dépôt au CEPICI."
    ])

    pdf.titre1("2. Situation administrative luxembourgeoise (Article 14 MENJE)")
    pdf.para(
        "La réponse officielle du MENJE reçue à 10h22 a été traitée avec rigueur par le pôle juridique virtuel :"
    )
    pdf.puces([
        "Orientation hiérarchique intégrée : Nécessité d'une transmission formelle par l'intermédiaire du Directeur du Lycée d'affectation ;",
        "Dossier complet finalisé (D031) : Note descriptive de l'activité solaire, preuve statutaire de la qualité d'associé passif non gérant, déclaration sur l'honneur d'absence d'impact sur la charge d'enseignement et déclaration sur la nature exclusivement capitalistique des revenus (dividendes) ;",
        "Stratégie de dépôt : Dossier tenu prêt pour remise officielle à la direction du lycée lors de la rentrée de septembre."
    ])

    pdf.titre1("3. Situation des ressources humaines et logistique")
    pdf.puces([
        "Direction Générale (Mohamed Coulibaly) : Accord contractuel totalement scellé ; le dirigeant est synchronisé pour la mission d'Abidjan du 12 au 25 août ;",
        "Direction Administrative et Financière (Mariam Brou) : Candidature réservée au chaud dans l'attente de l'entretien d'embauche conduit par Mohamed à Abidjan ;",
        "Logistique de mission : Billets Air France (1 285 €) et e-visa SNEDAI (73 €) validés, option sur la résidence hôtelière de Cocody active (1 690 €)."
    ])

    pdf.titre1("4. Affirmations vérifiées du jour (Pôle Juridique)")
    pdf.tableau(
        ["Élément analysé", "Statut de conformité", "Constat du Pôle Juridique"],
        [
            ["Conformité Statuts SASU OHADA", "VÉRIFIÉE", "Les statuts intègrent scrupuleusement la séparation entre détention du capital et mandat social exécutif, protégeant l'investisseur."],
            ["Alignement Convention Mandat DG", "VÉRIFIÉE", "La clause de non-concurrence de 12 mois à 50 % d'indemnité en cas de révocation unilatérale sans faute de gestion est juridiquement inattaquable."],
            ["Régime Article 14 MENJE", "VÉRIFIÉE", "La jurisprudence administrative luxembourgeoise admet la détention patrimoniale passive sans mandat exécutif dès lors que la tâche scolaire est intégralement respectée."],
        ],
        largeurs=[55, 45, 90]
    )

    pdf.titre1("5. Consommation du budget informatique virtuel")
    pdf.para(
        "La consommation de ressources informatiques pour la journée du 29 juillet 2041 s'établit à 1,20 € HT (analyse comparée des statuts, instruction MENJE et formalisation du dossier hiérarchique). "
        "Le cumul mensuel s'élève à 46,06 € sur le plafond alloué de 1 000,00 € (solde disponible : 953,94 €)."
    )

    pdf.titre1("6. Prochains jalons")
    pdf.para(
        "Mercredi 31 juillet 2041 (soir) : Virement du traitement mensuel de l'État luxembourgeois (+9 320,00 € net).\n"
        "Vendredi 2 août 2041 (matin) : Exécution des virements automatiques d'épargne (732 €) et investissement ETF Monde (5 755 €)."
    )

    cible = chemin("documents_william", "2041-07-29_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


if __name__ == "__main__":
    generer_courriel_validation_gnamien()
    generer_dossier_menje()
    generer_rapport_dg_29_juillet()
