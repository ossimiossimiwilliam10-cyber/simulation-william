"""PRIX DE RÉFÉRENCE projetés en 2040 (créé le 11/10/2026). Règle 1 de CLAUDE.md : prix actuels vérifiés, projetés en 2040 à
+30 à 40 %. Ici le coefficient est FIXE et écrit (1,35 par défaut, modifiable ligne par ligne dans la colonne `coef` par
l'utilisateur) : le même café ne coûte plus +30 % un jour et +40 % le lendemain, et la même nuit d'hôtel ne coûte plus 188 € dans
une session et 189 € dans une autre (incident de l'univers 1).

    python outils/prix.py cherche "coupe"                 # prix 2026 sourcé et prix 2040 projeté
    python outils/prix.py cherche carburant --pays lu
    python outils/prix.py tirer PX010                     # un montant réaliste dans la fourchette (jet consigné, jamais rejoué)
    python outils/prix.py ajouter --article "…" --lieu "…" --pays fr --categorie service --prix 12.5 --unite € --source "…"

Fichier : `donnees/prix.csv`. Le tirage dans une fourchette (± 12 % autour du prix projeté, loi triangulaire) est un jet sur un
PRIX, pas sur une réaction : il est libre et consigné (memoire/tirages-aleas.md et memoire/tirages.jsonl).
"""
import argparse
import datetime as dt
import random
import sys

from commun import DONNEES, OUTILS, ecrire_csv, lire_csv, sans_accents, utf8

sys.path.insert(0, str(OUTILS))
FICHIER = DONNEES / "prix.csv"
COLONNES = ["id", "article", "lieu", "pays", "categorie", "prix_2026", "unite", "source", "date_releve", "fiabilite", "coef", "note"]
COEF_DEFAUT = 1.35
ECART = 0.12


def lire():
    return lire_csv(FICHIER)


def coef(l):
    try:
        return float(l["coef"]) if l.get("coef") else COEF_DEFAUT
    except ValueError:
        return COEF_DEFAUT


def prix_2040(l):
    return float(l["prix_2026"]) * coef(l)


def fmt(x):
    return f"{x:,.2f}".replace(",", " ").replace(".", ",")


def chercher(mots, pays=None):
    cles = [sans_accents(m.lower()) for m in mots.split()]
    return [l for l in lire() if (not pays or l["pays"] in pays.split(","))
            and all(c in sans_accents(" ".join(l.values()).lower()) for c in cles)]


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("cherche")
    p.add_argument("mots")
    p.add_argument("--pays")
    p = sp.add_parser("tirer")
    p.add_argument("id")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("ajouter")
    for a in ("--article", "--lieu", "--pays", "--categorie", "--unite", "--source"):
        p.add_argument(a, required=True)
    p.add_argument("--prix", type=float, required=True)
    p.add_argument("--fiabilite", default="secondaire")
    p.add_argument("--note", default="")
    args = ap.parse_args()
    if args.cmd == "cherche":
        res = chercher(args.mots, args.pays)
        for l in res:
            print(f"{l['id']} {l['article']} ({l['lieu']}) : {fmt(float(l['prix_2026']))} {l['unite']} en 2026 "
                  f"-> {fmt(prix_2040(l))} {l['unite']} en 2040 (× {coef(l):g}) ; {l['source']}" + (f" ; {l['note']}" if l['note'] else ""))
        print(f"({len(res)} prix ; sinon : recherche web, puis « prix.py ajouter »)")
        return 0
    if args.cmd == "tirer":
        l = next((x for x in lire() if x["id"] == args.id), None)
        if not l:
            sys.exit(f"Prix inconnu : {args.id}")
        centre = prix_2040(l)
        montant = random.SystemRandom().triangular(centre * (1 - ECART), centre * (1 + ECART), centre)
        montant = round(montant, 2)
        ligne = (f"- Prix tiré « {l['article']} ({l['lieu']}) » : centre {fmt(centre)} {l['unite']} (2026 × {coef(l):g}), "
                 f"fourchette ± {int(ECART * 100)} % → **{fmt(montant)} {l['unite']}**")
        print(ligne)
        if not args.simule:
            import jet
            jet.consigner(ligne)
            jet.consigner_json({"mode": "prix", "libelle": l["article"], "issue": f"{montant:.2f}", "proba": None,
                                "distribution": {"centre": round(centre, 2), "ecart": ECART}, "ref": l["id"]})
        return 0
    if args.cmd == "ajouter":
        lignes = lire()
        nums = [int(x["id"][2:]) for x in lignes if x["id"][2:].isdigit()]
        n = {"id": f"PX{(max(nums) + 1 if nums else 1):03d}", "article": args.article, "lieu": args.lieu, "pays": args.pays,
             "categorie": args.categorie, "prix_2026": f"{args.prix:g}", "unite": args.unite, "source": args.source,
             "date_releve": dt.date.today().isoformat(), "fiabilite": args.fiabilite, "coef": "", "note": args.note}
        if any(";" in str(v) for v in n.values()):
            sys.exit("Pas de « ; » dans les champs (séparateur du fichier).")
        lignes.append(n)
        ecrire_csv(FICHIER, lignes, COLONNES)
        print(f"Ajouté : {n['id']} {n['article']} -> {fmt(prix_2040(n))} {n['unite']} en 2040")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
