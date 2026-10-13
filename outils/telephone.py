"""TÉLÉPHONE DE WILLIAM (créé le 11/10/2026 ; écran d'accueil et applications depuis le 12/10/2026) : une page HTML autonome qui
montre ce que l'écran du téléphone de William afficherait à l'heure de l'horloge. Pensée pour le joueur, qui joue parfois depuis son
propre téléphone : il « ouvre son téléphone » au lieu de relire le récit ou de demander une recherche au moteur.

    python outils/telephone.py                 # écrit sorties/telephone/index.html (+ telephone.json) et contrôle la page
    python outils/telephone.py --json          # affiche seulement les données

APPLICATIONS (demande de l'utilisateur, 12/10/2026 : « à chaque fois que j'ai un besoin […] crée l'application et rajoute-la dans
le téléphone ») : Messages, Courriels, Banque, Calendrier, Météo, Voyages. Une application = un fichier JS dans
`outils/telephone_web/` (qui appelle `appli({...})`), éventuellement un module Python qui fournit ses données
(`donnees_telephone(t)`), et une ligne dans APPLIS ci-dessous. La coque (`coque.html`) et le noyau (`noyau.js`) gèrent l'écran
d'accueil, l'ouverture des applications et les outils communs. Voir CLAUDE.md §14.
STRICTEMENT ce que William sait : jamais une ligne d'agenda « connu = non », jamais un tirage, une table, un modificateur, une
note du moteur, un fait caché ; seulement les mouvements d'argent déjà passés (et ceux qu'il a lui-même programmés) ; la météo
vue sous forme de PRÉVISION. Un contrôle automatique refuse d'écrire la page si un mot du moteur s'y glisse (tirage, jet,
T1…T14, M01…, « non connu »…).
Publication : Claude publie le fichier comme page privée (outil Artifact, toujours au même endroit : etat/relais-config.json) ;
tout autre agent peut ouvrir le fichier localement ou l'envoyer au joueur. Aucun nom de marque (banque, messagerie) n'apparaît.
"""
import argparse
import datetime as dt
import json
import re
import sys

from commun import ETAT, OUTILS, RACINE, SORTIES, JOURS, MOIS, ecrire_texte, lire_csv, lire_texte, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
INTERDITS = re.compile(r"\btirage|\bjet\b|\bjets\b|\bT\d{1,2}[a-d]?\b|\bM\d{2}\b|non connu|NON CONNU|moteur|dérogation|projection|"
                       r"modificateur|connu=non|\bE\d{3}-\d{8}\b|fait caché|secret_", re.I)
COMPTES_VISIBLES = {"courant": "Compte courant", "projet": "Compte épargne"}  # avant : « Épargne « Projet » » (renommé le 14/07/2040)
WEB = OUTILS / "telephone_web"
# Applications de l'écran d'accueil, dans l'ordre : (nom du fichier JS dans telephone_web/, module Python qui fournit
# D.applis[nom] par donnees_telephone(t), ou None si l'application se sert des données communes).
APPLIS = [("messages", None), ("courriels", None), ("banque", "banque"), ("calendrier", "appli_calendrier"), ("meteo", None),
          ("voyages", "voyages"), ("transports", "transports"), ("rencontres", "rencontres"), ("sante", "corps")]


def jour_court(d):
    return f"{JOURS[d.weekday()][:3]}. {d.day} {MOIS[d.month - 1][:4].rstrip('.')}{'.' if len(MOIS[d.month - 1]) > 4 else ''}"


def donnees():
    import agenda
    import base
    import calendrier_2040 as cal
    import grand_livre as gl
    import horloge
    import meteo
    h = horloge.lire()
    t = h["instant"]
    naif = t.replace(tzinfo=None)
    jour = t.date()
    reseau = ("PH · itinérance" if h["fuseau"] == "manille"
              else "LU" if re.search(r"luxembourg|esch|belval|findel|lux\b", h["lieu"], re.I) else "FR")
    # messages
    convs = {}
    for m in base.lire_messages():
        if f"{m['date']} {m['heure']}" > f"{naif:%Y-%m-%d %H:%M}":
            continue
        convs.setdefault(m["conversation"], []).append({"date": m["date"], "heure": m["heure"], "auteur": m["auteur"],
                                                        "texte": m["texte"], "moi": m["auteur"].split()[0] == "William"})
    conversations = sorted(({"nom": k.replace("_", " ").replace("-", " ").title(), "messages": v} for k, v in convs.items()),
                           key=lambda c: c["messages"][-1]["date"] + c["messages"][-1]["heure"], reverse=True)
    # courriels
    courriels = [{"date": d["date"], "objet": d["objet"][:1].upper() + d["objet"][1:], "fichier": d["fichier"]}
                 for d in base.lire_documents() if d["dossier"] == "courriels" and d["date"] <= jour.isoformat()]
    courriels.sort(key=lambda c: c["date"], reverse=True)
    # banque
    soldes = gl.soldes(naif)
    mouvements = [l for l in sorted(gl.lire(), key=gl.quand, reverse=True)
                  if l["type"] in ("mouvement", "prevu_realise") and gl.quand(l) <= naif and l["compte"] in COMPTES_VISIBLES]
    banque = {"comptes": [{"nom": n, "solde": round(soldes.get(c, 0.0), 2)} for c, n in COMPTES_VISIBLES.items()],
              "placements": round(soldes.get("etf", 0.0), 2),
              "operations": [{"date": l["date"], "libelle": re.sub(r"\s*\(.*?\)\s*$", "", l["libelle"]).strip(),
                              "montant": float(l["montant"]), "compte": COMPTES_VISIBLES[l["compte"]]} for l in mouvements[:40]]}
    # agenda (connu de William, hors fiction exclu) + fériés + événements publics
    evts = []
    for l in agenda.lire():
        if l["connu"] != "oui" or l["statut"] not in ("prevu", "latent") or "moteur" in l["qui"].lower():
            continue
        i = agenda.instant(l).astimezone(t.tzinfo)
        if i >= t:
            titre = re.sub(r"\s*\((?:projection|estimation)[^)]*\)", "", l["quoi"].split(" ; ")[0]).strip()
            evts.append({"date": i.date().isoformat(), "heure": f"{i:%H:%M}" if l["heure"] else "", "titre": titre, "type": "rdv"})
    fin = jour + dt.timedelta(days=75)
    for pays, nom_pays in (("fr", "France"), ("lu", "Luxembourg")):
        for annee in {jour.year, fin.year}:
            for d, nom, approx in cal.fetes(annee, pays):
                if jour <= d <= fin:
                    evts.append({"date": d.isoformat(), "heure": "", "titre": f"{nom.split(' (')[0]} (férié, {nom_pays})", "type": "ferie"})
    for e in cal.lire_donnees("evenements.csv"):
        if e["type"] in ("festival", "foire", "commerce") and jour.isoformat() <= e["debut"] <= fin.isoformat():
            evts.append({"date": e["debut"], "heure": "", "titre": e["evenement"].split(" : ")[0].split(",")[0], "type": "public"})
    evts.sort(key=lambda e: (e["date"], e["heure"]))
    # météo vue par William
    vraie = meteo.assurer(jour + dt.timedelta(days=4))[jour.isoformat()]
    maintenant_c = round(meteo.temperature_a(vraie, naif))
    previsions = []
    for i in range(0, 4):
        p = meteo.prevision(jour + dt.timedelta(days=i), jour)
        previsions.append({"jour": "Aujourd'hui" if i == 0 else "Demain" if i == 1 else JOURS[(jour + dt.timedelta(days=i)).weekday()].capitalize(),
                           "ciel": p["ciel"], "min": p["tmin"], "max": p["tmax"], "pluie": p["risque_pluie"]})
    lev, cou = cal.soleil(jour, meteo.lieu_affichage())
    return {
        "genere": dt.datetime.now().isoformat(timespec="minutes"),
        "heure": f"{t:%H:%M}", "date": jour_court(jour), "aujourdhui": jour.isoformat(), "date_longue": f"{JOURS[jour.weekday()]} {jour.day} {MOIS[jour.month - 1]} {jour.year}",
        "reseau": reseau, "lieu": h["lieu"].split(",")[0].split(" (")[0],
        "meteo": {"maintenant": maintenant_c, "previsions": previsions, "lever": f"{lev:%H:%M}", "coucher": f"{cou:%H:%M}"},
        "conversations": conversations, "courriels": courriels, "banque": banque, "agenda": evts[:40],
    }


# Le gabarit vit dans outils/telephone_web/ (coque.html, noyau.js et un fichier par application) depuis le 12/10/2026.


def construire():
    import importlib
    d = donnees()
    t = maintenant_simule()
    d["applis"] = {}
    for nom, module in APPLIS:
        if module:
            d["applis"][nom] = importlib.import_module(module).donnees_telephone(t)
    brut = json.dumps(d, ensure_ascii=False)
    fautes = sorted(set(m.group(0) for m in INTERDITS.finditer(brut)))
    if fautes:
        sys.exit("REFUSÉ : la page montrerait des éléments du moteur au joueur : " + ", ".join(fautes[:10]))
    scripts = "\n".join(lire_texte(WEB / f"{nom}.js") for nom in ["noyau"] + [n for n, _ in APPLIS])
    html = lire_texte(WEB / "coque.html").replace("__SCRIPTS__", scripts.replace("</script", "<\\/script"))
    html = html.replace("__DONNEES__", brut.replace("</", "<\\/"))
    dossier = SORTIES / "telephone"
    ecrire_texte(dossier / "index.html", html)
    ecrire_texte(dossier / "telephone.json", json.dumps(d, ensure_ascii=False, indent=1))
    return dossier / "index.html", d


def html_octets(chemin):
    return chemin.read_bytes()


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if args.json:
        print(json.dumps(donnees(), ensure_ascii=False, indent=1))
        return 0
    chemin, d = construire()
    print(f"Page écrite : {chemin.relative_to(RACINE).as_posix()} ({len(APPLIS)} applications ; {len(d['conversations'])} conversation(s), "
          f"{len(d['courriels'])} courriel(s), {len(d['banque']['operations'])} opération(s), "
          f"{len(d['applis'].get('calendrier', {}).get('evenements', []))} entrée(s) de calendrier ; {len(html_octets(chemin))} octets)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
