"""ACTIONS PROGRAMMÉES (créé le 14/10/2026 : univers vivant, simulation surtout informatique). Ce que le monde fait SANS qu'il y ait
de texte à écrire (un match qui tombe, un profil qui bloque William, un statut qui change) est programmé ici avec son heure, puis
exécuté tout seul par `tour.py fin` quand l'horloge passe cette heure. Le texte, lui, reste au moteur (agenda : « à écrire »).

    python outils/actions.py liste [--toutes]
    python outils/actions.py ajouter --quand "AAAA-MM-JJ HH:MM" --fuseau manille --commande "rencontres.py match kiara-reyes" --origine "T21a …"
    python outils/actions.py executer [--jusqua "AAAA-MM-JJ HH:MM" --fuseau …] [--simule]
    python outils/actions.py annuler X003 --raison "…"      # seulement une erreur du moteur (un tirage ne se rejoue jamais)

Seules les commandes de la liste blanche s'exécutent (PERMIS) ; chaque exécution est consignée dans le fichier (statut, résultat).
Fichier : `etat/actions.csv`.
"""
import argparse
import datetime as dt
import shlex
import subprocess
import sys

from commun import ETAT, OUTILS, RACINE, ecrire_csv, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
import fuseaux  # noqa: E402

FICHIER = ETAT / "actions.csv"
COLONNES = ["id", "quand", "fuseau", "commande", "statut", "origine", "note"]
PERMIS = {"rencontres.py": {"match", "bloquer", "passer", "aimer"}, "agenda.py": {"clore"}}


def lire():
    return lire_csv(FICHIER) if FICHIER.exists() else []


def instant(a):
    d, h = a["quand"].split()
    return fuseaux.analyser_instant(d, h, a["fuseau"])


def ajouter(quand, fuseau, commande, origine="", note=""):
    """quand : datetime aware (converti dans `fuseau`) ou texte « AAAA-MM-JJ HH:MM » ; commande : liste ou texte. Renvoie l'id."""
    morceaux = commande if isinstance(commande, list) else shlex.split(commande)
    if not morceaux or morceaux[0] not in PERMIS or len(morceaux) < 2 or morceaux[1] not in PERMIS[morceaux[0]]:
        sys.exit(f"Commande non permise : {' '.join(morceaux)} (liste blanche : {PERMIS})")
    if not isinstance(quand, str):
        quand = f"{fuseaux.convertir(quand, fuseau):%Y-%m-%d %H:%M}"
    lignes = lire()
    ident = f"X{len(lignes) + 1:03d}"
    lignes.append({"id": ident, "quand": quand, "fuseau": fuseaux.zone(fuseau), "commande": shlex.join(morceaux), "statut": "prevu",
                   "origine": origine.replace(";", ","), "note": note.replace(";", ",")})
    ecrire_csv(FICHIER, lignes, COLONNES)
    return ident


def executer(jusqua=None, simule=False):
    """Exécute les actions prévues dont l'heure est passée ; renvoie [(id, commande, sortie)]."""
    jusqua = jusqua or maintenant_simule()
    lignes = lire()
    faits = []
    for a in sorted(lignes, key=instant):
        if a["statut"] != "prevu" or instant(a) > jusqua:
            continue
        morceaux = shlex.split(a["commande"])
        if morceaux[0] not in PERMIS or morceaux[1] not in PERMIS[morceaux[0]]:
            a["statut"], a["note"] = "refuse", (a["note"] + " · commande hors liste blanche").strip(" ·")
            continue
        cmd = [sys.executable, str(OUTILS / morceaux[0]), *morceaux[1:]]
        if morceaux[0] == "rencontres.py" and "--quand" not in morceaux:
            cmd += ["--quand", a["quand"]]
        if morceaux[0] == "rencontres.py" and morceaux[1] in ("aimer",) and "--sans-reaction" not in morceaux:
            cmd += ["--sans-reaction"]
        if simule:
            faits.append((a["id"], a["commande"], "(essai)"))
            continue
        r = subprocess.run(cmd, cwd=str(RACINE), capture_output=True, text=True, encoding="utf-8", errors="replace")
        sortie = (r.stdout.strip() or r.stderr.strip()).splitlines()[-1:] or [""]
        a["statut"] = "fait" if r.returncode == 0 else "erreur"
        a["note"] = (a["note"] + f" · exécuté : {sortie[0][:120]}").strip(" ·").replace(";", ",")
        faits.append((a["id"], a["commande"], sortie[0]))
    if not simule:
        ecrire_csv(FICHIER, lignes, COLONNES)
    return faits


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("liste")
    p.add_argument("--toutes", action="store_true")
    p = sp.add_parser("ajouter")
    p.add_argument("--quand", required=True)
    p.add_argument("--fuseau", required=True)
    p.add_argument("--commande", required=True)
    p.add_argument("--origine", default="")
    p.add_argument("--note", default="")
    p = sp.add_parser("executer")
    p.add_argument("--jusqua")
    p.add_argument("--fuseau")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("annuler")
    p.add_argument("id")
    p.add_argument("--raison", required=True)
    args = ap.parse_args()
    if args.cmd == "liste":
        for a in lire():
            if args.toutes or a["statut"] == "prevu":
                print(f"{a['id']} {a['quand']} ({a['fuseau']}) [{a['statut']}] {a['commande']} · {a['origine']}")
        return 0
    if args.cmd == "ajouter":
        print("Action programmée :", ajouter(args.quand, args.fuseau, args.commande, args.origine, args.note))
        return 0
    if args.cmd == "executer":
        jusqua = None
        if args.jusqua:
            d, h = args.jusqua.split()
            jusqua = fuseaux.analyser_instant(d, h, args.fuseau or "luxembourg")
        for ident, cmd, sortie in executer(jusqua, args.simule):
            print(f"{ident} {cmd} → {sortie}")
        return 0
    lignes = lire()
    a = next((x for x in lignes if x["id"] == args.id), None)
    if a is None or a["statut"] != "prevu":
        sys.exit(f"Action introuvable ou déjà traitée : {args.id}")
    a["statut"], a["note"] = "annule", (a["note"] + f" · annulée : {args.raison}").strip(" ·").replace(";", ",")
    ecrire_csv(FICHIER, lignes, COLONNES)
    print(f"{args.id} annulée")
    return 0


if __name__ == "__main__":
    sys.exit(main())
