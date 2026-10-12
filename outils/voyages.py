"""VOYAGES (créé le 12/10/2026) : vols, hôtels, forfaits vol + hôtel et formalités, en prix projetés 2040. Un seul calcul, DÉTERMINISTE,
sert à la fois l'application « Voyages » du téléphone de William (`outils/telephone_web/voyages.js`) et le moteur, qui l'utilise
quand le joueur réserve : la même requête donne toujours le même prix, dans la page comme dans la fiction.
Demande de l'utilisateur (12/10/2026) : « crée l'application et rajoute-la dans le téléphone », pour ne plus refaire les recherches.

    python outils/voyages.py vols --de LUX --vers NSI --aller 2040-08-28 --retour 2040-09-18 [--voyageurs 1]
    python outils/voyages.py mois --de LUX --vers NSI --mois 2040-08 [--duree 21]     # calendrier des prix (vue « mois entier »)
    python outils/voyages.py hotels --vers NSI --arrivee 2040-08-28 --depart 2040-09-18
    python outils/voyages.py forfait --de LUX --vers NSI --aller 2040-08-28 --retour 2040-09-18 [--voyageurs 1]
    python outils/voyages.py formalites --vers NSI
    python outils/voyages.py verifier

Données : `donnees/voyages/` (aéroports, destinations et formalités, vols, saisons, retours, hôtels, paramètres) ; les prix des
hôtels et des visas viennent de `donnees/prix.csv` (prix 2026 sourcés × coefficient 2040). Modèle d'un aller-retour, par personne :
plancher de la saison de départ (aller-retour le moins cher de la destination) × facteur de l'itinéraire × (1 + cran × variation)
× facteur de durée du séjour × facteur de la date de retour, arrondi à l'euro. Le cran (0 à 6) est tiré par EMPREINTE (sha1 du
sel, de l'itinéraire et de la date) : c'est un tirage, mais reproductible. Un vol n'existe que les jours où il opère (aller et
retour). Hôtel : prix projeté × (1 + cran × variation), cran de 0 à 4 par nuit. Forfait : (vols + hôtel) × (1 − remise).
Pour ajouter une destination, un vol ou un hôtel : une ligne dans `donnees/voyages/` (après une recherche web), rien d'autre.
"""
import argparse
import datetime as dt
import hashlib
import math
import sys

from commun import DONNEES, OUTILS, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
DOSSIER = DONNEES / "voyages"
JOURS = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
NOMS_JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
NOMS_MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
_CACHE = {}


# ---------------------------------------------------------------- données
def table(nom):
    if nom not in _CACHE:
        _CACHE[nom] = lire_csv(DOSSIER / nom)
    return _CACHE[nom]


def parametres():
    p = {l["cle"]: l["valeur"] for l in table("parametres.csv")}
    duree = []
    for x in p["duree_facteurs"].split("|"):
        plage, f = x.split(":")
        a, b = plage.split("-")
        duree.append((int(a), int(b), float(f)))
    return {
        "duree": duree,
        "duree_defaut": int(p["duree_defaut"]), "sejour_max": int(p["sejour_max"]), "horizon": int(p["horizon_jours"]),
        "seuil_vert": float(p["seuil_vert"]), "seuil_orange": float(p["seuil_orange"]), "remise": float(p["remise_forfait"]),
        "var_vol": float(p["variation_vol"]), "var_hotel": float(p["variation_hotel"]), "sel": p["sel"],
    }


def prix_projete(px):
    """Prix 2040 d'une ligne de donnees/prix.csv (prix 2026 × coefficient, 1,35 par défaut), arrondi au centime."""
    for l in lire_csv(DONNEES / "prix.csv"):
        if l["id"] == px:
            return round(float(l["prix_2026"]) * float(l.get("coef") or 1.35), 2)
    sys.exit(f"Prix inconnu : {px} (donnees/prix.csv)")


def vols(de=None, vers=None):
    return [v for v in table("vols.csv") if (de is None or v["de"] == de) and (vers is None or v["vers"] == vers)]


def jours_operes(v):
    j = v["jours"].strip()
    return set(range(7)) if j == "tous" else {JOURS.index(x.strip()) for x in j.split(",")}


def dans(mmjj, debut, fin):
    """mmjj (« 08-24 ») dans la plage [debut, fin], qui peut enjamber le 31 décembre."""
    return debut <= mmjj <= fin if debut <= fin else (mmjj >= debut or mmjj <= fin)


def plancher(dest, d):
    for s in table("saisons.csv"):
        if s["destination"] == dest and dans(f"{d:%m-%d}", s["debut"], s["fin"]):
            return float(s["plancher"])
    sys.exit(f"Aucune saison pour {dest} le {d} (donnees/voyages/saisons.csv)")


def plancher_min(dest):
    return min(float(s["plancher"]) for s in table("saisons.csv") if s["destination"] == dest)


def facteur_retour(dest, r):
    for s in table("retours.csv"):
        if s["destination"] == dest and dans(f"{r:%m-%d}", s["debut"], s["fin"]):
            return float(s["facteur"])
    return 1.0


def facteur_duree(n, P=None):
    P = P or parametres()
    for a, b, f in P["duree"]:
        if a <= n <= b:
            return f
    return None


def cran(cle, n, sel):
    return int(hashlib.sha1(f"{sel}|{cle}".encode("utf-8")).hexdigest()[:8], 16) % n


def arrondi(x):
    return math.floor(x + 0.5)  # même arrondi que Math.floor(x + 0.5) dans la page (pas d'arrondi bancaire)


# ---------------------------------------------------------------- vols
def base_vol(v, d, P=None):
    P = P or parametres()
    return round(plancher(v["vers"], d) * float(v["facteur"]) * (1 + P["var_vol"] * cran(f"{v['id']}|{d.isoformat()}", 7, P["sel"])), 2)


def prix_vol(v, aller, retour, P=None):
    """Prix d'un aller-retour par personne (euros 2040), ou None si le vol n'opère pas ces jours-là ou si la durée est hors limites."""
    P = P or parametres()
    n = (retour - aller).days
    ops = jours_operes(v)
    if n < 1 or n > P["sejour_max"] or aller.weekday() not in ops or retour.weekday() not in ops:
        return None
    return arrondi(base_vol(v, aller, P) * facteur_duree(n, P) * facteur_retour(v["vers"], retour))


def options(de, vers, aller, retour, voyageurs=1):
    P = parametres()
    res = []
    for v in vols(de, vers):
        p = prix_vol(v, aller, retour, P)
        if p is not None:
            res.append({"vol": v, "par_personne": p, "total": p * voyageurs})
    return sorted(res, key=lambda x: x["par_personne"])


def couleur(prix, dest, P=None):
    P = P or parametres()
    m = plancher_min(dest)
    return "vert" if prix <= P["seuil_vert"] * m else "orange" if prix <= P["seuil_orange"] * m else "rouge"


def mois(de, vers, annee, mois_, duree=None):
    P = parametres()
    duree = duree or P["duree_defaut"]
    d = dt.date(annee, mois_, 1)
    res = []
    while d.month == mois_:
        prix = [p for p in (prix_vol(v, d, d + dt.timedelta(days=duree), P) for v in vols(de, vers)) if p is not None]
        res.append((d, min(prix) if prix else None))
        d += dt.timedelta(days=1)
    return res


# ---------------------------------------------------------------- hôtels et forfaits
def hotels(vers):
    return [h for h in table("hotels.csv") if h["ville"] == vers]


def prix_nuit(h, d, P=None):
    P = P or parametres()
    return arrondi(prix_projete(h["prix"]) * (1 + P["var_hotel"] * cran(f"{h['id']}|{d.isoformat()}", 5, P["sel"])))


def sejour(h, arrivee, depart, P=None):
    P = P or parametres()
    nuits = [arrivee + dt.timedelta(days=i) for i in range((depart - arrivee).days)]
    return sum(prix_nuit(h, n, P) for n in nuits), len(nuits)


def forfaits(de, vers, aller, retour, voyageurs=1):
    P = parametres()
    opts = options(de, vers, aller, retour, voyageurs)
    if not opts:
        return []
    meilleur = opts[0]
    res = []
    for h in hotels(vers):
        total_h, nuits = sejour(h, aller, retour, P)
        separe = meilleur["total"] + total_h
        res.append({"hotel": h, "vol": meilleur["vol"], "nuits": nuits, "hotel_total": total_h, "separe": separe,
                    "forfait": arrondi(separe * (1 - P["remise"]))})
    return sorted(res, key=lambda x: x["forfait"])


def formalites(vers):
    for d in table("destinations.csv"):
        if d["code"] == vers:
            texte = d["formalites"]
            for px in ("PX034", "PX039"):
                texte = texte.replace("{" + px + "}", f"{arrondi(prix_projete(px))}")
            return [x.strip() for x in texte.split("|")]
    return []


# ---------------------------------------------------------------- données du téléphone
def donnees_telephone(t=None):
    """Tout ce que l'application « Voyages » affiche : bases de prix précalculées (même calcul qu'ici), horaires, hôtels, formalités.
    Aucune source, aucun mot du moteur : seulement ce que William voit sur un site de voyages."""
    t = t or maintenant_simule()
    jour = t.date() if hasattr(t, "date") else t
    P = parametres()
    aeroports = {a["code"]: a["nom"] for a in table("aeroports.csv")}
    dests = []
    for d in table("destinations.csv"):
        vs = []
        for v in vols(vers=d["code"]):
            vs.append({"id": v["id"], "de": v["de"], "compagnies": v["compagnies"], "via": v["via"], "escales": int(v["escales"]),
                       "jours": sorted(jours_operes(v)),
                       "aller": [v["aller_dep"], v["aller_arr"], v["aller_duree"]],
                       "retour": [v["retour_dep"], v["retour_arr"], v["retour_duree"]],
                       "base": [base_vol(v, jour + dt.timedelta(days=i), P) for i in range(P["horizon"] + 1)]})
        hs = []
        for h in hotels(d["code"]):
            hs.append({"id": h["id"], "nom": h["nom"], "categorie": h["categorie"], "quartier": h["quartier"],
                       "des": arrondi(prix_projete(h["prix"])),
                       "nuits": [prix_nuit(h, jour + dt.timedelta(days=i), P) for i in range(P["horizon"] + P["sejour_max"] + 1)]})
        retours = [[s["debut"], s["fin"], float(s["facteur"])] for s in table("retours.csv") if s["destination"] == d["code"]]
        m = plancher_min(d["code"])
        dests.append({"code": d["code"], "ville": d["ville"], "pays": d["pays"], "vols": vs, "hotels": hs, "retours": retours,
                      "seuils": [round(P["seuil_vert"] * m, 2), round(P["seuil_orange"] * m, 2)],
                      "formalites": formalites(d["code"])})
    departs = sorted({v["de"] for v in table("vols.csv")}, key=lambda c: ["LUX", "BRU", "CDG"].index(c) if c in ("LUX", "BRU", "CDG") else 9)
    return {"jour": jour.isoformat(), "horizon": P["horizon"], "sejour_max": P["sejour_max"], "duree_defaut": P["duree_defaut"],
            "duree": [[a, b, f] for a, b, f in P["duree"]], "remise": P["remise"], "aeroports": aeroports, "departs": departs,
            "destinations": dests}


# ---------------------------------------------------------------- contrôle
def verifier():
    erreurs, aver = [], []
    P = parametres()
    codes = {a["code"] for a in table("aeroports.csv")}
    for v in table("vols.csv"):
        if v["de"] not in codes or v["vers"] not in codes:
            erreurs.append(f"vols.csv : aéroport inconnu ({v['id']})")
        try:
            jours_operes(v)
        except ValueError:
            erreurs.append(f"vols.csv : jours illisibles ({v['id']} : {v['jours']})")
    for dest in {v["vers"] for v in table("vols.csv")}:
        for i in range(366):  # chaque jour de l'année a une saison
            d = dt.date(2041, 1, 1) + dt.timedelta(days=i)
            if not any(s["destination"] == dest and dans(f"{d:%m-%d}", s["debut"], s["fin"]) for s in table("saisons.csv")):
                erreurs.append(f"saisons.csv : {dest} sans saison le {d:%d/%m}")
                break
    prix_ids = {l["id"] for l in lire_csv(DONNEES / "prix.csv")}
    for h in table("hotels.csv"):
        if h["prix"] not in prix_ids:
            erreurs.append(f"hotels.csv : prix inconnu {h['prix']} ({h['id']})")
    for a, b, f in P["duree"]:
        if a > b or f <= 0:
            erreurs.append(f"parametres.csv : facteur de durée incohérent {a}-{b}:{f}")
    return erreurs, aver


# ---------------------------------------------------------------- affichage
def date_fr(d):
    return f"{NOMS_JOURS[d.weekday()]} {d.day} {NOMS_MOIS[d.month - 1]} {d.year}"


def euros(x):
    return f"{x:,.0f} €".replace(",", " ")


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    for nom in ("vols", "forfait"):
        p = sp.add_parser(nom)
        p.add_argument("--de", default="LUX")
        p.add_argument("--vers", default="NSI")
        p.add_argument("--aller", required=True)
        p.add_argument("--retour", required=True)
        p.add_argument("--voyageurs", type=int, default=1)
    p = sp.add_parser("mois")
    p.add_argument("--de", default="LUX")
    p.add_argument("--vers", default="NSI")
    p.add_argument("--mois", required=True, help="AAAA-MM")
    p.add_argument("--duree", type=int)
    p = sp.add_parser("hotels")
    p.add_argument("--vers", default="NSI")
    p.add_argument("--arrivee", required=True)
    p.add_argument("--depart", required=True)
    p = sp.add_parser("formalites")
    p.add_argument("--vers", default="NSI")
    sp.add_parser("verifier")
    args = ap.parse_args()
    if args.cmd == "vols":
        a, r = dt.date.fromisoformat(args.aller), dt.date.fromisoformat(args.retour)
        res = options(args.de, args.vers, a, r, args.voyageurs)
        print(f"Vols {args.de} → {args.vers}, aller le {date_fr(a)}, retour le {date_fr(r)}, {args.voyageurs} voyageur(s) :")
        for o in res:
            v = o["vol"]
            print(f"  {v['id']} {v['compagnies']} ({'direct' if v['via'] == 'direct' else 'par ' + v['via']}) : aller {v['aller_dep']}-"
                  f"{v['aller_arr']} ({v['aller_duree']}), retour {v['retour_dep']}-{v['retour_arr']} ({v['retour_duree']}) : "
                  f"{euros(o['par_personne'])} par personne, {euros(o['total'])} au total")
        if not res:
            print("  aucun vol ces jours-là (jours d'opération ou durée du séjour)")
        return 0
    if args.cmd == "mois":
        a, m = (int(x) for x in args.mois.split("-"))
        P = parametres()
        print(f"Prix les plus bas {args.de} → {args.vers}, séjour de {args.duree or P['duree_defaut']} jours, départs de {NOMS_MOIS[m - 1]} {a} :")
        for d, p in mois(args.de, args.vers, a, m, args.duree):
            print(f"  {d:%d/%m} {JOURS[d.weekday()]} : " + (f"{euros(p)} ({couleur(p, args.vers, P)})" if p else "pas de vol"))
        return 0
    if args.cmd == "hotels":
        a, dpt = dt.date.fromisoformat(args.arrivee), dt.date.fromisoformat(args.depart)
        for h in hotels(args.vers):
            total, nuits = sejour(h, a, dpt)
            print(f"  {h['id']} {h['nom']} ({h['categorie']}) : {nuits} nuit(s), {euros(total)} (dès {euros(arrondi(prix_projete(h['prix'])))} la nuit)")
        return 0
    if args.cmd == "forfait":
        a, r = dt.date.fromisoformat(args.aller), dt.date.fromisoformat(args.retour)
        for f in forfaits(args.de, args.vers, a, r, args.voyageurs):
            print(f"  {f['hotel']['nom']} + {f['vol']['compagnies']} : {euros(f['forfait'])} (séparément : {euros(f['separe'])}, "
                  f"{f['nuits']} nuit(s))")
        return 0
    if args.cmd == "formalites":
        for x in formalites(args.vers):
            print(" -", x)
        return 0
    erreurs, aver = verifier()
    for e in erreurs:
        print("ERREUR", e)
    for x in aver:
        print("RELIRE", x)
    print("voyages :", "des erreurs" if erreurs else "conforme")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
