"""Grand livre de la simulation : tous les mouvements d'argent de William (EUR) et, le cas échéant, d'une société qu'il possède ; soldes CALCULÉS, jamais saisis à la main.
Fichier : `etat/grand-livre.csv` (audit du 09/08/2040, correction n° 46 : des soldes périmés restaient en tête de `etat/finances.md`).

Colonnes (séparateur « ; ») : date;heure;compte;montant;type;libelle;reference
- compte : voir COMPTES (courant, projet, future_vie_familiale, etf, pret, maison_part ; univers 2 depuis le 11/10/2026) ;
- montant : positif = entrée, négatif = sortie, dans la devise du compte ; point décimal ;
- type : calage (le solde devient ce montant : relevé de banque, estimation d'une fiche) | mouvement (réel) |
         prevu (attendu, pas encore arrivé ; référence Pnnn) | prevu_realise (devenu mouvement) | prevu_annule (n'aura pas lieu) |
         valeur (actif non liquide, comme calage) | retire (retirée par une correction hors fiction : jamais comptée).

    python outils/grand_livre.py solde                       # soldes à l'horloge (etat/horloge.txt) + patrimoine
    python outils/grand_livre.py solde --projete 2040-08-31  # + les « prévu » jusqu'à cette date
    python outils/grand_livre.py ajouter --compte courant --montant -48.90 --libelle "Courses" [--date --heure --type --ref]
    python outils/grand_livre.py realiser P003 [--montant -1097.5]     # un « prévu » est arrivé : il devient un mouvement
    python outils/grand_livre.py annuler P008 --note "abonnement résilié"    # un « prévu » n'aura pas lieu
    python outils/grand_livre.py journal --compte courant    # les mouvements d'un compte
    python outils/grand_livre.py convertir 1032 EUR          # parité fixe 1 € = 655,957 FCFA
    python outils/grand_livre.py verifier                    # contrôle du fichier (intégré à controle_coherence.py)
Règle : chaque dépense, recette ou virement d'un tour s'écrit ICI (commande « ajouter ») ; les fiches de finances citent le résultat de « solde ».
"""
import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import horloge  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
FICHIER = RACINE / "etat" / "grand-livre.csv"
COLONNES = ["date", "heure", "compte", "montant", "type", "libelle", "reference"]
PARITE = 655.957
# compte : (propriétaire, devise, description, entre dans le patrimoine ?)
# Univers 2 (11/10/2026) : les comptes d'OSIA (univers 1) sont retirés. Si William crée ou rachète une société, ajouter ici
# son compte (propriétaire = la société, n'entre pas dans le patrimoine) et la participation de William (entre dans le patrimoine).
COMPTES = {
    "courant": ("William", "EUR", "Compte courant (Spuerkeess)", True),
    # clé « projet » gardée pour l'historique ; nom affiché : avant « Compte épargne « Projet » » → maintenant « Compte épargne »,
    # renommé par William le 14/07/2040 à 10h12
    "projet": ("William", "EUR", "Compte épargne (Spuerkeess)", True),
    "future_vie_familiale": ("William", "EUR", "Compte « Future vie familiale »", True),
    "etf": ("William", "EUR", "ETF (valeur de marché : calages seulement)", True),
    "pret": ("William", "EUR", "Prêt logement : solde restant dû (passif, déjà déduit de la part de maison)", False),
    "maison_part": ("William", "EUR", "Part nette de la maison d'Audun-le-Tiche", True),
    # 14/10/2026 : espèces en poche (outils/devises.py : retraits au distributeur, dépenses en espèces)
    "especes_php": ("William", "PHP", "Espèces (pesos philippins)", True),
    "especes_krw": ("William", "KRW", "Espèces (wons coréens)", True),
    "especes_eur": ("William", "EUR", "Espèces (euros)", True),
}
TYPES = {"calage", "mouvement", "prevu", "prevu_realise", "prevu_annule", "valeur", "retire"}
# « retire » (12/10/2026) : ligne retirée par une correction HORS FICTION demandée par l'utilisateur (elle n'a jamais eu lieu
# dans la fiction) ; gardée pour l'historique, jamais comptée dans les soldes.


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


def quand(l):
    d = dt.date.fromisoformat(l["date"])
    h = dt.time.fromisoformat(l["heure"] or "12:00")
    return dt.datetime.combine(d, h)


def horloge_naif():
    h = horloge.lire()["instant"]
    return h.replace(tzinfo=None)


def soldes(au, projete=None):
    """{compte: solde} à l'instant `au` (heures du fichier lues comme heures locales sans conversion de fuseau)."""
    s = {c: 0.0 for c in COMPTES}
    lignes = sorted(lire(), key=quand)
    for l in lignes:
        t = l["type"]
        if t in ("calage", "valeur") and quand(l) <= au:
            s[l["compte"]] = float(l["montant"])
        elif t in ("mouvement", "prevu_realise") and quand(l) <= au:
            s[l["compte"]] += float(l["montant"])
    # les calages postérieurs à un mouvement ne rejouent pas le passé : l'ordre chronologique ci-dessus suffit
    if projete:
        fin = dt.datetime.combine(projete, dt.time(23, 59))
        for l in lignes:
            if l["type"] == "prevu" and au < quand(l) <= fin:
                s[l["compte"]] += float(l["montant"])
    return s


def vers_eur(montant, devise):
    if devise in ("PHP", "KRW"):  # 14/10/2026 : au dernier taux tiré (outils/devises.py) ; wons : 22/10/2026
        import devises
        return montant / devises.taux_connu(devise)
    return montant if devise == "EUR" else montant / PARITE


def vers_fcfa(montant, devise):
    return montant if devise == "FCFA" else montant * PARITE


def fmt(montant, devise):
    if devise == "EUR":
        return f"{montant:,.2f} €".replace(",", " ").replace(".", ",")
    if devise in ("PHP", "KRW"):
        return (f"{montant:,.0f}" if abs(montant - round(montant)) < 0.005 else f"{montant:,.2f}").replace(",", " ").replace(".", ",") + f" {devise}"
    return f"{montant:,.0f} FCFA".replace(",", " ")


def afficher_soldes(au, projete=None):
    s = soldes(au, projete)
    print(f"Soldes au {au:%d/%m/%Y %H:%M}" + (f", projetés jusqu'au {projete:%d/%m/%Y}" if projete else "") + " :")
    for c, (prop, dev, desc, _) in COMPTES.items():
        if abs(s[c]) < 1e-9 and not any(l["compte"] == c for l in lire()):
            continue
        # univers 2 : plus de conversion en FCFA à l'affichage (14/10/2026) ; une devise étrangère est montrée en euros
        autre = "" if dev == "EUR" else f"  (≈ {fmt(vers_eur(s[c], dev), 'EUR')})"
        print(f"  {prop:7s} {c:20s} {fmt(s[c], dev):>22s}{autre}")
    patri = sum(vers_eur(s[c], COMPTES[c][1]) for c in COMPTES if COMPTES[c][3])
    print(f"  Patrimoine net de William (comptes + ETF + part de maison + participations éventuelles) : {fmt(patri, 'EUR')}")
    return s


def cmd_solde(args):
    au = dt.datetime.fromisoformat(args.au) if args.au else horloge_naif()
    projete = dt.date.fromisoformat(args.projete) if args.projete else None
    afficher_soldes(au, projete)
    prevus = [l for l in sorted(lire(), key=quand) if l["type"] == "prevu" and quand(l) > au]
    if prevus:
        print("Prévu (pas encore arrivé) :")
        for l in prevus:
            dev = COMPTES[l["compte"]][1]
            print(f"  {l['reference']:5s} {l['date']} {l['compte']:18s} {fmt(float(l['montant']), dev):>20s}  {l['libelle']}")
    return 0


def prochaine_ref(lignes):
    nums = [int(l["reference"][1:]) for l in lignes if l["reference"][:1] == "P" and l["reference"][1:].isdigit()]
    return f"P{(max(nums) + 1 if nums else 1):03d}"


def cmd_ajouter(args):
    if args.compte not in COMPTES:
        sys.exit(f"Compte inconnu : {args.compte} (connus : {', '.join(COMPTES)})")
    if args.type not in TYPES - {"prevu_realise"}:
        sys.exit(f"Type inconnu : {args.type}")
    h = horloge.lire()["instant"]
    lignes = lire()
    ref = args.ref or (prochaine_ref(lignes) if args.type == "prevu" else "")
    nouvelle = {"date": args.date or f"{h:%Y-%m-%d}", "heure": args.heure or f"{h:%H:%M}", "compte": args.compte,
                "montant": f"{args.montant:.2f}", "type": args.type, "libelle": args.libelle, "reference": ref}
    lignes.append(nouvelle)
    ecrire(lignes)
    dev = COMPTES[args.compte][1]
    print(f"Ajouté : {nouvelle['date']} {nouvelle['heure']} {args.compte} {fmt(args.montant, dev)} [{args.type}] {args.libelle} {ref}")
    afficher_soldes(horloge_naif())
    return 0


def cmd_realiser(args):
    lignes = lire()
    cible = next((l for l in lignes if l["reference"] == args.ref and l["type"] == "prevu"), None)
    if not cible:
        sys.exit(f"Aucun « prévu » de référence {args.ref}")
    h = horloge.lire()["instant"]
    montant = args.montant if args.montant is not None else float(cible["montant"])
    cible["type"] = "prevu_realise"
    cible["date"] = args.date or f"{h:%Y-%m-%d}"
    cible["heure"] = args.heure or f"{h:%H:%M}"
    cible["montant"] = f"{montant:.2f}"
    ecrire(lignes)
    print(f"Réalisé : {cible['libelle']} {fmt(montant, COMPTES[cible['compte']][1])}")
    afficher_soldes(horloge_naif())
    return 0


def cmd_annuler(args):
    lignes = lire()
    cible = next((l for l in lignes if l["reference"] == args.ref and l["type"] == "prevu"), None)
    if not cible:
        sys.exit(f"Aucun « prévu » de référence {args.ref}")
    cible["type"] = "prevu_annule"
    if args.note:
        cible["libelle"] += f" [annulé : {args.note}]"
    ecrire(lignes)
    print(f"Annulé : {cible['libelle']}")
    return 0


def cmd_journal(args):
    for l in sorted(lire(), key=quand):
        if args.compte and l["compte"] != args.compte:
            continue
        dev = COMPTES[l["compte"]][1]
        print(f"{l['date']} {l['heure']:5s} {l['compte']:18s} {fmt(float(l['montant']), dev):>20s} [{l['type']}] {l['libelle']} {l['reference']}")
    return 0


def cmd_convertir(args):
    dev = args.devise.upper()
    if dev == "EUR":
        print(f"{fmt(args.montant, 'EUR')} = {fmt(args.montant * PARITE, 'FCFA')}")
    elif dev == "FCFA":
        print(f"{fmt(args.montant, 'FCFA')} = {fmt(args.montant / PARITE, 'EUR')}")
    elif dev in ("PHP", "KRW"):
        print(f"{fmt(args.montant, dev)} = {fmt(vers_eur(args.montant, dev), 'EUR')} (dernier taux tiré : outils/devises.py)")
    else:
        sys.exit("Devise : EUR, FCFA, PHP ou KRW")
    return 0


def verifier():
    erreurs, refs = [], set()
    lignes = lire()
    for n, l in enumerate(lignes, 2):
        if l["compte"] not in COMPTES:
            erreurs.append(f"grand-livre.csv:{n} compte inconnu {l['compte']}")
        if l["type"] not in TYPES:
            erreurs.append(f"grand-livre.csv:{n} type inconnu {l['type']}")
        try:
            quand(l)
            float(l["montant"])
        except ValueError as e:
            erreurs.append(f"grand-livre.csv:{n} date, heure ou montant illisible ({e})")
        if l["type"] in ("prevu", "prevu_realise", "prevu_annule"):
            if not l["reference"] or l["reference"] in refs:
                erreurs.append(f"grand-livre.csv:{n} référence de prévu absente ou en double {l['reference']}")
            refs.add(l["reference"])
    try:
        h = horloge_naif()
        retards = [l for l in lignes if l["type"] == "prevu" and quand(l) < h]
    except SystemExit:
        retards = []
    return erreurs, retards


def cmd_verifier(args):
    erreurs, retards = verifier()
    for e in erreurs:
        print("ERREUR", e)
    for l in retards:
        print(f"RELIRE prévu échu non réalisé : {l['reference']} {l['date']} {l['libelle']}")
    print("grand-livre.csv :", "des erreurs" if erreurs else "conforme", f"({len(lire())} lignes ; {len(retards)} prévu(s) échu(s))")
    return 1 if erreurs else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("solde")
    p.add_argument("--au", help="AAAA-MM-JJ HH:MM (par défaut l'horloge)")
    p.add_argument("--projete", help="AAAA-MM-JJ : ajoute les prévus jusqu'à cette date")
    p.set_defaults(f=cmd_solde)
    p = sp.add_parser("ajouter")
    p.add_argument("--compte", required=True)
    p.add_argument("--montant", type=float, required=True)
    p.add_argument("--libelle", required=True)
    p.add_argument("--date")
    p.add_argument("--heure")
    p.add_argument("--type", default="mouvement")
    p.add_argument("--ref")
    p.set_defaults(f=cmd_ajouter)
    p = sp.add_parser("realiser")
    p.add_argument("ref")
    p.add_argument("--montant", type=float)
    p.add_argument("--date")
    p.add_argument("--heure")
    p.set_defaults(f=cmd_realiser)
    p = sp.add_parser("annuler")
    p.add_argument("ref")
    p.add_argument("--note")
    p.set_defaults(f=cmd_annuler)
    p = sp.add_parser("journal")
    p.add_argument("--compte")
    p.set_defaults(f=cmd_journal)
    p = sp.add_parser("convertir")
    p.add_argument("montant", type=float)
    p.add_argument("devise")
    p.set_defaults(f=cmd_convertir)
    p = sp.add_parser("verifier")
    p.set_defaults(f=cmd_verifier)
    args = ap.parse_args()
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())
