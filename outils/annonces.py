"""ANNONCES PUBLIQUES DE WILLIAM ET RÉPONSES (créé le 27/10/2026, tour n° 6 de l'univers 3 : annonce de recherche d'un contact en Côte d'Ivoire).

Le programme porte la simulation (CLAUDE.md §14) : il tire les réponses à une annonce publique par plateforme et par heure, crée chaque répondant avec le
générateur de personnages (zone Abidjan : contexte `candidat_annonce_abidjan`), le classe selon les règles de tri de l'agent IA de William (A, B, C), consigne
tout ; le moteur n'écrit ensuite que le rapport et les textes des messages.

    python outils/annonces.py liste                                        # annonces publiées (plateformes, état)
    python outils/annonces.py tirer --jusqua "2041-07-16 18:00" [--simule] # réponses arrivées depuis le dernier traitement
    python outils/annonces.py reponses [--depuis "AAAA-MM-JJ HH:MM"]       # réponses déjà tirées (moteur seul)
    python outils/annonces.py reseau "Nom" [--simule]                      # réseau d'un répondant en clients potentiels, noté sur 100 (moteur seul)
    python outils/annonces.py verifier

Fichiers : `etat/annonces.csv` (annonce, plateforme, publiée le, état, traitée jusqu'au), `etat/reponses-annonce.csv` (une ligne par réponse :
instant, plateforme, nom, niveau, profil, signaux d'alerte). Les lignes sont du MOINS visibles : rien ne va dans la page du téléphone ; William n'apprend
une réponse que par le rapport de l'agent (18h00) ou son alerte immédiate (niveau A).

Règles de tri (« Annonce et règles de l'agent IA », 16/07/2041) : A = dix ans d'expérience ou plus, références vérifiables, qualification élevée, métier
pertinent (énergie, électricité, bâtiment, conseil, recherche, cadre) ; B = sérieux mais incomplet (métier voisin, expérience plus courte, références
manquantes) ; C = hors profil ou signal d'alerte (demande d'argent, paiement anticipé, promesse de rendement, profil récent). Un répondant sur huit environ est
une arnaque (frais d'avance) : le signal d'alerte l'écarte quel que soit son profil.

Tirages : le flux d'arrivée des répondants à une annonce publique n'a pas de table validée (aucun personnage n'existe avant sa réponse) : jets libres avec
DÉROGATION consignée ; proposition d'une table à valider à la revue du lundi (memoire/propositions-2026-10-27.md).
"""
import argparse
import datetime as dt
import re
import subprocess
import sys

from commun import ETAT, OUTILS, RACINE, ecrire_csv, lire_csv, utf8

sys.path.insert(0, str(OUTILS))
ANNONCES = ETAT / "annonces.csv"
REPONSES = ETAT / "reponses-annonce.csv"
COL_A = ["id", "plateforme", "publiee_le", "etat", "traitee_jusqua", "note"]
COL_R = ["id", "quand", "plateforme", "nom", "niveau", "profil", "signaux", "note"]
TAUX = {"LinkedIn": 0.30, "Educarriere.ci": 0.55, "NovoJob": 0.50, "Indeed": 0.0, "Facebook": 0.70, "Instagram": 0.10, "Reddit": 0.10, "CoinAfrique": 0.35,
        "Kosafi Annonce CI": 0.25}  # réponses attendues par heure juste après la publication (réseaux sociaux : plus de monde, moins de sérieux)
ARNAQUE = {"Facebook": 22, "Instagram": 20, "Reddit": 15, "CoinAfrique": 20, "Kosafi Annonce CI": 20}  # part d'arnaques aux frais d'avance (défaut : 12 %)
SEUIL_CONTACT = 70  # note sur 100 à partir de laquelle l'agent obtient le numéro du répondant pour William (18/07/2041 ; 60 à 69 : second entretien)
DEROGATION = ("flux d'arrivée de répondants à une annonce publique : aucun personnage n'existe avant sa réponse, pas de table validée "
              "(proposition à la revue du lundi 22/07/2041)")
RESEAUX = ETAT / "reseaux-repondants.csv"
COL_N = ["nom", "proprietaires", "decideurs_pct", "factures_pct", "intros", "motivation", "note", "detail"]
PERTINENCE = [("ingénieur", 3), ("chercheur", 3), ("consultant", 2), ("cadre", 2), ("technicien", 2), ("immobilier", 1), ("comptable", 1),
              ("commerçant", 1), ("fonctionnaire", 1), ("employé", 0), ("sans emploi", 0), ("étudiant", 0)]


def instant(texte):
    return dt.datetime.strptime(texte, "%Y-%m-%d %H:%M")


def annonces():
    return lire_csv(ANNONCES)


def reponses():
    return lire_csv(REPONSES)


def pertinence(metier):
    m = (metier or "").lower()
    return next((v for k, v in PERTINENCE if k in m), 0)


def creer_repondant(figurant, simule=False):
    """Appelle le générateur (zone Abidjan) ; renvoie (nom, ligne de description)."""
    cmd = [sys.executable, str(OUTILS / "personnage.py"), "nouveau", "--contexte", "candidat_annonce_abidjan", "--role", "répondant à l'annonce"]
    if figurant:
        cmd.append("--figurant")
    if simule:
        cmd.append("--simule")
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", cwd=str(RACINE))
    texte = r.stdout + r.stderr
    m = re.match(r"\s*(.+?) — ", texte)
    if r.returncode or not m:
        sys.exit("personnage.py nouveau a échoué : " + texte[:300])
    return m.group(1).strip(), texte


def tirer(jusqua, simule=False):
    import jet
    lignes_a = annonces()
    resultats = []
    for a in lignes_a:
        if a["etat"] != "en_ligne":
            continue
        debut = instant(a["traitee_jusqua"] or a["publiee_le"])
        fin = instant(jusqua)
        if fin <= debut:
            continue
        publiee = instant(a["publiee_le"])
        cur = debut
        while cur < fin:
            suivant = min(cur + dt.timedelta(hours=1), fin)
            frac = (suivant - cur).total_seconds() / 3600
            heures = (cur - publiee).total_seconds() / 3600
            nuit = 0.2 if 1 <= cur.hour < 7 else 1.0  # Abidjan a deux heures de moins qu'au Luxembourg : peu de monde entre 23 h et 5 h, heure d'Abidjan
            p = min(0.95, TAUX.get(a["plateforme"], 0.2) * frac * nuit * (0.85 ** max(0, heures)))  # le flux décroît avec l'âge de l'annonce
            r = jet.tirer_libre(f"Une personne répond à l'annonce sur {a['plateforme']} entre {cur:%H:%M} et {suivant:%H:%M}", p * 100, derogation=DEROGATION, simule=simule)
            if r["oui"]:
                minute = jet.tirer_libre(f"Minute d'arrivée de la réponse ({a['plateforme']}, {cur:%H:%M}-{suivant:%H:%M}) : minute = jet × durée / 100",
                                         50, procedure="minute dans une fenêtre d'une heure", simule=simule)
                quand = cur + dt.timedelta(minutes=round(minute["jet"] * (suivant - cur).total_seconds() / 60 / 100))
                resultats.append((a, quand))
            cur = suivant
        a["traitee_jusqua"] = jusqua
    sortie = []
    existants = reponses()
    for a, quand in sorted(resultats, key=lambda x: x[1]):
        arnaque = jet.tirer_libre(f"Le répondant de {quand:%H:%M} ({a['plateforme']}) est une arnaque aux frais d'avance (profil créé pour l'occasion)", ARNAQUE.get(a["plateforme"], 12),
                                  derogation=DEROGATION, simule=simule)["oui"]
        nom, desc = creer_repondant(figurant=arnaque, simule=simule)
        lignes_desc = desc.splitlines()
        metier = lignes_desc[2].split(" ; ")[0].strip() if len(lignes_desc) > 2 else ""
        if arnaque:
            niveau, profil, signaux = "C", "profil récent, expérience annoncée très élevée, aucune référence joignable", "demande de frais d'avance après l'accusé de réception"
        else:
            age = re.search(r"(\d+) ans", desc)
            age = int(age.group(1)) if age else 40
            pert = pertinence(metier)
            exp = jet.tirer_libre(f"Années d'expérience de {nom} dans le domaine : 3 + jet × (âge − 25 − 3) / 100", 50, procedure="années d'expérience d'un répondant", simule=simule)
            annees = int(3 + exp["jet"] * max(0, age - 25 - 3) / 100)
            refs = jet.tirer_libre(f"Les références de {nom} sont vérifiables", 60, derogation=DEROGATION, simule=simule)["oui"]
            if "gonflé son expérience" in desc:
                refs = False
            signaux = "" if refs else "références introuvables ou évasives"
            if pert >= 2 and annees >= 10 and refs:
                niveau = "A"
            elif pert >= 1:
                niveau = "B"
            else:
                niveau = "C"
            profil = f"{metier or 'métier non précisé'} · {annees} ans d'expérience · {age} ans · références {'vérifiables' if refs else 'non vérifiables'}"
        ligne = {"id": f"RA{len(existants) + len(sortie) + 1:03d}", "quand": f"{quand:%Y-%m-%d %H:%M}", "plateforme": a["plateforme"], "nom": nom,
                 "niveau": niveau, "profil": profil.replace(";", ","), "signaux": signaux.replace(";", ","), "note": "arnaque" if arnaque else ""}
        sortie.append(ligne)
    if not simule:
        ecrire_csv(ANNONCES, lignes_a, COL_A)
        ecrire_csv(REPONSES, existants + sortie, COL_R)
    return sortie


def reseau(nom, simule=False):
    """Réseau d'un répondant en clients potentiels (demande de William, 18/07/2041 : « évaluer à quel point son réseau est élevé en termes de clients potentiels,
    lui attribuer une note »). Cinq critères de l'agent IA : taille utile du réseau (30), pertinence pour le solaire (25), accès réel (20), fiabilité (15),
    disponibilité (10). Les valeurs se tirent une fois (jets libres avec dérogation consignée), puis le répondant les révèle par morceaux ; la note est celle de l'agent."""
    import jet
    import routines
    p = routines.personnage(nom)
    if any(l["nom"] == p["nom"] for l in lire_csv(RESEAUX)):
        sys.exit(f"Le réseau de {p['nom']} est déjà tiré (jamais rejoué) : python outils/annonces.py voir-reseau \"{p['nom']}\"")
    d = "réseau d'un répondant à une annonce publique : pas de table validée (proposition R6, revue du lundi 22/07/2041)"
    j = lambda lib: jet.tirer_libre(lib, 50, procedure="valeur d'un attribut de réseau (jet × 100)", simule=simule)["jet"]
    pert = pertinence(p.get("metier", ""))
    proprietaires = 4 + 4 * pert + int(j(f"{p['nom']} : nombre de propriétaires ou d'entreprises qu'il ou elle peut présenter (4 + 4 × pertinence du métier + jet × 0,36)") * 0.36)
    decideurs = int(30 + 5 * pert + j(f"{p['nom']} : part joignable jusqu'au décideur (30 + 5 × pertinence + jet × 0,5 %)") * 0.5)
    factures = int(20 + 5 * pert + j(f"{p['nom']} : part dont la facture d'électricité est élevée (20 + 5 × pertinence + jet × 0,4 %)") * 0.4)
    intros = int(j(f"{p['nom']} : introductions déjà faites dans un projet comparable (jet / 25)") / 25)
    motivation = round(0.5 + j(f"{p['nom']} : motivation et disponibilité (0,5 + jet / 200)") / 200, 2)
    oubli = 0
    m = re.search(r"oubli (\d+) %", p.get("traits", "")) 
    if m:
        oubli = int(m.group(1))
    eff = proprietaires * decideurs / 100 * factures / 100
    pts = {"réseau utile": 30 * min(1, eff / 10), "pertinence solaire": 25 * min(1, factures / 60), "accès réel": 20 * (0.3 + 0.7 * min(intros, 3) / 3),
           "fiabilité": 15 * (1 - oubli / 100) * 0.9, "disponibilité": 10 * motivation}
    note = int(round(sum(pts.values())))
    ligne = {"nom": p["nom"], "proprietaires": proprietaires, "decideurs_pct": decideurs, "factures_pct": factures, "intros": intros, "motivation": motivation,
             "note": note, "detail": " · ".join(f"{k} {v:.0f}" for k, v in pts.items())}
    if not simule:
        ecrire_csv(RESEAUX, lire_csv(RESEAUX) + [ligne], COL_N)
    return ligne


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("liste")
    p = sp.add_parser("tirer")
    p.add_argument("--jusqua", required=True)
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("reseau")
    p.add_argument("nom")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("voir-reseau")
    p.add_argument("nom")
    p = sp.add_parser("reponses")
    p.add_argument("--depuis")
    sp.add_parser("verifier")
    args = ap.parse_args()
    if args.cmd == "liste":
        for a in annonces():
            print(f"{a['id']} {a['plateforme']:<15} publiée {a['publiee_le']} · {a['etat']} · traitée jusqu'au {a['traitee_jusqua']} · {a['note']}")
    elif args.cmd == "tirer":
        sortie = tirer(args.jusqua, args.simule)
        print(f"{len(sortie)} réponse(s) tirée(s) jusqu'au {args.jusqua}" + (" (essai : rien d'écrit)" if args.simule else ""))
        for l in sortie:
            print(f"  {l['id']} {l['quand']} {l['plateforme']:<15} {l['niveau']} {l['nom']} : {l['profil']}" + (f" · {l['signaux']}" if l["signaux"] else ""))
    elif args.cmd == "reseau":
        l = reseau(args.nom, args.simule)
        print(f"{l['nom']} : {l['proprietaires']} propriétaires ou entreprises, {l['decideurs_pct']} % joints jusqu'au décideur, {l['factures_pct']} % à facture élevée, {l['intros']} introduction(s) déjà faite(s), motivation {l['motivation']} -> note {l['note']}/100 ({l['detail']})" + (" (essai : rien d'écrit)" if args.simule else ""))
    elif args.cmd == "voir-reseau":
        for l in lire_csv(RESEAUX):
            if l["nom"] == args.nom:
                print(l)
    elif args.cmd == "reponses":
        for l in reponses():
            if not args.depuis or l["quand"] >= args.depuis:
                print(f"{l['id']} {l['quand']} {l['plateforme']:<15} {l['niveau']} {l['nom']} : {l['profil']}" + (f" · {l['signaux']}" if l["signaux"] else ""))
    else:
        ok = True
        for a in annonces():
            if a["etat"] not in ("en_ligne", "moderation", "refusee", "en_attente", "bloque"):
                ok = False
                print("état inconnu :", a)
        print("annonces.csv : conforme" if ok else "annonces.csv : à corriger")
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
