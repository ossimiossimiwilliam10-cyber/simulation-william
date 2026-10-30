"""NOTATION CONTINUE DES DIRIGEANTS (validée par William le 06/10/2041 ; décision de l'utilisateur du 30/10/2026) : chaque dimanche,
le conseiller met à jour les fiches de l'application Gestion (`etat/gestion-collaborateurs.csv`, rubrique « Équipes et notes »)
d'après des faits datés. Grille : fiabilité 25, résultats 30, remontée d'information 20, qualité d'exécution 15, coopération 10.
Notation INTERNE (les dirigeants ne sont pas informés). Seuils : sous 60 deux semaines de suite, signalé à la séance du dimanche ;
sous 50 en période d'essai, point écrit demandé à Coulibaly.

    python outils/notation.py noter --nom "Viviane Tanoh" --note 52 --faits "…" [--vigilance "…"] [--quand "AAAA-MM-JJ HH:MM"]
    python outils/notation.py liste
"""
import argparse
import csv
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
FICHIER = Path(__file__).resolve().parent.parent / "etat" / "gestion-collaborateurs.csv"


def lire():
    with open(FICHIER, encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter=";")
        return r.fieldnames, list(r)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    n = sp.add_parser("noter")
    for k in ("--nom", "--note", "--faits"):
        n.add_argument(k, required=True)
    n.add_argument("--vigilance", default="")
    n.add_argument("--quand", default="")
    n.add_argument("--statut", default="")
    n.add_argument("--remplace", default="", help="nom d'une fiche « poste ouvert » à attribuer (ex. Direction Commerciale (Poste ouvert))")
    sp.add_parser("liste")
    a = ap.parse_args()
    cols, lignes = lire()
    if a.cmd == "liste":
        for l in lignes:
            print(f"{l['id']} {l['nom'][:40]:40s} {l['note_actuelle']:>4} (avant {l['note_precedente']}, {l['variation']})")
        return 0
    cible = next((l for l in lignes if l["nom"] == (a.remplace or a.nom)), None)
    if cible is None:
        sys.exit(f"Fiche inconnue : {a.remplace or a.nom}")
    avant = float(cible["note_actuelle"] or 0)
    cible["nom"] = a.nom
    cible["note_precedente"] = cible["note_actuelle"]
    cible["note_actuelle"] = a.note
    d = float(a.note) - avant
    cible["variation"] = "stable" if abs(d) < 1 else (f"+{d:.0f}" if d > 0 else f"{d:.0f}")
    cible["accomplissements"] = a.faits.replace(";", ",")
    if a.vigilance:
        cible["points_vigilance"] = a.vigilance.replace(";", ",")
    if a.statut:
        cible["statut"] = a.statut.replace(";", ",")
    if a.quand:
        cible["date_maj"] = a.quand
    with open(FICHIER, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter=";", lineterminator="\r\n")
        w.writeheader()
        w.writerows(lignes)
    print(f"{a.nom} : {a.note}/100 ({cible['variation']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
