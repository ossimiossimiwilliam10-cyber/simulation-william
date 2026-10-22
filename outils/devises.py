"""ARGENT SUR PLACE (créé le 14/10/2026, demande de l'utilisateur : « la simulation doit être surtout informatique ») : taux de
change du jour, paiements par carte en devise, retraits au distributeur, espèces. Calcul DÉTERMINISTE une fois le taux du jour tiré :
le moteur, l'application « Portefeuille » du téléphone et les autres outils (courses.py, voyages.py) donnent le même montant.

    python outils/devises.py taux [--jour AAAA-MM-JJ] [--devise PHP]          # taux du jour (tiré une fois, etat/taux.csv)
    python outils/devises.py convertir 850 PHP                                # en euros, au cours du jour (moyen et Visa)
    python outils/devises.py payer --carte visa_debit --montant 850 --devise PHP --marchand "…" [--quand "…"] [--reference …] [--simule]
    python outils/devises.py retirer --carte visa_debit --montant 10000 --distributeur bdo_naia3 [--quand "…"] [--simule]
    python outils/devises.py depenser --montant 120 --devise PHP --libelle "7-Eleven : eau" [--quand "…"] [--simule]
    python outils/devises.py especes                                          # espèces en poche (grand livre)
    python outils/devises.py distributeurs [--lieu naia_t3]
    python outils/devises.py verifier

RÈGLES
- Taux : marche au hasard rappelée vers la référence (donnees/devises.csv), tirée UNE fois par jour et consignée dans
  etat/taux.csv ; jamais rejouée. Le réseau Visa convertit à un cours un peu moins favorable (écart de la colonne ecart_visa).
- Paiement par carte en devise : montant / cours Visa + frais de la banque de William (donnees/frais-cartes.csv) ; le TOTAL passe
  par cartes.payer (plafond de la carte, refus consigné, débit immédiat ou relevé) : la même règle partout.
- Retrait : multiple du distributeur, plafond par retrait ; frais de l'exploitant (en devise) ajoutés au montant débité, puis frais
  de la banque ; si la carte l'autorise, les billets entrent dans le compte d'espèces du grand livre (especes_php).
- Espèces : une dépense en espèces est REFUSÉE si William n'a pas la somme en poche (rien n'est écrit).
- Projection 2040 : frais et plafonds des distributeurs × 1,35 (même coefficient que prix.py) ; le taux de référence reste celui de 2026.
"""
import argparse
import datetime as dt
import random
import sys

from commun import DONNEES, ETAT, OUTILS, analyser_instant_naif, ecrire_csv, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
DEVISES = DONNEES / "devises.csv"
FRAIS = DONNEES / "frais-cartes.csv"
DISTRIBUTEURS = DONNEES / "distributeurs.csv"
TAUX = ETAT / "taux.csv"
COL_TAUX = ["date", "devise", "taux", "tire_le"]
COEF = 1.35
DEBUT = dt.date(2041, 7, 16)  # premier jour de l'univers 3 (avant : 14/07/2040, univers 2)
COMPTE_ESPECES = {"PHP": "especes_php", "KRW": "especes_krw", "EUR": "especes_eur"}


def devise(code):
    d = next((x for x in lire_csv(DEVISES) if x["devise"] == code), None)
    if d is None:
        sys.exit(f"Devise inconnue : {code} (donnees/devises.csv)")
    return d


def _lus(code):
    return {l["date"]: float(l["taux"]) for l in lire_csv(TAUX) if l["devise"] == code}


def taux(jour, code="KRW", simule=False):
    """Taux moyen du jour (unités de devise pour 1 €) ; tire les jours manquants une fois pour toutes."""
    d = devise(code)
    ref, vol, rappel = float(d["reference_eur"]), float(d["volatilite_jour"]), float(d["rappel"])
    lus = _lus(code)
    if jour.isoformat() in lus:
        return lus[jour.isoformat()]
    lignes = lire_csv(TAUX)
    connus = sorted(k for k in lus if k < jour.isoformat())
    x = lus[connus[-1]] if connus else ref
    j = dt.date.fromisoformat(connus[-1]) + dt.timedelta(days=1) if connus else min(DEBUT, jour)
    rng = random.SystemRandom()
    nouveaux = []
    while j <= jour:
        x = x + rappel * (ref - x) + rng.gauss(0, vol * ref)
        nouveaux.append({"date": j.isoformat(), "devise": code, "taux": f"{x:.4f}", "tire_le": f"{dt.datetime.now():%Y-%m-%dT%H:%M}"})
        j += dt.timedelta(days=1)
    if not simule:
        ecrire_csv(TAUX, lignes + nouveaux, COL_TAUX)
    return round(x, 4)


def taux_connu(code="KRW", jour=None):
    """Dernier taux déjà tiré à cette date (lecture seule) ; la référence si aucun : pour le patrimoine et l'affichage."""
    jour = jour or maintenant_simule().date()
    lus = _lus(code)
    avant = sorted(k for k in lus if k <= jour.isoformat())
    return lus[avant[-1]] if avant else float(devise(code)["reference_eur"])


def cours_visa(jour, code="KRW", simule=False):
    return round(taux(jour, code, simule) * (1 - float(devise(code)["ecart_visa"])), 4)


def frais_banque(carte, operation, eur):
    f = next((x for x in lire_csv(FRAIS) if x["carte"] == carte and x["operation"] == operation), None)
    if f is None:
        return 0.0, "aucun frais connu"
    pct, fixe = float(f["pourcentage"]), float(f["fixe_eur"] or 0)
    return round(eur * pct / 100 + fixe, 2), f"{pct:g} % + {fixe:.2f} €".replace(".", ",")


def eur(x):
    return f"{x:,.2f} €".replace(",", " ").replace(".", ",")


def mt(x, code="KRW"):
    return (f"{x:,.0f}" if abs(x - round(x)) < 0.005 else f"{x:,.2f}").replace(",", " ").replace(".", ",") + f" {code}"


def maintenant_naif():
    return maintenant_simule().replace(tzinfo=None)


def estimer_carte(carte, montant, code, jour, operation="paiement", frais_local=0.0):
    """Ce que William paiera en euros (sans rien écrire) : le même calcul pour la page et pour le moteur."""
    c = cours_visa(jour, code, simule=True)
    base = (montant + frais_local) / c
    fb, bareme = frais_banque(carte, operation, base)
    return {"cours": c, "base_eur": round(base, 2), "frais_eur": fb, "bareme": bareme, "total_eur": round(base + fb, 2)}


def payer(carte, montant, code, marchand, quand=None, reference="", simule=False):
    """Paiement par carte en devise ; le total en euros (frais compris) passe par cartes.payer. Renvoie (autorisé, détail)."""
    import cartes
    quand = quand or maintenant_naif()
    c = cours_visa(quand.date(), code, simule)
    base = montant / c
    fb, bareme = frais_banque(carte, "paiement", base)
    total = round(base + fb, 2)
    note = f"{mt(montant, code)} au cours Visa {c:.4f} = {eur(base)} · frais hors zone euro {eur(fb)} ({bareme})"
    ok, op = cartes.payer(carte, total, f"{marchand} ({mt(montant, code)})", quand, reference=reference, note=note, simule=simule)
    return ok, {"operation": op, "total_eur": total, "cours": c, "frais_eur": fb, "note": note}


def distributeurs(lieu=None):
    return [d for d in lire_csv(DISTRIBUTEURS) if not lieu or d["lieu"] == lieu]


def distributeur(ident):
    d = next((x for x in lire_csv(DISTRIBUTEURS) if x["id"] == ident), None)
    if d is None:
        sys.exit(f"Distributeur inconnu : {ident} (donnees/distributeurs.csv)")
    return d


def frais_local(d):
    return round(float(d["frais_2026"]) * COEF)


def plafond(d):
    return round(float(d["plafond_2026"]) * COEF / 100) * 100


def retirer(carte, montant, ident, quand=None, simule=False):
    """Retrait au distributeur : (réussi, message, détail). Les billets entrent dans les espèces si la carte l'autorise."""
    import cartes
    import grand_livre as gl
    quand = quand or maintenant_naif()
    d = distributeur(ident)
    code, mult = d["devise"], int(d["multiple"] or 100)
    if montant <= 0 or montant % mult:
        return False, f"montant refusé par le distributeur : multiple de {mult} {code} attendu", {}
    if montant > plafond(d):
        return False, f"montant refusé par le distributeur : {mt(plafond(d), code)} au plus par retrait", {}
    fl = frais_local(d)
    c = cours_visa(quand.date(), code, simule)
    base = (montant + fl) / c
    fb, bareme = frais_banque(carte, "retrait", base)
    total = round(base + fb, 2)
    note = (f"{mt(montant, code)} + frais du distributeur {mt(fl, code)} au cours Visa {c:.4f} = {eur(base)} · frais de retrait "
            f"hors zone euro {eur(fb)} ({bareme})")
    ok, op = cartes.payer(carte, total, f"Retrait {d['banque']} : {mt(montant, code)}", quand, note=note, simule=simule)
    if not ok:
        return False, f"retrait refusé par la banque de la carte : {op['note']}", {"operation": op}
    if not simule:
        livre = gl.lire()
        livre.append({"date": quand.date().isoformat(), "heure": f"{quand:%H:%M}", "compte": COMPTE_ESPECES[code],
                      "montant": f"{montant:.2f}", "type": "mouvement", "libelle": f"Retrait {d['banque']} ({d['lieu']}) avec la {carte}",
                      "reference": op["id"]})
        gl.ecrire(livre)
    return True, f"{mt(montant, code)} retirés ; débité : {eur(total)}", {"operation": op, "total_eur": total, "frais_local": fl, "note": note}


def especes(quand=None):
    import grand_livre as gl
    quand = quand or maintenant_naif()
    s = gl.soldes(quand)
    return {code: round(s.get(compte, 0.0), 2) for code, compte in COMPTE_ESPECES.items()}


def depenser(montant, code, libelle, quand=None, simule=False):
    """Dépense en espèces : refusée si William n'a pas la somme (rien n'est écrit)."""
    import grand_livre as gl
    quand = quand or maintenant_naif()
    poche = especes(quand).get(code, 0.0)
    if montant > poche + 1e-9:
        return False, f"pas assez d'espèces : {mt(poche, code)} en poche pour {mt(montant, code)}"
    if not simule:
        livre = gl.lire()
        livre.append({"date": quand.date().isoformat(), "heure": f"{quand:%H:%M}", "compte": COMPTE_ESPECES[code],
                      "montant": f"{-montant:.2f}", "type": "mouvement", "libelle": f"Espèces : {libelle}", "reference": ""})
        gl.ecrire(livre)
    return True, f"{mt(montant, code)} payés en espèces ; reste {mt(poche - montant, code)}"


def donnees_telephone(t=None):
    """Portefeuille : espèces, taux du jour (moyen et Visa), frais connus, distributeurs de la ville où se trouve William."""
    t = t or maintenant_simule()
    naif = t.replace(tzinfo=None)
    import meteo
    ville = meteo.station_courante()
    pays, code = {"manille": ("ph", "PHP"), "seoul": ("kr", "KRW")}.get(ville, ("", ""))  # 22/10/2026 : Séoul
    poche = especes(naif)
    res = {"especes": poche, "devises": [], "code": code}
    if pays:
        tx = taux_connu(code, naif.date())
        c = round(tx * (1 - float(devise(code)["ecart_visa"])), 4)
        res["devises"].append({"code": code, "nom": devise(code)["nom"], "taux": tx, "cours_visa": c})
        res["frais"] = [{"carte": f["carte"], "operation": f["operation"], "pourcentage": float(f["pourcentage"]),
                         "fixe": float(f["fixe_eur"] or 0)} for f in lire_csv(FRAIS)]
        import lieux
        noms = {i: l["nom"] for i, l in lieux.lire().items()}
        res["distributeurs"] = [{"id": d["id"], "banque": d["banque"], "lieu": noms.get(d["lieu"], d["lieu"]), "frais": frais_local(d),
                                 "plafond": plafond(d), "devise": d["devise"]} for d in distributeurs() if d["pays"] == pays]
    return res


def verifier():
    erreurs = []
    codes = {d["devise"] for d in lire_csv(DEVISES)}
    for f in lire_csv(FRAIS):
        try:
            float(f["pourcentage"]), float(f["fixe_eur"] or 0)
        except ValueError:
            erreurs.append(f"frais-cartes.csv : nombre illisible ({f['carte']} {f['operation']})")
    for d in lire_csv(DISTRIBUTEURS):
        if d["devise"] not in codes:
            erreurs.append(f"distributeurs.csv : devise inconnue ({d['id']})")
    vus = set()
    for l in lire_csv(TAUX):
        k = (l["date"], l["devise"])
        if k in vus:
            erreurs.append(f"taux.csv : jour tiré deux fois ({l['date']} {l['devise']})")
        vus.add(k)
    return erreurs


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("taux")
    s.add_argument("--jour")
    s.add_argument("--devise", default="KRW")
    s = sub.add_parser("convertir")
    s.add_argument("montant", type=float)
    s.add_argument("devise")
    s.add_argument("--carte", default="visa_debit")
    for nom in ("payer", "retirer", "depenser"):
        s = sub.add_parser(nom)
        s.add_argument("--montant", type=float, required=True)
        s.add_argument("--quand")
        s.add_argument("--simule", action="store_true")
        if nom in ("payer", "depenser"):
            s.add_argument("--devise", default="KRW")
        if nom in ("payer", "retirer"):
            s.add_argument("--carte", default="visa_debit")
        if nom == "payer":
            s.add_argument("--marchand", required=True)
            s.add_argument("--reference", default="")
        if nom == "retirer":
            s.add_argument("--distributeur", required=True)
        if nom == "depenser":
            s.add_argument("--libelle", required=True)
    sub.add_parser("especes")
    s = sub.add_parser("distributeurs")
    s.add_argument("--lieu")
    sub.add_parser("verifier")
    a = ap.parse_args()
    quand = analyser_instant_naif(a.quand) if getattr(a, "quand", None) else None
    if a.cmd == "taux":
        j = dt.date.fromisoformat(a.jour) if a.jour else maintenant_naif().date()
        tx = taux(j, a.devise)
        print(f"{j:%d/%m/%Y} : 1 € = {tx:.4f} {a.devise} (cours Visa : {cours_visa(j, a.devise):.4f})")
    elif a.cmd == "convertir":
        j = maintenant_naif().date()
        e = estimer_carte(a.carte, a.montant, a.devise.upper(), j)
        print(f"{mt(a.montant, a.devise.upper())} = {eur(a.montant / taux(j, a.devise.upper()))} au cours moyen · par carte ({a.carte}) : "
              f"{eur(e['total_eur'])} (cours Visa {e['cours']:.4f}, frais {eur(e['frais_eur'])} : {e['bareme']})")
    elif a.cmd == "payer":
        ok, x = payer(a.carte, a.montant, a.devise.upper(), a.marchand, quand, a.reference, a.simule)
        print(("AUTORISÉ" if ok else "REFUSÉ") + f" : {eur(x['total_eur'])} · {x['note']}" + ("" if ok else f" · {x['operation']['note']}")
              + (" (essai : rien d'écrit)" if a.simule else ""))
    elif a.cmd == "retirer":
        ok, msg, _ = retirer(a.carte, a.montant, a.distributeur, quand, a.simule)
        print(("RÉUSSI" if ok else "REFUSÉ") + f" : {msg}" + (" (essai : rien d'écrit)" if a.simule else ""))
    elif a.cmd == "depenser":
        ok, msg = depenser(a.montant, a.devise.upper(), a.libelle, quand, a.simule)
        print(("PAYÉ" if ok else "REFUSÉ") + f" : {msg}" + (" (essai : rien d'écrit)" if a.simule else ""))
    elif a.cmd == "especes":
        for code, x in especes().items():
            print(f"{code} : {mt(x, code)}")
    elif a.cmd == "distributeurs":
        for d in distributeurs(a.lieu):
            print(f"{d['id']:24s} {d['banque']:14s} {d['lieu']:18s} frais {mt(frais_local(d), d['devise'])} · plafond {mt(plafond(d), d['devise'])}")
    elif a.cmd == "verifier":
        e = verifier()
        print("\n".join(e) if e else "devises : OK")
        return 1 if e else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
