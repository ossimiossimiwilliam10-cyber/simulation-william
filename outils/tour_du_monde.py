"""Tour du monde : tire la journée de chaque personnage récurrent dans la table T11 (vie propre), d'après `etat/vies-propres.md`.

Mécanisme validé par l'utilisateur le 09/08/2040. À lancer à chaque fin de journée simulée et à chaque « Go » :
    python outils/tour_du_monde.py 09/08            # tire et consigne (memoire/tirages-aleas.md)
    python outils/tour_du_monde.py 09/08 --simule   # essai, rien n'est consigné
Chaque fiche (« ### Nom ») porte une ligne « - **Modificateurs T11** : M80, M81 » (ou « — »). Les tirages passent par `outils/jet.py`
(table T11), qui consigne lui-même. Le contenu de chaque journée se choisit ensuite d'après la fiche (test d'intérêt).
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
FICHES = RACINE / "etat" / "vies-propres.md"
for flux in (sys.stdout, sys.stderr):
    if hasattr(flux, "reconfigure"):
        flux.reconfigure(encoding="utf-8")


def lire_fiches():
    personnages, courant = [], None
    for ligne in FICHES.read_text(encoding="utf-8").splitlines():
        if ligne.startswith("### "):
            courant = {"nom": ligne[4:].strip(), "mods": []}
            personnages.append(courant)
        elif courant and "**Modificateurs T11**" in ligne:
            courant["mods"] = re.findall(r"M\d{2}", ligne)
        elif ligne.startswith("## ") and courant:
            courant = None
    return personnages


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("date", help="jour simulé, JJ/MM")
    ap.add_argument("--simule", action="store_true", help="ne consigne rien")
    args = ap.parse_args()
    for p in lire_fiches():
        cmd = [sys.executable, str(RACINE / "outils" / "jet.py"), "--table", "T11"]
        for m in p["mods"]:
            cmd += ["--mod", m]
        if args.simule:
            cmd.append("--simule")
        cmd.append(f"Tour du monde du {args.date} : {p['nom']}")
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        sortie = [l for l in res.stdout.splitlines() if l.startswith("- Tirage")]
        issue = re.search(r"→ \*\*(\w+)\*\*", sortie[0]).group(1) if sortie else "ERREUR : " + (res.stderr.strip() or res.stdout.strip())
        print(f"{p['nom']} : {issue}")


if __name__ == "__main__":
    main()
