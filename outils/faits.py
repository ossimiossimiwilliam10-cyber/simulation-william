"""Base des FAITS VÉRIFIÉS (créée le 11/10/2026) : droit, fiscalité, calendriers, transports, climat, démographie… avec leur
source, leur date de vérification, leur fiabilité et leur projection en 2040. Partagée par tous les agents : un fait vérifié
par Claude n'est pas recherché de nouveau (avec un autre chiffre) par Gemini.

    python outils/faits.py cherche "taxe foncière"          # AVANT une recherche web : le fait est-il déjà connu ?
    python outils/faits.py cherche transport --pays fr-lu
    python outils/faits.py voir F013
    python outils/faits.py ajouter --pays lu --domaine sante --enonce "…" --source "URL ou titre" [--valeur … --fiabilite officielle
                                   --projection "…" --jusqua AAAA-MM-JJ]
    python outils/faits.py perimes                          # faits dont la validité est dépassée à l'horloge

Fichier : `donnees/faits.csv`. Fiabilité : officielle (texte ou statistique publique), secondaire (presse, guide), estimation.
Les leçons d'erreurs du moteur restent dans `memoire/pieges-connus.md` ; les FAITS vont ici (règle 1 : recherche web, puis consignation).
"""
import argparse
import datetime as dt
import sys

from commun import DONNEES, ecrire_csv, lire_csv, maintenant_simule, sans_accents, utf8

FICHIER = DONNEES / "faits.csv"
COLONNES = ["id", "pays", "domaine", "enonce", "valeur", "source", "date_verif", "fiabilite", "projection_2040", "valable_jusqua"]


def lire():
    return lire_csv(FICHIER)


def chercher(mots, pays=None):
    cles = [sans_accents(m.lower()) for m in mots.split()]
    res = []
    for f in lire():
        if pays and f["pays"] not in pays.split(","):
            continue
        texte = sans_accents(" ".join(f.values()).lower())
        if all(c in texte for c in cles):
            res.append(f)
    return res


def afficher(f, complet=False):
    print(f"{f['id']} [{f['pays']}/{f['domaine']}] {f['enonce']}")
    if complet:
        for c in ("valeur", "source", "date_verif", "fiabilite", "projection_2040", "valable_jusqua"):
            if f.get(c):
                print(f"    {c} : {f[c]}")
    else:
        print(f"    source : {f['source']} (vérifié le {f['date_verif']}, {f['fiabilite']})"
              + (f" ; 2040 : {f['projection_2040']}" if f.get("projection_2040") else ""))


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("cherche")
    p.add_argument("mots")
    p.add_argument("--pays")
    p = sp.add_parser("voir")
    p.add_argument("id")
    p = sp.add_parser("ajouter")
    for a in ("--pays", "--domaine", "--enonce", "--source"):
        p.add_argument(a, required=True)
    p.add_argument("--valeur", default="")
    p.add_argument("--fiabilite", default="secondaire", choices=("officielle", "secondaire", "estimation"))
    p.add_argument("--projection", default="")
    p.add_argument("--jusqua", default="")
    sp.add_parser("perimes")
    args = ap.parse_args()
    if args.cmd == "cherche":
        res = chercher(args.mots, args.pays)
        for f in res:
            afficher(f)
        print(f"({len(res)} fait(s) ; sinon : recherche web, puis « faits.py ajouter »)")
        return 0
    if args.cmd == "voir":
        f = next((x for x in lire() if x["id"] == args.id), None)
        if not f:
            sys.exit(f"Fait inconnu : {args.id}")
        afficher(f, complet=True)
        return 0
    if args.cmd == "ajouter":
        if ";" in "".join((args.enonce, args.source, args.valeur, args.projection)):
            sys.exit("Pas de « ; » dans les champs (séparateur du fichier) : utiliser « · » ou une virgule.")
        faits = lire()
        nums = [int(f["id"][1:]) for f in faits if f["id"][1:].isdigit()]
        nouveau = {"id": f"F{(max(nums) + 1 if nums else 1):03d}", "pays": args.pays, "domaine": args.domaine,
                   "enonce": args.enonce, "valeur": args.valeur, "source": args.source,
                   "date_verif": dt.date.today().isoformat(), "fiabilite": args.fiabilite,
                   "projection_2040": args.projection, "valable_jusqua": args.jusqua}
        faits.append(nouveau)
        ecrire_csv(FICHIER, faits, COLONNES)
        print("Ajouté :")
        afficher(nouveau, complet=True)
        return 0
    if args.cmd == "perimes":
        t = maintenant_simule()
        jour = t.date().isoformat() if t else "2040-01-01"
        res = [f for f in lire() if f.get("valable_jusqua") and f["valable_jusqua"] < jour]
        for f in res:
            afficher(f)
        print(f"({len(res)} fait(s) périmé(s) à l'horloge : à revérifier avant de s'en servir)")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
