"""CARTES BANCAIRES DE WILLIAM (créé le 12/10/2026, après le paiement refusé du forfait pour Manille) : plafonds, paiements, relevés.
Biographie fixée par l'utilisateur le 12/10/2026 : package Zebra Premium de la Spuerkeess (F062) : une Visa Debit (limite par défaut
de 2 500 € par mois, retraits, magasins et internet confondus : F059) et une Visa Premier à crédit (limite mensuelle de 5 000 €,
estimation acceptée par l'utilisateur ; hausse temporaire ou définitive demandable dans S-Net : F061 ; relevé clos le pénultième jour
ouvré du mois, solde débité du compte courant en une fois au début du mois suivant : F063).

    python outils/cartes.py liste [--au "AAAA-MM-JJ HH:MM"]        # cartes, plafond, utilisé, disponible, prochain débit du relevé
    python outils/cartes.py payer --carte visa_premier --montant 4890 --marchand "Kestrel Voyages" --quand "…" [--reference R003] [--simule]
    python outils/cartes.py limite --carte visa_premier --montant 8000 --quand "…" [--jusqua AAAA-MM-JJ]   # limite changée (temporaire si --jusqua)
    python outils/cartes.py verifier

RÈGLES : un paiement est AUTORISÉ s'il tient dans le disponible de la période (limite − paiements autorisés de la période) ; sinon il
est REFUSÉ (consigné, rien n'est débité). Carte de débit : débit immédiat du compte courant (grand livre, « mouvement »). Carte de
crédit : rien ne bouge sur le compte courant le jour du paiement ; le relevé de la période est débité en une fois à la date de débit
(un seul « prévu » par relevé au grand livre, référence « C-<carte>-<clôture> », réalisé par `tour.py fin`). Une hausse de limite se
joue d'abord dans la fiction (S-Net, friction, accord de la banque) ; `limite` l'enregistre ensuite. Un retrait au distributeur passe
par `payer` (marchand « Retrait … »). Les outils qui paient (voyages.py --carte) appellent `payer` : la même règle partout.
Fichiers : `etat/cartes.csv` (cartes et limites), `etat/cartes-operations.csv` (autorisations et refus).
"""
import argparse
import datetime as dt
import sys

from commun import ETAT, OUTILS, ecrire_csv, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
CARTES = ETAT / "cartes.csv"
OPERATIONS = ETAT / "cartes-operations.csv"
COL_CARTES = ["id", "nom", "type", "compte", "limite", "limite_temp", "temp_jusqua", "periode", "debit_jour", "statut", "source", "note"]
COL_OPS = ["id", "date", "heure", "carte", "montant", "marchand", "statut", "periode", "debit", "reference", "note"]


def lire(p):
    return lire_csv(p) if p.exists() else []


def carte(ident):
    for c in lire(CARTES):
        if c["id"] == ident:
            return c
    sys.exit(f"Carte inconnue : {ident} ({', '.join(c['id'] for c in lire(CARTES))})")


def ouvre(d):
    import calendrier_2040 as cal
    return d.weekday() < 5 and d not in cal.jours_feries(d.year, "lu")


def cloture(annee, mois):
    """Clôture du relevé d'une carte de crédit : pénultième jour ouvré du mois (F063)."""
    import calendrier_2040 as cal
    d = cal.dernier_ouvre(annee, mois, "lu") - dt.timedelta(days=1)
    while not ouvre(d):
        d -= dt.timedelta(days=1)
    return d


def mois_suivant(annee, mois, n=1):
    m = mois - 1 + n
    return annee + m // 12, m % 12 + 1


def periode(c, jour):
    """(début, fin) de la période de plafond qui contient `jour` ; pour une carte de crédit, fin = clôture du relevé."""
    if c["periode"] == "mois":
        debut = jour.replace(day=1)
        a, m = mois_suivant(jour.year, jour.month)
        return debut, dt.date(a, m, 1) - dt.timedelta(days=1)
    fin = cloture(jour.year, jour.month)
    if jour > fin:
        fin = cloture(*mois_suivant(jour.year, jour.month))
    a, m = mois_suivant(fin.year, fin.month, -1)
    return cloture(a, m) + dt.timedelta(days=1), fin


def date_debit(c, fin):
    """Débit du relevé : le jour `debit_jour` du mois qui suit la clôture, reporté au jour ouvré suivant (F063 : vers le 7)."""
    a, m = mois_suivant(fin.year, fin.month)
    d = dt.date(a, m, int(c["debit_jour"] or 7))
    while not ouvre(d):
        d += dt.timedelta(days=1)
    return d


def limite(c, jour):
    if c.get("limite_temp") and c.get("temp_jusqua") and jour <= dt.date.fromisoformat(c["temp_jusqua"]):
        return float(c["limite_temp"])
    return float(c["limite"])


def utilise(c, jour, ops=None):
    debut, fin = periode(c, jour)
    ops = lire(OPERATIONS) if ops is None else ops
    return sum(float(o["montant"]) for o in ops if o["carte"] == c["id"] and o["statut"] == "autorise"
               and debut.isoformat() <= o["date"] <= fin.isoformat())


def etat(c, jour):
    debut, fin = periode(c, jour)
    lim = limite(c, jour)
    u = utilise(c, jour)
    x = {"id": c["id"], "nom": c["nom"], "type": c["type"], "limite": lim, "utilise": round(u, 2), "disponible": round(max(lim - u, 0), 2),
         "debut": debut.isoformat(), "fin": fin.isoformat(), "temporaire": lim != float(c["limite"])}
    if c["type"] == "credit":
        x["debit"] = date_debit(c, fin).isoformat()
    return x


def payer(ident, montant, marchand, quand, reference="", note="", simule=False):
    """Autorise ou refuse un paiement ; écrit l'opération et l'argent (débit immédiat ou relevé). Renvoie (autorisé, opération)."""
    import grand_livre as gl
    c = carte(ident)
    if c["statut"] != "active":
        sys.exit(f"Carte {c['nom']} : {c['statut']}")
    jour = quand.date()
    debut, fin = periode(c, jour)
    e = etat(c, jour)
    ok = montant <= e["disponible"] + 1e-9
    ops = lire(OPERATIONS)
    op = {"id": f"K{len(ops) + 1:03d}", "date": jour.isoformat(), "heure": f"{quand:%H:%M}", "carte": c["id"], "montant": f"{montant:.2f}",
          "marchand": marchand, "statut": "autorise" if ok else "refuse", "periode": f"{debut.isoformat()}→{fin.isoformat()}",
          "debit": "", "reference": reference,
          "note": note or ("" if ok else f"limite de la période dépassée : disponible {e['disponible']:.2f} € sur {e['limite']:.2f} €")}
    if ok and c["type"] == "credit":
        op["debit"] = date_debit(c, fin).isoformat()
    if simule:
        return ok, op
    ops.append(op)
    ecrire_csv(OPERATIONS, ops, COL_OPS)
    if ok:
        livre = gl.lire()
        if c["type"] == "debit":
            livre.append({"date": jour.isoformat(), "heure": f"{quand:%H:%M}", "compte": c["compte"], "montant": f"{-montant:.2f}",
                          "type": "mouvement", "libelle": f"{c['nom']} : {marchand}", "reference": op["id"]})
        else:
            ref = f"C-{c['id']}-{fin:%Y%m%d}"
            total = utilise(c, jour, ops)
            ligne = next((l for l in livre if l["reference"] == ref and l["type"] == "prevu"), None)
            if ligne is None:
                ligne = {"date": op["debit"], "heure": "06:00", "compte": c["compte"], "montant": "", "type": "prevu", "libelle": "",
                         "reference": ref}
                livre.append(ligne)
            ligne["montant"] = f"{-total:.2f}"
            somme = f"{total:,.2f}".replace(",", " ").replace(".", ",")
            ligne["libelle"] = f"{c['nom']} : relevé clos le {fin:%d/%m/%Y}, débit du solde ({somme} €)"
        gl.ecrire(livre)
    return ok, op


def changer_limite(ident, montant, quand, jusqua=None):
    cs = lire(CARTES)
    c = next((x for x in cs if x["id"] == ident), None)
    if c is None:
        sys.exit(f"Carte inconnue : {ident}")
    if jusqua:
        c["limite_temp"], c["temp_jusqua"] = f"{montant:.0f}", jusqua
    else:
        c["note"] = (c["note"] + " · " if c["note"] else "") + f"limite {c['limite']} → {montant:.0f} € le {quand:%d/%m/%Y %H:%M}"
        c["limite"], c["limite_temp"], c["temp_jusqua"] = f"{montant:.0f}", "", ""
    ecrire_csv(CARTES, cs, COL_CARTES)
    return c


def releves_a_venir(jour, horizon=62):
    """Débits de relevés de cartes de crédit encore prévus (grand livre), pour le calendrier et la banque du téléphone."""
    import grand_livre as gl
    fin = jour + dt.timedelta(days=horizon)
    noms = {c["id"]: c["nom"] for c in lire(CARTES)}
    res = []
    for l in gl.lire():
        if l["type"] == "prevu" and l["reference"].startswith("C-") and jour.isoformat() <= l["date"] <= fin.isoformat():
            ident = l["reference"].split("-")[1]
            res.append({"date": l["date"], "titre": f"Relevé {noms.get(ident, ident)}", "montant": float(l["montant"])})
    return res


def donnees_telephone(t=None):
    t = t or maintenant_simule()
    jour = t.date()
    ops = [o for o in lire(OPERATIONS) if f"{o['date']} {o['heure']}" <= f"{t:%Y-%m-%d %H:%M}"]
    return {"cartes": [etat(c, jour) for c in lire(CARTES) if c["statut"] == "active"],
            "operations": [{"date": o["date"], "heure": o["heure"], "carte": o["carte"], "montant": float(o["montant"]),
                            "marchand": o["marchand"], "statut": o["statut"], "debit": o["debit"]} for o in reversed(ops[-40:])]}


def verifier():
    erreurs = []
    ids = set()
    for c in lire(CARTES):
        ids.add(c["id"])
        if c["type"] not in ("debit", "credit"):
            erreurs.append(f"cartes.csv : type inconnu ({c['id']})")
        if c["type"] == "credit" and not c["debit_jour"]:
            erreurs.append(f"cartes.csv : jour de débit manquant ({c['id']})")
    for o in lire(OPERATIONS):
        if o["carte"] not in ids:
            erreurs.append(f"cartes-operations.csv : carte inconnue ({o['id']})")
        if o["statut"] not in ("autorise", "refuse", "annule"):
            erreurs.append(f"cartes-operations.csv : statut inconnu ({o['id']} : {o['statut']})")
    return erreurs


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("liste")
    p.add_argument("--au")
    p = sp.add_parser("payer")
    p.add_argument("--carte", required=True)
    p.add_argument("--montant", type=float, required=True)
    p.add_argument("--marchand", required=True)
    p.add_argument("--quand", required=True)
    p.add_argument("--reference", default="")
    p.add_argument("--note", default="")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("limite")
    p.add_argument("--carte", required=True)
    p.add_argument("--montant", type=float, required=True)
    p.add_argument("--quand", required=True)
    p.add_argument("--jusqua")
    sp.add_parser("verifier")
    args = ap.parse_args()
    if args.cmd == "liste":
        t = dt.datetime.fromisoformat(args.au) if args.au else maintenant_simule().replace(tzinfo=None)
        for c in lire(CARTES):
            e = etat(c, t.date())
            print(f"{c['nom']:14s} ({c['type']}) : limite {e['limite']:,.2f} €{' (temporaire)' if e['temporaire'] else ''}, utilisé "
                  f"{e['utilise']:,.2f} €, disponible {e['disponible']:,.2f} € (période du {e['debut']} au {e['fin']})"
                  + (f" ; débit du relevé le {e['debit']}" if "debit" in e else ""))
        return 0
    if args.cmd == "payer":
        ok, op = payer(args.carte, args.montant, args.marchand, dt.datetime.fromisoformat(args.quand), args.reference, args.note, args.simule)
        print(f"{'(essai) ' if args.simule else ''}{op['id']} {'AUTORISÉ' if ok else 'REFUSÉ'} : {args.montant:,.2f} € chez {args.marchand}"
              + (f" ; débit du relevé le {op['debit']}" if op["debit"] else "") + (f" ({op['note']})" if op["note"] else ""))
        return 0 if ok else 2
    if args.cmd == "limite":
        c = changer_limite(args.carte, args.montant, dt.datetime.fromisoformat(args.quand), args.jusqua)
        if args.jusqua:
            print(f"{c['nom']} : limite temporaire de {c['limite_temp']} € jusqu'au {c['temp_jusqua']} (limite ordinaire : {c['limite']} €)")
        else:
            print(f"{c['nom']} : limite de {c['limite']} €")
        return 0
    erreurs = verifier()
    for e in erreurs:
        print("ERREUR", e)
    print("cartes : conforme" if not erreurs else f"{len(erreurs)} erreur(s)")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
