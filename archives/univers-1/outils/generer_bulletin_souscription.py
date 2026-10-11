"""Bulletin de souscription signé par William (jeudi 02/08/2040, 11h50, cabinet de Me Kouamé) -> documents_william/

Demandé par la SGBCI pour délivrer l'attestation de versement (friction du 02/08 : deuxième passage). Préparé par le cabinet (prêt avant midi,
pas de coursier : signature au cabinet). Données conformes à la décision du 26/07 (11 500 parts nouvelles de 10 000 FCFA, 115 000 000 FCFA)
et à l'apport crédité le 31/07 (115 585 600 FCFA, excédent de 585 600 FCFA en compte courant d'associé). Copie conservée par William.
"""
from osia_pdf import OsiaPDF, RACINE


class BulletinPDF(OsiaPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t(f"Bulletin de souscription — original signé en deux exemplaires — copie conservée par William — page {self.page_no()}/{{nb}}"), align="C")


pdf = BulletinPDF("Bulletin de souscription",
                  "OSIA ÉNERGIES SARL — augmentation du capital décidée le 26 juillet 2040 — préparé par le cabinet de Maître Kouamé")
pdf.meta("Société", "OSIA ÉNERGIES, SARL au capital de 30 000 000 FCFA, siège à Abidjan (Cocody Ambassades), RCCM d'Abidjan du 11 juillet 2040")
pdf.meta("Souscripteur", "M. William Ossimi, de nationalité luxembourgeoise, demeurant à Audun-le-Tiche (France), associé unique")
pdf.meta("Pièce d'identité", "Passeport luxembourgeois (copie jointe)")

pdf.titre1("Souscription")
pdf.para("Le soussigné déclare souscrire onze mille cinq cents (11 500) parts sociales nouvelles de dix mille (10 000) francs CFA de valeur "
         "nominale chacune, émises dans le cadre de l'augmentation du capital de la société de 30 000 000 à 145 000 000 de francs CFA décidée "
         "par l'associé unique le 26 juillet 2040.")
pdf.titre1("Libération")
pdf.para("Les parts souscrites sont libérées intégralement, soit cent quinze millions (115 000 000) de francs CFA, par le virement reçu le "
         "31 juillet 2040 sur le compte de la société ouvert à la SGBCI (115 585 600 francs CFA reçus, frais déduits ; l'excédent de "
         "585 600 francs CFA est inscrit au compte courant d'associé, conformément à la troisième décision du 26 juillet 2040).")
pdf.titre1("Signature")
pdf.para("Fait à Abidjan, le 2 août 2040, en deux originaux, dont l'un est remis à la SGBCI.")
pdf.para("Mention manuscrite : « Bon pour souscription de onze mille cinq cents parts sociales. »", italique=True)
pdf.para("Signé : William Ossimi", italique=True)

pdf.sauver(RACINE / "documents_william" / "2040-08-02_bulletin_souscription_signe.pdf")
