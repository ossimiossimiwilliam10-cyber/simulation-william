"""CYCLONES TROPICAUX ET MOUSSON RENFORCÉE SUR MANILLE (créé le 14/10/2026 : William passe juillet et août à Manille, en pleine saison
des typhons ; la météo journalière ne savait pas qu'une tempête existe). Les tempêtes qui entrent dans la zone de responsabilité
des Philippines (PAR) sont tirées jour après jour (processus de Poisson sur la climatologie mensuelle), nommées dans la liste PAGASA
de 2040 (même jeu que 2024, noms retirés remplacés), et chacune reçoit un effet sur Metro Manila : aucun, mousson (« habagat »)
renforcée, ou signal n° 1, 2 ou 3. Les jours touchés, la météo de Manille est forcée (pluie, orage, déluge) et la ville réagit :
cours suspendus, bureaux de l'État fermés, vols intérieurs annulés, quartiers bas inondés, EDSA saturée.

    python outils/tropiques.py assurer --jusqua 2040-07-31       # tire ce qui manque (appelé par meteo.py pour Manille)
    python outils/tropiques.py liste                              # tempêtes de 2040 (moteur seulement)
    python outils/tropiques.py jour 2040-07-21                    # effet sur Metro Manila ce jour-là, alertes publiques

Sources : PAGASA, environ 20 cyclones par an dans la PAR, pic de juillet à octobre (≈ 70 %) ; prévisions mensuelles PAGASA (2 à 4 en
août, 2 à 3 en septembre) ; la mousson du sud-ouest renforcée par des cyclones lointains fait l'essentiel des inondations de Metro
Manila (2012, 2018, 2024 : un mois d'août à plus du double de la normale) ; noms retirés de 2024 remplacés à partir de 2028 (Amuyao,
Edring, Josefa, Kidul, Lekep, Nanolay, Onos, Puwok). Répartition des effets sur Metro Manila : estimation du moteur (F076, F077).
Fichier : `etat/tropiques.csv` ; tirages consignés dans memoire/tirages-aleas.md (une ligne par tempête) et tirages.jsonl.
"""
import argparse
import datetime as dt
import math
import random
import sys

from commun import ETAT, OUTILS, ecrire_csv, lire_csv, utf8

sys.path.insert(0, str(OUTILS))
import jet  # noqa: E402

FICHIER = ETAT / "tropiques.csv"
COLONNES = ["id", "nom", "entree_par", "effet", "debut", "fin", "signal", "pluie_jour_min", "pluie_jour_max", "note"]
NOMS_2040 = ["Amuyao", "Butchoy", "Carina", "Dindo", "Edring", "Ferdie", "Gener", "Helen", "Igme", "Josefa", "Kidul", "Lekep", "Marce",
             "Nanolay", "Onos", "Puwok", "Querubin", "Romina", "Siony", "Tonyo", "Upang", "Vicky", "Warren", "Yoyong", "Zosimo"]
# cyclones entrant dans la PAR par mois (somme ≈ 19,7 ; pic juillet-octobre)
PAR_MENSUELLE = {1: 0.4, 2: 0.2, 3: 0.2, 4: 0.4, 5: 1.0, 6: 1.5, 7: 3.0, 8: 3.5, 9: 3.0, 10: 2.8, 11: 2.2, 12: 1.5}
# effet sur Metro Manila d'une tempête entrée dans la PAR, saison de la mousson (juin à octobre) / hors saison
EFFETS_MOUSSON = [("aucun", 50), ("habagat", 28), ("signal_1", 13), ("signal_2", 7), ("signal_3", 2)]
EFFETS_HORS = [("aucun", 75), ("signal_1", 15), ("signal_2", 8), ("signal_3", 2)]
DUREES = {"habagat": (2, 4), "signal_1": (1, 2), "signal_2": (1, 2), "signal_3": (2, 2)}
PLUIES = {"habagat": (40, 150), "signal_1": (20, 80), "signal_2": (50, 150), "signal_3": (80, 250)}
DELAI_ARRIVEE = (1, 3)  # jours entre l'entrée dans la PAR et l'effet sur Manille


def lire():
    return lire_csv(FICHIER) if FICHIER.exists() else []


def pondere(rng, couples):
    total = sum(p for _, p in couples)
    x = rng.uniform(0, total)
    for c, p in couples:
        x -= p
        if x <= 0:
            return c
    return couples[-1][0]


def poisson(rng, lam):
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def initialiser(debut_saison, rng):
    """Tempêtes déjà passées en 2040 avant le premier jour tiré (nombre tiré sur la climatologie), sans effet à jouer."""
    lam = sum(PAR_MENSUELLE[m] for m in range(1, debut_saison.month)) + PAR_MENSUELLE[debut_saison.month] * (debut_saison.day - 1) / 30
    n = poisson(rng, lam)
    lignes = []
    for i in range(min(n, len(NOMS_2040))):
        lignes.append({"id": f"TC{i + 1:02d}", "nom": NOMS_2040[i], "entree_par": "", "effet": "passee", "debut": "", "fin": "", "signal": "",
                       "pluie_jour_min": "", "pluie_jour_max": "", "note": f"tempête de 2040 antérieure au {debut_saison:%d/%m} (nombre tiré : {n})"})
    jet.consigner(f"- Tropiques 2040 : {n} tempête(s) nommée(s) avant le {debut_saison:%d/%m/%Y} (Poisson, λ = {lam:.1f}) "
                  f"[PROCÉDURE : climatologie PAGASA, outils/tropiques.py]")
    return lignes


def assurer(jusqua, depuis=None):
    """Tire jour par jour les entrées dans la PAR jusqu'à `jusqua` + 5 jours (pour que les prévisions voient venir les tempêtes)."""
    rng = random.SystemRandom()
    lignes = lire()
    fin = jusqua + dt.timedelta(days=5)
    if not lignes:
        depart = depuis or jusqua
        lignes = initialiser(depart, rng)
        dernier = depart - dt.timedelta(days=1)
    else:
        marques = [l for l in lignes if l["id"] == "JOUR"]
        dernier = dt.date.fromisoformat(marques[0]["debut"]) if marques else (depuis or jusqua) - dt.timedelta(days=1)
    if dernier >= fin:
        return lignes
    jour = dernier + dt.timedelta(days=1)
    nouveaux = []
    while jour <= fin:
        lam = PAR_MENSUELLE[jour.month] / 30
        for _ in range(poisson(rng, lam)):
            n = len([l for l in lignes + nouveaux if l["id"].startswith("TC")])
            nom = NOMS_2040[n] if n < len(NOMS_2040) else f"auxiliaire n° {n - len(NOMS_2040) + 1}"
            mousson = 6 <= jour.month <= 10
            effet = pondere(rng, EFFETS_MOUSSON if mousson else EFFETS_HORS)
            l = {"id": f"TC{n + 1:02d}", "nom": nom, "entree_par": jour.isoformat(), "effet": effet, "debut": "", "fin": "", "signal": "",
                 "pluie_jour_min": "", "pluie_jour_max": "", "note": ""}
            if effet != "aucun":
                d0 = jour + dt.timedelta(days=rng.randint(*DELAI_ARRIVEE))
                d1 = d0 + dt.timedelta(days=rng.randint(*DUREES[effet]) - 1)
                pmin, pmax = PLUIES[effet]
                l.update({"debut": d0.isoformat(), "fin": d1.isoformat(), "signal": effet[-1] if effet.startswith("signal") else "",
                          "pluie_jour_min": str(pmin), "pluie_jour_max": str(pmax)})
            nouveaux.append(l)
            jet.consigner(f"- Tropiques : tempête « {nom} » entrée dans la PAR le {jour:%d/%m/%Y} ; effet sur Metro Manila : {effet}"
                          + (f" du {l['debut']} au {l['fin']}" if l["debut"] else "") + " [PROCÉDURE : climatologie PAGASA, outils/tropiques.py]")
            jet.consigner_json({"mode": "procedure", "libelle": f"Tropiques : tempête {nom}", "valeur": effet, "regle": "tropiques.py"})
        jour += dt.timedelta(days=1)
    lignes = [l for l in lignes if l["id"] != "JOUR"] + nouveaux
    lignes.append({"id": "JOUR", "nom": "", "entree_par": "", "effet": "", "debut": fin.isoformat(), "fin": "", "signal": "",
                   "pluie_jour_min": "", "pluie_jour_max": "", "note": "dernier jour tiré"})
    ecrire_csv(FICHIER, lignes, COLONNES)
    return lignes


def effets_du_jour(jour):
    """Tempêtes qui touchent Metro Manila ce jour-là."""
    res = []
    for l in lire():
        if l["id"].startswith("TC") and l["debut"] and l["debut"] <= jour.isoformat() <= l["fin"]:
            res.append(l)
    return res


def consequences(l, pluie):
    s = l["signal"]
    effets = []
    if s or pluie >= 80:
        effets.append("cours suspendus dans plusieurs villes de Metro Manila")
    if (s and int(s) >= 2) or pluie >= 150:
        effets.append("bureaux de l'État fermés (travail suspendu), vols intérieurs annulés")
    if s and int(s) >= 3:
        effets.append("vols internationaux retardés ou annulés à l'aéroport Ninoy-Aquino")
    if pluie >= 60:
        effets.append("rues inondées dans les quartiers bas, EDSA saturée")
    return effets


def appliquer(ligne, jour, rng=None):
    """Force la météo d'un jour de Manille touché par une tempête (pluie, type, description). Renvoie la ligne."""
    ts = effets_du_jour(jour)
    if not ts:
        return ligne
    rng = rng or random.SystemRandom()
    l = max(ts, key=lambda x: (x["signal"] or "0", x["pluie_jour_max"]))
    pluie = round(rng.uniform(float(l["pluie_jour_min"]), float(l["pluie_jour_max"])), 1)
    if pluie > float(ligne.get("pluie_mm") or 0):
        ligne["pluie_mm"] = f"{pluie:.1f}"
    ligne["type"] = "deluge" if pluie >= 60 else "pluie"
    ligne["soleil_h"] = f"{min(float(ligne.get('soleil_h') or 0), 1.5):.1f}"
    try:
        ligne["tmax"] = f"{min(float(ligne['tmax']), 30.5):.1f}"
    except (KeyError, ValueError):
        pass
    titre = (f"Signal n° {l['signal']} sur Metro Manila (tempête « {l['nom']} »)" if l["signal"]
             else f"Mousson renforcée par la tempête « {l['nom']} »")
    ligne["description"] = f"{titre} ; {pluie:g} mm de pluie ; " + " ; ".join(consequences(l, pluie) or ["pluies fortes"])
    return ligne


def alertes(jour):
    """Alertes publiques (radio, télévision, téléphone) : tempêtes qui touchent Manille aujourd'hui ou demain, ou entrées dans la PAR."""
    res = []
    for l in lire():
        if not l["id"].startswith("TC") or l["effet"] == "passee":
            continue
        if l["debut"] and l["debut"] <= (jour + dt.timedelta(days=1)).isoformat() and l["fin"] >= jour.isoformat():
            quand = "aujourd'hui" if l["debut"] <= jour.isoformat() else "demain"
            res.append(f"PAGASA : signal n° {l['signal']} sur Metro Manila {quand} (tempête « {l['nom']} »)" if l["signal"]
                       else f"PAGASA : mousson renforcée par « {l['nom']} », pluies fortes sur Metro Manila {quand}")
        elif l["entree_par"] and 0 <= (jour - dt.date.fromisoformat(l["entree_par"])).days <= 1:
            res.append(f"PAGASA : « {l['nom']} » est entrée dans la zone de responsabilité des Philippines")
    return res


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("assurer")
    p.add_argument("--jusqua", required=True)
    sp.add_parser("liste")
    p = sp.add_parser("jour")
    p.add_argument("date")
    args = ap.parse_args()
    if args.cmd == "assurer":
        assurer(dt.date.fromisoformat(args.jusqua))
        print("Tempêtes tirées jusqu'au", args.jusqua, "(+ 5 jours)")
    elif args.cmd == "liste":
        for l in lire():
            if l["id"].startswith("TC"):
                print(f"{l['id']} {l['nom']:10s} PAR {l['entree_par'] or '—':10s} effet {l['effet']:9s} {l['debut']} → {l['fin']}")
    else:
        j = dt.date.fromisoformat(args.date)
        for l in effets_du_jour(j):
            print(f"{l['nom']} : {l['effet']} (pluie {l['pluie_jour_min']}-{l['pluie_jour_max']} mm/jour)")
        for a in alertes(j):
            print("ALERTE", a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
