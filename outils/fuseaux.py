"""Fuseaux horaires de la simulation : plus jamais de conversion d'heure « de tête » (audit du 09/08/2040, correction n° 48 :
le Cap-Vert est en UTC−1 toute l'année, Lisbonne en été en UTC+1, soit 2 h d'écart et non 1 h).

    python outils/fuseaux.py 2040-08-09 14:15 lisbonne              # l'heure dans tous les lieux
    python outils/fuseaux.py 09/08 12h40 mindelo --vers lisbonne    # une conversion
    python outils/fuseaux.py --ecarts 2040-08-09                    # écarts à Abidjan ce jour-là

Lieux (alias acceptés) : abidjan, lisbonne, luxembourg (esch, audun, differdange), mindelo (sao vicente, sal, praia),
casablanca, douala (yaoundé), paris. Règles de l'heure d'été : base de données IANA (zoneinfo) ; en 2040 le moteur suppose que les
règles actuelles de l'Union européenne et du Maroc (heure à UTC+0 pendant le Ramadan) sont inchangées (projection).
Utilisable en module : `import fuseaux; fuseaux.heure(2040, 8, 9, 14, 15, "lisbonne")`.
"""
import argparse
import datetime as dt
import re
import sys
from zoneinfo import ZoneInfo

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ZONES = {
    "abidjan": "Africa/Abidjan",
    "lisbonne": "Europe/Lisbon",
    "luxembourg": "Europe/Luxembourg",
    "mindelo": "Atlantic/Cape_Verde",
    "casablanca": "Africa/Casablanca",
    "douala": "Africa/Douala",
    "addis": "Africa/Addis_Ababa",
    "manille": "Asia/Manila",
    "paris": "Europe/Paris",
}
ALIAS = {
    "esch": "luxembourg", "audun": "luxembourg", "audun-le-tiche": "luxembourg", "differdange": "luxembourg",
    "lux": "luxembourg", "findel": "luxembourg", "sao vicente": "mindelo", "são vicente": "mindelo", "sal": "mindelo",
    "praia": "mindelo", "cap-vert": "mindelo", "cabo verde": "mindelo", "yaoundé": "douala", "yaounde": "douala",
    "cameroun": "douala", "côte d'ivoire": "abidjan", "cote d'ivoire": "abidjan", "abj": "abidjan", "lis": "lisbonne",
    "cmn": "casablanca", "vxe": "mindelo", "lisbon": "lisbonne",
    "nsi": "douala", "add": "addis", "addis-abeba": "addis", "bru": "luxembourg", "fra": "luxembourg", "cdg": "paris",
    "mnl": "manille", "manila": "manille", "philippines": "manille",
}


def zone(nom):
    n = nom.strip().lower()
    n = ALIAS.get(n, n)
    if n not in ZONES:
        sys.exit(f"Lieu inconnu : {nom} (connus : {', '.join(ZONES)} ; alias : {', '.join(sorted(ALIAS))})")
    return n


def heure(annee, mois, jour, h, m, lieu):
    """datetime aware à `lieu`."""
    return dt.datetime(annee, mois, jour, h, m, tzinfo=ZoneInfo(ZONES[zone(lieu)]))


def convertir(instant, lieu):
    return instant.astimezone(ZoneInfo(ZONES[zone(lieu)]))


def decalage(instant):
    """Écart à UTC, en heures (float)."""
    return instant.utcoffset().total_seconds() / 3600


def analyser_date(texte, defaut_annee=2040):
    t = texte.strip()
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", t)
    if m:
        return int(m.group(1)), int(m.group(2)), int(m.group(3))
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})(?:/(\d{4}))?", t)
    if m:
        return int(m.group(3) or defaut_annee), int(m.group(2)), int(m.group(1))
    sys.exit(f"Date illisible : {texte} (attendu AAAA-MM-JJ ou JJ/MM[/AAAA])")


def analyser_heure(texte):
    m = re.fullmatch(r"(\d{1,2})\s*[h:]\s*(\d{0,2})", texte.strip().lower())
    if not m:
        sys.exit(f"Heure illisible : {texte} (attendu 14:15 ou 14h15)")
    return int(m.group(1)), int(m.group(2) or 0)


def analyser_instant(date_txt, heure_txt, lieu):
    a, mo, j = analyser_date(date_txt)
    h, mi = analyser_heure(heure_txt)
    return heure(a, mo, j, h, mi, lieu)


def libelle_ecart(instant):
    d = decalage(instant)
    signe = "+" if d >= 0 else "−"
    return f"UTC{signe}{abs(d):g}"


def tableau(instant, origine=None):
    lignes = []
    ref = instant.date()
    for nom in ZONES:
        loc = convertir(instant, nom)
        jour = (loc.date() - ref).days
        suffixe = "" if jour == 0 else f" (J{jour:+d})"
        marque = "  <- origine" if origine and nom == origine else ""
        lignes.append(f"  {nom:11s} {loc:%a %d/%m/%Y %H:%M}{suffixe}  {libelle_ecart(loc)}{marque}")
    return "\n".join(lignes)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("date", nargs="?")
    ap.add_argument("heure", nargs="?")
    ap.add_argument("lieu", nargs="?")
    ap.add_argument("--vers", help="ne donner que l'heure dans ce lieu")
    ap.add_argument("--ecarts", metavar="DATE", help="écarts de chaque lieu avec Abidjan à midi, ce jour-là")
    args = ap.parse_args()
    if args.ecarts:
        a, mo, j = analyser_date(args.ecarts)
        base = heure(a, mo, j, 12, 0, "abidjan")
        print(f"Écarts avec Abidjan (UTC+0) le {j:02d}/{mo:02d}/{a} :")
        for nom in ZONES:
            loc = convertir(base, nom)
            e = decalage(loc)
            print(f"  {nom:11s} {libelle_ecart(loc):8s} ({e:+g} h par rapport à Abidjan)")
        return 0
    if not (args.date and args.heure and args.lieu):
        ap.print_help()
        return 1
    origine = zone(args.lieu)
    instant = analyser_instant(args.date, args.heure, origine)
    if args.vers:
        loc = convertir(instant, args.vers)
        jour = (loc.date() - instant.date()).days
        suffixe = "" if jour == 0 else f" (J{jour:+d})"
        print(f"{instant:%d/%m/%Y %H:%M} à {origine} = {loc:%d/%m/%Y %H:%M}{suffixe} à {zone(args.vers)} ({libelle_ecart(loc)})")
        return 0
    print(f"{instant:%d/%m/%Y %H:%M} à {origine} ({libelle_ecart(instant)}) :")
    print(tableau(instant, origine))
    return 0


if __name__ == "__main__":
    sys.exit(main())
