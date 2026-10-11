"""Rapport quotidien d'Aïcha (jeudi 02/08/2040, 17h00) -> serveur/direction/rapport_direction_0208.pdf

À l'heure (jet : OUI, 0.1). Faits tirés : SGBCI le matin (attestation refusée sans bulletin ; procuration et spécimen d'Yves acceptés) ;
bulletin signé par William à 11h50, remis à la SGBCI à 13h15, attestation pas avant demain (jet : NON, 82.0) ; statuts modifiés signés à 11h58 ;
A09 : un salaire mal affecté, mentionné sans dire que c'est le sien (évitement) ; section 3 vide.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de direction — jeudi 2 août 2040",
              "OSIA Énergies — établi par Aïcha Diomandé, gérante — à l'attention de M. William Ossimi — 17h00")

pdf.titre1("1. Ce qui s'est passé")
pdf.puces([
    "SGBCI (8h-9h20, avec M. Kanga) : procuration et spécimen de signature de M. Kanga acceptés ; double signature au-delà de 5 000 000 FCFA en place.",
    "Bulletin de souscription signé par vous au cabinet (11h50), remis à la SGBCI à 13h15 ; l'attestation de versement est promise pour demain matin. "
    "Maître Kouamé dépose ensuite les formalités de l'augmentation et des statuts modifiés (décision signée par vous à 11h58).",
    "Villa Riviera : Grace a appelé le client ce matin ; acompte de 20 % confirmé. Projet de contrat en relecture (Grace et moi) ; signature la semaine prochaine.",
    "Salaires de juillet : un virement a été mal affecté (erreur de RIB dans l'ordre groupé). Mariette le refait dès le retour des fonds, sous cinq à dix jours ouvrés.",
    "M. Koné : réponse attendue demain. Vridi : livraison toujours annoncée vers le 19 août ; M. Touré relance chaque jour.",
    "Note de Grace sur les offres en location : demain, sur le serveur.",
])

pdf.titre1("2. Décisions prises")
pdf.puces([
    "Point d'équipe demain à 8h30, avec M. Kanga.",
    "Retrait de l'attestation demain à l'ouverture, puis remise au cabinet.",
])

pdf.titre1("3. Décisions qui vous concernent")
pdf.puces(["Aucune aujourd'hui."])

pdf.titre1("4. Prochains jours")
pdf.puces([
    "Vendredi 3/08 : attestation (SGBCI) ; point d'équipe 8h30 ; réponse de M. Koné ; note de Grace ; votre départ.",
    "Semaine du 6/08 : contrat de la villa ; formalités au RCCM.",
])
pdf.para("Aïcha Diomandé", italique=True)

pdf.sauver(serveur("direction", "rapport_direction_0208.pdf"))
