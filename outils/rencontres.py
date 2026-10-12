"""APPLICATION DE RENCONTRE du téléphone de William (créée le 12/10/2026 à la demande de l'utilisateur : « une application de
rencontre aux Philippines, pour rencontrer des femmes philippines »). Affichage : `outils/telephone_web/rencontres.js`.

    python outils/rencontres.py generer --ville MNL --nombre 24 [--simule]   # profils tirés par personnage.py (une fois par ville)
    python outils/rencontres.py completer --ville MNL --de 18 --a 20 [--simule]  # tranche d'âge ouverte après coup : vivier complété
    python outils/rencontres.py inscription --bio "…" --quand "AAAA-MM-JJ HH:MM" [--abonnement plus]
    python outils/rencontres.py aimer <id> --quand "…"          # William aime un profil (la suite se tire en T21, à valider)
    python outils/rencontres.py passer <id>
    python outils/rencontres.py match <id> --quand "…"          # le moteur enregistre un match tiré en T21
    python outils/rencontres.py message <id> --auteur william|profil --texte "…" --quand "…"
    python outils/rencontres.py liste | voir <id>

RÈGLES : chaque profil est une personne tirée par `personnage.py` (contexte `appli_rencontre_manille` : femmes de 18 ans au moins,
majorité aux Philippines, F058 ; garde absolue AGE_MIN, CLAUDE.md §11 limite b ; avant : 21 ans, marge du moteur → maintenant :
18 ans, demande de l'utilisateur du 12/10/2026), inscrite dans `etat/personnages.csv` (statut pre_genere, puis figurant ou récurrent
quand elle entre vraiment en scène). L'application montre ce qu'un vrai profil montre (prénom, âge, quartier, métier, ce qu'elle
cherche, une courte présentation en anglais) ; l'INTENTION réelle (relation sérieuse, aventure, amitié, aide financière attendue,
travail du sexe, faux profil) est tirée à la création et reste cachée (moteur seulement) : elle sert de modificateur aux réactions,
qui se tirent dans les tables (T21 pour un « j'aime » ou un premier message, à valider par l'utilisateur ; T20b pour une proposition
d'argent ; T10 pour l'heure d'une réponse). Rien n'est explicite ; les échanges se jouent comme le reste de la simulation.
Fichiers : `etat/rencontres.csv` (profils et statuts), `etat/rencontres-messages.csv` (discussions), `etat/rencontres-compte.csv`
(inscription de William).
"""
import argparse
import datetime as dt
import random
import sys

from commun import ETAT, OUTILS, ecrire_csv, lire_csv, maintenant_simule, slug, utf8

sys.path.insert(0, str(OUTILS))
PROFILS = ETAT / "rencontres.csv"
MESSAGES = ETAT / "rencontres-messages.csv"
COMPTE = ETAT / "rencontres-compte.csv"
COL_P = ["id", "ville", "prenom", "quartier", "distance_km", "metier", "cherche", "bio", "connexion", "verifie", "intention", "statut",
         "cree_le", "note"]
COL_M = ["profil", "date", "heure", "auteur", "texte"]
COL_C = ["inscrit_le", "ville", "bio", "recherche", "abonnement", "note"]
QUARTIERS = {"MNL": [("Makati", 2, 6), ("Bonifacio Global City (Taguig)", 3, 7), ("Pasay", 5, 9), ("Mandaluyong", 4, 8),
                     ("Pasig", 7, 12), ("Quezon City", 10, 18), ("Ermita (Manille)", 6, 9), ("Malate (Manille)", 6, 9),
                     ("San Juan", 7, 10), ("Parañaque", 10, 15), ("Marikina", 14, 20), ("Las Piñas", 15, 22), ("Sampaloc (Manille)", 8, 12)]}
# ce qu'affiche le profil (« cherche ») et l'intention réelle cachée : estimations du moteur (12/10/2026), à corriger à la revue
CHERCHE = [("Une relation sérieuse", 40), ("On verra bien", 30), ("De nouveaux amis", 15), ("Quelque chose de léger", 15)]
INTENTIONS = {"Une relation sérieuse": [("serieux", 70), ("aide_financiere", 15), ("arnaque", 8), ("aventure", 7)],
              "On verra bien": [("aventure", 40), ("serieux", 30), ("aide_financiere", 15), ("travail_sexuel", 8), ("arnaque", 7)],
              "De nouveaux amis": [("amitie", 60), ("serieux", 15), ("aventure", 15), ("arnaque", 10)],
              "Quelque chose de léger": [("aventure", 55), ("travail_sexuel", 25), ("aide_financiere", 12), ("arnaque", 8)]}
FOYERS = [("vit seul(e)", 45), ("vit chez ses parents", 30), ("en colocation", 10), ("parent isolé", 10), ("en couple, sans enfant", 5)]
PRIX_PLUS = 24.99  # abonnement « Plus » (mode voyage) en 2040 : estimation (≈ 15 à 20 € par mois en 2026 pour ce type d'offre, × 1,35)
# Âge minimum des profils : la majorité aux Philippines (18 ans, RA 6809 de 1989 : F058). Garde absolue : aucun profil sans date de
# naissance ni de moins de 18 ans, ni dans les tirages ni dans le téléphone. Avant : 21 ans (marge de sécurité ajoutée par le moteur
# le 12/10/2026) → maintenant : 18 ans, demande de l'utilisateur du 12/10/2026 (« 18 ans est la majorité »).
AGE_MIN = 18


def lire(p):
    return lire_csv(p) if p.exists() else []


def pondere(rng, couples):
    total = sum(w for _, w in couples)
    x = rng.uniform(0, total)
    for v, w in couples:
        x -= w
        if x <= 0:
            return v
    return couples[-1][0]


def bio(rng, metier, loisirs, cherche):
    metiers_en = {"employée ou employé de centre d'appels": "Call center agent", "vendeur ou vendeuse en centre commercial": "Mall sales staff",
                  "infirmier ou infirmière": "Nurse", "enseignant ou enseignante": "Teacher", "employé(e) de banque ou de bureau": "Office worker",
                  "serveur ou serveuse": "Waitress", "comptable": "Accountant", "étudiant(e)": "Student",
                  "développeur ou développeuse, informatique": "Software developer",
                  "travailleur ou travailleuse indépendante (en ligne)": "Freelancer", "aide-soignant(e)": "Caregiver",
                  "chauffeur (VTC, jeepney)": "Driver", "sans emploi": "Between jobs", "employé(e) d'hôtel": "Hotel staff",
                  "ouvrier ou ouvrière": "Factory worker"}
    loisirs_en = {"karaoké (videoke) entre amis": "videoke nights", "centres commerciaux climatisés le week-end": "mall dates",
                  "basket de quartier": "basketball", "séries coréennes": "K-dramas", "messe du dimanche": "Sunday mass",
                  "cuisine": "cooking", "lecture": "books", "vélo": "biking", "jeux vidéo": "gaming", "musique": "music"}
    cherche_en = {"Une relation sérieuse": "Looking for something real.", "On verra bien": "Let's see where it goes.",
                  "De nouveaux amis": "New friends welcome.", "Quelque chose de léger": "Nothing too serious."}
    m = metiers_en.get(metier, metier.capitalize())
    l = [loisirs_en.get(x, None) for x in loisirs]
    l = [x for x in l if x]
    gouts = (" · " + ", ".join(l)) if l else ""
    ouverture = rng.choice(["", "Simple girl. ", "Coffee first. ", "God-fearing. ", "Laughs a lot. ", "Introvert-ish. "])
    return f"{ouverture}{m}{gouts}. {cherche_en[cherche]}".strip()


def generer(ville, nombre, simule=False, ages=None, complement=False):
    """Tire `nombre` profils pour `ville` ; `ages` (« 18-20 ») restreint la tranche ; `complement` autorise l'ajout à une ville déjà
    tirée (commande `completer` : les profils existants ne sont jamais retirés ni modifiés)."""
    import jet
    import personnage as P
    rng = random.SystemRandom()
    profils = lire(PROFILS)
    if any(p["ville"] == ville for p in profils) and not simule and not complement:
        sys.exit(f"Des profils existent déjà pour {ville} : on ne retire jamais une ville (règle : un tirage est définitif).")
    registre = P.lire()
    existants = [l["nom"] for l in registre]
    jour = P.aujourd_hui()
    nouveaux = []
    for _ in range(nombre):
        pers = P.tirer("appli_rencontre_manille", "profil d'application de rencontre (Manille)", sexe="F", ages=ages, rng=rng,
                       existants=existants, foyers=FOYERS)
        existants.append(pers["nom"])
        if pers["age"] < AGE_MIN:  # garde absolue (majorité)
            continue
        cherche = pondere(rng, CHERCHE)
        intention = pondere(rng, INTENTIONS[cherche])
        q, dmin, dmax = rng.choice(QUARTIERS[ville])
        nouveaux.append((pers, {"id": slug(pers["nom"]), "ville": ville, "prenom": pers["prenom"], "quartier": q,
                                "distance_km": str(rng.randint(dmin, dmax)), "metier": pers["metier"], "cherche": cherche,
                                "bio": bio(rng, pers["metier"], pers["loisirs"], cherche),
                                "connexion": pondere(rng, [("en ligne", 15), ("il y a 1 h", 20), ("aujourd'hui", 35), ("hier", 20), ("cette semaine", 10)]),
                                "verifie": "oui" if rng.random() < 0.55 else "non", "intention": intention, "statut": "nouveau",
                                "cree_le": f"{jour:%Y-%m-%d}", "note": ""}))
    for pers, prof in nouveaux:
        print(f"  {prof['prenom']:12s} {pers['age']:>2} ans · {prof['quartier']} · {prof['metier']} · « {prof['cherche']} » "
              f"(intention cachée : {prof['intention']})")
    if simule:
        print(f"(essai : {len(nouveaux)} profil(s), rien n'est écrit)")
        return nouveaux
    for pers, prof in nouveaux:
        registre.append(P.ligne_registre(pers, "pre_genere", "", cercle="4",
                                         note=f"profil de l'application de rencontre ({ville}) · intention cachée : {prof['intention']}"))
        jet.consigner_json({"mode": "profil_rencontre", "libelle": f"profil de rencontre {prof['prenom']} ({ville})", "pour": pers["nom"],
                            "issue": prof["intention"], "distribution": {"cherche": prof["cherche"], "quartier": prof["quartier"]}})
    ecrire_csv(P.REGISTRE, registre, P.COLONNES)
    ecrire_csv(PROFILS, profils + [p for _, p in nouveaux], COL_P)
    print(f"{len(nouveaux)} profil(s) écrit(s) : etat/rencontres.csv et etat/personnages.csv (statut pre_genere)")
    return nouveaux


def part_tranche(ctx, a_min, a_max):
    """Part des âges a_min à a_max (inclus) dans le tirage du contexte, qui vaut int(triangular(age_min, age_max + 1, age_mode))."""
    lo, hi, mode = int(ctx["age_min"]), int(ctx["age_max"]) + 1, int(ctx["age_mode"])

    def repartition(x):
        if x <= lo:
            return 0.0
        if x >= hi:
            return 1.0
        if x <= mode:
            return (x - lo) ** 2 / ((hi - lo) * (mode - lo))
        return 1 - (hi - x) ** 2 / ((hi - lo) * (hi - mode))
    return repartition(a_max + 1) - repartition(a_min)


def completer(ville, a_min, a_max, simule=False):
    """Une tranche d'âge s'ouvre après coup (12/10/2026 : âge minimum ramené de 21 à 18 ans à la demande de l'utilisateur). Les
    profils déjà tirés restent tels quels (un tirage est définitif) ; on ajoute le nombre de profils que la tranche aurait eus si
    elle avait été ouverte dès le départ : n × p / (1 − p), où n est le nombre de profils existants de la ville et p la part de la
    tranche dans la loi d'âge du contexte ; la partie décimale se joue au dé (consigné)."""
    import jet
    import personnage as P
    if a_min < AGE_MIN:
        sys.exit(f"REFUSÉ : aucun profil de moins de {AGE_MIN} ans (majorité, garde absolue).")
    ctx = P.contextes()["appli_rencontre_manille"]
    if a_min < int(ctx["age_min"]):
        sys.exit(f"La tranche {a_min}-{a_max} commence sous l'âge minimum du contexte ({ctx['age_min']} ans).")
    n = sum(1 for p in lire(PROFILS) if p["ville"] == ville)
    p = part_tranche(ctx, a_min, a_max)
    attendu = n * p / (1 - p)
    base = int(attendu)
    jet_ = random.SystemRandom().uniform(0, 100)
    nombre = base + (1 if jet_ < (attendu - base) * 100 else 0)
    ligne = (f"- Complément du vivier de l'application de rencontre ({ville}, tranche {a_min}-{a_max} ans ouverte après coup) : "
             f"{n} profils existants, part de la tranche {p:.2%}, attendu {attendu:.2f} → {base} + jet {jet_:5.1f} contre "
             f"{(attendu - base) * 100:.1f} % → **{nombre} profil(s)**")
    print(ligne)
    if not simule:
        jet.consigner(ligne)
        jet.consigner_json({"mode": "complement_vivier", "libelle": f"complément du vivier {ville} {a_min}-{a_max} ans", "pour": "",
                            "proba": round((attendu - base) * 100, 2), "jet": round(jet_, 2), "issue": nombre,
                            "distribution": {"existants": n, "part": round(p, 4), "attendu": round(attendu, 3)}})
    if nombre:
        return generer(ville, nombre, simule=simule, ages=f"{a_min}-{a_max}", complement=True)
    return []


def trouver(ident):
    profils = lire(PROFILS)
    for p in profils:
        if p["id"] == ident or p["prenom"].lower() == ident.lower():
            return profils, p
    sys.exit(f"Profil inconnu : {ident}")


def changer_statut(ident, statut, note=""):
    profils, p = trouver(ident)
    p["statut"] = statut
    if note:
        p["note"] = (p["note"] + " · " if p["note"] else "") + note
    ecrire_csv(PROFILS, profils, COL_P)
    return p


def donnees_telephone(t=None):
    """Ce que l'application montre : profils (sans intention), statuts, discussions, compte de William."""
    import personnage as P
    from commun import age
    t = t or maintenant_simule()
    jour = t.date()
    naissances = {slug(l["nom"]): l["naissance"] for l in P.lire()}
    compte = lire(COMPTE)
    msgs = lire(MESSAGES)
    profils = []
    for p in lire(PROFILS):
        if p["statut"] == "bloque":
            continue
        a = age(naissances[p["id"]], jour) if p["id"] in naissances else None
        if a is None or a < AGE_MIN:
            continue  # garde : jamais un profil sans âge vérifiable ni mineur
        profils.append({"id": p["id"], "prenom": p["prenom"], "age": a, "ville": p["ville"], "quartier": p["quartier"],
                        "distance": int(p["distance_km"]), "cherche": p["cherche"], "bio": p["bio"], "connexion": p["connexion"],
                        "verifie": p["verifie"] == "oui", "statut": p["statut"]})
    discussions = {}
    for m in msgs:
        if f"{m['date']} {m['heure']}" <= f"{t:%Y-%m-%d %H:%M}":
            discussions.setdefault(m["profil"], []).append({"date": m["date"], "heure": m["heure"], "moi": m["auteur"] == "william",
                                                             "texte": m["texte"]})
    return {"inscrit": bool(compte), "compte": compte[-1] if compte else None, "prix_plus": PRIX_PLUS, "profils": profils,
            "discussions": discussions, "villes": {"MNL": "Manille"}}


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("generer")
    p.add_argument("--ville", default="MNL")
    p.add_argument("--nombre", type=int, default=24)
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("completer")
    p.add_argument("--ville", default="MNL")
    p.add_argument("--de", type=int, required=True, help="âge le plus bas de la tranche ouverte (18 au moins)")
    p.add_argument("--a", type=int, required=True, help="âge le plus haut de la tranche ouverte")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("inscription")
    p.add_argument("--bio", required=True)
    p.add_argument("--ville", default="MNL")
    p.add_argument("--recherche", default="femmes de 18 à 40 ans")
    p.add_argument("--abonnement", choices=("gratuit", "plus"), default="gratuit")
    p.add_argument("--quand", required=True)
    for nom in ("aimer", "passer", "match", "bloquer"):
        p = sp.add_parser(nom)
        p.add_argument("id")
        p.add_argument("--quand")
        p.add_argument("--note", default="")
    p = sp.add_parser("message")
    p.add_argument("id")
    p.add_argument("--auteur", choices=("william", "profil"), required=True)
    p.add_argument("--texte", required=True)
    p.add_argument("--quand", required=True)
    sp.add_parser("liste")
    p = sp.add_parser("voir")
    p.add_argument("id")
    args = ap.parse_args()
    if args.cmd == "generer":
        generer(args.ville, args.nombre, args.simule)
        return 0
    if args.cmd == "completer":
        completer(args.ville, args.de, args.a, args.simule)
        return 0
    if args.cmd == "inscription":
        quand = dt.datetime.fromisoformat(args.quand)
        compte = lire(COMPTE)
        compte.append({"inscrit_le": f"{quand:%Y-%m-%d %H:%M}", "ville": args.ville, "bio": args.bio.replace(";", ","),
                       "recherche": args.recherche, "abonnement": args.abonnement, "note": ""})
        ecrire_csv(COMPTE, compte, COL_C)
        if args.abonnement == "plus":
            import echeancier
            import grand_livre as gl
            lignes = echeancier.lire()
            n = max(int(l["id"][1:]) for l in lignes) + 1
            lignes.append({"id": f"E{n:03d}", "libelle": "Application de rencontre : abonnement Plus (mode voyage)", "compte": "courant",
                           "montant": f"{-PRIX_PLUS:.2f}", "periodicite": "mensuel", "jour": str(quand.day), "mois": "", "heure": f"{quand:%H:%M}",
                           "debut": (quand.date() + dt.timedelta(days=28)).isoformat(), "fin": "", "statut": "actif",
                           "source": "estimation (offres comparables ≈ 15 à 20 €/mois en 2026, × 1,35)",
                           "note": f"souscrit le {quand:%d/%m/%Y} ; premier mois payé à l'inscription", "contrepartie": "", "pret": ""})
            ecrire_csv(echeancier.FICHIER, lignes, echeancier.COLONNES)
            livre = gl.lire()
            livre.append({"date": f"{quand:%Y-%m-%d}", "heure": f"{quand:%H:%M}", "compte": "courant", "montant": f"{-PRIX_PLUS:.2f}",
                          "type": "mouvement", "libelle": "Application de rencontre : abonnement Plus, premier mois", "reference": f"E{n:03d}-0"})
            gl.ecrire(livre)
            echeancier.prevoir(quand.date() + dt.timedelta(days=60))
        print(f"Inscription enregistrée ({args.ville}, {args.abonnement})")
        return 0
    if args.cmd in ("aimer", "passer", "match", "bloquer"):
        statut = {"aimer": "aime", "passer": "passe", "match": "match", "bloquer": "bloque"}[args.cmd]
        p = changer_statut(args.id, statut, (f"{args.cmd} le {args.quand} " if args.quand else "") + args.note)
        print(f"{p['prenom']} : {statut}" + (" (la suite se tire en T21 : réaction à un « j'aime »)" if statut == "aime" else ""))
        return 0
    if args.cmd == "message":
        profils, p = trouver(args.id)
        quand = dt.datetime.fromisoformat(args.quand)
        msgs = lire(MESSAGES)
        msgs.append({"profil": p["id"], "date": f"{quand:%Y-%m-%d}", "heure": f"{quand:%H:%M}", "auteur": args.auteur,
                     "texte": args.texte.replace(";", ",")})
        ecrire_csv(MESSAGES, msgs, COL_M)
        if p["statut"] in ("match", "aime", "nouveau", "vu"):
            p["statut"] = "conversation"
            ecrire_csv(PROFILS, profils, COL_P)
        print(f"Message enregistré ({args.auteur} → {p['prenom']})")
        return 0
    if args.cmd == "liste":
        for p in lire(PROFILS):
            print(f"{p['id']:28s} {p['prenom']:12s} {p['quartier']:30s} {p['statut']:12s} « {p['cherche']} » [{p['intention']}]")
        return 0
    profils, p = trouver(args.id)
    for k in COL_P:
        print(f"{k:12s} {p[k]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
