"""BILAN DES TIRAGES POUR OU CONTRE WILLIAM (P65, validée par l'utilisateur le 01/11/2026 : « je valide tout »).

À chaque revue mensuelle, le moteur montre au joueur, chiffres à l'appui, si le monde a penché pour ou contre William : pour chaque table
où l'issue a un sens pour lui, la part favorable, neutre et défavorable observée, comparée à la part attendue (pourcentages de
`etat/modele-pouvoir.md`), et la probabilité d'un tel écart par le seul hasard. Lecture seule : rien n'est écrit.

    python outils/bilan_tirages.py --depuis 2026-10-27          # date d'enregistrement (heure machine) du premier tirage compté
"""
import argparse
import collections
import io
import json
import sys
from math import comb
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

# issue -> sens pour William (+1 favorable, 0 neutre, -1 défavorable)
SENS = {
    "T7b": {"succes_net": 1, "succes_cout": 0, "doute_visible": -1, "incredule_silencieux": -1, "frontal_dement": -1},
    "T7c": {"execute_sans_discuter": 1, "execute_a_contrecoeur": 0, "execute_partiellement": -1, "frontal_refus": -1},
    "T12": {"concede_beaucoup": 1, "concede_un_peu": 1, "temporise": 0, "maintient_sa_position": -1},
    "T15": {"accepte_volontiers": 1, "rien_laisse_passer": 0, "en_parle_a_d_autres": 0, "rend_la_pareille": 0,
            "demande_explication": 0, "garde_distance": -1, "decline": -1, "frontal_conflit": -1},
    "T17": {"reciproque": 1, "conversation": 1, "poli_bref": 0, "ignore": -1, "mefiance": -1, "refus_net": -1},
    "T26": {"favorable": 1, "neutre": 0, "defavorable": -1},
}


def attendus():
    import jet
    tables, _ = jet.charger()
    res = {}
    for t, sens in SENS.items():
        if t not in tables:
            continue
        tot = {1: 0.0, 0: 0.0, -1: 0.0}
        for nom, pct, _ in tables[t]["issues"]:
            tot[sens.get(nom, 0)] += float(pct)
        s = sum(tot.values()) or 1
        res[t] = {k: v / s for k, v in tot.items()}
    return res


def p_queue(n, k, p, haut):
    if haut:
        return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--depuis", required=True)
    a = ap.parse_args()
    obs = collections.defaultdict(collections.Counter)
    prospects = collections.Counter()
    for l in io.open(RACINE / "memoire" / "tirages.jsonl", encoding="utf-8"):
        try:
            d = json.loads(l)
        except ValueError:
            continue
        if d.get("enregistre", "") < a.depuis or d.get("simule"):
            continue
        if d.get("mode") == "prospects":
            prospects[d.get("issue")] += 1
            continue
        t = d.get("table")
        if t in SENS:
            obs[t][SENS[t].get(d.get("issue") or d.get("resultat"), 0)] += 1
    try:
        att = attendus()
    except Exception:  # le format interne de jet.py a changé : on montre les observations seules
        att = {}
    print(f"Bilan des tirages enregistrés depuis le {a.depuis} (favorable / neutre / défavorable à William)")
    for t in SENS:
        c = obs.get(t)
        if not c:
            continue
        n = sum(c.values())
        ligne = f"  {t} : {c[1]} / {c[0]} / {c[-1]} sur {n}"
        if t in att:
            e = att[t]
            ligne += f" ; attendu {e[1]:.0%} / {e[0]:.0%} / {e[-1]:.0%}"
            pf = p_queue(n, c[1], e[1], c[1] / n > e[1])
            pd = p_queue(n, c[-1], e[-1], c[-1] / n > e[-1])
            ligne += f" ; hasard d'un tel écart : favorables {pf:.0%}, défavorables {pd:.0%}"
        print(ligne)
    if prospects:
        print(f"  prospects : {prospects['avance']} avancées, {prospects['perdu']} pertes, {prospects['rien']} semaines sans mouvement")
    return 0


if __name__ == "__main__":
    sys.exit(main())
