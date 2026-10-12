"""Agenda structuré de la simulation (règle 14 de CLAUDE.md : « rien ne disparaît »). Fichier : `etat/agenda.csv`.

Colonnes (séparateur « ; ») : id;date;heure;lieu;qui;quoi;statut;connu;note
- date AAAA-MM-JJ, heure HH:MM dans le fuseau `lieu` (abidjan, lisbonne, luxembourg, mindelo, casablanca, douala, paris) ;
- statut : prevu | fait | reporte | annule | latent (échéance sans heure ferme) ;
- connu : oui (William le sait) | non (pré-tiré ou caché, jamais montré au joueur) ;
- note : raison d'un report, source, résultat.

    python outils/agenda.py dus                         # ce qui tombe entre l'horloge et +24 h (à lire AVANT chaque tour)
    python outils/agenda.py dus --jusqua "2040-08-10 12:00"
    python outils/agenda.py retards                     # prévu mais échu : à jouer, reporter (avec raison) ou annuler
    python outils/agenda.py liste --jours 14 [--connus]
    python outils/agenda.py ajouter --date 2040-08-12 --heure 10:00 --lieu abidjan --qui "Aïcha" --quoi "Rapport" [--connu non]
    python outils/agenda.py clore A012 --statut fait --note "joué le 10/08 à 10h02"
    python outils/agenda.py reporter A012 --a "2040-08-14 09:00" --raison "Me Kouamé hospitalisé"
    python outils/agenda.py verifier                    # contrôle du fichier (intégré à controle_coherence.py)
Les heures s'affichent dans le fuseau de l'horloge (etat/horloge.txt) ; `--fuseau` pour un autre lieu.
"""
import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fuseaux  # noqa: E402
import horloge  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
FICHIER = RACINE / "etat" / "agenda.csv"
COLONNES = ["id", "date", "heure", "lieu", "qui", "quoi", "statut", "connu", "note"]
STATUTS = {"prevu", "fait", "reporte", "annule", "latent"}


def lire():
    if not FICHIER.exists():
        return []
    with FICHIER.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def ecrire(lignes):
    with FICHIER.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLONNES, delimiter=";", lineterminator="\r\n")
        w.writeheader()
        w.writerows(lignes)


def instant(ligne):
    h = ligne["heure"] or "12:00"
    return fuseaux.analyser_instant(ligne["date"], h, ligne["lieu"])


def prochain_id(lignes):
    nums = [int(l["id"][1:]) for l in lignes if l["id"][:1] == "A" and l["id"][1:].isdigit()]
    return f"A{(max(nums) + 1 if nums else 1):03d}"


def afficher(l, fuseau):
    loc = fuseaux.convertir(instant(l), fuseau)
    heure_txt = f"{loc:%H:%M}" if l["heure"] else "(sans heure)"
    cache = "  [NON CONNU DE WILLIAM : ne pas montrer]" if l["connu"] == "non" else ""
    note = f"  — {l['note']}" if l["note"] else ""
    return f"{l['id']} {loc:%a %d/%m} {heure_txt} ({fuseau}) | {l['qui']} : {l['quoi']} [{l['statut']}]{cache}{note}"


def parse_instant(texte, fuseau):
    d, h = texte.split()
    return fuseaux.analyser_instant(d, h, fuseau)


def cmd_dus(args):
    h = horloge.lire()
    fuseau = fuseaux.zone(args.fuseau) if args.fuseau else h["fuseau"]
    debut = parse_instant(args.depuis, fuseau) if args.depuis else h["instant"]
    fin = parse_instant(args.jusqua, fuseau) if args.jusqua else debut + dt.timedelta(hours=24)
    print(f"Échéances du {debut:%a %d/%m %H:%M} au {fin:%a %d/%m %H:%M} ({fuseau}) :")
    n = 0
    for l in sorted(lire(), key=instant):
        if l["statut"] in ("prevu", "latent") and debut <= instant(l) <= fin:
            print("  " + afficher(l, fuseau))
            n += 1
    print(f"  {n} échéance(s)." if n else "  Rien de prévu sur cette période.")
    retards = [l for l in lire() if l["statut"] == "prevu" and instant(l) < debut]
    if retards:
        print(f"  ATTENTION : {len(retards)} échéance(s) échue(s) non closes (commande « retards »).")
    return 0


def cmd_retards(args):
    h = horloge.lire()
    fuseau = fuseaux.zone(args.fuseau) if args.fuseau else h["fuseau"]
    retards = [l for l in sorted(lire(), key=instant) if l["statut"] == "prevu" and instant(l) < h["instant"]]
    print(f"Échéances échues et non closes à {h['instant']:%d/%m %H:%M} ({h['fuseau']}) : {len(retards)}")
    for l in retards:
        print("  " + afficher(l, fuseau))
    return 1 if retards and args.strict else 0


def cmd_liste(args):
    h = horloge.lire()
    fuseau = fuseaux.zone(args.fuseau) if args.fuseau else h["fuseau"]
    fin = h["instant"] + dt.timedelta(days=args.jours)
    for l in sorted(lire(), key=instant):
        if l["statut"] in ("prevu", "latent") and h["instant"] <= instant(l) <= fin:
            if args.connus and l["connu"] == "non":
                continue
            print(afficher(l, fuseau))
    return 0


def cmd_ajouter(args):
    lignes = lire()
    fuseaux.analyser_instant(args.date, args.heure or "12:00", args.lieu)  # validation
    if args.statut not in STATUTS:
        sys.exit(f"Statut inconnu : {args.statut}")
    nouvelle = {"id": prochain_id(lignes), "date": args.date, "heure": args.heure or "", "lieu": fuseaux.zone(args.lieu),
                "qui": args.qui, "quoi": args.quoi, "statut": args.statut, "connu": args.connu, "note": args.note or ""}
    lignes.append(nouvelle)
    ecrire(lignes)
    print("Ajouté :", afficher(nouvelle, horloge.lire()["fuseau"]))
    return 0


def trouver(lignes, ident):
    for l in lignes:
        if l["id"] == ident:
            return l
    sys.exit(f"Identifiant inconnu : {ident}")


def cmd_clore(args):
    lignes = lire()
    l = trouver(lignes, args.id)
    if args.statut not in ("fait", "annule"):
        sys.exit("clore : statut fait ou annule (pour un report : commande « reporter »)")
    l["statut"] = args.statut
    if args.note:
        l["note"] = (l["note"] + " | " if l["note"] else "") + args.note
    ecrire(lignes)
    print("Clos :", afficher(l, horloge.lire()["fuseau"]))
    return 0


def cmd_reporter(args):
    if not args.raison:
        sys.exit("reporter : --raison obligatoire (règle 14 : un report a toujours une raison)")
    lignes = lire()
    l = trouver(lignes, args.id)
    d, h = args.a.split()
    fuseaux.analyser_instant(d, h, l["lieu"])
    ancien = f"{l['date']} {l['heure'] or '--:--'}"
    l["date"], l["heure"] = d, h
    l["statut"] = "prevu"
    l["note"] = (l["note"] + " | " if l["note"] else "") + f"reporté de {ancien} : {args.raison}"
    ecrire(lignes)
    print("Reporté :", afficher(l, horloge.lire()["fuseau"]))
    return 0


def verifier():
    erreurs, vus = [], set()
    for n, l in enumerate(lire(), 2):
        if l["id"] in vus:
            erreurs.append(f"agenda.csv:{n} identifiant en double {l['id']}")
        vus.add(l["id"])
        if l["statut"] not in STATUTS:
            erreurs.append(f"agenda.csv:{n} statut inconnu {l['statut']}")
        if l["connu"] not in ("oui", "non"):
            erreurs.append(f"agenda.csv:{n} « connu » doit valoir oui ou non")
        try:
            instant(l)
        except SystemExit as e:
            erreurs.append(f"agenda.csv:{n} {e}")
    return erreurs


def cmd_verifier(args):
    erreurs = verifier()
    for e in erreurs:
        print("ERREUR", e)
    print("agenda.csv :", "des erreurs" if erreurs else "conforme", f"({len(lire())} lignes)")
    return 1 if erreurs else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    for nom, f in (("dus", cmd_dus), ("retards", cmd_retards), ("liste", cmd_liste)):
        p = sp.add_parser(nom)
        p.add_argument("--fuseau")
        p.set_defaults(f=f)
        if nom == "dus":
            p.add_argument("--depuis")
            p.add_argument("--jusqua")
        if nom == "retards":
            p.add_argument("--strict", action="store_true")
        if nom == "liste":
            p.add_argument("--jours", type=int, default=14)
            p.add_argument("--connus", action="store_true", help="ne montre pas les lignes « connu = non »")
    p = sp.add_parser("ajouter")
    p.add_argument("--date", required=True)
    p.add_argument("--heure")
    p.add_argument("--lieu", required=True)
    p.add_argument("--qui", required=True)
    p.add_argument("--quoi", required=True)
    p.add_argument("--statut", default="prevu")
    p.add_argument("--connu", default="oui")
    p.add_argument("--note")
    p.set_defaults(f=cmd_ajouter)
    p = sp.add_parser("clore")
    p.add_argument("id")
    p.add_argument("--statut", default="fait")
    p.add_argument("--note")
    p.set_defaults(f=cmd_clore)
    p = sp.add_parser("reporter")
    p.add_argument("id")
    p.add_argument("--a", required=True, metavar="AAAA-MM-JJ HH:MM")
    p.add_argument("--raison")
    p.set_defaults(f=cmd_reporter)
    p = sp.add_parser("verifier")
    p.set_defaults(f=cmd_verifier)
    args = ap.parse_args()
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())
