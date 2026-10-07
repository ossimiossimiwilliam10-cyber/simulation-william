"""Scan de la décision de l'associé unique signée (augmentation de capital, 115 000 000 FCFA) -> courriels/

Pièce jointe du courriel du secrétariat de Me Kouamé à William du 26/07/2040, 15h42 (« ci-joint le scan de la décision de l'associé unique
signée ce matin ») ; ouverte par William le vendredi 27/07/2040 à 06h50. Texte identique au projet corrigé du 25/07 (même rédaction),
signé par William le 26/07/2040 à 09h18 en deux originaux ; la ligne de la gérante (« pour les formalités ») n'est pas encore signée :
prévu : Aïcha la complète au cabinet le 27/07 → elle ne l'a pas signée ce jour-là (elle relit d'abord le projet de statuts) ; le 27/07 à 17h13, elle refuse de déposer ce scan dans serveur/juridique/. Jet « erreur matérielle dans le scan » (10 %) : NON.
"""
from osia_pdf import OsiaPDF, RACINE

pdf = OsiaPDF("Décision de l'associé unique",
              "OSIA ÉNERGIES SARL — Augmentation de capital — décision du 26/07/2040 (scan de l'original signé)")
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
pdf.para("Fait à Abidjan, le 26 juillet 2040, en deux originaux.")
pdf.para("L'associé unique : [signature manuscrite]  (William Ossimi)")
pdf.para("La gérante, pour les formalités : ______________________  (Aïcha Diomandé)")
pdf.para("Scan de l'original signé le 26/07/2040 à 9h18 au cabinet de Maître Kouamé, transmis par courriel le même jour à 15h42. "
         "Ligne de la gérante à compléter au cabinet.", italique=True)

pdf.sauver(RACINE / "courriels" / "2040-07-26_decision_augmentation_capital_signee.pdf")
