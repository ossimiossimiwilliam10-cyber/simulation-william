"""Copies numérisées des contrats (Mariette, 20/07/2040) -> serveur/rh/contrats/contrat_<prenom>.pdf

Version corrigée le 21/07/2040 :
- salaires en BRUT (avant : « Net », en contradiction avec osia/equipe.md et avec les
  virements du 21/07 calculés sur le brut) ;
- dates de début ET de fin de CDD (24 mois, maximum légal en Côte d'Ivoire) ;
- clauses propres à Grace (éthique commerciale, révision écrite à 6 mois) ;
- accents et noms propres corrects.
Les congés payés n'y figurent pas : William les a demandés pour les FUTURS contrats (19/07).
"""
from osia_pdf import OsiaPDF, serveur

EMPLOYEUR = "La société OSIA Énergies SARL, représentée par son Gérant, M. William Ossimi"
LIEU = "le QG d'OSIA Énergies, Cocody Ambassades, Abidjan"

employes = [
    {"fichier": "aicha", "nom": "Mme Aïcha Diomandé", "poste": "Directrice générale (gérante par procuration)",
     "debut": "22/05/2040", "fin": "21/05/2042", "salaire": "750 000 FCFA brut"},
    {"fichier": "mariette", "nom": "Mme Mariette Kouadio", "poste": "Directrice des ressources humaines (RH et administration)",
     "debut": "01/06/2040", "fin": "31/05/2042", "salaire": "650 000 FCFA brut, auxquels s'ajoutent 10 000 FCFA par mois de forfait internet"},
    {"fichier": "grace", "nom": "Mme Grace Adjoua-Mensah", "poste": "Directrice commerciale",
     "debut": "16/07/2040", "fin": "15/07/2042",
     "salaire": "850 000 FCFA brut, auxquels s'ajoutent 2 % du chiffre d'affaires et un bonus trimestriel",
     "extra": [
         ("Article 5 — Éthique commerciale",
          "Sont exclus de la mission de la salariée les marchés publics ainsi que toute commission, "
          "rétro-commission ou avantage occulte, sous quelque forme que ce soit."),
         ("Article 6 — Révision",
          "Les conditions de rémunération font l'objet d'une révision écrite à l'issue des six premiers mois, "
          "soit à compter du 16/01/2041."),
     ]},
    {"fichier": "abdoul", "nom": "M. Abdoul Karim Touré", "poste": "Directeur technique",
     "debut": "16/07/2040", "fin": "15/07/2042", "salaire": "900 000 FCFA brut"},
    {"fichier": "yves", "nom": "M. Yves Kanga", "poste": "Responsable SAV et relation client",
     "debut": "16/07/2040", "fin": "15/07/2042", "salaire": "600 000 FCFA brut"},
]

for e in employes:
    pdf = OsiaPDF("Contrat de travail à durée déterminée", "OSIA Énergies SARL — copie numérisée conforme à l'original signé")
    pdf.titre1("Entre les soussignés")
    pdf.para(EMPLOYEUR + ",")
    pdf.para("et")
    pdf.para(e["nom"] + ",")
    pdf.para("il a été convenu ce qui suit.")
    articles = [
        ("Article 1 — Engagement", f"Le salarié est engagé en qualité de {e['poste']} à compter du {e['debut']}."),
        ("Article 2 — Durée", f"Le présent contrat est conclu pour une durée déterminée de vingt-quatre (24) mois, "
                              f"du {e['debut']} au {e['fin']} inclus."),
        ("Article 3 — Rémunération", f"La rémunération mensuelle est fixée à {e['salaire']}."),
        ("Article 4 — Lieu de travail", f"Le lieu de travail principal est fixé au {LIEU}."),
    ] + e.get("extra", [])
    for titre, texte in articles:
        pdf.titre1(titre)
        pdf.para(texte)
    pdf.ln(10)
    pdf.set_font(pdf.fam, "", 10)
    pdf.cell(90, 6, pdf.t("Pour la société (le Gérant)"))
    pdf.cell(0, 6, pdf.t("Le salarié"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(pdf.fam, "I", 10)
    pdf.cell(90, 6, pdf.t("[Signature — W. Ossimi]"))
    pdf.cell(0, 6, pdf.t(f"[Signature — {e['nom']}]"), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)
    pdf.para("Copie numérisée par la DRH le 20/07/2040 et classée sur le serveur de l'entreprise.", italique=True, taille=9)
    pdf.sauver(serveur("rh", "contrats", f"contrat_{e['fichier']}.pdf"))
