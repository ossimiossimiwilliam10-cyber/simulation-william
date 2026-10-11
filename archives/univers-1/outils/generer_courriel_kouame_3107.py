"""Courriel de Me Kouamé à William (mardi 31/07/2040, 16h39) -> courriels/

Réponse à la question de William (WhatsApp, 09h34) : pouvoirs actuels de la gérante et risque pour la société. T6 (autorité propre, sans
tirage sur le fond) ; heure tirée (13h00 + 43.8 × 5 min). Droit vérifié : AUSCGIE art. 328 (pouvoirs les plus étendus envers les tiers),
art. 329 (clauses limitatives inopposables aux tiers), art. 326 (révocation par l'associé ; dommages-intérêts sans juste motif), art. 330
(responsabilité du gérant), art. 891 (abus de biens sociaux). État réel : statuts du 04/07 (gérante quatre ans, procuration générale),
seule signataire SGBCI, statuts modifiés (seuils 5 M / 10 M) non signés.
"""
from osia_pdf import OsiaPDF, RACINE


class CourrielPDF(OsiaPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t(f"Courriel reçu — copie conservée par William — page {self.page_no()}/{{nb}}"), align="C")


pdf = CourrielPDF("Courriel de Maître Kouamé", "Reçu le mardi 31 juillet 2040 à 16h39 (Abidjan)")
pdf.meta("De", "Maître Kouamé, avocat (cabinet au Plateau, Abidjan)")
pdf.meta("À", "M. William Ossimi, associé unique d'OSIA Énergies SARL")
pdf.meta("Objet", "Pouvoirs de la gérante — situation au 31 juillet")

pdf.titre1("Message")
pdf.para("Monsieur Ossimi,")
pdf.para("Vous m'interrogez sur les pouvoirs actuels de Mme Diomandé et sur le risque qu'ils font courir à la société. Je vous réponds en "
         "avocat de la société ; je ne présume rien de la gérante.")
pdf.para("1. Ses pouvoirs aujourd'hui. Les statuts du 4 juillet la nomment gérante pour quatre ans, sans limitation. Envers les tiers, "
         "elle a les pouvoirs les plus étendus pour agir au nom de la société (article 328 de l'Acte uniforme) : signer des contrats, "
         "engager des dépenses, embaucher, licencier, payer. Elle est la seule signataire du compte à la SGBCI, sur lequel l'apport vient "
         "d'arriver. Elle ne peut pas, en revanche, toucher à ce qui vous est réservé comme associé unique : vos parts, le capital, les "
         "statuts, la nomination ou la révocation du gérant, l'approbation des comptes.")
pdf.para("2. Les statuts modifiés (seuils de 5 et 10 millions, actes réservés) ne sont pas encore signés. Ils sont prêts. Dès votre "
         "décision signée, la limitation s'impose à elle dans ses rapports avec vous ; elle reste inopposable aux tiers (article 329) : "
         "une banque ou un fournisseur de bonne foi qui traite avec elle est protégé, et la société reste engagée.")
pdf.para("3. Peut-elle nuire à la société ? Oui, matériellement, comme tout gérant seul signataire : un virement, un contrat ruineux, un "
         "engagement mal venu. Les recours viennent après coup : révocation à tout moment par votre décision (article 326 ; sans juste "
         "motif, elle peut réclamer des dommages-intérêts), action en responsabilité pour faute de gestion ou violation des statuts "
         "(article 330), et, au pénal, l'abus de biens sociaux. Après coup, l'argent ne revient pas toujours.")
pdf.para("4. Ce qui ferme réellement la porte avant votre départ :")
pdf.puces([
    "signer les statuts modifiés cette semaine ;",
    "faire signer à la gérante, avec la banque, une convention de fonctionnement du compte : au-dessus d'un montant (par exemple 5 millions), "
    "double signature. Ce que la banque a accepté lui est opposable. Le second signataire ne doit pas être vous (gérance de fait) : un cadre "
    "salarié avec délégation écrite, ou plus tard la responsable de la conformité ;",
    "recevoir chaque mois, en copie, les relevés bancaires directement de la banque.",
])
pdf.para("Tout cela se fait au grand jour : la gérante en sera informée, puisqu'elle doit signer la convention de compte.")
pdf.para("Le temps passé sera porté sur la note de la société.")
pdf.para("Cordialement,")
pdf.para("Maître Kouamé")

pdf.sauver(RACINE / "courriels" / "2040-07-31_courriel_kouame_pouvoirs_gerante.pdf")
