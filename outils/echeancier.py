"""ÉCHÉANCIER des mouvements d'argent récurrents (créé le 11/10/2026) : traitement, crédit, énergie, internet, club, impôts…
Dans l'univers 1, le compte courant ne bougeait que si le récit parlait d'argent (la mensualité de ≈ 940 € et l'électricité
n'ont jamais été prélevées : piège n° 77). Ici, chaque ligne ACTIVE de `etat/echeancier.csv` produit ses « prévus » dans le grand
livre, qui deviennent des mouvements réels quand l'horloge passe leur date (`tour.py fin` le fait automatiquement).

    python outils/echeancier.py liste                       # les lignes, leur prochaine date, leur statut
    python outils/echeancier.py prevoir --jusqua 2040-09-30 # écrit les prévus manquants dans etat/grand-livre.csv
    python outils/echeancier.py realiser                    # les prévus échus (à l'horloge) deviennent des mouvements
    python outils/echeancier.py budget 2040-08              # ce qui sort et entre ce mois-là (moteur)

Colonnes : id;libelle;compte;montant;periodicite;jour;mois;heure;debut;fin;statut;source;note;contrepartie;pret
- periodicite : mensuel | trimestriel | semestriel | annuel | ponctuel ; jour : 1-31, « dernier_ouvre » ou « premier_ouvre » ;
  mois : pour annuel « 10 », semestriel « 3,9 », trimestriel « 1,4,7,10 » ; ponctuel : la date est `debut`.
- statut : actif (produit des mouvements) | a_valider (montant ou existence à confirmer par l'utilisateur : rien n'est produit)
  | suspendu | termine. Un montant estimé le dit dans `source` ; on le remplace par le vrai dès qu'une pièce le donne.
- La référence d'un prévu est « Eid-AAAAMMJJ » : jamais de doublon, et l'historique reste lisible.
- contrepartie (depuis le 11/10/2026) : pour un virement entre deux comptes de William (ordre permanent vers l'épargne ou les
  ETF), le compte crédité ; le prévu s'écrit en deux lignes liées (« -C » pour la contrepartie).
- pret (depuis le 11/10/2026) : identifiant d'un prêt de `etat/prets.csv` ; le montant de chaque échéance vient alors du TABLEAU
  D'AMORTISSEMENT (outils/prets.py), en trois lignes liées : mensualité + assurance (compte de la ligne), capital remboursé
  (« -K », compte du capital restant dû) et même somme sur la part nette du bien (« -M ») ; la colonne montant n'est qu'un
  repère (mensualité courante) ; plus rien n'est produit après la dernière échéance.
"""
import argparse
import datetime as dt
import sys

from commun import ETAT, OUTILS, ecrire_csv, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
FICHIER = ETAT / "echeancier.csv"
COLONNES = ["id", "libelle", "compte", "montant", "periodicite", "jour", "mois", "heure", "debut", "fin", "statut", "source", "note",
            "contrepartie", "pret"]
MOIS_PAR_PERIODE = {"mensuel": list(range(1, 13)), "trimestriel": [1, 4, 7, 10], "semestriel": [1, 7], "annuel": [1]}


def lire():
    return lire_csv(FICHIER)


def date_du_mois(l, annee, mois):
    import calendrier_2040 as cal
    pays = "lu" if "traitement" in l["libelle"].lower() else "fr"
    j = (l["jour"] or "1").strip()
    if j == "dernier_ouvre":
        return cal.dernier_ouvre(annee, mois, pays)
    if j == "premier_ouvre":
        d = dt.date(annee, mois, 1)
        while d.weekday() >= 5 or d in cal.jours_feries(annee, pays):
            d += dt.timedelta(days=1)
        return d
    fin_mois = (dt.date(annee + (mois == 12), mois % 12 + 1, 1) - dt.timedelta(days=1)).day
    d = dt.date(annee, mois, min(int(j), fin_mois))
    # banque luxembourgeoise (Spuerkeess) : un prélèvement dû un week-end ou un jour férié passe au jour ouvré suivant
    while d.weekday() >= 5 or d in cal.jours_feries(d.year, "lu"):
        d += dt.timedelta(days=1)
    return d


def occurrences(l, du, au):
    """Dates d'échéance de la ligne dans [du, au]."""
    debut = dt.date.fromisoformat(l["debut"]) if l.get("debut") else du
    fin = dt.date.fromisoformat(l["fin"]) if l.get("fin") else au
    per = l["periodicite"]
    if per == "ponctuel":
        return [debut] if du <= debut <= au and debut <= fin else []
    mois = [int(m) for m in l["mois"].split(",")] if l.get("mois") else MOIS_PAR_PERIODE.get(per, [])
    res = []
    for annee in range(du.year, au.year + 1):
        for m in mois:
            d = date_du_mois(l, annee, m)
            if du <= d <= au and debut <= d <= fin:
                res.append(d)
    return sorted(res)


def mouvements(l, d):
    """Lignes du grand livre produites par la ligne `l` à la date `d` : une ; deux pour un virement (contrepartie) ; trois pour
    l'échéance d'un prêt (tableau d'amortissement) ; aucune après la dernière échéance d'un prêt."""
    base = {"date": d.isoformat(), "heure": l.get("heure") or "06:00", "type": "prevu"}
    ref = f"{l['id']}-{d:%Y%m%d}"
    if l.get("pret"):
        import prets
        p = prets.trouver(l["pret"])
        e = prets.echeance_du_mois(p, d.year, d.month)
        if e is None:
            return []
        total = round(e["echeance"] + e["assurance"], 2)
        lignes = [dict(base, compte=l["compte"], montant=f"{-total:.2f}", reference=ref,
                       libelle=f"{l['libelle']} (échéance n° {e['n']} : capital {e['capital']:.2f} €, intérêts {e['interet']:.2f} €, "
                               f"assurance {e['assurance']:.2f} €)"),
                  dict(base, compte=p.get("compte_capital") or "pret", montant=f"{-e['capital']:.2f}", reference=ref + "-K",
                       libelle=f"{p['libelle']} : capital remboursé (échéance n° {e['n']})")]
        if p.get("compte_actif"):
            lignes.append(dict(base, compte=p["compte_actif"], montant=f"{e['capital']:.2f}", reference=ref + "-M",
                               libelle=f"Part nette du bien financé : + capital remboursé (échéance n° {e['n']} du prêt {p['id']})"))
        return lignes
    m = float(l["montant"])
    lignes = [dict(base, compte=l["compte"], montant=f"{m:.2f}", libelle=l["libelle"], reference=ref)]
    if l.get("contrepartie"):
        lignes.append(dict(base, compte=l["contrepartie"], montant=f"{-m:.2f}", libelle=l["libelle"] + " (compte crédité)",
                           reference=ref + "-C"))
    return lignes


def prevoir(jusqua, depuis=None, simule=False):
    """Écrit au grand livre les prévus manquants des lignes actives, de `depuis` (horloge) à `jusqua`. Renvoie les lignes ajoutées."""
    import grand_livre as gl
    t = maintenant_simule()
    depuis = depuis or (t.date() if t else jusqua)
    livre = gl.lire()
    refs = {l["reference"] for l in livre}
    ajouts = []
    for l in lire():
        if l["statut"] != "actif":
            continue
        for d in occurrences(l, depuis, jusqua):
            for m in mouvements(l, d):
                if m["reference"] in refs:
                    continue
                refs.add(m["reference"])
                ajouts.append(m)
    if ajouts and not simule:
        gl.ecrire(livre + ajouts)
    return ajouts


def verifier():
    """(erreurs, avertissements) de etat/echeancier.csv : statuts, comptes, contreparties, prêts."""
    import grand_livre as gl
    erreurs, aver = [], []
    prets_connus = set()
    try:
        import prets
        prets_connus = {p["id"] for p in prets.lire()}
    except SystemExit:
        pass
    for l in lire():
        if l["statut"] not in ("actif", "a_valider", "suspendu", "termine"):
            erreurs.append(f"echeancier.csv : statut inconnu « {l['statut']} » ({l['id']})")
        for c in (l["compte"], l.get("contrepartie")):
            if c and c not in gl.COMPTES:
                erreurs.append(f"echeancier.csv : compte inconnu « {c} » ({l['id']})")
        if l.get("pret") and l["pret"] not in prets_connus:
            erreurs.append(f"echeancier.csv : prêt inconnu « {l['pret']} » ({l['id']}) : absent de etat/prets.csv")
        try:
            float(l["montant"])
        except ValueError:
            erreurs.append(f"echeancier.csv : montant illisible ({l['id']})")
    return erreurs, aver


def realiser(jusqua=None, simule=False):
    """Les prévus dont la date/heure est passée à l'horloge deviennent des mouvements (prevu_realise) : échéancier (« E… »), virements
    programmés de la banque (« B… », banque.py) et relevés de cartes de crédit (« C-… », cartes.py) (avant le 12/10/2026 : « E… » seuls ;
    un virement daté dans le futur ne se réalisait jamais)."""
    import grand_livre as gl
    t = maintenant_simule()
    limite = jusqua or (t.replace(tzinfo=None) if t else None)
    if limite is None:
        return []
    livre = gl.lire()
    faits = []
    for l in livre:
        if l["type"] == "prevu" and l["reference"].startswith(("E", "B", "C-")) and gl.quand(l) <= limite:
            l["type"] = "prevu_realise"
            faits.append(l)
    if faits and not simule:
        gl.ecrire(livre)
    return faits


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("liste")
    sp.add_parser("verifier")
    p = sp.add_parser("prevoir")
    p.add_argument("--jusqua", required=True)
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("realiser")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("budget")
    p.add_argument("mois", help="AAAA-MM")
    args = ap.parse_args()
    t = maintenant_simule()
    aujourd = t.date() if t else dt.date(2040, 7, 14)
    if args.cmd == "liste":
        for l in lire():
            prochaine = occurrences(l, aujourd, aujourd + dt.timedelta(days=400))
            vers = f" → {l['contrepartie']}" if l.get("contrepartie") else ""
            pret = f" ; prêt {l['pret']} (tableau d'amortissement)" if l.get("pret") else ""
            print(f"{l['id']} [{l['statut']:9s}] {l['libelle']} : {float(l['montant']):+.2f} € sur {l['compte']}{vers} "
                  f"({l['periodicite']}, jour {l['jour']}){pret} ; prochaine : {prochaine[0] if prochaine else '—'} ; "
                  f"source : {l['source']}")
        return 0
    if args.cmd == "verifier":
        erreurs, aver = verifier()
        for e in erreurs:
            print("ERREUR", e)
        for x in aver:
            print("RELIRE", x)
        print("echeancier.csv :", "des erreurs" if erreurs else "conforme", f"({len(lire())} lignes)")
        return 1 if erreurs else 0
    if args.cmd == "prevoir":
        ajouts = prevoir(dt.date.fromisoformat(args.jusqua), simule=args.simule)
        for a in ajouts:
            print(f"  prévu {a['date']} {a['compte']:8s} {float(a['montant']):+10.2f} €  {a['libelle']}  [{a['reference']}]")
        print(f"{len(ajouts)} prévu(s) {'à écrire (essai)' if args.simule else 'écrit(s)'} dans etat/grand-livre.csv")
        return 0
    if args.cmd == "realiser":
        faits = realiser(simule=args.simule)
        for l in faits:
            print(f"  réalisé {l['date']} {l['heure']} {l['compte']:8s} {float(l['montant']):+10.2f} €  {l['libelle']}")
        print(f"{len(faits)} mouvement(s) réalisé(s)")
        return 0
    if args.cmd == "budget":
        a, m = (int(x) for x in args.mois.split("-"))
        du = dt.date(a, m, 1)
        au = dt.date(a + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1)
        par_compte = {}
        evts = sorted(((d, l) for l in lire() for d in occurrences(l, du, au)), key=lambda x: x[0])
        for d, l in evts:
            if l["statut"] != "actif":
                print(f"  {d} {float(l['montant']):+10.2f} €  {l['libelle']}  ({l['statut']} : non compté)")
                continue
            for mv in mouvements(l, d):
                x = float(mv["montant"])
                par_compte[mv["compte"]] = par_compte.get(mv["compte"], 0.0) + x
                print(f"  {d} {mv['compte']:12s} {x:+10.2f} €  {mv['libelle']}")
        for c, x in par_compte.items():
            print(f"Solde des lignes actives sur {args.mois}, compte {c} : {x:+.2f} €")
        if not par_compte:
            print(f"Solde des lignes actives sur {args.mois} : +0.00 €")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
