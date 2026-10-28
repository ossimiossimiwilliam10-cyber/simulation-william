#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""outils/dashboard_gestion.py — Tableau de bord financier et de trésorerie SOLEIL B2B CI (Application Gestion)

Usage:
    python outils/dashboard_gestion.py
    python outils/dashboard_gestion.py --json
"""

import argparse
import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

def obtenir_donnees_financieres():
    # Paramètres de référence validés dans l'Univers 3
    taux_fcfa = 655.957
    cca_total_eur = 65560.0
    cca_total_fcfa = 43000000.0
    cca_rembourse_eur = 0.0
    cca_rembourse_fcfa = 0.0
    
    financement_epargne_eur = 32780.0
    financement_etf_eur = 32780.0
    
    opex_mensuel = {
        "Loyer villa Deux-Plateaux Vallons": 1750000,
        "Rémunération Direction Générale (Coulibaly)": 1800000,
        "Salaire Direction Administrative et Financière (Brou)": 1200000,
        "Intendance, cantine d'entreprise et fournitures": 350000,
        "Gardiennage sécurisé 24/7": 250000,
        "Charges fluides (split climatisation, électricité CIE, eau, fibre)": 300000,
    }
    
    total_opex_fcfa = sum(opex_mensuel.values())
    total_opex_eur = total_opex_fcfa / taux_fcfa
    
    capex_initial = {
        "Dépôt de garantie villa (2 mois)": 3500000,
        "Premier loyer après franchise de 15 jours": 1750000,
        "Équipements informatiques, mobilier et split-climatisations (4 pôles)": 15000000,
        "Véhicules de fonction et mobilité commerciale (2 utilitaires légers)": 18000000,
        "Trésorerie de réserve opérationnelle": 4750000,
    }
    
    total_capex_fcfa = sum(capex_initial.values())
    total_capex_eur = total_capex_fcfa / taux_fcfa
    
    # Runway prévisionnel (trésorerie de démarrage divisée par opex)
    # Après investissements CAPEX, les 4,75 M FCFA de trésorerie résiduelle représentent environ 0,8 mois,
    # mais l'engagement total du CCA (43 M FCFA) couvre l'ensemble des besoins de démarrage.
    runway_mois = (cca_total_fcfa - (total_capex_fcfa - 4750000)) / total_opex_fcfa
    
    return {
        "entite": "SOLEIL B2B CI SASU",
        "statut_legal": "En cours d'attribution RCCM & IDU (Guichet unique CEPICI)",
        "cca_total_eur": cca_total_eur,
        "cca_total_fcfa": cca_total_fcfa,
        "cca_rembourse_eur": cca_rembourse_eur,
        "cca_restant_eur": cca_total_eur - cca_rembourse_eur,
        "pourcentage_recouvre": (cca_rembourse_eur / cca_total_eur) * 100,
        "financement_mixte": {
            "compte_epargne_eur": financement_epargne_eur,
            "compte_etf_monde_eur": financement_etf_eur,
        },
        "opex_mensuel_fcfa": opex_mensuel,
        "total_opex_mensuel_fcfa": total_opex_fcfa,
        "total_opex_mensuel_eur": round(total_opex_eur, 2),
        "capex_initial_fcfa": capex_initial,
        "total_capex_fcfa": total_capex_fcfa,
        "total_capex_eur": round(total_capex_eur, 2),
        "runway_mois_estime": round(runway_mois, 1),
    }

def afficher_tableau_bord(donnees):
    print("=" * 70)
    print(f"TABLEAU DE BORD DE GESTION — {donnees['entite']}")
    print(f"Statut : {donnees['statut_legal']}")
    print("=" * 70)
    
    print("\n1. SUIVI DU COMPTE COURANT D'ASSOCIÉ (CCA — WILLIAM OSSIMI)")
    print(f"   • Prêt total consenti      : {donnees['cca_total_eur']:,.2f} €  ({donnees['cca_total_fcfa']:,.0f} FCFA)")
    print(f"     - Tranche Épargne        : {donnees['financement_mixte']['compte_epargne_eur']:,.2f} €")
    print(f"     - Tranche ETF Monde      : {donnees['financement_mixte']['compte_etf_monde_eur']:,.2f} €")
    print(f"   • Montant remboursé        : {donnees['cca_rembourse_eur']:,.2f} € ({donnees['pourcentage_recouvre']:.1f} %)")
    print(f"   • Capital restant dû       : {donnees['cca_restant_eur']:,.2f} €")
    print("   • Règle de remboursement   : 100 % des dividendes prélevés reversés sur ETF Monde")
    
    print("\n2. PROGRAMME D'INVESTISSEMENTS DE DÉMARRAGE (CAPEX INITIAL)")
    for poste, montant in donnees['capex_initial_fcfa'].items():
        print(f"   • {poste:<60} : {montant:10,d} FCFA")
    print(f"   --> Total Démarrage & Aménagement : {donnees['total_capex_fcfa']:,.0f} FCFA ({donnees['total_capex_eur']:,.2f} €)")
    
    print("\n3. CHARGES FIXES MENSUELLES RÉCURRENTES (OPEX PRÉVISIONNEL)")
    for poste, montant in donnees['opex_mensuel_fcfa'].items():
        print(f"   • {poste:<60} : {montant:10,d} FCFA")
    print(f"   --> Total Charges Fixes / mois    : {donnees['total_opex_mensuel_fcfa']:,.0f} FCFA ({donnees['total_opex_mensuel_eur']:,.2f} €)")
    
    print("\n4. HORIZON DE TRÉSORERIE & RUNWAY")
    print(f"   • Runway opérationnel estimé      : ~{donnees['runway_mois_estime']} mois de fonctionnement")
    print("   • Alerte trésorerie                : Dépôt de garantie et caution de bail à verser vendredi")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Tableau de bord financier SOLEIL B2B CI")
    parser.add_argument("--json", action="store_true", help="Sortie au format JSON")
    args = parser.parse_args()

    data = obtenir_donnees_financieres()
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        afficher_tableau_bord(data)

if __name__ == "__main__":
    main()
