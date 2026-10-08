"""Copies numérisées des contrats (Mariette, 20/07/2040) -> serveur/rh/contrats/contrat_<prenom>.pdf

Version corrigée le 26/07/2040 (hors fiction, demande de l'utilisateur, corrections n° 34) : **CDI avec période d'essai**
(avant : CDD de 24 mois, erreur de réalisme du moteur précédent : un poste de direction permanent ne relève pas des cas de
recours au CDD) ; essai la plus longue possible selon la catégorie (décret n° 2024-900) : six mois pour les cadres supérieurs,
trois mois pour Yves (cadre), renouvelable une seule fois par écrit.

Version corrigée le 21/07/2040 :
- salaires en BRUT (avant : « Net », en contradiction avec osia/equipe.md et avec les
  virements du 21/07 calculés sur le brut) ;
- dates de début ET de fin de CDD (24 mois) [remplacé le 26/07 : CDI, dates de fin d'essai] ;
- clauses propres à Grace (éthique commerciale, révision écrite à 6 mois) ;
- accents et noms propres corrects.
Les congés payés n'y figurent pas : William les a demandés pour les FUTURS contrats (19/07).
"""
from osia_pdf import OsiaPDF, serveur

EMPLOYEUR = "La société OSIA Énergies SARL, représentée par son Gérant, M. William Ossimi"
LIEU = "QG d'OSIA Énergies, Cocody Ambassades, Abidjan"

employes = [
    {"fichier": "aicha", "nom": "Mme Aïcha Diomandé", "poste": "Directrice générale (gérante par procuration)",
     "debut": "22/05/2040", "essai": "six (6) mois, du 22/05/2040 au 21/11/2040 inclus", "cat": "cadre supérieur", "preavis": "un mois", "salaire": "750 000 FCFA brut"},
    {"fichier": "mariette", "nom": "Mme Mariette Kouadio", "poste": "Directrice des ressources humaines (RH et administration)",
     "debut": "01/06/2040", "essai": "six (6) mois, du 01/06/2040 au 30/11/2040 inclus", "cat": "cadre supérieur", "preavis": "un mois", "salaire": "650 000 FCFA brut, auxquels s'ajoutent 10 000 FCFA par mois de forfait internet"},
    {"fichier": "grace", "nom": "Mme Grace Adjoua-Mensah", "poste": "Directrice commerciale",
     "debut": "16/07/2040", "essai": "six (6) mois, du 16/07/2040 au 15/01/2041 inclus", "cat": "cadre supérieur", "preavis": "un mois",
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
     "debut": "16/07/2040", "essai": "six (6) mois, du 16/07/2040 au 15/01/2041 inclus", "cat": "cadre supérieur", "preavis": "un mois", "salaire": "900 000 FCFA brut"},
    {"fichier": "yves", "nom": "M. Yves Kanga", "poste": "Responsable SAV et relation client",
     "debut": "16/07/2040", "essai": "trois (3) mois, du 16/07/2040 au 15/10/2040 inclus", "cat": "cadre", "preavis": "quinze jours", "salaire": "600 000 FCFA brut"},
]

for e in employes:
    pdf = OsiaPDF("Contrat de travail à durée indéterminée", "OSIA Énergies SARL — copie numérisée conforme à l'original signé")
    pdf.titre1("Entre les soussignés")
    pdf.para(EMPLOYEUR + ",")
    pdf.para("et")
    pdf.para(e["nom"] + ",")
    pdf.para("il a été convenu ce qui suit.")
    articles = [
        ("Article 1 — Engagement", f"Le salarié est engagé en qualité de {e['poste']} à compter du {e['debut']}."),
        ("Article 2 — Durée et période d'essai", f"Le présent contrat est conclu pour une durée indéterminée. Il comporte une période "
                                                 f"d'essai de {e['essai']} (catégorie : {e['cat']}), renouvelable une seule fois par écrit "
                                                 f"notifié au salarié au moins {e['preavis']} avant son terme. Pendant la période d'essai, "
                                                 f"chacune des parties peut rompre le contrat sans préavis ni indemnité."),
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
