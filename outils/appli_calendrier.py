"""DONNÉES DE L'APPLICATION « CALENDRIER » du téléphone de William (créé le 12/10/2026, demande de l'utilisateur : « ajouter
également un calendrier sur le téléphone »). Affichage : `outils/telephone_web/calendrier.js`.

    python outils/appli_calendrier.py            # résumé des entrées produites (contrôle)

Ce que William sait, et seulement cela, de la date de l'horloge à dix-huit mois plus tard :
- jours fériés français (droit local d'Alsace-Moselle compris) et luxembourgeois (`calendrier_2040.fetes`) ;
- vacances scolaires et rentrées (`donnees/calendrier-scolaire.csv`) ;
- événements publics (`donnees/evenements.csv`, hors jours fériés déjà comptés) ;
- rendez-vous et échéances connus de William (`etat/agenda.csv` : « connu = oui », jamais les lignes du moteur) ;
- mouvements d'argent récurrents qu'il a lui-même mis en place ou qu'il paie (`etat/echeancier.csv`, lignes actives), avec le
  montant débité sur son compte courant (échéance exacte du prêt comprise).
"""
import datetime as dt
import re
import sys

from commun import OUTILS, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
MOIS_HORIZON = 18
NOMS_PERIODES = {"vacances_ete": "Vacances d'été", "vacances_toussaint": "Vacances de la Toussaint", "vacances_noel": "Vacances de Noël",
                 "vacances_carnaval": "Vacances de carnaval", "vacances_paques": "Vacances de Pâques",
                 "vacances_pentecote": "Vacances de Pentecôte", "vacances_hiver": "Vacances d'hiver", "vacances_printemps": "Vacances de printemps",
                 "conge_toussaint": "Congé de la Toussaint", "rentree": "Rentrée scolaire",
                 "session_automne_examen": "Session d'automne de l'examen de fin d'études"}
PAYS = {"lu": "Luxembourg", "fr": "France"}


def propre(texte):
    """Titre lisible : sans parenthèse finale, sans mention de projection ou d'estimation."""
    t = re.sub(r"\s*\((?:projection|estimation)[^)]*\)", "", texte)
    return t.split(" ; ")[0].strip()


def donnees_telephone(t=None):
    import agenda
    import calendrier_2040 as cal
    import echeancier
    t = t or maintenant_simule()
    jour = t.date()
    debut = jour.replace(day=1)
    m = debut.month - 1 + MOIS_HORIZON
    fin = dt.date(debut.year + m // 12, m % 12 + 1, 1) - dt.timedelta(days=1)
    ev = []
    for annee in range(debut.year, fin.year + 1):
        for pays in ("fr", "lu"):
            for d, nom, approx in cal.fetes(annee, pays):
                if debut <= d <= fin:
                    ev.append({"date": d.isoformat(), "type": "ferie", "titre": nom.split(" (")[0], "detail": PAYS[pays]})
    for l in cal.lire_donnees("calendrier-scolaire.csv"):
        if l["periode"] == "annee" or l["fin"] < debut.isoformat() or l["debut"] > fin.isoformat():
            continue
        nom = NOMS_PERIODES.get(l["periode"], l["periode"].replace("_", " ").capitalize())
        zone = "" if l["zone"] in ("", "national") else f", zone {l['zone']}"
        ev.append({"date": l["debut"], "fin": l["fin"], "type": "vacances" if l["periode"].startswith(("vacances", "conge")) else "ecole",
                   "titre": nom, "detail": f"{PAYS.get(l['pays'], l['pays'])}{zone}"})
    for e in cal.lire_donnees("evenements.csv"):
        if e["type"] == "ferie" or e["fin"] < debut.isoformat() or e["debut"] > fin.isoformat():
            continue
        ev.append({"date": e["debut"], "fin": e["fin"] if e["fin"] != e["debut"] else "", "type": "public",
                   "titre": e["evenement"].split(" : ")[0].split(" · ")[0], "detail": e["lieu"]})
    for l in agenda.lire():
        if l["connu"] != "oui" or l["statut"] not in ("prevu", "latent") or "moteur" in l["qui"].lower():
            continue
        if not debut.isoformat() <= l["date"] <= fin.isoformat():
            continue
        ev.append({"date": l["date"], "heure": l["heure"], "type": "rdv", "titre": propre(l["quoi"]), "detail": l["qui"]})
    for l in echeancier.lire():
        if l["statut"] != "actif":
            continue
        for d in echeancier.occurrences(l, max(jour, debut), fin):
            mv = [x for x in echeancier.mouvements(l, d) if x["compte"] == l["compte"]]
            if not mv:
                continue
            montant = float(mv[0]["montant"])
            titre = re.sub(r"\s*\((?:net|mensualisation)[^)]*\)", "", l["libelle"]).split(" (")[0].strip()
            ev.append({"date": d.isoformat(), "type": "argent", "titre": titre, "montant": montant,
                       "detail": "Compte courant"})
    import cartes  # relevés des cartes de crédit (débit en une fois au début du mois suivant : F063)
    for r in cartes.releves_a_venir(max(jour, debut), (fin - max(jour, debut)).days):
        ev.append({"date": r["date"], "type": "argent", "titre": r["titre"], "montant": r["montant"], "detail": "Compte courant"})
    ev.sort(key=lambda e: (e["date"], e.get("heure") or "", e["type"]))
    return {"aujourd_hui": jour.isoformat(), "debut": debut.isoformat(), "fin": fin.isoformat(), "evenements": ev}


def main():
    utf8()
    d = donnees_telephone()
    par_type = {}
    for e in d["evenements"]:
        par_type[e["type"]] = par_type.get(e["type"], 0) + 1
    print(f"Calendrier du {d['debut']} au {d['fin']} : " + ", ".join(f"{n} {t}" for t, n in sorted(par_type.items())))
    for e in d["evenements"][:12]:
        print(f"  {e['date']} [{e['type']}] {e['titre']}" + (f" : {e['montant']:+.2f} €" if "montant" in e else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
