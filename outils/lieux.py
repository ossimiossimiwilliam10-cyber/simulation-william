"""Lieux de la simulation (créé le 11/10/2026) : horaires vérifiés ou estimés, fermetures des jours fériés selon le pays (droit
local d'Alsace-Moselle compris), accès, prix repères, et RÉSERVOIR D'AMBIANCES qui tourne pour éviter les tics d'écriture
(« la clim souffle », « l'odeur de lessive »… relevés dans l'univers 1).

    python outils/lieux.py liste
    python outils/lieux.py voir supermarche_audun                       # à l'heure de l'horloge : ouvert ? + 2 détails d'ambiance
    python outils/lieux.py voir club_combat --quand "2040-07-14 18:30"  # à une autre heure
    python outils/lieux.py ouverts --quand "2040-07-14 10:00"           # qui est ouvert à ce moment-là
    python outils/lieux.py voir rue_william --simule                     # sans marquer les détails comme utilisés

Données : `donnees/lieux.csv` (horaires « lun-ven 08:30-12:00,14:00-19:00 / sam 08:30-19:00 / dim fermé » ; jours fériés
« ferme:fr », « ferme:lu » ou « ouvert ») et `donnees/ambiances.csv` (lieu ; saison ; moment ; détail ; dernier usage).
`voir` propose les deux détails les moins récemment utilisés et note leur usage (date de l'horloge) : la variété devient mécanique.
Statut d'un lieu : etabli (fait du profil ou vérifié), generique (type réaliste, horaires estimés), propose (à confirmer par
l'utilisateur), a_definir, projection. Un lieu nouveau s'ajoute à la main dans le CSV, après une recherche web si ses horaires comptent.
"""
import argparse
import datetime as dt
import re
import sys

from commun import DONNEES, OUTILS, ecrire_csv, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
LIEUX = DONNEES / "lieux.csv"
AMBIANCES = DONNEES / "ambiances.csv"
COL_AMB = ["lieu", "saison", "moment", "detail", "dernier_usage"]
JOURS_ABR = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]


def lire():
    return {l["id"]: l for l in lire_csv(LIEUX)}


def jours_de(spec):
    spec = spec.strip()
    if spec == "tous":
        return set(range(7))
    res = set()
    for morceau in spec.split(","):
        if "-" in morceau:
            a, b = morceau.split("-")
            i, j = JOURS_ABR.index(a), JOURS_ABR.index(b)
            res |= set(range(i, j + 1)) if i <= j else set(range(i, 7)) | set(range(0, j + 1))
        else:
            res.add(JOURS_ABR.index(morceau))
    return res


def plages(horaires, jour_semaine):
    """Liste de (début, fin) en minutes pour ce jour de la semaine ; [] si fermé."""
    res = None
    for partie in horaires.split("/"):
        partie = partie.strip()
        if not partie:
            continue
        m = re.match(r"([a-z,\-]+)\s+(.*)", partie)
        if not m:
            continue
        jours, reste = m.group(1), m.group(2).strip()
        if jour_semaine not in jours_de(jours):
            continue
        if reste.startswith("ferm"):
            res = []
        elif reste == "24h":
            res = [(0, 24 * 60)]
        else:
            res = []
            for p in reste.split(","):
                a, b = p.strip().split("-")
                ha, ma = (int(x) for x in a.split(":"))
                hb, mb = (int(x) for x in b.split(":"))
                fin = hb * 60 + mb
                res.append((ha * 60 + ma, fin if fin > ha * 60 + ma else fin + 24 * 60))
    return res or []


def ferie(jour, pays):
    import calendrier_2040 as cal
    return [nom for d, nom, _ in cal.fetes(jour.year, pays) if d == jour]


def ouvert(lieu, quand):
    """(ouvert ?, raison)"""
    regle = lieu.get("feries", "ouvert")
    if regle.startswith("ferme:"):
        for pays in regle[6:].split(","):
            f = ferie(quand.date(), pays)
            if f:
                return False, f"fermé : jour férié ({pays.upper()} : {f[0]})"
    minutes = quand.hour * 60 + quand.minute
    p = plages(lieu["horaires"], quand.weekday())
    if not p:
        return False, f"fermé le {JOURS_ABR[quand.weekday()]}"
    for a, b in p:
        if a <= minutes < b:
            return True, f"ouvert jusqu'à {b // 60 % 24:02d}:{b % 60:02d}"
    prochaines = [a for a, _ in p if a > minutes]
    if prochaines:
        return False, f"fermé pour l'instant, ouvre à {prochaines[0] // 60:02d}:{prochaines[0] % 60:02d}"
    return False, "fermé pour la journée"


def saison(jour):
    m = jour.month
    return "ete" if m in (6, 7, 8) else "automne" if m in (9, 10, 11) else "hiver" if m in (12, 1, 2) else "printemps"


def moment(quand):
    h = quand.hour
    return "nuit" if h < 6 or h >= 22 else "matin" if h < 12 else "journee" if h < 18 else "soir"


def details(lieu_id, quand, n=2, marquer=True):
    amb = lire_csv(AMBIANCES)
    s, mo = saison(quand.date()), moment(quand)
    candidats = [a for a in amb if a["lieu"] == lieu_id and a["saison"] in (s, "toutes") and a["moment"] in (mo, "tous")]
    if not candidats:
        candidats = [a for a in amb if a["lieu"] == lieu_id]
    candidats.sort(key=lambda a: (a.get("dernier_usage") or "0000"))
    choisis = candidats[:n]
    if marquer and choisis:
        for a in choisis:
            a["dernier_usage"] = f"{quand:%Y-%m-%d %H:%M}"
        ecrire_csv(AMBIANCES, amb, COL_AMB)
    return [a["detail"].strip() for a in choisis]


def instant(texte):
    if texte:
        d, h = texte.split()
        return dt.datetime.combine(dt.date.fromisoformat(d), dt.time.fromisoformat(h))
    t = maintenant_simule()
    return t.replace(tzinfo=None) if t else dt.datetime(2040, 7, 14, 9, 0)


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("liste")
    p = sp.add_parser("voir")
    p.add_argument("id")
    p.add_argument("--quand")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("ouverts")
    p.add_argument("--quand")
    args = ap.parse_args()
    lieux = lire()
    if args.cmd == "liste":
        for i, l in lieux.items():
            print(f"{i:20s} [{l['statut']:9s}] {l['nom']} ({l['commune']})")
        return 0
    if args.cmd == "ouverts":
        q = instant(args.quand)
        for i, l in lieux.items():
            o, raison = ouvert(l, q)
            print(f"{'OUVERT' if o else 'fermé ':6s} {i:20s} {raison}")
        return 0
    if args.id not in lieux:
        sys.exit(f"Lieu inconnu : {args.id} (python outils/lieux.py liste)")
    l = lieux[args.id]
    q = instant(args.quand)
    o, raison = ouvert(l, q)
    print(f"{l['nom']} — {l['commune']} ({l['pays'].upper()}) [{l['statut']}]")
    print(f"  {q:%d/%m/%Y %H:%M} : {raison}")
    for cle in ("horaires", "acces", "prix", "notes", "source"):
        if l.get(cle):
            print(f"  {cle} : {l[cle]}")
    d = details(args.id, q, marquer=not args.simule)
    if d:
        print("  Ambiance (détails les moins utilisés récemment) : " + " / ".join(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
