"""ÉCHÉANCIER des mouvements d'argent récurrents (créé le 11/10/2026) : traitement, crédit, énergie, internet, club, impôts…
Dans l'univers 1, le compte courant ne bougeait que si le récit parlait d'argent (la mensualité de ≈ 940 € et l'électricité
n'ont jamais été prélevées : piège n° 77). Ici, chaque ligne ACTIVE de `etat/echeancier.csv` produit ses « prévus » dans le grand
livre, qui deviennent des mouvements réels quand l'horloge passe leur date (`tour.py fin` le fait automatiquement).

    python outils/echeancier.py liste                       # les lignes, leur prochaine date, leur statut
    python outils/echeancier.py prevoir --jusqua 2040-09-30 # écrit les prévus manquants dans etat/grand-livre.csv
    python outils/echeancier.py realiser                    # les prévus échus (à l'horloge) deviennent des mouvements
    python outils/echeancier.py budget 2040-08              # ce qui sort et entre ce mois-là (moteur)

Colonnes : id;libelle;compte;montant;periodicite;jour;mois;heure;debut;fin;statut;source;note
- periodicite : mensuel | trimestriel | semestriel | annuel | ponctuel ; jour : 1-31, « dernier_ouvre » ou « premier_ouvre » ;
  mois : pour annuel « 10 », semestriel « 3,9 », trimestriel « 1,4,7,10 » ; ponctuel : la date est `debut`.
- statut : actif (produit des mouvements) | a_valider (montant ou existence à confirmer par l'utilisateur : rien n'est produit)
  | suspendu | termine. Un montant estimé le dit dans `source` ; on le remplace par le vrai dès qu'une pièce le donne.
- La référence d'un prévu est « Eid-AAAAMMJJ » : jamais de doublon, et l'historique reste lisible.
"""
import argparse
import datetime as dt
import sys

from commun import ETAT, OUTILS, ecrire_csv, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
FICHIER = ETAT / "echeancier.csv"
COLONNES = ["id", "libelle", "compte", "montant", "periodicite", "jour", "mois", "heure", "debut", "fin", "statut", "source", "note"]
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
            ref = f"{l['id']}-{d:%Y%m%d}"
            if ref in refs:
                continue
            ajouts.append({"date": d.isoformat(), "heure": l.get("heure") or "06:00", "compte": l["compte"],
                           "montant": f"{float(l['montant']):.2f}", "type": "prevu", "libelle": l["libelle"], "reference": ref})
    if ajouts and not simule:
        gl.ecrire(livre + ajouts)
    return ajouts


def realiser(jusqua=None, simule=False):
    """Les prévus de l'échéancier dont la date/heure est passée à l'horloge deviennent des mouvements (prevu_realise)."""
    import grand_livre as gl
    t = maintenant_simule()
    limite = jusqua or (t.replace(tzinfo=None) if t else None)
    if limite is None:
        return []
    livre = gl.lire()
    faits = []
    for l in livre:
        if l["type"] == "prevu" and l["reference"].startswith("E") and gl.quand(l) <= limite:
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
            print(f"{l['id']} [{l['statut']:9s}] {l['libelle']} : {float(l['montant']):+.2f} € sur {l['compte']} ({l['periodicite']}, "
                  f"jour {l['jour']}) ; prochaine : {prochaine[0] if prochaine else '—'} ; source : {l['source']}")
        return 0
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
        total = 0.0
        evts = sorted(((d, l) for l in lire() for d in occurrences(l, du, au)), key=lambda x: x[0])
        for d, l in evts:
            marque = "" if l["statut"] == "actif" else f"  ({l['statut']} : non compté)"
            print(f"  {d} {float(l['montant']):+10.2f} €  {l['libelle']}{marque}")
            if l["statut"] == "actif":
                total += float(l["montant"])
        print(f"Solde des lignes actives sur {args.mois} : {total:+.2f} €")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
