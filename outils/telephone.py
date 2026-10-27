"""TÉLÉPHONE DE WILLIAM (créé le 11/10/2026 ; écran d'accueil et applications depuis le 12/10/2026) : une page HTML autonome qui
montre ce que l'écran du téléphone de William afficherait à l'heure de l'horloge. Pensée pour le joueur, qui joue parfois depuis son
propre téléphone : il « ouvre son téléphone » au lieu de relire le récit ou de demander une recherche au moteur.

    python outils/telephone.py                 # écrit sorties/telephone/index.html (+ telephone.json) et contrôle la page
    python outils/telephone.py --json          # affiche seulement les données
    python outils/telephone.py --fichiers      # liste JSON des PDF à publier avec la page (application Fichiers)

APPLICATIONS (demande de l'utilisateur, 12/10/2026 : « à chaque fois que j'ai un besoin […] crée l'application et rajoute-la dans
le téléphone ») : Messages, Courriels, Fichiers, Banque, Calendrier, Météo, Voyages. Une application = un fichier JS dans
`outils/telephone_web/` (qui appelle `appli({...})`), éventuellement un module Python qui fournit ses données
(`donnees_telephone(t)`), et une ligne dans APPLIS ci-dessous. La coque (`coque.html`) et le noyau (`noyau.js`) gèrent l'écran
d'accueil, l'ouverture des applications et les outils communs. Voir CLAUDE.md §14.
STRICTEMENT ce que William sait : jamais une ligne d'agenda « connu = non », jamais un tirage, une table, un modificateur, une
note du moteur, un fait caché ; seulement les mouvements d'argent déjà passés (et ceux qu'il a lui-même programmés) ; la météo
vue sous forme de PRÉVISION. Un contrôle automatique refuse d'écrire la page si un mot du moteur s'y glisse (tirage, jet,
T1…T14, M01…, « non connu »…).
Publication : Claude publie le fichier comme page privée (outil Artifact, toujours au même endroit : etat/relais-config.json) ;
tout autre agent peut ouvrir le fichier localement ou l'envoyer au joueur. Les PDF de l'application Fichiers se publient avec la page : outil
Artifact, `file_path` sorties/telephone/index.html, `root` sorties/telephone et `files` = la sortie de `--fichiers`. Aucun nom de marque (banque, messagerie) n'apparaît.
"""
import argparse
import datetime as dt
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

from commun import ETAT, OUTILS, RACINE, SORTIES, JOURS, MOIS, ecrire_texte, lire_csv, lire_texte, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
INTERDITS = re.compile(r"\btirage|\bjet\b|\bjets\b|\bT\d{1,2}[a-d]?\b|\bM\d{2,3}\b|non connu|NON CONNU|moteur|dérogation|projection|"
                       r"modificateur|connu=non|\bE\d{3}-\d{8}\b|fait caché|secret_", re.I)
COMPTES_VISIBLES = {"courant": "Compte courant", "projet": "Compte épargne"}  # avant : « Épargne « Projet » » (renommé le 14/07/2040)
WEB = OUTILS / "telephone_web"
# Applications de l'écran d'accueil, dans l'ordre : (nom du fichier JS dans telephone_web/, module Python qui fournit
# D.applis[nom] par donnees_telephone(t), ou None si l'application se sert des données communes).
APPLIS = [("messages", None), ("courriels", None), ("fichiers", None), ("banque", "banque"), ("portefeuille", "devises"), ("calendrier", "appli_calendrier"),
          ("meteo", None), ("voyages", "voyages"), ("transports", "transports"), ("courses", "courses"), ("rencontres", "rencontres"),
          ("sante", "corps")]  # 14/10/2026 : Portefeuille (devises.py) et Courses (courses.py) ; 27/10/2026 : Fichiers
# Fichiers (27/10/2026, demande de l'utilisateur : « les fichiers directement accessibles depuis mon téléphone ») : les PDF de documents_william/ et de
# courriels/ DATÉS d'un jour passé ou du jour même sont copiés dans sorties/telephone/fichiers/ et publiés avec la page (`--fichiers`).
DOSSIERS_FICHIERS = ("documents_william", "Documents"), ("courriels", "Reçus")
FICHIERS = SORTIES / "telephone" / "fichiers"
# Mode de l'application Fichiers (demande de l'utilisateur, 27/10/2026, « pour l'instant, le lien direct ») :
#   "direct"  : un appui ouvre le fichier du PC par son adresse file:/// (dossier principal du dépôt) ; rien n'est publié avec la page ;
#   "lecteur" : le PDF est publié avec la page et lu dans la page (pdf.js) ; un lien vers le fichier publié est refusé par le viewer (constaté).
MODE_FICHIERS = "direct"


def racine_principale():
    """Dossier principal du dépôt (celui qui porte `master`) : le dossier de travail d'un worktree peut disparaître, pas celui-ci."""
    parties = RACINE.parts
    return Path(*parties[:parties.index(".claude")]) if ".claude" in parties else RACINE


def _nom_publie(nom):
    """Nom du fichier publié : sans accents ni espaces (les adresses de la page restent sûres)."""
    s = unicodedata.normalize("NFKD", nom).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s)


def fichiers_visibles(jour):
    """PDF que William a en main à `jour` : date du nom (AAAA-MM-JJ_…) au plus égale au jour courant ; un fichier sans date n'est pas listé."""
    res = []
    for dossier, libelle in DOSSIERS_FICHIERS:
        for p in sorted((RACINE / dossier).glob("*.pdf")):
            m = re.match(r"(\d{4}-\d{2}-\d{2})_(.*)", p.stem)
            if not m or m.group(1) > jour.isoformat():
                continue
            objet = re.sub(r"\b([dl]) (?=[AEIOUÉÈÊÎÔÂaeiouéèêîôâh])", r"\1'", m.group(2).replace("_", " "))  # « d Ivoire » -> « d'Ivoire »
            res.append({"nom": objet[:1].upper() + objet[1:], "fichier": p.name, "dossier": libelle, "date": m.group(1),
                        "ko": max(1, round(p.stat().st_size / 1024)), "url": f"fichiers/{dossier}/{_nom_publie(p.name)}",
                        "lien": (racine_principale() / dossier / p.name).as_uri(),
                        "source": f"{dossier}/{p.name}"})
    res.sort(key=lambda f: (f["date"], f["nom"]), reverse=True)
    return res


def copier_fichiers(fichiers):
    """Recopie les fichiers visibles dans sorties/telephone/fichiers/ (le dossier est refait : un fichier pas encore reçu n'y reste jamais)."""
    shutil.rmtree(FICHIERS, ignore_errors=True)
    for f in fichiers:
        cible = SORTIES / "telephone" / f["url"]
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(RACINE / f["source"], cible)


def jour_court(d):
    return f"{JOURS[d.weekday()][:3]}. {d.day} {MOIS[d.month - 1][:4].rstrip('.')}{'.' if len(MOIS[d.month - 1]) > 4 else ''}"


def donnees():
    import agenda
    import base
    import calendrier_2040 as cal
    import grand_livre as gl
    import horloge
    import meteo
    import mobile
    h = horloge.lire()
    t = h["instant"]
    naif = t.replace(tzinfo=None)
    jour = t.date()
    reseau = ("PH · itinérance" if h["fuseau"] == "manille"
              else "KR · " + mobile.reseau_court(naif) if h["fuseau"] == "seoul"
              else "LU" if re.search(r"luxembourg|esch|belval|findel|lux\b", h["lieu"], re.I) else "FR")
    # messages
    convs = {}
    for m in base.lire_messages():
        if f"{m['date']} {m['heure']}" > f"{naif:%Y-%m-%d %H:%M}":
            continue
        convs.setdefault(m["conversation"], []).append({"date": m["date"], "heure": m["heure"], "auteur": m["auteur"],
                                                        "texte": m["texte"], "moi": m["auteur"].split()[0] == "William"})
    def nom_conversation(cle, messages):
        """Nom affiché : l'interlocuteur, accents compris, s'il est seul ; sinon le nom du fichier (13/10/2026)."""
        autres = {m["auteur"] for m in messages if not m["moi"]}
        return autres.pop() if len(autres) == 1 else cle.replace("_", " ").replace("-", " ").title()

    conversations = sorted(({"nom": nom_conversation(k, v), "messages": v} for k, v in convs.items()),
                           key=lambda c: c["messages"][-1]["date"] + c["messages"][-1]["heure"], reverse=True)
    # courriels
    fichiers = fichiers_visibles(jour)
    liens = {f["source"]: f for f in fichiers}
    courriels = [{"date": d["date"], "objet": d["objet"][:1].upper() + d["objet"][1:], "fichier": d["fichier"],
                  "url": liens.get(f"courriels/{d['fichier']}", {}).get("url", ""), "lien": liens.get(f"courriels/{d['fichier']}", {}).get("lien", "")}
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
        "meteo": {"maintenant": maintenant_c, "previsions": previsions, "lever": f"{lev:%H:%M}", "coucher": f"{cou:%H:%M}",
                  "alertes": alertes_meteo(jour)},
        "conversations": conversations, "courriels": courriels, "fichiers": [{k: v for k, v in f.items() if k != "source"} for f in fichiers], "fichiers_mode": MODE_FICHIERS,
        "banque": banque, "agenda": evts[:40],
    }


# Le gabarit vit dans outils/telephone_web/ (coque.html, noyau.js et un fichier par application) depuis le 12/10/2026.


def alertes_meteo(jour):
    """Alertes publiques du lieu où se trouve William (tempêtes et mousson renforcée à Manille : outils/tropiques.py)."""
    import meteo
    if meteo.station_courante() != "manille":
        return []
    import tropiques
    return tropiques.alertes(jour)


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
    copier_fichiers(fichiers_visibles(t.date()) if MODE_FICHIERS == "lecteur" else [])
    return dossier / "index.html", d


# ---------------------------------------------------------------- page publiée (14/10/2026) : relire seulement ce qui change
PUBLIE = SORTIES / "telephone" / "publie.html"


def _separer(html):
    """(code sans les données, données D) d'une page générée."""
    import re
    m = re.search(r"^\s*const D = (\{.*\});?\s*$", html, re.M)
    if not m:
        return html, {}
    return html.replace(m.group(0), ""), json.loads(m.group(1))


def _comparer(a, b, chemin, sortie, compteur):
    if chemin.startswith("D.applis.voyages.destinations") or chemin in ("D.genere",):
        if a != b:
            compteur[chemin.split("[")[0] if "[" in chemin else chemin] = compteur.get(chemin.split("[")[0], 0) + 1
        return
    if type(a) != type(b):
        sortie.append(f"~ {chemin} : {json.dumps(a, ensure_ascii=False)[:120]} -> {json.dumps(b, ensure_ascii=False)[:120]}")
    elif isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a:
                sortie.append(f"+ {chemin}.{k} = {json.dumps(b[k], ensure_ascii=False)[:200]}")
            elif k not in b:
                sortie.append(f"- {chemin}.{k}")
            else:
                _comparer(a[k], b[k], f"{chemin}.{k}", sortie, compteur)
    elif isinstance(a, list):
        if len(a) != len(b):
            sa = {json.dumps(x, ensure_ascii=False, sort_keys=True) for x in a}
            sb = [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in b]
            nouveaux = [x for x in sb if x not in sa]
            sortie.append(f"~ {chemin} : {len(a)} -> {len(b)} élément(s)" + (f" ; + {nouveaux[0][:200]}" if nouveaux else ""))
            for x in nouveaux[1:4]:
                sortie.append(f"    + {x[:200]}")
        else:
            for n, (x, y) in enumerate(zip(a, b)):
                _comparer(x, y, f"{chemin}[{n}]", sortie, compteur)
    elif a != b:
        sortie.append(f"~ {chemin} : {json.dumps(a, ensure_ascii=False)[:120]} -> {json.dumps(b, ensure_ascii=False)[:120]}")


def diff_publie():
    """Ce qui a changé depuis la dernière page publiée : le code (lignes) et les données (clé par clé), en bref."""
    courant = SORTIES / "telephone" / "index.html"
    if not PUBLIE.exists():
        return ["(aucune copie publiée enregistrée : relire la page entière avant de publier, puis telephone.py --marquer-publie)"]
    code_a, d_a = _separer(lire_texte(PUBLIE))
    code_b, d_b = _separer(lire_texte(courant))
    sortie, compteur = [], {}
    if code_a != code_b:
        import difflib
        diff = [l for l in difflib.unified_diff(code_a.splitlines(), code_b.splitlines(), lineterm="", n=0) if l[:1] in "+-" and not l.startswith(("+++", "---"))]
        sortie.append(f"CODE MODIFIÉ : {len(diff)} ligne(s) à relire (telephone.py --diff --code)")
    _comparer(d_a, d_b, "D", sortie, compteur)
    for k, n in compteur.items():
        if k != "D.genere":
            sortie.append(f"(prix des voyages recalculés : {n} valeur(s))")
    return sortie or ["aucun changement depuis la page publiée"]


def diff_code():
    import difflib
    code_a, _ = _separer(lire_texte(PUBLIE))
    code_b, _ = _separer(lire_texte(SORTIES / "telephone" / "index.html"))
    return [l for l in difflib.unified_diff(code_a.splitlines(), code_b.splitlines(), lineterm="", n=1)]


def marquer_publie():
    ecrire_texte(PUBLIE, lire_texte(SORTIES / "telephone" / "index.html"))


def html_octets(chemin):
    return chemin.read_bytes()


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--diff", action="store_true", help="changements depuis la dernière page publiée (code et données)")
    ap.add_argument("--code", action="store_true", help="avec --diff : les lignes de code modifiées")
    ap.add_argument("--fichiers", action="store_true", help="liste JSON des fichiers à publier avec la page (paramètre `files` de l'outil Artifact, racine sorties/telephone)")
    ap.add_argument("--marquer-publie", action="store_true", help="la page courante vient d'être publiée : elle devient la référence")
    args = ap.parse_args()
    if args.diff:
        for l in (diff_code() if args.code else diff_publie()):
            print(l)
        return 0
    if args.fichiers:
        print(json.dumps([{"path": f["url"]} for f in fichiers_visibles(maintenant_simule().date())] if MODE_FICHIERS == "lecteur" else [], ensure_ascii=False))
        return 0
    if args.marquer_publie:
        marquer_publie()
        print("Page courante enregistrée comme publiée (sorties/telephone/publie.html)")
        return 0
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
