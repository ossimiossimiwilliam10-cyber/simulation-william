"""PIÈCES DU 26/07/2041 NUIT (univers 3, tour n° 60) :
1. D022 : Courriel officiel au Cabinet d'Avocats Ismaël Gnamien & Associés — Transmission des paramètres définitifs du mandat social du DG (Mohamed Coulibaly).
2. D023 : Courriel officiel à M. Mohamed Coulibaly — Confirmation d'accord, protocole institutionnel de communication et organigramme cible à 6 pôles.

Génération des fichiers PDF physiques (règle 4 et directives de William)
déposés dans `documents_william/` et vérifiés par `verifier_pdf.py`.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_gnamien_parametres_dg():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Cadrage du Mandat Social DG",
        "Transmission au Cabinet d'Avocats Ismaël Gnamien & Associés · Abidjan (RCI)",
        auteur="William Ossimi, Associé Unique & Fondateur",
        pied="Projet Solaire B2B Abidjan — Paramètres Mandat DG (Me Gnamien)"
    )

    pdf.meta("Émetteur", "Monsieur William Ossimi, Associé Unique et Fondateur (Audun-le-Tiche / Luxembourg)")
    pdf.meta("Destinataire", "Maître Ismaël Gnamien, Avocat à la Cour, Barreau d'Abidjan")
    pdf.meta("Date et heure", "Vendredi 26 juillet 2041, 20h15 (heure de Luxembourg / 18h15 Abidjan)")
    pdf.meta("Objet", "Transmission des paramètres définitifs du mandat social du Directeur Général pour insertion aux statuts")
    pdf.ln(3)

    pdf.titre1("1. Désignation du dirigeant et nature juridique du mandat")
    pdf.para(
        "Maître,"
    )
    pdf.para(
        "Faisant suite à nos précédents échanges et au règlement du premier acompte provisionnel de votre convention d'honoraires, "
        "j'ai l'honneur de vous informer qu'un accord verbal ferme et exhaustif a été conclu ce jour avec Monsieur Mohamed Coulibaly, "
        "cadre supérieur en banque d'affaires à Bruxelles, pour assurer les fonctions de Directeur Général de la future société SASU "
        "Projet Solaire B2B Abidjan."
    )
    pdf.para(
        "Afin de finaliser le projet de statuts constitutifs et la convention de mandat social attendus pour le lundi 29 juillet 2041, "
        "je vous transmets les stipulations contractuelles arrêtées entre les parties :"
    )
    pdf.puces([
        "Qualification juridique : Mandat social pur de Directeur Général d'une SAS régie par l'Acte uniforme OHADA (art. 414 et suivants AUSCGIE), "
        "sans cumul avec un contrat de travail salarié et sans aucun lien de subordination civil ou hiérarchique au sens du Code du travail ivoirien ;",
        "Révocabilité : Révocation ad nutum par décision discrétionnaire unilatérale de l'Associé Unique / Président, conformément aux principes directeurs OHADA ;",
        "Prise d'effet juridique : Nomination prenant effet au 1er octobre 2041 avec présence effective à Abidjan pour la signature des actes du 12 au 25 août 2041."
    ])

    pdf.titre1("2. Rémunération, primes d'objectifs et caducité")
    pdf.para(
        "La structure financière du mandat social a été arrêtée sur la formule suivante :"
    )
    pdf.puces([
        "Rémunération fixe mensuelle : 2 000 000 FCFA net de toutes retenues fiscales et sociales applicables en Côte d'Ivoire (soit environ 3 050 € net/mois), payable à terme échu ;",
        "Intéressement variable au chiffre d'affaires : 2,5 % du chiffre d'affaires hors taxes effectivement encaissé par la société sur ses contrats commerciaux ;",
        "Prime forfaitaire d'infrastructure : Prime de réalisation de 5 000 000 FCFA (soit environ 7 622 €) versée à l'achèvement et au raccordement effectif au réseau CIE de chaque tranche de 500 kWc de centrales solaires installées ;",
        "Clause de caducité et seuils probatoires : Le mandat comportera des clauses d'évaluation trimestrielle stricte (signature d'au moins 2 contrats fermes au premier trimestre d'exploitation, puis seuil minimal de marge brute de 15 000 000 FCFA par trimestre subséquent)."
    ])

    pdf.titre1("3. Clause de non-concurrence et indemnité compensatrice")
    pdf.para(
        "Au terme de négociations approfondies, l'encadrement de la protection post-mandat a été convenu comme suit :"
    )
    pdf.puces([
        "Durée d'application : 12 mois consécutifs à compter de la date de cessation effective des fonctions sociales ;",
        "Périmètre territorial : Région du Grand Abidjan (notamment zones industrielles de Vridi, Yopougon, Koumassi, Bonoua et agglomération abidjanaise) ;",
        "Indemnité compensatrice mensuelle : 50 % de la dernière rémunération fixe nette perçue (soit 1 000 000 FCFA par mois pendant la durée de l'interdiction). "
        "Cette indemnité sera due exclusivement en cas de révocation prononcée à l'initiative discrétionnaire de l'actionnaire, hors faute lourde, faute intentionnelle de gestion ou violation des statuts ;",
        "Clause pénale : Pénalité forfaitaire égale à 12 mois de rémunération fixe due de plein droit en cas de violation de l'engagement de non-concurrence."
    ])

    pdf.titre1("4. Articulation de la gouvernance et reporting")
    pdf.para(
        "L'organisation interne de la gouvernance de la SAS doit refléter l'équilibre suivant :"
    )
    pdf.puces([
        "Délégation de gestion : Monsieur Coulibaly dispose des pouvoirs les plus étendus pour la gestion courante opérationnelle, technique et commerciale dans le cadre du budget annuel approuvé ;",
        "Compétences réservées au Président : Tout engagement financier unitaire supérieur à 10 000 000 FCFA, toute souscription d'emprunt, acquisition/cession d'immobilisations ou cautionnement reste soumis à l'autorisation préalable écrite de l'Associé Unique ;",
        "Rattachement de la DAF : La Direction Administrative et Financière sera rattachée hiérarchiquement au DG au quotidien pour la fluidité opérationnelle, mais les statuts devront stipuler expressément une obligation de transparence financière absolue et un droit de communication direct et permanent de tous les états comptables et bancaires au profit de l'Associé Unique."
    ])

    pdf.para(
        "Je vous remercie d'intégrer l'ensemble de ces dispositions dans le jeu de statuts et la convention de mandat en cours de rédaction, "
        "dont la transmission est attendue le lundi 29 juillet 2041."
    )
    pdf.ln(2)
    pdf.para("Veuillez agréer, Maître, l'expression de mes salutations distinguées.")
    pdf.ln(4)
    pdf.para("William OSSIMI\nAssocié Unique & Fondateur")

    cible = chemin("documents_william", "2041-07-26_Courriel_Cabinet_Gnamien_Transmission_parametres_mandat_DG.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


def generer_courriel_mohamed_coulibaly():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Notification de Mandat & Gouvernance",
        "Protocole institutionnel de direction et organigramme cible · À l'attention de M. Mohamed Coulibaly",
        auteur="William Ossimi, Associé Unique & Président",
        pied="Projet Solaire B2B Abidjan — Notification DG & Protocole (M. Coulibaly)"
    )

    pdf.meta("Émetteur", "Monsieur William Ossimi, Président Fondateur / Bureau de la Présidence")
    pdf.meta("Destinataire", "Monsieur Mohamed Coulibaly (Bruxelles / futur Directeur Général Abidjan)")
    pdf.meta("Date et heure", "Vendredi 26 juillet 2041, 20h25 (heure de Bruxelles et Luxembourg)")
    pdf.meta("Objet", "Confirmation d'accord, protocole institutionnel de gouvernance et organigramme cible à 6 pôles")
    pdf.ln(3)

    pdf.titre1("1. Confirmation de votre sélection à la Direction Générale")
    pdf.para(
        "Cher Monsieur Coulibaly,"
    )
    pdf.para(
        "Je fais suite à notre entretien approfondi en visioconférence de ce vendredi 26 juillet 2041. "
        "C'est avec une grande satisfaction que je vous confirme officiellement par la présente notre plein accord "
        "pour votre nomination en qualité de Directeur Général de notre future société par actions simplifiée (SAS) "
        "dédiée au développement de centrales solaires en toiture pour le secteur industriel et commercial en Côte d'Ivoire."
    )
    pdf.para(
        "L'ensemble des conditions négociées ensemble — mandat social pur, rémunération fixe mensuelle de 2 000 000 FCFA net, "
        "intéressement de 2,5 % du chiffre d'affaires HT encaissé, prime de 5 000 000 FCFA par tranche de 500 kWc raccordée, "
        "et clause de non-concurrence de 12 mois assortie d'une indemnité compensatrice de 50 % en cas de révocation à l'initiative "
        "de l'actionnaire — a été officiellement notifié ce soir même à notre conseil juridique, Maître Ismaël Gnamien, pour "
        "incorporation aux statuts et à la convention de mandat social."
    )

    pdf.titre1("2. Protocole de gouvernance et canal institutionnel de communication")
    pdf.para(
        "Afin d'assurer le plus haut niveau d'efficacité stratégique, de rigueur analytique et de pérennité dans la conduite de nos affaires, "
        "notre collaboration reposera sur un protocole de gouvernance clair et structuré :"
    )
    pdf.puces([
        "Canal écrit exclusif et institutionnel : L'ensemble de nos échanges opérationnels, notes de cadrage, rapports périodiques, "
        "propositions d'arbitrage et demandes d'approbation budgétaire devront transiter exclusivement par l'adresse électronique officielle "
        "de la présidence. Ce canal écrit centralisé assure une parfaite traçabilité des décisions et permet à mon bureau de direction "
        "de vous apporter des retours analytiques d'une précision et d'une rigueur de niveau élite sous 24 à 48 heures ouvrées ;",
        "Visioconférences et réunions téléphoniques : Les échanges oraux ou réunions en distanciel sont strictement réservés aux comités "
        "de direction formels ou à la survenance d'urgences opérationnelles majeures. Ils feront systématiquement l'objet d'une planification "
        "préalable avec transmission d'un ordre du jour arrêté (aucun échange impromptu non planifié) ;",
        "Sessions de travail en présentiel : Des séances d'immersion et de travail direct auront lieu lors de mes missions régulières sur le terrain, "
        "dont la première se déroulera à Abidjan du 12 au 25 août 2041.",
        "Adhésion au protocole : Je vous invite à me confirmer par écrit votre accord plein et entier sur ce cadre de travail institutionnel."
    ])

    pdf.titre1("3. Organigramme cible à six pôles et feuille de route des recrutements")
    pdf.para(
        "Pour structurer nos futures opérations sur Abidjan, la configuration cible de l'entreprise s'articule autour de six pôles d'activité majeurs :"
    )
    pdf.tableau(
        ["Pôle d'activité", "Statut actuel", "Responsable / Mission assignée"],
        [
            ["Direction Générale", "Pourvu", "Mohamed Coulibaly — Mandataire social opérationnel, gouvernance globale terrain."],
            ["Direction Admin. & Financière", "Pré-positionné", "Profil en cours de sécurisation — Reporting OHADA, trésorerie, rattaché au DG."],
            ["Direction Technique Solaire", "À recruter", "Ingénieur solaire senior — Chantiers, dimensionnement, raccordement CIE (mi-septembre)."],
            ["Direction Commerciale B2B", "À recruter", "Cadre grands comptes — Prospection zones industrielles Vridi/Yopougon (mi-septembre)."],
            ["Ressources Humaines", "Actif", "Pôle sous supervision DAF & conseil externe — Recrutement ouvriers et techniciens."],
            ["Juridique & Conformité", "Actif", "Cabinet Me Ismaël Gnamien — Statuts, conformité réglementaire ANARE-CI / CIE."],
        ],
        largeurs=[50, 40, 100]
    )
    pdf.ln(2)
    pdf.para(
        "Comme évoqué, vous disposez de la pleine initiative pour activer vos réseaux et présélectionner vos futurs Directeurs Technique et Commercial "
        "dès les premières semaines d'août, en vue de finaliser leurs entretiens et d'assurer leur présence sur le terrain à la mi-septembre 2041."
    )

    pdf.titre1("4. Jalons opérationnels immédiats")
    pdf.para(
        "Les échéances immédiates s'organisent comme suit :"
    )
    pdf.puces([
        "Lundi 29 juillet 2041 : Réception des projets d'actes juridiques rédigés par le Cabinet Gnamien et transmission pour relecture conjointe ;",
        "Du 12 au 25 août 2041 : Mission conjointe à Abidjan (signatures notariales, visite et choix du siège à Cocody, dépôt au CEPICI) ;",
        "1er octobre 2041 : Prise de fonction permanente physique à Abidjan."
    ])
    pdf.ln(2)
    pdf.para("Dans l'attente de vous lire, je vous renouvelle mes félicitations et me réjouis de cette collaboration d'excellence.")
    pdf.ln(4)
    pdf.para("William OSSIMI\nPrésident Fondateur")

    cible = chemin("documents_william", "2041-07-26_Courriel_Mohamed_Coulibaly_Protocole_communication_et_Organigramme.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


if __name__ == "__main__":
    generer_courriel_gnamien_parametres_dg()
    generer_courriel_mohamed_coulibaly()
