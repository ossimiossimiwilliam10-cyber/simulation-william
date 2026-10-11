"""Premier rapport quotidien d'Aïcha (26/07/2040, 17h00) -> serveur/direction/rapport_direction_2607.pdf

Demandé par William le 26/07 (13h38 : rapport chaque soir ; 13h48 : PDF sur le serveur, chaque jour à 17h). T7c : execute_sans_discuter
(jet 34.8) : remis à l'heure. Aïcha écrit dans un dossier lisible par la direction : rien sur les évaluations, Grace, Mariette ou son propre
sentiment ; elle vouvoie dans l'écrit formel. Corrigé le 26/07 (corrections n° 34) : la ligne sur les CDD porte désormais sur les fins d'essai. CNPS : friction 30 % NON (pas de second passage). Rendez-vous au cabinet de Me Kouamé fixé à 10h.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de direction — jeudi 26 juillet 2040",
              "OSIA Énergies — établi par Aïcha Diomandé, gérante — à l'attention de M. William Ossimi — 17h00")

pdf.titre1("1. Ce qui s'est passé")
pdf.puces([
    "Abdoul : vu à 14h05 ; plan technique déposé à 16h41 (technique/plan_technique_2607.pdf). Je le lis demain.",
    "Grace : devis comparatif de la villa Riviera reçu à 16h30 (commercial/devis_villa_riviera_2607.pdf) : option A 15 900 000 FCFA HT, "
    "option B 19 600 000 FCFA HT ; marges indiquées par Grace : 21 % et 20 %. Devis de la clinique : en cours avec Abdoul, pour demain.",
    "CNPS : appelée à 15h10. Le numéro employeur est attribué (dossier du guichet unique du 11/07). ITS : déclaration de juin préparée en ligne "
    "avec Mariette. Déclarations et paiements de juin demain, avec les autres ordres ; des pénalités de retard sont à prévoir (montant en cours de calcul).",
    "Contrats de direction : Mariette fait le point des fins de période d'essai ; elle a écrit à Maître Kouamé (clause de sanction de la matrice après l'essai). Point au cabinet demain.",
    "SécuTech : réception signée ce matin ; solde de 525 000 FCFA réglé demain.",
])

pdf.titre1("2. Décisions prises")
pdf.puces([
    "Paiements groupés demain après le cabinet : solde de la création de Maître Kouamé (2 000 000 FCFA), convention d'honoraires, "
    "SécuTech (525 000 FCFA), CNPS et ITS de juin.",
    "Les évaluations de lundi sont en préparation.",
])

pdf.titre1("3. Décisions qui vous concernent")
pdf.puces([
    "Devis de la villa Riviera : je le transmets au client demain à 10h, sauf avis contraire de votre part avant.",
    "Avances : le dossier reste en attente.",
])

pdf.titre1("4. Demain, vendredi 27 juillet")
pdf.puces([
    "10h : cabinet de Maître Kouamé (ratification des cinq contrats, convention d'honoraires, formalités de la décision).",
    "Ordres de paiement à la SGBCI après le cabinet.",
    "Midi : déjeuner d'équipe proposé par Grace.",
    "Devis de la clinique : remis au Dr Yapi après ma lecture.",
    "16h : contrôle du serveur par Mariette.",
])
pdf.para("Aïcha Diomandé", italique=True)

pdf.sauver(serveur("direction", "rapport_direction_2607.pdf"))
