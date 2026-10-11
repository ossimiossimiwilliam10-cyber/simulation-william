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
    ("tour_du_monde", "chaque jour simulé (à sa clôture) et à chaque « Go »",
     "python outils/tour_du_monde.py JJ/MM (sans objet tant qu'aucune fiche n'existe dans etat/vies-propres.md)"),
    ("fiche_complete", "tous les 3 jours simulés", "Fiche complète (« Fiche complète » dans le journal) + mise à jour de tous les fichiers d'état"),
    ("synthese_semaine", "chaque dimanche soir", "memoire/semaine-AAAA-WNN.md (semaine ISO)"),
    ("t4_t5_dimanche", "chaque dimanche soir, pour chaque affaire ouverte", "python outils/savoir.py t5 (commandes T4 et T5 prêtes)"),
    ("revue_lundi", "chaque lundi, avant le reste", "memoire/revue-lundi-AAAA-MM-JJ.md (CLAUDE.md §12)"),
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
            if f"Tour du monde du {d:%d/%m}" not in tirages:
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
        if not (MEMOIRE / f"revue-lundi-{m:%Y-%m-%d}.md").exists():
            res.append(("revue_lundi", statut, f"revue du lundi {m:%d/%m/%Y} absente", f"memoire/revue-lundi-{m:%Y-%m-%d}.md"))
        if f"Tirage de la semaine du {m:%Y-%m-%d}" not in tirages:
            res.append(("tirage_aleas", statut, f"aléas de la semaine du {m:%d/%m/%Y} non tirés",
                        f"python outils/tirage_aleas.py {m:%Y-%m-%d}"))
        if not re.search(rf"(Message spontané|proche)[^\n]*semaine du {m:%Y-%m-%d}", tirages):
            res.append(("message_proche", statut, f"message spontané d'un proche (semaine du {m:%d/%m}) non tiré",
                        f"python outils/jet.py \"Message spontané d'un proche, semaine du {m:%Y-%m-%d} : <qui>\" <proba>"))
        dim = m + dt.timedelta(days=6)
        if not re.search(rf"Semaine du 0?{m.day} au 0?{dim.day}/{dim:%m}", lire_texte(ETAT / "monde.md")):
            res.append(("monde_semaine", statut, f"nouvelles du monde de la semaine du {m:%d/%m} absentes de etat/monde.md",
                        f"## Semaine du {m.day} au {dim:%d/%m/%Y}"))
    return res


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("dus")
    p.add_argument("--strict", action="store_true")
    sp.add_parser("liste")
    args = ap.parse_args()
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
