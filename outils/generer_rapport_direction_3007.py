"""Rapport quotidien d'Aïcha (lundi 30/07/2040, 17h00) -> serveur/direction/rapport_direction_3007.pdf

Semaine sans William au QG. Faits du jour tirés : point d'équipe (annonce du départ de William le 4 août) ; évaluations remises puis déposées
dans rh/evaluations/ ; recrutement SAV lancé sur l'accord rapporté par Yves (T7c : execute_sans_discuter) ; mention non signée : Me Kouamé au
tribunal (friction : deuxième passage, rendez-vous mardi 8h30) ; apport non crédité ; salaires préparés ; fibre Orange reportée ; Bertin
accepte la sous-traitance. Section « Décisions qui vous concernent » : demande de confirmation écrite anticipée de son poste (négociation
tacite cachée, correction n° 36), forme de la mission d'Estelle, confirmation écrite du recrutement SAV.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de direction — lundi 30 juillet 2040",
              "OSIA Énergies — établi par Aïcha Diomandé, gérante — à l'attention de M. William Ossimi — 17h00")

pdf.titre1("1. Ce qui s'est passé")
pdf.puces([
    "Point d'équipe de 8h30 : présents Grace, Mariette, Abdoul, Yves. J'ai annoncé votre départ du 4 août et votre retour à confirmer.",
    "Évaluations remises individuellement (Grace 78, Mariette 81, Abdoul 66, Yves 69 ; toutes dans la tranche « performance standard »), "
    "puis déposées dans rh/evaluations/. Ajustement discrétionnaire non appliqué : il vous revient.",
    "Recrutement du technicien SAV : lancé à votre demande, transmise par Yves ; entretiens des trois candidats mercredi 1er août à 10h ; "
    "salaire prévu au plan : 350 000 FCFA brut par mois.",
    "Mention « pour les formalités » : Maître Kouamé était au tribunal à 15h ; sa collaboratrice n'a pas l'original. Rendez-vous demain à 8h30 au cabinet, avant son audience.",
    "Apport de 115 000 000 FCFA : pas encore crédité. La SGBCI compte deux à quatre jours ouvrés.",
    "Salaires de juillet : préparés par Mariette (mois complet pour Mariette et moi ; du 16 au 31 juillet pour Grace, Abdoul et Yves, la "
    "première quinzaine ayant été versée le 21/07) ; masse brute d'environ 2 620 000 FCFA ; virements demain matin.",
    "Fibre Orange : raccordement reporté au 14 août (travaux de voirie sur le boulevard), à confirmer par Orange.",
    "Abdoul a informé Bertin de son statut de sous-traitant : il accepte.",
    "Villa Riviera : toujours pas de réponse. Clinique de Marcory : conseil d'administration demain.",
])

pdf.titre1("2. Décisions prises")
pdf.puces([
    "Mme Estelle reçue demain à 10h au QG pour le suivi de trésorerie.",
    "Entretiens SAV mercredi à 10h, avec Abdoul et Yves.",
])

pdf.titre1("3. Décisions qui vous concernent")
pdf.puces([
    "Votre départ : je me permets de vous demander, avant le 4 août, la confirmation écrite de mon poste (fin anticipée de ma période d'essai), "
    "pour la continuité de la gérance pendant votre absence.",
    "Mme Estelle : sous quelle forme la rémunérer (contrat de prestation à 150 000 FCFA par mois) ? Je lui remets les relevés après votre accord écrit.",
    "Recrutement SAV : je l'engage sur votre accord transmis par Yves, alors que le plan prévoit d'attendre le premier contrat. Merci de me le "
    "confirmer par écrit.",
])

pdf.titre1("4. Prochains jours")
pdf.puces([
    "Mardi 31/07 : 8h30, cabinet (mention) ; 10h, Mme Estelle ; conseil d'administration de la clinique ; salaires.",
    "Mercredi 1/08 : entretiens SAV.",
    "Samedi 4/08 : votre départ.",
])
pdf.para("Aïcha Diomandé", italique=True)

pdf.sauver(serveur("direction", "rapport_direction_3007.pdf"))
