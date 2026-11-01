"""PROSPECTS DE SOLEIL B2B CI (P51, validée par l'utilisateur le 30/10/2026) : chaque client potentiel a une étape
(cible, rendez-vous, devis, négociation, signé, perdu) et avance ou non chaque lundi selon une probabilité TIRÉE, jamais choisie
par le moteur. Probabilités par semaine (modifiables par l'utilisateur seul, dans TRANSITIONS) ; un concurrent cité par le
prospect retire 10 points ; aucune avance commerciale tant que la direction commerciale n'est pas en poste (avant le 01/10/2041).

    python outils/prospects.py liste
    python outils/prospects.py semaine --lundi 2041-10-07 [--simule]     # appelé par lenteur.py chaque lundi
    python outils/prospects.py ajouter --nom "…" --secteur "…" [--etape rendez_vous] [--note "…"]
"""
import argparse
import csv
import datetime as dt
import random
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))
FICHIER = RACINE / "etat" / "prospects.csv"
COLS = ["id", "nom", "secteur", "etape", "concurrent", "maj", "note"]
# étape -> (étape suivante, probabilité par semaine d'y passer, probabilité par semaine d'être perdu)
TRANSITIONS = {"cible": ("rendez_vous", 0.12, 0.03), "rendez_vous": ("devis", 0.45, 0.10),
               "devis": ("negociation", 0.40, 0.12), "negociation": ("signe", 0.30, 0.15)}


def lire():
    return list(csv.DictReader(open(FICHIER, encoding="utf-8"), delimiter=";")) if FICHIER.exists() else []


def ecrire(l):
    # 01/11/2026 (U3-28) : un « ; » dans une note avait deux fois vidé le fichier (champ en trop, écriture interrompue) ;
    # les champs en trop rejoignent la note, les « ; » deviennent des virgules, et l'écriture passe par un fichier temporaire
    propres = []
    for p in l:
        extra = p.pop(None, None)
        if extra:
            p["note"] = ", ".join([p.get("note") or ""] + [x for x in extra if x])
        propres.append({k: (p.get(k) or "").replace(";", ",") for k in COLS})
    tmp = FICHIER.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, delimiter=";", lineterminator="\r\n")
        w.writeheader()
        w.writerows(propres)
    tmp.replace(FICHIER)


def semaine(lundi, simule=False):
    import jet
    res, l = [], lire()
    rng = random.SystemRandom()
    for p in l:
        if p["etape"] not in TRANSITIONS:
            continue
        suiv, pa, pp = TRANSITIONS[p["etape"]]
        if p.get("concurrent"):
            pa = max(0.0, pa - 0.10)
        x = rng.random()
        issue = "avance" if x < pa else "perdu" if x < pa + pp else "rien"
        if not simule:
            jet.consigner_json({"mode": "prospects", "libelle": f"{p['nom']} ({p['etape']}) semaine du {lundi:%d/%m/%Y}", "issue": issue, "jet": round(x * 100, 1)})
            if issue != "rien":
                p["etape"] = suiv if issue == "avance" else "perdu"
                p["maj"] = lundi.isoformat()
        if issue != "rien":
            res.append(f"{p['nom']} : {issue} -> {suiv if issue == 'avance' else 'perdu'}")
    if not simule:
        ecrire(l)
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("liste")
    s = sp.add_parser("semaine"); s.add_argument("--lundi", required=True); s.add_argument("--simule", action="store_true")
    s = sp.add_parser("ajouter"); s.add_argument("--nom", required=True); s.add_argument("--secteur", default=""); s.add_argument("--etape", default="cible"); s.add_argument("--note", default=""); s.add_argument("--concurrent", default="")
    a = ap.parse_args()
    if a.cmd == "liste":
        for p in lire():
            print(f"{p['id']} {p['etape']:12s} {p['nom']} ({p['secteur']}){' · concurrent : ' + p['concurrent'] if p['concurrent'] else ''}")
    elif a.cmd == "semaine":
        for r in semaine(dt.date.fromisoformat(a.lundi), a.simule) or ["rien ne bouge"]:
            print(" ", r)
    else:
        l = lire()
        l.append({"id": f"PR{len(l) + 1:03d}", "nom": a.nom, "secteur": a.secteur, "etape": a.etape, "concurrent": a.concurrent, "maj": "", "note": a.note})
        ecrire(l)
        print("ajouté")
    return 0


if __name__ == "__main__":
    sys.exit(main())
