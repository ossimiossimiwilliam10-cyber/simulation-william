"""Projet corrigé de décision de l'associé unique (augmentation de capital, 115 000 000 FCFA) -> courriels/

Pièce jointe du courriel de Me Kouamé à William du 25/07/2040, 17h38 (« projet corrigé, à transmettre à votre banque »), transmise par William
à la Spuerkeess par S-Net à 18h20. Le dossier `courriels/` contient les pièces reçues par William par courriel, hors serveur partagé.
Contenu fixé au rendez-vous du 25/07 (15h14-16h15) : 115 M FCFA ronds, surplus en compte courant d'associé, réalisation conditionnée à la
réception des fonds avant le 31/08/2040, droits d'enregistrement 0,6 % = 690 000 FCFA. Document NON SIGNÉ (signature prévue le 26/07/2040, 9h).
"""
from osia_pdf import OsiaPDF, RACINE

pdf = OsiaPDF("Décision de l'associé unique", "OSIA ÉNERGIES SARL — Augmentation de capital — PROJET corrigé du 25/07/2040 (non signé)")
pdf.meta("Société", "OSIA ÉNERGIES, société à responsabilité limitée, siège à Abidjan (Cocody Ambassades), immatriculée au registre du "
                    "commerce et du crédit mobilier d'Abidjan le 11 juillet 2040")
pdf.meta("Capital actuel", "30 000 000 de francs CFA, divisé en 3 000 parts sociales de 10 000 francs CFA")
pdf.meta("Associé unique", "M. William Ossimi, de nationalité luxembourgeoise, demeurant à Audun-le-Tiche (France)")
pdf.meta("Rédacteur", "Maître Kouamé, avocat de la société")

pdf.titre1("Première décision — Augmentation du capital")
pdf.para("Le capital social est augmenté de cent quinze millions (115 000 000) de francs CFA, par la création de onze mille cinq cents "
         "(11 500) parts sociales nouvelles de dix mille (10 000) francs CFA de valeur nominale chacune, souscrites en totalité par l'associé unique "
         "et libérées intégralement en numéraire.")

pdf.titre1("Deuxième décision — Condition de réalisation")
pdf.para("L'augmentation de capital sera réalisée à la date de réception des fonds sur le compte de la société ouvert auprès de la SGBCI, "
         "constatée par une attestation de versement de la banque, au plus tard le 31 août 2040. À défaut, la présente décision sera caduque de plein droit.")

pdf.titre1("Troisième décision — Excédent éventuel")
pdf.para("Toute somme reçue par la société au-delà de cent quinze millions (115 000 000) de francs CFA, notamment après déduction des frais bancaires "
         "d'intermédiaires, sera inscrite au crédit du compte courant d'associé de M. William Ossimi.")

pdf.titre1("Quatrième décision — Modification des statuts")
pdf.para("Sous la même condition, l'article 6 des statuts est modifié comme suit : « Le capital social est fixé à cent quarante-cinq millions "
         "(145 000 000) de francs CFA, divisé en quatorze mille cinq cents (14 500) parts sociales de dix mille (10 000) francs CFA, souscrites et "
         "intégralement libérées par l'associé unique. »")

pdf.titre1("Cinquième décision — Pouvoirs")
pdf.para("Tous pouvoirs sont donnés à la gérante, Mme Aïcha Diomandé, pour accomplir les formalités consécutives à la présente décision : "
         "statuts modifiés, inscription modificative au registre du commerce et du crédit mobilier, publication, déclaration de l'investissement "
         "étranger, et toute formalité utile.")

pdf.titre1("Frais")
pdf.para("Les honoraires, les frais de formalités et les droits d'enregistrement liés à l'augmentation de capital sont supportés par la société. "
         "Les droits d'enregistrement sont estimés à 0,6 % du montant des apports, soit 690 000 francs CFA.")

pdf.titre1("Signature")
pdf.para("Fait à Abidjan, le ______ juillet 2040, en deux originaux.")
pdf.para("L'associé unique : ______________________  (William Ossimi)")
pdf.para("La gérante, pour les formalités : ______________________  (Aïcha Diomandé)")
pdf.para("PROJET — non signé. Signature prévue le 26 juillet 2040 à 9h au cabinet de Maître Kouamé.", italique=True)

pdf.sauver(RACINE / "courriels" / "2040-07-25_decision_augmentation_capital_projet.pdf")
