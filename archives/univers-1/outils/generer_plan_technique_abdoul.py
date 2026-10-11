"""Plan technique d'Abdoul (équipe d'installation et SAV) -> serveur/technique/plan_technique_2607.pdf

Promis « très vite » le 20/07, « Jeudi. » le 23/07, « cet après-midi » le 26/07 (12h58) ; déposé le jeudi 26/07/2040 à 16h41
(jets : remis aujourd'hui 60 % OUI ; avant 16h 50 % NON). Salaires projetés en 2040 à partir des fourchettes ivoiriennes de 2025-2026
(technicien BAC+2 : 180 000 à 400 000 FCFA, moyenne 250 000 ; SMIG 75 000) majorées d'environ 35 %. Abdoul écrit court, chiffré,
et place Bertin Assi en sous-traitant (il le protège ; il ne lui a pas encore annoncé).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Plan technique — équipe d'installation et SAV",
              "OSIA Énergies — Abdoul Karim Touré, directeur technique — 26/07/2040")
pdf.meta("Objet", "Constituer l'équipe qui installe et entretient nos systèmes solaires, au rythme des contrats signés")
pdf.meta("Base", "Clinique de Marcory (devis le 27/07, 18 à 24 M FCFA), villa Riviera (devis le 26/07), toit du QG (10 kWc + 20 kWh)")

pdf.titre1("1. Principe")
pdf.para("Pas d'embauche avant le premier contrat signé. Dès la signature de la clinique, on recrute le noyau ; on renforce après le deuxième contrat. "
         "Les gros chantiers de pose passent en sous-traitance encadrée pour ne pas payer une équipe à l'arrêt.")

pdf.titre1("2. Noyau (dès la signature du premier contrat)")
pdf.tableau(["Poste", "Profil", "Nombre", "Salaire brut mensuel (FCFA)"], [
    ["Chef d'équipe électricien", "BT, habilitation électrique, 8 ans de chantier", "1", "550 000"],
    ["Technicien installateur", "BTS électrotechnique, pose photovoltaïque", "2", "380 000 chacun"],
    ["Aide-monteur", "Manœuvre formé sur chantier", "2", "160 000 chacun"],
    ["Technicien SAV", "BTS électronique (trois CV présélectionnés par Yves le 18/07)", "1", "350 000"],
], (45, 70, 18, 37))
pdf.para("Masse salariale brute du noyau : 1 980 000 FCFA par mois, soit environ 2 380 000 FCFA avec les charges patronales (environ 20 %, à confirmer par Mariette).")
pdf.para("Yves reste responsable du SAV et de la relation client ; le technicien SAV travaille sous lui.")

pdf.titre1("3. Renfort (après le deuxième contrat)")
pdf.puces(["Un technicien installateur supplémentaire (380 000 FCFA).", "Un aide-monteur supplémentaire (160 000 FCFA)."])

pdf.titre1("4. Sous-traitance")
pdf.para("Bertin Assi (électricien, Yopougon) en sous-traitant pour la pose sur les gros chantiers, au forfait par chantier, sous la "
         "responsabilité du chef d'équipe. Contrat écrit, prix fixé avant chaque chantier, réception par OSIA.")

pdf.titre1("5. Matériel")
pdf.tableau(["Poste", "Estimation (FCFA)"], [
    ["Outillage et EPI pour six personnes", "2 500 000"],
    ["Appareils de mesure (pince, mégohmmètre, analyseur de réseau)", "1 800 000"],
    ["Habilitations électriques et formation sécurité", "600 000"],
    ["Véhicule utilitaire : location au chantier au début, achat d'occasion après trois chantiers", "45 000 par jour de location"],
], (120, 50))

pdf.titre1("6. Fournisseurs")
pdf.para("Fournisseur de Vridi : onduleurs hybrides et batteries gel (commande du 18/07, livraison vers le 3 août, 4 % sur la prochaine commande). "
         "Pour la clinique (bloc opératoire, froid des vaccins), je recommande des batteries lithium fer phosphate : plus chères à l'achat, "
         "plus de cycles, pas d'entretien.")

pdf.titre1("7. Calendrier")
pdf.puces(["Semaine 1 après la signature : commande du matériel, publication des postes.",
           "Semaines 2 à 3 : entretiens, recrutement du noyau, habilitations.",
           "Semaines 4 à 6 : premier chantier (clinique), selon les délais du fournisseur."])
pdf.para("Abdoul Karim Touré", italique=True)

pdf.sauver(serveur("technique", "plan_technique_2607.pdf"))
