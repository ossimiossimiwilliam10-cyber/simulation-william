"""DEVIS SOLAIRE B2B (P48, validée par l'utilisateur le 29/10/2026) : prix d'une installation en toiture à Abidjan, production,
économies du client, retour sur investissement et marge de SOLEIL B2B CI. Calcul déterministe à partir de `donnees/solaire-abidjan.csv`
(valeurs 2026 projetées en 2041 par le coefficient fixe × 1,35, comme prix.py). Toutes les valeurs sont des estimations à confirmer.

    python outils/devis_solaire.py --kwc 100                     # devis type
    python outils/devis_solaire.py --kwc 100 --remise 0.10       # avec une remise de 10 % sur le prix de vente
    python outils/devis_solaire.py --kwc 100 --prix-concurrent 60000000   # comparaison avec le devis d'un concurrent
"""
import argparse
import csv
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
COEF = 1.35
EUR = 655.957


def donnees():
    return {l["cle"]: float(l["valeur_2026"]) for l in csv.DictReader(open(RACINE / "donnees" / "solaire-abidjan.csv", encoding="utf-8"), delimiter=";")}


def devis(kwc, remise=0.0):
    d = donnees()
    cout = kwc * d["prix_kwc_installe"] * COEF
    prix = cout / (1 - d["marge_cible"]) * (1 - remise)
    prod = kwc * d["production_kwh_par_kwc"]
    eco = prod * d["tarif_cie_industriel"] * COEF
    return {"kwc": kwc, "cout": cout, "prix": prix, "marge": prix - cout, "taux_marge": (prix - cout) / prix,
            "production": prod, "economies": eco, "retour_ans": prix / eco, "maintenance": prix * d["maintenance_annuelle"]}


def f(x):
    return f"{x:,.0f}".replace(",", " ") + f" FCFA ({x / EUR:,.0f} €)".replace(",", " ")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kwc", type=float, required=True)
    ap.add_argument("--remise", type=float, default=0.0)
    ap.add_argument("--prix-concurrent", type=float)
    a = ap.parse_args()
    r = devis(a.kwc, a.remise)
    print(f"Devis type pour {a.kwc:g} kWc (estimations 2041) :")
    print(f"  coût d'installation : {f(r['cout'])}")
    print(f"  prix de vente{' après remise' if a.remise else ''} : {f(r['prix'])} ; marge : {f(r['marge'])} ({r['taux_marge']:.0%})")
    print(f"  production : {r['production']:,.0f} kWh par an ; économies du client : {f(r['economies'])} par an".replace(",", " "))
    print(f"  retour sur investissement du client : {r['retour_ans']:.1f} ans ; maintenance : {f(r['maintenance'])} par an")
    if a.prix_concurrent:
        ecart = (a.prix_concurrent - r["prix"]) / r["prix"]
        print(f"  devis concurrent : {f(a.prix_concurrent)} ({ecart:+.0%} par rapport au nôtre) ; il est sous notre coût : {'oui' if a.prix_concurrent < r['cout'] else 'non'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
