"""PRÊTS de William (créé le 11/10/2026) : tableau d'amortissement CALCULÉ (aujourd'hui : le prêt de la maison d'Audun-le-Tiche).
Avant, la mensualité était une somme fixe sans lien avec le capital restant dû : 110 000 € remboursés à 940 €/mois « jusqu'en
2059 » supposaient un taux d'environ 8 % (incohérence relevée le 11/10/2026 ; l'utilisateur a demandé « un bail réaliste »).

    python outils/prets.py liste                                   # les prêts : mensualité, capital restant dû à l'horloge, fin
    python outils/prets.py tableau PR1 [--de 2040-01 --a 2041-12]  # tableau d'amortissement (intérêts, capital, assurance, CRD)
    python outils/prets.py crd PR1 [--date 2040-07-14]             # capital restant dû à une date
    python outils/prets.py verifier                                # CRD calculé = calage du grand livre (intégré au contrôle)

Fichier : `etat/prets.csv` (une ligne par prêt ; séparateur « ; », jamais de « ; » dans un champ). Colonnes :
id;libelle;preteur;capital;taux;duree_mois;premiere_echeance;assurance_mensuelle;anticipations;compte_capital;compte_actif;
statut;source;note
- taux : nominal annuel fixe, en % ; échéances mensuelles constantes hors assurance, arrondies au centime ; la dernière échéance
  solde le capital (un reliquat de moins de 1 € est repris dans l'échéance où il apparaît) ;
- anticipations : « AAAA-MM-JJ|montant|duree|indemnité », séparées par « / » ; le remboursement anticipé s'impute juste après
  l'échéance de cette date ; « duree » garde la mensualité et raccourcit le prêt, « mensualite » garde la fin et recalcule la
  mensualité ; l'indemnité (IRA) est payée à part (plafond légal en France : 6 mois d'intérêts au taux du prêt sur la somme
  remboursée, sans dépasser 3 % du capital restant dû avant le remboursement, Code de la consommation, art. R313-25 : F041) ;
- compte_capital : compte du grand livre qui porte le capital restant dû (« pret ») ; compte_actif : compte de la part nette du
  bien financé (« maison_part »), qui monte du capital remboursé à chaque échéance (vide si le bien n'est pas suivi).
L'échéancier (`etat/echeancier.csv`, colonne « pret ») écrit chaque échéance au grand livre en trois lignes liées : la mensualité
avec l'assurance (compte courant), le capital remboursé (compte_capital, en baisse) et la même somme sur compte_actif.
"""
import argparse
import datetime as dt
import sys

from commun import ETAT, OUTILS, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
FICHIER = ETAT / "prets.csv"
COLONNES = ["id", "libelle", "preteur", "capital", "taux", "duree_mois", "premiere_echeance", "assurance_mensuelle",
            "anticipations", "compte_capital", "compte_actif", "statut", "source", "note"]


def lire():
    return lire_csv(FICHIER) if FICHIER.exists() else []


def trouver(pid):
    for p in lire():
        if p["id"] == pid:
            return p
    sys.exit(f"Prêt inconnu : {pid} (etat/prets.csv)")


def ajouter_mois(d, n):
    m = d.month - 1 + n
    a, m = d.year + m // 12, m % 12 + 1
    fin_mois = (dt.date(a + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1)).day
    return dt.date(a, m, min(d.day, fin_mois))


def mensualite(capital, taux, n):
    r = float(taux) / 1200
    if n <= 0:
        return round(capital, 2)
    return round(capital * r / (1 - (1 + r) ** -n), 2) if r else round(capital / n, 2)


def anticipations(p):
    res = {}
    for bloc in (p.get("anticipations") or "").split("/"):
        bloc = bloc.strip()
        if not bloc:
            continue
        morceaux = [x.strip() for x in bloc.split("|")]
        d = dt.date.fromisoformat(morceaux[0])
        montant = float(morceaux[1])
        option = morceaux[2] if len(morceaux) > 2 and morceaux[2] else "duree"
        ira = float(morceaux[3]) if len(morceaux) > 3 and morceaux[3] else 0.0
        if option not in ("duree", "mensualite"):
            sys.exit(f"{p['id']} : option de remboursement anticipé inconnue « {option} » (duree ou mensualite)")
        res[d] = (montant, option, ira)
    return res


def tableau(p):
    """Toutes les lignes du prêt, dans l'ordre : échéances (type « echeance ») et remboursements anticipés (« anticipation »)."""
    taux = float(p["taux"])
    r = taux / 1200
    n = int(p["duree_mois"])
    crd = float(p["capital"])
    ass = float(p.get("assurance_mensuelle") or 0)
    d0 = dt.date.fromisoformat(p["premiere_echeance"])
    antic = anticipations(p)
    m = mensualite(crd, taux, n)
    derniere = n  # rang de la dernière échéance prévue (None : le prêt s'arrête quand le capital est remboursé)
    lignes = []
    k = 0
    while crd > 0.004 and k < n + 600:
        k += 1
        d = ajouter_mois(d0, k - 1)
        interet = round(crd * r, 2)
        capital = round(m - interet, 2)
        if capital >= crd - 1.0 or (derniere is not None and k >= derniere):
            capital = round(crd, 2)
        crd = round(crd - capital, 2)
        lignes.append({"type": "echeance", "n": k, "date": d, "echeance": round(capital + interet, 2), "interet": interet,
                       "capital": capital, "assurance": ass, "crd": crd})
        if d in antic and crd > 0:
            montant, option, ira = antic[d]
            montant = min(montant, crd)
            crd = round(crd - montant, 2)
            lignes.append({"type": "anticipation", "n": k, "date": d, "capital": montant, "ira": ira, "option": option, "crd": crd})
            if option == "mensualite":
                m = mensualite(crd, taux, n - k)
                derniere = n
            else:
                derniere = None
    return lignes


def crd(p, quand):
    """Capital restant dû le jour `quand` (après les échéances et remboursements de ce jour)."""
    reste = float(p["capital"])
    for l in tableau(p):
        if l["date"] <= quand:
            reste = l["crd"]
    return reste


def echeance_du_mois(p, annee, mois):
    for l in tableau(p):
        if l["type"] == "echeance" and l["date"].year == annee and l["date"].month == mois:
            return l
    return None


def fin(p):
    return [l for l in tableau(p) if l["type"] == "echeance"][-1]


def mensualite_courante(p, quand):
    """Mensualité hors assurance de la prochaine échéance après `quand` (ou de la dernière, si le prêt est fini)."""
    lignes = [l for l in tableau(p) if l["type"] == "echeance"]
    suivantes = [l for l in lignes if l["date"] > quand]
    return (suivantes[0] if suivantes else lignes[-1])["echeance"]


def aujourd_hui():
    t = maintenant_simule()
    return t.date() if t else dt.date(2040, 7, 14)


def verifier():
    """(erreurs, avertissements) : le capital restant dû calculé doit égaler les calages du compte du prêt au grand livre."""
    import grand_livre as gl
    erreurs, aver = [], []
    livre = gl.lire()
    for p in lire():
        if p["statut"] not in ("actif", "termine"):
            continue
        try:
            lignes = tableau(p)
        except (ValueError, KeyError) as exc:
            erreurs.append(f"prets.csv : {p['id']} illisible ({exc})")
            continue
        compte = p.get("compte_capital") or "pret"
        if compte not in gl.COMPTES:
            erreurs.append(f"prets.csv : {p['id']} compte_capital inconnu « {compte} »")
        if p.get("compte_actif") and p["compte_actif"] not in gl.COMPTES:
            erreurs.append(f"prets.csv : {p['id']} compte_actif inconnu « {p['compte_actif']} »")
        for l in livre:
            if l["compte"] == compte and l["type"] == "calage":
                attendu = crd(p, dt.date.fromisoformat(l["date"]))
                if abs(attendu - float(l["montant"])) > 1.0:
                    erreurs.append(f"grand-livre.csv : calage du {l['date']} sur « {compte} » = {float(l['montant']):.2f} € ; "
                                   f"capital restant dû calculé ({p['id']}) = {attendu:.2f} €")
        if not lignes:
            aver.append(f"prets.csv : {p['id']} sans échéance")
    return erreurs, aver


def fmt(x):
    return f"{x:,.2f} €".replace(",", " ").replace(".", ",")


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("liste")
    p = sp.add_parser("tableau")
    p.add_argument("id")
    p.add_argument("--de", help="AAAA-MM")
    p.add_argument("--a", help="AAAA-MM")
    p = sp.add_parser("crd")
    p.add_argument("id")
    p.add_argument("--date")
    sp.add_parser("verifier")
    args = ap.parse_args()
    jour = aujourd_hui()
    if args.cmd == "liste":
        for p in lire():
            f = fin(p)
            print(f"{p['id']} [{p['statut']}] {p['libelle']} ({p['preteur']}) : {fmt(float(p['capital']))} à {p['taux']} % sur "
                  f"{p['duree_mois']} mois dès le {p['premiere_echeance']} ; mensualité actuelle {fmt(mensualite_courante(p, jour))} "
                  f"+ assurance {fmt(float(p['assurance_mensuelle'] or 0))} ; capital restant dû au {jour:%d/%m/%Y} : "
                  f"{fmt(crd(p, jour))} ; dernière échéance le {f['date']:%d/%m/%Y} (n° {f['n']})")
        return 0
    if args.cmd == "tableau":
        p = trouver(args.id)
        de = args.de or "0000-00"
        a = args.a or "9999-99"
        total_i = total_a = 0.0
        print(f"{'n°':>4} {'date':10} {'échéance':>11} {'intérêts':>10} {'capital':>10} {'assurance':>9} {'restant dû':>12}")
        for l in tableau(p):
            cle = f"{l['date']:%Y-%m}"
            if not de <= cle <= a:
                continue
            if l["type"] == "anticipation":
                print(f"{'':>4} {l['date']} remboursement anticipé {fmt(l['capital'])} (option {l['option']}, indemnité "
                      f"{fmt(l['ira'])}) ; restant dû {fmt(l['crd'])}")
                continue
            total_i += l["interet"]
            total_a += l["assurance"]
            print(f"{l['n']:>4} {l['date']} {l['echeance']:>11.2f} {l['interet']:>10.2f} {l['capital']:>10.2f} "
                  f"{l['assurance']:>9.2f} {l['crd']:>12.2f}")
        print(f"Intérêts sur la période affichée : {fmt(total_i)} ; assurance : {fmt(total_a)}")
        return 0
    if args.cmd == "crd":
        p = trouver(args.id)
        quand = dt.date.fromisoformat(args.date) if args.date else jour
        print(f"{p['id']} : capital restant dû au {quand:%d/%m/%Y} = {fmt(crd(p, quand))}")
        return 0
    erreurs, aver = verifier()
    for e in erreurs:
        print("ERREUR", e)
    for a in aver:
        print("RELIRE", a)
    print("prets.csv :", "des erreurs" if erreurs else "conforme", f"({len(lire())} prêt(s))")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
