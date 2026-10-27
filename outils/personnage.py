"""GÉNÉRATEUR ET REGISTRE DES PERSONNAGES (créé le 11/10/2026). Le moteur avait tendance à créer des personnages commodes,
disponibles, cohérents et tous de la même origine (règle 2 : « personnages ordinaires et imparfaits »). Ici, tout ce que le rôle
n'impose pas est TIRÉ au hasard dans des distributions sourcées (`donnees/population/`) : sexe, âge, origine et nationalité selon
la démographie réelle du lieu (Luxembourg-Ville, Esch, Audun-le-Tiche…), prénom selon la génération, langues, foyer, métier,
personnalité (cinq grands traits), attachement, défauts, qualité, contradiction, objectif, souci, secret, loisirs, fiabilité.

    python outils/personnage.py nouveau --contexte voisin_audun --role "voisine mitoyenne"
    python outils/personnage.py nouveau --contexte collegue_lycee --role "professeur de chimie" --sexe H --age 30-40
    python outils/personnage.py nouveau --contexte club_combat --role "entraîneur" --figurant      # figurant : registre seulement
    python outils/personnage.py nouveau --contexte eleve_lycee --role "élève de 2e" --simule        # essai, rien n'est écrit
    python outils/personnage.py promouvoir "Rui Ferreira"         # un figurant devient récurrent (fiche + vie propre)
    python outils/personnage.py liste [--statut pre_genere] | voir "Nom" | audit | contextes
    python outils/personnage.py completer "Nom" [--zone seoul] [--celibataire] [--simule]   # tire ce qui manque à un personnage écrit à la main
    python outils/personnage.py reseau --plan donnees/population/reseau-william.csv [--simule]   # entourage existant, en coulisse
    python outils/personnage.py apparait "Nom" --scene "salle des profs, 17/09"   # un pré-généré entre en scène (→ figurant)

STATUTS (depuis le 11/10/2026) : pre_genere (existe dans le monde, William le connaît dans la fiction, mais le JOUEUR ne l'a pas
encore rencontré : jamais montré, ni listé, ni nommé hors d'une scène ; demande de l'utilisateur : « j'aimerais bien les découvrir
au fil du jeu, mais tu peux déjà les mettre dans la base de données ») → figurant (est apparu dans une scène : `apparait`) →
recurrent (fiche, vie propre, tour du monde : `promouvoir`). Le tirage d'un pré-généré est définitif : à son apparition, le moteur
le joue tel qu'il a été tiré (secret, défauts, foyer compris), sans le retoucher pour la scène.

Écritures (sauf --simule) : `etat/personnages.csv` (registre de TOUS les personnages, avec date de naissance : garde « mineurs »
de jet.py --pour) ; pour un personnage récurrent : `personnes/<prenom-nom>.md` (fiche à compléter par le moteur), un bloc
« ### Prénom Nom (rôle) » dans `etat/vies-propres.md` (lu par tour_du_monde.py), son secret dans `etat/savoir.csv` ; le tirage
est consigné dans `memoire/tirages.jsonl` (on ne régénère jamais un personnage).
Le moteur ne fixe que ce que le RÔLE impose ; il écrit ensuite la scène avec ce qui a été tiré (test d'intérêt, règle 17).
La biographie de William (famille, amis de longue date, ex) n'est JAMAIS tirée ici sans l'accord de l'utilisateur.
MINEURS : un personnage de moins de 18 ans est marqué ; aucun champ amoureux, aucune table T1/T1b/T9 (jet.py le refuse).
"""
import argparse
import datetime as dt
import json
import random
import re
import sys

from commun import (DONNEES, ETAT, OUTILS, RACINE, ajouter_texte, age, ecrire_csv, ecrire_texte, lire_csv, lire_texte,
                    maintenant_simule, sans_accents, slug, utf8)

sys.path.insert(0, str(OUTILS))
POP = DONNEES / "population"
REGISTRE = ETAT / "personnages.csv"
COLONNES = ["id", "nom", "alias", "sexe", "naissance", "nationalite", "origine", "langues", "langue_avec_william", "registre",
            "commune", "metier", "employeur", "role", "contexte", "cercle", "statut", "fiche", "cree_le", "traits", "notes"]
VIES = ETAT / "vies-propres.md"

COHORTES = [(1940, 1964), (1965, 1984), (1985, 2004), (2005, 2022), (2023, 2035)]
MATIERES = ["mathématiques", "physique", "chimie", "biologie", "français", "allemand", "anglais", "luxembourgeois", "histoire",
            "géographie", "éducation physique", "informatique", "économie", "philosophie", "arts plastiques", "musique"]
METIERS_AUDUN = [("retraité(e) de la sidérurgie ou du commerce", 23), ("ouvrier ou ouvrière (frontalier au Luxembourg)", 21),
                 ("employé(e) de commerce ou de bureau", 18), ("technicien(ne), profession intermédiaire", 12),
                 ("cadre (frontalier)", 5), ("artisan ou commerçant", 5), ("aide-soignant(e) ou infirmier(ère)", 6),
                 ("sans emploi", 8), ("étudiant(e)", 2)]
METIERS_REGION = [("employé(e) de banque ou d'assurance", 10), ("ouvrier ou ouvrière du bâtiment", 10), ("informaticien(ne)", 8),
                  ("infirmier(ère) ou aide-soignant(e)", 8), ("vendeur ou vendeuse", 8), ("chauffeur ou livreur", 7),
                  ("comptable ou juriste", 6), ("étudiant(e) à Belval", 8), ("agent de sécurité", 5), ("cuisinier ou serveur", 7),
                  ("fonctionnaire ou employé(e) de l'État", 8), ("technicien(ne) de maintenance", 6), ("indépendant(e)", 5),
                  ("sans emploi", 4)]
METIERS_MANILLE = [("employée ou employé de centre d'appels", 14), ("vendeur ou vendeuse en centre commercial", 10),
                   ("infirmier ou infirmière", 7), ("enseignant ou enseignante", 6), ("employé(e) de banque ou de bureau", 9),
                   ("serveur ou serveuse", 7), ("comptable", 5), ("étudiant(e)", 6), ("développeur ou développeuse, informatique", 4),
                   ("travailleur ou travailleuse indépendante (en ligne)", 6), ("aide-soignant(e)", 4), ("chauffeur (VTC, jeepney)", 6),
                   ("sans emploi", 8), ("employé(e) d'hôtel", 5), ("ouvrier ou ouvrière", 4)]
METIERS_SEOUL = [("employé(e) de bureau (grande entreprise)", 18), ("étudiant(e)", 10), ("serveur ou serveuse, barista", 8),
                 ("vendeur ou vendeuse en grand magasin ou boutique", 9), ("ingénieur(e) ou développeur(se), informatique", 9),
                 ("fonctionnaire ou employé(e) d'administration", 6), ("enseignant(e) (collège, lycée ou hagwon)", 6),
                 ("infirmier(ère) ou aide-soignant(e)", 5), ("travailleur(se) indépendant(e) (design, contenu en ligne)", 8),
                 ("chauffeur (taxi, livraison)", 6), ("sans emploi", 5), ("cadre d'entreprise", 6), ("employé(e) d'hôtel ou de restauration", 4)]
METIERS_BRESIL = [("ingénieur(e) ou technicien(ne) (énergie, industrie)", 10), ("employé(e) de bureau ou de banque", 14),
                  ("commerçant(e) ou vendeur(se)", 14), ("entrepreneur(se) ou indépendant(e)", 12), ("enseignant(e)", 8),
                  ("comptable ou conseiller(ère) financier(ère)", 8), ("infirmier(ère) ou aide-soignant(e)", 6),
                  ("chauffeur (VTC, camion, livraison)", 8), ("agent immobilier ou courtier", 4), ("sans emploi", 7),
                  ("étudiant(e)", 6), ("fonctionnaire", 3)]
METIERS_ABIDJAN = [("ingénieur(e) en énergie, électricité ou bâtiment", 12), ("consultant(e) ou chef de projet", 10), ("enseignant(e)-chercheur(se) ou docteur(e)", 4),
                   ("cadre de banque, d'assurance ou d'entreprise", 14), ("commerçant(e) ou entrepreneur(se)", 16), ("comptable ou gestionnaire", 9),
                   ("technicien(ne) (installation, maintenance)", 8), ("agent immobilier ou promoteur", 4), ("employé(e) de bureau", 9),
                   ("sans emploi ou en recherche d'opportunités", 8), ("étudiant(e)", 3), ("fonctionnaire", 3)]
LOCALES = {"audun": ("française",), "manille": ("philippine",), "seoul": ("sud-coréenne",), "bresil": ("brésilienne",), "abidjan": ("ivoirienne",)}  # nationalités « d'ici » par zone (défaut : Luxembourg)
ROLES_F = ("directrice", "voisine", "boulangère", "vendeuse", "serveuse", "infirmière", "caissière", "coiffeuse", "banquière",
           "conseillère", "professeure", "entraîneuse", "avocate", "policière", "pharmacienne", "secrétaire générale", "mère",
           "sœur", "tante", "cousine", "fille", "épouse", "femme", "patronne", "gérante", "élève (fille)", "collègue (femme)")
ROLES_H = ("directeur", "voisin", "boulanger", "vendeur", "serveur", "infirmier", "caissier", "coiffeur", "banquier", "conseiller",
           "entraîneur", "avocat", "policier", "pharmacien", "père", "frère", "oncle", "cousin", "fils", "mari", "patron", "gérant",
           "élève (garçon)", "collègue (homme)")
METIER_DANS_ROLE = ("entraîneur", "entraîneuse", "coach", "gérant", "gérante", "patron", "patronne", "professeur", "médecin",
                    "pharmacien", "kiné", "boulanger", "boulangère", "vendeur", "vendeuse", "serveur", "serveuse", "caissier",
                    "caissière", "infirmier", "infirmière", "conseiller", "conseillère", "banquier", "banquière", "agent", "facteur",
                    "factrice", "mécanicien", "garagiste", "coiffeur", "coiffeuse", "avocat", "avocate", "notaire", "policier",
                    "policière", "secrétaire", "directeur", "directrice")
EXCLUS_ORIGINE_LU = ("apprendre le luxembourgeois", "obtenir la nationalité luxembourgeoise", "faire venir un proche resté au pays")
# prénoms des personnages principaux de l'univers 1 (archivé) : jamais réattribués, pour qu'aucun nom ne prête à confusion
PRENOMS_UNIVERS_1 = {"Sandra", "Kevin", "Aïcha", "Grace", "Yves", "Mariette", "Abdoul", "Ibrahim"}
SOUCIS_MINEUR = ["notes en baisse dans une matière", "conflit avec un parent", "timidité qui l'isole en classe",
                 "pression des examens", "séparation récente de ses parents", "moqueries sur les réseaux sociaux"]
OBJECTIFS_MINEUR = ["réussir son année", "changer de section", "trouver un petit boulot d'été", "entrer dans une équipe de sport",
                    "partir en échange linguistique"]


# ---------------------------------------------------------------- données
def table(nom):
    return lire_csv(POP / nom)


def contextes():
    return {c["contexte"]: c for c in table("contextes.csv")}


def pondere(rng, couples):
    total = sum(p for _, p in couples)
    x = rng.uniform(0, total)
    for v, p in couples:
        x -= p
        if x <= 0:
            return v
    return couples[-1][0]


def aujourd_hui():
    t = maintenant_simule()
    return t.date() if t else dt.date(2040, 7, 14)


def lire():
    return lire_csv(REGISTRE)


# ---------------------------------------------------------------- tirages élémentaires
def tirer_origine(rng, zone):
    lignes = [l for l in table("zones.csv") if l["zone"] == zone]
    if not lignes:
        sys.exit(f"Zone inconnue : {zone} (donnees/population/zones.csv)")
    origine = pondere(rng, [(l["origine"], float(l["poids"])) for l in lignes])
    part_lu = float(next(l["part_nationalite_lu"] for l in lignes if l["origine"] == origine) or 0)
    return origine, part_lu


def nationalite(rng, origine, part_lu, zone):
    lang = {l["origine"]: l for l in table("langues.csv")}
    if origine == "lu":
        return "luxembourgeoise"
    if zone == "audun":
        return "française" if origine == "fr" or rng.random() < 0.85 else lang.get(origine, {}).get("nationalite", "?")
    if rng.random() < part_lu:
        return f"luxembourgeoise (famille d'origine {origine})"
    return lang.get(origine, {}).get("nationalite", "?")


def cohorte(annee):
    for a, b in COHORTES:
        if a <= annee <= b:
            return f"{a}-{b}"
    return "1985-2004"


def tirer_prenom(rng, origine, sexe, annee, zone):
    prenoms = table("prenoms.csv")
    hote = {"audun": "fr", "manille": "ph", "seoul": "kr", "bresil": "br", "abidjan": "ci"}.get(zone, "lu")
    if origine not in (hote, "lu", "fr") and rng.random() < 0.25:
        origine = hote  # descendants : prénom du pays d'accueil
    voulu = cohorte(annee)

    def candidats(o):
        lignes = [l for l in prenoms if l["origine"] == o and l["sexe"] == sexe]
        exact = [l for l in lignes if l["cohorte"] == voulu]
        if exact:
            return exact[0]["prenoms"]
        if lignes:  # cohorte la plus proche
            cible = int(voulu[:4])
            return min(lignes, key=lambda l: abs(int(l["cohorte"][:4]) - cible))["prenoms"]
        return None

    liste = candidats(origine) or candidats("autres") or candidats("fr")
    noms = list(dict.fromkeys(x.strip() for x in liste.split(",") if x.strip()))
    return rng.choice(noms)


def tirer_nom(rng, origine):
    for l in table("noms.csv"):
        if l["origine"] == origine:
            return rng.choice([x.strip() for x in l["noms"].split(",") if x.strip()])
    return rng.choice([x.strip() for x in next(l for l in table("noms.csv") if l["origine"] == "autres")["noms"].split(",")])


def big_five(rng, sexe, age_ans):
    t = {k: rng.gauss(50, 10) for k in "OCEAN"}
    if sexe == "F":  # écarts moyens faibles à modérés (Costa et al. 2001 ; Schmitt et al. 2008)
        t["N"] += 4
        t["A"] += 3
    if age_ans > 30:  # maturation (Soto et al. 2011, ordre de grandeur)
        t["A"] += 0.15 * (age_ans - 30)
        t["C"] += 0.10 * (age_ans - 30)
        t["N"] -= 0.10 * (age_ans - 30)
    return {k: int(max(20, min(80, round(v)))) for k, v in t.items()}


def mot_trait(k, v):
    noms = {"O": ("très curieux, ouvert à la nouveauté", "plutôt curieux", "attaché à ses habitudes"),
            "C": ("très organisé et fiable", "assez sérieux", "désorganisé, peu ponctuel"),
            "E": ("très sociable, bavard", "sociable sans excès", "réservé, peu bavard"),
            "A": ("conciliant, chaleureux", "aimable", "méfiant, peu conciliant"),
            "N": ("anxieux, susceptible", "émotif par moments", "calme, peu inquiet")}
    return noms[k][0] if v >= 60 else noms[k][2] if v <= 40 else noms[k][1]


def situation(a, metier, foyer, nationalite, zone):
    """Ce que le catalogue doit respecter (12/10/2026 : un retraité de 74 ans tiré avec un « burn-out qui couve », un parent
    isolé avec un « couple en crise ») : âge, emploi, couple, enfants à charge, nationalité, pays de résidence."""
    m, f, nat = (metier or "").lower(), (foyer or "").lower(), (nationalite or "").lower()
    retraite, sans_emploi = "retraité" in m, "sans emploi" in m
    etudiant = "étudiant" in m or m == "élève"
    en_couple = "en couple" in f
    locales = LOCALES.get(zone, ("luxembourgeoise", "française"))
    return {"age": a, "retraite": retraite, "sans_emploi": sans_emploi, "actif": not (retraite or sans_emploi or etudiant),
            "en_couple": en_couple, "seul": not en_couple, "veuf": "veuf" in f,
            "parent": any(x in f for x in ("avec enfants", "enfants en bas âge", "parent isolé")),
            "immigre": not any(nat.startswith(x) for x in locales + ("luxembourgeoise",)
                             if zone not in ("manille", "seoul", "bresil", "abidjan") or x in LOCALES.get(zone, ())),
            "non_lu": not nat.startswith("luxembourgeoise"),
            "reside_lu": zone in ("luxembourg_ville", "esch", "lycee", "club_mma"),
            "europe": zone not in ("manille", "seoul", "bresil", "abidjan"), "manille": zone == "manille",
            "seoul": zone == "seoul", "bresil": zone == "bresil", "abidjan": zone == "abidjan"}


def convient(condition, s):
    """« actif,age:22-45 », « pas_veuf », « non_lu,reside_lu » : toutes les clauses doivent être vraies."""
    if not s:
        return True
    for c in (condition or "").split(","):
        c = c.strip()
        if not c:
            continue
        if c.startswith("age:"):
            lo, hi = (int(x) for x in c[4:].split("-"))
            if not lo <= s["age"] <= hi:
                return False
        elif c.startswith("pas_"):
            if s.get(c[4:]):
                return False
        elif not s.get(c):
            return False
    return True


def catalogue(rng, categorie, traits, n=1, exclus=(), situation_=None):
    lignes = [l for l in table("catalogues.csv") if l["categorie"] == categorie and l["element"] not in exclus
              and convient(l.get("condition"), situation_)]
    choix = []
    for _ in range(n):
        couples = []
        for l in lignes:
            if l["element"] in choix:
                continue
            p = float(l["poids"] or 1)
            for aff in (l["affinite"] or "").split(","):
                aff = aff.strip()
                if len(aff) == 2 and aff[0] in "OCEAN":
                    v = traits[aff[0]]
                    if (aff[1] == "+" and v >= 60) or (aff[1] == "-" and v <= 40):
                        p *= 2
            couples.append((l, p))
        if not couples:
            break
        choix.append(pondere(rng, couples)["element"])
    return choix


def gravite(element):
    l = next((x for x in table("catalogues.csv") if x["element"] == element), None)
    return int(l["gravite"]) if l and l.get("gravite", "").isdigit() else 1


def tirer_foyer(rng, a):
    if a < 18:
        return pondere(rng, [("vit chez ses deux parents", 60), ("vit chez un parent seul", 30), ("garde alternée", 10)])
    if a < 25:
        return pondere(rng, [("vit chez ses parents", 45), ("vit seul(e)", 25), ("en couple, sans enfant", 20), ("en colocation", 10)])
    if a < 35:
        return pondere(rng, [("vit seul(e)", 35), ("en couple, sans enfant", 30), ("en couple, enfants en bas âge", 20),
                             ("vit chez ses parents", 8), ("parent isolé", 7)])
    if a < 50:
        return pondere(rng, [("en couple, avec enfants", 45), ("vit seul(e)", 25), ("en couple, sans enfant", 15),
                             ("parent isolé", 12), ("en colocation", 3)])
    if a < 65:
        return pondere(rng, [("en couple, enfants partis", 40), ("en couple, avec enfants", 20), ("vit seul(e)", 30),
                             ("parent isolé", 10)])
    return pondere(rng, [("en couple", 45), ("veuf ou veuve, seul(e)", 50), ("vit chez un enfant", 5)])


def sexe_du_role(role):
    r = role.lower()
    mots = set(r.replace("(", " ").replace(")", " ").replace(",", " ").split())
    if any(x in r for x in ROLES_F if " " in x) or mots & {x for x in ROLES_F if " " not in x}:
        return "F"
    if any(x in r for x in ROLES_H if " " in x) or mots & {x for x in ROLES_H if " " not in x}:
        return "H"
    return None


def tirer_metier(rng, ctx, role, a):
    c = ctx["contexte"]
    if any(m in role.lower().split() or role.lower().startswith(m) for m in METIER_DANS_ROLE) and c != "collegue_lycee":
        return role, ("lycée de William" if c in ("direction_lycee", "secretariat_lycee") else "")
    if c == "collegue_lycee":
        if role.lower().startswith("professeur"):
            return role.split(" (")[0], "lycée de William"
        return f"professeur de {rng.choice(MATIERES)}", "lycée de William"
    if c == "direction_lycee":
        return role, "lycée de William"
    if c == "secretariat_lycee":
        return role, "lycée de William"
    if c == "eleve_lycee":
        return "élève", "lycée de William"
    if c in ("commerce_audun", "commerce_lux", "administration", "sante"):
        return role, ""
    if a >= 65:
        return "retraité(e)", ""
    # pas de retraité avant 58 ans (départs anticipés pour carrière longue au plus tôt), pas d'étudiant après 30 ans (12/10/2026)
    liste = [(m, p) for m, p in (METIERS_AUDUN if ctx["zone"] == "audun" else METIERS_MANILLE if ctx["zone"] == "manille" else METIERS_SEOUL if ctx["zone"] == "seoul"
             else METIERS_BRESIL if ctx["zone"] == "bresil" else METIERS_ABIDJAN if ctx["zone"] == "abidjan" else METIERS_REGION)
             if not (("retraité" in m and a < 58) or ("étudiant" in m and a >= 30))]
    return pondere(rng, liste), ""


def tirer_registre(rng, ctx, a):
    base = ctx["registre"]
    if base == "tu" and ctx["contexte"] == "collegue_lycee":
        return "tu" if rng.random() < 0.75 else "vous"
    if base == "vous" and ctx["contexte"] in ("voisin_audun", "rencontre") and a < 32:
        return "tu" if rng.random() < 0.5 else "vous"
    return base


def physique(rng, origine, sexe, ctx, a):
    lang = {l["origine"]: l for l in table("langues.csv")}.get(origine, {})
    moyenne = float(lang.get("taille_h" if sexe == "H" else "taille_f") or (176 if sexe == "H" else 163))
    if a < 16:
        moyenne -= 6 * (16 - a) / 4
    taille = int(round(rng.gauss(moyenne, 6.8 if sexe == "H" else 6.2)))
    sportif = ctx["contexte"] == "club_combat"
    corpulence = pondere(rng, [("mince", 22), ("moyenne", 45), ("enveloppée", 23 if not sportif else 5),
                               ("sportive, musclée", 10 if not sportif else 70)])
    signes = []
    if rng.random() < 0.35 + (0.25 if a > 45 else 0):
        signes.append("lunettes")
    if rng.random() < (0.45 if sportif else 0.18) and a >= 18:
        signes.append("tatouage visible")
    if sexe == "H" and a >= 18 and rng.random() < 0.4:
        signes.append("barbe")
    if rng.random() < 0.05:
        signes.append("cicatrice visible")
    return taille, corpulence, signes


def nom_trop_proche(prenom, nom, existants, strict=True):
    """Évite les homonymes, qui embrouillent le récit (11/10/2026 : trois « Goergen » et trois « Camille » sur 43 personnes) :
    même nom complet, ou même nom de famille avec la même initiale, toujours refusés ; en mode strict, aussi un nom de famille ou
    un prénom déjà porté par quelqu'un du registre (après 45 essais, le tirage l'accepte : un réservoir épuisé ne bloque rien)."""
    def norme(s):  # sans accents ni majuscules : « Léo » et « Leo » sont le même prénom pour le lecteur
        return sans_accents(s).lower()

    complet, pn, nn = norme(f"{prenom} {nom}"), norme(prenom), norme(nom)
    for e in existants:
        x = norme(e)
        if x == complet:
            return True
        if x.endswith(" " + nn) and x[0] == pn[0]:
            return True
        if strict and (x.endswith(" " + nn) or x.split()[0] == pn):
            return True
    return False


def tirer(contexte, role, sexe=None, ages=None, rng=None, existants=(), foyers=None):
    rng = rng or random.SystemRandom()
    ctxs = contextes()
    if contexte not in ctxs:
        sys.exit(f"Contexte inconnu : {contexte} ({', '.join(ctxs)})")
    ctx = ctxs[contexte]
    jour = aujourd_hui()
    sexe = sexe or sexe_du_role(role) or ("F" if rng.random() < float(ctx["part_femmes"]) else "H")
    if ages:
        a_min, a_max = (int(x) for x in ages.split("-"))
        a = int(rng.uniform(a_min, a_max + 1))
    else:
        a = int(rng.triangular(int(ctx["age_min"]), int(ctx["age_max"]) + 1, int(ctx["age_mode"])))
    naissance = jour - dt.timedelta(days=int(a * 365.2425 + rng.uniform(0, 364)))
    while age(naissance, jour) != a:
        naissance += dt.timedelta(days=1 if age(naissance, jour) > a else -1)
    zone = ctx["zone"]
    origine, part_lu = tirer_origine(rng, zone)
    nat = nationalite(rng, origine, part_lu, zone)
    for essai in range(60):
        prenom = tirer_prenom(rng, origine, sexe, naissance.year, zone)
        nom = tirer_nom(rng, origine)
        if prenom not in PRENOMS_UNIVERS_1 and not nom_trop_proche(prenom, nom, existants, strict=essai < 45):
            break
    traits = big_five(rng, sexe, a)
    attachement = pondere(rng, [("sécure", 56), ("évitant", 25), ("anxieux", 19)])  # Hazan et Shaver (1987)
    mineur = a < 18
    defauts = catalogue(rng, "defaut", traits, 2)
    qualite = catalogue(rng, "qualite", traits, 1)
    foyer = pondere(rng, foyers) if foyers else tirer_foyer(rng, a)  # foyers : distribution propre au contexte (ex. application de rencontre)
    metier, employeur = tirer_metier(rng, ctx, role, a)
    s = situation(a, metier, foyer, nat, zone)
    contradiction = catalogue(rng, "contradiction", traits, 1, situation_=s) if (not mineur and rng.random() < 0.5) else []
    if mineur:
        objectif, souci, secret, grav = [rng.choice(OBJECTIFS_MINEUR)], [rng.choice(SOUCIS_MINEUR)], [], 0
    else:
        objectif = catalogue(rng, "objectif", traits, 1, exclus=EXCLUS_ORIGINE_LU if origine == "lu" else (), situation_=s)
        souci = catalogue(rng, "souci", traits, 1, situation_=s)
        secret = catalogue(rng, "secret", traits, 1, situation_=s)
        grav = gravite(secret[0]) if secret else 0
    loisirs = catalogue(rng, "loisir", traits, 1 + (rng.random() < 0.5), situation_=s)
    oubli = max(0.03, min(0.30, 0.12 - (traits["C"] - 50) * 0.004))
    lang = {l["origine"]: l for l in table("langues.csv")}.get(origine, {})
    taille, corpulence, signes = physique(rng, origine, sexe, ctx, a)
    return {
        "prenom": prenom, "nom_famille": nom, "nom": f"{prenom} {nom}", "sexe": sexe, "age": a, "naissance": naissance.isoformat(),
        "mineur": mineur, "origine": origine, "nationalite": nat, "langues": lang.get("langues", ""),
        "langue_avec_william": lang.get("langue_avec_william", "français"), "registre": tirer_registre(rng, ctx, a),
        "commune": ctx["commune"], "metier": metier, "employeur": employeur, "role": role, "contexte": contexte,
        "traits": traits, "attachement": attachement, "defauts": defauts, "qualite": qualite, "contradiction": contradiction,
        "objectif": objectif, "souci": souci, "secret": secret, "gravite_secret": grav, "loisirs": loisirs, "oubli": oubli,
        "foyer": foyer, "taille": taille, "corpulence": corpulence, "signes": signes,
    }


# ---------------------------------------------------------------- écriture
def resume(p):
    t = p["traits"]
    lignes = [
        f"{p['nom']} — {p['role']} ({p['contexte']}) ; {'femme' if p['sexe'] == 'F' else 'homme'}, {p['age']} ans "
        f"({'née' if p['sexe'] == 'F' else 'né'} le {p['naissance']}){' — MINEUR(E)' if p['mineur'] else ''}",
        f"  origine {p['origine']} ; nationalité {p['nationalite']} ; langues : {p['langues']} ; avec William : {p['langue_avec_william']}, "
        f"« {p['registre']} »",
        f"  {p['metier']}{' (' + p['employeur'] + ')' if p['employeur'] else ''} ; {p['foyer']} ; {p['commune']}",
        f"  physique : {p['taille']} cm, corpulence {p['corpulence']}" + (f", {', '.join(p['signes'])}" if p['signes'] else ""),
        "  caractère : " + " ; ".join(mot_trait(k, t[k]) for k in "OCEAN") + f" ; attachement {p['attachement']}",
        f"  défauts : {' / '.join(p['defauts'])} ; qualité : {' / '.join(p['qualite'])}"
        + (f" ; contradiction : {p['contradiction'][0]}" if p['contradiction'] else ""),
        f"  objectif : {' / '.join(p['objectif'])} ; souci : {' / '.join(p['souci'])} ; loisirs : {' / '.join(p['loisirs'])}",
        f"  secret (fait caché) : {p['secret'][0] + ' (gravité ' + str(p['gravite_secret']) + ')' if p['secret'] else 'aucun'} ; "
        f"risque d'oubli ou d'annulation : {round(p['oubli'] * 100)} %",
    ]
    return "\n".join(lignes)


def ligne_registre(p, statut, fiche, cercle=None, note=""):
    t = p["traits"]
    traits = (f"O{t['O']} C{t['C']} E{t['E']} A{t['A']} N{t['N']} · attachement {p['attachement']} · défauts : "
              f"{' / '.join(p['defauts'])} · qualité : {' / '.join(p['qualite'])} · oubli {round(p['oubli'] * 100)} %")
    notes = (f"foyer : {p['foyer']} · objectif : {' / '.join(p['objectif'])} · souci : {' / '.join(p['souci'])} · loisirs : "
             f"{' / '.join(p['loisirs'])} · physique : {p['taille']} cm, {p['corpulence']}"
             + (f", {', '.join(p['signes'])}" if p['signes'] else "") + (" · MINEUR" if p["mineur"] else ""))
    if statut != "recurrent":  # le tirage complet reste dans le registre : la promotion le reprend tel quel (jamais de nouveau tirage)
        notes += (f" · secret : {p['secret'][0] + ' (gravité ' + str(p['gravite_secret']) + ')' if p['secret'] else 'aucun'}"
                  f" · contradiction : {p['contradiction'][0] if p['contradiction'] else 'aucune'}")
    if note:
        notes += f" · {note}"
    return {"id": slug(p["nom"]), "nom": p["nom"], "alias": "", "sexe": p["sexe"], "naissance": p["naissance"],
            "nationalite": p["nationalite"], "origine": p["origine"], "langues": p["langues"],
            "langue_avec_william": p["langue_avec_william"], "registre": p["registre"], "commune": p["commune"],
            "metier": p["metier"], "employeur": p["employeur"], "role": p["role"], "contexte": p["contexte"],
            "cercle": cercle or ("4" if statut == "figurant" else "3"), "statut": statut, "fiche": fiche,
            "cree_le": f"{aujourd_hui():%Y-%m-%d}", "traits": traits.replace(";", ","), "notes": notes.replace(";", ",")}


def ecrire_fiche(p):
    chemin = RACINE / "personnes" / f"{slug(p['nom'])}.md"
    t = p["traits"]
    texte = f"""# {p['nom']} — {p['role']}

> Fiche créée le {aujourd_hui():%d/%m/%Y} (simulation) par `outils/personnage.py` : les éléments ci-dessous ont été TIRÉS
> (registre : `etat/personnages.csv`). Le moteur complète la description au fil des scènes, sans contredire le tirage ;
> toute évolution s'écrit « avant → maintenant ».

## Identité
- {'Femme, née' if p['sexe'] == 'F' else 'Homme, né'} le {p['naissance']} ({p['age']} ans){' — **MINEUR(E)** : aucune scène ni table relationnelle (§11, b)' if p['mineur'] else ''}.
- Origine familiale : {p['origine']} ; nationalité : {p['nationalite']}.
- Langues : {p['langues']} ; avec William : {p['langue_avec_william']}, registre « {p['registre']} ».
- Vit à : {p['commune']} ; {p['foyer']}.
- Métier : {p['metier']}{' (' + p['employeur'] + ')' if p['employeur'] else ''}.

## Physique (graines tirées, à préciser dans la première scène)
- {p['taille']} cm, corpulence {p['corpulence']}{', ' + ', '.join(p['signes']) if p['signes'] else ''}.

## Caractère
- {' ; '.join(mot_trait(k, t[k]) for k in 'OCEAN')} ; attachement {p['attachement']}.
- Défauts : {' ; '.join(p['defauts'])}.
- Qualité : {' ; '.join(p['qualite'])}.{chr(10) + '- Contradiction : ' + p['contradiction'][0] + '.' if p['contradiction'] else ''}
- Fiabilité : environ {round(p['oubli'] * 100)} % de risque d'oubli ou d'annulation d'un rendez-vous ou d'une promesse.

## Vie propre
- Objectif : {' ; '.join(p['objectif'])}.
- Souci : {' ; '.join(p['souci'])}.
- Loisirs : {' ; '.join(p['loisirs'])}.
- Secret : {p['secret'][0] + ' (fait caché, gravité ' + str(p['gravite_secret']) + ' ; ne ressort que par un tirage ou une révélation consignée dans etat/savoir.csv)' if p['secret'] else 'aucun'}.

## Lien avec William
- Contexte : {p['contexte']} ; rôle : {p['role']}.

## Historique
- {aujourd_hui():%d/%m/%Y} : fiche créée (tirage du générateur).
"""
    ecrire_texte(chemin, texte)
    return chemin.relative_to(RACINE).as_posix()


def ecrire_vie_propre(p):
    texte = lire_texte(VIES).replace("\r\n", "\n")
    bloc = (f"### {p['nom']} ({p['role']})\n"
            f"- **Objectif du moment** : {' ; '.join(p['objectif'])}.\n"
            f"- **Souci en cours** : {' ; '.join(p['souci'])}.\n"
            f"- **Alliés et tensions** : à établir au fil du jeu.\n"
            f"- **Agenda de la semaine** : à établir.\n"
            f"- **Secret** : {p['secret'][0] + ' (tiré à la création)' if p['secret'] else 'aucun'}.\n"
            f"- **Modificateurs T11** : aucun\n"
            f"- **Modificateurs T13** : —\n"
            f"- **Modificateurs T14** : {'aucun' if p['contexte'] in ('collegue_lycee', 'club_combat', 'voisin_audun', 'direction_lycee') and not p['mineur'] else '—'}\n\n")
    if "## Liens entre personnages" in texte:
        texte = texte.replace("## Liens entre personnages", bloc + "## Liens entre personnages", 1)
    else:
        texte += "\n" + bloc
    ecrire_texte(VIES, texte)


def ecrire_secret(p):
    if not p["secret"]:
        return
    import savoir
    lignes = savoir.lire()
    fait = f"secret_{slug(p['nom']).replace('-', '_')}"
    if not any(l["fait"] == fait and l["personne"] == p["nom"] for l in lignes):
        lignes.append({"fait": fait, "personne": p["nom"], "canal": "propre", "date": f"{aujourd_hui():%Y-%m-%d}",
                       "note": p["secret"][0]})
        savoir.ecrire(lignes)


def consigner(p, statut):
    import jet
    jet.consigner_json({"mode": "personnage", "libelle": f"création de {p['nom']} ({p['role']})", "pour": p["nom"],
                        "issue": statut, "distribution": {k: (v if not isinstance(v, set) else list(v)) for k, v in p.items()}})


# ---------------------------------------------------------------- commandes
def cmd_nouveau(args):
    existants = [l["nom"] for l in lire()]
    p = tirer(args.contexte, args.role, args.sexe, args.age, existants=existants)
    statut = "figurant" if args.figurant else "recurrent"
    print(resume(p))
    if p["mineur"]:
        print("  !! MINEUR(E) : aucune scène ni table relationnelle (T1, T1b, T9) ; jet.py --pour le refuse.")
    if args.simule:
        print("(essai : rien n'est écrit)")
        return 0
    fiche = ecrire_fiche(p) if statut == "recurrent" else ""
    lignes = lire()
    lignes.append(ligne_registre(p, statut, fiche))
    ecrire_csv(REGISTRE, lignes, COLONNES)
    if statut == "recurrent":
        ecrire_vie_propre(p)
        ecrire_secret(p)
    consigner(p, statut)
    print(f"Écrit : etat/personnages.csv{' ; ' + fiche + ' ; etat/vies-propres.md ; etat/savoir.csv (secret)' if fiche else ''}")
    return 0


def libelle_sexe(role, sexe):
    """« {professeur|professeure} de physique », « {directeur adjoint|directrice adjointe} » : entre accolades, la forme masculine
    avant la barre, la féminine après ; le reste du libellé est commun."""
    return re.sub(r"\{([^|}]*)\|([^}]*)\}", lambda m: m.group(1) if sexe == "H" else m.group(2), role)


def cmd_reseau(args):
    """Entourage existant de William, généré d'avance d'après un plan (contexte ; rôle ; nombre ; âges ; sexe ; cercle ; note)."""
    plan = lire_csv(RACINE / args.plan)
    deja = [l for l in lire() if l["statut"] == "pre_genere"]
    if deja and not args.forcer and not args.simule:
        sys.exit(f"{len(deja)} personnage(s) déjà pré-généré(s) : un réseau ne se tire qu'une fois (--forcer pour en ajouter).")
    rng = random.SystemRandom()
    ctxs = contextes()
    existants = [l["nom"] for l in lire()]
    nouveaux = []
    for ligne in plan:
        ctx = ctxs.get(ligne["contexte"])
        if not ctx:
            sys.exit(f"Contexte inconnu dans le plan : {ligne['contexte']}")
        for _ in range(int(ligne["nombre"] or 1)):
            sexe = ligne.get("sexe") or None
            if not sexe:
                sexe = sexe_du_role(ligne["role"]) if "{" not in ligne["role"] else None
                sexe = sexe or ("F" if rng.random() < float(ctx["part_femmes"]) else "H")
            role = libelle_sexe(ligne["role"], sexe)
            ages = None
            if ligne.get("ages"):
                bornes = [int(x) for x in ligne["ages"].split("-")]
                a = int(rng.triangular(bornes[0], bornes[-1] + 1, bornes[1])) if len(bornes) == 3 else int(rng.uniform(bornes[0], bornes[1] + 1))
                ages = f"{a}-{a}"
            pers = tirer(ligne["contexte"], role, sexe, ages, rng=rng, existants=existants)
            existants.append(pers["nom"])
            nouveaux.append((pers, ligne))
    lignes = lire()
    for pers, ligne in nouveaux:
        note = f"pré-généré le {aujourd_hui():%d/%m/%Y} (entourage existant, plan {args.plan})" + (f" · {ligne['note']}" if ligne.get("note") else "")
        lignes.append(ligne_registre(pers, "pre_genere", "", cercle=ligne.get("cercle") or "3", note=note))
        print(f"  {pers['nom']:28s} {pers['age']:>3} ans {pers['sexe']} {pers['role']} ({pers['contexte']}){'  MINEUR' if pers['mineur'] else ''}")
    if args.simule:
        print(f"(essai : {len(nouveaux)} personnage(s), rien n'est écrit)")
        return 0
    ecrire_csv(REGISTRE, lignes, COLONNES)
    for pers, _ in nouveaux:
        consigner(pers, "pre_genere")
    print(f"{len(nouveaux)} personnage(s) pré-généré(s) dans etat/personnages.csv (statut pre_genere : jamais montrés au joueur avant "
          f"leur apparition dans une scène)")
    return 0


def cmd_apparait(args):
    lignes = lire()
    l = trouver(args.nom)
    cible = next(x for x in lignes if x["id"] == l["id"])
    if cible["statut"] != "pre_genere":
        print(f"{cible['nom']} est déjà {cible['statut']}.")
        return 0
    cible["statut"] = "figurant"
    cible["notes"] += f" · première apparition le {aujourd_hui():%d/%m/%Y}" + (f" ({args.scene})" if args.scene else "")
    ecrire_csv(REGISTRE, lignes, COLONNES)
    print(f"{cible['nom']} apparaît : statut figurant ({cible['role']}). Pour une fiche et une vie propre : personnage.py promouvoir")
    return 0


def trouver(nom):
    for l in lire():
        if nom.lower() in (l["nom"].lower(), l["id"].lower(), l["nom"].split()[0].lower()):
            return l
    sys.exit(f"Personnage inconnu : {nom}")


def cmd_promouvoir(args):
    lignes = lire()
    l = trouver(args.nom)
    if l["statut"] == "recurrent":
        print(f"{l['nom']} est déjà récurrent ({l['fiche']}).")
        return 0
    rng = random.SystemRandom()
    a = age(l["naissance"], aujourd_hui())
    traits = {k: int(v) for k, v in re.findall(r"([OCEAN])(\d+)", l["traits"])}
    p = {"nom": l["nom"], "role": l["role"], "contexte": l["contexte"], "sexe": l["sexe"], "naissance": l["naissance"], "age": a,
         "mineur": a < 18, "origine": l["origine"], "nationalite": l["nationalite"], "langues": l["langues"],
         "langue_avec_william": l["langue_avec_william"], "registre": l["registre"], "commune": l["commune"], "metier": l["metier"],
         "employeur": l["employeur"], "traits": traits,
         "attachement": (re.search(r"attachement (\w+)", l["traits"]) or [None, "sécure"])[1]}
    foyer = re.search(r"foyer : ([^·]+)", l["notes"])
    p["foyer"] = foyer.group(1).strip() if foyer else tirer_foyer(rng, a)
    p["defauts"] = (re.search(r"défauts : ([^·]+)", l["traits"]).group(1).strip().split(" / ")
                    if "défauts" in l["traits"] else catalogue(rng, "defaut", traits, 2))
    p["qualite"] = (re.search(r"qualité : ([^·]+)", l["traits"]).group(1).strip().split(" / ")
                    if "qualité" in l["traits"] else catalogue(rng, "qualite", traits, 1))
    p["oubli"] = float(re.search(r"oubli (\d+)", l["traits"]).group(1)) / 100 if "oubli" in l["traits"] else 0.1
    p["contradiction"] = []
    p["objectif"] = [re.search(r"objectif : ([^·]+)", l["notes"]).group(1).strip()] if "objectif" in l["notes"] else catalogue(rng, "objectif", traits)
    p["souci"] = [re.search(r"souci : ([^·]+)", l["notes"]).group(1).strip()] if "souci" in l["notes"] else catalogue(rng, "souci", traits)
    p["loisirs"] = re.search(r"loisirs : ([^·]+)", l["notes"]).group(1).strip().split(" / ") if "loisirs" in l["notes"] else []
    secret = re.search(r"secret : ([^·]+?)(?: \(gravité (\d)\))?\s*(?:·|$)", l["notes"])
    if secret:  # tirage d'origine conservé (pré-généré ou figurant créé depuis le 11/10/2026)
        p["secret"] = [] if secret.group(1).strip() == "aucun" else [secret.group(1).strip()]
        p["gravite_secret"] = int(secret.group(2)) if secret.group(2) else (gravite(p["secret"][0]) if p["secret"] else 0)
    else:
        p["secret"] = [] if p["mineur"] else catalogue(rng, "secret", traits, 1)
        p["gravite_secret"] = gravite(p["secret"][0]) if p["secret"] else 0
    contra = re.search(r"contradiction : ([^·]+?)\s*(?:·|$)", l["notes"])
    if contra and contra.group(1).strip() != "aucune":
        p["contradiction"] = [contra.group(1).strip()]
    phys = re.search(r"physique : (\d+) cm, ([^,·]+)", l["notes"])
    p["taille"], p["corpulence"], p["signes"] = (int(phys.group(1)), phys.group(2).strip(), []) if phys else physique(rng, l["origine"], l["sexe"], contextes()[l["contexte"]], a)
    l["fiche"] = ecrire_fiche(p)
    l["statut"] = "recurrent"
    l["cercle"] = "3"
    ecrire_csv(REGISTRE, lignes, COLONNES)
    ecrire_vie_propre(p)
    ecrire_secret(p)
    print(f"{l['nom']} devient récurrent : {l['fiche']} ; bloc ajouté à etat/vies-propres.md")
    return 0


def maj_vie_propre(p, foyer):
    """Remplit le bloc « vie propre » d'un personnage écrit à la main (champs vides) ; sinon ajoute un bloc."""
    texte = lire_texte(VIES).replace("\r\n", "\n")
    m = re.search(rf"(### {re.escape(p['nom'])} \([^\n]*\n)(.*?)(?=\n### |\n## |\Z)", texte, re.S)
    if not m:
        ecrire_vie_propre(p)
        return
    corps = m.group(2)
    corps = corps.replace("- **Objectif** : — ; **souci** : — ; **foyer** : —",
                          f"- **Objectif** : {' ; '.join(p['objectif'])} ; **souci** : {' ; '.join(p['souci'])} ; **foyer** : {foyer}")
    corps = corps.replace("- **Secret (moteur seulement)** : —",
                          f"- **Secret (moteur seulement)** : {p['secret'][0] + ' (tiré le 22/10/2026)' if p['secret'] else 'aucun'}")
    ecrire_texte(VIES, texte[:m.start(2)] + corps + texte[m.end(2):])


def cmd_completer(args):
    """Complète un personnage écrit à la main (sans défauts, secret, souci ni objectif tirés) : tire seulement ce qui manque,
    d'après sa zone, son âge, son métier et ses traits déjà écrits ; ne modifie rien de ce qui a été joué (22/10/2026, U3-2)."""
    lignes = lire()
    l = trouver(args.nom)
    cible = next(x for x in lignes if x["id"] == l["id"])
    if "complété le" in cible["notes"]:
        print(f"{cible['nom']} a déjà été complété : le tirage est définitif.")
        return 0
    ctx = contextes().get(cible["contexte"])
    zone = args.zone or (ctx["zone"] if ctx else None)
    if zone not in {z["zone"] for z in table("zones.csv")}:
        sys.exit("Zone inconnue ou absente : préciser --zone (seoul, bresil, abidjan, manille, audun…).")
    a = age(cible["naissance"], aujourd_hui())
    if a < 18:
        sys.exit(f"{cible['nom']} a moins de 18 ans : aucun tirage relationnel.")
    traits = {k: int(v) for k, v in re.findall(r"([OCEAN])(\d+)", cible["traits"])}
    if len(traits) < 5:
        sys.exit("Traits (Big Five) absents du registre : à écrire avant de compléter.")
    rng = random.SystemRandom()
    foyer = (pondere(rng, [("vit seul(e)", 55), ("en colocation", 25), ("vit chez ses parents", 20 if a < 30 else 0)])
             if args.celibataire else tirer_foyer(rng, a))
    s = situation(a, cible["metier"], foyer, cible["nationalite"], zone)
    p = {"nom": cible["nom"], "role": cible["role"], "contexte": cible["contexte"], "age": a, "mineur": False, "zone": zone,
         "traits": traits, "foyer": foyer,
         "attachement": pondere(rng, [("sécure", 56), ("évitant", 25), ("anxieux", 19)]),
         "defauts": catalogue(rng, "defaut", traits, 2), "qualite": catalogue(rng, "qualite", traits, 1),
         "contradiction": catalogue(rng, "contradiction", traits, 1, situation_=s) if rng.random() < 0.5 else [],
         "objectif": catalogue(rng, "objectif", traits, 1, situation_=s), "souci": catalogue(rng, "souci", traits, 1, situation_=s),
         "secret": catalogue(rng, "secret", traits, 1, situation_=s),
         "loisirs": catalogue(rng, "loisir", traits, 1 + (rng.random() < 0.5), situation_=s),
         "oubli": max(0.03, min(0.30, 0.12 - (traits["C"] - 50) * 0.004))}
    p["gravite_secret"] = gravite(p["secret"][0]) if p["secret"] else 0
    secret = f"{p['secret'][0]} (gravité {p['gravite_secret']})" if p["secret"] else "aucun"
    print(f"{p['nom']} ({a} ans, zone {zone}) : foyer {foyer} ; attachement {p['attachement']} ; défauts {' / '.join(p['defauts'])} ; "
          f"qualité {' / '.join(p['qualite'])} ; contradiction {p['contradiction'][0] if p['contradiction'] else 'aucune'}\n"
          f"  objectif {' / '.join(p['objectif'])} ; souci {' / '.join(p['souci'])} ; loisirs {' / '.join(p['loisirs'])} ; "
          f"secret {secret} ; oubli {round(p['oubli'] * 100)} %")
    if args.simule:
        print("(essai : rien n'est écrit)")
        return 0
    cible["traits"] = (cible["traits"] + f" · attachement {p['attachement']} · défauts : {' / '.join(p['defauts'])} · qualité : "
                       f"{' / '.join(p['qualite'])} · oubli {round(p['oubli'] * 100)} %").replace(";", ",")
    cible["notes"] = (cible["notes"] + f" · complété le {aujourd_hui():%d/%m/%Y} (tirage, audit U3-2) : foyer : {foyer} · objectif : "
                      f"{' / '.join(p['objectif'])} · souci : {' / '.join(p['souci'])} · loisirs : {' / '.join(p['loisirs'])} · secret : "
                      f"{secret} · contradiction : {p['contradiction'][0] if p['contradiction'] else 'aucune'}").replace(";", ",")
    ecrire_csv(REGISTRE, lignes, COLONNES)
    if cible["fiche"] and (RACINE / cible["fiche"]).exists():
        ajouter_texte(RACINE / cible["fiche"], f"""
## Complément tiré le {aujourd_hui():%d/%m/%Y} (audit U3-2)
> Tirage du générateur pour un personnage écrit à la main : il complète la fiche sans modifier ce qui a été joué. Définitif.
- Foyer : {foyer}.
- Attachement : {p['attachement']}. Défauts : {' ; '.join(p['defauts'])}. Qualité : {' ; '.join(p['qualite'])}.{' Contradiction : ' + p['contradiction'][0] + '.' if p['contradiction'] else ''}
- Fiabilité : environ {round(p['oubli'] * 100)} % de risque d'oubli ou d'annulation d'un rendez-vous ou d'une promesse.
- Objectif du moment : {' ; '.join(p['objectif'])}. Souci en cours : {' ; '.join(p['souci'])}. Loisirs : {' ; '.join(p['loisirs'])}.
- Secret : {secret} (fait caché ; ne ressort que par un tirage ou une révélation consignée dans etat/savoir.csv).
""")
    maj_vie_propre(p, foyer)
    ecrire_secret(p)
    consigner(p, "complete")
    print("Écrit : etat/personnages.csv ; fiche ; etat/vies-propres.md ; etat/savoir.csv (secret)")
    return 0


def cmd_liste(args):
    jour = aujourd_hui()
    for l in lire():
        if args.statut and l["statut"] != args.statut:
            continue
        a = age(l["naissance"], jour) if l["naissance"] else "?"
        print(f"{l['id']:28s} {l['nom']:26s} {a!s:>3} ans {l['sexe']} {l['statut']:9s} {l['role']} ({l['contexte']})"
              + ("  MINEUR" if isinstance(a, int) and a < 18 else ""))
    return 0


def cmd_voir(args):
    l = trouver(args.nom)
    for c in COLONNES:
        if l.get(c):
            print(f"{c:20s} {l[c]}")
    return 0


def cmd_audit(args):
    tous = lire()
    par_statut = {}
    for l in tous:
        par_statut[l["statut"]] = par_statut.get(l["statut"], 0) + 1
    print("Registre : " + (", ".join(f"{n} {s}" for s, n in sorted(par_statut.items())) or "vide"))
    lignes = [l for l in tous if l["statut"] == "recurrent"]
    print(f"{len(lignes)} personnage(s) récurrent(s)")
    if not lignes:
        return 0
    attendu = {}
    for l in lignes:
        z = contextes().get(l["contexte"], {}).get("zone")
        for zl in table("zones.csv"):
            if zl["zone"] == z:
                tot = sum(float(x["poids"]) for x in table("zones.csv") if x["zone"] == z)
                attendu[zl["origine"]] = attendu.get(zl["origine"], 0) + float(zl["poids"]) / tot
    observe = {}
    for l in lignes:
        observe[l["origine"]] = observe.get(l["origine"], 0) + 1
    print("Origines (observé / attendu d'après les contextes) :")
    for o in sorted(set(attendu) | set(observe), key=lambda x: -attendu.get(x, 0)):
        obs, att = observe.get(o, 0), attendu.get(o, 0)
        alerte = "  <- SURREPRÉSENTÉ" if att and obs > 2 * att and obs >= 3 else ("  <- absent" if att >= 3 and obs == 0 else "")
        print(f"  {o:10s} {obs:3d} / {att:5.1f}{alerte}")
    femmes = sum(l["sexe"] == "F" for l in lignes)
    print(f"Femmes : {femmes} sur {len(lignes)}")
    sans = [l["nom"] for l in lignes if not l["naissance"]]
    if sans:
        print("Sans date de naissance (garde « mineurs » impossible) : " + ", ".join(sans))
    return 0


def cmd_contextes(args):
    for c in contextes().values():
        print(f"{c['contexte']:18s} zone {c['zone']:16s} {c['age_min']}-{c['age_max']} ans, {float(c['part_femmes']):.0%} de femmes : {c['note']}")
    return 0


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("nouveau")
    p.add_argument("--contexte", required=True)
    p.add_argument("--role", required=True)
    p.add_argument("--sexe", choices=("H", "F"))
    p.add_argument("--age", help="fourchette, ex. 30-40 (sinon : tirée selon le contexte)")
    p.add_argument("--figurant", action="store_true", help="registre seulement (pas de fiche ni de vie propre)")
    p.add_argument("--simule", action="store_true")
    p.set_defaults(f=cmd_nouveau)
    p = sp.add_parser("promouvoir")
    p.add_argument("nom")
    p.set_defaults(f=cmd_promouvoir)
    p = sp.add_parser("completer")
    p.add_argument("nom")
    p.add_argument("--zone", help="seoul, bresil, manille, audun… (sinon : celle du contexte du personnage)")
    p.add_argument("--celibataire", action="store_true", help="foyer sans conjoint ni enfants")
    p.add_argument("--simule", action="store_true")
    p.set_defaults(f=cmd_completer)
    p = sp.add_parser("liste")
    p.add_argument("--statut", help="pre_genere, figurant ou recurrent")
    p.set_defaults(f=cmd_liste)
    p = sp.add_parser("reseau")
    p.add_argument("--plan", required=True, help="CSV : contexte;role;nombre;ages;sexe;cercle;note")
    p.add_argument("--simule", action="store_true")
    p.add_argument("--forcer", action="store_true")
    p.set_defaults(f=cmd_reseau)
    p = sp.add_parser("apparait")
    p.add_argument("nom")
    p.add_argument("--scene", default="")
    p.set_defaults(f=cmd_apparait)
    p = sp.add_parser("voir")
    p.add_argument("nom")
    p.set_defaults(f=cmd_voir)
    sp.add_parser("audit").set_defaults(f=cmd_audit)
    sp.add_parser("contextes").set_defaults(f=cmd_contextes)
    args = ap.parse_args()
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())
