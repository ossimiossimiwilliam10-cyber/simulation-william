"""TÉLÉPHONE EN CORÉE (créé le 22/10/2026 ; proposition R2 de la revue du lundi n° 1 de l'univers 3, validée par l'utilisateur) : hors
Union européenne, l'itinérance de l'opérateur luxembourgeois coûte cher ; à l'arrivée à Séoul William choisit une eSIM, une SIM
physique ou, faute de mieux, un pass journalier d'itinérance (Wi-Fi libre à l'aéroport et dans la plupart des cafés).

    python outils/mobile.py options                                           # offres et prix projetés (prix.py, × 1,35)
    python outils/mobile.py acheter --option esim_30j_3go --quand "2041-07-22 10:00" [--carte visa_debit] [--simule]
    python outils/mobile.py acheter --option passe_itinerance --quand "…" --carte facture   # pass journalier, facturé le mois suivant
    python outils/mobile.py etat [--quand "…"]                                # forfait en cours ?
    python outils/mobile.py verifier

Règles : eSIM et SIM se paient par carte à l'achat (plafond contrôlé par cartes.py) et valent du moment de l'achat à la durée du forfait ;
le pass d'itinérance se facture sur la facture mensuelle (ligne « prevu » au grand livre, le 5 du mois suivant). Sans forfait ni pass,
William n'a que le Wi-Fi : le moteur ne lui fait pas utiliser de données mobiles sans qu'il l'ait voulu ; s'il en utilise malgré tout
(décision du joueur), le moteur applique le pass journalier. Données : `donnees/mobile.csv` ; état : `etat/mobile.csv`.
"""
import argparse
import datetime as dt
import sys

from commun import DONNEES, ETAT, OUTILS, analyser_instant_naif, ecrire_csv, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
OPTIONS = DONNEES / "mobile.csv"
ETAT_MOBILE = ETAT / "mobile.csv"
COL = ["id", "achat", "debut", "fin", "option", "montant_eur", "carte", "note"]


def options():
    return lire_csv(OPTIONS)


def option(ident):
    o = next((x for x in options() if x["id"] == ident), None)
    if o is None:
        sys.exit(f"Offre inconnue : {ident} ({', '.join(x['id'] for x in options())})")
    return o


def prix_eur(o):
    import prix as P
    px = next((p for p in P.lire() if p["id"] == o["prix"]), None)
    if px is None:
        sys.exit(f"Prix {o['prix']} absent de donnees/prix.csv")
    return round(float(px["prix_2026"]) * P.coef(px), 2)


def lignes():
    return lire_csv(ETAT_MOBILE) if ETAT_MOBILE.exists() else []


def naif(t=None):
    t = t or maintenant_simule()
    return t.replace(tzinfo=None) if getattr(t, "tzinfo", None) else t


def en_cours(t=None):
    """Lignes d'état actives à l'instant `t` (forfaits et pass)."""
    t = naif(t)
    return [l for l in lignes() if l["debut"] <= f"{t:%Y-%m-%d %H:%M}" <= l["fin"]]


def forfait(t=None):
    """Forfait local (eSIM ou SIM) en cours, ou None."""
    for l in en_cours(t):
        o = next((x for x in options() if x["id"] == l["option"]), None)
        if o and o["type"] in ("esim", "sim"):
            return l, o
    return None


def reseau_court(t=None):
    if forfait(t):
        return "SIM locale" if forfait(t)[1]["type"] == "sim" else "eSIM"
    return "itinérance"


def acheter(ident, quand, carte="visa_debit", simule=False):
    """Achat d'un forfait : paiement par carte (eSIM, SIM) ou ligne de facture (pass d'itinérance). Renvoie (réussi, message)."""
    o = option(ident)
    montant = prix_eur(o)
    jours = int(o["jours"])
    fin = quand + dt.timedelta(days=jours)
    rows = lignes()
    mid = f"MB{len(rows) + 1:03d}"
    if o["type"] == "itinerance" or carte == "facture":
        if o["type"] != "itinerance":
            return False, "seul le pass d'itinérance se facture : une eSIM ou une SIM se paie par carte"
        d = dt.date(quand.year + (quand.month == 12), quand.month % 12 + 1, 5)
        if not simule:
            import grand_livre as gl
            livre = gl.lire()
            livre.append({"date": d.isoformat(), "heure": "06:00", "compte": "courant", "montant": f"{-montant:.2f}", "type": "prevu",
                          "libelle": f"Facture de l'opérateur mobile : pass d'itinérance du {quand:%d/%m/%Y} (Corée du Sud)",
                          "reference": f"P-{mid}"})
            gl.ecrire(livre)
        msg = f"{o['nom']} : {montant:.2f} € sur la facture mensuelle du {d:%d/%m/%Y}"
        payee = "facture"
    else:
        import cartes
        ok, op = cartes.payer(carte, montant, f"{o['nom']} (Corée du Sud)", quand, reference=mid, note=f"forfait mobile {ident}", simule=simule)
        if not ok:
            return False, f"paiement refusé : {op['note']}"
        msg = f"{o['nom']} : {montant:.2f} € payés par {carte} ; valable jusqu'au {fin:%d/%m/%Y %H:%M}"
        payee = carte
    if not simule:
        rows.append({"id": mid, "achat": f"{quand:%Y-%m-%d %H:%M}", "debut": f"{quand:%Y-%m-%d %H:%M}", "fin": f"{fin:%Y-%m-%d %H:%M}",
                     "option": ident, "montant_eur": f"{montant:.2f}", "carte": payee, "note": o["nom"]})
        ecrire_csv(ETAT_MOBILE, rows, COL)
    return True, msg


def donnees_telephone(t=None):
    """Bloc affiché par l'application Portefeuille quand William est à Séoul : réseau actuel et offres (None ailleurs)."""
    import meteo
    if meteo.station_courante() != "seoul":
        return None
    t = naif(t)
    f = forfait(t)
    if f:
        l, o = f
        fin = dt.datetime.fromisoformat(l["fin"])
        reseau = f"{o['nom']}, jusqu'au {fin:%d/%m/%Y}"
        detail = f"{o['donnees']} de données, {o['jours']} jours"
    elif any(x for x in en_cours(t)):
        reseau, detail = "Itinérance de ton opérateur (pass journalier activé)", "facturé sur ta facture mensuelle"
    else:
        reseau, detail = "Wi-Fi seulement : aucun forfait local", "l'itinérance hors Union européenne coûte cher ; le Wi-Fi est libre à l'aéroport et dans la plupart des cafés"
    return {"reseau": reseau, "forfait": detail, "options": [
        {"id": o["id"], "type": o["type"], "nom": o["nom"], "jours": int(o["jours"]), "donnees": o["donnees"], "prix": prix_eur(o),
         "lieu": o["lieu"], "note": o["note"]} for o in options()]}


def verifier():
    import prix as P
    erreurs = []
    ids = {p["id"] for p in P.lire()}
    for o in options():
        if o["prix"] not in ids:
            erreurs.append(f"mobile.csv : prix inconnu {o['prix']} ({o['id']})")
        if o["type"] not in ("esim", "sim", "itinerance"):
            erreurs.append(f"mobile.csv : type inconnu ({o['id']})")
    return erreurs


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("options")
    p = sp.add_parser("acheter")
    p.add_argument("--option", required=True)
    p.add_argument("--quand")
    p.add_argument("--carte", default="visa_debit")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("etat")
    p.add_argument("--quand")
    sp.add_parser("verifier")
    a = ap.parse_args()
    if a.cmd == "options":
        for o in options():
            print(f"{o['id']:16s} {o['nom']:55s} {prix_eur(o):7.2f} € · {o['lieu']}")
        return 0
    if a.cmd == "acheter":
        quand = analyser_instant_naif(a.quand) if a.quand else naif()
        ok, msg = acheter(a.option, quand, a.carte, a.simule)
        print(("RÉUSSI : " if ok else "REFUSÉ : ") + msg + (" (essai : rien d'écrit)" if a.simule else ""))
        return 0 if ok else 2
    if a.cmd == "etat":
        t = analyser_instant_naif(a.quand) if a.quand else naif()
        f = forfait(t)
        print(f"Réseau : {reseau_court(t)}" + (f" ({f[1]['nom']}, jusqu'au {f[0]['fin']})" if f else " (aucun forfait local)"))
        return 0
    e = verifier()
    for x in e:
        print("ERREUR", x)
    print("mobile : OK" if not e else f"{len(e)} erreur(s)")
    return 1 if e else 0


if __name__ == "__main__":
    sys.exit(main())
