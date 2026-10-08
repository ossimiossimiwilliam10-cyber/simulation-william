"""Décision de l'associé unique modifiant les statuts (jeudi 02/08/2040, 11h58, cabinet de Me Kouamé) -> documents_william/

Signée par William au cabinet (au lieu de 15h ; friction « erreur matérielle » : NON). Contenu : seuils validés le 26/07 (5 M / 10 M FCFA,
actes réservés (a)-(f)), double signature au-delà de 5 M (Aïcha + Yves, procuration et spécimen acceptés le 02/08), relevés en copie à
l'associé, état mensuel de trésorerie. Limitation inopposable aux tiers (AUSCGIE art. 329). Copie conservée par William.
"""
from osia_pdf import OsiaPDF, RACINE


class DecisionPDF(OsiaPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t(f"Décision de l'associé unique du 2 août 2040 — copie conservée par William — page {self.page_no()}/{{nb}}"), align="C")


pdf = DecisionPDF("Décision de l'associé unique",
                  "OSIA ÉNERGIES SARL — modification des statuts (gérance, comptes bancaires, information de l'associé) — 2 août 2040")
pdf.meta("Associé unique", "M. William Ossimi, de nationalité luxembourgeoise, demeurant à Audun-le-Tiche (France)")
pdf.meta("Gérante", "Mme Aïcha Diomandé")
pdf.meta("Rédacteur", "Maître Kouamé, avocat de la société")

pdf.titre1("Première décision — Article 8 (Gérance), complété")
pdf.para("Dans ses rapports avec l'associé unique, la gérante doit obtenir l'autorisation préalable et écrite de celui-ci pour : "
         "a) tout engagement ou toute opération d'un montant supérieur à 5 000 000 de francs CFA ; b) tout emprunt, toute garantie ou "
         "sûreté ; c) l'acquisition ou la cession d'actifs durables ; d) le recrutement ou le licenciement d'un cadre ; e) tout contrat "
         "client d'un montant supérieur à 10 000 000 de francs CFA ; f) l'ouverture, la clôture ou la modification du fonctionnement d'un "
         "compte bancaire. La procuration générale du 4 juillet 2040 est modifiée en conséquence. Ces limitations sont inopposables aux "
         "tiers (article 329 de l'Acte uniforme relatif au droit des sociétés commerciales).")

pdf.titre1("Deuxième décision — Article 8 bis (Comptes bancaires), créé")
pdf.para("Toute opération d'un montant supérieur à 5 000 000 de francs CFA sur les comptes de la société requiert la signature conjointe "
         "de la gérante et d'un cadre salarié titulaire d'une délégation écrite. Les relevés mensuels des comptes sont adressés en copie "
         "à l'associé unique.")

pdf.titre1("Troisième décision — Article 9 (Décisions de l'associé unique), complété")
pdf.para("La gérante adresse chaque mois à l'associé unique un état de la trésorerie et des engagements de la société.")

pdf.titre1("Quatrième décision — Pouvoirs")
pdf.para("Tous pouvoirs sont donnés à la gérante pour accomplir les formalités consécutives à la présente décision, avec celles de "
         "l'augmentation de capital décidée le 26 juillet 2040.")

pdf.titre1("Signature")
pdf.para("Fait à Abidjan, le 2 août 2040, en deux originaux.")
pdf.para("Signé : William Ossimi, associé unique", italique=True)

pdf.sauver(RACINE / "documents_william" / "2040-08-02_decision_statuts_modifies_signee.pdf")
