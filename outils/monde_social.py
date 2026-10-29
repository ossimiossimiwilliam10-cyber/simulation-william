"""VIE SOCIALE ENTRE PERSONNAGES (P37, validée par l'utilisateur le 29/10/2026 : « si on force une interaction, ça ne va pas être réaliste »).

Rien n'est forcé : chaque jour, pour chaque paire de personnages d'un même groupe (`etat/groupes.csv` : équipe, club, profession…), un
contact a lieu ou non (probabilité du groupe, moitié moins le week-end pour un groupe de travail) ; s'il a lieu, son issue est TIRÉE :
rien de notable (le plus souvent), échange banal, information transmise, tension, service rendu. Une information ne circule que si
celui qui la connaît la répète : un bavard (« aime les commérages ») le fait souvent, un discret (« discret : ne répète rien ») presque
jamais ; elle s'écrit alors dans `etat/savoir.csv` (canal « bouche-à-oreille »). William ne voit RIEN de ce fichier : seulement des traces
(une allusion, un ton, un message), que le moteur tire de `etat/monde-social.csv` quand elles le concernent.

    python outils/monde_social.py avancer [--jusqua AAAA-MM-JJ] [--simule]   # jours non encore joués (appelé par tour.py fin)
    python outils/monde_social.py voir [--jours 7]                           # les derniers contacts (moteur seul)

Tous les tirages sont consignés dans memoire/tirages.jsonl (mode « monde_social »), jamais rejoués.
"""
import argparse
import csv
import datetime as dt
import random
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))
GROUPES = RACINE / "etat" / "groupes.csv"
JOURNAL = RACINE / "etat" / "monde-social.csv"
COLS = ["date", "groupe", "a", "b", "issue", "detail"]
ISSUES = [("rien", 55), ("banal", 20), ("information", 12), ("tension", 8), ("service", 5)]
GENS = None


def lire_csv(p):
    if not p.exists():
        return []
    return list(csv.DictReader(open(p, encoding="utf-8"), delimiter=";"))


def personnages():
    global GENS
    if GENS is None:
        GENS = {l["nom"]: l for l in lire_csv(RACINE / "etat" / "personnages.csv")}
    return GENS


def present(nom):
    p = personnages().get(nom)
    return p is not None and p["statut"] in ("figurant", "recurrent")


def bavardage(nom):
    """Probabilité que ce personnage répète une information qu'il connaît."""
    t = (personnages().get(nom) or {}).get("traits", "")
    if "commérages" in t or "répète ce qu'on lui confie" in t:
        return 0.6
    if "discret" in t:
        return 0.05
    m = re.search(r"\bE(\d{2})\b", t)
    return 0.35 if m and int(m.group(1)) >= 60 else 0.2


def deja_joue():
    l = lire_csv(JOURNAL)
    return max((x["date"] for x in l), default=None)


def ecrire(lignes):
    neuf = not JOURNAL.exists()
    with open(JOURNAL, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, delimiter=";", lineterminator="\r\n")
        if neuf:
            w.writeheader()
        for l in lignes:
            w.writerow({k: str(l[k]).replace(";", ",") for k in COLS})


def consigner(libelle, issue, jet):
    try:
        import jet as j
        j.consigner_json({"mode": "monde_social", "libelle": libelle, "issue": issue, "jet": round(jet, 2)})
    except Exception:  # noqa: BLE001 : la consignation ne doit jamais bloquer le tour
        pass


def tirer_issue(rng):
    x = rng.random() * 100
    cumul = 0
    for nom, pc in ISSUES:
        cumul += pc
        if x < cumul:
            return nom, x
    return ISSUES[-1][0], x


def information(a, b, jour, rng, simule):
    """A répète-t-il à B un fait qu'il connaît et que B ignore ? -> description ou None."""
    import savoir
    faits_a = {l["fait"] for l in savoir.lire() if l["personne"] == a}
    faits_b = {l["fait"] for l in savoir.lire() if l["personne"] == b}
    a_slug = re.sub(r"[^a-z]+", "_", a.lower())
    candidats = sorted(f for f in faits_a - faits_b if not f.startswith("secret_" + a_slug.split("_")[0]))
    if not candidats:
        return None
    fait = rng.choice(candidats)
    p = bavardage(a)
    x = rng.random()
    if not simule:
        consigner(f"{a} répète-t-il « {fait} » à {b} ? (probabilité {p:.2f})", "oui" if x < p else "non", x * 100)
    if x >= p:
        return None
    if not simule:
        lignes = savoir.lire()
        lignes.append({"fait": fait, "personne": b, "canal": f"bouche-à-oreille ({a})", "date": jour.isoformat(),
                       "note": f"appris de {a} lors d'un contact du {jour:%d/%m/%Y} (monde_social)"})
        savoir.ecrire(lignes)
    return f"{a} a parlé à {b} de « {fait} »"


def jour_suivant(jour, rng, simule=False):
    lignes = []
    for g in lire_csv(GROUPES):
        membres = [m.strip() for m in g["membres"].split("·") if m.strip() and present(m.strip())]
        p = float(g["force"])
        if g["type"] == "travail" and jour.weekday() >= 5:
            p /= 2
        for i, a in enumerate(membres):
            for b in membres[i + 1:]:
                x = rng.random()
                if x >= p:
                    continue
                issue, jet = tirer_issue(rng)
                if not simule:
                    consigner(f"contact {a} / {b} ({g['groupe']}) le {jour:%d/%m/%Y}", issue, jet)
                detail = ""
                if issue == "information":
                    a1, b1 = (a, b) if rng.random() < 0.5 else (b, a)
                    detail = information(a1, b1, jour, rng, simule) or "rien d'intéressant à se dire"
                elif issue == "tension":
                    detail = "désaccord ou agacement entre eux (se lit dans leur ton, leurs retards, leurs messages)"
                elif issue == "service":
                    detail = "l'un rend un service à l'autre (crédit de confiance)"
                elif issue == "banal":
                    detail = "échange ordinaire"
                if issue != "rien":
                    lignes.append({"date": jour.isoformat(), "groupe": g["groupe"], "a": a, "b": b, "issue": issue, "detail": detail})
    return lignes


def avancer(jusqua, simule=False):
    """Joue les jours de (dernier jour joué + 1) à `jusqua` inclus ; renvoie les lignes notables."""
    rng = random.SystemRandom()
    dernier = deja_joue()
    debut = dt.date.fromisoformat(dernier) + dt.timedelta(days=1) if dernier else jusqua
    res, jour = [], debut
    while jour <= jusqua:
        lignes = jour_suivant(jour, rng, simule)
        if lignes and not simule:
            ecrire(lignes)
        if not lignes and not simule and not dernier:
            ecrire([{"date": jour.isoformat(), "groupe": "-", "a": "-", "b": "-", "issue": "debut", "detail": "premier jour joué par monde_social"}])
        res += lignes
        dernier = jour.isoformat()
        jour += dt.timedelta(days=1)
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("avancer")
    p.add_argument("--jusqua")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("voir")
    p.add_argument("--jours", type=int, default=7)
    a = ap.parse_args()
    if a.cmd == "avancer":
        if a.jusqua:
            jusqua = dt.date.fromisoformat(a.jusqua)
        else:
            import horloge
            jusqua = horloge.lire()["instant"].date()
        lignes = avancer(jusqua, a.simule)
        print(f"{'(essai) ' if a.simule else ''}monde social : {len(lignes)} contact(s) notable(s) jusqu'au {jusqua:%d/%m/%Y}")
        for l in lignes[:15]:
            print(f"  {l['date']} {l['groupe']} : {l['a']} / {l['b']} : {l['issue']} ({l['detail']})")
    else:
        lignes = lire_csv(JOURNAL)[-50:]
        for l in lignes:
            print(f"  {l['date']} {l['groupe']} : {l['a']} / {l['b']} : {l['issue']} ({l['detail']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
