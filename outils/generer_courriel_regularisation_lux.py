"""Courriel de William à sa direction (Luxembourg) -> documents_william/

Rédigé par William le dimanche 29/07/2040 vers 08h10 au Capitol (Abidjan), envoi PROGRAMMÉ pour le lundi 30/07/2040 à 08h00 (heure de
Luxembourg). Version choisie par William : il dit avoir cru que le Luxembourg n'était pas concerné, l'entreprise étant en Côte d'Ivoire ;
il constate un retard et demande à régulariser au plus vite. Procédure (vérifiée) : la demande d'autorisation d'une activité accessoire
(art. 14 du statut général) passe par la voie hiérarchique, donc par le directeur du lycée, puis le ministre du ressort, sur avis du
ministre de la Fonction publique. Texte reconstitué par le moteur à partir de la dictée : rien n'est ajouté sur la gérance, le capital,
les contrats signés « Gérant » ni les dates de ses démarches (William ne l'a pas choisi).
"""
from osia_pdf import OsiaPDF, RACINE


class CourrielPDF(OsiaPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t(f"Courriel programmé — copie conservée par William — page {self.page_no()}/{{nb}}"), align="C")


pdf = CourrielPDF("Courriel programmé",
                  "Envoi automatique le lundi 30 juillet 2040 à 08h00 (heure de Luxembourg) — rédigé le dimanche 29 juillet à Abidjan")
pdf.meta("De", "William Ossimi, professeur de mathématiques et de physique, régent de la 4e B")
pdf.meta("À", "Monsieur le Directeur du lycée (secrétariat de direction)")
pdf.meta("Objet", "Demande d'autorisation d'une activité accessoire — régularisation")

pdf.titre1("Message")
pdf.para("Monsieur le Directeur,")
pdf.para("Je me permets de vous écrire au sujet de ma situation administrative.")
pdf.para("Je suis associé d'une société de droit ivoirien, OSIA Énergies SARL, créée en juillet 2040 à Abidjan, qui installe des "
         "équipements d'énergie solaire. Avant de m'engager, je m'étais renseigné ; la société étant uniquement établie en Côte d'Ivoire, "
         "j'avais compris que cela ne concernait pas mon statut au Luxembourg.")
pdf.para("En me renseignant de nouveau, je constate que l'article 14 du statut général des fonctionnaires de l'État impose une "
         "autorisation préalable, et que j'ai donc pris du retard dans cette démarche.")
pdf.para("Je souhaite régulariser ma situation au plus vite. Je vous remercie de bien vouloir transmettre ma demande d'autorisation par "
         "la voie hiérarchique et de m'indiquer les pièces à fournir.")
pdf.para("Je reste à votre disposition pour tout renseignement.")
pdf.para("Veuillez agréer, Monsieur le Directeur, l'expression de mes salutations distinguées.")
pdf.para("William Ossimi")

pdf.sauver(RACINE / "documents_william" / "2040-07-29_courriel_regularisation_programme.pdf")
