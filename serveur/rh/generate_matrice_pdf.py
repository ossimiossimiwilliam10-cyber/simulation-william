import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "Matrice d'Evaluation Detaillee - OSIA Energies", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "I", 10)
        self.cell(0, 10, "Version 1.0 - Redigee par Aicha Diomande et Mariette Kouadio (20/07/2040)", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

texte = """
Bareme Commun (Tronc Commun - 30 points)
1. Assiduite et Ponctualite (10 pts)
   - Aucun retard : 10 pts
   - 1 a 2 retards justifies : 5 pts
   - Retard non justifie ou absence : 0 pt

2. Respect des directives et Hierarchie (10 pts)
   - Execution immediate et sans faille : 10 pts
   - Execution avec rappel : 5 pts
   - Insubordination / Refus : 0 pt (Alerte licenciement)

3. Usage du Serveur et Tracabilite (10 pts)
   - 100% des documents numerises et classes sur le serveur : 10 pts
   - Un oubli mineur : 5 pts
   - Fichier perdu ou garde en local : 0 pt

Criteres Specifiques par Pole (70 points)

Pole Commercial (Grace Adjoua-Mensah)
1. Acquisition Client (30 pts) : Atteinte de l'objectif mensuel de contrats signes.
2. Qualite du Pipeline (20 pts) : Suivi CRM a jour, devis precis, relances effectuees.
3. Marge Nette (20 pts) : Maintien d'une marge beneficiaire elevee sans brader les prix.

Pole Technique / Installation (Abdoul Toure & Yves Kanga)
1. Qualite d'Installation (30 pts) : Aucun defaut technique, conformite electrique parfaite.
2. Respect des Delais (20 pts) : Chantier termine dans le temps imparti.
3. Satisfaction Client SAV (20 pts) : Zero plainte post-installation, interventions rapides.

Pole RH & Administration (Mariette Kouadio)
1. Conformite Juridique (30 pts) : 0 faille dans les contrats, respect du code du travail.
2. Gestion de la Paie (20 pts) : Fiches de paie exactes, versees en temps et en heure.
3. Climat Social / Discipline (20 pts) : Maintien de la rigueur sans baisse de productivite.

Direction / Gestion (Aicha Diomande)
1. Rentabilite Globale (30 pts) : Suivi de la tresorerie et respect du budget.
2. Coordination des Poles (20 pts) : Fluidite de l'information entre commercial et technique.
3. Reporting (20 pts) : Transparence totale envers le Gerant (William).

REGLE DE SANCTION ET PROMOTION :
- < 30/100 : Licenciement pour incompetence notoire + Naming & Shaming (Signalement externe).
- 30 a 60/100 : Avertissement formel.
- 61 a 85/100 : Performance standard (Maintien).
- 86 a 94/100 : Prime d'excellence de 150 000 FCFA.
- > 95/100 : Prime d'excellence + Eligibilite immediate a une promotion (Directeur ou PDG).

AJUSTEMENT DISCRETIONNAIRE (Bonus/Malus) : La Direction Generale (W. Ossimi) se reserve le droit exclusif d'ajouter ou de retirer des points a tout employe.
"""

pdf.multi_cell(0, 6, texte)
pdf.output("matrice_evaluation.pdf")
