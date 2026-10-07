"""Note juridique de Mariette (23/07/2040) -> serveur/rh/note_juridique_2307.pdf

Demandée par William le 19/07 (WhatsApp) et relancée le 21/07 ; promise « lundi avant midi ».
Version corrigée le 26/07/2040 (hors fiction, corrections n° 34) : les contrats de direction sont des CDI avec période d'essai (avant : CDD ;
le point 1 portait sur le risque de requalification, la rupture anticipée et l'indemnité de 3 %).
Références vérifiées le 23/07/2040 : Code du travail ivoirien (loi 2015-532) art. 5 et 14.5 ; décret n° 2024-900 (vérifié le 26/07) ;
décret 96-197 (règlement intérieur) ; échéances CNPS/ITS ; diffamation par communication publique.
Ton : prudent, très précis, la note ne se substitue pas à un avis d'avocat.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Note juridique : chartes, contrats et conformité sociale",
              "OSIA Énergies — confidentiel — à valider par Maître Kouamé")
pdf.meta("Date", "23/07/2040")
pdf.meta("Auteur", "Mariette Kouadio (DRH)")
pdf.meta("Destinataires", "William Ossimi, Aïcha Diomandé")
pdf.meta("Références", "Code du travail (loi n° 2015-532 du 20 juillet 2015), art. 5 et 14.5 ; décret n° 2024-900 du 16 octobre 2024 (période d'essai) ; décret n° 96-197 (règlement intérieur)")

pdf.titre1("Résumé")
pdf.para("Quatre points demandent une décision rapide. (1) Nos contrats de direction sont des CDI avec période d'essai : une fois "
         "l'essai terminé, on ne peut plus licencier sur un simple score d'évaluation, et chaque fin d'essai doit être suivie. "
         "(2) Le « naming and shaming » nous expose à des poursuites pour diffamation. (3) La charte du 19/07 n'a pas encore valeur "
         "de règlement intérieur. (4) La régularisation sociale (CNPS, impôt sur salaires) est en retard, y compris pour mon propre contrat.")

pdf.titre1("1. Les contrats de direction et la période d'essai")
pdf.puces([
    "Nos contrats sont à durée indéterminée et écrits ; ils fixent la durée de l'essai (art. 14.5). Condition respectée.",
    "Décret n° 2024-900 : durée maximale de six mois pour les cadres supérieurs (Mme Diomandé, Grace, Abdoul, moi-même ; Esther à son "
    "arrivée), trois mois pour les cadres (Yves). Renouvellement possible une seule fois, notifié par écrit au moins un mois avant la fin "
    "(six mois) ou quinze jours avant la fin (trois mois) ; sans notification, l'essai s'arrête à sa date.",
    "Fins d'essai : Yves le 15/10/2040 ; Mme Diomandé le 21/11/2040 ; moi-même le 30/11/2040 ; Grace et Abdoul le 15/01/2041.",
    "Pendant l'essai, chacune des parties peut rompre le contrat sans préavis ni indemnité, de préférence par écrit et avant la date de "
    "fin. Une rupture détournée de son objet (motif étranger aux compétences) peut être contestée : à confirmer avec Maître Kouamé.",
    "Après l'essai, le contrat est définitif : un licenciement demande un motif légitime (l'insuffisance professionnelle en est un, à "
    "prouver), une lettre, un préavis et, selon l'ancienneté, des indemnités.",
])
pdf.para("Recommandation : décider par écrit, avant chaque fin d'essai, de la confirmation, du renouvellement ou de la rupture ; faire "
         "relire par Maître Kouamé la clause de sanction de la matrice pour la période qui suit l'essai.", italique=True)

pdf.titre1("2. La matrice d'évaluation et le « naming and shaming »")
pdf.puces([
    "Un système de primes est tout à fait possible. Les critères chiffrés (chiffre d'affaires, délais, plaintes) sont défendables. "
    "L'ajustement discrétionnaire (bonus ou malus du Gérant, sans critère) est le point le plus fragile : il peut être présenté "
    "comme arbitraire en cas de litige. Je recommande de l'encadrer (plafond, motif écrit).",
    "La sanction maximale « licenciement pour incompétence notoire » n'est possible sans motif que pendant l'essai ; après l'essai, voir le point 1.",
    "Le « naming and shaming » (signalement d'un ancien salarié sur des forums ou réseaux professionnels) : la diffamation par "
    "communication publique est punie d'une amende de 1 à 3 millions de FCFA d'après les textes consultés, sans compter les "
    "dommages-intérêts civils. L'écrire dans un document interne signé aggrave la preuve de l'intention. Je recommande de le retirer de la matrice.",
])

pdf.titre1("3. Règlement intérieur")
pdf.puces([
    "Obligatoire au-delà de 10 salariés (décret n° 96-197). OSIA compte aujourd'hui 6 cadres : il n'est pas encore obligatoire, "
    "mais la charte du 19/07 ne peut pas servir de base à des sanctions tant qu'elle n'a pas suivi la procédure : présentation aux "
    "délégués du personnel, transmission à l'inspecteur du travail (observations sous un mois), dépôt au greffe, affichage.",
    "Il devra rappeler l'interdiction du harcèlement moral et sexuel (art. 5 du Code du travail), la procédure de signalement et les voies de recours.",
])

pdf.titre1("4. Qualité du signataire (gérance)")
pdf.para("Les cinq contrats numérisés sont signés « William Ossimi, Gérant ». Les statuts et le registre désignent Mme Diomandé comme "
         "gérante par procuration. À clarifier avec Maître Kouamé : validité des signatures et représentation de la société.")

pdf.titre1("5. Régularisation sociale et fiscale")
pdf.puces([
    "Les contrats de Mme Diomandé (22/05) et de moi-même (01/06) sont antérieurs au RCCM du 11/07 : actes passés pour la société "
    "en formation, à faire reprendre par la société.",
    "Les salaires de juin (payés en net par M. Ossimi, sans fiche de paie) n'ont fait l'objet ni de déclaration à la CNPS ni de "
    "retenue d'ITS. Échéances dépassées : ITS le 10/07, CNPS le 15/07. Majoration de 10 % par mois de retard à la CNPS et amende "
    "de 50 000 à 500 000 FCFA pour défaut de déclaration, selon les sources consultées (à confirmer auprès de la CNPS). Mon propre "
    "contrat est concerné.",
    "L'affiliation CNPS et la déclaration fiscale d'existence sont toujours « en cours » : à finaliser avant la paie de juillet "
    "(échéances du 10/08 pour l'ITS et du 15/08 pour la CNPS).",
    "Les salaires du 1er au 15/07 de Grace, Abdoul et Yves (période précédant leur prise de poste du 16/07) sont à qualifier "
    "(salaire ou indemnité) avant d'être déclarés.",
])

pdf.titre1("6. Plan d'action proposé")
pdf.tableau(["Action", "Responsable", "Échéance"], [
    ["Faire valider cette note par Maître Kouamé", "A. Diomandé", "25/07"],
    ["Suivre les fins d'essai (confirmation, renouvellement écrit ou rupture écrite avant le terme)", "W. Ossimi, A. Diomandé", "15/10, 21/11, 30/11, 15/01"],
    ["Retirer le « naming and shaming » ; encadrer le bonus/malus", "W. Ossimi, A. Diomandé", "avant la légalisation de la matrice"],
    ["Clarifier la gérance et la qualité des signataires", "Maître Kouamé", "31/07"],
    ["Régulariser CNPS et ITS de juin ; préparer la déclaration de la paie de juillet", "M. Kouadio, A. Diomandé", "avant le 10/08 et le 15/08"],
    ["Lancer la procédure de règlement intérieur (anticiper le seuil de 11 salariés)", "M. Kouadio", "à planifier"],
], [95, 45, 34])

pdf.para("Cette note est une analyse RH, pas un avis d'avocat : elle doit être validée par Maître Kouamé avant toute décision. "
         "Je reste disponible à tout moment pour la détailler.", italique=True)
pdf.para("Mariette Kouadio, DRH", italique=True)

pdf.sauver(serveur("rh", "note_juridique_2307.pdf"))
