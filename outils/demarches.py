"""DÉMARCHES DE VOYAGE (P61, validée par l'utilisateur le 31/10/2026) : e-visa et autres formalités suivies de bout en bout.

Données : `etat/demarches.csv` (id ; destination ; demarche ; statut a_deposer|deposee|second_passage|acceptee|refusee ; depose_le ;
reponse_le ; connu ; note). La date de réponse est tirée au dépôt et reste CACHÉE (colonne `connu` = non) jusqu'au jour dit : l'application
Voyages ne montre que ce que William voit (« déposée le …, en cours d'examen »). Friction administrative de `etat/economie.md` : 30 % de
« deuxième passage demandé » (pièce à reprendre), tirée au dépôt comme procédure (jet.py --procedure).

    python outils/demarches.py liste
    python outils/demarches.py ajouter --destination ABJ --demarche "e-visa ivoirien (séjour du 21/12 au 04/01)" --note "…"
    python outils/demarches.py deposer DV001 [--quand "AAAA-MM-JJ HH:MM"]   # William a déposé : délai et friction tirés
    python outils/demarches.py echues                                      # réponses arrivées à l'horloge (à jouer, puis « repondre »)
    python outils/demarches.py repondre DV001 --statut acceptee|second_passage|refusee
"""
import argparse
import datetime as dt
import json
import random
import subprocess
import sys

from commun import ETAT, RACINE, ecrire_csv, lire_csv, maintenant_simule, utf8

FICHIER = ETAT / "demarches.csv"
COLONNES = ["id", "destination", "demarche", "statut", "depose_le", "reponse_le", "connu", "note"]
DELAI_JOURS = (2, 5)  # e-visa SNEDAI : traitement annoncé en 48 à 72 h ouvrées, parfois plus en haute saison
FRICTION = 30
VISIBLE = {"a_deposer": "à déposer", "deposee": "déposée le {d}, en cours d'examen", "second_passage": "pièce à reprendre (demande du {r})",
           "acceptee": "acceptée le {r}", "refusee": "refusée le {r}"}


def lire():
    return lire_csv(FICHIER)


def ecrire(l):
    ecrire_csv(FICHIER, l, COLONNES)


def visibles(destination, au=None):
    """Lignes que l'application Voyages affiche pour cette destination."""
    au = au or maintenant_simule()
    res = []
    for d in lire():
        if d["destination"] != destination:
            continue
        statut = d["statut"]
        if statut in ("acceptee", "second_passage", "refusee") and d["reponse_le"] and d["reponse_le"] > f"{au:%Y-%m-%d %H:%M}":
            statut = "deposee"  # la réponse tirée n'est pas encore arrivée
        fmt = lambda x: dt.datetime.fromisoformat(x).strftime("%d/%m/%Y") if x else ""
        res.append(f"Votre démarche : {d['demarche']} — " + VISIBLE[statut].format(d=fmt(d["depose_le"]), r=fmt(d["reponse_le"])))
    return res


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("liste")
    sp.add_parser("echues")
    p = sp.add_parser("ajouter")
    p.add_argument("--destination", required=True)
    p.add_argument("--demarche", required=True)
    p.add_argument("--note", default="")
    p = sp.add_parser("deposer")
    p.add_argument("id")
    p.add_argument("--quand")
    p = sp.add_parser("repondre")
    p.add_argument("id")
    p.add_argument("--statut", required=True, choices=["acceptee", "second_passage", "refusee"])
    a = ap.parse_args()
    L = lire()
    if a.cmd == "liste":
        for d in L:
            print(f"{d['id']} {d['destination']} | {d['demarche']} | {d['statut']} | déposée {d['depose_le'] or '-'} | réponse {d['reponse_le'] or '-'} ({d['connu']})")
        return 0
    if a.cmd == "ajouter":
        n = f"DV{len(L) + 1:03d}"
        L.append({"id": n, "destination": a.destination, "demarche": a.demarche, "statut": "a_deposer", "connu": "oui", "note": a.note})
        ecrire(L)
        print(f"{n} ajoutée : {a.demarche}")
        return 0
    d = next((x for x in L if x["id"] == getattr(a, "id", None)), None)
    if a.cmd == "echues":
        t = f"{maintenant_simule():%Y-%m-%d %H:%M}"
        for x in L:
            if x["connu"] == "non" and x["reponse_le"] and x["reponse_le"] <= t:
                print(f"{x['id']} : réponse due le {x['reponse_le']} ({x['statut']}) — à jouer, puis connu=oui (repondre)")
        return 0
    if d is None:
        sys.exit("Démarche inconnue")
    if a.cmd == "deposer":
        quand = dt.datetime.fromisoformat(a.quand) if a.quand else maintenant_simule().replace(tzinfo=None)
        r = subprocess.run([sys.executable, "outils/jet.py", "--procedure", "friction administrative 30 % (etat/economie.md)",
                            f"{d['id']} {d['demarche']} : deuxième passage demandé", str(FRICTION)],
                           capture_output=True, text=True, encoding="utf-8", cwd=str(RACINE))
        friction = "OUI" in (r.stdout or "").splitlines()[-1] if r.stdout else False
        jours = random.SystemRandom().randint(*DELAI_JOURS)
        reponse = (quand + dt.timedelta(days=jours)).replace(hour=random.SystemRandom().randint(8, 18), minute=random.SystemRandom().randint(0, 59))
        d.update({"statut": "second_passage" if friction else "acceptee", "depose_le": f"{quand:%Y-%m-%d %H:%M}",
                  "reponse_le": f"{reponse:%Y-%m-%d %H:%M}", "connu": "non",
                  "note": (d["note"] + " · " if d["note"] else "") + f"délai tiré : {jours} j ; friction : {'oui' if friction else 'non'}"})
        ecrire(L)
        print(f"{d['id']} déposée ; réponse le {d['reponse_le']} (cachée) : {d['statut']}")
        return 0
    if a.cmd == "repondre":
        d.update({"statut": a.statut, "connu": "oui"})
        ecrire(L)
        print(f"{d['id']} : {a.statut}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
