import sys
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 14)
        self.cell(0, 10, "Charte Interne et Système d'Évaluation - OSIA Énergies", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()

# Metadonnees
pdf.set_font("helvetica", "B", 10)
pdf.cell(30, 6, "Date : ", new_x="RIGHT")
pdf.set_font("helvetica", size=10)
pdf.cell(0, 6, "19/07/2040", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("helvetica", "B", 10)
pdf.cell(30, 6, "Auteurs : ", new_x="RIGHT")
pdf.set_font("helvetica", size=10)
pdf.cell(0, 6, "Aïcha Diomandé, Mariette Kouadio, Grace Adjoua-Mensah, Abdoul Touré, Yves Kanga", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

# Section 1 : Reglement Interieur
pdf.set_font("helvetica", "B", 12)
pdf.cell(0, 8, "1. Règlement Intérieur (Charte)", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("helvetica", size=10)
reglement = (
    "- Horaires de travail : 08h00 - 17h00 (pause de 12h30 à 13h30).\n"
    "- Confidentialité : Interdiction stricte de divulguer les informations financières, les salaires et les données clients.\n"
    "- Pôle Technique : Port obligatoire des EPI (Équipements de Protection Individuelle) sur les chantiers. Entretien rigoureux du matériel.\n"
    "- Pôle Commercial & Direction : Tenue professionnelle exigée au QG et en rendez-vous.\n"
    "- Congés (Futurs contrats) : 2,2 jours ouvrables par mois de présence effective, conformément au code du travail ivoirien."
)
pdf.multi_cell(0, 5, reglement)
pdf.ln(5)

# Section 2 : Systeme d'evaluation (Bareme sur 100)
pdf.set_font("helvetica", "B", 12)
pdf.cell(0, 8, "2. Barème d'Évaluation Trimestrielle (sur 100 points)", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("helvetica", size=10)
bareme = (
    "- Objectifs quantitatifs (40 pts) : CA généré (Commercial), délais respectés (Technique), rigueur budgétaire (Direction).\n"
    "- Qualité et Satisfaction (30 pts) : Taux de SAV, retours clients, absence d'erreurs administratives.\n"
    "- Comportement et Esprit d'équipe (20 pts) : Ponctualité, entraide, respect de la charte interne.\n"
    "- Initiative et Leadership (10 pts) : Force de proposition, résolution de problèmes."
)
pdf.multi_cell(0, 5, bareme)
pdf.ln(5)

# Section 3 : Primes et Sanctions
pdf.set_font("helvetica", "B", 12)
pdf.cell(0, 8, "3. Primes, Sanctions et Conséquences", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("helvetica", size=10)
primes = (
    "- Score >= 85/100 : Attribution d'une prime trimestrielle de 150 000 FCFA (Cadres) / 50 000 FCFA (Employés).\n"
    "- Score de 50 à 84/100 : Performance standard, maintien du poste sans prime.\n"
    "- Score < 50/100 : Avertissement écrit, plan d'amélioration sur 1 mois.\n"
    "- Score < 30/100 (ou récidive < 50) : Faute grave. Convocation pour licenciement avec indemnités minimales légales."
)
pdf.multi_cell(0, 5, primes)
pdf.ln(5)

pdf.set_font("helvetica", "I", 10)
pdf.multi_cell(0, 5, "Note de l'équipe : Nous, soussignés, validons ce système et considérons la période actuelle comme une 'période de grâce' pour l'ajuster. Le présent document servira de base au règlement intérieur officiel déposable à l'Inspection du Travail.")

pdf.output(sys.argv[1])
