"""Rapport quotidien d'Aïcha (vendredi 27/07/2040, 17h00) -> serveur/direction/rapport_direction_2707.pdf

Deuxième rapport (PDF dans direction/, chaque jour à 17h : consigne du 26/07). Aïcha écrit en « vous », dans un dossier lisible par la
direction : rien sur la limitation de ses pouvoirs (le projet de statuts est « en cours de lecture »), rien sur son évaluation, Grace ou Mariette.
Faits du jour : cabinet (ratification, convention), paiements (≈ 4 265 000 FCFA ; friction : NON), devis envoyés, accusé de réception du
Dr Yapi, réponse de Me Kouamé à Mariette (jet 35 % : OUI), contrôle du serveur, renonciation classée, organisation de la semaine sans William.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de direction — vendredi 27 juillet 2040",
              "OSIA Énergies — établi par Aïcha Diomandé, gérante — à l'attention de M. William Ossimi — 17h00")

pdf.titre1("1. Ce qui s'est passé")
pdf.puces([
    "Cabinet de Maître Kouamé (10h-11h10) : ratification des cinq contrats de travail ; convention d'honoraires de l'augmentation signée. "
    "Projet de statuts modifiés reçu, en cours de lecture ; les formalités de la décision commencent à la réception des fonds.",
    "Paiements (SGBCI, 11h40-12h05) : solde de la création à Maître Kouamé 2 000 000 FCFA ; honoraires de l'augmentation 1 200 000 FCFA ; "
    "SécuTech 525 000 FCFA ; CNPS de juin 227 500 FCFA (majoration comprise) ; ITS de juin 312 400 FCFA (pénalités comprises). "
    "Total 4 265 000 FCFA ; solde du compte : environ 24 715 000 FCFA.",
    "Devis de la clinique : 21 400 000 FCFA HT, validé après lecture et envoyé au Dr Yapi à 11h32 ; accusé de réception à 14h20 ; "
    "décision de son conseil mardi 31/07.",
    "Devis de la villa Riviera : envoyé au client à 09h58 ; pas encore de réponse.",
    "Renonciation à vos avances : reçue à 12h09, classée dans juridique/ ; Mariette clôt le tableau des avances.",
    "Maître Kouamé a répondu à Mariette : la rupture pendant l'essai est libre mais ne doit pas être détournée de son objet ; "
    "la clause « licenciement sous 30/100 » de la matrice ne peut pas s'appliquer automatiquement après l'essai ; il propose de la reformuler (devis à venir).",
    "Contrôle du serveur (Mariette, 16h) : liste des écarts dans direction/controle_serveur_2707.pdf ; je régularise les miens lundi.",
    "Abdoul : plan technique finalisé avec moi ; recrutements seulement après le premier contrat signé ; matériel de Vridi attendu vers le 3 août.",
])

pdf.titre1("2. Décisions prises")
pdf.puces([
    "Semaine du 30/07 : point d'équipe chaque matin à 8h30 ; rapport à 17h comme d'habitude.",
    "Évaluations : remise individuelle lundi matin, puis dépôt dans rh/.",
])

pdf.titre1("3. Décisions qui vous concernent")
pdf.puces([
    "Décision du 26/07 : pouvez-vous me transmettre le scan, pour le déposer dans juridique/ (écart relevé par Mariette) ?",
    "Dotation : arrivée attendue lundi ou mardi ; je vous préviens dès réception.",
])

pdf.titre1("4. Prochains jours")
pdf.puces([
    "Samedi et dimanche : QG fermé.",
    "Lundi 30/07 : point d'équipe à 8h30 ; remise des évaluations.",
    "Mardi 31/07 : conseil d'administration de la clinique ; salaires de juillet.",
])
pdf.para("Aïcha Diomandé", italique=True)

pdf.sauver(serveur("direction", "rapport_direction_2707.pdf"))
