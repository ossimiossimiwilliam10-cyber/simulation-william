"""ESSAIS AUTOMATIQUES des outils du moteur (créé le 11/10/2026), sur une COPIE du dépôt : la partie en cours n'est jamais touchée.

    python outils/tests_moteur.py            # tous les essais (≈ 1 minute)
    python outils/tests_moteur.py --garder   # garde la copie pour l'inspecter (chemin affiché)

But : qu'un agent qui arrive (Claude, Gemini, Codex…) vérifie en une commande que tous les outils fonctionnent chez lui (version de
Python, encodage de la console, dépendances), et qu'une modification d'un outil n'en a pas cassé un autre. Chaque essai lance
l'outil comme le ferait le moteur et vérifie le code de sortie et un morceau de la sortie ou d'un fichier écrit.
"""
import argparse
import datetime as dt
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
IGNORES = shutil.ignore_patterns(".git", "archives", "sorties", ".claude", "__pycache__", "*.pyc")


class Essais:
    def __init__(self, copie):
        self.copie = copie
        self.ok = 0
        self.echecs = []

    def lancer(self, *args, attendu=0, contient=None, nom=None):
        env = dict(os.environ, PYTHONIOENCODING="utf-8", SIMULATION_AGENT="tests_moteur")
        r = subprocess.run([sys.executable, *args], cwd=str(self.copie), capture_output=True, text=True, encoding="utf-8",
                           errors="replace", env=env, timeout=180)
        nom = nom or " ".join(str(a) for a in args)[:90]
        sortie = r.stdout + r.stderr
        bon = (r.returncode == attendu) and (contient is None or contient in sortie)
        if bon:
            self.ok += 1
            print(f"  OK    {nom}")
        else:
            self.echecs.append(nom)
            print(f"  ÉCHEC {nom} (code {r.returncode}, attendu {attendu}"
                  + (f", « {contient} » absent" if contient and contient not in sortie else "") + ")")
            print("        " + sortie.strip().replace("\n", "\n        ")[:1200])
        return sortie

    def verifier(self, condition, nom):
        if condition:
            self.ok += 1
            print(f"  OK    {nom}")
        else:
            self.echecs.append(nom)
            print(f"  ÉCHEC {nom}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--garder", action="store_true")
    args = ap.parse_args()
    tmp = Path(tempfile.mkdtemp(prefix="simulation-essais-"))
    copie = tmp / "depot"
    shutil.copytree(RACINE, copie, ignore=IGNORES)
    print(f"Copie de travail : {copie}")
    e = Essais(copie)
    o = "outils/"

    print("\n[Relais et fichiers maîtres]")
    e.lancer(o + "maitres.py", "verifier", contient="synchronisés")
    e.lancer(o + "relais.py", "entree", "--court", contient="Où en est la partie")
    e.lancer(o + "relais.py", "verifier")

    print("\n[Horloge, agenda, argent, savoir]")
    e.lancer(o + "horloge.py", contient="tour n°")
    e.lancer(o + "agenda.py", "dus")
    e.lancer(o + "agenda.py", "verifier", contient="conforme")
    e.lancer(o + "grand_livre.py", "solde", contient="Patrimoine net")
    e.lancer(o + "grand_livre.py", "verifier", contient="conforme")
    e.lancer(o + "echeancier.py", "liste", contient="E001")
    e.lancer(o + "echeancier.py", "budget", "2040-08", contient="Solde des lignes actives")
    e.lancer(o + "echeancier.py", "prevoir", "--jusqua", "2040-12-31", "--simule", contient="prévu")
    e.lancer(o + "echeancier.py", "verifier", contient="conforme")
    e.lancer(o + "echeancier.py", "budget", "2040-08", contient="compte projet", nom="échéancier : virement permanent crédité sur « Projet »")
    e.lancer(o + "prets.py", "liste", contient="110 003,13", nom="prêt PR1 : capital restant dû au 14/07/2040 = 110 003,13 €")
    e.lancer(o + "prets.py", "verifier", contient="conforme")
    e.lancer(o + "prets.py", "tableau", "PR1", "--de", "2052-10", "--a", "2052-10", contient="0.00", nom="prêt PR1 : soldé en octobre 2052")
    e.lancer(o + "savoir.py", "verifier", contient="conforme")

    print("\n[Monde : météo, calendrier, lieux, faits, prix]")
    e.lancer(o + "meteo.py", "jour", contient="Météo du")
    e.lancer(o + "meteo.py", "prevision", "--jours", "3", contient="Prévisions consultées")
    e.lancer(o + "meteo.py", "heure", "2040-07-14 15:30", contient="°C")
    e.lancer(o + "calendrier_2040.py", "--soleil", "2040-06-21", "--lieu", "luxembourg", contient="lever 05:2")
    e.lancer(o + "calendrier_2040.py", "--scolaire", contient="vacances_ete")
    e.lancer(o + "calendrier_2040.py", "--evenements", "--du", "2040-07-14", "--au", "2040-09-30", contient="Schueberfouer")
    e.lancer(o + "calendrier_2040.py", "--ouvres", "2040-07-13", "--jours", "2", "--pays", "fr", contient="17/07/2040")
    sortie = e.lancer(o + "lieux.py", "ouverts", "--quand", "2040-07-14 10:00")
    e.verifier("fermé  supermarche_audun" in sortie and "OUVERT hypermarche_belval" in sortie,
               "lieux : le 14 juillet, supermarché d'Audun fermé (droit local) et hypermarché de Belval ouvert")
    e.lancer(o + "lieux.py", "voir", "boulangerie_audun", "--quand", "2040-07-15 08:00", "--simule", contient="ouvert")
    e.lancer(o + "lieux.py", "voir", "club_combat", "--quand", "2040-08-20 18:00", "--simule", contient="congés",
             nom="lieux : fermeture d'été du club (règle conges:)")
    e.lancer(o + "faits.py", "cherche", "taxe foncière", contient="F018")
    e.lancer(o + "prix.py", "cherche", "coupe", contient="PX009")
    e.lancer(o + "prix.py", "tirer", "PX010", "--simule", contient="Prix tiré")

    print("\n[Corps, fronts, rituels]")
    e.lancer(o + "corps.py", "seance", "--duree", "90", "--note", "essai", "--quand", "2040-07-13 18:00", contient="Corps :")
    e.lancer(o + "fronts.py", "creer", "--nom", "Essai de front", "--type", "menace", "--segments", "4",
             "--paliers", "2:premier palier|4:dernier palier", contient="H001")
    e.lancer(o + "fronts.py", "avancer", "H001", "--de", "2", "--raison", "essai", contient="PALIER 2 ATTEINT")
    e.lancer(o + "rituels.py", "dus", contient="Rituels du moteur")

    print("\n[Personnages et garde « mineurs »]")
    e.lancer(o + "personnage.py", "nouveau", "--contexte", "voisin_audun", "--role", "voisin d'en face", "--age", "40-60",
             contient="Écrit : etat/personnages.csv")
    e.lancer(o + "personnage.py", "nouveau", "--contexte", "eleve_lycee", "--role", "élève de 3e", "--age", "14-15",
             contient="MINEUR")
    e.lancer(o + "personnage.py", "liste", contient="MINEUR")
    e.lancer(o + "personnage.py", "nouveau", "--contexte", "rencontre_seoul", "--role", "rencontre à Séoul", "--sexe", "F",
             "--simule", contient="Séoul", nom="personnage.py : contexte de Séoul (âge de 20 ans au moins)")
    noms = [l.split(";")[1] for l in (copie / "etat" / "personnages.csv").read_text(encoding="utf-8").splitlines()[1:] if l.strip()]
    adulte, mineur = noms[-2], noms[-1]  # les deux personnages que l'essai vient de créer (le registre n'est plus vide)
    e.lancer(o + "jet.py", "--table", "T1", "--pour", mineur, "essai sur un mineur", attendu=1, contient="REFUSÉ",
             nom="jet.py refuse T1 pour un mineur")
    e.lancer(o + "jet.py", "--table", "T10", "--pour", mineur, "délai de réponse d'un élève", "--simule", contient="Tirage [T10]",
             nom="jet.py accepte T10 pour un mineur")
    e.lancer(o + "jet.py", "--table", "T1", "--pour", adulte, "essai sur un adulte", "--simule", contient="Tirage [T1]",
             nom="jet.py accepte T1 pour un adulte (essai)")
    e.lancer(o + "jet.py", "--table", "T20a", "proposition sans personne nommée", attendu=1, contient="REFUSÉ",
             nom="jet.py refuse T20a sans --pour")
    e.lancer(o + "jet.py", "--table", "T20b", "--pour", mineur, "essai sur un mineur", attendu=1, contient="REFUSÉ",
             nom="jet.py refuse T20b pour un mineur")
    e.lancer(o + "jet.py", "--table", "T20a", "--pour", adulte, "essai sur une adulte", "--simule", contient="Tirage [T20a]",
             nom="jet.py accepte T20a pour une adulte inscrite (essai)")
    e.lancer(o + "jet.py", "La voisine en parle à son mari", "50", attendu=1, contient="REFUSÉ",
             nom="garde de la règle 17 : rôle reconnu sans fiche")
    e.verifier((copie / "memoire" / "simulations.jsonl").exists(), "les essais --simule sont tracés (memoire/simulations.jsonl)")
    e.lancer(o + "personnage.py", "audit", contient="récurrent")
    e.lancer(o + "personnage.py", "reseau", "--plan", "donnees/population/reseau-william.csv", "--simule", contient="essai :",
             nom="personnage.py reseau --simule (entourage)")
    e.lancer(o + "personnage.py", "reseau", "--plan", "donnees/population/reseau-william.csv", attendu=1, contient="déjà",
             nom="personnage.py reseau : un réseau ne se tire qu'une fois")
    caches = [l.split(";")[1] for l in (copie / "etat" / "personnages.csv").read_text(encoding="utf-8").splitlines()[1:]
              if ";pre_genere;" in l]
    if caches:
        e.lancer(o + "personnage.py", "apparait", caches[0], "--scene", "essai", contient="apparaît",
                 nom="personnage.py apparait : pré-généré → figurant")
        e.lancer(o + "personnage.py", "liste", "--statut", "figurant", contient=caches[0].split()[0])

    print("\n[Base de données]")
    e.lancer(o + "base.py", "construire", contient="Base reconstruite")
    e.lancer(o + "base.py", "requete", "SELECT nom, age, mineur FROM v_personnages", contient="oui")
    e.lancer(o + "base.py", "requete", "SELECT CASE WHEN COUNT(*) >= 40 THEN 'au moins quarante' END AS n FROM faits", contient="au moins quarante",
             nom="base : la table des faits est remplie (40 faits ou plus)")
    e.lancer(o + "base.py", "requete", "SELECT id, capital FROM prets", contient="PR1")
    e.lancer(o + "base.py", "cherche", "boulangerie", contient="lieux")
    e.lancer(o + "base.py", "requete", "DELETE FROM faits", attendu=1, contient="Lecture seule", nom="base : écriture refusée")
    e.lancer(o + "base.py", "verifier", contient="Base :")

    print("\n[Tour complet : début, fin avec texte, téléphone, contrôle]")
    e.lancer(o + "tour.py", "debut", "--simule", contient="Fiche moteur")
    # l'essai part de l'horloge de la partie, quelle qu'elle soit (12/10/2026 : il supposait le tour 0 du 14/07 à 08h37)
    texte_h = (copie / "etat" / "horloge.txt").read_text(encoding="utf-8")
    t0 = dt.datetime.strptime(re.search(r"^horloge:\s*(.+)$", texte_h, re.M).group(1).strip(), "%Y-%m-%d %H:%M")
    n0 = int(re.search(r"^tour:\s*(\d+)", texte_h, re.M).group(1)) if re.search(r"^tour:", texte_h, re.M) else 0
    t1 = t0 + dt.timedelta(minutes=25)
    jours = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"]
    mois = ["JANVIER", "FÉVRIER", "MARS", "AVRIL", "MAI", "JUIN", "JUILLET", "AOÛT", "SEPTEMBRE", "OCTOBRE", "NOVEMBRE", "DÉCEMBRE"]
    brouillon = copie / "brouillon-essai.md"
    brouillon.write_text(f"**{jours[t1.weekday()]} {t1.day} {mois[t1.month - 1]} {t1.year} — {t1:%H}h{t1:%M} — Essai**\n\n"
                         "Texte d'essai du tour.\n\nQue veux-tu faire ?\n", encoding="utf-8")
    e.lancer(o + "tour.py", "fin", "--jusqua", f"{t1:%Y-%m-%d %H:%M}", "--attente", "Essai", "--texte", str(brouillon),
             "--message", "message d'essai du joueur", contient="Texte du tour enregistré")
    e.verifier("Texte d'essai du tour" in (copie / "etat" / "dernier-tour.md").read_text(encoding="utf-8"),
               "etat/dernier-tour.md contient le texte exact du tour")
    e.verifier((copie / "journal" / "tours" / f"{t1:%Y-%m-%d}.md").exists(), f"journal/tours/{t1:%Y-%m-%d}.md écrit")
    e.lancer(o + "horloge.py", contient=f"tour n° {n0 + 1}", nom="horloge : le compteur de tours avance d'un cran")
    e.lancer(o + "tour.py", "apercu", "--jusqua", f"{t1 + dt.timedelta(days=3):%Y-%m-%d} 08:00", contient="Aperçu de l'avance rapide")
    e.lancer(o + "telephone.py", contient="11 applications",
             nom="téléphone : écran d'accueil et onze applications (Portefeuille et Courses : 14/10/2026)")

    print("\n[Applications du téléphone : voyages et calendrier]")
    e.lancer(o + "voyages.py", "verifier", contient="conforme")
    e.lancer(o + "voyages.py", "vols", "--de", "LUX", "--vers", "NSI", "--aller", "2040-08-28", "--retour", "2040-09-18", contient="1 005 €",
             nom="voyages : le prix montré au tour n° 2 (1 005 € le 28/08) est retrouvé")
    e.lancer(o + "voyages.py", "mois", "--de", "LUX", "--vers", "NSI", "--mois", "2040-07", contient="1 737 €",
             nom="voyages : plancher de juillet (1 737 €) retrouvé")
    e.lancer(o + "voyages.py", "forfait", "--aller", "2040-08-28", "--retour", "2040-09-18", contient="séparément")
    e.lancer(o + "voyages.py", "formalites", "--vers", "NSI", contient="Fièvre jaune")
    e.lancer(o + "appli_calendrier.py", contient="ferie")
    e.lancer(o + "voyages.py", "vols", "--de", "LUX", "--vers", "MNL", "--aller", "2040-07-20", "--retour", "2040-08-31", contient="1 705 €",
             nom="voyages : Manille, prix montré au tour n° 4 retrouvé")
    e.lancer(o + "voyages.py", "formalites", "--vers", "MNL", contient="eTravel")
    e.lancer(o + "banque.py", "liste", contient="ordre E012")
    e.lancer(o + "banque.py", "ordre-modifier", "E014", "--montant", "2900", "--quand", "2040-07-14 10:30", contient="modifié",
             nom="banque : un ordre permanent se modifie (prévus recalculés)")
    e.lancer(o + "banque.py", "virement", "--de", "courant", "--vers", "projet", "--montant", "100", "--quand", "2040-07-14 10:31",
             contient="exécuté", nom="banque : virement immédiat entre comptes")
    e.lancer(o + "grand_livre.py", "verifier", contient="conforme", nom="grand livre conforme après les opérations bancaires")
    e.lancer(o + "rencontres.py", "liste", contient="«", nom="rencontres : profils de Manille")
    e.lancer(o + "rencontres.py", "completer", "--ville", "MNL", "--de", "17", "--a", "20", "--simule", attendu=1, contient="REFUSÉ",
             nom="rencontres : garde absolue, aucun profil de moins de 18 ans (12/10/2026)")
    e.lancer(o + "cartes.py", "liste", contient="Visa Premier", nom="cartes : plafonds et disponible")
    e.lancer(o + "cartes.py", "payer", "--carte", "visa_debit", "--montant", "3000", "--marchand", "Essai", "--quand", "2040-07-14 11:00",
             "--simule", attendu=2, contient="REFUSÉ", nom="cartes : paiement au-delà du plafond refusé")
    e.lancer(o + "cartes.py", "payer", "--carte", "visa_debit", "--montant", "20", "--marchand", "Essai", "--quand", "2040-07-14 11:01",
             contient="AUTORISÉ", nom="cartes : paiement dans le plafond autorisé (débit immédiat)")
    e.lancer(o + "cartes.py", "verifier", contient="conforme")
    e.lancer(o + "transports.py", "verifier", contient="conforme")
    e.lancer(o + "etravel.py", "inscrire", "--reservation", "R004", "--quand", "2040-07-14 11:20", "--simule", attendu=1, contient="REFUSÉ",
             nom="eTravel : refusé plus de 72 heures avant l'arrivée (tour du 14/07)")
    e.lancer(o + "transports.py", "options", "--de", "AUD", "--vers", "FDL", "--quand", "2040-07-18 11:30", contient="Findel",
             nom="transports : Audun-le-Tiche → aéroport de Findel (tour du 16/07)")
    e.lancer(o + "etiquettes.py", "--simule", "--texte", "Test [banque: ordre-suspendre id=E014] [rencontres: aimer id=x] [voyages: reserver vol=W1 aller=2040-09-04 retour=2040-09-25 voyageurs=1]",
             contient="ordre-suspendre", nom="étiquettes : lecture des actions copiées depuis le téléphone")
    e.lancer(o + "appli_calendrier.py", contient="argent")
    e.lancer(o + "voyages.py", "reserver", "--vol", "V3", "--aller", "2040-08-28", "--retour", "2040-09-18", "--quand", "2040-07-14 10:00",
             "--simule", contient="1 005", nom="voyages : réservation (essai) au prix de la page")

    print("\n[Monde vivant, réactions, argent sur place, courses, actualités (14/10/2026)]")
    e.lancer(o + "routines.py", "voir", "Kiara Reyes", contient="sommeil", nom="routines : horaires de vie d'un personnage")
    e.lancer(o + "reactions.py", "en-attente", nom="réactions : réponses programmées")
    e.lancer(o + "monde_vivant.py", "liens", contient="Kiara Reyes", nom="monde vivant : états des liens")
    e.lancer(o + "actions.py", "liste", nom="actions programmées : liste")
    e.lancer(o + "tropiques.py", "liste", contient="TC01", nom="tropiques : tempêtes de la saison")
    e.lancer(o + "jet.py", "essai de procédure", "50", "--procedure", "essai", "--simule", contient="[PROCÉDURE : essai]",
             nom="jet : sous-tirage de procédure (ni dérogation, ni réaction)")
    e.lancer(o + "devises.py", "verifier", contient="devises : OK")
    e.lancer(o + "devises.py", "taux", "--jour", "2040-07-19", contient="PHP", nom="devises : taux du jour")
    e.lancer(o + "devises.py", "retirer", "--montant", "10000", "--distributeur", "bdo_naia3", "--quand", "2040-07-19 23:40", "--simule",
             contient="RÉUSSI", nom="devises : retrait au distributeur (frais du distributeur et de la banque)")
    e.lancer(o + "devises.py", "retirer", "--montant", "10050", "--distributeur", "bdo_naia3", "--quand", "2040-07-19 23:40", "--simule",
             contient="multiple de 100", nom="devises : montant refusé par le distributeur")
    e.lancer(o + "devises.py", "payer", "--montant", "850", "--marchand", "Essai", "--quand", "2040-07-19 23:40", "--simule",
             contient="AUTORISÉ", nom="devises : paiement par carte en pesos (cours Visa et frais)")
    e.lancer(o + "courses.py", "verifier", contient="courses : OK")
    e.lancer(o + "courses.py", "options", "--de", "naia_t3", "--vers", "city_garden", "--quand", "2040-07-19 23:45", contient="Taxi à coupon",
             nom="courses : options depuis l'aéroport (Grab et taxis)")
    e.lancer(o + "courses.py", "commander", "--service", "grab_car", "--de", "naia_t3", "--vers", "city_garden", "--quand", "2040-07-19 23:45",
             "--simule", attendu=1, contient="pas installé", nom="courses : Grab exige l'application installée")
    e.lancer(o + "courses.py", "installer", "--quand", "2040-07-19 23:46", contient="Grab installé", nom="courses : installation de Grab")
    e.lancer(o + "courses.py", "commander", "--service", "grab_car", "--de", "naia_t3", "--vers", "city_garden", "--quand", "2040-07-19 23:47",
             "--simule", contient="pas assez d'espèces", nom="courses : Grab payé en espèces sans pesos (problème à l'arrivée)")
    e.lancer(o + "actualites.py", "verifier", contient="actualités : OK")
    e.lancer(o + "actualites.py", "semaine", "--lundi", "2040-07-23", contient="SONA", nom="actualités : semaine du 23/07 (SONA)")
    e.lancer(o + "etiquettes.py", "--simule", "--texte", "[portefeuille: retirer carte=visa_debit montant=10000 distributeur=bdo_naia3] "
             "[courses: commander service=taxi_coupon de=naia_t3 vers=city_garden paiement=especes]", contient="courses.py",
             nom="étiquettes : Portefeuille et Courses")

    print("\n[P22 à P26, validées le 14/10/2026 : « j'aime » reçus, intentions, matchs, chauffeurs]")
    e.lancer(o + "jet.py", "--table", "T21c", "--mod", "M100", "--mod", "M101", "essai", "--simule", contient="Tirage [T21c]",
             nom="jet : T21c et modificateurs à trois chiffres (M100, M101)")
    e.lancer(o + "jet.py", "--table", "T23", "--pour", "Kiara Reyes", "essai", "--simule", contient="Tirage [T23]",
             nom="jet : T23 pour une adulte")
    e.lancer(o + "jet.py", "--table", "T23", "--pour", mineur, "essai sur un mineur", attendu=1, contient="REFUSÉ",
             nom="garde : T23 refusée pour un mineur")
    e.lancer(o + "rencontres.py", "likes-recus", "--jour", "2040-07-20", "--simule", contient="T21c",
             nom="rencontres : « j'aime » reçus (T21c)")
    e.lancer(o + "rencontres.py", "menage", "--lundi", "2040-07-23", "--simule", nom="rencontres : ménage des matchs (T21d)")
    e.lancer(o + "reactions.py", "rencontre", "--pour", "Kiara Reyes", "--quand", "2040-07-21 15:00", "--lieu", "essai", "--simule",
             contient="T23", nom="réactions : rencontre en personne, puis T23")
    e.lancer(o + "courses.py", "commander", "--service", "taxi_blanc", "--de", "naia_t3", "--vers", "city_garden",
             "--quand", "2040-07-19 23:50", "--simule", contient="T24a", nom="courses : chauffeur de taxi tiré (aléa A33, T24a)")
    e.lancer(o + "courses.py", "annuler", "C999", attendu=1, contient="rien à annuler", nom="courses : annulation sans course")
    e.lancer(o + "controle_coherence.py", contient="RÉSULTAT")

    print(f"\n{e.ok} essai(s) réussi(s), {len(e.echecs)} échec(s).")
    for n in e.echecs:
        print("  -", n)
    if args.garder:
        print(f"Copie gardée : {copie}")
    else:
        shutil.rmtree(tmp, ignore_errors=True)
    return 1 if e.echecs else 0


if __name__ == "__main__":
    sys.exit(main())
