#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""outils/intelligence_economique.py — Flux d'intelligence économique informelle (Signaux faibles & Bruits du marché)

Usage:
    python outils/intelligence_economique.py
    python outils/intelligence_economique.py --sujet "solaire_energie"
    python outils/intelligence_economique.py --marquer-connu INT-xxx
"""

import argparse
import csv
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

def charger_interactions(sujet_filtre=None):
    p = RACINE / "etat" / "interactions.csv"
    if not p.exists():
        return []
    interactions = []
    with open(p, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            if sujet_filtre and row.get("sujet") != sujet_filtre:
                continue
            interactions.append(row)
    return interactions

def main():
    parser = argparse.ArgumentParser(description="Intelligence économique et signaux faibles d'Abidjan")
    parser.add_argument("--sujet", help="Filtrer par sujet (ex: solaire_energie, emploi_business, immobilier)")
    parser.add_argument("--limite", type=int, default=5, help="Nombre max de signaux à afficher")
    parser.add_argument("--tous", action="store_true", help="Afficher tous les signaux y compris déjà connus")
    args = parser.parse_args()

    interactions = charger_interactions(sujet_filtre=args.sujet)
    
    # Filtrer par pertinence business
    pertinents = []
    for it in interactions:
        sujet = it.get("sujet", "")
        if sujet in ("solaire_energie", "emploi_business", "immobilier", "formalites_administratives"):
            if args.tous or it.get("connu_william") != "oui":
                pertinents.append(it)

    print(f"=== Veille Économique SOLEIL B2B CI : Signaux Faibles du Marché ({len(pertinents)} captés) ===")
    for idx, it in enumerate(pertinents[:args.limite], 1):
        print(f"\n[{idx}] {it.get('id')} | Sujet : {it.get('sujet').upper()} | Lieu : {it.get('lieu')}")
        print(f"    Acteurs : {it.get('personnage_a')} & {it.get('personnage_b')} ({it.get('type_lien')})")
        print(f"    Signal : {it.get('description')}")
        print(f"    Impact stratégique : {it.get('impact')}")

if __name__ == "__main__":
    main()
