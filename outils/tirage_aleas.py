"""Tirage d'aléas avec un VRAI hasard (un modèle de langage ne sait pas tirer au sort : on le fait ici).

    python outils/tirage_aleas.py 2040-07-23            # tire les aléas « actifs » pour la semaine commençant à cette date
    python outils/tirage_aleas.py 2040-07-23 --simule   # affiche sans écrire dans le journal des tirages

Lit `etat/aleas.md` (tableau Markdown : ID | Événement | Probabilité par semaine | Statut | Effets / conditions).
Ne tire que les lignes dont le statut est « actif » (validées par l'utilisateur lors de la revue du lundi).
Chaque tirage est consigné dans `memoire/tirages-aleas.md` pour la traçabilité (le moteur ne triche pas, ne rejoue pas).
"""
import argparse
import random
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def lire_catalogue(fichier):
    evenements = []
    for ligne in Path(fichier).read_text(encoding="utf-8").splitlines():
        if not ligne.startswith("|"):
            continue
        cases = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cases) < 5 or not re.fullmatch(r"A\d+", cases[0]):
            continue
        m = re.search(r"(\d+(?:[.,]\d+)?)\s*%", cases[2])
        if not m:
            continue
        evenements.append({
            "id": cases[0], "nom": cases[1], "proba": float(m.group(1).replace(",", ".")),
            "statut": cases[3].lower(), "effets": cases[4],
        })
    return evenements


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date", help="AAAA-MM-JJ, début de la semaine tirée")
    ap.add_argument("--fichier", default=str(RACINE / "etat" / "aleas.md"))
    ap.add_argument("--simule", action="store_true", help="ne pas écrire dans memoire/tirages-aleas.md")
    args = ap.parse_args()

    actifs = [e for e in lire_catalogue(args.fichier) if e["statut"] == "actif"]
    if not actifs:
        print("Aucun aléa « actif » dans le catalogue : rien à tirer (valider d'abord lors de la revue du lundi).")
        return 0

    hasard = random.SystemRandom()
    lignes, declenches = [], []
    for e in actifs:
        jet = hasard.uniform(0, 100)
        tombe = jet < e["proba"]
        lignes.append(f"| {e['id']} | {e['nom']} | {e['proba']:g} % | {jet:5.1f} | {'**DÉCLENCHÉ**' if tombe else 'non'} |")
        if tombe:
            declenches.append(e)

    sortie = [f"## Tirage de la semaine du {args.date}", "",
              "| ID | Événement | Probabilité | Jet (0-100) | Résultat |", "|---|---|---|---|---|", *lignes, ""]
    if declenches:
        sortie.append("Effets à jouer : " + " ; ".join(f"{e['id']} : {e['effets']}" for e in declenches))
    else:
        sortie.append("Aucun aléa déclenché cette semaine.")
    texte = "\n".join(sortie)
    print(texte)

    if not args.simule:
        journal = RACINE / "memoire" / "tirages-aleas.md"
        if not journal.exists():
            journal.write_text("# Journal des tirages d'aléas (ne jamais effacer, ne jamais rejouer)\n\n", encoding="utf-8")
        with journal.open("a", encoding="utf-8") as f:
            f.write("\n" + texte + "\n")
        print("\nConsigné dans", journal.relative_to(RACINE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
