"""Calendrier réel de la simulation : jours fériés (Côte d'Ivoire, Luxembourg, Cap-Vert, France avec le droit local d'Alsace-Moselle),
fêtes mobiles chrétiennes et musulmanes,
Ramadan, phases de la lune. Audit du 09/08/2040 : la simulation ne tenait ni Ramadan, ni Korité, ni Tabaski.

    python outils/calendrier_2040.py                          # toute l'année 2040, Luxembourg et France (univers 2)
    python outils/calendrier_2040.py --annee 2041 --pays ci
    python outils/calendrier_2040.py --du 2040-08-09 --au 2040-10-31
    python outils/calendrier_2040.py --jour 2040-08-15        # qu'est-ce qui est férié ce jour-là ?
    python outils/calendrier_2040.py --lune --du 2040-08-01 --au 2040-09-30

Sources et limites (à dire quand un fait en dépend) :
- fêtes chrétiennes : calcul de Pâques (algorithme grégorien), exact ;
- fêtes musulmanes : calendrier hégirien TABULAIRE (arithmétique) : le jour réel dépend de l'observation de la lune et de l'annonce
  officielle (Conseil supérieur des imams de Côte d'Ivoire) : écart de 1 à 2 jours possible ; toujours affichées avec « ≈ » ;
- listes de fériés : état 2025-2026 projeté en 2040 ; les listes du Cap-Vert marquées « ? » sont à vérifier avant usage ;
- phases de la lune : lunaison moyenne (précision ≈ ± 14 h).
"""
import argparse
import datetime as dt
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

JOURS = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]


def paques(annee):
    a = annee % 19
    b, c = divmod(annee, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mois, jour = divmod(h + l - 7 * m + 114, 31)
    return dt.date(annee, mois, jour + 1)


def hijri_vers_gregorien(hy, hm, hd):
    """Calendrier hégirien tabulaire (arithmétique) -> date grégorienne (± 1-2 jours de la date observée)."""
    jd = hd + int(29.5 * (hm - 1) + 0.5) + (hy - 1) * 354 + (3 + 11 * hy) // 30 + 1948439.5 - 1
    jd = int(jd + 0.5)
    a = jd + 32044
    b = (4 * a + 3) // 146097
    c = a - 146097 * b // 4
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    jour = e - (153 * m + 2) // 5 + 1
    mois = m + 3 - 12 * (m // 10)
    annee = 100 * b + d - 4800 + m // 10
    return dt.date(annee, mois, jour)


def fetes_musulmanes(annee):
    """[(date, libellé, approx)] pour l'année grégorienne donnée."""
    resultat = []
    hy0 = int((annee - 622) * 33 / 32)
    for hy in range(hy0 - 1, hy0 + 3):
        for (hm, hd, nom) in ((3, 12, "Maouloud (naissance du Prophète)"), (9, 1, "Début du Ramadan"),
                              (10, 1, "Aïd el-Fitr / Korité"), (12, 10, "Tabaski / Aïd el-Adha")):
            d = hijri_vers_gregorien(hy, hm, hd)
            if d.year == annee:
                resultat.append((d, nom, True))
    return sorted(resultat)


def fetes(annee, pays):
    p = paques(annee)
    lundi_paques = p + dt.timedelta(days=1)
    ascension = p + dt.timedelta(days=39)
    lundi_pentecote = p + dt.timedelta(days=50)
    carnaval = p - dt.timedelta(days=47)
    vendredi_saint = p - dt.timedelta(days=2)
    liste = []
    ajout = lambda d, nom, approx=False: liste.append((d, nom, approx))
    if pays == "ci":
        ajout(dt.date(annee, 1, 1), "Jour de l'an")
        ajout(lundi_paques, "Lundi de Pâques")
        ajout(dt.date(annee, 5, 1), "Fête du travail")
        ajout(ascension, "Ascension")
        ajout(lundi_pentecote, "Lundi de Pentecôte")
        ajout(dt.date(annee, 8, 7), "Fête de l'Indépendance")
        ajout(dt.date(annee, 8, 15), "Assomption")
        ajout(dt.date(annee, 11, 1), "Toussaint")
        ajout(dt.date(annee, 11, 15), "Journée nationale de la Paix")
        ajout(dt.date(annee, 12, 25), "Noël")
        for d, nom, ap in fetes_musulmanes(annee):
            if nom != "Début du Ramadan":
                ajout(d, nom, ap)
    elif pays == "lu":
        ajout(dt.date(annee, 1, 1), "Nouvel An")
        ajout(lundi_paques, "Lundi de Pâques")
        ajout(dt.date(annee, 5, 1), "Fête du travail")
        ajout(dt.date(annee, 5, 9), "Journée de l'Europe")
        ajout(ascension, "Ascension")
        ajout(lundi_pentecote, "Lundi de Pentecôte")
        ajout(dt.date(annee, 6, 23), "Fête nationale")
        ajout(dt.date(annee, 8, 15), "Assomption")
        ajout(dt.date(annee, 11, 1), "Toussaint")
        ajout(dt.date(annee, 12, 25), "Noël")
        ajout(dt.date(annee, 12, 26), "Saint-Étienne")
    elif pays == "cv":
        ajout(dt.date(annee, 1, 1), "Jour de l'an")
        ajout(dt.date(annee, 1, 13), "Jour de la démocratie ?")
        ajout(dt.date(annee, 1, 20), "Jour des héros nationaux ?")
        ajout(carnaval, "Mardi gras (Carnaval) ?")
        ajout(vendredi_saint, "Vendredi saint")
        ajout(dt.date(annee, 5, 1), "Fête du travail")
        ajout(dt.date(annee, 7, 5), "Indépendance")
        ajout(dt.date(annee, 8, 15), "Assomption")
        ajout(dt.date(annee, 9, 12), "Fête nationale ?")
        ajout(dt.date(annee, 11, 1), "Toussaint")
        ajout(dt.date(annee, 12, 25), "Noël")
    elif pays == "fr":
        # France ; Audun-le-Tiche est en Moselle : droit local (Vendredi saint, Saint-Étienne) ajouté (univers 2, 11/10/2026)
        ajout(dt.date(annee, 1, 1), "Jour de l'an")
        ajout(vendredi_saint, "Vendredi saint (Alsace-Moselle)")
        ajout(lundi_paques, "Lundi de Pâques")
        ajout(dt.date(annee, 5, 1), "Fête du travail")
        ajout(dt.date(annee, 5, 8), "Victoire 1945")
        ajout(ascension, "Ascension")
        ajout(lundi_pentecote, "Lundi de Pentecôte (journée de solidarité possible)")
        ajout(dt.date(annee, 7, 14), "Fête nationale")
        ajout(dt.date(annee, 8, 15), "Assomption")
        ajout(dt.date(annee, 11, 1), "Toussaint")
        ajout(dt.date(annee, 11, 11), "Armistice 1918")
        ajout(dt.date(annee, 12, 25), "Noël")
        ajout(dt.date(annee, 12, 26), "Saint-Étienne (Alsace-Moselle)")
    else:
        sys.exit(f"Pays inconnu : {pays} (ci, lu, cv, fr)")
    return sorted(liste)


def ramadan(annee):
    deb = [d for d, nom, _ in fetes_musulmanes(annee) if nom == "Début du Ramadan"]
    fit = [d for d, nom, _ in fetes_musulmanes(annee) if nom.startswith("Aïd el-Fitr")]
    return (deb[0] if deb else None, (fit[0] - dt.timedelta(days=1)) if fit else None)


def lunes(du, au):
    """Pleines et nouvelles lunes (lunaison moyenne). Référence : nouvelle lune du 2000-01-06 18:14 UTC."""
    ref = dt.datetime(2000, 1, 6, 18, 14)
    lunaison = 29.530588853
    resultat = []
    n = int((dt.datetime.combine(du, dt.time()) - ref).days / lunaison) - 2
    while True:
        nouvelle = ref + dt.timedelta(days=n * lunaison)
        pleine = nouvelle + dt.timedelta(days=lunaison / 2)
        for quand, nom in ((nouvelle, "Nouvelle lune"), (pleine, "Pleine lune")):
            if du <= quand.date() <= au:
                resultat.append((quand, nom))
        if nouvelle.date() > au:
            break
        n += 1
    return sorted(resultat)


def date_arg(texte):
    return dt.date.fromisoformat(texte)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--annee", type=int, default=2040)
    ap.add_argument("--pays", default="lu,fr", help="ci, lu, cv, fr (séparés par des virgules ; univers 2 : lu,fr par défaut)")
    ap.add_argument("--du", type=date_arg)
    ap.add_argument("--au", type=date_arg)
    ap.add_argument("--jour", type=date_arg, help="fériés de ce jour")
    ap.add_argument("--lune", action="store_true", help="phases de la lune sur la période --du / --au")
    args = ap.parse_args()
    if args.lune:
        du = args.du or dt.date(args.annee, 1, 1)
        au = args.au or dt.date(args.annee, 12, 31)
        for quand, nom in lunes(du, au):
            print(f"{JOURS[quand.weekday()]} {quand:%d/%m/%Y %Hh%M UTC}  {nom} (± 14 h)")
        return 0
    pays_liste = [p.strip() for p in args.pays.split(",") if p.strip()]
    annees = {args.annee}
    if args.du:
        annees |= {args.du.year}
    if args.au:
        annees |= {args.au.year}
    if args.jour:
        annees = {args.jour.year}
    lignes = []
    for a in sorted(annees):
        for p in pays_liste:
            for d, nom, approx in fetes(a, p):
                lignes.append((d, p.upper(), nom, approx))
        deb, fin = ramadan(a)
        if deb and fin:
            lignes.append((deb, "CI", f"Ramadan : du {deb:%d/%m} au {fin:%d/%m} (≈ ; ± 1-2 jours)", True))
    lignes.sort()
    for d, p, nom, approx in lignes:
        if args.jour and d != args.jour:
            continue
        if args.du and d < args.du:
            continue
        if args.au and d > args.au:
            continue
        if not (args.jour or args.du or args.au) and d.year != args.annee:
            continue
        print(f"{JOURS[d.weekday()]} {d:%d/%m/%Y}  {p}  {'≈ ' if approx else ''}{nom}")
    if args.jour and not any(d == args.jour for d, *_ in lignes):
        print(f"Aucun férié le {args.jour:%d/%m/%Y} ({JOURS[args.jour.weekday()]}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
