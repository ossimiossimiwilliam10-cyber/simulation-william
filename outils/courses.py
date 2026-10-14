"""COURSES EN VILLE (créé le 14/10/2026 : William arrive à Manille sans pesos ; besoin : rejoindre son hôtel, puis circuler).
VTC (application Grab) et taxis (ordinaires, jaunes de l'aéroport, à coupon). Calcul DÉTERMINISTE : distance, durée, majoration et
attente se déduisent du lieu, de l'heure (créneau de 15 minutes), du jour et de la pluie du jour (etat/meteo-manille.csv) ; la page
« Courses » du téléphone et le moteur obtiennent le même prix. Tarifs 2026 × 1,35 (même coefficient que prix.py).

    python outils/courses.py options --de naia_t3 --vers city_garden [--quand "AAAA-MM-JJ HH:MM"]
    python outils/courses.py installer [--quand …]                        # l'application Grab (décision du joueur)
    python outils/courses.py carte --carte visa_debit [--quand …]         # carte enregistrée dans l'application
    python outils/courses.py commander --service grab_car --de naia_t3 --vers city_garden [--paiement especes|carte] [--quand …] [--simule]
    python outils/courses.py lieux | ici | verifier

RÈGLES : un VTC exige l'application installée (et une carte enregistrée pour payer par carte) ; un taxi se paie en espèces. Taxi à
coupon : payé d'avance au comptoir (refusé sans assez d'espèces). Compteur ou VTC payé en espèces : le paiement se fait à l'arrivée ;
s'il manque des pesos, la course est notée « impayée » et le moteur joue la scène. Paiement écrit à l'heure d'arrivée (devises.py).
Les aléas de la course (chauffeur qui annule, compteur « en panne », détour) ne sont PAS tirés ici : aléas et tables du moteur.
Données : donnees/courses.csv (tarifs), donnees/coordonnees.csv, donnees/distances.csv ; état : etat/courses.csv, etat/courses-compte.csv.
"""
import argparse
import datetime as dt
import hashlib
import math
import sys

from commun import DONNEES, ETAT, OUTILS, analyser_instant_naif, ecrire_csv, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
TARIFS = DONNEES / "courses.csv"
COORD = DONNEES / "coordonnees.csv"
DISTANCES = DONNEES / "distances.csv"
JOURNAL = ETAT / "courses.csv"
COMPTE = ETAT / "courses-compte.csv"
COL_JOURNAL = ["id", "demande", "service", "de", "vers", "km", "minutes", "attente", "prix", "devise", "paiement", "statut", "arrivee", "note"]
COEF = 1.35
DETOUR = 1.45  # distance par la route ≈ distance à vol d'oiseau × 1,45 dans Metro Manila (estimation), sauf ligne de distances.csv
VILLES = {"manille": {"pays": "ph", "devise": "PHP", "meteo": ETAT / "meteo-manille.csv"}}
# km/h de porte à porte selon l'heure, en semaine (estimation : Metro Manila, parmi les circulations les plus lentes d'Asie)
VITESSES = [(0, 32), (5, 24), (7, 13), (10, 17), (16, 11), (20, 17), (22, 26)]


def _alea(*cles):
    """Nombre fixe dans [0, 1) pour ces clés (même résultat en Python et à chaque relecture)."""
    return int(hashlib.sha1("|".join(map(str, cles)).encode("utf-8")).hexdigest()[:8], 16) / 2 ** 32


def maintenant_naif():
    return maintenant_simule().replace(tzinfo=None)


def lieux(ville="manille"):
    import lieux as L
    noms = L.lire()
    return {c["lieu"]: {"id": c["lieu"], "nom": noms.get(c["lieu"], {}).get("nom", c["lieu"]), "lat": float(c["lat"]), "lon": float(c["lon"]),
                        "zone": c["zone"], "motcles": [m.strip() for m in c["motcles"].split("·")]}
            for c in lire_csv(COORD) if c["lieu"] in noms and noms[c["lieu"]]["fuseau"] == ville}


def ici(ville="manille"):
    """Lieu connu où se trouve William (d'après le lieu de l'horloge), ou None."""
    import horloge
    texte = horloge.lire()["lieu"].lower()
    for i, l in lieux(ville).items():
        if any(m and m in texte for m in l["motcles"]):
            return i
    return None


def distance_km(a, b, L=None):
    for d in lire_csv(DISTANCES):
        if {d["de"], d["vers"]} == {a, b}:
            return float(d["km"])
    L = L or lieux()
    x, y = L[a], L[b]
    r = 6371.0
    p1, p2 = math.radians(x["lat"]), math.radians(y["lat"])
    dp, dl = p2 - p1, math.radians(y["lon"] - x["lon"])
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return round(2 * r * math.asin(math.sqrt(h)) * DETOUR, 1)


def pluie(quand, ville="manille"):
    """0 sec, 1 pluie, 2 forte pluie ou rues inondées, à cette heure (fixe pour la journée et l'heure)."""
    ligne = next((l for l in lire_csv(VILLES[ville]["meteo"]) if l["date"] == quand.date().isoformat()), None)
    if not ligne:
        return 0
    mm = float(ligne.get("pluie_mm") or 0)
    if mm < 1:
        return 0
    p = min(0.85, mm / 25) * (1.4 if 13 <= quand.hour <= 21 else 0.8)
    if _alea("pluie", quand.date(), quand.hour) >= p:
        return 0
    return 2 if mm >= 30 or "inond" in (ligne.get("description") or "").lower() else 1


def type_jour(jour, pays="ph"):
    import calendrier_2040 as cal
    if jour.weekday() == 6 or jour in cal.jours_feries(jour.year, pays):
        return "dimanche"
    return "samedi" if jour.weekday() == 5 else "semaine"


def vitesse(quand, niveau_pluie, de, vers):
    v = next(v for h, v in reversed(VITESSES) if quand.hour >= h)
    tj = type_jour(quand.date())
    if tj == "samedi" and 7 <= quand.hour < 20:
        v *= 1.15
    elif tj == "dimanche" and 7 <= quand.hour < 20:
        v *= 1.3
    v *= (1.0, 0.8, 0.55)[niveau_pluie]
    return v * (0.9 + 0.2 * _alea("vitesse", de, vers, quand.date(), quand.hour))


def creneau(quand):
    return quand.replace(minute=quand.minute // 15 * 15, second=0, microsecond=0)


def majoration(t, de, quand, niveau_pluie, L):
    if t["type"] != "vtc":
        return 1.0
    h, tj, zone = quand.hour, type_jour(quand.date()), L[de]["zone"]
    m = 1.05
    if zone == "aeroport":
        m = 1.35 if (h >= 21 or h < 3) else 1.15
    if tj == "semaine" and (7 <= h < 10 or 16 <= h < 20):
        m = max(m, 1.45)
    if quand.weekday() in (4, 5) and (h >= 21 or h < 3) and zone in ("makati", "taguig"):
        m = max(m, 1.35)
    m += (0, 0.2, 0.45)[niveau_pluie] + (_alea("majoration", de, creneau(quand)) - 0.4) * 0.3
    return round(min(max(m, 1.0), float(t["majoration_max"] or 1)), 2)


def attente(t, de, quand, niveau_pluie, L):
    """Minutes avant de monter : arrivée du VTC, ou file des taxis."""
    h = quand.hour
    a = _alea("attente", t["id"], de, creneau(quand))
    if t["type"] == "vtc":
        base = 8 if L[de]["zone"] == "aeroport" else 5
        if type_jour(quand.date()) == "semaine" and (7 <= h < 10 or 16 <= h < 20):
            base *= 1.6
        base *= (1.0, 1.5, 2.2)[niveau_pluie]
        return max(2, round(base * (0.7 + 0.8 * a)))
    if t["depart"] == "aeroport":
        return round(5 + 20 * a * (1.5 if niveau_pluie else 1.0))
    return round((3 + 12 * a) * (1.0, 1.8, 3.0)[niveau_pluie])


def tarif(ident):
    t = next((x for x in lire_csv(TARIFS) if x["id"] == ident), None)
    if t is None:
        sys.exit(f"Service inconnu : {ident} (donnees/courses.csv)")
    return t


def disponible(t, de, L):
    return t["depart"] == "partout" or (t["depart"] == "aeroport" and L[de]["zone"] == "aeroport")


def estimer(ident, de, vers, quand, L=None):
    """Prix, durée et attente d'une course (aucune écriture)."""
    L = L or lieux()
    t = tarif(ident)
    if de not in L or vers not in L:
        sys.exit(f"Lieu inconnu : {de if de not in L else vers} (donnees/coordonnees.csv)")
    if not disponible(t, de, L):
        return None
    np_ = pluie(quand)
    km = distance_km(de, vers, L)
    att = attente(t, de, quand, np_, L)
    depart = quand + dt.timedelta(minutes=att)
    minutes = max(4, round(km / vitesse(depart, np_, de, vers) * 60))
    maj = majoration(t, de, quand, np_, L)
    if t["forfaits"]:
        f = dict(x.split(":") for x in t["forfaits"].split("|"))
        zone = L[vers]["zone"]
        prix = float(f.get(zone, f.get("autre"))) * COEF
    else:
        prise, par_km, par_min = float(t["prise_en_charge"]), float(t["par_km"]), float(t["par_min"])
        premiers = float(t["premiers_km"] or 0)
        if t["id"] == "taxi_jaune":  # la part « temps » ne compte que l'attente dans les bouchons (au-delà de 30 km/h)
            temps = max(0, minutes - km * 2) * par_min
        else:
            temps = minutes * par_min
        prix = (prise + (max(km - premiers, 0) * par_km + temps) * maj) * COEF
    return {"service": t["id"], "nom": t["nom"], "type": t["type"], "de": de, "vers": vers, "km": km, "minutes": minutes, "attente": att,
            "prix": round(prix), "devise": VILLES["manille"]["devise"], "majoration": maj, "pluie": np_, "paiement": t["paiement"],
            "depart": f"{depart:%Y-%m-%d %H:%M}", "arrivee": f"{depart + dt.timedelta(minutes=minutes):%Y-%m-%d %H:%M}"}


def options(de, vers, quand):
    L = lieux()
    res = [estimer(t["id"], de, vers, quand, L) for t in lire_csv(TARIFS) if disponible(t, de, L)]
    return sorted([r for r in res if r], key=lambda r: r["prix"])


def compte():
    return {l["cle"]: l["valeur"] for l in lire_csv(COMPTE)}


def _regler(cle, valeur, quand):
    lignes = [l for l in lire_csv(COMPTE) if l["cle"] != cle]
    lignes.append({"cle": cle, "valeur": valeur, "depuis": f"{quand:%Y-%m-%d %H:%M}"})
    ecrire_csv(COMPTE, lignes, ["cle", "valeur", "depuis"])


def installer(quand):
    if compte().get("installe") == "oui":
        return "Grab est déjà installé."
    _regler("installe", "oui", quand)
    import traces
    traces.ajouter(f"{quand:%d/%m/%Y %H:%M}", "Inscription à l'application Grab (numéro de téléphone de William vérifié par SMS)", "application",
                   "Grab", "faible")
    return "Grab installé ; numéro vérifié par SMS ; aucune carte enregistrée (paiement en espèces par défaut)."


def enregistrer_carte(carte, quand):
    import cartes
    cartes.carte(carte)
    _regler("carte", carte, quand)
    return f"Carte enregistrée dans Grab : {carte}."


def commander(ident, de, vers, quand, paiement="especes", simule=False):
    """Commande ou prend une course ; renvoie (ok, message, course)."""
    import devises
    L = lieux()
    t = tarif(ident)
    c = compte()
    if t["type"] == "vtc" and c.get("installe") != "oui":
        return False, "Grab n'est pas installé sur le téléphone de William.", None
    if paiement == "carte":
        if t["type"] != "vtc":
            return False, "Ce taxi se paie en espèces.", None
        if not c.get("carte"):
            return False, "Aucune carte enregistrée dans Grab.", None
    e = estimer(ident, de, vers, quand, L)
    if e is None:
        return False, f"{t['nom']} : pas de départ depuis {L[de]['nom']}.", None
    journal = lire_csv(JOURNAL)
    course = {"id": f"C{len(journal) + 1:03d}", "demande": f"{quand:%Y-%m-%d %H:%M}", "service": ident, "de": de, "vers": vers,
              "km": e["km"], "minutes": e["minutes"], "attente": e["attente"], "prix": e["prix"], "devise": e["devise"],
              "paiement": "carte" if paiement == "carte" else "especes", "statut": "", "arrivee": e["arrivee"], "note": ""}
    arrivee = dt.datetime.fromisoformat(e["arrivee"])
    msg = f"{t['nom']} : {e['km']} km, {e['minutes']} min de trajet après {e['attente']} min d'attente ; {e['prix']} {e['devise']}"
    if paiement == "carte":
        ok, x = devises.payer(c["carte"], e["prix"], e["devise"], f"Grab : {L[de]['nom'][:30]} → {L[vers]['nom'][:30]}", arrivee,
                              reference=course["id"], simule=simule)
        course["statut"] = "payee" if ok else "carte_refusee"
        course["note"] = x["note"]
        msg += f" ; carte : {'débit de ' + devises.eur(x['total_eur']) if ok else 'REFUSÉE (' + x['operation']['note'] + ')'}"
    else:
        moment = quand if t["forfaits"] else arrivee  # coupon : payé d'avance au comptoir
        ok, m = devises.depenser(e["prix"], e["devise"], f"{t['nom']} ({L[vers]['nom'][:40]})", moment, simule=simule)
        if not ok and t["forfaits"]:
            return False, f"Comptoir des taxis à coupon : {m}", None
        course["statut"] = "payee" if ok else "impayee"
        course["note"] = m
        msg += f" ; espèces : {m}"
    if not simule:
        journal.append(course)
        ecrire_csv(JOURNAL, journal, COL_JOURNAL)
    return True, msg + f" ; arrivée prévue à {arrivee:%H:%M}", course


def donnees_telephone(t=None):
    """Lieux de la ville où se trouve William et prix de toutes les courses possibles maintenant (même calcul que le moteur)."""
    t = t or maintenant_simule()
    naif = t.replace(tzinfo=None)
    import meteo
    ville = meteo.station_courante()
    if ville not in VILLES:
        return {"ville": "", "lieux": [], "courses": {}, "compte": compte()}
    import devises
    L = lieux(ville)
    tarifs = lire_csv(TARIFS)
    courses = {}
    for a in L:
        for b in L:
            if a != b:
                courses[f"{a}>{b}"] = [{k: e[k] for k in ("service", "nom", "type", "km", "minutes", "attente", "prix", "majoration", "paiement")}
                                       for e in sorted((estimer(x["id"], a, b, naif, L) for x in tarifs if disponible(x, a, L)),
                                                       key=lambda e: e["prix"])]
    return {"ville": ville, "heure": f"{naif:%H:%M}", "ici": ici(ville) or "", "taux": devises.taux_connu("PHP", naif.date()),
            "lieux": [{"id": i, "nom": l["nom"]} for i, l in L.items()], "courses": courses, "compte": compte()}


def verifier():
    erreurs = []
    L = lieux()
    for t in lire_csv(TARIFS):
        if t["type"] not in ("vtc", "taxi"):
            erreurs.append(f"courses.csv : type inconnu ({t['id']})")
        if not t["forfaits"]:
            try:
                float(t["prise_en_charge"]), float(t["par_km"]), float(t["par_min"])
            except ValueError:
                erreurs.append(f"courses.csv : tarif illisible ({t['id']})")
    for d in lire_csv(DISTANCES):
        for x in (d["de"], d["vers"]):
            if x not in L:
                erreurs.append(f"distances.csv : lieu inconnu {x}")
    for c in lire_csv(COORD):
        if c["lieu"] not in L:
            erreurs.append(f"coordonnees.csv : {c['lieu']} absent de donnees/lieux.csv")
    return erreurs


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("options")
    s.add_argument("--de", required=True)
    s.add_argument("--vers", required=True)
    s.add_argument("--quand")
    s = sub.add_parser("installer")
    s.add_argument("--quand")
    s = sub.add_parser("carte")
    s.add_argument("--carte", required=True)
    s.add_argument("--quand")
    s = sub.add_parser("commander")
    s.add_argument("--service", required=True)
    s.add_argument("--de", required=True)
    s.add_argument("--vers", required=True)
    s.add_argument("--paiement", default="especes", choices=["especes", "carte"])
    s.add_argument("--quand")
    s.add_argument("--simule", action="store_true")
    sub.add_parser("lieux")
    sub.add_parser("ici")
    sub.add_parser("verifier")
    a = ap.parse_args()
    quand = analyser_instant_naif(a.quand) if getattr(a, "quand", None) else maintenant_naif()
    if a.cmd == "options":
        for e in options(a.de, a.vers, quand):
            print(f"{e['nom']:40s} {e['prix']:>6d} {e['devise']}  attente {e['attente']:>2d} min · trajet {e['minutes']:>3d} min · {e['km']} km"
                  + (f" · majoration × {e['majoration']}" if e["majoration"] > 1 else "") + f" · {e['paiement']}"
                  + (" · pluie" if e["pluie"] == 1 else " · forte pluie" if e["pluie"] == 2 else ""))
    elif a.cmd == "installer":
        print(installer(quand))
    elif a.cmd == "carte":
        print(enregistrer_carte(a.carte, quand))
    elif a.cmd == "commander":
        ok, msg, _ = commander(a.service, a.de, a.vers, quand, a.paiement, a.simule)
        print(("OK" if ok else "REFUSÉ") + f" : {msg}" + (" (essai : rien d'écrit)" if a.simule else ""))
        return 0 if ok else 1
    elif a.cmd == "lieux":
        for i, l in lieux().items():
            print(f"{i:22s} {l['zone']:10s} {l['nom']}")
    elif a.cmd == "ici":
        print(ici() or "(lieu de l'horloge non reconnu)")
    elif a.cmd == "verifier":
        e = verifier()
        print("\n".join(e) if e else "courses : OK")
        return 1 if e else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
