import sys
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "Synthese des Equipes par Pole", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

pdf.set_font("helvetica", "B", 11)
pdf.cell(30, 8, "Date : ", new_x="RIGHT")
pdf.set_font("helvetica", size=11)
pdf.cell(0, 8, "18/07/2040", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("helvetica", "B", 11)
pdf.cell(30, 8, "Auteur : ", new_x="RIGHT")
pdf.set_font("helvetica", size=11)
pdf.cell(0, 8, "Mariette Kouadio (DRH)", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("helvetica", "B", 11)
pdf.cell(30, 8, "Destinataire : ", new_x="RIGHT")
pdf.set_font("helvetica", size=11)
pdf.cell(0, 8, "William Ossimi (Gerant)", new_x="LMARGIN", new_y="NEXT")

pdf.ln(10)

# Table
col_widths = [25, 35, 35, 30, 50, 20]
headers = ["Pole", "Nom", "Poste", "Salaire", "Contrat", "Evaluation"]
data = [
    ["Direction", "Aicha Diomande", "Gerante / DG", "750 000", "CDD (22/05/2040 - 21/05/2042)", ""],
    ["Direction", "Mariette Kouadio", "DRH", "650 000 (+ 10k net)", "CDD (01/06/2040 - 31/05/2042)", ""],
    ["Commercial", "Grace Adjoua", "Directrice comm.", "850 000 + 2% + b", "CDD (16/07/2040 - 15/07/2042)", ""],
    ["Technique", "Abdoul Toure", "Directeur tech.", "900 000", "CDD (16/07/2040 - 15/07/2042)", ""],
    ["Technique", "Yves Kanga", "Resp. SAV", "600 000", "CDD (16/07/2040 - 15/07/2042)", ""],
    ["Conformite", "Esther N'Guessan", "Conformite / R.", "1 000 000", "CDD (01/09/2040 - 31/08/2042)*", "Fin aout"]
]

pdf.set_font("helvetica", "B", 9)
for i in range(len(headers)):
    pdf.cell(col_widths[i], 10, headers[i], border=1, align="C")
pdf.ln()

pdf.set_font("helvetica", size=8)
for row in data:
    for i in range(len(row)):
        pdf.cell(col_widths[i], 10, row[i], border=1)
    pdf.ln()

pdf.ln(10)
pdf.set_font("helvetica", "I", 10)
pdf.multi_cell(0, 5, "*Note de la DRH : Ce tableau ne comprend pour l'instant que les cadres de l'equipe de direction. Les recrutements des sous-equipes (techniciens SAV, ouvriers poseurs) sont en cours de budgetisation par les responsables respectifs (livrables attendus pour le 31/07).")

pdf.output(sys.argv[1])
