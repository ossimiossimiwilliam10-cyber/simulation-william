import os
from fpdf import FPDF

employes = [
    {"nom": "Aicha Diomande", "poste": "Gerante (par procuration)", "salaire": "750 000 FCFA Net", "debut": "22/05/2040", "type": "CDD (2 ans)"},
    {"nom": "Mariette Kouadio", "poste": "Responsable RH et Administrative", "salaire": "650 000 FCFA Net", "debut": "01/06/2040", "type": "CDD (2 ans)"},
    {"nom": "Grace Adjoua-Mensah", "poste": "Directrice Commerciale", "salaire": "850 000 FCFA Net + 2% sur CA", "debut": "16/07/2040", "type": "CDD (2 ans)"},
    {"nom": "Abdoul Toure", "poste": "Directeur Technique", "salaire": "900 000 FCFA Net", "debut": "16/07/2040", "type": "CDD (2 ans)"},
    {"nom": "Yves Kanga", "poste": "Responsable SAV", "salaire": "600 000 FCFA Net", "debut": "16/07/2040", "type": "CDD (2 ans)"}
]

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "OSIA Énergies - Contrat de Travail", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

for emp in employes:
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)
    
    texte = (
        f"ENTRE LES SOUSSIGNÉS :\n\n"
        f"La société OSIA Énergies, représentée par son Gérant M. William Ossimi.\n\n"
        f"ET\n\n"
        f"M/Mme {emp['nom']}\n\n"
        f"Il a été convenu ce qui suit :\n\n"
        f"Article 1 : Engagement\n"
        f"Le salarié est engagé en qualité de {emp['poste']} à compter du {emp['debut']}.\n\n"
        f"Article 2 : Type de contrat\n"
        f"Le présent contrat est un {emp['type']}.\n\n"
        f"Article 3 : Rémunération\n"
        f"La rémunération mensuelle est fixée à {emp['salaire']}.\n\n"
        f"Article 4 : Lieu de travail\n"
        f"Le lieu de travail principal est fixé au QG d'OSIA Énergies, Abidjan, Cocody Ambassades.\n\n"
        f"(Ceci est une copie numérisée du contrat original signé.)\n\n"
        f"Signatures :\n"
        f"[Signature Employeur]                                [Signature {emp['nom']}]"
    )
    
    pdf.multi_cell(0, 7, texte)
    
    filename = f"contrat_{emp['nom'].split(' ')[0].lower()}.pdf"
    pdf.output(filename)
