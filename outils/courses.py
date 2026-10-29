"""COURSES EN VILLE (créé le 14/10/2026 : William arrive à Manille sans pesos ; besoin : rejoindre son hôtel, puis circuler).
VTC (application Kakao T) et taxis (ordinaires, jaunes de l'aéroport, à coupon). Calcul DÉTERMINISTE : distance, durée, majoration et
attente se déduisent du lieu, de l'heure (créneau de 15 minutes), du jour et de la pluie du jour (etat/meteo-manille.csv) ; la page
« Courses » du téléphone et le moteur obtiennent le même prix. Tarifs 2026 × 1,35 (même coefficient que prix.py).

    python outils/courses.py options --de naia_t3 --vers city_garden [--quand "AAAA-MM-JJ HH:MM"]
    python outils/courses.py installer [--quand …]                        # l'application Kakao T (décision du joueur)
    python outils/courses.py carte --carte visa_debit [--quand …]         # carte enregistrée dans l'application
    python outils/courses.py commander --service grab_car --de naia_t3 --vers city_garden [--paiement especes|carte] [--quand …] [--simule]
    python outils/courses.py accepter C003 [--quand …] | annuler C003       # prix fixe demandé par un chauffeur (aléa A33)
    python outils/courses.py lieux | ici | verifier
ALÉA A33 (validé par l'utilisateur le 14/10/2026) : à chaque course, le chauffeur est tiré (T24a pour un taxi au compteur :
compteur 70 %, prix fixe demandé 20 %, détour 10 % ; T24b pour un VTC : arrive 90 %, annule 10 %) ; un prix fixe attend la décision
de William (accepter ou annuler) ; l'application du téléphone montre les prix ordinaires, jamais l'aléa.

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
import random
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
DETOUR = 1.35  # distance par la route ≈ distance à vol d'oiseau × 1,35 à Séoul (estimation), sauf ligne de distances.csv ; avant : 1,45 (Metro Manila)
VILLES = {"manille": {"pays": "ph", "devise": "PHP", "meteo": ETAT / "meteo-manille.csv", "appli": "Grab"},
          "seoul": {"pays": "kr", "devise": "KRW", "meteo": ETAT / "meteo-seoul.csv", "appli": "Kakao T"},
          "abidjan": {"pays": "ci", "devise": "XOF", "meteo": ETAT / "meteo-abidjan.csv", "appli": "Yango"}}  # 29/10/2026 : P40
# km/h de porte à porte selon l'heure, en semaine (estimation : Metro Manila, parmi les circulations les plus lentes d'Asie)
VITESSES = [(0, 45), (5, 36), (7, 19), (10, 27), (16, 21), (20, 30), (22, 42)]  # Séoul (estimation du moteur : vitesse moyenne en ville ≈ 25 km/h) ; avant : Metro Manila


def _alea(*cles):
    """Nombre fixe dans [0, 1) pour ces clés (même résultat en Python et à chaque relecture)."""
    return int(hashlib.sha1("|".join(map(str, cles)).encode("utf-8")).hexdigest()[:8], 16) / 2 ** 32


def maintenant_naif():
    return maintenant_simule().replace(tzinfo=None)


def ville_courante():
    """Ville des courses : celle de la station météo du lieu de William (fuseau de l'horloge), Séoul sinon (29/10/2026 : Abidjan, P40)."""
    try:
        import meteo
        v = meteo.station_courante()
    except Exception:  # noqa: BLE001
        v = "seoul"
    return v if v in VILLES else "seoul"


def lieux(ville=None):
    ville = ville or ville_courante()
    import lieux as L
    noms = L.lire()
    return {c["lieu"]: {"id": c["lieu"], "nom": noms.get(c["lieu"], {}).get("nom", c["lieu"]), "lat": float(c["lat"]), "lon": float(c["lon"]),
                        "zone": c["zone"], "motcles": [m.strip() for m in c["motcles"].split("·")]}
            for c in lire_csv(COORD) if c["lieu"] in noms and noms[c["lieu"]]["fuseau"] == ville}


def ici(ville=None):
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


def pluie(quand, ville=None):
    """0 sec, 1 pluie, 2 forte pluie ou rues inondées, à cette heure (fixe pour la journée et l'heure)."""
    ville = ville or ville_courante()
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


def type_jour(jour, pays=None):
    pays = pays or VILLES[ville_courante()]["pays"]
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


def duree_minutes(km, depart, niveau_pluie, de, vers):
    """Durée de la course : les 12 premiers kilomètres à la vitesse de la ville, le reste sur voie rapide (≈ 70 km/h, ralentie aux
    heures de pointe et sous la pluie ; 22/10/2026 : l'aéroport d'Incheon est à 57 km de Yeonnam-dong, pas à 3 heures de route)."""
    v = vitesse(depart, niveau_pluie, de, vers)
    urbain = min(km, 12.0)
    rapide = km - urbain
    vr = 70 * (0.7 if (7 <= depart.hour < 10 or 16 <= depart.hour < 20) else 1.0) * (1.0, 0.85, 0.65)[niveau_pluie]
    return max(4, round(urbain / v * 60 + (rapide / vr * 60 if rapide else 0)))


def creneau(quand):
    return quand.replace(minute=quand.minute // 15 * 15, second=0, microsecond=0)


def majoration(t, de, quand, niveau_pluie, L):
    if t["id"].endswith("_seoul"):  # taxis de Séoul : supplément de nuit de 20 % (22 h - 23 h et 2 h - 4 h) ou 40 % (23 h - 2 h), F093
        h = quand.hour
        return 1.4 if (h >= 23 or h < 2) else 1.2 if (h == 22 or 2 <= h < 4) else 1.0
    if t["type"] != "vtc":
        return 1.0
    h, tj, zone = quand.hour, type_jour(quand.date()), L[de]["zone"]
    m = 1.05
    if zone == "aeroport":
        m = 1.35 if (h >= 21 or h < 3) else 1.15
    if tj == "semaine" and (7 <= h < 10 or 16 <= h < 20):
        m = max(m, 1.45)
    if quand.weekday() in (4, 5) and (h >= 21 or h < 3) and zone in ("gangnam", "mapo"):
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
    t = tarif(ident)
    L = L or lieux(t["ville"])
    if de not in L or vers not in L:
        sys.exit(f"Lieu inconnu : {de if de not in L else vers} (donnees/coordonnees.csv)")
    if not disponible(t, de, L):
        return None
    np_ = pluie(quand, t["ville"])
    km = distance_km(de, vers, L)
    att = attente(t, de, quand, np_, L)
    depart = quand + dt.timedelta(minutes=att)
    minutes = duree_minutes(km, depart, np_, de, vers)
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
            "prix": round(prix), "devise": VILLES[t["ville"]]["devise"], "majoration": maj, "pluie": np_, "paiement": t["paiement"],
            "depart": f"{depart:%Y-%m-%d %H:%M}", "arrivee": f"{depart + dt.timedelta(minutes=minutes):%Y-%m-%d %H:%M}"}


def options(de, vers, quand, ville=None):
    ville = ville or ville_courante()
    L = lieux(ville)
    res = [estimer(t["id"], de, vers, quand, L) for t in lire_csv(TARIFS) if t["ville"] == ville and disponible(t, de, L)]
    return sorted([r for r in res if r], key=lambda r: r["prix"])


def compte():
    return {l["cle"]: l["valeur"] for l in lire_csv(COMPTE)}


def _regler(cle, valeur, quand):
    lignes = [l for l in lire_csv(COMPTE) if l["cle"] != cle]
    lignes.append({"cle": cle, "valeur": valeur, "depuis": f"{quand:%Y-%m-%d %H:%M}"})
    ecrire_csv(COMPTE, lignes, ["cle", "valeur", "depuis"])


def appli(ville=None):
    return VILLES[ville or ville_courante()]["appli"]


def cle_installe(ville=None):
    """Clé du compte : « installe » pour Kakao T (Séoul, historique), « installe_<appli> » pour les autres (29/10/2026)."""
    a = appli(ville)
    return "installe" if a == "Kakao T" else f"installe_{a.lower().replace(' ', '_')}"


def installer(quand):
    a = appli()
    if compte().get(cle_installe()) == "oui":
        return f"{a} est déjà installé."
    _regler(cle_installe(), "oui", quand)
    import traces
    traces.ajouter(f"{quand:%d/%m/%Y %H:%M}", f"Inscription à l'application {a} (numéro de téléphone de William vérifié par SMS)", "application",
                   a, "faible")
    return f"{a} installé ; numéro vérifié par SMS ; aucune carte enregistrée (paiement en espèces par défaut)."


def enregistrer_carte(carte, quand):
    import cartes
    cartes.carte(carte)
    _regler("carte", carte, quand)
    return f"Carte enregistrée dans {appli()} : {carte}."


def _journal_ajouter(course):
    journal = lire_csv(JOURNAL)
    journal.append(course)
    ecrire_csv(JOURNAL, journal, COL_JOURNAL)


def _procedure(libelle, valeur):
    import jet
    jet.consigner_json({"mode": "procedure", "libelle": libelle, "valeur": valeur, "regle": "courses.py (aléa A33)"})


def _payer(course, t, L, carte, simule):
    """Paiement à l'arrivée : par la carte enregistrée dans Kakao T, ou en espèces. Met à jour le statut ; renvoie le message."""
    import devises
    arrivee = dt.datetime.fromisoformat(course["arrivee"])
    prix = float(course["prix"])
    if course["paiement"] == "carte":
        ok, x = devises.payer(carte, prix, course["devise"], f"{appli()} : {L[course['de']]['nom'][:30]} → {L[course['vers']]['nom'][:30]}",
                              arrivee, reference=course["id"], simule=simule)
        course["statut"] = "payee" if ok else "carte_refusee"
        course["note"] = (course["note"] + " · " if course["note"] else "") + x["note"]
        return "carte : " + ("débit de " + devises.eur(x["total_eur"]) if ok else "REFUSÉE (" + x["operation"]["note"] + ")")
    ok, m = devises.depenser(prix, course["devise"], f"{t['nom']} ({L[course['vers']]['nom'][:40]})", arrivee, simule=simule)
    course["statut"] = "payee" if ok else "impayee"
    course["note"] = (course["note"] + " · " if course["note"] else "") + m
    return "espèces : " + m + ("" if ok else " (IMPAYÉE à l'arrivée : scène à jouer)")


def commander(ident, de, vers, quand, paiement="especes", simule=False):
    """Commande ou prend une course ; renvoie (ok, message, course). Aléa A33 (validé le 14/10/2026) : T24a pour un taxi au
    compteur (compteur, prix fixe demandé, détour), T24b pour un VTC (arrive, annule) ; le taxi à coupon n'a pas d'aléa."""
    import devises
    import jet
    t = tarif(ident)
    L = lieux(t["ville"])
    c = compte()
    if t["type"] == "vtc" and c.get(cle_installe(t["ville"])) != "oui":
        return False, f"{appli(t['ville'])} n'est pas installé sur le téléphone de William.", None
    if paiement == "carte":
        if t["type"] != "vtc":
            return False, "Ce taxi se paie en espèces.", None
        if not c.get("carte"):
            return False, f"Aucune carte enregistrée dans {appli(t['ville'])}.", None
    e = estimer(ident, de, vers, quand, L)
    if e is None:
        return False, f"{t['nom']} : pas de départ depuis {L[de]['nom']}.", None
    rng = random.SystemRandom()
    course = {"id": f"C{len(lire_csv(JOURNAL)) + 1:03d}", "demande": f"{quand:%Y-%m-%d %H:%M}", "service": ident, "de": de, "vers": vers,
              "km": e["km"], "minutes": e["minutes"], "attente": e["attente"], "prix": e["prix"], "devise": e["devise"],
              "paiement": "carte" if paiement == "carte" else "especes", "statut": "", "arrivee": e["arrivee"], "note": ""}
    trajet = f"de {L[de]['nom'][:40]} à {L[vers]['nom'][:40]}, {quand:%d/%m %H:%M}"
    if t["type"] == "vtc":
        r = jet.tirer("T24b", [], f"Chauffeur {appli(t['ville'])} ({trajet})", simule=simule, texte=False)
        course["note"] = f"T24b : {r['issue']} (jet {r['jet']:.1f})"
        if r["issue"] == "annule":
            apres = rng.randint(2, max(3, e["attente"]))
            e2 = estimer(ident, de, vers, quand + dt.timedelta(minutes=apres), L)
            course.update(attente=apres + e2["attente"], minutes=e2["minutes"], prix=e2["prix"], arrivee=e2["arrivee"])
            course["note"] += f" · le premier chauffeur annule après {apres} min ; un autre accepte (prix recalculé : {e2['prix']} {e2['devise']})"
            if not simule:
                _procedure(f"Course {course['id']} : annulation du premier chauffeur", f"après {apres} min")
    elif not t["forfaits"]:
        r = jet.tirer("T24a", [], f"Chauffeur de taxi ({t['nom']}, {trajet})", simule=simule, texte=False)
        course["note"] = f"T24a : {r['issue']} (jet {r['jet']:.1f})"
        if r["issue"] == "prix_fixe":
            propose = max(int(round(e["prix"] * rng.uniform(1.6, 2.2) / 50.0)) * 50, int(e["prix"]) + 50)
            course.update(prix=propose, statut="prix_fixe_propose")
            course["note"] += f" · refuse le compteur et annonce {propose} {e['devise']} (compteur estimé : {e['prix']})"
            if not simule:
                _journal_ajouter(course)
                _procedure(f"Course {course['id']} : prix fixe demandé", f"{propose} {e['devise']}")
            return True, (f"PRIX FIXE DEMANDÉ : le chauffeur refuse le compteur et annonce {propose} {e['devise']} (compteur ≈ {e['prix']}) ; "
                          f"William décide : courses.py accepter {course['id']} ou courses.py annuler {course['id']}"), course
        if r["issue"] == "detour":
            fp, fd = rng.uniform(1.25, 1.5), rng.uniform(1.2, 1.4)
            minutes = round(e["minutes"] * fd)
            depart = dt.datetime.fromisoformat(e["depart"])
            course.update(prix=round(e["prix"] * fp), minutes=minutes, arrivee=f"{depart + dt.timedelta(minutes=minutes):%Y-%m-%d %H:%M}")
            course["note"] += f" · détour ou compteur rapide : {course['prix']} {e['devise']} au lieu d'environ {e['prix']}, {minutes} min"
            if not simule:
                _procedure(f"Course {course['id']} : détour", f"prix × {fp:.2f}, durée × {fd:.2f}")
    if t["forfaits"]:  # taxi à coupon : payé d'avance au comptoir
        ok, m = devises.depenser(e["prix"], e["devise"], f"{t['nom']} ({L[vers]['nom'][:40]})", quand, simule=simule)
        if not ok:
            return False, f"Comptoir des taxis à coupon : {m}", None
        course["statut"], course["note"] = "payee", m
        msg_p = "espèces : " + m
    else:
        msg_p = _payer(course, t, L, c.get("carte"), simule)
    if not simule:
        _journal_ajouter(course)
    arr = dt.datetime.fromisoformat(course["arrivee"])
    return True, (f"{t['nom']} : {course['km']} km, {course['minutes']} min de trajet après {course['attente']} min d'attente ; "
                  f"{course['prix']} {course['devise']} ; {msg_p} ; arrivée prévue à {arr:%H:%M} [{course['note']}]"), course


def accepter(cid, quand, simule=False):
    """William accepte le prix fixe demandé par le chauffeur : le taxi part maintenant ; paiement en espèces à l'arrivée."""
    journal = lire_csv(JOURNAL)
    course = next((x for x in journal if x["id"] == cid), None)
    if course is None or course["statut"] != "prix_fixe_propose":
        return False, f"{cid} : aucune course en attente d'un accord sur le prix"
    t = tarif(course["service"])
    L = lieux(t["ville"])
    arrivee = quand + dt.timedelta(minutes=int(course["minutes"]))
    course["arrivee"] = f"{arrivee:%Y-%m-%d %H:%M}"
    course["note"] += f" · prix fixe accepté à {quand:%H:%M}"
    msg = _payer(course, t, L, None, simule)
    if not simule:
        ecrire_csv(JOURNAL, journal, COL_JOURNAL)
    return True, f"{course['prix']} {course['devise']} convenus ; arrivée prévue à {arrivee:%H:%M} ; {msg}"


def annuler(cid, quand, simule=False):
    journal = lire_csv(JOURNAL)
    course = next((x for x in journal if x["id"] == cid), None)
    if course is None or course["statut"] not in ("prix_fixe_propose", ""):
        return False, f"{cid} : rien à annuler"
    course["statut"] = "annulee"
    course["note"] += f" · William refuse à {quand:%H:%M}"
    if not simule:
        ecrire_csv(JOURNAL, journal, COL_JOURNAL)
    return True, f"{cid} annulée (William ne monte pas)"


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
    tarifs = [x for x in lire_csv(TARIFS) if x["ville"] == ville]
    courses = {}
    for a in L:
        for b in L:
            if a != b:
                courses[f"{a}>{b}"] = [{k: e[k] for k in ("service", "nom", "type", "km", "minutes", "attente", "prix", "majoration", "paiement")}
                                       for e in sorted((estimer(x["id"], a, b, naif, L) for x in tarifs if disponible(x, a, L)),
                                                       key=lambda e: e["prix"])]
    return {"ville": ville, "heure": f"{naif:%H:%M}", "ici": ici(ville) or "", "taux": devises.taux_connu(VILLES[ville]["devise"], naif.date()), "devise": VILLES[ville]["devise"], "appli": VILLES[ville]["appli"],
            "lieux": [{"id": i, "nom": l["nom"]} for i, l in L.items()], "courses": courses, "compte": compte()}


def verifier():
    erreurs = []
    L = {k: v for ville in VILLES for k, v in lieux(ville).items()}
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
    for nom in ("accepter", "annuler"):
        s = sub.add_parser(nom)
        s.add_argument("course")
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
    elif a.cmd in ("accepter", "annuler"):
        ok, msg = (accepter if a.cmd == "accepter" else annuler)(a.course, quand, a.simule)
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
