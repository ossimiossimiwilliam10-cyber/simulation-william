"""APPLICATION DE RENCONTRE du téléphone de William (créée le 12/10/2026 à la demande de l'utilisateur : « une application de
rencontre aux Philippines, pour rencontrer des femmes philippines »). Affichage : `outils/telephone_web/rencontres.js`.

    python outils/rencontres.py generer --ville SEL --nombre 24 [--simule]   # profils tirés par personnage.py (une fois par ville)
    python outils/rencontres.py completer --ville SEL --de 20 --a 22 [--simule]  # tranche d'âge ouverte après coup : vivier complété
    python outils/rencontres.py inscription --bio "…" --quand "AAAA-MM-JJ HH:MM" [--abonnement plus]
    python outils/rencontres.py aimer <id> --quand "…"          # William aime un profil : T21a et T10 tirés tout seuls (reactions.py)
    python outils/rencontres.py passer <id>
    python outils/rencontres.py match <id> --quand "…"          # le moteur enregistre un match tiré en T21
    python outils/rencontres.py message <id> --auteur william|profil --texte "…" --quand "…" [--m47] [--sans-reaction]
Depuis le 14/10/2026 : un « j'aime » ou un message de William déclenche tout seul la réaction du profil (T21a ou T21b, avec M45,
M46 et M48 selon l'intention cachée ; --m47 si le message est sexuel ou propose de l'argent d'emblée), son heure (T10 et horaires
de vie) et la programmation (actions.py, agenda « à écrire ») ; le message de William s'ajoute au dossier des traces.
    python outils/rencontres.py liste | voir <id>
    python outils/rencontres.py likes-recus --jour AAAA-MM-JJ [--simule]   # T21c (14/10/2026) : « j'aime » reçus ce jour-là
    python outils/rencontres.py menage --lundi AAAA-MM-JJ [--simule]       # T21d (14/10/2026) : matchs sans échange depuis 7 jours
Depuis le 14/10/2026 (P23, P25, validées) : chaque jour où William est inscrit, des profils l'aiment d'eux-mêmes (T21c, lancé par
monde_vivant.py) ; ils restent parmi les profils à découvrir (l'application montre seulement leur nombre) et un « j'aime » de
William sur l'un d'eux fait un match immédiat ; la pile « à découvrir » est complétée à 6 profils (nouvelles inscrites) ;
chaque semaine, un match resté sans échange depuis 7 jours peut disparaître (T21d).

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
         "cree_le", "note", "aime_william"]  # aime_william (14/10/2026) : date et heure de son « j'aime » spontané (T21c)
PILE_MIN = 12  # profils « à découvrir » au moins, hors profils qui ont aimé William (estimation du moteur, 14/10/2026 ; avant : 6 → maintenant : 12, pour que ceux qui l'ont aimé restent une minorité de la pile)
NL = chr(10)
VILLES_ASIE_SE = {"MNL", "SEL"}  # M101 : étranger aisé dans une ville d'Asie (Séoul ajouté le 22/10/2026)
CONTEXTES = {"MNL": "appli_rencontre_manille", "SEL": "appli_rencontre_seoul"}  # contexte de personnage.py de chaque ville
NOMS_VILLES = {"MNL": "Manille", "SEL": "Séoul"}
COL_M = ["profil", "date", "heure", "auteur", "texte"]
COL_C = ["inscrit_le", "ville", "bio", "recherche", "abonnement", "note"]
QUARTIERS = {"MNL": [("Makati", 2, 6), ("Bonifacio Global City (Taguig)", 3, 7), ("Pasay", 5, 9), ("Mandaluyong", 4, 8),
                     ("Pasig", 7, 12), ("Quezon City", 10, 18), ("Ermita (Manille)", 6, 9), ("Malate (Manille)", 6, 9),
                     ("San Juan", 7, 10), ("Parañaque", 10, 15), ("Marikina", 14, 20), ("Las Piñas", 15, 22), ("Sampaloc (Manille)", 8, 12)],
             "SEL": [("Hongdae (Mapo-gu)", 1, 4), ("Mangwon-dong (Mapo-gu)", 1, 3), ("Sinchon", 2, 4), ("Seongsu-dong", 8, 12),
                     ("Gangnam", 11, 17), ("Itaewon", 5, 9), ("Jongno", 5, 8), ("Yeouido", 6, 10), ("Seodaemun", 3, 6),
                     ("Konkuk University (Gwangjin)", 10, 14), ("Songpa", 14, 20), ("Guro", 12, 18), ("Gwanak", 11, 16)]}
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


def bio(rng, metier, loisirs, cherche, ville="MNL"):
    metiers_en = {"employée ou employé de centre d'appels": "Call center agent", "vendeur ou vendeuse en centre commercial": "Mall sales staff",
                  "infirmier ou infirmière": "Nurse", "enseignant ou enseignante": "Teacher", "employé(e) de banque ou de bureau": "Office worker",
                  "serveur ou serveuse": "Waitress", "comptable": "Accountant", "étudiant(e)": "Student",
                  "développeur ou développeuse, informatique": "Software developer",
                  "travailleur ou travailleuse indépendante (en ligne)": "Freelancer", "aide-soignant(e)": "Caregiver",
                  "chauffeur (VTC, jeepney)": "Driver", "sans emploi": "Between jobs", "employé(e) d'hôtel": "Hotel staff",
                  "ouvrier ou ouvrière": "Factory worker",
                  "employé(e) de bureau (grande entreprise)": "Office worker", "serveur ou serveuse, barista": "Barista",
                  "vendeur ou vendeuse en grand magasin ou boutique": "Retail staff", "ingénieur(e) ou développeur(se), informatique": "Developer",
                  "fonctionnaire ou employé(e) d'administration": "Civil servant", "enseignant(e) (collège, lycée ou hagwon)": "Teacher",
                  "infirmier(ère) ou aide-soignant(e)": "Nurse", "travailleur(se) indépendant(e) (design, contenu en ligne)": "Freelancer",
                  "chauffeur (taxi, livraison)": "Driver", "cadre d'entreprise": "Manager", "employé(e) d'hôtel ou de restauration": "Hotel staff"}
    loisirs_en = {"karaoké (videoke) entre amis": "videoke nights", "centres commerciaux climatisés le week-end": "mall dates",
                  "basket de quartier": "basketball", "séries coréennes": "K-dramas", "messe du dimanche": "Sunday mass",
                  "cuisine": "cooking", "lecture": "books", "vélo": "biking", "jeux vidéo": "gaming", "musique": "music",
                  "karaoké (noraebang) entre amis": "noraebang", "cafés à thème et expositions": "cafés and exhibitions",
                  "randonnée sur les montagnes autour de Séoul (Bukhansan, Inwangsan)": "hiking", "jeux vidéo dans un PC bang": "gaming",
                  "bains publics (jjimjilbang) le week-end": "jjimjilbang"}
    cherche_en = {"Une relation sérieuse": "Looking for something real.", "On verra bien": "Let's see where it goes.",
                  "De nouveaux amis": "New friends welcome.", "Quelque chose de léger": "Nothing too serious."}
    m = metiers_en.get(metier, metier.capitalize())
    l = [loisirs_en.get(x, None) for x in loisirs]
    l = [x for x in l if x]
    gouts = (" · " + ", ".join(l)) if l else ""
    ouverture = rng.choice(["", "Coffee addict. ", "Cat person. ", "Foodie. ", "Weekend hiker. ", "Introvert-ish. "] if ville == "SEL"
                           else ["", "Simple girl. ", "Coffee first. ", "God-fearing. ", "Laughs a lot. ", "Introvert-ish. "])
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
        pers = P.tirer(CONTEXTES[ville], f"profil d'application de rencontre ({NOMS_VILLES[ville]})", sexe="F", ages=ages, rng=rng,
                       existants=existants, foyers=FOYERS)
        existants.append(pers["nom"])
        if pers["age"] < AGE_MIN:  # garde absolue (majorité)
            continue
        cherche = pondere(rng, CHERCHE)
        intention = pondere(rng, INTENTIONS[cherche])
        q, dmin, dmax = rng.choice(QUARTIERS[ville])
        nouveaux.append((pers, {"id": slug(pers["nom"]), "ville": ville, "prenom": pers["prenom"], "quartier": q,
                                "distance_km": str(rng.randint(dmin, dmax)), "metier": pers["metier"], "cherche": cherche,
                                "bio": bio(rng, pers["metier"], pers["loisirs"], cherche, ville),
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
    ctx = P.contextes()[CONTEXTES[ville]]
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


def likes_recus(jour, simule=False):
    """T21c : « j'aime » reçus spontanément par William ce jour-là (s'il est inscrit) ; la pile « à découvrir » est d'abord
    complétée à PILE_MIN profils (nouvelles inscrites), puis les profils qui l'aiment y sont choisis au hasard."""
    import jet
    import reactions
    import routines
    compte = lire(COMPTE)
    if not compte or compte[-1]["inscrit_le"][:10] > jour.isoformat():
        return []
    c = compte[-1]
    ville = c["ville"]
    sortie = remplir_pile(ville, simule)
    mods = (["M100"] if c["abonnement"] == "plus" else []) + (["M101"] if ville in VILLES_ASIE_SE else [])
    r = jet.tirer("T21c", mods, f"« J'aime » reçus par William le {jour:%d/%m/%Y} ({ville})", simule=simule, texte=False)
    n = {"aucun": 0, "un": 1, "deux": 2, "trois_ou_plus": 3}.get(r["issue"], 0)
    sortie.append(f"T21c : {r['issue']} (jet {r['jet']:.1f}{', ' + ', '.join(mods) if mods else ''})")
    if not n or simule:
        return sortie
    profils = lire(PROFILS)
    libres = [p for p in profils if p["ville"] == ville and p["statut"] in ("nouveau", "vu")]
    for p in random.SystemRandom().sample(libres, min(n, len(libres))):
        fiche = routines.personnage(p["id"])
        heure = fuseaux_local(reactions.minute_libre(fiche, jour, "07:00", "23:59"), fiche)
        reactions.procedure(f"{fiche['nom']} : heure de son « j'aime » spontané", f"{heure:%d/%m %H:%M}",
                            "horaires de vie (routines.py) · T21c", pour=fiche["nom"])
        p["statut"] = "vous_aime"
        p["aime_william"] = f"{heure:%Y-%m-%d %H:%M}"
        sortie.append(f"{p['prenom']} aime le profil de William ({heure:%d/%m %H:%M}) · intention cachée : {p['intention']}")
    ecrire_csv(PROFILS, profils, COL_P)
    return sortie


def remplir_pile(ville, simule=False):
    """Complète la pile « à découvrir » à PILE_MIN profils jamais vus (nouvelles inscrites, tirées par generer)."""
    pile = [p for p in lire(PROFILS) if p["ville"] == ville and p["statut"] in ("nouveau", "vu")]
    if len(pile) >= PILE_MIN or simule:
        return []
    n = PILE_MIN - len(pile)
    generer(ville, n, complement=True)
    return [f"{n} nouvelle(s) inscrite(s) dans la pile à découvrir"]


def fuseaux_local(instant, fiche):
    import fuseaux
    import routines
    return fuseaux.convertir(instant, routines.zone_de(fiche)).replace(tzinfo=None)


def menage(lundi, simule=False):
    """T21d : chaque semaine, un match resté sans aucun échange depuis 7 jours peut disparaître (retiré ou bloqué)."""
    import re
    import jet
    import routines
    profils = lire(PROFILS)
    parle = {m["profil"] for m in lire(MESSAGES)}
    sortie, change = [], False
    for p in profils:
        m = re.search(r"match le (\d{4}-\d{2}-\d{2})", p["note"])
        if p["statut"] != "match" or p["id"] in parle or not m or dt.date.fromisoformat(m.group(1)) > lundi - dt.timedelta(days=7):
            continue
        fiche = routines.personnage(p["id"])
        r = jet.tirer("T21d", [], f"{fiche['nom']} : match sans échange depuis le {m.group(1)}", pour=fiche["nom"], simule=simule,
                      texte=False)
        sortie.append(f"{p['prenom']} : T21d {r['issue']} (jet {r['jet']:.1f})")
        if r["issue"] in ("retire", "bloque") and not simule:
            p["statut"] = "match_retire" if r["issue"] == "retire" else "bloque"
            p["note"] = (p["note"] + " · " if p["note"] else "") + f"T21d : {r['issue']} (semaine du {lundi:%d/%m/%Y})"
            change = True
    if change:
        ecrire_csv(PROFILS, profils, COL_P)
    return sortie


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
    bloques = set()
    likes = 0
    for p in lire(PROFILS):
        if p["statut"] in ("bloque", "match_retire"):
            bloques.add(p["id"])  # bloqué ou match retiré : profil ET discussion disparaissent, comme dans une vraie application
            continue
        statut = p["statut"]
        if statut == "vous_aime":  # l'application ne dit pas qui : le profil reste « à découvrir », seul le nombre s'affiche
            statut = "nouveau"
            if (p.get("aime_william") or "9999") <= f"{t:%Y-%m-%d %H:%M}":
                likes += 1
        a = age(naissances[p["id"]], jour) if p["id"] in naissances else None
        if a is None or a < AGE_MIN:
            continue  # garde : jamais un profil sans âge vérifiable ni mineur
        profils.append({"id": p["id"], "prenom": p["prenom"], "age": a, "ville": p["ville"], "quartier": p["quartier"],
                        "distance": int(p["distance_km"]), "cherche": p["cherche"], "bio": p["bio"], "connexion": p["connexion"],
                        "verifie": p["verifie"] == "oui", "statut": statut})
    discussions = {}
    for m in msgs:
        if m["profil"] in bloques:
            continue
        if f"{m['date']} {m['heure']}" <= f"{t:%Y-%m-%d %H:%M}":
            discussions.setdefault(m["profil"], []).append({"date": m["date"], "heure": m["heure"], "moi": m["auteur"] == "william",
                                                             "texte": m["texte"]})
    return {"inscrit": bool(compte), "compte": {k: v for k, v in compte[-1].items() if k != "note"} if compte else None, "prix_plus": PRIX_PLUS, "profils": profils,
            "discussions": discussions, "villes": {"SEL": NOMS_VILLES["SEL"]}, "ville_defaut": "SEL",
            "age_min": int(P.contextes()[CONTEXTES["SEL"]]["age_min"]), "likes_recus": likes}


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("generer")
    p.add_argument("--ville", default="SEL")
    p.add_argument("--nombre", type=int, default=24)
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("completer")
    p.add_argument("--ville", default="SEL")
    p.add_argument("--de", type=int, required=True, help="âge le plus bas de la tranche ouverte (18 au moins)")
    p.add_argument("--a", type=int, required=True, help="âge le plus haut de la tranche ouverte")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("inscription")
    p.add_argument("--bio", required=True)
    p.add_argument("--ville", default="SEL")
    p.add_argument("--recherche", default="femmes de 20 à 40 ans")
    p.add_argument("--abonnement", choices=("gratuit", "plus"), default="gratuit")
    p.add_argument("--carte", default="visa_debit", help="carte qui paie l'abonnement Plus (etat/cartes.csv)")
    p.add_argument("--quand", required=True)
    for nom in ("aimer", "passer", "match", "bloquer"):
        p = sp.add_parser(nom)
        p.add_argument("id")
        p.add_argument("--quand")
        p.add_argument("--note", default="")
        p.add_argument("--sans-reaction", action="store_true", help="ne tire pas la réaction (aimer)")
    p = sp.add_parser("message")
    p.add_argument("id")
    p.add_argument("--auteur", choices=("william", "profil"), required=True)
    p.add_argument("--texte", required=True)
    p.add_argument("--quand", required=True)
    p.add_argument("--m47", action="store_true", help="message sexuel ou proposition d'argent d'emblée (modificateur M47)")
    p.add_argument("--sans-reaction", action="store_true", help="n'en tire pas la réaction (déjà tirée à part)")
    sp.add_parser("liste")
    p = sp.add_parser("voir")
    p.add_argument("id")
    p = sp.add_parser("likes-recus")
    p.add_argument("--jour", required=True)
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("pile")
    p.add_argument("--ville", default="SEL")
    p = sp.add_parser("menage")
    p.add_argument("--lundi", required=True)
    p.add_argument("--simule", action="store_true")
    args = ap.parse_args()
    if args.cmd == "likes-recus":
        print("\n".join(likes_recus(dt.date.fromisoformat(args.jour), args.simule)) or "(pas inscrit ce jour-là)")
        return 0
    if args.cmd == "pile":
        print(NL.join(remplir_pile(args.ville)) or f"pile déjà à {PILE_MIN} profils ou plus")
        return 0
    if args.cmd == "menage":
        print("\n".join(menage(dt.date.fromisoformat(args.lundi), args.simule)) or "aucun match sans échange depuis 7 jours")
        return 0
    if args.cmd == "generer":
        generer(args.ville, args.nombre, args.simule)
        return 0
    if args.cmd == "completer":
        completer(args.ville, args.de, args.a, args.simule)
        return 0
    if args.cmd == "inscription":
        quand = dt.datetime.fromisoformat(args.quand)
        if lire(COMPTE):  # garde (13/10/2026) : une inscription recopiée depuis le téléphone n'est jamais refaite
            print("Déjà inscrit (compte du " + lire(COMPTE)[-1]["inscrit_le"] + ") : rien n'est refait")
            return 0
        n = None
        if args.abonnement == "plus":
            # paiement du premier mois par carte (cartes.py, depuis le 13/10/2026) : plafond contrôlé ; refusé, pas d'inscription Plus
            import cartes
            import echeancier
            lignes = echeancier.lire()
            n = max(int(l["id"][1:]) for l in lignes) + 1
            ok, op = cartes.payer(args.carte, PRIX_PLUS, "Application de rencontre (abonnement Plus)", quand, reference=f"E{n:03d}-0")
            if not ok:
                print(f"PAIEMENT REFUSÉ ({op['id']}) : {op['note']} · inscription Plus non faite")
                return 2
            lignes.append({"id": f"E{n:03d}", "libelle": "Application de rencontre : abonnement Plus (mode voyage)", "compte": "courant",
                           "montant": f"{-PRIX_PLUS:.2f}", "periodicite": "mensuel", "jour": str(quand.day), "mois": "", "heure": f"{quand:%H:%M}",
                           "debut": (quand.date() + dt.timedelta(days=28)).isoformat(), "fin": "", "statut": "actif",
                           "source": "estimation (offres comparables ≈ 15 à 20 €/mois en 2026, × 1,35)",
                           "note": f"souscrit le {quand:%d/%m/%Y} ; premier mois payé à l'inscription par {cartes.carte(args.carte)['nom']} ({op['id']}) ; "
                                   "renouvellement mensuel sur la même carte", "contrepartie": "", "pret": ""})
            ecrire_csv(echeancier.FICHIER, lignes, echeancier.COLONNES)
            echeancier.prevoir(quand.date() + dt.timedelta(days=60))
        compte = lire(COMPTE)
        compte.append({"inscrit_le": f"{quand:%Y-%m-%d %H:%M}", "ville": args.ville, "bio": args.bio.replace(";", ","),
                       "recherche": args.recherche, "abonnement": args.abonnement, "note": f"échéancier E{n:03d}" if n else ""})
        ecrire_csv(COMPTE, compte, COL_C)
        print(f"Inscription enregistrée ({args.ville}, {args.abonnement})")
        return 0
    if args.cmd in ("aimer", "passer", "match", "bloquer"):
        _, avant = trouver(args.id)
        if args.cmd == "aimer" and avant["statut"] == "vous_aime" and (avant.get("aime_william") or "9999") <= (args.quand or "9999"):
            # elle l'avait déjà aimé (T21c) : match immédiat, sans nouveau tirage (14/10/2026)
            p = changer_statut(args.id, "match", f"match le {args.quand} (réciproque : elle l'avait aimé le {avant['aime_william']})")
            print(f"{p['prenom']} : match immédiat (elle avait aimé le profil de William le {avant['aime_william']})")
            return 0
        statut = {"aimer": "aime", "passer": "passe", "match": "match", "bloquer": "bloque"}[args.cmd]
        p = changer_statut(args.id, statut, (f"{args.cmd} le {args.quand} " if args.quand else "") + args.note)
        print(f"{p['prenom']} : {statut}")
        if args.cmd == "aimer" and not args.sans_reaction:
            import json
            import reactions
            print("  réaction :", json.dumps(reactions.like(p["id"], reactions.quand_arg(args.quand)), ensure_ascii=False))
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
        if args.auteur == "william":
            import json
            import reactions
            import traces
            traces.ajouter(f"{quand:%d/%m/%Y %Hh%M}", f"Message à {p['prenom']} sur l'application de rencontre : « {args.texte[:160]} »",
                           "historique de la discussion", f"l'éditeur de l'application · {p['prenom']} (captures possibles)", "faible",
                           etiquette=f"{quand:%d/%m/%Y, %Hh%M}")
            if not args.sans_reaction:
                r = reactions.message(p["id"], reactions.quand_arg(args.quand), args.texte, mods=["M47"] if args.m47 else [])
                print("  réaction :", json.dumps(r, ensure_ascii=False))
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
