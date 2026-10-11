"""Rapport quotidien d'Aïcha (vendredi 03/08/2040, 17h00) -> serveur/direction/rapport_direction_0308.pdf

À l'heure (jet : OUI, 19.5). Faits tirés : attestation à l'ouverture (OUI), dépôt au CEPICI lundi (Me Kouamé, 14h54) ; point d'équipe avec Yves ;
Koné accepte, début le 01/09 (78.0) ; note de Grace à 15h59 ; villa : contrat relu, signature mercredi 8 (mardi 7 férié) ; évaluations
mensuelles : question posée à Me Kouamé ; salaire mal affecté : retour attendu. Ton : vouvoiement, rien de personnel.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de direction — vendredi 3 août 2040",
              "OSIA Énergies — établi par Aïcha Diomandé, gérante — à l'attention de M. William Ossimi — 17h00")

pdf.titre1("1. Ce qui s'est passé")
pdf.puces([
    "Attestation de versement retirée à la SGBCI à 7h50, remise au cabinet à 8h20. Maître Kouamé dépose le dossier lundi au guichet unique du CEPICI.",
    "Point d'équipe de 8h30 : M. Kanga a transmis votre message ; l'équipe l'a écouté sans question.",
    "M. Koné accepte le poste de technicien SAV (380 000 FCFA brut). Début le 1er septembre : son employeur prolonge son préavis. Mariette prépare le contrat.",
    "Note de Grace sur les offres en location déposée dans commercial/ à 15h59 : deux projets pilotes proposés (école privée, hôtel).",
    "Villa Riviera : projet de contrat relu. Signature prévue mercredi 8 août (le 7 est férié). Acompte de 20 % : 3 180 000 FCFA HT.",
    "Évaluations mensuelles : question posée à Maître Kouamé ce matin ; réponse attendue la semaine prochaine.",
    "Virement de salaire mal affecté : retour des fonds attendu la semaine prochaine, puis nouveau virement.",
])

pdf.titre1("2. Décisions prises")
pdf.puces([
    "Contrat de M. Koné : rédaction par Mariette, signature à son arrivée.",
    "Signature du contrat de la villa le mercredi 8 août ; commande du matériel après l'acompte, selon votre autorisation du 1er août.",
])

pdf.titre1("3. Décisions qui vous concernent")
pdf.puces([
    "Projets pilotes en location (note de Grace) : aucun engagement avant votre décision.",
    "Le premier état mensuel de trésorerie (article 9 des statuts) vous sera adressé le 1er septembre.",
])

pdf.titre1("4. Prochains jours")
pdf.puces([
    "Lundi 6/08 : dépôt au CEPICI (Maître Kouamé).",
    "Mardi 7/08 : fête nationale, QG fermé.",
    "Mercredi 8/08 : signature du contrat de la villa.",
    "Vers le 19/08 : livraison de Vridi.",
])
pdf.para("Aïcha Diomandé", italique=True)

pdf.sauver(serveur("direction", "rapport_direction_0308.pdf"))
