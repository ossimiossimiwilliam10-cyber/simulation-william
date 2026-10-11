"""Statuts d'OSIA Énergies SARL -> serveur/direction/statuts_osia_energies.pdf

Document demandé le 23/07/2040 pour le dossier de la Spuerkeess (justificatif de l'opération). Il fixe la gouvernance
telle que William l'a énoncée (« j'ai désigné Aïcha comme gérante ») : William associé unique, Aïcha gérante.
Date de signature des statuts retenue par le moteur : 04/07/2040 (avant le RCCM du 11/07/2040).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Statuts de la société OSIA Énergies SARL",
              "Société à responsabilité limitée unipersonnelle — Abidjan, Côte d'Ivoire")
pdf.meta("Date", "04/07/2040")
pdf.meta("Copie", "Version du dossier interne (remise à la banque sur demande)")

articles = [
    ("Article 1 — Forme",
     "Il est constitué une société à responsabilité limitée unipersonnelle régie par l'Acte uniforme OHADA relatif au droit "
     "des sociétés commerciales et du groupement d'intérêt économique, par la législation ivoirienne et par les présents statuts."),
    ("Article 2 — Dénomination", "La société prend la dénomination : OSIA Énergies SARL."),
    ("Article 3 — Objet",
     "La société a pour objet, en Côte d'Ivoire et à l'étranger : l'installation, la maintenance et l'exploitation de systèmes "
     "d'énergie solaire photovoltaïque et de stockage ; le négoce de matériels s'y rapportant ; les études et le conseil énergétiques."),
    ("Article 4 — Siège", "Le siège social est fixé à Abidjan, Cocody Ambassades. Il peut être transféré par décision de l'associé unique."),
    ("Article 5 — Durée", "La durée de la société est de quatre-vingt-dix-neuf (99) ans à compter de son immatriculation au RCCM."),
    ("Article 6 — Capital",
     "Le capital social est fixé à trente millions (30 000 000) de francs CFA, divisé en trois mille (3 000) parts sociales de "
     "dix mille (10 000) francs CFA, souscrites et intégralement libérées par l'associé unique. Les fonds ont été déposés auprès "
     "de la Société Générale Côte d'Ivoire (SGBCI)."),
    ("Article 7 — Associé unique",
     "M. William Ossimi, de nationalité luxembourgeoise, demeurant à Audun-le-Tiche (France), détient la totalité des parts sociales."),
    ("Article 8 — Gérance",
     "Mme Aïcha Diomandé, de nationalité ivoirienne, est nommée gérante pour une durée de quatre (4) ans, renouvelable. Elle dispose "
     "des pouvoirs les plus étendus pour agir en toute circonstance au nom de la société, dans la limite de l'objet social et sous "
     "réserve des décisions réservées à l'associé unique (article 9). Elle exerce en vertu d'une procuration générale délivrée par "
     "l'associé unique."),
    ("Article 9 — Décisions de l'associé unique",
     "L'associé unique décide seul de l'approbation des comptes, de l'affectation des résultats, de la modification des statuts, de "
     "l'augmentation ou de la réduction du capital, de la cession des parts, de la nomination ou de la révocation du gérant et de la "
     "dissolution de la société. Ses décisions sont écrites, signées et consignées dans un registre."),
    ("Article 10 — Exercice social",
     "L'exercice social commence le 1er janvier et se termine le 31 décembre. Le premier exercice court de l'immatriculation au "
     "31 décembre 2040."),
]
for titre, texte in articles:
    pdf.titre1(titre)
    pdf.para(texte)

pdf.ln(8)
pdf.set_font(pdf.fam, "", 10)
pdf.cell(95, 6, pdf.t("Fait à Abidjan, le 04/07/2040, en trois exemplaires originaux."), new_x="LMARGIN", new_y="NEXT")
pdf.ln(4)
pdf.cell(90, 6, pdf.t("L'associé unique"))
pdf.cell(0, 6, pdf.t("La gérante"), new_x="LMARGIN", new_y="NEXT")
pdf.set_font(pdf.fam, "I", 10)
pdf.cell(90, 6, pdf.t("[Signature — W. Ossimi]"))
pdf.cell(0, 6, pdf.t("[Signature — A. Diomandé]"), new_x="LMARGIN", new_y="NEXT")

pdf.sauver(serveur("direction", "statuts_osia_energies.pdf"))
