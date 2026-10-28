"""
Système d'Interactions Sociales Aléatoires et Réseau Vivant
Créé le 14/08/2041 (demande de l'utilisateur : « les personnages peuvent potentiellement interagir entre eux,
de façon purement aléatoire, pas forcé comme dans les séries télévisées »).

Modélise le graphe social vivant de l'univers :
1. Liens de structure : voisinage, secteur professionnel, amitié, clientèle, famille.
2. Événements et interactions dynamiques : discussions, recommandations, tensions mineures, entraide, rumeurs.
3. Archivage dans `etat/interactions.csv` et base SQLite.

Usage :
    python outils/interactions_sociales.py tisser --zone abidjan
    python outils/interactions_sociales.py simuler --zone abidjan --nombre 15
    python outils/interactions_sociales.py voir "Mohamed Coulibaly"
    python outils/interactions_sociales.py rumeurs --zone abidjan
"""
import argparse
import datetime as dt
import random
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from commun import ETAT, ecrire_csv, lire_csv, maintenant_simule, slug, utf8
import personnage
import base

FICHIER_INTERACTIONS = ETAT / "interactions.csv"
COLONNES_INTERACTIONS = [
    "id", "date", "personnage_a", "personnage_b", "type_lien", "sujet", "description", "lieu", "connu_william", "impact"
]

TYPES_LIEN = [
    ("voisinage", "Voisinage dans le même quartier", 30),
    ("professionnel", "Relation d'affaires, collaboration ou recommandation", 35),
    ("amical_social", "Amitié, connaissance de maquis, sport ou culte", 20),
    ("famille_proche", "Lien familial étendu (cousins, fratrie)", 10),
    ("client_fournisseur", "Commerçant habituel, artisan ou prestataire de service", 15)
]

SUJETS_ABIDJAN = [
    ("immobilier", "Hausse des loyers de villas à Cocody et recherche de bureaux aux Deux-Plateaux"),
    ("solaire_energie", "Coupures d'électricité récurrentes de la CIE et intérêt croissant pour le photovoltaïque d'entreprise"),
    ("emploi_business", "Opportunités d'embauche dans les PME et retards de paiement dans les chantiers"),
    ("transport_voirie", "Circulation dense au carrefour Duncan et nouveaux chantiers du grand Abidjan"),
    ("vie_locale", "Organisation d'un mariage traditionnel le week-end et cotisations familiales"),
    ("commerce_approvisionnement", "Approvisionnement en vivres frais et hausse du coût de la vie"),
    ("formalites_administratives", "Délais de traitement des dossiers d'entreprises au guichet unique du CEPICI")
]


def charger_interactions():
    if not FICHIER_INTERACTIONS.exists():
        return []
    return lire_csv(FICHIER_INTERACTIONS)


def sauvegarder_interactions(lignes):
    ecrire_csv(FICHIER_INTERACTIONS, lignes, COLONNES_INTERACTIONS)


def personnages_zone(zone="abidjan"):
    tous = personnage.lire()
    if zone == "abidjan":
        return [p for p in tous if "abidjan" in (p.get("commune", "").lower() + p.get("contexte", "").lower())]
    return tous


def tisser_reseau(zone="abidjan", simule=False):
    """Établit des connexions réalistes et non forcées entre les personnages de la zone."""
    persos = personnages_zone(zone)
    if len(persos) < 2:
        print("Pas assez de personnages pour tisser un réseau social.")
        return 0

    rng = random.SystemRandom()
    interactions = charger_interactions()
    existants_ids = {i["id"] for i in interactions}
    nouveaux = []

    date_courante = (maintenant_simule() or dt.datetime(2041, 8, 14)).strftime("%Y-%m-%d")

    # On crée quelques dizaines de liens de proximité
    nb_liens = min(len(persos) * 2, 60)
    for _ in range(nb_liens):
        pa, pb = rng.sample(persos, 2)
        if pa["nom"] == pb["nom"]:
            continue

        id_lien = f"INT-{slug(pa['nom'])[:8]}-{slug(pb['nom'])[:8]}"
        if id_lien in existants_ids:
            continue

        type_lien = personnage.pondere(rng, [(t[0], t[2]) for t in TYPES_LIEN])
        sujet_cle, sujet_desc = rng.choice(SUJETS_ABIDJAN)

        if type_lien == "voisinage":
            desc = f"{pa['nom']} et {pb['nom']} résident dans le même secteur et se saluent régulièrement lors des trajets du matin."
            lieu = pa.get("commune", "Abidjan")
        elif type_lien == "professionnel":
            desc = f"{pa['nom']} ({pa['role']}) a échangé avec {pb['nom']} ({pb['role']}) sur {sujet_desc.lower()}."
            lieu = "Plateau / Deux-Plateaux"
        elif type_lien == "client_fournisseur":
            desc = f"{pa['nom']} fait régulièrement appel aux services de {pb['nom']} ({pb['role']}) pour ses besoins courants."
            lieu = "Cocody"
        elif type_lien == "amical_social":
            desc = f"{pa['nom']} et {pb['nom']} se retrouvent occasionnellement en soirée dans un maquis convivial pour partager un repas."
            lieu = "Deux-Plateaux Vallons"
        else:
            desc = f"{pa['nom']} et {pb['nom']} partagent des attaches familiales élargies et prennent des nouvelles des anciens."
            lieu = "Abidjan"

        ligne = {
            "id": id_lien,
            "date": date_courante,
            "personnage_a": pa["nom"],
            "personnage_b": pb["nom"],
            "type_lien": type_lien,
            "sujet": sujet_cle,
            "description": desc,
            "lieu": lieu,
            "connu_william": "non",
            "impact": "bénin"
        }
        nouveaux.append(ligne)
        existants_ids.add(id_lien)

    if simule:
        print(f"[SIMULATION] {len(nouveaux)} interactions tissées pour la zone '{zone}' :")
        for n in nouveaux[:8]:
            print(f"  - [{n['type_lien']}] {n['personnage_a']} <-> {n['personnage_b']} : {n['description']}")
        return len(nouveaux)

    interactions.extend(nouveaux)
    sauvegarder_interactions(interactions)
    print(f"[SUCCÈS] {len(nouveaux)} nouvelles interactions sociales aléatoires enregistrées dans etat/interactions.csv.")
    return len(nouveaux)


def simuler_evenements(zone="abidjan", nombre=10, simule=False):
    """Génère des événements vivants aléatoires entre personnages."""
    persos = personnages_zone(zone)
    if len(persos) < 2:
        return 0

    rng = random.SystemRandom()
    interactions = charger_interactions()
    date_courante = (maintenant_simule() or dt.datetime(2041, 8, 14)).strftime("%Y-%m-%d")
    nouveaux = []

    for k in range(nombre):
        pa, pb = rng.sample(persos, 2)
        id_event = f"EVT-{date_courante}-{k+1:03d}-{slug(pa['nom'])[:6]}"
        type_lien = rng.choice(["rencontre_fortuite", "recommandation", "rumeur_partagee", "entraide_locale", "devis_commercial"])
        sujet_cle, sujet_desc = rng.choice(SUJETS_ABIDJAN)

        if type_lien == "recommandation":
            desc = f"{pa['nom']} a vivement recommandé les compétences de {pb['nom']} ({pb['role']}) à un responsable de société locale."
        elif type_lien == "rumeur_partagee":
            desc = f"{pa['nom']} a partagé avec {pb['nom']} une rumeur concernant {sujet_desc.lower()}."
        elif type_lien == "entraide_locale":
            desc = f"{pa['nom']} a apporté une aide logistique ponctuelle à {pb['nom']} suite à un aléa de transport."
        elif type_lien == "devis_commercial":
            desc = f"{pa['nom']} a sollicité {pb['nom']} pour une étude tarifaire sur des prestations professionnelles."
        else:
            desc = f"{pa['nom']} et {pb['nom']} se sont croisés par hasard dans un commerce des Deux-Plateaux et ont discuté quelques minutes."

        ligne = {
            "id": id_event,
            "date": date_courante,
            "personnage_a": pa["nom"],
            "personnage_b": pb["nom"],
            "type_lien": type_lien,
            "sujet": sujet_cle,
            "description": desc,
            "lieu": "Abidjan (Cocody / Plateau)",
            "connu_william": "non",
            "impact": "organique"
        }
        nouveaux.append(ligne)

    if simule:
        print(f"[SIMULATION] {len(nouveaux)} événements de vie simulés :")
        for n in nouveaux[:5]:
            print(f"  - {n['description']}")
        return len(nouveaux)

    interactions.extend(nouveaux)
    sauvegarder_interactions(interactions)
    print(f"[SUCCÈS] {len(nouveaux)} événements relationnels simulés et inscrits au registre du monde vivant.")
    return len(nouveaux)


def voir_personnage(nom):
    interactions = charger_interactions()
    liens = [i for i in interactions if i["personnage_a"] == nom or i["personnage_b"] == nom]
    print(f"\n--- Réseau et interactions de {nom} ({len(liens)} liens répertoriés) ---")
    if not liens:
        print("  Aucune interaction enregistrée pour le moment.")
        return
    for l in liens:
        autre = l["personnage_b"] if l["personnage_a"] == nom else l["personnage_a"]
        print(f"  - [{l['date']}] Avec {autre} ({l['type_lien']}) : {l['description']}")


def rumeurs(zone="abidjan"):
    interactions = charger_interactions()
    bruits = [i for i in interactions if "rumeur" in i.get("type_lien", "") or i.get("sujet") in ("immobilier", "solaire_energie")]
    print(f"\n--- Bruits de couloir et échos sociaux ({zone}) ---")
    for b in bruits[-8:]:
        print(f"  - [{b['date']}] ({b['sujet']}) {b['description']}")


def main():
    utf8()
    parser = argparse.ArgumentParser(description="Système d'Interactions Sociales Aléatoires")
    subparsers = parser.add_subparsers(dest="commande")

    p_tisser = subparsers.add_parser("tisser", help="Tisser des liens initiaux de réseau social")
    p_tisser.add_argument("--zone", default="abidjan")
    p_tisser.add_argument("--simule", action="store_true")

    p_simuler = subparsers.add_parser("simuler", help="Simuler des interactions et événements sociaux")
    p_simuler.add_argument("--zone", default="abidjan")
    p_simuler.add_argument("--nombre", type=int, default=15)
    p_simuler.add_argument("--simule", action="store_true")

    p_voir = subparsers.add_parser("voir", help="Voir le réseau social d'un personnage")
    p_voir.add_argument("nom")

    p_rumeurs = subparsers.add_parser("rumeurs", help="Afficher les rumeurs et bruits du monde")
    p_rumeurs.add_argument("--zone", default="abidjan")

    args = parser.parse_args()

    if args.commande == "tisser":
        tisser_reseau(zone=args.zone, simule=args.simule)
    elif args.commande == "simuler":
        simuler_evenements(zone=args.zone, nombre=args.nombre, simule=args.simule)
    elif args.commande == "voir":
        voir_personnage(args.nom)
    elif args.commande == "rumeurs":
        rumeurs(zone=args.zone)
    else:
        parser.print_help()
    return 0


if __name__ == "__main__":
    main()
