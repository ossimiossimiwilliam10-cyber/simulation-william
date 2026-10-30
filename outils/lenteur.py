"""LENTEUR RÉELLE DES AFFAIRES (P38, validée par l'utilisateur le 29/10/2026 : « rien ne marche du premier coup », règle 8).

Chaque démarche longue (immatriculation, abonnements, travaux, livraisons) et chaque menace qui mûrit seule (concurrents, P41) est un
FRONT « temps » de `etat/fronts.csv` (`fronts.py creer --avance temps`), avec ses paliers écrits d'avance. Chaque lundi, la table T22
(validée le 12/10/2026) dit de combien de segments il avance : 55 % rien, 35 % un, 10 % deux. Un palier atteint est joué au tour suivant
(le moteur l'écrit d'après sa description : pièce manquante, second passage, livraison partielle…).

Les PROMESSES des personnes (prise de poste, références promises, livraison annoncée) se tiennent ou non selon leur fiabilité tirée
(« oubli N % » dans `etat/personnages.csv`) : `lenteur.py promesse --pour "Nom" --libelle "…"`.

    python outils/lenteur.py semaine [--jusqua AAAA-MM-JJ] [--simule]   # les lundis non encore joués (appelé par tour.py fin)
    python outils/lenteur.py promesse --pour "Éric Koffi Yao" --libelle "prend son poste le 2 septembre"
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))
ETAT_LENTEUR = RACINE / "etat" / "lenteur.txt"
SEGMENTS = {"zero_segment": 0, "un_segment": 1, "deux_segments": 2}


def lancer(*a):
    r = subprocess.run([sys.executable, *a], capture_output=True, text=True, encoding="utf-8", cwd=str(RACINE))
    return r.returncode, (r.stdout + r.stderr).strip()


def derniere_issue():
    l = (RACINE / "memoire" / "tirages.jsonl").read_text(encoding="utf-8").strip().splitlines()[-1]
    d = json.loads(l)
    return d.get("issue") or d.get("resultat")


def dernier_lundi_joue():
    if ETAT_LENTEUR.exists():
        m = re.search(r"(\d{4}-\d{2}-\d{2})", ETAT_LENTEUR.read_text(encoding="utf-8"))
        if m:
            return dt.date.fromisoformat(m.group(1))
    return None


def semaine(jusqua, simule=False):
    import fronts
    res = []
    dernier = dernier_lundi_joue()
    lundi = jusqua - dt.timedelta(days=jusqua.weekday())
    lundis = []
    j = (dernier + dt.timedelta(days=7)) if dernier else lundi
    while j <= lundi:
        lundis.append(j)
        j += dt.timedelta(days=7)
    for l in lundis:
        for f in fronts.lire():
            if f["avance"] != "temps" or f["statut"] not in ("ouvert", "actif"):
                continue
            if simule:
                res.append(f"(essai) {f['id']} « {f['nom']} » : T22 à tirer pour la semaine du {l:%d/%m}")
                continue
            lancer("outils/jet.py", "--table", "T22", f"Front {f['id']} « {f['nom'][:60]} » : semaine du {l:%d/%m/%Y}")
            issue = derniere_issue()
            n = SEGMENTS.get(issue, 0)
            if n:
                code, sortie = lancer("outils/fronts.py", "avancer", f["id"], "--de", str(n), "--raison", f"T22 ({issue}) semaine du {l:%d/%m/%Y}")
                res.append(f"{f['id']} « {f['nom'][:50]} » avance de {n} (T22) : {sortie[:120]}")
            else:
                res.append(f"{f['id']} « {f['nom'][:50]} » : rien ne bouge cette semaine (T22)")
        if l >= dt.date(2041, 10, 7):  # 30/10/2026 (P51) : les prospects avancent ou non chaque lundi, une fois la direction commerciale en poste
            import prospects
            res += [f"prospects : {x}" for x in prospects.semaine(l, simule)]
        if not simule:
            ETAT_LENTEUR.write_text(f"dernier lundi joué : {l.isoformat()}\r\n", encoding="utf-8")
    return res


def promesse(nom, libelle):
    p = next((l for l in __import__("csv").DictReader(open(RACINE / "etat" / "personnages.csv", encoding="utf-8"), delimiter=";") if l["nom"] == nom), None)
    if p is None:
        sys.exit(f"Personnage inconnu : {nom}")
    m = re.search(r"oubli (\d+) %", p["traits"])
    oubli = int(m.group(1)) if m else 12
    code, sortie = lancer("outils/jet.py", "--procedure", "fiabilité tirée du personnage (lenteur.py)", f"{nom} tient sa promesse : {libelle}", str(100 - oubli))
    return f"{sortie.splitlines()[-1] if sortie else ''} (fiabilité de {nom} : {100 - oubli} %)"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("semaine")
    p.add_argument("--jusqua")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("promesse")
    p.add_argument("--pour", required=True)
    p.add_argument("--libelle", required=True)
    a = ap.parse_args()
    if a.cmd == "semaine":
        if a.jusqua:
            jusqua = dt.date.fromisoformat(a.jusqua)
        else:
            import horloge
            jusqua = horloge.lire()["instant"].date()
        for l in semaine(jusqua, a.simule) or ["lenteur : aucun front « temps » à faire avancer (ou lundi déjà joué)"]:
            print(" ", l)
    else:
        print(promesse(a.pour, a.libelle))
    return 0


if __name__ == "__main__":
    sys.exit(main())
