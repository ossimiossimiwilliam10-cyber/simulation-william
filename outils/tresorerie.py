"""TRÉSORERIE DE LA SOCIÉTÉ (P41, validée par l'utilisateur le 29/10/2026) : ce que coûte SOLEIL B2B CI chaque mois, face à l'argent apporté.

Données : `etat/societe-engagements.csv` (sens ; poste ; montant_fcfa ; periodicite unique|mensuel ; debut ; fin ; statut ; source). Un montant
inconnu s'écrit vide et le poste « à confirmer » : l'outil le signale au lieu de l'inventer. Les charges sociales patronales (CNPS) sont une
estimation à confirmer (`TAUX_CNPS`). 1 € = 655,957 FCFA (parité fixe).

    python outils/tresorerie.py                      # situation au jour de l'horloge : apports, dépenses, charge mensuelle, mois d'autonomie
    python outils/tresorerie.py --au 2041-10-01      # à une autre date
Le directeur général virtuel cite ces chiffres dans ses rapports (pôle finance) ; aucun mouvement n'est inscrit ici à la place de William.
"""
import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
FICHIER = RACINE / "etat" / "societe-engagements.csv"
EUR = 655.957
TAUX_CNPS = 0.40  # coût employeur / salaire NET (25/08/2041, estimation du moteur) : net → brut ≈ × 1,28 (CNPS salarié 6,3 %, ITS),
# puis charges patronales ≈ 10 % du brut (retraite 7,7 % ; prestations familiales, maternité, accidents plafonnés à 70 000 FCFA ;
# impôt employeur, FDFP) : afrotools.com, cleiss.fr, africarrieres.com (2025-2026) ; avant : 0,16 (CNPS seule, appliquée au net)


def lire():
    return list(csv.DictReader(open(FICHIER, encoding="utf-8"), delimiter=";")) if FICHIER.exists() else []


def mois_entre(debut, fin):
    return max(0, (fin.year - debut.year) * 12 + fin.month - debut.month + (1 if fin.day >= debut.day else 0))


def situation(au):
    lignes = lire()
    apports = depenses = mensuel = 0.0
    inconnus, details = [], []
    for l in lignes:
        if l["statut"] == "annule":
            continue
        debut = dt.date.fromisoformat(l["debut"]) if l["debut"] else None
        montant = float(l["montant_fcfa"]) if l["montant_fcfa"] else None
        if montant is None:
            inconnus.append(l["poste"])
            continue
        if l["statut"] == "a_confirmer":
            inconnus.append(f"{l['poste']} (compté : " + f"{montant:,.0f}".replace(",", " ") + " FCFA)")
        charge = montant * (1 + TAUX_CNPS) if l["sens"] == "salaire" else montant
        if l["periodicite"] == "mensuel":
            signe = -1 if l["sens"] == "apport" else 1  # 25/08/2041 : un apport mensuel (ordre permanent de William) réduit la charge nette
            if debut and debut <= au:
                fin = dt.date.fromisoformat(l["fin"]) if l["fin"] else au
                n = mois_entre(debut, min(fin, au))
                if signe < 0:
                    apports += montant * n
                else:
                    depenses += charge * n
            if not l["fin"] or dt.date.fromisoformat(l["fin"]) >= au:
                mensuel += signe * charge
        elif debut and debut <= au:
            if l["sens"] == "apport":
                apports += montant
            else:
                depenses += montant
        details.append(l)
    reste = apports - depenses
    return {"apports": apports, "depenses": depenses, "reste": reste, "mensuel": mensuel,
            "autonomie": (reste / mensuel) if mensuel else None, "inconnus": inconnus}


def fcfa(x):
    return f"{x:,.0f}".replace(",", " ") + f" FCFA ({x / EUR:,.0f} €)".replace(",", " ")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--au")
    a = ap.parse_args()
    if a.au:
        au = dt.date.fromisoformat(a.au)
    else:
        sys.path.insert(0, str(RACINE / "outils"))
        import horloge
        au = horloge.lire()["instant"].date()
    s = situation(au)
    print(f"Trésorerie de SOLEIL B2B CI au {au:%d/%m/%Y}")
    print(f"  apports reçus : {fcfa(s['apports'])}")
    print(f"  dépenses engagées : {fcfa(s['depenses'])}")
    print(f"  reste : {fcfa(s['reste'])}")
    print(f"  charge mensuelle nette (coût employeur des salaires nets × {1 + TAUX_CNPS:.2f}, estimation, loyer, moins les apports mensuels) : {fcfa(s['mensuel'])}")
    if s["reste"] < 0:
        print(f"  autonomie : aucune (il manque {fcfa(-s['reste'])} pour couvrir ce qui est déjà engagé)")
    elif s["autonomie"] is not None:
        print(f"  autonomie au rythme actuel, sans recette : {s['autonomie']:.1f} mois")
    if s["inconnus"]:
        print("  montants à confirmer : " + " ; ".join(s["inconnus"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
