"""Échéancier des RITUELS DU MOTEUR (créé le 11/10/2026) : ce que le moteur doit faire, d'après l'horloge, et qu'il a souvent oublié
dans l'univers 1 (fiche complète du 03/08, rapport du 06/08, tour du monde des 07-09/08, revue n° 4 jamais tenue…).

    python outils/rituels.py dus            # rituels échus ou dus aujourd'hui, avec la commande à lancer
    python outils/rituels.py dus --strict   # code de sortie 1 s'il y a un rituel en retard (contrôle de fin de tour)
    python outils/rituels.py liste          # la liste des rituels et leur règle

Rien n'est saisi à la main : chaque rituel est « prouvé » par une trace dans les fichiers (marqueur dans le journal, fichier de
synthèse, ligne dans le journal des tirages). Règles d'origine : CLAUDE.md §6 (fiches), §7 (fin de journée, fin de semaine), §12
(revue du lundi, aléas, message spontané d'un proche, monde extérieur, T4/T5 du dimanche).
Le départ de l'univers (etat/univers.json) borne le contrôle : rien n'est dû avant.
"""
import argparse
import datetime as dt
import json
import re
import sys

from commun import ETAT, JOURNAL, MEMOIRE, lire_texte, maintenant_simule, utf8

UNIVERS = ETAT / "univers.json"
TIRAGES = MEMOIRE / "tirages-aleas.md"

RITUELS = [
    ("fiche_courte", "chaque jour simulé (à sa clôture)", "Fiche courte en fin de journal du jour (« Fiche courte » dans journal/AAAA-MM-JJ.md)"),
    ("tour_du_monde", "chaque jour simulé et à chaque « Go »",
     "automatique depuis le 14/10/2026 : tour.py fin → monde_vivant.py avancer (à la main : python outils/monde_vivant.py avancer)"),
    ("fiche_complete", "tous les 3 jours simulés", "Fiche complète (« Fiche complète » dans le journal) + mise à jour de tous les fichiers d'état"),
    ("synthese_semaine", "chaque dimanche soir", "memoire/semaine-AAAA-WNN.md (semaine ISO)"),
    ("t4_t5_dimanche", "chaque dimanche soir, pour chaque affaire ouverte", "python outils/savoir.py t5 (commandes T4 et T5 prêtes)"),
    ("revue_lundi", "le premier lundi du mois, avant le reste (chaque lundi jusqu'au 21/10/2041)", "memoire/revue-lundi-AAAA-MM-JJ.md (CLAUDE.md §12)"),
    ("invitation_mois", "le premier lundi du mois (P57)", "jour et expéditeur d'une invitation de l'entourage, libellé « Invitation du mois AAAA-MM : … »"),
    ("calendrier_social", "le premier lundi du mois (P62)", "pots, anniversaires, fêtes du lycée et du club, libellé « Calendrier social du mois AAAA-MM : … »"),
    ("tirage_aleas", "chaque lundi", "python outils/tirage_aleas.py AAAA-MM-JJ"),
    ("message_proche", "chaque lundi", "tirer l'expéditeur et le jour d'un message spontané d'un proche (CLAUDE.md §12), "
                                       "libellé « Message spontané d'un proche, semaine du AAAA-MM-JJ »"),
    ("monde_semaine", "chaque lundi", "3 à 5 nouvelles du monde dans etat/monde.md, section « ## Semaine du JJ au JJ/MM/AAAA »"),
]


def depart():
    """Date de départ de l'univers en cours (etat/univers.json)."""
    try:
        u = json.loads(lire_texte(UNIVERS) or "{}")
        return dt.date.fromisoformat(u["depart"][:10])
    except (KeyError, ValueError):
        return None


def monde_vivant_fait(d):
    """Journée déjà tirée par outils/monde_vivant.py (14/10/2026 : tour du monde automatique dans tour.py fin)."""
    try:
        e = json.loads(lire_texte(ETAT / "monde-vivant.json") or "{}")
    except ValueError:
        return False
    return bool(e.get("dernier_jour")) and e["dernier_jour"] >= d.isoformat()


def fiches_vies_propres():
    return [l for l in lire_texte(ETAT / "vies-propres.md").splitlines() if l.startswith("### ")]


def affaires_ouvertes():
    import savoir
    return sorted({l["fait"] for l in savoir.lire() if l["fait"].startswith("affaire_")})


def journal_contient(jour, motif):
    return re.search(motif, lire_texte(JOURNAL / f"{jour:%Y-%m-%d}.md"), re.I) is not None


def derniere_fiche_complete(avant):
    """Date du dernier journal (≤ avant) qui contient « Fiche complète »."""
    meilleurs = []
    for p in JOURNAL.glob("*.md"):
        try:
            d = dt.date.fromisoformat(p.stem)
        except ValueError:
            continue
        if d <= avant and re.search(r"fiche complète", p.read_text(encoding="utf-8"), re.I):
            meilleurs.append(d)
    return max(meilleurs) if meilleurs else None


def bilan(instant=None):
    """[(rituel, statut, détail, commande)] ; statut : « EN RETARD », « DÛ », « sans objet »."""
    instant = instant or maintenant_simule()
    if instant is None:
        return [("horloge", "EN RETARD", "etat/horloge.txt illisible", "python outils/horloge.py --regler ...")]
    aujourd_hui = instant.date()
    d0 = depart() or aujourd_hui
    tirages = lire_texte(TIRAGES)
    res = []
    jours_clos = [d0 + dt.timedelta(days=i) for i in range((aujourd_hui - d0).days)]  # jours simulés terminés
    # 1. fiche courte et tour du monde de chaque jour clos
    for d in jours_clos:
        if not journal_contient(d, r"fiche courte"):
            res.append(("fiche_courte", "EN RETARD", f"journal du {d:%d/%m/%Y} sans fiche courte",
                        f"compléter journal/{d:%Y-%m-%d}.md"))
        if fiches_vies_propres():
            if f"Tour du monde du {d:%d/%m}" not in tirages and not monde_vivant_fait(d):
                res.append(("tour_du_monde", "EN RETARD", f"aucun tour du monde consigné pour le {d:%d/%m/%Y}",
                            f"python outils/tour_du_monde.py {d:%d/%m}"))
    if not fiches_vies_propres():
        res.append(("tour_du_monde", "sans objet", "aucune fiche dans etat/vies-propres.md", ""))
    # 2. fiche complète tous les 3 jours (le départ compte comme jour 0)
    derniere = derniere_fiche_complete(aujourd_hui) or d0
    ecart = (aujourd_hui - derniere).days
    if ecart >= 3:
        res.append(("fiche_complete", "EN RETARD" if ecart > 3 else "DÛ",
                    f"dernière fiche complète : {derniere:%d/%m/%Y} ({ecart} jours)", "fiche complète + tous les fichiers d'état"))
    # 3. dimanches clos : synthèse de semaine, T4/T5
    for d in jours_clos:
        if d.weekday() == 6:
            iso = d.isocalendar()
            nom = f"semaine-{iso[0]}-W{iso[1]:02d}.md"
            if not (MEMOIRE / nom).exists():
                res.append(("synthese_semaine", "EN RETARD", f"memoire/{nom} absent (semaine close le {d:%d/%m/%Y})",
                            f"écrire memoire/{nom}"))
            for a in affaires_ouvertes():
                if not re.search(rf"\[T5\][^\n]*{re.escape(a)}[^\n]*{d:%d/%m}|\[T5\][^\n]*{d:%d/%m}[^\n]*{re.escape(a)}", tirages):
                    res.append(("t4_t5_dimanche", "EN RETARD", f"{a} : T4/T5 du dimanche {d:%d/%m} non trouvés",
                                "python outils/savoir.py t5"))
    if aujourd_hui.weekday() == 6:
        res.append(("synthese_semaine", "DÛ", "ce soir : synthèse de la semaine, T4/T5 des affaires ouvertes", "python outils/savoir.py t5"))
    # 4. lundis (y compris aujourd'hui) : revue, aléas, message d'un proche, monde
    lundis = [d for d in jours_clos + [aujourd_hui] if d.weekday() == 0]
    for m in lundis:
        statut = "DÛ" if m == aujourd_hui else "EN RETARD"
        mensuel = m >= dt.date(2041, 10, 28)  # 31/10/2026 (demande de l'utilisateur) : revue le premier lundi du mois seulement ; avant : chaque lundi
        if (not mensuel or m.day <= 7) and not (MEMOIRE / f"revue-lundi-{m:%Y-%m-%d}.md").exists():
            res.append(("revue_lundi", statut, f"revue du lundi {m:%d/%m/%Y} absente", f"memoire/revue-lundi-{m:%Y-%m-%d}.md"))
        if m >= dt.date(2041, 11, 1) and m.day <= 7:  # P57 et P62 (validées les 30 et 31/10/2026) : premier lundi du mois
            for cle, motif in (("invitation_mois", "Invitation du mois"), ("calendrier_social", "Calendrier social du mois")):
                if not re.search(rf"{motif}[^\n]*{m:%Y-%m}", tirages):
                    res.append((cle, statut, f"{motif.lower()} ({m:%m/%Y}) non tiré",
                                f'python outils/jet.py --procedure "rituel mensuel" "{motif} {m:%Y-%m} : ..." <proba>'))
        if f"Tirage de la semaine du {m:%Y-%m-%d}" not in tirages:
            res.append(("tirage_aleas", statut, f"aléas de la semaine du {m:%d/%m/%Y} non tirés",
                        f"python outils/tirage_aleas.py {m:%Y-%m-%d}"))
        if not re.search(rf"(Message spontané|proche)[^\n]*semaine du {m:%Y-%m-%d}", tirages):
            res.append(("message_proche", statut, f"message spontané d'un proche (semaine du {m:%d/%m}) non tiré",
                        f"python outils/rituels.py message-proche --semaine {m:%Y-%m-%d}"))
        dim = m + dt.timedelta(days=6)
        if not re.search(rf"Semaine du 0?{m.day} au 0?{dim.day}/{dim:%m}", lire_texte(ETAT / "monde.md")):
            res.append(("monde_semaine", statut, f"nouvelles du monde de la semaine du {m:%d/%m} absentes de etat/monde.md",
                        f"## Semaine du {m.day} au {dim:%d/%m/%Y}"))
    return res


# Message spontané d'un proche (CLAUDE.md §12 ; outil créé le 12/10/2026, univers 2) : l'expéditeur est tiré dans l'entourage
# existant (pré-généré, figurant ou récurrent), jamais les parents (ponts coupés), jamais un mineur, jamais un profil ou une
# rencontre de Manille ; pondération par proximité (estimation du moteur, à revoir en revue du lundi) : partenaires du club 3,
# collègues 2, voisins, direction et secrétariat du lycée 1 ; services et commerces exclus (ils n'écrivent pas « spontanément »).
# Le jour (lundi à dimanche) et l'heure (8 h à 22 h, heure de l'expéditeur) sont tirés ; le contenu se choisit le jour dit d'après
# la fiche du personnage (test d'intérêt), qui entre alors en scène par `personnage.py apparait`.
POIDS_PROCHES = {"club_combat": 3, "collegue_lycee": 2, "voisin_audun": 1, "direction_lycee": 1, "secretariat_lycee": 1}


def message_proche(semaine, simule=False):
    import random
    import jet
    import personnage as P
    from commun import age
    lundi = dt.date.fromisoformat(semaine)
    if lundi.weekday() != 0:
        sys.exit("--semaine : un lundi (AAAA-MM-JJ)")
    candidats = []
    for l in P.lire():
        if l["statut"] not in ("pre_genere", "figurant", "recurrent") or l["contexte"] not in POIDS_PROCHES:
            continue
        if "parent" in (l["role"] or "").lower() or not l["naissance"] or age(dt.date.fromisoformat(l["naissance"]), lundi) < 18:
            continue
        candidats.append((l, POIDS_PROCHES[l["contexte"]]))
    if not candidats:
        print("Aucun proche tirable (entourage vide)")
        return None
    rng = random.SystemRandom()
    x = rng.uniform(0, sum(w for _, w in candidats))
    for l, w in candidats:
        x -= w
        if x <= 0:
            break
    jour = lundi + dt.timedelta(days=rng.randrange(7))
    heure = f"{rng.randrange(8, 22):02d}:{rng.randrange(0, 60, 5):02d}"
    ligne = (f"- Message spontané d'un proche, semaine du {lundi:%Y-%m-%d} : {l['nom']} ({l['role']}) écrira le "
             f"{jour:%d/%m/%Y} vers {heure} (heure de l'expéditeur) · tiré parmi {len(candidats)} personnes de l'entourage, "
             f"pondérées par proximité")
    print(ligne)
    if not simule:
        jet.consigner(ligne)
        jet.consigner_json({"mode": "message_proche", "libelle": f"Message spontané d'un proche, semaine du {lundi:%Y-%m-%d}",
                            "pour": l["nom"], "issue": f"{jour.isoformat()} {heure}", "distribution": {"candidats": len(candidats)}})
    return l, jour, heure


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("dus")
    p.add_argument("--strict", action="store_true")
    sp.add_parser("liste")
    p = sp.add_parser("message-proche")
    p.add_argument("--semaine", required=True, help="le lundi de la semaine tirée (AAAA-MM-JJ)")
    p.add_argument("--simule", action="store_true")
    args = ap.parse_args()
    if args.cmd == "message-proche":
        message_proche(args.semaine, args.simule)
        return 0
    if args.cmd == "liste":
        for nom, quand, comment in RITUELS:
            print(f"- {nom} ({quand}) : {comment}")
        return 0
    b = bilan()
    retards = [x for x in b if x[1] == "EN RETARD"]
    dus = [x for x in b if x[1] == "DÛ"]
    print(f"Rituels du moteur : {len(retards)} en retard, {len(dus)} dû(s) aujourd'hui")
    for nom, statut, detail, cmd in b:
        if statut == "sans objet":
            continue
        print(f"  [{statut}] {nom} : {detail}" + (f"  ->  {cmd}" if cmd else ""))
    return 1 if (args.strict and retards) else 0


if __name__ == "__main__":
    sys.path.insert(0, str(ETAT.parent / "outils"))
    sys.exit(main())
