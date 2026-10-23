"""TRANSPORTS (créé le 12/10/2026 ; proposition P21 validée par l'utilisateur à la revue n° 1, besoin concret : aller de
chez William, à Audun-le-Tiche, à l'aéroport de Findel sans sa voiture). Calcul DÉTERMINISTE partagé avec l'application
« Transports » du téléphone (`outils/telephone_web/transports.js`) : la même requête donne les mêmes horaires, dans la page comme
dans la fiction.

    python outils/transports.py options --de AUD --vers FDL --quand "2040-07-18 12:00" [--arrivee]   # partir à / arriver avant
    python outils/transports.py options --de ICN2 --vers HGU --quand "2041-07-22 09:30"             # Séoul (22/10/2026, R4)
    python outils/transports.py arrets | lignes | verifier

Modèle (projection 2040) : chaque ligne a un premier et un dernier départ, une durée, et une fréquence selon le type de jour
(pointe et heures creuses en semaine scolaire ; heures creuses toute la journée pendant les vacances scolaires
luxembourgeoises ; samedi ; dimanche et jours fériés luxembourgeois ; 0 = pas de service). Les départs se suivent depuis le
premier départ (phase fixe). Un itinéraire enchaîne des tronçons avec un temps de correspondance minimal à chaque arrêt.
Prix : transports gratuits au Luxembourg (F023) ; partie française payante : un billet RegioZone de 2 h (F024, PX051).
Données : `donnees/transports/` (arrêts, lignes, itinéraires) ; sources et estimations écrites ligne par ligne. Les horaires
exacts de 2026 n'ont pas été trouvés (mobiliteit.lu) : fréquences estimées, à corriger par une ligne de données.
"""
import argparse
import datetime as dt
import sys

from commun import DONNEES, OUTILS, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
DOSSIER = DONNEES / "transports"
PRIX_REGIOZONE = "PX051"


def arrets():
    return {a["id"]: a for a in lire_csv(DOSSIER / "arrets.csv")}


def lignes():
    return {l["id"]: l for l in lire_csv(DOSSIER / "lignes.csv")}


def itineraires():
    return lire_csv(DOSSIER / "itineraires.csv")


def minutes(hhmm):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def hhmm(n):
    n = int(n)
    return f"{(n // 60) % 24:02d}:{n % 60:02d}"


def type_jour(d, pays="lu"):
    """semaine | vacances | samedi | dimanche (dimanches et fériés du pays : Luxembourg, ou Corée du Sud pour le réseau de Séoul)."""
    import calendrier_2040 as cal
    if d.weekday() == 6 or d in cal.jours_feries(d.year, "kr" if pays == "kr" else "lu"):
        return "dimanche"
    if d.weekday() == 5:
        return "samedi"
    if pays == "kr":
        return "semaine"  # réseau de Séoul : pas de calendrier scolaire
    p = cal.periode_scolaire(d, "lu")
    if p and (p["periode"].startswith("vacances") or p["periode"].startswith("conge")):
        return "vacances"
    return "semaine"


def frequence(l, typ, m):
    if typ == "samedi":
        return int(l["freq_samedi"])
    if typ == "dimanche":
        return int(l["freq_dimanche"])
    if typ == "semaine":
        for plage in (l["pointe"] or "").split(","):
            if "-" in plage:
                a, b = plage.split("-")
                if minutes(a) <= m < minutes(b):
                    return int(l["freq_pointe"])
    return int(l["freq_creuse"])


def departs(l, typ):
    """Minutes depuis minuit des départs de la ligne ce type de jour (liste vide si pas de service)."""
    res, m, fin = [], minutes(l["premier"]), minutes(l["dernier"])
    while m <= fin:
        f = frequence(l, typ, m)
        if f <= 0:
            return res
        res.append(m)
        m += f
    return res


def suivre(route, t0, typ, L, A):
    """Itinéraire au plus tôt en partant de t0 (minutes) ; None si une correspondance manque ce jour-là."""
    t, troncons = t0, []
    for i, lid in enumerate(route):
        l = L[lid]
        if i > 0:
            t += int(A[l["de"]]["correspondance_min"])
        dep = next((d for d in departs(l, typ) if d >= t), None)
        if dep is None:
            return None
        arr = dep + int(l["duree"])
        troncons.append({"ligne": lid, "mode": l["mode"], "nom": l["nom"], "de": l["de"], "vers": l["vers"], "depart": dep, "arrivee": arr})
        t = arr
    return troncons


def options(de, vers, quand, arrivee=False):
    """Itinéraires de `de` à `vers` le jour de `quand` : partir à partir de `quand`, ou (arrivee=True) arriver au plus tard à `quand`.
    Renvoie au plus un résultat par itinéraire type, trié par heure d'arrivée (ou de départ décroissante pour « arriver avant »)."""
    L, A = lignes(), arrets()
    typ = type_jour(quand.date(), A[de]["pays"])
    cible = quand.hour * 60 + quand.minute
    res = []
    for it in itineraires():
        if it["de"] != de or it["vers"] != vers:
            continue
        route = it["troncons"].split("|")
        if not arrivee:
            tr = suivre(route, cible, typ, L, A)
        else:
            tr = None
            for d in reversed(departs(L[route[0]], typ)):
                essai = suivre(route, d, typ, L, A)
                if essai and essai[-1]["arrivee"] <= cible:
                    tr = essai
                    break
        if tr:
            res.append({"itineraire": it["id"], "note": it["note"], "troncons": tr, "depart": tr[0]["depart"], "arrivee": tr[-1]["arrivee"],
                        "duree": tr[-1]["arrivee"] - tr[0]["depart"], "prix": prix(route, L), "prix_krw": prix_krw(it)})
    res.sort(key=(lambda r: -r["depart"]) if arrivee else (lambda r: r["arrivee"]))
    return typ, res


def prix_krw(it):
    """Prix en wons d'un itinéraire de Séoul (colonne prix_krw_2026 de itineraires.csv × 1,35, arrondi à 50 KRW), sinon None."""
    base = (it.get("prix_krw_2026") or "").strip()
    return int(round(float(base) * 1.35 / 50) * 50) if base else None


def prix(route, L=None):
    """Prix d'un trajet : un billet RegioZone de 2 h si une partie se fait côté français (F024), sinon gratuit (F023)."""
    import prix as P
    L = L or lignes()
    if any(L[x]["tarif"] == "regiozone" for x in route):
        px = next((p for p in P.lire() if p["id"] == PRIX_REGIOZONE), None)
        if px is None:
            sys.exit(f"Prix {PRIX_REGIOZONE} absent de donnees/prix.csv")
        return round(float(px["prix_2026"]) * P.coef(px), 2)
    return 0.0


def donnees_telephone(t=None):
    """Arrêts, lignes, itinéraires et types de jours (aujourd'hui + 60 jours) : la page refait le même calcul."""
    t = t or maintenant_simule()
    jour = t.date()
    L = lignes()
    jours = {(jour + dt.timedelta(days=i)).isoformat(): type_jour(jour + dt.timedelta(days=i)) for i in range(61)}
    jours_kr = {(jour + dt.timedelta(days=i)).isoformat(): type_jour(jour + dt.timedelta(days=i), "kr") for i in range(61)}
    import meteo
    seoul = meteo.station_courante() == "seoul"
    return {"aujourdhui": jour.isoformat(), "heure": f"{t:%H:%M}", "arrets": list(arrets().values()), "jours_kr": jours_kr,
            "defaut": {"de": "ICN2", "vers": "HGU"} if seoul else {"de": "AUD", "vers": "FDL"},
            "lignes": [{k: l[k] for k in ("id", "mode", "nom", "de", "vers", "duree", "premier", "dernier", "freq_pointe", "freq_creuse",
                                          "freq_samedi", "freq_dimanche", "pointe", "tarif")} for l in L.values()],
            "itineraires": [{"id": i["id"], "de": i["de"], "vers": i["vers"], "troncons": i["troncons"].split("|"), "note": i["note"],
                             "prix_krw": prix_krw(i)} for i in itineraires()],
            "jours": jours, "prix_regiozone": prix(["B604-AE"], L)}


def verifier():
    erreurs = []
    A, L = arrets(), lignes()
    for l in L.values():
        for cote in ("de", "vers"):
            if l[cote] not in A:
                erreurs.append(f"lignes.csv : arrêt inconnu {l[cote]} ({l['id']})")
        if l["tarif"] not in ("gratuit", "regiozone", "wons"):
            erreurs.append(f"lignes.csv : tarif inconnu ({l['id']})")
        try:
            minutes(l["premier"]), minutes(l["dernier"]), int(l["duree"])
        except ValueError:
            erreurs.append(f"lignes.csv : horaire ou durée illisible ({l['id']})")
    for it in itineraires():
        route = it["troncons"].split("|")
        if any(x not in L for x in route):
            erreurs.append(f"itineraires.csv : ligne inconnue ({it['id']})")
            continue
        if L[route[0]]["de"] != it["de"] or L[route[-1]]["vers"] != it["vers"]:
            erreurs.append(f"itineraires.csv : départ ou arrivée incohérents ({it['id']})")
        for a, b in zip(route, route[1:]):
            if L[a]["vers"] != L[b]["de"]:
                erreurs.append(f"itineraires.csv : correspondance impossible {a} → {b} ({it['id']})")
    return erreurs, []


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("options")
    p.add_argument("--de", required=True)
    p.add_argument("--vers", required=True)
    p.add_argument("--quand", required=True, help="AAAA-MM-JJ HH:MM")
    p.add_argument("--arrivee", action="store_true", help="arriver au plus tard à --quand (sinon : partir à partir de --quand)")
    sp.add_parser("arrets")
    sp.add_parser("lignes")
    sp.add_parser("verifier")
    args = ap.parse_args()
    if args.cmd == "options":
        A = arrets()
        quand = dt.datetime.fromisoformat(args.quand)
        typ, res = options(args.de, args.vers, quand, args.arrivee)
        print(f"{A[args.de]['nom']} → {A[args.vers]['nom']}, {quand:%d/%m/%Y} ({typ}), "
              f"{'arrivée au plus tard à' if args.arrivee else 'départ à partir de'} {quand:%H:%M} :")
        for r in res:
            prix_txt = (f"{r['prix_krw']:,} KRW".replace(",", " ") if r["prix_krw"] else
                        "gratuit" if not r["prix"] else f"{r['prix']:.2f} €".replace(".", ","))
            print(f"  {hhmm(r['depart'])} → {hhmm(r['arrivee'])} ({r['duree']} min, {prix_txt}) : " +
                  " ; ".join(f"{x['nom']} {hhmm(x['depart'])} {A[x['de']]['nom']} → {hhmm(x['arrivee'])} {A[x['vers']]['nom']}"
                             for x in r["troncons"]))
        if not res:
            print("  aucun itinéraire ce jour-là à cette heure")
        return 0
    if args.cmd == "arrets":
        for a in arrets().values():
            print(f"{a['id']} {a['nom']} (correspondance {a['correspondance_min']} min)")
        return 0
    if args.cmd == "lignes":
        for l in lignes().values():
            print(f"{l['id']:9s} {l['nom']:18s} {l['de']} → {l['vers']} {l['duree']} min, {l['premier']}-{l['dernier']}, "
                  f"toutes les {l['freq_pointe']}/{l['freq_creuse']}/{l['freq_samedi']}/{l['freq_dimanche']} min, {l['tarif']}")
        return 0
    erreurs, _ = verifier()
    for e in erreurs:
        print("ERREUR", e)
    print("transports : conforme" if not erreurs else f"{len(erreurs)} erreur(s)")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
