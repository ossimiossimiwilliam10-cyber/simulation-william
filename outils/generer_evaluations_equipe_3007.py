"""Évaluations de Grace, Mariette, Abdoul et Yves par Aïcha (lundi 30/07/2040) -> serveur/rh/evaluations/

Consigne de William (26/07) : chaque membre reçoit d'abord sa propre évaluation, individuellement, puis les fiches sont déposées dans
rh/evaluations/ (accès restreint). Matrice v1.0 : tronc commun à barème discret (10 / 5 / 0) ; critères du pôle sur 70 ; l'ajustement
discrétionnaire est réservé à la Direction générale (non appliqué par Aïcha). Première évaluation après deux semaines : aucun contrat
signé, aucune installation ; les notes de pôle portent sur les livrables et la préparation. Scores établis par le moteur à partir des
faits consignés (devis livrés, retards CNPS/ITS, pro forma de Vridi absente du serveur, CV SAV hors serveur, etc.).
"""
from osia_pdf import OsiaPDF, serveur

FICHES = [
    ("grace", "Grace Adjoua-Mensah", "directrice commerciale (pôle commercial)",
     [("1. Assiduité et ponctualité", 10, 10), ("2. Respect des directives et de la hiérarchie", 10, 10),
      ("3. Usage du serveur et traçabilité", 10, 10)],
     "Pôle commercial",
     [("4. Acquisition client", 15, 30), ("5. Qualité du pipeline", 17, 20), ("6. Marge nette", 16, 20)],
     "Deux devis émis dans les délais (villa Riviera, clinique de Marcory) ; aucun contrat signé à ce jour ; marges internes de 20 à 26 %."),
    ("mariette", "Mariette Kouadio", "directrice des ressources humaines (pôle RH et administration)",
     [("1. Assiduité et ponctualité", 10, 10), ("2. Respect des directives et de la hiérarchie", 10, 10),
      ("3. Usage du serveur et traçabilité", 10, 10)],
     "Pôle RH et administration",
     [("4. Conformité juridique", 22, 30), ("5. Gestion de la paie", 14, 20), ("6. Climat social / discipline", 15, 20)],
     "Règles de classement et contrôle du serveur en place ; note juridique confirmée par Me Kouamé ; paie de juillet préparée, "
     "premières fiches de paie à établir ; déclarations CNPS et ITS de juin régularisées en retard, avec pénalités."),
    ("abdoul", "Abdoul Karim Touré", "directeur technique (pôle technique / installation)",
     [("1. Assiduité et ponctualité", 10, 10), ("2. Respect des directives et de la hiérarchie", 5, 10),
      ("3. Usage du serveur et traçabilité", 5, 10)],
     "Pôle technique / installation",
     [("4. Qualité d'installation", 20, 30), ("5. Respect des délais", 12, 20), ("6. Satisfaction client SAV", 14, 20)],
     "Plan technique remis ; aucune installation encore ; livraison de Vridi retardée de huit jours ; pro forma du fournisseur absente "
     "de technique/."),
    ("yves", "Yves Kanga", "responsable SAV et relation client (pôle technique / installation)",
     [("1. Assiduité et ponctualité", 10, 10), ("2. Respect des directives et de la hiérarchie", 10, 10),
      ("3. Usage du serveur et traçabilité", 5, 10)],
     "Pôle technique / installation",
     [("4. Qualité d'installation", 18, 30), ("5. Respect des délais", 14, 20), ("6. Satisfaction client SAV", 12, 20)],
     "Présélection de trois candidats SAV le 18/07 (CV hors serveur) ; aucun client à suivre à ce jour."),
]

for code, nom, poste, tronc, bloc, pole, obs in FICHES:
    total = sum(n for _, n, _ in tronc) + sum(n for _, n, _ in pole)
    pdf = OsiaPDF(f"Évaluation de {nom}", "OSIA Énergies — évaluation du 30/07/2040 selon la matrice d'évaluation détaillée v1.0 (20/07/2040)")
    pdf.meta("Évalué(e)", f"{nom}, {poste}")
    pdf.meta("Évaluatrice", "Aïcha Diomandé, gérante et directrice générale")
    pdf.meta("Date", "30 juillet 2040 — remise individuelle, puis dépôt dans rh/evaluations/")
    pdf.titre1("Notes")
    lignes = []
    for i, (crit, n, m) in enumerate(tronc):
        lignes.append(["Tronc commun" if i == 0 else "", crit, str(n), str(m)])
    lignes.append(["", "Sous-total tronc commun", str(sum(n for _, n, _ in tronc)), "30"])
    for i, (crit, n, m) in enumerate(pole):
        lignes.append([bloc if i == 0 else "", crit, str(n), str(m)])
    lignes.append(["", "Sous-total du pôle", str(sum(n for _, n, _ in pole)), "70"])
    lignes.append(["Ajustement", "7. Ajustement discrétionnaire (réservé à la Direction générale)", "—", "—"])
    lignes.append(["Total", "", str(total), "100"])
    pdf.tableau(["Bloc", "Critère", "Note", "Maximum"], lignes, (34, 86, 25, 25))
    pdf.titre1("Observations")
    pdf.para("Première évaluation, après deux semaines d'activité : pas encore de contrat signé ni de chantier ; les notes du pôle portent "
             "sur les livrables et la préparation. " + obs)
    pdf.titre1("Résultat")
    pdf.para(f"Score : {total} / 100. Tranche de la matrice : de 61 à 85 / 100 — performance standard (maintien).")
    pdf.para("Aïcha Diomandé", italique=True)
    pdf.sauver(serveur("rh", "evaluations", f"evaluation_{code}_3007.pdf"))
