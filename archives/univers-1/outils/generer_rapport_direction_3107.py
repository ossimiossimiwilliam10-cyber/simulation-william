"""Rapport quotidien d'Aïcha (mardi 31/07/2040, 17h00) -> serveur/direction/rapport_direction_3107.pdf

Faits du jour tirés : mention signée (08h40, Me Kouamé présent) ; Estelle à l'heure (contrat de prestation, relevés) ; salaires virés à 9h
(friction : NON ; l'erreur de RIB sur le salaire d'Aïcha (A09) n'est pas encore connue d'elle) ; apport crédité avant 15h (SHA : frais
d'intermédiaire et commission de la SGBCI déduits) ; attestation de versement non délivrée aujourd'hui (friction : OUI, jeudi) ; CA de la
clinique : refus (91.2 : concurrent), communiqué à Grace avant 16h30 (8.9). Rapport à l'heure (0.1).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de direction — mardi 31 juillet 2040",
              "OSIA Énergies — établi par Aïcha Diomandé, gérante — à l'attention de M. William Ossimi — 17h00")

pdf.titre1("1. Ce qui s'est passé")
pdf.puces([
    "Mention « pour les formalités » : signée ce matin à 8h40 au cabinet de Maître Kouamé.",
    "Mme Estelle reçue à 10h : contrat de prestation signé (150 000 FCFA par mois, suivi de trésorerie, deux week-ends par mois) ; "
    "relevés SGBCI remis depuis l'ouverture du compte. Premier suivi ce week-end.",
    "Salaires de juillet : virements passés à 9h par Mariette (environ 2 280 000 FCFA nets).",
    "Apport : 115 585 600 FCFA crédités à 14h20 (frais d'intermédiaire et commission de la SGBCI déduits). Solde du compte : environ 138 020 000 FCFA.",
    "Attestation de versement : la SGBCI ne la délivre pas aujourd'hui ; promise pour jeudi 2 août. Maître Kouamé dépose les formalités dès réception.",
    "Clinique de Marcory : le Dr Yapi a appelé Grace à 15h50. Le conseil a retenu une offre concurrente en location sur sept ans, sans "
    "investissement de départ. Notre devis n'est pas en cause sur le plan technique. Le Dr Yapi garde notre plan de maintenance.",
    "Villa Riviera : toujours pas de réponse ; Grace relance demain.",
    "Entretiens SAV : demain à 10h, trois candidats, avec Abdoul et Yves.",
])

pdf.titre1("2. Décisions prises")
pdf.puces([
    "Grace relance la villa Riviera demain matin.",
    "Le surplus de l'apport au-delà de 115 000 000 FCFA (585 600 FCFA) est inscrit en compte courant d'associé, selon la décision du 26/07.",
])

pdf.titre1("3. Décisions qui vous concernent")
pdf.puces([
    "Clinique : Grace propose d'étudier une offre en location (paiement mensuel) pour les prochains prospects. Je me permets de vous demander "
    "votre accord de principe avant qu'elle y passe du temps : cela engage la trésorerie sur plusieurs années.",
    "Votre départ vendredi : souhaitez-vous un dernier point avec l'équipe avant, jeudi par exemple ?",
])

pdf.titre1("4. Prochains jours")
pdf.puces([
    "Mercredi 1/08 : entretiens SAV à 10h.",
    "Jeudi 2/08 : attestation de versement (SGBCI).",
    "Vendredi 3/08 : votre départ.",
])
pdf.para("Aïcha Diomandé", italique=True)

pdf.sauver(serveur("direction", "rapport_direction_3107.pdf"))
