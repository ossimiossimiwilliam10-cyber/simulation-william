#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""outils/lieux_frequentation.py — Fréquentation dynamique des lieux (Qui est là quand William y va ?)

Usage:
    python outils/lieux_frequentation.py "sofitel_ivoire_cocody"
    python outils/lieux_frequentation.py "Deux-Plateaux" --quand "2041-08-14 15:30"
    python outils/lieux_frequentation.py "maquis" --nombre 3
"""

import argparse
import csv
import os
import random
import sys
from datetime import datetime
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

def charger_horloge():
    p = RACINE / "etat" / "horloge.txt"
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    return line
    return "2041-08-14 12:30"

def charger_lieux():
    lieux = []
    p = RACINE / "donnees" / "lieux.csv"
    if not p.exists():
        return lieux
    with open(p, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            lieux.append(row)
    return lieux

def trouver_lieu(requete, lieux):
    req = requete.lower().strip()
    for l in lieux:
        if l["id"].lower() == req or req in l["nom"].lower():
            return l
    for l in lieux:
        if req in l.get("commune", "").lower() or req in l.get("type", "").lower():
            return l
    return None

def charger_personnages_zone(zone="abidjan"):
    persos = []
    p = RACINE / "etat" / "personnages.csv"
    if not p.exists():
        return persos
    with open(p, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            # Personnages avec statut pre_genere ou connu dans la zone
            z = row.get("zone", "").lower()
            ville = row.get("ville", "").lower()
            commune = row.get("commune", "").lower()
            if zone in z or "abidjan" in ville or "cocody" in commune or "plateau" in commune:
                persos.append(row)
    return persos

ACTIVITES_PAR_TYPE = {
    "sport": [
        "enchaîne des séries d'étirements sur le tapis avec concentration",
        "effectue une séance de cardio rythmée sur le vélo elliptique",
        "termine une session de musculation en réhydratant avec une gourde isotherme",
        "observe les courts de tennis extérieurs depuis la verrière climatisée",
        "discute calmement au bar diététique après son entraînement",
        "ajuste ses écouteurs sans fil avant d'attaquer une série de développé couché",
    ],
    "restaurant": [
        "déjeune tranquillement en consultant des dossiers sur sa tablette",
        "partage un poisson braisé et une assiette d'alloco avec entrain",
        "attend son plat tout en répondant à des messages vocaux professionnels",
        "sirote un jus de bissap frais à une table d'angle ombragée",
        "règle discrètement son addition auprès du responsable du maquis",
    ],
    "affaires": [
        "discute à voix basse d'un montage de financement près des mange-debout",
        "consulte une présentation commerciale sur son écran d'ordinateur ultra-fin",
        "salue chaleureusement une connaissance croisée dans les couloirs feutrés",
        "prend des notes méthodiques dans un carnet en cuir rigide",
        "attend son interlocuteur en savourant un espresso serré",
    ],
    "universite": [
        "relit attentivement des polycopiés de cours assis sur un banc sous les manguiers",
        "discute méthodologie de recherche de master avec un camarade",
        "traverse l'allée centrale d'un pas alerte, sac à dos en bandoulière",
        "consulte les panneaux d'affichage des départements académiques",
    ],
    "plage": [
        "marche pieds nus sur le sable humide en regardant les rouleaux atlantiques",
        "est assis sous une paillote en buvant de l'eau de coco fraîche",
        "observe les pêcheurs artisanaux ranger leurs filets au loin",
        "lit un roman à l'abri du soleil sous un parasol en raphia",
    ],
    "bureau": [
        "passe d'une pièce à l'autre avec une chemise cartonnée sous le bras",
        "vérifie l'étalonnage d'un appareil de mesure ou d'un équipement de bureau",
        "partage un bref échange opérationnel près de la fontaine à eau",
    ],
    "hotel": [
        "traverse le hall d'accueil avec une mallette en cuir souple",
        "consulte les horaires des navettes auprès du comptoir de la conciergerie",
        "attend confortablement assis dans un fauteuil club du salon d'attente",
    ],
}

def tirer_frequentation(lieu_info, personnages, dt, nb=2):
    t = lieu_info.get("type", "commerce").lower()
    activites = ACTIVITES_PAR_TYPE.get(t, [
        "est présent sur place et s'occupe tranquillement",
        "croise le regard des passants avant de reprendre son activité",
        "effectue une démarche courante sans précipitation"
    ])
    
    # Échantillonnage de personnages
    candidats = [p for p in personnages if p.get("statut") in ("pre_genere", "connu")]
    if not candidats:
        return []
    
    # Mélange reproductible ou basé sur l'heure/date
    seed_val = int(dt.strftime("%Y%m%d%H%M")) + sum(ord(c) for c in lieu_info.get("id", ""))
    rng = random.Random(seed_val)
    
    selection = rng.sample(candidats, min(nb, len(candidats)))
    resultats = []
    
    for p in selection:
        act = rng.choice(activites)
        nom_complet = p.get("nom", "").strip()
        # Calcul de l'âge approximatif depuis naissance
        naissance = p.get("naissance", "")
        age = "?"
        if naissance:
            annee = naissance.split("-")[0] if "-" in naissance else naissance
            if annee.isdigit():
                age = str(2041 - int(annee))
        prof = p.get("metier", "") or p.get("role", "") or "Actif local"
        commune = p.get("commune", "Abidjan")
        statut = p.get("statut", "pre_genere")
        traits = p.get("traits", "")
        notes = p.get("notes", "")
        
        resultats.append({
            "nom": nom_complet,
            "age": age,
            "profession": prof,
            "commune": commune,
            "statut": statut,
            "activite": act,
            "traits": traits,
            "notes": notes,
        })
        
    return resultats

def main():
    parser = argparse.ArgumentParser(description="Fréquentation dynamique des lieux d'Abidjan")
    parser.add_argument("lieu", help="Identifiant ou nom du lieu (ex: sofitel_ivoire_cocody, vallons)")
    parser.add_argument("--quand", help="Date et heure AAAA-MM-JJ HH:MM (défaut: horloge courante)")
    parser.add_argument("--nombre", type=int, default=2, help="Nombre de personnes présentes à tirer (défaut: 2)")
    args = parser.parse_args()

    date_str = args.quand or charger_horloge()
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        dt = datetime.now()

    lieux = charger_lieux()
    lieu_info = trouver_lieu(args.lieu, lieux)
    if not lieu_info:
        print(f"Lieu '{args.lieu}' non trouvé dans donnees/lieux.csv.")
        sys.exit(1)

    personnages = charger_personnages_zone(zone="abidjan")
    frequentation = tirer_frequentation(lieu_info, personnages, dt, nb=args.nombre)

    print(f"=== Fréquentation : {lieu_info['nom']} ===")
    print(f"Type : {lieu_info.get('type')} | Commune : {lieu_info.get('commune')} | Horodatage : {date_str}")
    print(f"Personnages locaux pré-générés présents ({len(frequentation)}) :")
    for idx, f in enumerate(frequentation, 1):
        print(f"  {idx}. {f['nom']} ({f['age']} ans, {f['profession']}, commune : {f['commune']}) [{f['statut']}]")
        print(f"     Action sur place : {f['activite']}")
        if f['traits']:
            print(f"     Traits : {f['traits']}")

if __name__ == "__main__":
    main()
