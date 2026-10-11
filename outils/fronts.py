"""FRONTS ET HORLOGES DE PROGRESSION (créé le 11/10/2026 ; inspiré des « horloges » des jeux de rôle Blades in the Dark et
Apocalypse World). Une menace, une occasion ou un projet qui avance par segments, avec ses PALIERS ÉCRITS D'AVANCE : aucune
conséquence n'est inventée au dernier moment (règles 7 et 14), et rien ne mûrit seulement « quand le moteur s'en souvient ».

    python outils/fronts.py creer --nom "Déclaration de revenus française" --type menace --segments 6 \\
        --paliers "2:rappel par courriel des impôts|4:avis de majoration de 10 %|6:taxation d'office" --visibilite cachee --echeance 2040-06-04
    python outils/fronts.py avancer H001 --de 1 --raison "William n'a rien fait avant l'échéance"
    python outils/fronts.py liste [--toutes]
    python outils/fronts.py voir H001
    python outils/fronts.py clore H001 --raison "déclaration faite le 12/07"

Fichier : `etat/fronts.csv` (id;nom;type;segments;rempli;visibilite;avance;paliers;echeance;liens;statut;historique).
type : menace | occasion | projet | personnage | monde ; visibilite : connue (William le sait) | cachee ; avance : evenement (à la
main, après un acte ou une échéance manquée) | temps (avance périodique TIRÉE : mode à faire valider par l'utilisateur, table
proposée dans memoire/propositions-2026-10-11.md, inactif tant qu'il ne l'a pas validé).
Un palier atteint est un ÉVÉNEMENT DÛ : `tour.py debut` le signale ; il se joue, se reporte (avec raison) ou s'annule (règle 14).
"""
import argparse
import datetime as dt
import sys

from commun import ETAT, ecrire_csv, lire_csv, maintenant_simule, utf8

FICHIER = ETAT / "fronts.csv"
COLONNES = ["id", "nom", "type", "segments", "rempli", "visibilite", "avance", "paliers", "echeance", "liens", "statut", "historique"]


def lire():
    return lire_csv(FICHIER)


def paliers(f):
    res = []
    for morceau in (f.get("paliers") or "").split("|"):
        if ":" in morceau:
            n, texte = morceau.split(":", 1)
            if n.strip().isdigit():
                res.append((int(n), texte.strip()))
    return sorted(res)


def paliers_atteints(f):
    rempli = int(f["rempli"] or 0)
    return [(n, t) for n, t in paliers(f) if n <= rempli]


def dus():
    """Fronts ouverts dont un palier est atteint (à jouer) ou dont l'échéance est passée."""
    t = maintenant_simule()
    jour = t.date().isoformat() if t else "2040-01-01"
    res = []
    for f in lire():
        if f["statut"] != "ouvert":
            continue
        atteints = paliers_atteints(f)
        if atteints:
            res.append(f"{f['id']} « {f['nom']} » ({f['visibilite']}) : {f['rempli']}/{f['segments']} -> palier {atteints[-1][0]} : "
                       f"{atteints[-1][1]}")
        if f.get("echeance") and f["echeance"] <= jour:
            res.append(f"{f['id']} « {f['nom']} » : échéance du {f['echeance']} passée ({f['rempli']}/{f['segments']})")
    return res


def horodatage():
    t = maintenant_simule()
    return f"{t:%d/%m/%Y %H:%M}" if t else dt.datetime.now().strftime("%d/%m/%Y")


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("creer")
    p.add_argument("--nom", required=True)
    p.add_argument("--type", required=True, choices=("menace", "occasion", "projet", "personnage", "monde"))
    p.add_argument("--segments", type=int, default=6)
    p.add_argument("--paliers", default="")
    p.add_argument("--visibilite", choices=("connue", "cachee"), default="cachee")
    p.add_argument("--avance", choices=("evenement", "temps"), default="evenement")
    p.add_argument("--echeance", default="")
    p.add_argument("--liens", default="")
    p = sp.add_parser("avancer")
    p.add_argument("id")
    p.add_argument("--de", type=int, default=1)
    p.add_argument("--raison", required=True)
    p = sp.add_parser("clore")
    p.add_argument("id")
    p.add_argument("--raison", required=True)
    p = sp.add_parser("liste")
    p.add_argument("--toutes", action="store_true")
    p = sp.add_parser("voir")
    p.add_argument("id")
    args = ap.parse_args()
    fronts = lire()
    if args.cmd == "creer":
        if ";" in args.nom + args.paliers + args.liens:
            sys.exit("Pas de « ; » dans les champs (séparateur du fichier).")
        nums = [int(f["id"][1:]) for f in fronts if f["id"][1:].isdigit()]
        f = {"id": f"H{(max(nums) + 1 if nums else 1):03d}", "nom": args.nom, "type": args.type, "segments": str(args.segments),
             "rempli": "0", "visibilite": args.visibilite, "avance": args.avance, "paliers": args.paliers, "echeance": args.echeance,
             "liens": args.liens, "statut": "ouvert", "historique": f"{horodatage()} créé"}
        fronts.append(f)
        ecrire_csv(FICHIER, fronts, COLONNES)
        print(f"Créé : {f['id']} « {f['nom']} » 0/{f['segments']}")
        return 0
    cible = next((f for f in fronts if f["id"] == getattr(args, "id", None)), None)
    if args.cmd in ("avancer", "clore", "voir") and not cible:
        sys.exit(f"Front inconnu : {args.id}")
    if args.cmd == "avancer":
        avant = int(cible["rempli"] or 0)
        cible["rempli"] = str(min(int(cible["segments"]), max(0, avant + args.de)))
        cible["historique"] += f" | {horodatage()} {avant}->{cible['rempli']} : {args.raison}"
        ecrire_csv(FICHIER, fronts, COLONNES)
        print(f"{cible['id']} « {cible['nom']} » : {avant} -> {cible['rempli']}/{cible['segments']}")
        for n, t in paliers(cible):
            if avant < n <= int(cible["rempli"]):
                print(f"  PALIER {n} ATTEINT : {t}  (à jouer, reporter avec raison ou annuler : règle 14)")
        return 0
    if args.cmd == "clore":
        cible["statut"] = "clos"
        cible["historique"] += f" | {horodatage()} clos : {args.raison}"
        ecrire_csv(FICHIER, fronts, COLONNES)
        print(f"{cible['id']} clos.")
        return 0
    if args.cmd == "voir":
        for c in COLONNES:
            print(f"{c:11s} {cible.get(c, '')}")
        return 0
    for f in fronts:
        if f["statut"] == "ouvert" or args.toutes:
            print(f"{f['id']} [{f['statut']}] « {f['nom']} » ({f['type']}, {f['visibilite']}) {f['rempli']}/{f['segments']}"
                  + (f" ; échéance {f['echeance']}" if f.get("echeance") else ""))
    for d in dus():
        print("DÛ :", d)
    return 0


if __name__ == "__main__":
    sys.exit(main())
