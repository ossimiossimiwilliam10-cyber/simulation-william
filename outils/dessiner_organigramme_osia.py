"""Image de l'organigramme cible de William (rendu de son schéma Mermaid, `organigramme_osia.md`, 05-06/08/2040).

Libellés repris tels quels ; couleurs reprises des classes du schéma (boss, ceo, dgo, dgf, pole, team).
Sortie : documents_william/2040-08-06_organigramme_osia.png (envoyée à l'utilisateur, hors fiction, le 06/08/2040).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "documents_william" / "2040-08-06_organigramme_osia.png"

STYLES = {
    "boss": dict(fc="#1a1a1a", ec="#ffffff", tc="#ffffff", gras=True, tirets=False),
    "ceo": dict(fc="#800020", ec="#ffffff", tc="#ffffff", gras=True, tirets=False),
    "dgo": dict(fc="#003366", ec="#ffffff", tc="#ffffff", gras=False, tirets=False),
    "dgf": dict(fc="#004d00", ec="#ffffff", tc="#ffffff", gras=False, tirets=False),
    "pole": dict(fc="#e6e6e6", ec="#333333", tc="#000000", gras=False, tirets=False),
    "team": dict(fc="#ffffff", ec="#666666", tc="#333333", gras=False, tirets=True),
}

# id : (texte, classe, x, y)
NOEUDS = {
    "W": ("William Ossimi\n(Président / Actionnaire)", "boss", 50, 92),
    "CEO": ("CEO / Administrateur Général\n(À recruter - Le Poids Lourd)", "ceo", 50, 74),
    "DG1": ("Directeur Général\nOpérations (COO)\n(À définir)", "dgo", 26, 55),
    "DG2": ("Directeur Général\nSupport & Finances (CFO)\n(Estelle ?)", "dgf", 74, 55),
    "P_BUS": ("Pôle Business & Client\n(Grace & Yves)", "pole", 13, 35),
    "P_TECH": ("Pôle Technique & Déploiement\n(Abdoul)", "pole", 38, 35),
    "P_SUP": ("Pôle Support & Légal\n(Mariette & Esther)", "pole", 62, 35),
    "P_FIN": ("Pôle Financier\n(Directeur Financier)", "pole", 87, 35),
    "EQ_BUS": ("Équipe Commerciale\n(2 à 3 démarcheurs terrains)", "team", 13, 14),
    "EQ_TECH": ("Équipe Technique\n(2 à 3 techniciens/installateurs)", "team", 38, 14),
    "EQ_SUP": ("Équipe Administrative\n(Assistante RH +\nAssistante Conformité)", "team", 62, 14),
    "EQ_FIN": ("Équipe Analyse\n(2 Analystes Quantitatifs /\nRisque)", "team", 87, 14),
}
LIENS = [("W", "CEO", "Reçoit le rapport hebdo"), ("CEO", "DG1", None), ("CEO", "DG2", None),
         ("DG1", "P_BUS", None), ("DG1", "P_TECH", None), ("P_BUS", "EQ_BUS", None), ("P_TECH", "EQ_TECH", None),
         ("DG2", "P_SUP", None), ("DG2", "P_FIN", None), ("P_SUP", "EQ_SUP", None), ("P_FIN", "EQ_FIN", None)]
LARGEUR, HAUTEUR = 22, 10

fig, ax = plt.subplots(figsize=(16, 10), dpi=150)
ax.set_xlim(0, 100)
ax.set_ylim(0, 102)
ax.axis("off")
fig.patch.set_facecolor("#ffffff")

for a, b, etiquette in LIENS:
    xa, ya = NOEUDS[a][2], NOEUDS[a][3] - HAUTEUR / 2
    xb, yb = NOEUDS[b][2], NOEUDS[b][3] + HAUTEUR / 2
    ax.annotate("", xy=(xb, yb), xytext=(xa, ya),
                arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.4, shrinkA=0, shrinkB=0))
    if etiquette:
        ax.text((xa + xb) / 2 + 1, (ya + yb) / 2, etiquette, fontsize=9, color="#333333", va="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="#f5f5f5", ec="#cccccc"))

for code, (texte, classe, x, y) in NOEUDS.items():
    s = STYLES[classe]
    boite = FancyBboxPatch((x - LARGEUR / 2, y - HAUTEUR / 2), LARGEUR, HAUTEUR,
                           boxstyle="round,pad=0.4,rounding_size=1.2", fc=s["fc"], ec=s["ec"], lw=1.5,
                           linestyle="--" if s["tirets"] else "-")
    if s["fc"] != "#ffffff" and s["ec"] == "#ffffff":
        boite.set_edgecolor("#222222")
    ax.add_patch(boite)
    ax.text(x, y, texte, ha="center", va="center", fontsize=9.5, color=s["tc"],
            fontweight="bold" if s["gras"] else "normal", linespacing=1.3)

ax.set_title("Organigramme cible d'OSIA Énergies", fontsize=16, fontweight="bold", pad=12)
SORTIE.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(SORTIE, bbox_inches="tight", facecolor=fig.get_facecolor())
print("Image écrite :", SORTIE.relative_to(RACINE))
