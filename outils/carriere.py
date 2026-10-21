#!/usr/bin/env python3
"""carriere.py -- Calcul automatique du salaire, de la repartition et du patrimoine
de William (maquette integrale solo, celibataire sans enfant, Classe U, enseignant Luxembourg).

Commandes :
    python outils/carriere.py salaire --age 35 [--hsup 3]
    python outils/carriere.py patrimoine --age 35 [--hsup 3]
    python outils/carriere.py grille [--hsup 3]
    python outils/carriere.py repartition --net 8980
    python outils/carriere.py soldes --age 35

Tous les montants sont en euros constants 2026 sauf indication contraire.
"""

import argparse
import sys
import os

# --- DONNEES DE REFERENCE (Maquette Solo sans enfant, Classe U) ---

# Grille indicaire par age (age_debut, age_fin, groupe, points, note)
GRILLE_INDICIAIRE = [
    (26, 27, "Stage A1",          340, "Stage, 0 h. sup."),
    (28, 29, "Titulaire Gr. 12",  410, "Titulaire"),
    (30, 31, "Gr. 12/13",         445, "Sweet spot entrepreneuriat"),
    (32, 33, "Gr. 13",            480, "Incubation projet"),
    (34, 35, "Gr. 13",            515, ""),
    (36, 37, "Gr. 14",            540, "Lean FIRE possible"),
    (38, 39, "Gr. 14",            560, "Bascule temps partiel possible"),
    (40, 41, "Gr. 14 allonge",    580, ""),
    (42, 44, "Gr. 14 allonge",    600, ""),
    (45, 47, "Plafond A1",        625, "Decharge 1 lecon (21)"),
    (48, 49, "Plafond A1",        625, "Fin amortissement pret"),
    (50, 54, "Plafond A1",        625, "Decharge 2 lecons (20)"),
    (55, 59, "Plafond A1",        625, "Decharge 4 lecons (18)"),
    (60, 65, "Plafond A1",        625, "Fin de carriere"),
]

# Revenus NET lisses (avec 3 lecons sup. de maths des 28 ans, en euros constants 2026)
REVENU_NET_AVEC_HSUP = {
    (26, 27): 6140,   # 0 h sup pendant le stage
    (28, 29): 7580,
    (30, 31): 8060,
    (32, 33): 8520,
    (34, 35): 8980,
    (36, 37): 9320,
    (38, 39): 9560,
    (40, 41): 9830,
    (42, 44): 10100,
    (45, 47): 10440,
    (48, 49): 10370,
    (50, 65): 10370,
}

# Decharges d'age officielles (F078)
DECHARGES_AGE = {
    45: 1,
    50: 2,
    55: 4,
}

# Tache normale de base
TACHE_NORMALE_BASE = 22

# Parametres financiers
NET_PAR_LECON_SUP = 117       # euros nets/mois par lecon supplementaire
BRUT_PAR_LECON_SUP = 233.33   # euros bruts/mois par lecon supplementaire

# Parametres de flux
SOCLE_VITAL = 2000            # euros/mois (fixe)
BUDGET_VACANCES = 833         # euros/mois (plafonne a 10 000 euros/an)
PART_SECURITE_EXCEDENT = 0.10 # 10% de l'excedent apres socle vital

# Jalons exacts de patrimoine cumule (maquette utilisateur 2026)
JALONS_PATRIMOINE = {
    28: {"total": 82940,   "etf": 73200,   "securite": 9740},
    30: {"total": 209990,  "etf": 186700,  "securite": 23290},
    32: {"total": 361380,  "etf": 322800,  "securite": 38580},
    34: {"total": 539050,  "etf": 483300,  "securite": 55750},
    36: {"total": 745630,  "etf": 670380,  "securite": 75250},
    40: {"total": 1245980, "etf": 1125000, "securite": 120980},
    45: {"total": 2057190, "etf": 1868000, "securite": 189190},
    50: {"total": 3113690, "etf": 2845000, "securite": 268690},
    55: {"total": 4454110, "etf": 4098000, "securite": 356110},
    60: {"total": 6159770, "etf": 5705000, "securite": 454770},
    65: {"total": 8333040, "etf": 7861818, "securite": 471220},
}


def get_tache_normale(age):
    """Retourne la tache normale (lecons) selon l'age, apres decharges."""
    if age >= 55:
        return 18
    elif age >= 50:
        return 20
    elif age >= 45:
        return 21
    return 22


def get_grille_info(age):
    """Retourne les infos de la grille indiciaire pour un age donne."""
    for (a_min, a_max, groupe, points, note) in GRILLE_INDICIAIRE:
        if a_min <= age <= a_max:
            return {"groupe": groupe, "points": points, "note": note}
    return {"groupe": "?", "points": 0, "note": ""}


def calcul_hsup_net(nb_lecons):
    """Calcule le gain net mensuel pour un nombre de lecons supplementaires."""
    return round(nb_lecons * NET_PAR_LECON_SUP)


def calcul_salaire(age, hsup_demandees=3):
    """Calcule le salaire net lisse total pour un age donne."""
    is_stage = age < 28
    grille = get_grille_info(age)

    # Recherche du net lisse standard (avec 3 lecons sup, ou 0 si stage)
    net_reference = 6140
    for (a_min, a_max), revenu in REVENU_NET_AVEC_HSUP.items():
        if a_min <= age <= a_max:
            net_reference = revenu
            break

    if is_stage:
        hsup_reelles = 0
        gain_hsup = 0
        revenu_base = net_reference
        net_total = net_reference
    else:
        # Tache normale et heures sup selon la presence de decharges
        tache = get_tache_normale(age)
        lecons_totales = TACHE_NORMALE_BASE + hsup_demandees  # 25 lecons
        hsup_reelles = max(0, lecons_totales - tache)
        gain_hsup = calcul_hsup_net(hsup_reelles)
        
        # Le net_reference du tableau inclut 3 lecons sup (+350)
        revenu_base = net_reference - calcul_hsup_net(3)
        net_total = revenu_base + gain_hsup

    return {
        "age": age,
        "groupe": grille["groupe"],
        "points": grille["points"],
        "note": grille["note"],
        "revenu_base": revenu_base,
        "tache_normale": get_tache_normale(age),
        "lecons_donnees": TACHE_NORMALE_BASE + (0 if is_stage else hsup_demandees),
        "hsup": hsup_reelles,
        "gain_hsup": gain_hsup,
        "total": net_total,
    }


def calcul_repartition(net_total):
    """Calcule la repartition selon la formule exacte validee par l'utilisateur :
    - 2 000 euros/mois (Socle Vital fixe)
    - 10 % de l'excedent net apres socle vital vers la Securite Liquide
    - Vacances plafonnees a 833 euros/mois (10 000 euros/an)
    - Le solde restant vers l'ETF Monde (90 % de l'excedent net moins vacances)
    """
    socle = min(net_total, SOCLE_VITAL)
    excedent = max(0, net_total - socle)
    
    securite = round(excedent * PART_SECURITE_EXCEDENT)
    vacances = min(max(0, excedent - securite), BUDGET_VACANCES)
    etf = max(0, net_total - socle - vacances - securite)

    return {
        "socle_vital": socle,
        "excedent": excedent,
        "vacances": vacances,
        "securite_total": securite,
        "etf_total": etf,
        "total_epargne": securite + etf,
    }


def calcul_patrimoine(age_cible, hsup_demandees=3):
    """Calcule ou interpole le patrimoine projete pour un age donne d'apres les jalons."""
    jalons_tries = sorted(JALONS_PATRIMOINE.items())
    
    # Si l'age exact est un jalon
    if age_cible in JALONS_PATRIMOINE:
        j = JALONS_PATRIMOINE[age_cible]
        return {
            "age": age_cible,
            "etf": j["etf"],
            "securite": j["securite"],
            "patrimoine_total": j["total"],
        }
    
    # Avant le premier jalon
    if age_cible < jalons_tries[0][0]:
        ratio = max(0, (age_cible - 26) / (jalons_tries[0][0] - 26))
        j = jalons_tries[0][1]
        return {
            "age": age_cible,
            "etf": round(j["etf"] * ratio),
            "securite": round(j["securite"] * ratio),
            "patrimoine_total": round(j["total"] * ratio),
        }
        
    # Interpolation lineaire entre deux jalons
    for i in range(len(jalons_tries) - 1):
        age1, j1 = jalons_tries[i]
        age2, j2 = jalons_tries[i+1]
        if age1 <= age_cible <= age2:
            fraction = (age_cible - age1) / (age2 - age1)
            etf = round(j1["etf"] + fraction * (j2["etf"] - j1["etf"]))
            sec = round(j1["securite"] + fraction * (j2["securite"] - j1["securite"]))
            tot = round(j1["total"] + fraction * (j2["total"] - j1["total"]))
            return {
                "age": age_cible,
                "etf": etf,
                "securite": sec,
                "patrimoine_total": tot,
            }
            
    # Au-dela de 65 ans
    j = jalons_tries[-1][1]
    return {
        "age": age_cible,
        "etf": j["etf"],
        "securite": j["securite"],
        "patrimoine_total": j["total"],
    }


def cmd_salaire(args):
    """Affiche le salaire net pour un age donne."""
    sal = calcul_salaire(args.age, args.hsup)
    print(f"=== Salaire de William a {args.age} ans (Solo, Classe U) ===")
    print(f"  Groupe          : {sal['groupe']} ({sal['points']} points)")
    if sal["note"]:
        print(f"  Note            : {sal['note']}")
    print(f"  Tache normale   : {sal['tache_normale']} lecons")
    print(f"  Lecons donnees  : {sal['lecons_donnees']} lecons")
    print(f"  H. sup. payees  : {sal['hsup']} lecons")
    print(f"  Revenu de base  : {sal['revenu_base']:,.0f} euros/mois")
    print(f"  Gain h. sup.    : +{sal['gain_hsup']:,.0f} euros/mois")
    print(f"  TOTAL NET LISSE : {sal['total']:,.0f} euros/mois")


def cmd_repartition(args):
    """Affiche la repartition du surplus."""
    rep = calcul_repartition(args.net)
    print(f"=== Repartition du surplus (net {args.net:,.0f} euros) ===")
    print(f"  Socle vital     : {rep['socle_vital']:,.0f} euros/mois")
    print(f"  Vacances        : {rep['vacances']:,.0f} euros/mois (plafond 10 000 euros/an)")
    print(f"  Securite (10 %) : +{rep['securite_total']:,.0f} euros/mois")
    print(f"  ETF Monde       : +{rep['etf_total']:,.0f} euros/mois")
    print(f"  ---")
    print(f"  TOTAL EPARGNE   : +{rep['total_epargne']:,.0f} euros/mois")
    total_somme = rep['socle_vital'] + rep['vacances'] + rep['total_epargne']
    print(f"  VERIFICATION    : {total_somme:,.0f} euros/mois (equilibre : {total_somme == round(args.net)})")


def cmd_patrimoine(args):
    """Affiche le patrimoine projete."""
    pat = calcul_patrimoine(args.age, args.hsup)
    print(f"=== Patrimoine projete a {args.age} ans (Solo, avec 3 h. sup.) ===")
    print(f"  ETF Monde       : {pat['etf']:,.0f} euros")
    print(f"  Securite        : {pat['securite']:,.0f} euros")
    print(f"  Patrimoine total: {pat['patrimoine_total']:,.0f} euros (hors maison)")


def cmd_grille(args):
    """Affiche le tableau complet de carriere."""
    print(f"=== Grille de carriere Solo (avec {args.hsup} h. sup. des 28 ans) ===")
    print(f"{'Age':<8} {'Groupe':<20} {'Pts':<5} {'Net Lisse':<11} {'Socle':<8} {'Vacances':<10} "
          f"{'Securite':<10} {'ETF Monde':<12} {'Patrimoine':<12}")
    print("-" * 105)

    ages_cles = [27, 29, 31, 33, 35, 39, 44, 49, 54, 59, 65]
    for age in ages_cles:
        sal = calcul_salaire(age, args.hsup)
        rep = calcul_repartition(sal["total"])
        pat = calcul_patrimoine(age, args.hsup)
        print(f"{age:<8} {sal['groupe']:<20} {sal['points']:<5} {sal['total']:>9,.0f} € "
              f"{rep['socle_vital']:>6,.0f} € {rep['vacances']:>8,.0f} € {rep['securite_total']:>8,.0f} € "
              f"{rep['etf_total']:>10,.0f} € {pat['patrimoine_total']:>10,.0f} €")


def cmd_soldes(args):
    """Calcule les soldes de depart suggeres pour un age donne."""
    pat = calcul_patrimoine(args.age, args.hsup)
    sal = calcul_salaire(args.age, args.hsup)
    rep = calcul_repartition(sal["total"])
    print(f"=== Soldes de depart suggeres a {args.age} ans (Solo) ===")
    print(f"  Patrimoine total (hors maison) : {pat['patrimoine_total']:,.0f} euros")
    print(f"  Dont ETF Monde                 : {pat['etf']:,.0f} euros")
    print(f"  Dont Securite/Epargne          : {pat['securite']:,.0f} euros")
    print(f"  Compte courant suggere         : ~{SOCLE_VITAL * 5:,.0f} euros (5 mois de socle)")
    print()
    print(f"  Flux mensuels a cet age :")
    print(f"  Traitement net lisse           : {sal['total']:,.0f} euros/mois")
    print(f"  Virement ETF automatique       : {rep['etf_total']:,.0f} euros/mois")
    print(f"  Virement Securite automatique  : {rep['securite_total']:,.0f} euros/mois")


def main():
    parser = argparse.ArgumentParser(
        description="Calcul de carriere de William (Solo, euros constants 2026)"
    )
    sub = parser.add_subparsers(dest="cmd")

    # salaire
    p_sal = sub.add_parser("salaire", help="Salaire net pour un age donne")
    p_sal.add_argument("--age", type=int, required=True, help="Age de William")
    p_sal.add_argument("--hsup", type=int, default=3, help="Lecons sup. demandees (defaut: 3)")

    # repartition
    p_rep = sub.add_parser("repartition", help="Repartition du surplus")
    p_rep.add_argument("--net", type=float, required=True, help="Revenu net total")

    # patrimoine
    p_pat = sub.add_parser("patrimoine", help="Patrimoine projete")
    p_pat.add_argument("--age", type=int, required=True, help="Age cible")
    p_pat.add_argument("--hsup", type=int, default=3, help="Lecons sup. demandees (defaut: 3)")

    # grille
    p_gri = sub.add_parser("grille", help="Tableau complet de carriere")
    p_gri.add_argument("--hsup", type=int, default=3, help="Lecons sup. demandees (defaut: 3)")

    # soldes
    p_sol = sub.add_parser("soldes", help="Soldes de depart pour un univers")
    p_sol.add_argument("--age", type=int, required=True, help="Age de William au depart")
    p_sol.add_argument("--hsup", type=int, default=3, help="Lecons sup. demandees (defaut: 3)")

    args = parser.parse_args()
    if args.cmd is None:
        parser.print_help()
        sys.exit(1)

    cmds = {
        "salaire": cmd_salaire,
        "repartition": cmd_repartition,
        "patrimoine": cmd_patrimoine,
        "grille": cmd_grille,
        "soldes": cmd_soldes,
    }
    cmds[args.cmd](args)


if __name__ == "__main__":
    main()
