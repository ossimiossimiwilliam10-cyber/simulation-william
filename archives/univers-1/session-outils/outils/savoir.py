"""« Qui sait quoi » : un fait × une personne × un canal. Fichier : `etat/savoir.csv`.

But : (1) compter automatiquement les informés d'une affaire pour le tirage de fuite T5 (William exclu) ; (2) vérifier qu'un personnage
n'agit pas sur une information qu'il n'a pas (audit du 09/08/2040 : l'organigramme, l'offre LinkedIn, l'hospitalisation de Me Kouamé…).

Colonnes (séparateur « ; ») : fait;personne;canal;date;note
- fait : identifiant court en minuscules ; les faits dont l'identifiant commence par « affaire_ » sont suivis par T4/T5 chaque dimanche ;
- personne : un nom (William, Aïcha, Mariette, Grace, Abdoul, Yves, Estelle, Me Kouamé, Sandra, Kevin…) ou « proche_de_X » ;
- canal : oral, WhatsApp, courriel, LinkedIn, rumeur, vu_de_ses_yeux, deviné… ; date AAAA-MM-JJ ; note libre (« croit la version arrangée »…).

    python outils/savoir.py qui affaire_grace_2307          # qui sait, par quel canal
    python outils/savoir.py connait Abdoul                  # ce qu'Abdoul sait
    python outils/savoir.py peut Yves organigramme_note     # Yves peut-il agir sur ce fait ? (oui/non + canal)
    python outils/savoir.py informes affaire_grace_2307     # nombre d'informés hors William + commande T5
    python outils/savoir.py t5                              # toutes les affaires ouvertes : commandes T5 prêtes (dimanche soir)
    python outils/savoir.py ajouter FAIT PERSONNE --canal oral --date 2040-08-10 --note "..."
    python outils/savoir.py verifier
Règle : chaque révélation (parole, message, document transmis, rumeur) se consigne ici le jour même.
"""
import argparse
import csv
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
FICHIER = RACINE / "etat" / "savoir.csv"
COLONNES = ["fait", "personne", "canal", "date", "note"]
FUITE_INTERNE = (3, 40)
FUITE_EXTERNE = (1, 15)


def lire():
    if not FICHIER.exists():
        return []
    with FICHIER.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def ecrire(lignes):
    with FICHIER.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLONNES, delimiter=";", lineterminator="\r\n")
        w.writeheader()
        w.writerows(lignes)


def informes(fait, hors_william=True):
    noms = []
    for l in lire():
        if l["fait"] == fait and l["personne"] not in noms:
            noms.append(l["personne"])
    return [n for n in noms if not (hors_william and n == "William")]


def pourcentages_t5(n):
    ext = min(FUITE_EXTERNE[1], FUITE_EXTERNE[0] * n)
    inte = min(FUITE_INTERNE[1], FUITE_INTERNE[0] * n)
    return inte, ext


def cmd_qui(args):
    lignes = [l for l in lire() if l["fait"] == args.fait]
    if not lignes:
        sys.exit(f"Fait inconnu : {args.fait}")
    for l in lignes:
        print(f"  {l['personne']:22s} {l['canal']:16s} {l['date']}  {l['note']}")
    print(f"  -> {len(informes(args.fait))} informé(s) hors William")
    return 0


def cmd_connait(args):
    lignes = [l for l in lire() if l["personne"].lower() == args.personne.lower()]
    for l in lignes:
        print(f"  {l['fait']:36s} {l['canal']:16s} {l['date']}  {l['note']}")
    print(f"  -> {len(lignes)} fait(s) connu(s) de {args.personne}")
    return 0


def cmd_peut(args):
    for l in lire():
        if l["fait"] == args.fait and l["personne"].lower() == args.personne.lower():
            print(f"OUI : {args.personne} sait « {args.fait} » depuis le {l['date']} ({l['canal']}). {l['note']}")
            return 0
    print(f"NON : {args.personne} ne connaît pas « {args.fait} » ; il ou elle ne peut pas agir dessus (sauf rumeur à tirer).")
    return 1


def cmd_informes(args):
    n = len(informes(args.fait))
    inte, ext = pourcentages_t5(n)
    print(f"{args.fait} : {n} informé(s) hors William ({', '.join(informes(args.fait))})")
    print(f"  T5 : interne {inte} %, externe {ext} %")
    print(f"  python outils/jet.py --table T5 --informes {n} \"Fuite de l'affaire {args.fait} : semaine du JJ/MM\"")
    return 0


def cmd_t5(args):
    faits = sorted({l["fait"] for l in lire() if l["fait"].startswith("affaire_")})
    if not faits:
        print("Aucune affaire ouverte.")
        return 0
    print("Affaires ouvertes (T4 puis T5 chaque dimanche soir, règle 17) :")
    for f in faits:
        n = len(informes(f))
        inte, ext = pourcentages_t5(n)
        print(f"  {f} : {n} informé(s) ; interne {inte} %, externe {ext} %")
        print(f"      python outils/jet.py --table T4 \"{f} : escalade externe, semaine du JJ/MM\"")
        print(f"      python outils/jet.py --table T5 --informes {n} \"{f} : fuite, semaine du JJ/MM\"")
    return 0


def cmd_ajouter(args):
    lignes = lire()
    if any(l["fait"] == args.fait and l["personne"] == args.personne for l in lignes):
        sys.exit(f"{args.personne} connaît déjà « {args.fait} » (modifier la ligne à la main si le canal ou la date change)")
    lignes.append({"fait": args.fait, "personne": args.personne, "canal": args.canal or "", "date": args.date or "", "note": args.note or ""})
    ecrire(lignes)
    print(f"Ajouté : {args.personne} sait « {args.fait} » ; {len(informes(args.fait))} informé(s) hors William")
    return 0


def verifier():
    erreurs, vus = [], set()
    for n, l in enumerate(lire(), 2):
        cle = (l["fait"], l["personne"])
        if cle in vus:
            erreurs.append(f"savoir.csv:{n} doublon {cle}")
        vus.add(cle)
        if not l["fait"] or l["fait"] != l["fait"].lower() or " " in l["fait"]:
            erreurs.append(f"savoir.csv:{n} identifiant de fait invalide « {l['fait']} » (minuscules, sans espace)")
        if not l["personne"]:
            erreurs.append(f"savoir.csv:{n} personne vide")
    return erreurs


def cmd_verifier(args):
    erreurs = verifier()
    for e in erreurs:
        print("ERREUR", e)
    print("savoir.csv :", "des erreurs" if erreurs else "conforme", f"({len(lire())} lignes)")
    return 1 if erreurs else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("qui")
    p.add_argument("fait")
    p.set_defaults(f=cmd_qui)
    p = sp.add_parser("connait")
    p.add_argument("personne")
    p.set_defaults(f=cmd_connait)
    p = sp.add_parser("peut")
    p.add_argument("personne")
    p.add_argument("fait")
    p.set_defaults(f=cmd_peut)
    p = sp.add_parser("informes")
    p.add_argument("fait")
    p.set_defaults(f=cmd_informes)
    p = sp.add_parser("t5")
    p.set_defaults(f=cmd_t5)
    p = sp.add_parser("ajouter")
    p.add_argument("fait")
    p.add_argument("personne")
    p.add_argument("--canal")
    p.add_argument("--date")
    p.add_argument("--note")
    p.set_defaults(f=cmd_ajouter)
    p = sp.add_parser("verifier")
    p.set_defaults(f=cmd_verifier)
    args = ap.parse_args()
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())
