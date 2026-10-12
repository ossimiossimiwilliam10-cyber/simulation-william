"""BANQUE DE WILLIAM (créé le 12/10/2026, demande de l'utilisateur : « la possibilité de moi-même configurer mes virements sur
l'application bancaire »). Le joueur prépare ses opérations dans l'application Banque du téléphone (`telephone_web/banque.js`),
les copie et les colle dans la simulation ; chaque ligne porte une étiquette [banque: …] que le moteur applique ici, en une commande,
au grand livre et à l'échéancier (prévus recalculés, rien n'est effacé : les prévus remplacés passent en « prevu_annule »).

    python outils/banque.py virement --de courant --vers projet --montant 500 --quand "2040-07-14 10:30" [--date 2040-07-20] [--libelle "…"]
    python outils/banque.py virement --de courant --vers externe --beneficiaire "Nom" --montant 200 --quand "…"
    python outils/banque.py ordre-modifier E012 [--montant 3000] [--jour 2] --quand "…"
    python outils/banque.py ordre-creer --de courant --vers etf --montant 500 --jour 5 --debut 2040-08-01 --quand "…" [--libelle "…"]
    python outils/banque.py ordre-suspendre E014 --quand "…"      |   ordre-reprendre E014 --quand "…"
    python outils/banque.py liste                                  # ordres permanents et prélèvements

Comptes de William utilisables : courant, projet (affiché « Compte épargne »), etf ; « externe » = un tiers (seul le débit est écrit).
Un virement entre ses comptes est immédiat (même banque ou plateforme reliée) ; vers un tiers, le débit est immédiat (virement
instantané) ; une date future crée un prévu. Le solde n'est pas vérifié à l'avance : un découvert se voit au grand livre.
"""
import argparse
import datetime as dt
import sys

from commun import OUTILS, ecrire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
COMPTES_WILLIAM = {"courant": "Compte courant", "projet": "Compte épargne", "etf": "Compte-titres ETF"}


def nom(c):
    return COMPTES_WILLIAM.get(c, c)


def annuler_prevus(ligne_id, apres, raison):
    """Les prévus futurs d'une ligne de l'échéancier passent en « prevu_annule » (référence suffixée : jamais de doublon)."""
    import grand_livre as gl
    livre = gl.lire()
    n = 0
    for l in livre:
        if l["type"] == "prevu" and l["reference"].startswith(ligne_id + "-") and gl.quand(l) > apres:
            l["type"] = "prevu_annule"
            l["reference"] += f"-x{apres:%Y%m%d%H%M}"
            l["libelle"] += f" [annulé : {raison}]"
            n += 1
    gl.ecrire(livre)
    return n


def virement(de, vers, montant, quand, date=None, libelle="", beneficiaire=""):
    import grand_livre as gl
    if de not in COMPTES_WILLIAM or (vers not in COMPTES_WILLIAM and vers != "externe"):
        sys.exit(f"Comptes : {', '.join(COMPTES_WILLIAM)} (ou « externe » pour un tiers)")
    if montant <= 0:
        sys.exit("Montant positif attendu")
    jour = date or quand.date()
    futur = jour > quand.date()
    livre = gl.lire()
    n = sum(1 for l in livre if l["reference"].startswith("B")) + 1
    ref = f"B{n:03d}"
    lib = libelle or (f"Virement vers {beneficiaire}" if vers == "externe" else f"Virement {nom(de)} → {nom(vers)}")
    heure = "08:00" if futur else f"{quand:%H:%M}"
    typ = "prevu" if futur else "mouvement"
    livre.append({"date": jour.isoformat(), "heure": heure, "compte": de, "montant": f"{-montant:.2f}", "type": typ, "libelle": lib,
                  "reference": ref})
    if vers != "externe":
        livre.append({"date": jour.isoformat(), "heure": heure, "compte": vers, "montant": f"{montant:.2f}", "type": typ,
                      "libelle": lib + " (compte crédité)", "reference": ref + "-C"})
    gl.ecrire(livre)
    return ref, futur


def ordre_modifier(ident, quand, montant=None, jour=None):
    import echeancier
    lignes = echeancier.lire()
    l = next((x for x in lignes if x["id"] == ident), None)
    if l is None:
        sys.exit(f"Ordre inconnu : {ident}")
    avant = f"{abs(float(l['montant'])):.2f} € le {l['jour']}"
    if montant is not None:
        l["montant"] = f"{-abs(montant):.2f}"
    if jour is not None:
        l["jour"] = str(jour)
    l["note"] = (l["note"] + " · " if l["note"] else "") + (f"avant : {avant} → maintenant : {abs(float(l['montant'])):.2f} € le "
                                                          f"{l['jour']} (modifié par William le {quand:%d/%m/%Y} à {quand:%H:%M})")
    ecrire_csv(echeancier.FICHIER, lignes, echeancier.COLONNES)
    n = annuler_prevus(ident, quand, f"ordre modifié le {quand:%d/%m/%Y}")
    echeancier.prevoir(quand.date() + dt.timedelta(days=60))
    return l, n


def ordre_creer(de, vers, montant, jour, debut, quand, libelle=""):
    import echeancier
    lignes = echeancier.lire()
    n = max(int(x["id"][1:]) for x in lignes) + 1
    l = {"id": f"E{n:03d}", "libelle": libelle or (f"Virement permanent vers {nom(vers)}" if vers != "externe" else "Virement permanent"),
         "compte": de, "montant": f"{-abs(montant):.2f}", "periodicite": "mensuel", "jour": str(jour), "mois": "", "heure": "08:00",
         "debut": debut.isoformat(), "fin": "", "statut": "actif", "source": f"ordre créé par William le {quand:%d/%m/%Y} à {quand:%H:%M}",
         "note": "", "contrepartie": vers if vers in COMPTES_WILLIAM else "", "pret": ""}
    lignes.append(l)
    ecrire_csv(echeancier.FICHIER, lignes, echeancier.COLONNES)
    echeancier.prevoir(quand.date() + dt.timedelta(days=60))
    return l


def ordre_statut(ident, statut, quand):
    import echeancier
    lignes = echeancier.lire()
    l = next((x for x in lignes if x["id"] == ident), None)
    if l is None:
        sys.exit(f"Ordre inconnu : {ident}")
    avant = l["statut"]
    l["statut"] = statut
    l["note"] = (l["note"] + " · " if l["note"] else "") + f"avant : {avant} → maintenant : {statut} (William, {quand:%d/%m/%Y} {quand:%H:%M})"
    ecrire_csv(echeancier.FICHIER, lignes, echeancier.COLONNES)
    n = 0
    if statut == "suspendu":
        n = annuler_prevus(ident, quand, f"ordre suspendu le {quand:%d/%m/%Y}")
    else:
        echeancier.prevoir(quand.date() + dt.timedelta(days=60))
    return l, n


def donnees_telephone(t=None):
    """Ordres permanents (virements de William) et prélèvements connus, pour l'application Banque."""
    import echeancier
    t = t or maintenant_simule()
    jour = t.date()
    ordres, prelevements = [], []
    for l in echeancier.lire():
        if l["statut"] not in ("actif", "suspendu"):
            continue
        prochaine = echeancier.occurrences(l, jour, jour + dt.timedelta(days=400)) if l["statut"] == "actif" else []
        x = {"id": l["id"], "libelle": l["libelle"].split(" (")[0], "montant": float(l["montant"]), "jour": l["jour"],
             "statut": l["statut"], "prochaine": prochaine[0].isoformat() if prochaine else "", "vers": nom(l.get("contrepartie") or ""),
             "periodicite": l["periodicite"]}
        if l.get("contrepartie") or "virement" in l["libelle"].lower():
            ordres.append(x)
        elif float(l["montant"]) < 0:
            prelevements.append(x)
    return {"ordres": ordres, "prelevements": prelevements, "comptes": COMPTES_WILLIAM}


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("virement")
    p.add_argument("--de", required=True)
    p.add_argument("--vers", required=True)
    p.add_argument("--montant", type=float, required=True)
    p.add_argument("--quand", required=True)
    p.add_argument("--date")
    p.add_argument("--libelle", default="")
    p.add_argument("--beneficiaire", default="")
    p = sp.add_parser("ordre-modifier")
    p.add_argument("id")
    p.add_argument("--montant", type=float)
    p.add_argument("--jour", type=int)
    p.add_argument("--quand", required=True)
    p = sp.add_parser("ordre-creer")
    p.add_argument("--de", default="courant")
    p.add_argument("--vers", required=True)
    p.add_argument("--montant", type=float, required=True)
    p.add_argument("--jour", type=int, required=True)
    p.add_argument("--debut", required=True)
    p.add_argument("--quand", required=True)
    p.add_argument("--libelle", default="")
    for c in ("ordre-suspendre", "ordre-reprendre"):
        p = sp.add_parser(c)
        p.add_argument("id")
        p.add_argument("--quand", required=True)
    sp.add_parser("liste")
    args = ap.parse_args()
    if args.cmd == "liste":
        d = donnees_telephone()
        for o in d["ordres"]:
            print(f"ordre {o['id']} [{o['statut']}] {o['libelle']} : {o['montant']:+.2f} € le {o['jour']} → {o['vers']} (prochaine : {o['prochaine'] or '—'})")
        for o in d["prelevements"]:
            print(f"prélèvement {o['id']} {o['libelle']} : {o['montant']:+.2f} € ({o['periodicite']}, jour {o['jour']}) ; prochaine : {o['prochaine'] or '—'}")
        return 0
    quand = dt.datetime.fromisoformat(args.quand)
    if args.cmd == "virement":
        ref, futur = virement(args.de, args.vers, args.montant, quand, dt.date.fromisoformat(args.date) if args.date else None,
                              args.libelle, args.beneficiaire)
        print(f"Virement {ref} : {args.montant:.2f} € {nom(args.de)} → {args.beneficiaire or nom(args.vers)} ({'prévu' if futur else 'exécuté'})")
    elif args.cmd == "ordre-modifier":
        l, n = ordre_modifier(args.id, quand, args.montant, args.jour)
        print(f"Ordre {l['id']} modifié : {abs(float(l['montant'])):.2f} € le {l['jour']} ; {n} prévu(s) remplacé(s)")
    elif args.cmd == "ordre-creer":
        l = ordre_creer(args.de, args.vers, args.montant, args.jour, dt.date.fromisoformat(args.debut), quand, args.libelle)
        print(f"Ordre {l['id']} créé : {args.montant:.2f} € le {args.jour} → {nom(args.vers)}, dès le {args.debut}")
    else:
        statut = "suspendu" if args.cmd == "ordre-suspendre" else "actif"
        l, n = ordre_statut(args.id, statut, quand)
        print(f"Ordre {l['id']} : {statut}" + (f" ; {n} prévu(s) annulé(s)" if n else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
