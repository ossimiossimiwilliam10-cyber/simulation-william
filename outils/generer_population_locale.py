"""
Générateur de population locale en masse (créé le 14/08/2041, demande de l'utilisateur).
Génère à chaque début de semaine (chaque lundi simulé) un grand nombre de personnages
en lien avec l'environnement immédiat de William (Côte d'Ivoire / Abidjan, Luxembourg, etc.),
avec statut 'pre_genere', traits psychologiques, secrets, métiers et traits physiques.

Usage:
    python outils/generer_population_locale.py --zone abidjan --nombre 50
    python outils/generer_population_locale.py --zone abidjan --nombre 25 --simule
"""
import argparse
import random
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from commun import ETAT, ecrire_csv, lire_csv, utf8
import personnage
import base

REGISTRE = ETAT / "personnages.csv"
COLONNES = personnage.COLONNES

PONDERATIONS_ZONES = {
    "abidjan": [
        ("voisin_abidjan", [
            ("voisin de quartier", None, "25-65"),
            ("voisine de palier", "F", "28-60"),
            ("habitant des Deux-Plateaux", None, "30-55"),
            ("résident des Vallons", None, "35-65"),
            ("copropriétaire de la résidence", None, "40-70"),
        ], 25),
        ("commerce_abidjan", [
            ("restaurateur de maquis", None, "30-55"),
            ("commerçante de marché", "F", "25-60"),
            ("gérant de café de plage", "H", "28-50"),
            ("pharmacienne de garde", "F", "30-55"),
            ("boulanger-pâtissier", "H", "24-48"),
            ("gérant de supérette", None, "26-52"),
        ], 20),
        ("services_abidjan", [
            ("chauffeur VTC régulier", "H", "24-48"),
            ("gardien d'immeuble de standing", "H", "28-55"),
            ("employée d'intendance et ménage", "F", "22-45"),
            ("agent de sécurité privée", "H", "23-45"),
            ("mécanicien automobile spécialisé", "H", "25-50"),
            ("livreur express de documents", "H", "20-35"),
        ], 20),
        ("professionnel_plateau", [
            ("cadre supérieur bancaire", None, "32-58"),
            ("juriste d'affaires cabinet OHADA", None, "28-50"),
            ("clerc de notaire", None, "27-46"),
            ("comptable d'entreprise B2B", None, "29-52"),
            ("courtier d'assurances professionnelles", None, "33-56"),
            ("agent instructeur CEPICI", None, "30-55"),
        ], 15),
        ("solaire_technique_ci", [
            ("électricien industriel haute tension", "H", "25-48"),
            ("technicien installateur photovoltaïque", None, "23-42"),
            ("chef d'équipe de chantier toiture", "H", "30-52"),
            ("ingénieur bureau d'études électricité", None, "26-45"),
            ("technicien de maintenance onduleurs", "H", "24-44"),
        ], 10),
        ("etudiante_abidjan", [
            ("étudiante en master d'économie UFHB", "F", "21-25"),
            ("étudiant en master de droit des affaires", "H", "21-25"),
            ("étudiante en école d'ingénieurs INP-HB", "F", "20-24"),
            ("jeune diplômé en marketing digital", None, "22-26"),
        ], 10),
    ]
}


def generer_contingent(zone="abidjan", nombre=50, simule=False):
    if zone not in PONDERATIONS_ZONES:
        sys.exit(f"Zone non configurée pour la génération de masse : {zone}")

    pool = PONDERATIONS_ZONES[zone]
    rng = random.SystemRandom()
    existants = [l["nom"] for l in personnage.lire()]
    lignes_existantes = personnage.lire()

    nouveaux_personnages = []

    for _ in range(nombre):
        # Tirage pondéré du contexte
        ctx_nom, roles_possibles, _ = personnage.pondere(rng, [(item, item[2]) for item in pool])
        role_modele, sexe_force, tranche_age = rng.choice(roles_possibles)

        sexe = sexe_force
        if not sexe:
            sexe = "F" if rng.random() < 0.5 else "H"

        role = personnage.libelle_sexe(role_modele, sexe)
        pers = personnage.tirer(ctx_nom, role, sexe, tranche_age, rng=rng, existants=existants)
        existants.append(pers["nom"])

        # Enregistrement au registre avec statut pre_genere
        note = f"génération de masse zone {zone} ({pers['commune']}) · réseau local vivant"
        ligne = personnage.ligne_registre(pers, "pre_genere", "", cercle="4", note=note)
        nouveaux_personnages.append((pers, ligne))

    if simule:
        print(f"[SIMULATION] {len(nouveaux_personnages)} personnages pré-générés pour {zone} :")
        for p, _ in nouveaux_personnages[:10]:
            print(f"  - {p['nom']} ({p['age']} ans, {p['sexe']}) : {p['role']} — {p['commune']}")
        print(f"  ... et {len(nouveaux_personnages) - 10} autres.")
        return len(nouveaux_personnages)

    # Écriture dans etat/personnages.csv
    for _, ligne in nouveaux_personnages:
        lignes_existantes.append(ligne)

    ecrire_csv(REGISTRE, lignes_existantes, COLONNES)

    # Consignation dans tirages.jsonl
    for pers, _ in nouveaux_personnages:
        personnage.consigner(pers, "pre_genere")

    print(f"[SUCCÈS] {len(nouveaux_personnages)} nouveaux personnages pré-générés pour la zone '{zone}'.")
    print(f"Total des personnages enregistrés : {len(lignes_existantes)}")

    # Mise à jour de la base SQLite
    try:
        base.construire()
        print("[SUCCÈS] Base sorties/monde.sqlite synchronisée.")
    except Exception as e:
        print(f"[ATTENTION] Synchronisation SQLite différée : {e}")

    return len(nouveaux_personnages)


def main():
    utf8()
    parser = argparse.ArgumentParser(description="Générateur de population locale en masse")
    parser.add_argument("--zone", default="abidjan", help="Zone géographique (abidjan, luxembourg, etc.)")
    parser.add_argument("--nombre", type=int, default=50, help="Nombre de personnages à générer")
    parser.add_argument("--simule", action="store_true", help="Essai sans écriture sur disque")
    args = parser.parse_args()

    generer_contingent(zone=args.zone, nombre=args.nombre, simule=args.simule)
    return 0


if __name__ == "__main__":
    main()
