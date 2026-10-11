"""Renonciation de William au remboursement de ses avances -> documents_william/

Écrit rédigé par William le 26/07/2040 (vers 14h05) après sa décision orale de renoncer au remboursement de ses avances à OSIA
(« une sorte de don ou je ne sais quoi », annoncée à Aïcha vers 13h50). Texte reconstitué par le moteur : William n'a pas dicté la
formulation ; aucune qualification juridique (don, apport, abandon de créance) n'est choisie à sa place ; aucun détail des avances
n'est donné (ni les salaires de juin payés en net, ni les fournisseurs). Document NON SIGNÉ et NON TRANSMIS (William le donnera
plus tard à Aïcha). Le dossier `documents_william/` contient les pièces rédigées par William et gardées par lui (hors serveur partagé).
"""
from osia_pdf import OsiaPDF, RACINE

pdf = OsiaPDF("Renonciation au remboursement d'avances",
              "OSIA ÉNERGIES SARL — texte rédigé par l'associé unique le 26/07/2040 (non signé, non transmis)")
pdf.meta("Société", "OSIA ÉNERGIES, société à responsabilité limitée, siège à Abidjan (Cocody Ambassades)")
pdf.meta("Auteur", "M. William Ossimi, associé unique")
pdf.meta("Destinataire", "Mme Aïcha Diomandé, gérante (transmission ultérieure)")

pdf.titre1("Déclaration")
pdf.para("Je soussigné, William Ossimi, associé unique d'OSIA Énergies SARL, déclare renoncer définitivement au remboursement "
         "des avances que j'ai consenties à la société avant l'ouverture de son compte bancaire, d'un montant total d'environ "
         "trois millions cinq cent quarante-trois mille (3 543 000) francs CFA, soit environ cinq mille quatre cents (5 400) euros.")
pdf.para("Cette renonciation est faite sans contrepartie. Elle ne donne lieu à aucun remboursement, ni en capital ni en intérêts.")

pdf.titre1("Signature")
pdf.para("Fait à Abidjan, le 26 juillet 2040.")
pdf.para("L'associé unique : ______________________  (William Ossimi)")
pdf.para("Texte rédigé par l'associé unique — non signé. À transmettre à la gérante.", italique=True)

pdf.sauver(RACINE / "documents_william" / "2040-07-26_renonciation_avances.pdf")
