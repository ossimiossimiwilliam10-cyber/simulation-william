"""HORAIRES DE VIE DES PERSONNAGES (créé le 14/10/2026 : univers vivant, demande de l'utilisateur) : sommeil, travail et trajets
de chaque personnage, déduits de son métier (`donnees/population/routines.csv`) et personnalisés de façon stable (décalage de
± 30 minutes et jour de repos tirés de son identifiant). Ils fixent L'HEURE des réponses et des initiatives : un personnage qui
dort, travaille ou conduit ne répond pas avant d'être libre (fini les heures choisies à la main).

    python outils/routines.py voir "Kiara Reyes" [--jour 2040-07-20]     # horaires du jour, fenêtres libres
    python outils/routines.py etat "Kiara Reyes" --quand "2040-07-20 10:00" [--fuseau manille]
    python outils/routines.py prochaine "Kiara Reyes" --quand "2040-07-20 10:00"

États : sommeil, travail, trajet, libre. Un personnage est JOIGNABLE quand il est libre ou en trajet (il lit et répond sur son
téléphone) ; le travail et le sommeil retardent une réponse jusqu'à la fin de la plage.
Fuseau d'un personnage : contexte « …_manille » → Manille, « …_seoul » → Séoul, « …_bresil » → Brésil (22/10/2026) ; sinon Luxembourg (Audun-le-Tiche et Esch sont dans le même fuseau).
"""
import argparse
import datetime as dt
import hashlib
import re
import sys
from zoneinfo import ZoneInfo

from commun import DONNEES, OUTILS, lire_csv, utf8

sys.path.insert(0, str(OUTILS))
import fuseaux  # noqa: E402

FICHIER = DONNEES / "population" / "routines.csv"
JOURS = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
PAS = 5  # minutes


def lire():
    return lire_csv(FICHIER)


def personnage(nom):
    import jet
    p = jet.fiche_personnage(nom)
    if p is None:
        sys.exit(f"Personnage inconnu : {nom} (etat/personnages.csv)")
    return p


def zone_de(p):
    c = p.get("contexte") or ""
    for suffixe, z in (("_manille", "manille"), ("_seoul", "seoul"), ("_bresil", "bresil"), ("_abidjan", "abidjan")):
        if c.endswith(suffixe):
            return z
    return "luxembourg"


def _h(texte):
    hh, mm = texte.split(":")
    return int(hh) * 60 + int(mm)


def _graine(p, sel):
    return int(hashlib.sha256(f"{p.get('id') or p.get('nom')}|{sel}".encode("utf-8")).hexdigest(), 16)


def regle(p):
    """Ligne de routines.csv qui convient au métier et au fuseau du personnage (la première qui correspond)."""
    metier = f"{p.get('metier', '')} {p.get('role', '')}".lower()
    z = zone_de(p)
    for r in lire():
        if r["zone"] not in ("*", z):
            continue
        if re.search(r["motif"], metier, re.I):
            return r
    return lire()[-1]


def routine(p):
    """Routine personnalisée : décalage stable de -30 à +30 min, jour(s) de repos stables pour les rythmes « 6/7 » et « 5/7 »."""
    r = regle(p)
    decal = _graine(p, "decalage") % 61 - 30
    if r["jours"] in ("6/7", "5/7"):
        n_repos = 1 if r["jours"] == "6/7" else 2
        g = _graine(p, "repos")
        repos = {(g + k * 3) % 7 for k in range(n_repos)}
        jours = [j for i, j in enumerate(JOURS) if i not in repos]
    else:
        jours = [j for j in r["jours"].split(",") if j]
    travail = None
    if r["travail"]:
        a, b = r["travail"].split("-")
        travail = ((_h(a) + decal) % 1440, (_h(b) + decal) % 1440)
    a, b = r["sommeil"].split("-")
    sommeil = ((_h(a) + decal) % 1440, (_h(b) + decal) % 1440)
    return {"regle": r["id"], "zone": zone_de(p), "jours": jours, "travail": travail, "trajet": int(r["trajet_min"] or 0),
            "sommeil": sommeil, "vacances": r["vacances"] == "oui", "decalage": decal}


def _dans(m, plage):
    a, b = plage
    return a <= m < b if a <= b else (m >= a or m < b)


def en_vacances(p, jour):
    """Vacances scolaires (pays du personnage) pour les élèves, étudiants et enseignants."""
    import calendrier_2040 as cal
    pays = {"manille": "ph", "seoul": "kr", "bresil": "br", "abidjan": "ci"}.get(zone_de(p), "lu")
    for l in cal.lire_donnees("calendrier-scolaire.csv"):
        if l.get("pays") == pays and l["periode"].startswith(("vacances", "conge")) and l["debut"] <= jour.isoformat() <= l["fin"]:
            return True
    return False


def travaille_ce_jour(p, rt, jour):
    if rt["travail"] is None:
        return False
    if rt["vacances"] and en_vacances(p, jour):
        return False
    return JOURS[jour.weekday()] in rt["jours"]


def etat(p, instant):
    """sommeil | travail | trajet | libre, à l'instant (aware) converti dans le fuseau du personnage."""
    rt = routine(p)
    loc = fuseaux.convertir(instant, rt["zone"])
    m = loc.hour * 60 + loc.minute
    jour = loc.date()
    if rt["travail"]:
        a, b = rt["travail"]
        # un poste qui passe minuit appartient au jour où il commence
        debut_jour = jour if (a <= b or m >= a) else jour - dt.timedelta(days=1)
        if travaille_ce_jour(p, rt, debut_jour) and _dans(m, rt["travail"]):
            return "travail"
        t = rt["trajet"]
        if t and travaille_ce_jour(p, rt, debut_jour if _dans(m, (a, b)) else jour):
            if _dans(m, ((a - t) % 1440, a)) or _dans(m, (b, (b + t) % 1440)):
                return "trajet"
    if _dans(m, rt["sommeil"]):
        return "sommeil"
    return "libre"


def joignable(p, instant):
    return etat(p, instant) in ("libre", "trajet")


def prochaine_dispo(p, apres, max_jours=4):
    """Premier instant (pas de 5 min) où le personnage est joignable, à partir de `apres` (aware)."""
    t = apres.replace(second=0, microsecond=0)
    fin = t + dt.timedelta(days=max_jours)
    while t <= fin:
        if joignable(p, t):
            return t
        t += dt.timedelta(minutes=PAS)
    return apres


def fenetres_libres(p, jour, de="07:00", a="23:59"):
    """Fenêtres joignables d'un jour (heure locale du personnage), bornées à [de, a] : [(début aware, fin aware)]."""
    rt = routine(p)
    tz = ZoneInfo(fuseaux.ZONES[rt["zone"]])
    res, debut = [], None
    m = _h(de)
    while m <= _h(a):
        t = dt.datetime.combine(jour, dt.time(m // 60, m % 60), tzinfo=tz)
        ok = joignable(p, t)
        if ok and debut is None:
            debut = t
        if not ok and debut is not None:
            res.append((debut, t))
            debut = None
        m += PAS
    if debut is not None:
        res.append((debut, dt.datetime.combine(jour, dt.time(23, 59), tzinfo=tz)))
    return res


def decrire(p, jour=None):
    rt = routine(p)
    f = lambda x: f"{x // 60:02d}:{x % 60:02d}"  # noqa: E731
    t = f"{p['nom']} ({p.get('metier', '')}) : règle « {rt['regle']} », fuseau {rt['zone']}, décalage {rt['decalage']:+d} min ; "
    t += (f"travail {f(rt['travail'][0])}-{f(rt['travail'][1])} ({', '.join(rt['jours'])}), trajet {rt['trajet']} min ; "
          if rt["travail"] else "pas d'horaires de travail ; ")
    t += f"sommeil {f(rt['sommeil'][0])}-{f(rt['sommeil'][1])}"
    if jour:
        fen = fenetres_libres(p, jour, "00:00")
        t += f"\n  {jour:%d/%m/%Y} : " + ("travaille" if travaille_ce_jour(p, rt, jour) else "repos") + " ; joignable : " + \
             ", ".join(f"{a:%H:%M}-{b:%H:%M}" for a, b in fen)
    return t


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    for nom in ("voir", "etat", "prochaine"):
        q = sp.add_parser(nom)
        q.add_argument("nom")
        q.add_argument("--jour")
        q.add_argument("--quand")
        q.add_argument("--fuseau")
    args = ap.parse_args()
    p = personnage(args.nom)
    if args.cmd == "voir":
        print(decrire(p, dt.date.fromisoformat(args.jour) if args.jour else None))
        return 0
    from commun import maintenant_simule
    if args.quand:
        d, h = args.quand.split()
        t = fuseaux.analyser_instant(d, h, args.fuseau or zone_de(p))
    else:
        t = maintenant_simule()
    if args.cmd == "etat":
        print(f"{p['nom']} à {fuseaux.convertir(t, zone_de(p)):%d/%m %H:%M} ({zone_de(p)}) : {etat(p, t)}")
    else:
        n = prochaine_dispo(p, t)
        print(f"{p['nom']} joignable à partir du {fuseaux.convertir(n, zone_de(p)):%d/%m %H:%M} ({zone_de(p)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
