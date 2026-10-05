import sys
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "Rapport de Prospection Commerciale", align="C", new_x="LMARGIN", new_y="NEXT")
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
pdf.cell(0, 8, "Grace Adjoua-Mensah (Directrice Commerciale)", new_x="LMARGIN", new_y="NEXT")

pdf.ln(10)

# Section 1
pdf.set_font("helvetica", "B", 12)
pdf.cell(0, 8, "1. Clinique privée (Marcory)", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("helvetica", size=11)
pdf.multi_cell(0, 6, "- Besoin identifié : Sécurisation des blocs opératoires et des réfrigérateurs à vaccins contre les délestages et micro-coupures.\n- Budget estimé : Élevé. Le client recherche une solution premium et hautement fiable.\n- Statut actuel : Prospect chaud.\n- Prochaine étape : Le directeur de la clinique attend une visite de notre directeur technique (Abdoul) pour un relevé de puissance et l'établissement d'un devis précis.")

pdf.ln(8)

# Section 2
pdf.set_font("helvetica", "B", 12)
pdf.cell(0, 8, "2. Grande Villa (Riviera)", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("helvetica", size=11)
pdf.multi_cell(0, 6, "- Besoin identifié : Autonomie totale hors réseau électrique national (le client est excédé par les coupures répétitives).\n- Budget estimé : À définir lors de l'étude technique, mais capacité financière importante.\n- Statut actuel : Prospect tiède.\n- Prochaine étape : Le client dispose déjà de deux autres devis concurrents. Nous devons proposer une offre très agressive sur les garanties et le service après-vente (SAV) pour remporter le marché.")

pdf.ln(10)
pdf.set_font("helvetica", "I", 10)
pdf.multi_cell(0, 5, "Conclusion : Je recommande une intervention rapide d'Abdoul sur la clinique de Marcory. C'est une belle opportunité pour signer notre premier gros contrat B2B.")

pdf.output(sys.argv[1])
