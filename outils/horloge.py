"""Horloge de la simulation : l'heure « maintenant » du monde, le lieu de William et ce qu'on attend de lui.

Fichier lu par agenda.py, grand_livre.py et resume_etat.py : `etat/horloge.txt` (clés horloge, fuseau, lieu, tour ; `attente:` peut
se répéter). `tour:` compte les tours joués depuis le départ de l'univers (ajouté le 11/10/2026 pour le relais : deux sessions qui
jouent en parallèle font diverger ce compteur, ce qui rend la divergence visible à la fusion git).

    python outils/horloge.py                                   # affiche l'horloge et l'heure dans tous les lieux
    python outils/horloge.py --regler "2040-08-09 14:15" --fuseau lisbonne --lieu "Lisbonne, hall de l'hôtel" \\
                              --attente "Où dormir cette nuit" --attente "Réponse à M. Konan"
    python outils/horloge.py --regler "2040-07-14 09:12" --tour +1           # avance le compteur de tours

À mettre à jour à la FIN DE CHAQUE TOUR (checklist de CLAUDE.md §13). `--attente` remplace toute la liste précédente.
"""
import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fuseaux  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
FICHIER = RACINE / "etat" / "horloge.txt"


def lire():
    """Retourne {'instant': datetime aware, 'fuseau': str, 'lieu': str, 'attentes': [str], 'tour': int}."""
    if not FICHIER.exists():
        sys.exit("etat/horloge.txt introuvable : lancer horloge.py --regler ...")
    cles, attentes = {}, []
    for ligne in FICHIER.read_text(encoding="utf-8").splitlines():
        if ":" not in ligne or ligne.lstrip().startswith("#"):
            continue
        k, v = ligne.split(":", 1)
        k, v = k.strip().lower(), v.strip()
        if k == "attente":
            attentes.append(v)
        else:
            cles[k] = v
    for k in ("horloge", "fuseau", "lieu"):
        if k not in cles:
            sys.exit(f"etat/horloge.txt : clé « {k} » manquante")
    d, h = cles["horloge"].split()
    instant = fuseaux.analyser_instant(d, h, cles["fuseau"])
    tour = int(cles["tour"]) if cles.get("tour", "").isdigit() else 0
    return {"instant": instant, "fuseau": fuseaux.zone(cles["fuseau"]), "lieu": cles["lieu"], "attentes": attentes, "tour": tour}


def ecrire(horloge_txt, fuseau, lieu, attentes, tour=None):
    if tour is None:
        tour = lire()["tour"] if FICHIER.exists() else 0
    lignes = ["# Horloge de la simulation (mise à jour à la fin de chaque tour ; lue par agenda.py, grand_livre.py, resume_etat.py)",
              f"horloge: {horloge_txt}", f"fuseau: {fuseau}", f"lieu: {lieu}", f"tour: {tour}"]
    lignes += [f"attente: {a}" for a in attentes]
    FICHIER.write_bytes(("\r\n".join(lignes) + "\r\n").encode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--regler", metavar="AAAA-MM-JJ HH:MM")
    ap.add_argument("--fuseau")
    ap.add_argument("--lieu")
    ap.add_argument("--attente", action="append", default=None)
    ap.add_argument("--tour", help="numéro du tour (N) ou +1 pour avancer le compteur")
    args = ap.parse_args()
    if args.regler or args.tour:
        actuel = lire() if FICHIER.exists() else {"fuseau": "luxembourg", "lieu": "?", "attentes": [], "tour": 0,
                                                  "instant": None}
        if args.regler:
            d, h = args.regler.split()
        else:
            d, h = f"{actuel['instant']:%Y-%m-%d}", f"{actuel['instant']:%H:%M}"
        fuseau = fuseaux.zone(args.fuseau) if args.fuseau else actuel["fuseau"]
        fuseaux.analyser_instant(d, h, fuseau)  # validation
        tour = actuel["tour"]
        if args.tour:
            tour = tour + int(args.tour[1:] or 1) if args.tour.startswith("+") else int(args.tour)
        ecrire(f"{d} {h}", fuseau, args.lieu or actuel["lieu"], args.attente if args.attente is not None else actuel["attentes"],
               tour)
    h = lire()
    print(f"Horloge : {h['instant']:%a %d/%m/%Y %H:%M} ({h['fuseau']}, {fuseaux.libelle_ecart(h['instant'])}) ; tour n° {h['tour']}")
    print(f"Lieu de William : {h['lieu']}")
    for a in h["attentes"]:
        print(f"  attente : {a}")
    print(fuseaux.tableau(h["instant"], h["fuseau"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
