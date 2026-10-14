"""MONDE VIVANT (créé le 14/10/2026, demande de l'utilisateur : « que l'univers soit indépendant, soit vivant… réaliste, pas moral »).
Chaque personnage inscrit (`etat/personnages.csv`, adulte) vit sa vie, que William le voie ou non : sa semaine ou sa journée se tire
dans T11, la catégorie de ce qui lui arrive dans T13a-d, et, s'il est en lien actif avec William, son initiative envers lui dans T14
(l'heure en T10, calée sur ses horaires de vie). Tout est calculé par le programme ; le moteur n'écrit que le texte des messages,
au moment où ils arrivent (`reactions.py jouer`), et se sert des événements de vie pour colorer les scènes.

    python outils/monde_vivant.py jour 2040-07-20 [--simule]      # liens actifs : journée (T11, T13) et initiative (T14, T10)
    python outils/monde_vivant.py semaine 2040-07-16 [--simule]   # tous les autres : une semaine (T11, jour tiré, T13)
    python outils/monde_vivant.py avancer --jusqua 2040-07-21     # tout ce qui manque jusqu'à ce jour (appelé par tour.py fin)
    python outils/monde_vivant.py liens                           # liens de William (actifs, en pause, rejetés, bloqués…)
    python outils/monde_vivant.py lien "Julia Dimaculangan" rejete_par_william --note "« not interested anymore », 19/07"
    python outils/monde_vivant.py vies "Kiara Reyes"               # ce qui lui est arrivé (moteur seulement)
    python outils/monde_vivant.py fiches                          # régénère la section « Fiches » de etat/vies-propres.md

CADENCE (réalisme, 14/10/2026) : T11 décrit une journée ; tirée chaque jour pour tout le monde, elle donnerait à chacun un tournant
par mois et un coup dur toutes les deux semaines. Elle est donc tirée chaque jour pour les personnages EN SCÈNE (liens actifs avec
William), et une fois par semaine (jour tiré) pour tous les autres : environ deux tournants et trois ou quatre coups durs par an
et par personne. Proposition à valider par l'utilisateur (memoire/propositions-2026-10-14.md).
MODIFICATEURS appliqués d'après les faits (jamais au jugé) : M80 souci fragile (dette, santé, crise, contrat qui finit) ; M82 jour
férié ou veille de fête dans son pays ; M83 vacances scolaires d'un élève, d'un étudiant ou d'un enseignant ; M95 dette (coup dur) ;
M96 proche malade (coup dur) ; M99 saison des pluies à Manille (petit événement) ; T14 : M84 enjeu actif (rendez-vous, argent,
promesse), M85 rejet ou froid de William, M86 lien proche, M87 coup dur du jour. Pas de T14 si une réponse du personnage est déjà
programmée dans les 48 h (il ne double pas un message en attente).
Fichiers : `etat/vies.csv` (événements, moteur seulement), `etat/liens.csv` (états des liens fixés par le moteur),
`etat/monde-vivant.json` (jours et semaines déjà tirés).
"""
import argparse
import datetime as dt
import hashlib
import json
import random
import re
import sys

from commun import ETAT, OUTILS, RACINE, age, ecrire_csv, ecrire_texte, lire_csv, lire_texte, utf8

sys.path.insert(0, str(OUTILS))
import fuseaux  # noqa: E402
import jet  # noqa: E402
import routines  # noqa: E402

VIES = ETAT / "vies.csv"
COL_VIES = ["date", "personnage", "cadence", "t11", "categorie", "detail", "initiative", "agenda", "note"]
LIENS = ETAT / "liens.csv"
COL_LIENS = ["personnage", "etat", "depuis", "note"]
ETAT_JSON = ETAT / "monde-vivant.json"
CONTENU = {"coup_dur": "T13a", "tournant": "T13b", "petit_evenement": "T13c", "avancee_objectif": "T13d"}
FRAGILE = re.compile(r"dette|prêteur|5-6|malad|santé|hôpital|crise|chômage|non renouvelé|endo|licenci|impayé|divorce|séparation|"
                     r"retard de loyer|fin de contrat", re.I)
DETTE = re.compile(r"dette|prêteur|5-6|crédit|impayé|rembourser", re.I)
PROCHE_MALADE = re.compile(r"(mère|père|parent|enfant|fils|fille|conjoint|mari|femme).{0,20}malad|malad.{0,30}(mère|père|parent|enfant)", re.I)
ETATS_LIEN = ("actif", "proche", "enjeu", "en_pause", "rejete_par_william", "rejet_de_sa_part", "bloque", "clos")

DETAILS = {
    "T13a": {"sante": "malade ({mal})", "sante_proche": "maladie ou accident de {proche}", "argent": "{argent}",
             "famille": "dispute sérieuse ou mauvaise nouvelle dans la famille", "travail": "ennui avec son employeur ou un client{travail}",
             "logement_transport": "panne, coupure ou souci de logement", "relation": "rupture, trahison d'un ami ou conflit de voisinage"},
    "T13b": {"offre_travail": "proposition d'emploi ou de collaboration ailleurs", "famille": "naissance, mariage, décès ou retour d'un proche",
             "sante": "diagnostic, guérison, grossesse ou opération", "logement": "déménagement, bail ou proche hébergé",
             "rencontre": "rencontre qui compte (amicale, amoureuse ou professionnelle)", "argent": "rentrée ou perte d'argent importante",
             "voyage": "départ, retour ou projet de voyage"},
    "T13c": {"depense": "dépense imprévue ({depense})", "rencontre": "croisement, visite ou conversation de voisinage",
             "service_rendu": "service rendu ou reçu", "dispute_breve": "querelle courte", "nouvelle_famille": "nouvelle de la famille ou des amis",
             "transport_meteo": "{transport}", "achat": "achat ({achat})", "rumeur": "rumeur entendue ou colportée"},
    "T13d": {"demarche": "démarche pour son objectif : {objectif}", "rendez_vous": "rendez-vous obtenu ou tenu pour son objectif : {objectif}",
             "argent": "somme reçue, économisée ou investie pour son objectif : {objectif}",
             "decision": "décision prise pour son objectif : {objectif}", "apprentissage": "formation, lecture ou conseil utile : {objectif}"},
}
MAUX = ["forte fièvre", "grippe", "gastro-entérite", "mal de dos", "migraine qui dure", "dengue légère"]
DEPENSES = ["réparation du téléphone", "médicaments", "frais de scolarité", "facture d'électricité plus lourde", "réparation de la moto",
            "cotisation imprévue"]
ACHATS = ["vêtements", "petit électroménager", "cadeau d'anniversaire", "matériel pour la maison"]
TRANSPORTS = {"manille": ["embouteillage monstre sur l'EDSA", "rue inondée après l'averse", "panne du MRT-3, files au quai",
                          "coupure de courant dans le quartier"],
              "luxembourg": ["bouchons sur l'A4 et la frontière", "bus en retard", "orage et routes glissantes", "chantier d'été qui bloque la rue"]}


# ---------------------------------------------------------------- personnages et liens
def personnages():
    return lire_csv(ETAT / "personnages.csv")


def adulte(p, jour):
    try:
        return age(p["naissance"], jour) >= 18
    except (ValueError, KeyError, TypeError):
        return False


def champ(p, cle):
    m = re.search(rf"{cle} : ([^·]+)", p.get("notes", "") or "")
    return m.group(1).strip() if m else ""


def liens_fixes():
    return {l["personnage"]: l for l in (lire_csv(LIENS) if LIENS.exists() else [])}


def fixer_lien(nom, etat, note=""):
    if etat not in ETATS_LIEN:
        sys.exit(f"État inconnu : {etat} ({', '.join(ETATS_LIEN)})")
    p = jet.fiche_personnage(nom)
    if p is None:
        sys.exit(f"Personnage inconnu : {nom}")
    import horloge
    h = horloge.lire()["instant"]
    lignes = [l for l in (lire_csv(LIENS) if LIENS.exists() else []) if l["personnage"] != p["nom"]]
    ancien = next((l for l in (lire_csv(LIENS) if LIENS.exists() else []) if l["personnage"] == p["nom"]), None)
    hist = f"avant : {ancien['etat']} → maintenant : {etat}" if ancien else ""
    lignes.append({"personnage": p["nom"], "etat": etat, "depuis": f"{h:%Y-%m-%d %H:%M}",
                   "note": " · ".join(x for x in (note, hist) if x).replace(";", ",")})
    ecrire_csv(LIENS, lignes, COL_LIENS)
    return p["nom"]


def derniers_echanges():
    """{nom: (dernière date d'échange 'AAAA-MM-JJ', canal)} d'après l'application de rencontre et WhatsApp."""
    res = {}
    profils = {r["id"]: r for r in lire_csv(ETAT / "rencontres.csv")}
    noms = {p["id"]: p["nom"] for p in personnages()}
    for m in lire_csv(ETAT / "rencontres-messages.csv"):
        nom = noms.get(m["profil"])
        if nom and (nom not in res or m["date"] > res[nom][0]):
            res[nom] = (m["date"], "rencontres")
    import base
    for m in base.lire_messages():
        p = jet.fiche_personnage(m["auteur"]) if m["auteur"] != "William" else None
        nom = p["nom"] if p else None
        if nom is None:
            continue
        if nom not in res or m["date"] > res[nom][0]:
            res[nom] = (m["date"], "whatsapp")
    for ident, r in profils.items():
        if r.get("statut") == "bloque" and noms.get(ident):
            res[noms[ident]] = (res.get(noms[ident], ("", "rencontres"))[0], "rencontres")
    return res


def etat_lien(p, jour, echanges=None, fixes=None):
    """(etat, canal) du lien entre William et ce personnage au jour donné."""
    fixes = liens_fixes() if fixes is None else fixes
    echanges = derniers_echanges() if echanges is None else echanges
    profil = next((r for r in lire_csv(ETAT / "rencontres.csv") if r["id"] == p["id"]), None)
    canal = echanges.get(p["nom"], ("", "rencontres" if profil else "whatsapp"))[1]
    if profil and profil.get("statut") == "bloque":
        return "bloque", canal
    if p["nom"] in fixes:
        return fixes[p["nom"]]["etat"], canal
    der = echanges.get(p["nom"])
    if der and der[0] and (jour - dt.date.fromisoformat(der[0])).days <= 7:
        return ("actif" if profil else "contact_recent"), canal
    return "aucun", canal


# ---------------------------------------------------------------- tirages
def pays_de(p):
    return "ph" if routines.zone_de(p) == "manille" else "lu"


def ferie_proche(p, jour):
    import calendrier_2040 as cal
    pays = pays_de(p)
    pays_liste = ("ph",) if pays == "ph" else ("lu", "fr")
    for pp in pays_liste:
        try:
            for d, nom, _ in cal.fetes(jour.year, pp):
                if 0 <= (d - jour).days <= 2:
                    return True
        except Exception:  # noqa: BLE001 (pays sans données de fêtes)
            continue
    return False


def mods_t11(p, jour):
    mods = []
    if FRAGILE.search(champ(p, "souci")):
        mods.append("M80")
    if ferie_proche(p, jour):
        mods.append("M82")
    rt = routines.routine(p)
    if rt["vacances"] and routines.en_vacances(p, jour) and "M83" not in mods:
        mods.append("M83")
    return mods[:3]


def mods_t13(p, table, jour):
    souci = champ(p, "souci") + " " + champ(p, "secret")
    if table == "T13a":
        if DETTE.search(souci):
            return ["M95"]
        if PROCHE_MALADE.search(souci):
            return ["M96"]
    if table == "T13c" and routines.zone_de(p) == "manille" and 6 <= jour.month <= 10:
        return ["M99"]
    return []


def detail(p, table, categorie, rng):
    zone = routines.zone_de(p)
    foyer = champ(p, "foyer")
    proche = "son enfant" if re.search(r"enfant|parent isolé", foyer, re.I) else rng.choice(["sa mère", "son père", "un frère ou une sœur"])
    souci = champ(p, "souci")
    argent = souci if DETTE.search(souci) else rng.choice(["dépense imprévue", "prêt à un proche jamais rendu", "facture en retard",
                                                           "vol ou arnaque"])
    gabarit = DETAILS[table].get(categorie, categorie)
    return gabarit.format(mal=rng.choice(MAUX), proche=proche, argent=argent, travail=(f" ({souci})" if re.search(r"chef|travail|contrat|poste", souci, re.I) else ""),
                          depense=rng.choice(DEPENSES), achat=rng.choice(ACHATS), transport=rng.choice(TRANSPORTS[zone]),
                          objectif=champ(p, "objectif") or "son projet du moment")


def charger_etat():
    try:
        return json.loads(lire_texte(ETAT_JSON) or "{}")
    except ValueError:
        return {}


def sauver_etat(e):
    ecrire_texte(ETAT_JSON, json.dumps(e, ensure_ascii=False, indent=1) + "\n")


def ajouter_vies(lignes):
    vieux = lire_csv(VIES) if VIES.exists() else []
    ecrire_csv(VIES, vieux + lignes, COL_VIES)


def tirer_vie(p, jour, cadence, rng, simule):
    t11 = jet.tirer("T11", mods_t11(p, jour), f"Vie de {p['nom']} ({cadence}, {jour:%d/%m/%Y})", pour=p["nom"], simule=simule, texte=False)
    ligne = {"date": jour.isoformat(), "personnage": p["nom"], "cadence": cadence, "t11": t11["issue"], "categorie": "", "detail": "",
             "initiative": "", "agenda": "", "note": f"T11 jet {t11['jet']:.1f}"}
    if t11["issue"] in CONTENU:
        table = CONTENU[t11["issue"]]
        t13 = jet.tirer(table, mods_t13(p, table, jour), f"Contenu ({t11['issue']}) pour {p['nom']} ({jour:%d/%m/%Y})", pour=p["nom"],
                        simule=simule, texte=False)
        ligne["categorie"] = f"{table}:{t13['issue']}"
        ligne["detail"] = detail(p, table, t13["issue"], rng).replace(";", ",")
        ligne["note"] += f" · {table} jet {t13['jet']:.1f}"
    return ligne


def reponse_en_attente(p, debut, heures=72):
    import agenda
    fin = debut + dt.timedelta(hours=heures)
    for l in agenda.lire():
        if l["statut"] == "prevu" and l["qui"].startswith(p["nom"]) and debut - dt.timedelta(hours=24) <= agenda.instant(l) <= fin:
            return True
    return False


def enjeu_actif(p, fixes):
    l = fixes.get(p["nom"])
    return bool(l and (l["etat"] == "enjeu" or "enjeu" in (l.get("note") or "")))


def initiative(p, jour, etat_l, canal, vie, fixes, simule):
    """T14 (initiative envers William) pour un lien actif ; programme le texte à écrire (reactions.programmer)."""
    import reactions
    zone = routines.zone_de(p)
    tz = fuseaux.analyser_instant(jour.isoformat(), "08:00", zone).tzinfo
    debut_jour = dt.datetime.combine(jour, dt.time(8, 0), tzinfo=tz)
    if reponse_en_attente(p, debut_jour):
        return "", ""
    mods = []
    if etat_l == "enjeu" or enjeu_actif(p, fixes):
        mods.append("M84")
    if etat_l in ("rejete_par_william", "rejet_de_sa_part", "en_pause"):
        mods.append("M85")
    if etat_l == "proche":
        mods.append("M86")
    if vie and vie["t11"] == "coup_dur" and len(mods) < 3:
        mods.append("M87")
    r = jet.tirer("T14", mods[:3], f"Initiative de {p['nom']} envers William ({jour:%d/%m/%Y})", pour=p["nom"], simule=simule)
    if r["issue"] == "aucune" or simule:
        return r["issue"], ""
    m10 = ["M71"] if r["issue"] in ("demande", "information") else ["M74"]
    d = jet.tirer("T10", m10, f"Heure de l'initiative ({r['issue']}) de {p['nom']} ({jour:%d/%m/%Y})", pour=p["nom"])
    if d["issue"] == "plus_tard_ou_jamais":
        return f"{r['issue']} (pas aujourd'hui : T10 plus_tard_ou_jamais)", ""
    fen = routines.fenetres_libres(p, jour, "08:00", "23:00")
    base = fen[0][0] if fen else debut_jour
    import horloge
    base = max(base, horloge.lire()["instant"])  # jamais dans le passé de l'horloge (journée tirée en cours de route)
    t = reactions.heure_apres_delai(p, base, d["issue"])
    raison = (vie or {}).get("detail") or champ(p, "objectif") or "envie de garder le contact"
    i = reactions.intention(p)
    resume = (f"Initiative de {p['nom'].split()[0]} envers William ({r['issue']}) · raison possible tirée de sa vie : {raison}"
              + (f" · intention cachée : {i}" if i else "") + f" · {reactions.fiche_courte(p)}")
    aid, loc = reactions.programmer(p, t, canal if canal in ("rencontres", "whatsapp") else "sms", resume,
                                    f"T14 : {r['issue']} (jet {r['jet']:.1f}{', ' + ', '.join(mods) if mods else ''}) · T10 : {d['issue']}")
    return f"{r['issue']} à {loc:%d/%m %H:%M}", aid


def jour_(jour, simule=False):
    """Journée des personnages en lien actif avec William (T11, T13) et leurs initiatives (T14)."""
    rng = random.SystemRandom()
    echanges, fixes = derniers_echanges(), liens_fixes()
    lignes, resume = [], []
    for p in personnages():
        if not adulte(p, jour):
            continue
        etat_l, canal = etat_lien(p, jour, echanges, fixes)
        if etat_l not in ("actif", "proche", "enjeu", "rejete_par_william", "rejet_de_sa_part"):
            continue
        vie = tirer_vie(p, jour, "jour", rng, simule)
        ini, aid = ("", "")
        if etat_l in ("actif", "proche", "enjeu", "rejete_par_william"):
            ini, aid = initiative(p, jour, etat_l, canal, vie, fixes, simule)
        vie["initiative"], vie["agenda"] = ini, aid
        lignes.append(vie)
        resume.append(f"{p['nom']} [{etat_l}] : {vie['t11']}" + (f" ({vie['detail']})" if vie["detail"] else "") +
                      (f" ; initiative : {ini}" if ini and ini != "aucune" else ""))
    if not simule:
        ajouter_vies(lignes)
    return resume


def semaine(lundi, simule=False):
    """Semaine de tous les personnages qui ne sont pas en scène : T11 une fois, à un jour tiré de la semaine."""
    rng = random.SystemRandom()
    echanges, fixes = derniers_echanges(), liens_fixes()
    lignes, resume = [], []
    for p in personnages():
        if not adulte(p, lundi):
            continue
        etat_l, _ = etat_lien(p, lundi, echanges, fixes)
        if etat_l in ("actif", "proche", "enjeu", "rejete_par_william", "rejet_de_sa_part"):
            continue
        jour = lundi + dt.timedelta(days=rng.randint(0, 6))
        vie = tirer_vie(p, jour, "semaine", rng, simule)
        lignes.append(vie)
        if vie["t11"] != "sans_histoire":
            resume.append(f"{p['nom']} ({jour:%a %d/%m}) : {vie['t11']} ({vie['detail']})")
    if not simule:
        ajouter_vies(lignes)
    return resume


def avancer(jusqua, simule=False):
    """Tire tout ce qui manque : chaque jour jusqu'à `jusqua` INCLUS pour les liens actifs (le jour en cours est tiré dès le premier
    tour du jour : ses événements peuvent arriver pendant la journée), et chaque semaine commencée pour les autres."""
    e = charger_etat()
    import horloge
    dernier = dt.date.fromisoformat(e.get("dernier_jour") or (horloge.lire()["instant"].date() - dt.timedelta(days=1)).isoformat())
    semaines = set(e.get("semaines", []))
    sortie = []
    jour = dernier + dt.timedelta(days=1)
    while jour <= jusqua:
        lundi = jour - dt.timedelta(days=jour.weekday())
        if lundi.isoformat() not in semaines:
            sortie += [f"[semaine du {lundi:%d/%m}] {x}" for x in semaine(lundi, simule)]
            semaines.add(lundi.isoformat())
        sortie += [f"[{jour:%d/%m}] {x}" for x in jour_(jour, simule)]
        e["dernier_jour"] = jour.isoformat()
        jour += dt.timedelta(days=1)
    e["semaines"] = sorted(semaines)
    if not simule:
        sauver_etat(e)
        fiches()
    return sortie


# ---------------------------------------------------------------- lecture
def vies_de(nom, n=12):
    p = jet.fiche_personnage(nom)
    nom = p["nom"] if p else nom
    return [l for l in (lire_csv(VIES) if VIES.exists() else []) if l["personnage"] == nom][-n:]


def fiches():
    """Section « Fiches » de etat/vies-propres.md régénérée : les personnages en lien avec William, avec leurs derniers événements."""
    f = ETAT / "vies-propres.md"
    t = lire_texte(f)
    tete = t.split("\n## Fiches")[0].rstrip("\n")
    import horloge
    jour = horloge.lire()["instant"].date()
    echanges, fixes = derniers_echanges(), liens_fixes()
    blocs = []
    for p in personnages():
        if not adulte(p, jour):
            continue
        etat_l, canal = etat_lien(p, jour, echanges, fixes)
        if etat_l == "aucun" and p.get("statut") not in ("recurrent", "figurant"):
            continue
        vs = vies_de(p["nom"], 5)
        rt = routines.decrire(p)
        lignes = [f"### {p['nom']} ({p.get('role') or p.get('metier')})",
                  f"- **Lien avec William** : {etat_l} ({canal})" + (f" · {fixes[p['nom']]['note']}" if p['nom'] in fixes and fixes[p['nom']]['note'] else ""),
                  f"- **Objectif** : {champ(p, 'objectif') or '—'} ; **souci** : {champ(p, 'souci') or '—'} ; **foyer** : {champ(p, 'foyer') or '—'}",
                  f"- **Secret (moteur seulement)** : {champ(p, 'secret') or '—'}",
                  f"- **Horaires** : {rt.split(' : ', 1)[-1]}",
                  "- **Derniers événements** : " + ("; ".join(f"{v['date'][8:10]}/{v['date'][5:7]} {v['t11']}" + (f" ({v['detail']})" if v['detail'] else "")
                                                       + (f", initiative {v['initiative']}" if v['initiative'] and v['initiative'] != 'aucune' else "")
                                                       for v in vs) or "—")]
        blocs.append("\n".join(lignes))
    corps = ("\n\n## Fiches\n\n> Section RÉGÉNÉRÉE par `python outils/monde_vivant.py fiches` (appelé par `tour.py fin`) : ne pas éditer à la main ; "
             "les événements complets sont dans `etat/vies.csv`.\n\n" + ("\n\n".join(blocs) if blocs else "*(Aucun personnage en lien avec William.)*") + "\n")
    ecrire_texte(f, tete + corps)


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    for nom in ("jour", "semaine"):
        q = sp.add_parser(nom)
        q.add_argument("date")
        q.add_argument("--simule", action="store_true")
    q = sp.add_parser("avancer")
    q.add_argument("--jusqua", required=True)
    q.add_argument("--simule", action="store_true")
    sp.add_parser("liens")
    q = sp.add_parser("lien")
    q.add_argument("nom")
    q.add_argument("etat")
    q.add_argument("--note", default="")
    q = sp.add_parser("vies")
    q.add_argument("nom")
    sp.add_parser("fiches")
    args = ap.parse_args()
    if args.cmd == "jour":
        for x in jour_(dt.date.fromisoformat(args.date), args.simule):
            print(x)
    elif args.cmd == "semaine":
        for x in semaine(dt.date.fromisoformat(args.date), args.simule):
            print(x)
    elif args.cmd == "avancer":
        for x in avancer(dt.date.fromisoformat(args.jusqua), args.simule):
            print(x)
    elif args.cmd == "liens":
        import horloge
        jour = horloge.lire()["instant"].date()
        echanges, fixes = derniers_echanges(), liens_fixes()
        for p in personnages():
            e, c = etat_lien(p, jour, echanges, fixes)
            if e != "aucun":
                print(f"{p['nom']:24s} {e:20s} {c}")
    elif args.cmd == "lien":
        print(f"Lien fixé : {fixer_lien(args.nom, args.etat, args.note)} → {args.etat}")
    elif args.cmd == "vies":
        for v in vies_de(args.nom, 50):
            print(f"{v['date']} [{v['cadence']}] {v['t11']} {v['categorie']} {v['detail']} {v['initiative']}")
    else:
        fiches()
        print("Fiches régénérées : etat/vies-propres.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
