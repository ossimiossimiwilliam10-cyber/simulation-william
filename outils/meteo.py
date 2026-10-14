"""Météo réaliste de la simulation (créée le 11/10/2026) : tirée jour après jour à partir des NORMALES OFFICIELLES de
Luxembourg-Findel 1991-2020 (`donnees/climat-findel.csv`, MeteoLux), projetées en 2040 (`donnees/meteo-parametres.csv`).
Fini la météo écrite à l'intuition et sans continuité d'un tour à l'autre.

    python outils/meteo.py jour                     # le temps d'aujourd'hui (horloge) : tiré s'il ne l'est pas encore, puis affiché
    python outils/meteo.py jour 2040-07-15          # un autre jour (tous les jours manquants avant lui sont tirés dans l'ordre)
    python outils/meteo.py heure "2040-07-14 15:30" # température et ciel à une heure donnée (pour une scène)
    python outils/meteo.py prevision --jours 3      # ce que William voit sur son téléphone : prévision un peu bruitée
    python outils/meteo.py mois 2040-07             # bilan du mois tiré (moteur) comparé aux normales
    python outils/meteo.py jour 2040-07-20 --simule # essai : rien n'est écrit

Modèle (paramètres et sources dans donnees/meteo-parametres.csv) :
- jour de pluie (≥ 1 mm) : chaîne de Markov à deux états dont la fréquence stationnaire égale la normale du mois (jours ≥ 1 mm) ;
- hauteur de pluie : loi gamma dont la moyenne égale la normale (mm du mois / jours de pluie) ; orage : fréquence des jours d'orage ;
- température : normale interpolée au jour près + décalage 2040 + anomalie persistante (AR(1)) + effet du ciel (pluie, sec) ;
- ensoleillement, brouillard matinal : normales du mois ; lever et coucher du soleil : calendrier_2040.soleil (NOAA).
Chaque jour est tiré UNE fois (vrai hasard), écrit dans `etat/meteo.csv` et ne se rejoue jamais (comme les aléas).
STATIONS (12/10/2026) : `donnees/stations-meteo.csv` ; la station est celle du lieu où se trouve William (fuseau de l'horloge) :
Luxembourg-Findel par défaut, Manille (normales PAGASA de Port Area) quand il y séjourne ; chaque station a son climat, ses
paramètres et son fichier de tirages (`etat/meteo-manille.csv`…). `--station` force une station.
William ne connaît que les PRÉVISIONS (bruit croissant avec l'échéance) ; le moteur, lui, lit la vérité du jour.
"""
import argparse
import datetime as dt
import hashlib
import json
import math
import random
import sys

from commun import DONNEES, ETAT, JOURS, date_fr, ecrire_csv, lire_csv, lire_texte, maintenant_simule, utf8

FICHIER = ETAT / "meteo.csv"
STATIONS_CSV = DONNEES / "stations-meteo.csv"
COLONNES = ["date", "type", "tmin", "tmax", "pluie_mm", "orage", "soleil_h", "brouillard", "description", "anomalie", "tire_le"]
MOIS_COLS = ["jan", "fev", "mar", "avr", "mai", "juin", "juil", "aout", "sep", "oct", "nov", "dec"]
LIBELLES = {"ensoleille": "grand soleil", "peu_nuageux": "soleil et quelques nuages", "nuageux": "ciel partagé",
            "couvert": "ciel gris et couvert", "averses": "averses", "pluie": "pluie", "orage": "orage",
            "deluge": "pluies torrentielles"}


def stations():
    if not STATIONS_CSV.exists():
        return {"findel": {"station": "findel", "nom": "Luxembourg-Findel", "fuseaux": "luxembourg,paris", "climat": "climat-findel.csv",
                           "parametres": "meteo-parametres.csv", "etat": "meteo.csv", "lieu_soleil": "luxembourg", "lieu_affichage": "audun"}}
    return {l["station"]: l for l in lire_csv(STATIONS_CSV)}


def station_courante():
    """Station du lieu où se trouve William (fuseau de l'horloge) ; Luxembourg-Findel par défaut."""
    try:
        import horloge
        fz = horloge.lire()["fuseau"]
    except Exception:  # noqa: BLE001
        return "findel"
    for s, l in stations().items():
        if fz in [x.strip() for x in l["fuseaux"].split(",")]:
            return s
    return "findel"


def _st(station):
    return station or station_courante()


def fichier(station=None):
    return ETAT / stations()[_st(station)]["etat"]


def lieu_affichage(station=None):
    return stations()[_st(station)].get("lieu_affichage") or "audun"


def climat(station=None):
    return {l["parametre"]: [float(l[m]) for m in MOIS_COLS] for l in lire_csv(DONNEES / stations()[_st(station)]["climat"])}


def parametres(station=None):
    return {l["cle"]: float(l["valeur"]) for l in lire_csv(DONNEES / stations()[_st(station)]["parametres"])}


def jours_du_mois(annee, mois):
    return ((dt.date(annee + (mois == 12), mois % 12 + 1, 1)) - dt.date(annee, mois, 1)).days


def normale(param, jour, par_jour=False, station=None):
    """Valeur interpolée au jour près (valeurs mensuelles placées au 15 du mois). par_jour : un total mensuel ramené à un jour."""
    c = climat(station)[param]

    def valeur(annee, mois):
        v = c[mois - 1]
        return v / jours_du_mois(annee, mois) if par_jour else v

    milieu = dt.date(jour.year, jour.month, 15)
    if jour >= milieu:
        m2 = (jour.month % 12) + 1
        a2 = jour.year + (jour.month == 12)
        d1, v1 = milieu, valeur(jour.year, jour.month)
        d2, v2 = dt.date(a2, m2, 15), valeur(a2, m2)
    else:
        m0 = (jour.month - 2) % 12 + 1
        a0 = jour.year - (jour.month == 1)
        d1, v1 = dt.date(a0, m0, 15), valeur(a0, m0)
        d2, v2 = milieu, valeur(jour.year, jour.month)
    f = (jour - d1).days / (d2 - d1).days
    return v1 + f * (v2 - v1)


def lire(station=None):
    return {l["date"]: l for l in lire_csv(fichier(station))}


def depart_univers():
    try:
        return dt.date.fromisoformat(json.loads(lire_texte(ETAT / "univers.json") or "{}")["depart"][:10])
    except (KeyError, ValueError):
        return None


def tirer_jour(jour, veille, rng, station=None):
    """Tire le temps de `jour` d'après la veille (dict ou None). Retourne une ligne de etat/meteo.csv."""
    import calendrier_2040 as cal
    station = _st(station)

    def normale(param, j, par_jour=False):  # noqa: F811 (normale de la station)
        return normale_station(param, j, par_jour, station)

    p = parametres(station)
    pi = min(0.95, normale("NM_ODRR01", jour, par_jour=True))
    p11 = p["persistance_pluie"]
    p01 = max(0.01, min(0.95, pi * (1 - p11) / (1 - pi)))
    veille_humide = bool(veille) and float(veille["pluie_mm"] or 0) >= 1
    humide = rng.random() < (p11 if veille_humide else p01) if veille else rng.random() < pi
    # pluie
    pluie = 0.0
    orage = False
    if humide:
        moyenne = normale("NM_RR06_06", jour) / max(1.0, normale("NM_ODRR01", jour))
        k = p["forme_gamma_pluie"]
        pluie = round(1 + rng.gammavariate(k, max(0.1, moyenne - 1) / k), 1)
        p_orage = min(0.6, normale("NM_OTHSTORM", jour) / max(0.5, normale("NM_ODRR01", jour)))
        orage = rng.random() < p_orage
    # température
    phi = p["phi_temperature"]
    sigma = p["sigma_tmax_ete"] if 5 <= jour.month <= 9 else p["sigma_tmax"]
    a_prec = float(veille["anomalie"]) if veille and veille.get("anomalie") not in (None, "") else rng.gauss(0, sigma)
    anomalie = phi * a_prec + rng.gauss(0, sigma * math.sqrt(1 - phi * phi))
    # effet du ciel centré : un jour sec est plus chaud, un jour de pluie plus frais, sans déplacer la moyenne du mois
    effet = p["effet_pluie_tmax"] if humide else -p["effet_pluie_tmax"] * pi / (1 - pi)
    tmax = normale("NM_XT", jour) + p["decalage_2040"] + anomalie + effet
    tmin = (normale("NM_NT", jour) + p["decalage_2040"] + 0.55 * anomalie + (0.8 if humide else -0.6) + rng.gauss(0, 1.1))
    tmin = min(tmin, tmax - 1.5)
    # soleil
    lever, coucher = cal.soleil(jour, stations()[station]["lieu_soleil"])
    duree_jour = (coucher - lever).total_seconds() / 3600
    soleil_normal = normale("NM_INS", jour, par_jour=True)
    soleil = soleil_normal * (rng.uniform(1.15, 1.65) if not humide else rng.uniform(0.12, 0.7))
    soleil = round(max(0.0, min(duree_jour - 1.0, soleil)), 1)
    brouillard = (not humide) and rng.random() < 1.6 * normale("NM_OFOG", jour, par_jour=True)
    # type et description
    f = soleil / duree_jour
    if humide:
        typ = "orage" if orage else ("deluge" if pluie >= 60 else "pluie" if pluie >= 10 else "averses")
    else:
        typ = "ensoleille" if f >= 0.62 else "peu_nuageux" if f >= 0.45 else "nuageux" if f >= 0.28 else "couvert"
    moment_orage = rng.choice(["en fin d'après-midi", "en fin d'après-midi", "en soirée", "dans la nuit", "en début d'après-midi"])
    morceaux = [LIBELLES[typ].capitalize() + (f" {moment_orage}" if orage else "")]
    if brouillard:
        morceaux.append("brouillard au lever du jour")
    morceaux.append(f"{round(tmax)} °C au plus chaud, {round(tmin)} °C au petit matin")
    if humide:
        morceaux.append(f"{pluie:g} mm de pluie".replace(".", ","))
    if tmax >= p.get("seuil_chaleur", 30):
        morceaux.append("chaleur pesante" if p.get("seuil_chaleur", 30) < 33 else "chaleur écrasante")
    return {"date": jour.isoformat(), "type": typ, "tmin": f"{tmin:.1f}", "tmax": f"{tmax:.1f}", "pluie_mm": f"{pluie:.1f}",
            "orage": "oui" if orage else "non", "soleil_h": f"{soleil:.1f}", "brouillard": "oui" if brouillard else "non",
            "description": " ; ".join(morceaux), "anomalie": f"{anomalie:.2f}",
            "tire_le": dt.datetime.now().isoformat(timespec="minutes")}


def assurer(jusqua, simule=False, station=None):
    """Tire dans l'ordre tous les jours manquants jusqu'à `jusqua` inclus. Retourne {date: ligne}."""
    station = _st(station)
    deja = lire(station)
    if jusqua.isoformat() in deja:
        return deja
    rng = random.SystemRandom()
    if deja:
        debut = dt.date.fromisoformat(max(deja)) + dt.timedelta(days=1)
    elif station == "findel":
        debut = depart_univers() or jusqua
        debut = min(debut, jusqua)
    else:  # première visite d'une autre station : on part du jour de l'horloge (ou plus tôt si on demande avant)
        debut = min(aujourd_hui(), jusqua)
    tropiques = None
    if station == "manille" and not simule:  # 14/10/2026 : tempêtes et mousson renforcée (outils/tropiques.py)
        import tropiques
        tropiques.assurer(jusqua, depuis=debut)
    jour = debut
    while jour <= jusqua:
        veille = deja.get((jour - dt.timedelta(days=1)).isoformat())
        deja[jour.isoformat()] = tirer_jour(jour, veille, rng, station)
        if tropiques:
            deja[jour.isoformat()] = tropiques.appliquer(deja[jour.isoformat()], jour, rng)
        jour += dt.timedelta(days=1)
    if not simule:
        ecrire_csv(fichier(station), [deja[k] for k in sorted(deja)], COLONNES)
    return deja


def station_du_jour(jour):
    """Station où se trouvait William ce jour-là : la station courante, sauf avant le premier jour qui y a été tiré (alors
    Findel, la station de chez lui) ; 14/10/2026 : « heure » et « jour » d'une date passée au Luxembourg depuis Manille."""
    st = station_courante()
    deja = lire(st)
    if st != "findel" and deja and jour.isoformat() < min(deja):
        return "findel"
    return st


def normale_station(param, jour, par_jour, station):
    return normale(param, jour, par_jour, station)


def temperature_a(ligne, instant, station=None):
    """Température à l'instant (courbe journalière : minimum au lever du soleil, maximum vers 16 h)."""
    import calendrier_2040 as cal
    jour = instant.date()
    lever, coucher = cal.soleil(jour, stations()[_st(station)]["lieu_soleil"])
    h = instant.hour + instant.minute / 60
    hl = lever.hour + lever.minute / 60
    tmin, tmax = float(ligne["tmin"]), float(ligne["tmax"])
    if hl <= h <= 16:
        return tmin + (tmax - tmin) * math.sin(math.pi / 2 * (h - hl) / (16 - hl))
    if h > 16:
        hc = coucher.hour + coucher.minute / 60
        t_coucher = tmin + (tmax - tmin) * 0.72
        if h <= hc:
            return tmax - (tmax - t_coucher) * (h - 16) / max(0.5, hc - 16)
        return t_coucher - (t_coucher - (tmin + 1.5)) * min(1.0, (h - hc) / (24 + hl - hc))
    return tmin + 1.5 * (1 - h / max(1.0, hl))  # avant le lever : on approche du minimum


def _bruit(cle, sigma):
    graine = int(hashlib.sha1(cle.encode()).hexdigest()[:8], 16)
    return random.Random(graine).gauss(0, sigma)


def prevision(cible, emise, station=None):
    """Prévision vue par William pour `cible`, émise le jour `emise` (déterministe : la même si on la consulte deux fois)."""
    verite = assurer(cible, station=station)[cible.isoformat()]
    ech = (cible - emise).days
    sig = [0.6, 1.3, 1.8, 2.3, 2.8, 3.2, 3.6][min(ech, 6)]
    cle = f"{cible}|{emise}"
    tmax = float(verite["tmax"]) + _bruit(cle + "tx", sig)
    tmin = float(verite["tmin"]) + _bruit(cle + "tn", sig * 0.8)
    humide = float(verite["pluie_mm"]) >= 1
    base = 0.82 if humide else 0.08
    risque = base * (1 - 0.12 * ech) + 0.5 * (0.12 * ech) + _bruit(cle + "p", 0.08 + 0.03 * ech)
    risque = int(round(max(0.0, min(0.95, risque)) * 10)) * 10
    orage = verite["orage"] == "oui" and _bruit(cle + "o", 1) > -0.6 + 0.25 * ech
    ciel = ("orageux" if orage else "fortes pluies" if verite["type"] == "deluge" and risque >= 70
            else "pluvieux" if risque >= 70 else "averses possibles" if risque >= 40
            else "plutôt ensoleillé" if verite["type"] in ("ensoleille", "peu_nuageux") or _bruit(cle + "c", 1) > 0.8
            else "nuageux")
    return {"date": cible, "tmax": round(tmax), "tmin": round(tmin), "risque_pluie": risque, "ciel": ciel, "echeance": ech}


def aujourd_hui():
    t = maintenant_simule()
    return t.date() if t else dt.date(2040, 7, 14)


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("jour")
    p.add_argument("date", nargs="?")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("heure")
    p.add_argument("instant", help="« AAAA-MM-JJ HH:MM »")
    p = sp.add_parser("prevision")
    p.add_argument("--jours", type=int, default=3)
    p.add_argument("--depuis", help="date d'émission (par défaut : aujourd'hui à l'horloge)")
    p = sp.add_parser("mois")
    p.add_argument("mois", help="AAAA-MM")
    args = ap.parse_args()
    if args.cmd == "jour":
        jour = dt.date.fromisoformat(args.date) if args.date else aujourd_hui()
        l = assurer(jour, args.simule, station=station_du_jour(jour))[jour.isoformat()]
        print(f"Météo du {date_fr(jour)} (vérité du moteur) : {l['description']}.")
        print(f"  type {l['type']} ; min {l['tmin']} °C ; max {l['tmax']} °C ; pluie {l['pluie_mm']} mm ; orage {l['orage']} ; "
              f"soleil {l['soleil_h']} h ; brouillard {l['brouillard']}")
        return 0
    if args.cmd == "heure":
        d, h = args.instant.split()
        inst = dt.datetime.combine(dt.date.fromisoformat(d), dt.time.fromisoformat(h))
        st = station_du_jour(inst.date())
        l = assurer(inst.date(), station=st)[inst.date().isoformat()]
        print(f"{date_fr(inst)} à {h} : environ {temperature_a(l, inst, st):.0f} °C ; {l['description']}.")
        return 0
    if args.cmd == "prevision":
        emise = dt.date.fromisoformat(args.depuis) if args.depuis else aujourd_hui()
        print(f"Prévisions consultées le {date_fr(emise)} (ce que William voit) :")
        for i in range(0, args.jours + 1):
            c = emise + dt.timedelta(days=i)
            pv = prevision(c, emise)
            nom = "aujourd'hui" if i == 0 else "demain" if i == 1 else JOURS[c.weekday()]
            print(f"  {nom:12s} {pv['ciel']:20s} {pv['tmin']:3d} / {pv['tmax']:3d} °C   pluie {pv['risque_pluie']:3d} %")
        return 0
    if args.cmd == "mois":
        a, m = (int(x) for x in args.mois.split("-"))
        lignes = [l for k, l in sorted(lire().items()) if k.startswith(args.mois)]
        if not lignes:
            print("Aucun jour tiré pour ce mois.")
            return 0
        tx = [float(l["tmax"]) for l in lignes]
        pl = [float(l["pluie_mm"]) for l in lignes]
        c = climat()
        print(f"{args.mois} : {len(lignes)} jour(s) tiré(s) ; max moyen {sum(tx) / len(tx):.1f} °C (normale {c['NM_XT'][m - 1]} °C + "
              f"décalage 2040 {parametres()['decalage_2040']:+g}) ; jours de pluie {sum(x >= 1 for x in pl)} ; cumul {sum(pl):.0f} mm ; "
              f"jours ≥ 30 °C : {sum(x >= 30 for x in tx)} ; orages : {sum(l['orage'] == 'oui' for l in lignes)}")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
