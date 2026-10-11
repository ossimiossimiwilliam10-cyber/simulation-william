"""Base commune des PDF de la simulation (univers 2, 11/10/2026 ; reprend `osia_pdf.py` de l'univers 1, archivé).

Règles du simulateur (voir CLAUDE.md §3.4) :
- tout livrable demandé par William est un VRAI fichier (ici PDF) dans le bon dossier : `documents_william/` (pièces rédigées
  ou gardées par William), `courriels/` (pièces reçues), ou le serveur d'une organisation s'il en existe un ;
- les accents sont obligatoires (William les exige) : police Unicode (Arial, sinon DejaVu). Repli sur Helvetica + nettoyage
  latin-1 si aucune police n'existe ;
- après génération : `python outils/verifier_pdf.py`.

Usage depuis un script de `outils/` :
    from pdf_base import DocPDF, chemin
    pdf = DocPDF("Titre", "Sous-titre", auteur="Banque X", pied="Banque X")
    pdf.para("Texte avec accents : é, è, à, ç.")
    pdf.sauver(chemin("courriels", "2040-07-18_courrier.pdf"))
"""
from pathlib import Path

from fpdf import FPDF
from fpdf.fonts import FontFace

RACINE = Path(__file__).resolve().parent.parent

_POLICES = [
    # (dossiers, regular, bold, italic)
    (["C:/Windows/Fonts"], "arial.ttf", "arialbd.ttf", "ariali.ttf"),
    (["/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/dejavu"],
     "DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf"),
    (["/Library/Fonts", "/System/Library/Fonts/Supplemental"],
     "Arial.ttf", "Arial Bold.ttf", "Arial Italic.ttf"),
]

_REPLI_LATIN1 = {"’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-",
                 "→": "->", "≥": ">=", "≤": "<=", "•": "-", "œ": "oe", "Œ": "OE",
                 "\u202f": " ", "\u00a0": " "}


def chemin(*morceaux):
    """Chemin absolu dans le dépôt : chemin("documents_william", "note.pdf"), chemin("courriels", "x.pdf")…"""
    return RACINE.joinpath(*morceaux)


def _enregistrer_police(pdf):
    for dossiers, reg, bold, ital in _POLICES:
        for d in dossiers:
            if all((Path(d) / f).exists() for f in (reg, bold, ital)):
                pdf.add_font("doc", "", str(Path(d) / reg))
                pdf.add_font("doc", "B", str(Path(d) / bold))
                pdf.add_font("doc", "I", str(Path(d) / ital))
                return "doc", True
    return "helvetica", False


class DocPDF(FPDF):
    """PDF A4 avec titre, sous-titre et pied de page « <pied> — page x/y » (ou « page x/y » sans pied)."""

    def __init__(self, titre, sous_titre=None, orientation="P", auteur=None, pied=None):
        super().__init__(orientation=orientation, unit="mm", format="A4")
        self.titre_doc = titre
        self.sous_titre = sous_titre
        self.pied = pied
        self.fam, self.unicode = _enregistrer_police(self)
        self.set_margins(18, 18, 18)
        self.set_auto_page_break(auto=True, margin=18)
        self.set_title(titre)
        if auteur:
            self.set_author(auteur)
        self.alias_nb_pages()
        self.add_page()

    # -- texte ---------------------------------------------------------
    def t(self, texte):
        if self.unicode:
            return texte
        for k, v in _REPLI_LATIN1.items():
            texte = texte.replace(k, v)
        return texte.encode("latin-1", "replace").decode("latin-1")

    # -- gabarit -------------------------------------------------------
    def header(self):
        if self.page_no() == 1:
            self.set_font(self.fam, "B", 15)
            self.cell(0, 9, self.t(self.titre_doc), align="C", new_x="LMARGIN", new_y="NEXT")
            if self.sous_titre:
                self.set_font(self.fam, "I", 10)
                self.cell(0, 6, self.t(self.sous_titre), align="C", new_x="LMARGIN", new_y="NEXT")
            self.ln(4)
        else:
            self.set_font(self.fam, "I", 8)
            self.cell(0, 6, self.t(self.titre_doc), align="R", new_x="LMARGIN", new_y="NEXT")
            self.ln(2)

    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        texte = f"{self.pied} — page {self.page_no()}/{{nb}}" if self.pied else f"page {self.page_no()}/{{nb}}"
        self.cell(0, 8, self.t(texte), align="C")

    # -- blocs ---------------------------------------------------------
    def meta(self, label, valeur):
        self.set_font(self.fam, "B", 10)
        self.cell(34, 6, self.t(label + " :"))
        self.set_font(self.fam, "", 10)
        self.multi_cell(0, 6, self.t(valeur), new_x="LMARGIN", new_y="NEXT")

    def titre1(self, texte):
        if self.get_y() > self.h - 45:  # évite un titre orphelin en bas de page
            self.add_page()
        self.ln(3)
        self.set_font(self.fam, "B", 12)
        self.multi_cell(0, 7, self.t(texte), new_x="LMARGIN", new_y="NEXT")
        self.set_font(self.fam, "", 10)

    def para(self, texte, taille=10, italique=False):
        self.set_font(self.fam, "I" if italique else "", taille)
        self.multi_cell(0, 5.5, self.t(texte), new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def puces(self, items, taille=10):
        self.set_font(self.fam, "", taille)
        for it in items:
            self.set_x(self.l_margin + 3)
            self.multi_cell(0, 5.5, self.t("• " + it), new_x="LMARGIN", new_y="NEXT")

    def tableau(self, entetes, lignes, largeurs, taille=9):
        self.set_font(self.fam, "", taille)
        with self.table(col_widths=largeurs, text_align="LEFT", line_height=5.5,
                        headings_style=FontFace(emphasis="BOLD", fill_color=(225, 225, 225))) as tb:
            for ligne in [entetes] + lignes:
                r = tb.row()
                for c in ligne:
                    r.cell(self.t(c))
        self.ln(2)

    def sauver(self, chemin_pdf):
        chemin_pdf = Path(chemin_pdf)
        chemin_pdf.parent.mkdir(parents=True, exist_ok=True)
        self.output(str(chemin_pdf))
        print("PDF écrit :", chemin_pdf.relative_to(RACINE))
