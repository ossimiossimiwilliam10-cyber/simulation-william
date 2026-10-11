"""Renonciation de William au remboursement de ses avances, version SIGNÉE -> documents_william/

Même texte que le brouillon du 26/07/2040 (`documents_william/2040-07-26_renonciation_avances.pdf`), signé électroniquement par William
(signature manuscrite tracée à l'écran) le vendredi 27/07/2040 vers 12h08 au QG, puis envoyé par courriel à Aïcha, qui le lui avait
demandé à 08h41 (« il me faut votre renonciation écrite et signée »). Aucune qualification juridique choisie à la place de William.
"""
from osia_pdf import OsiaPDF, RACINE

pdf = OsiaPDF("Renonciation au remboursement d'avances",
              "OSIA ÉNERGIES SARL — texte de l'associé unique, signé le 27/07/2040")
pdf.meta("Société", "OSIA ÉNERGIES, société à responsabilité limitée, siège à Abidjan (Cocody Ambassades)")
pdf.meta("Auteur", "M. William Ossimi, associé unique")
pdf.meta("Destinataire", "Mme Aïcha Diomandé, gérante")

pdf.titre1("Déclaration")
pdf.para("Je soussigné, William Ossimi, associé unique d'OSIA Énergies SARL, déclare renoncer définitivement au remboursement "
         "des avances que j'ai consenties à la société avant l'ouverture de son compte bancaire, d'un montant total d'environ "
         "trois millions cinq cent quarante-trois mille (3 543 000) francs CFA, soit environ cinq mille quatre cents (5 400) euros.")
pdf.para("Cette renonciation est faite sans contrepartie. Elle ne donne lieu à aucun remboursement, ni en capital ni en intérêts.")

pdf.titre1("Signature")
pdf.para("Fait à Abidjan, le 26 juillet 2040.")
pdf.para("L'associé unique : [signature manuscrite, apposée électroniquement le 27/07/2040]  (William Ossimi)")
pdf.para("Transmis par courriel à la gérante le 27/07/2040.", italique=True)

pdf.sauver(RACINE / "documents_william" / "2040-07-27_renonciation_avances_signee.pdf")

# Copie déposée par Aïcha dans juridique/ le 27/07/2040 à 13h05 (règles de classement : actes de l'associé unique).
import shutil
shutil.copyfile(RACINE / "documents_william" / "2040-07-27_renonciation_avances_signee.pdf",
                RACINE / "serveur" / "juridique" / "renonciation_avances_2707.pdf")
