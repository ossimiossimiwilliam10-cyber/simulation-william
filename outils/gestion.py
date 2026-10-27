"""APPLICATION « GESTION » DU TÉLÉPHONE DE WILLIAM (créée le 27/10/2026 ; installée dans le jeu le 19/07/2041 à 03h12, version 0.1).

William l'a imaginée et « codée » (tour n° 16) : une application de gestion pilotée par l'IA, sur son téléphone, avec la transparence totale sur l'entreprise. Un document
envoyé par un collaborateur (avocat, comptable, ingénieur…) passe par la messagerie de l'application, est routé vers le bon PÔLE (RH, juridique, finance, technique,
commercial), comparé aux sources officielles du pôle, puis résumé pour William : est-ce clair, peut-on faire mieux, que répondre. Elle fonctionne avec la clé d'API du
modèle d'IA le plus puissant du marché ; budget mensuel plafonné à 1 000 € (la consommation réelle est le plus souvent bien plus basse).

Version 0.1 : tableau de bord (budget d'API, pôles, sources), pôle RH actif (poste ouvert, annonces, candidats : ce que l'agent IA a rapporté à William), boîte de documents.
Les autres pôles et la messagerie de dépôt sont annoncés « à venir ».

    python outils/gestion.py etat                                  # budget du mois, pôles, documents, candidats
    python outils/gestion.py recevoir --expediteur "Me Untel" --objet "Rapport sur les statuts" --pole juridique [--quand "2041-07-20 10:00"]
    python outils/gestion.py analyser D001 --retour "texte du retour du pôle" --cout 2.4 [--quand "…"]   # l'analyse du pôle : écrite par le moteur, coût au budget
    python outils/gestion.py candidat --nom "Hervé Touré" --niveau B --etat "entretien en cours" --resume "…" --plateforme NovoJob [--note 62] [--quand "…"]
    python outils/gestion.py verifier

Fichiers : `donnees/gestion-poles.csv`, `donnees/gestion-sources.csv` (référence) ; `etat/gestion-config.csv`, `etat/gestion-budget.csv`, `etat/gestion-documents.csv`,
`etat/gestion-candidats.csv` (état). La page du téléphone ne montre que ce que William sait : un candidat n'y figure qu'après le rapport de l'agent, un document qu'après sa
réception, un retour qu'après son analyse. Règles des applications : CLAUDE.md §14 (elle ne décide ni ne paie à la place de William).
"""
import argparse
import datetime as dt
import sys

from commun import DONNEES, ETAT, ecrire_csv, lire_csv, utf8

POLES = DONNEES / "gestion-poles.csv"
SOURCES = DONNEES / "gestion-sources.csv"
CONFIG = ETAT / "gestion-config.csv"
BUDGET = ETAT / "gestion-budget.csv"
DOCUMENTS = ETAT / "gestion-documents.csv"
CANDIDATS = ETAT / "gestion-candidats.csv"
COL_B = ["date", "pole", "objet", "cout_eur"]
COL_D = ["id", "date", "expediteur", "objet", "pole", "statut", "retour", "cout_eur"]
COL_C = ["id", "nom", "niveau", "note", "etat", "resume", "plateforme", "date"]
ETATS_ANNONCES = {"en_ligne": "En ligne", "moderation": "En attente", "en_attente": "En attente", "refusee": "Refusée", "bloque": "Bloquée"}


def config():
    return {l["cle"]: l["valeur"] for l in lire_csv(CONFIG)}


def installee(t):
    c = config()
    return bool(c.get("installee_le")) and f"{t:%Y-%m-%d %H:%M}" >= c["installee_le"]


def _avant(date, t):
    return (date or "") <= f"{t:%Y-%m-%d %H:%M}"


def depense_mois(t):
    mois = f"{t:%Y-%m}"
    return round(sum(float(l["cout_eur"] or 0) for l in lire_csv(BUDGET) if l["date"].startswith(mois) and _avant(l["date"], t)), 2)


def donnees_telephone(t):
    """Ce que montre l'application Gestion à l'heure `t` (rien d'autre que ce que William sait)."""
    t = t.replace(tzinfo=None) if getattr(t, "tzinfo", None) else t
    if not installee(t):
        return {"installee": False}
    c = config()
    plafond = float(c.get("plafond_api_eur", "1000"))
    dep = depense_mois(t)
    poles = [{"id": p["id"], "nom": p["nom"], "description": p["description"], "statut": p["statut"]} for p in lire_csv(POLES)]
    sources = [{"pole": s["pole"], "titre": s["titre"], "reference": s["reference"]} for s in lire_csv(SOURCES)]
    docs = [{"id": d["id"], "date": d["date"][:10], "expediteur": d["expediteur"], "objet": d["objet"], "pole": d["pole"], "statut": d["statut"],
             "retour": d["retour"] if d["statut"] == "analysé" else "", "cout": float(d["cout_eur"] or 0)}
            for d in lire_csv(DOCUMENTS) if _avant(d["date"], t)]
    docs.sort(key=lambda d: d["date"], reverse=True)
    candidats = [{"nom": x["nom"], "niveau": x["niveau"], "note": x["note"], "etat": x["etat"], "resume": x["resume"], "plateforme": x["plateforme"], "date": x["date"][:10]}
                 for x in lire_csv(CANDIDATS) if _avant(x["date"], t)]
    import annonces
    plateformes = [{"nom": a["plateforme"], "etat": ETATS_ANNONCES.get(a["etat"], a["etat"])} for a in annonces.annonces()]
    return {"installee": True, "version": c.get("version", "0.1"), "plafond": plafond, "depense": dep, "restant": round(plafond - dep, 2),
            "modele": c.get("modele", ""), "poles": poles, "sources": sources, "documents": docs, "candidats": candidats, "annonces": plateformes,
            "poste": {"intitule": c.get("poste", ""), "forme": c.get("forme_sociale", "")}}


def _quand(texte):
    import horloge
    if texte:
        return dt.datetime.strptime(texte, "%Y-%m-%d %H:%M")
    return horloge.lire()["instant"].replace(tzinfo=None)


def recevoir(expediteur, objet, pole, quand):
    if pole not in {p["id"] for p in lire_csv(POLES)}:
        sys.exit("Pôle inconnu : " + pole)
    docs = lire_csv(DOCUMENTS)
    ident = f"D{len(docs) + 1:03d}"
    docs.append({"id": ident, "date": f"{quand:%Y-%m-%d %H:%M}", "expediteur": expediteur, "objet": objet, "pole": pole, "statut": "reçu", "retour": "", "cout_eur": "0"})
    ecrire_csv(DOCUMENTS, docs, COL_D)
    return ident


def analyser(ident, retour, cout, quand):
    docs = lire_csv(DOCUMENTS)
    d = next((x for x in docs if x["id"] == ident), None)
    if d is None:
        sys.exit("Document inconnu : " + ident)
    d.update({"statut": "analysé", "retour": retour.replace(";", ","), "cout_eur": f"{float(cout):.2f}"})
    ecrire_csv(DOCUMENTS, docs, COL_D)
    ecrire_csv(BUDGET, lire_csv(BUDGET) + [{"date": f"{quand:%Y-%m-%d %H:%M}", "pole": d["pole"], "objet": f"{ident} : {d['objet']}", "cout_eur": f"{float(cout):.2f}"}], COL_B)
    return d


def candidat(nom, niveau, etat, resume, plateforme, note, quand):
    lignes = lire_csv(CANDIDATS)
    x = next((l for l in lignes if l["nom"] == nom), None)
    if x is None:
        x = {"id": f"C{len(lignes) + 1:03d}", "nom": nom, "niveau": niveau, "note": note or "", "etat": etat, "resume": resume, "plateforme": plateforme, "date": f"{quand:%Y-%m-%d %H:%M}"}
        lignes.append(x)
    else:
        x.update({"niveau": niveau or x["niveau"], "etat": etat or x["etat"], "resume": resume or x["resume"], "note": note or x["note"]})
    ecrire_csv(CANDIDATS, lignes, COL_C)
    return x


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("etat")
    sp.add_parser("verifier")
    p = sp.add_parser("recevoir")
    p.add_argument("--expediteur", required=True)
    p.add_argument("--objet", required=True)
    p.add_argument("--pole", required=True)
    p.add_argument("--quand")
    p = sp.add_parser("analyser")
    p.add_argument("id")
    p.add_argument("--retour", required=True)
    p.add_argument("--cout", required=True)
    p.add_argument("--quand")
    p = sp.add_parser("candidat")
    p.add_argument("--nom", required=True)
    p.add_argument("--niveau", default="")
    p.add_argument("--etat", default="")
    p.add_argument("--resume", default="")
    p.add_argument("--plateforme", default="")
    p.add_argument("--note", default="")
    p.add_argument("--quand")
    args = ap.parse_args()
    if args.cmd == "etat":
        d = donnees_telephone(_quand(None))
        if not d["installee"]:
            print("Application Gestion : pas encore installée.")
            return 0
        print(f"Gestion v{d['version']} : budget d'API {d['depense']:.2f} € sur {d['plafond']:.0f} € ce mois-ci (reste {d['restant']:.2f} €)")
        print("Pôles : " + " ; ".join(f"{p['nom']} ({p['statut']})" for p in d["poles"]))
        print(f"Poste : {d['poste']['intitule']} · forme sociale : {d['poste']['forme']}")
        print(f"{len(d['candidats'])} candidat(s) · {len(d['documents'])} document(s)")
    elif args.cmd == "recevoir":
        print("Document reçu :", recevoir(args.expediteur, args.objet, args.pole, _quand(args.quand)))
    elif args.cmd == "analyser":
        d = analyser(args.id, args.retour, args.cout, _quand(args.quand))
        print(f"{d['id']} analysé par le pôle {d['pole']} : coût {float(args.cout):.2f} €")
    elif args.cmd == "candidat":
        print("Candidat :", candidat(args.nom, args.niveau, args.etat, args.resume, args.plateforme, args.note, _quand(args.quand))["id"])
    else:
        ok = True
        poles = {p["id"] for p in lire_csv(POLES)}
        for s in lire_csv(SOURCES):
            if s["pole"] not in poles:
                ok = False
                print("source d'un pôle inconnu :", s)
        for d in lire_csv(DOCUMENTS):
            if d["pole"] not in poles:
                ok = False
                print("document d'un pôle inconnu :", d)
        c = config()
        if float(c.get("plafond_api_eur", "0")) <= 0:
            ok = False
            print("plafond d'API absent ou nul")
        print("gestion : conforme" if ok else "gestion : à corriger")
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
