"""RÉACTIONS PROGRAMMÉES (créé le 14/10/2026 : univers vivant, simulation surtout informatique, moins de travail pour l'IA).
Quand William écrit, aime un profil ou attend une réponse, CET OUTIL tire la réaction dans la table (règle 17), tire le délai (T10)
avec les modificateurs qui découlent des faits (le personnage dort, travaille ou conduit : M70 ; l'argent est en jeu pour lui :
M71 ; froideur déjà tirée : M72), cale l'heure sur les HORAIRES DE VIE du personnage (`outils/routines.py`) et programme la suite :
  - un texte à écrire → une ligne d'agenda NON CONNUE de William, avec un résumé pour le moteur (`agenda.csv`, marque [reaction …]) ;
  - un fait sans texte (match, blocage) → une action programmée exécutée toute seule par `tour.py fin` (`actions.py`).
Au moment voulu, le moteur écrit seulement le texte : `python outils/reactions.py jouer A031 --texte "…"` enregistre le message
dans la bonne application, à la bonne heure, et clôt la ligne d'agenda.

    python outils/reactions.py message --pour "Kiara Reyes" --quand "2040-07-20 10:05" --acte "texte de William" [--mod M47] [--canal rencontres]
    python outils/reactions.py like --pour "Yuna …" --quand "…"            # « j'aime » : T21a (M45 selon l'intention cachée, M48)
    python outils/reactions.py delai --pour "Clément Grandjean" --quand "…" --canal whatsapp --resume "répond au refus" [--mod M73]
    python outils/reactions.py jouer A031 --texte "Hi William! …"
    python outils/reactions.py en-attente                                  # réponses programmées, non jouées
    python outils/reactions.py rencontre --pour "Kiara Reyes" --quand "…" --lieu "…"   # rencontre en personne : consignée, puis T23
Depuis le 14/10/2026 (P24, validée) : un message de William à un profil dont l'intention cachée tourne autour de l'argent, après au
moins un jour sans échange, tire aussi T23 (évolution de l'intention : M102 rencontre déjà faite, M103 argent déjà donné, M104
situation financière mise en avant) ; l'issue s'écrit dans le résumé de la réponse programmée. Même tirage après une rencontre.

`rencontres.py message --auteur william` et `rencontres.py aimer` appellent cet outil d'eux-mêmes (sauf --sans-reaction).
Les sous-tirages qui appliquent une issue déjà tirée (jour d'une réponse tardive, minute dans une fenêtre libre) sont consignés
[PROCÉDURE : …] (jet.py) ; rien n'est choisi à la main, rien n'est rejoué.
"""
import argparse
import datetime as dt
import json
import random
import re
import sys

from commun import ETAT, MEMOIRE, OUTILS, lire_csv, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
import agenda  # noqa: E402
import fuseaux  # noqa: E402
import jet  # noqa: E402
import routines  # noqa: E402

DELAIS = {"immediat": (1, 4), "rapide": (5, 30), "dans_l_heure": (30, 60), "dans_la_journee": (60, 360),
          "le_soir_ou_lendemain": (360, 1440), "plus_tard_ou_jamais": (1440, 4320)}
FROIDS = {"froideur", "evitement", "garde_distance", "ignore", "rancune_silencieuse", "esquive_pro", "agacement_net", "bloque",
          "releve_esquive", "refus_net", "mefiance"}
ARGENT = {"aide_financiere", "arnaque", "travail_sexuel"}
RENCONTRES_FAITES = ETAT / "rencontres-en-personne.csv"  # 14/10/2026 : rencontres en personne (M102)
COL_RF = ["personnage", "date", "heure", "lieu", "note"]
MOTS_ARGENT = re.compile(r"situation|rich|wealth|money|salary|well[- ]off|financ|argent|riche|salaire|fortune|afford", re.I)
MARQUE = re.compile(r"\[reaction pour=([\w-]+) canal=(\w+)\]")
CANAUX = {"rencontres": "application de rencontre", "whatsapp": "WhatsApp", "sms": "SMS"}


def profil_rencontre(p):
    for r in lire_csv(ETAT / "rencontres.csv"):
        if r["id"] == p.get("id"):
            return r
    return None


def intention(p):
    r = profil_rencontre(p)
    return (r or {}).get("intention", "")


def instant_txt(texte, fuseau):
    d, h = texte.split()
    return fuseaux.analyser_instant(d, h, fuseau)


def froideur_recente(p, quand, jours=7):
    """M72 : une issue froide déjà tirée pour ce personnage dans les `jours` derniers jours (memoire/tirages.jsonl)."""
    f = MEMOIRE / "tirages.jsonl"
    if not f.exists():
        return False
    limite = quand - dt.timedelta(days=jours)
    for l in f.read_text(encoding="utf-8").splitlines():
        try:
            o = json.loads(l)
        except ValueError:
            continue
        if o.get("simule") or o.get("pour") != p.get("nom") or o.get("mode") != "table" or o.get("issue") not in FROIDS:
            continue
        try:
            d, h, z = (o.get("horloge") or "").split()
            t = fuseaux.analyser_instant(d, h, z)
        except ValueError:
            continue
        if t >= limite:
            return True
    return False


def langue_scolaire(p):
    """R5 (22/10/2026) : « anglais : scolaire » écrit dans les notes ou les traits du registre."""
    return bool(re.search(r"anglais\s*:?\s*scolaire", (p.get("notes") or "") + " " + (p.get("traits") or ""), re.I))


def message_complexe(acte):
    return len(acte or "") > 200 or len(re.findall(r"[.!?…]+(?:\s|$)", acte or "")) > 3


def mods_delai(p, quand, extra=(), acte=None):
    mods = []
    if routines.etat(p, quand) in ("sommeil", "travail", "trajet"):
        mods.append("M70")
    if froideur_recente(p, quand):
        mods.append("M72")
    elif intention(p) in ARGENT:
        mods.append("M71")
    if acte and langue_scolaire(p) and message_complexe(acte) and "M105" not in mods and len(mods) < 3:
        mods.append("M105")  # R5 : friction de langue (jamais de refus, seulement un délai plus long)
    for m in extra:
        if m not in mods and len(mods) < 3:
            mods.append(m)
    return mods[:3]


def procedure(libelle, valeur, regle, pour=""):
    """Consigne un calcul de procédure (heure fixée par les horaires de vie, minute au hasard dans un intervalle tiré)."""
    ligne = f"- Procédure « {libelle} » : {valeur} [PROCÉDURE : {regle}]"
    jet.consigner(ligne)
    jet.consigner_json({"mode": "procedure", "libelle": libelle, "pour": pour, "valeur": valeur, "regle": regle})
    return ligne


def heure_apres_delai(p, quand, issue_t10):
    """Instant de la réponse : minute au hasard dans l'intervalle de T10, puis décalée à la première minute où le personnage est
    joignable (s'il dort, travaille ou conduit à ce moment-là, il répond quand il redevient libre, 0 à 20 min plus tard)."""
    rng = random.SystemRandom()
    a, b = DELAIS[issue_t10]
    t = quand + dt.timedelta(minutes=rng.randint(a, b))
    if not routines.joignable(p, t):
        t = routines.prochaine_dispo(p, t) + dt.timedelta(minutes=rng.randint(0, 20))
    return t


def heure_tardive(p, quand):
    """Réponse « un ou deux jours plus tard » (T21b repond_tard) : le jour (lendemain ou surlendemain, 50/50), puis une minute au
    hasard dans les fenêtres joignables de ce jour (de 8 h à 23 h 30, heure du personnage)."""
    r = jet.tirer_libre(f"{p['nom']} : jour de la réponse tardive (lendemain OUI, surlendemain NON)", 50, pour=p["nom"],
                        procedure="T21b repond_tard : un ou deux jours plus tard")
    zone = routines.zone_de(p)
    jour = fuseaux.convertir(quand, zone).date() + dt.timedelta(days=1 if r["oui"] else 2)
    return minute_libre(p, jour, "08:00", "23:30")


def programmer(p, quand_reponse, canal, resume, note_tirages):
    """Ligne d'agenda NON CONNUE de William : le texte se écrit au moment voulu (reactions.py jouer)."""
    zone = routines.zone_de(p)
    loc = fuseaux.convertir(quand_reponse, zone)
    lignes = agenda.lire()
    nouvelle = {"id": agenda.prochain_id(lignes), "date": f"{loc:%Y-%m-%d}", "heure": f"{loc:%H:%M}", "lieu": zone,
                "qui": f"{p['nom']} ({CANAUX.get(canal, canal)})", "quoi": resume.replace(";", ","), "statut": "prevu", "connu": "non",
                "note": (f"NON CONNU DE WILLIAM avant l'heure · {note_tirages} · texte à écrire d'après la fiche (reactions.py jouer) "
                         f"[reaction pour={p['id']} canal={canal}]").replace(";", ",")}
    lignes.append(nouvelle)
    agenda.ecrire(lignes)
    return nouvelle["id"], loc


def fiche_courte(p):
    """Ce que le moteur doit garder en tête pour écrire le texte (ton, intention, défauts, souci)."""
    morceaux = []
    i = intention(p)
    if i:
        morceaux.append(f"intention cachée : {i}")
    notes = p.get("notes", "")
    for cle in ("souci", "objectif", "foyer"):
        m = re.search(rf"{cle} : ([^·]+)", notes)
        if m:
            morceaux.append(f"{cle} : {m.group(1).strip()}")
    traits = p.get("traits", "")
    m = re.search(r"défauts : ([^·]+)", traits)
    if m:
        morceaux.append(f"défauts : {m.group(1).strip()}")
    return " · ".join(morceaux)


def minute_libre(p, jour, de="08:00", a="23:30"):
    """Une minute au hasard dans les heures où le personnage est joignable ce jour-là (heure de son fuseau)."""
    fen = routines.fenetres_libres(p, jour, de, a)
    if not fen:
        zone = routines.zone_de(p)
        tz = fuseaux.analyser_instant(jour.isoformat(), "08:00", zone).tzinfo
        return routines.prochaine_dispo(p, dt.datetime.combine(jour, dt.time(8, 0), tzinfo=tz))
    x = random.SystemRandom().uniform(0, sum((b - a_).total_seconds() for a_, b in fen))
    for a_, b in fen:
        d = (b - a_).total_seconds()
        if x <= d:
            return (a_ + dt.timedelta(seconds=x)).replace(second=0, microsecond=0)
        x -= d
    return fen[-1][0]


def _messages_rencontre(p):
    return [m for m in lire_csv(ETAT / "rencontres-messages.csv") if m["profil"] == p.get("id")]


def echange_suivi(p, quand):
    """Nouvel échange suivi (T23) : la conversation existe et rien ne s'est dit depuis au moins un jour avant ce message."""
    zone = routines.zone_de(p)
    local = fuseaux.convertir(quand, zone).replace(tzinfo=None)
    avant = [dt.datetime.fromisoformat(f"{m['date']} {m['heure']}") for m in _messages_rencontre(p)]
    avant = [x for x in avant if x < local - dt.timedelta(minutes=1)]
    return bool(avant) and local - max(avant) >= dt.timedelta(days=1)


def mods_t23(p, apres_rencontre=False):
    mods = []
    if apres_rencontre or any(r["personnage"] == p["nom"] for r in lire_csv(RENCONTRES_FAITES)):
        mods.append("M102")
    import grand_livre as gl
    if any(float(l["montant"] or 0) < 0 and l["type"] in ("mouvement", "prevu_realise") and (p["nom"] in l["libelle"] or p.get("id", "@") in l["libelle"])
           for l in gl.lire()):
        mods.append("M103")
    if any(m["auteur"] == "william" and MOTS_ARGENT.search(m["texte"]) for m in _messages_rencontre(p)):
        mods.append("M104")
    return mods[:3]


def tirer_t23(p, libelle, apres_rencontre=False, simule=False):
    """T23 : évolution de l'intention cachée d'un profil intéressé par l'argent (aide financière, arnaque, travail sexuel)."""
    mods = mods_t23(p, apres_rencontre)
    r = jet.tirer("T23", mods, f"{p['nom']} : évolution de son intention ({libelle})", pour=p["nom"], simule=simule)
    return {"issue": r["issue"], "jet": r["jet"], "mods": mods}


def rencontre(nom, quand, lieu, note="", simule=False):
    """Rencontre en personne avec William : consignée (M102 ensuite), puis T23 si l'intention cachée tourne autour de l'argent."""
    from commun import ecrire_csv
    p = routines.personnage(nom)
    loc = fuseaux.convertir(quand, routines.zone_de(p))
    res = {"pour": p["nom"], "rencontre": f"{loc:%d/%m %H:%M}"}
    if not simule:
        lignes = lire_csv(RENCONTRES_FAITES) + [{"personnage": p["nom"], "date": f"{loc:%Y-%m-%d}", "heure": f"{loc:%H:%M}",
                                                 "lieu": lieu.replace(";", ","), "note": note.replace(";", ",")}]
        ecrire_csv(RENCONTRES_FAITES, lignes, COL_RF)
    if intention(p) in ARGENT:
        t = tirer_t23(p, f"après la rencontre du {loc:%d/%m} ({lieu[:40]})", apres_rencontre=True, simule=simule)
        res["T23"] = t
    return res


def message(nom, quand, acte, table="T21b", mods=(), canal="rencontres", simule=False):
    """Réaction d'un profil (ou d'un contact) à un message de William ; renvoie un dict résumé."""
    p = routines.personnage(nom)
    mods = list(mods)
    if table == "T21b" and intention(p) in ARGENT and "M46" not in mods:
        mods.insert(0, "M46")
    zone = routines.zone_de(p)
    heure_p = fuseaux.convertir(quand, zone)
    r = jet.tirer(table, mods[:3], f"{p['nom']} : réaction au message de William du {heure_p:%d/%m %H:%M} ({zone}) : « {acte[:90]} »",
                  pour=p["nom"], simule=simule)
    res = {"pour": p["nom"], "table": table, "issue": r["issue"], "jet": r["jet"], "mods": mods[:3]}
    if simule:
        return res
    if r["issue"] in ("repond", "repond_tard"):
        if r["issue"] == "repond":
            m10 = mods_delai(p, quand, acte=acte)
            d = jet.tirer("T10", m10, f"{p['nom']} : délai de sa réponse ({table} : repond)", pour=p["nom"])
            t = heure_apres_delai(p, quand, d["issue"])
            note = f"{table} : {r['issue']} (jet {r['jet']:.1f}{', ' + ', '.join(mods[:3]) if mods else ''}) · T10 : {d['issue']} (jet {d['jet']:.1f}{', ' + ', '.join(m10) if m10 else ''})"
        else:
            t = heure_tardive(p, quand)
            note = f"{table} : repond_tard (jet {r['jet']:.1f}{', ' + ', '.join(mods[:3]) if mods else ''})"
        procedure(f"{p['nom']} : heure de la réponse", f"{fuseaux.convertir(t, zone):%d/%m %H:%M} ({zone})",
                  "horaires de vie (routines.py) et intervalle tiré", pour=p["nom"])
        resume = (f"Réponse de {p['prenom'] if 'prenom' in p else p['nom'].split()[0]} au message de William du {heure_p:%d/%m à %H:%M} "
                  f"(« {acte[:120]} ») · {fiche_courte(p)}")
        if canal == "rencontres" and intention(p) in ARGENT and echange_suivi(p, quand):  # T23 (P24, validée le 14/10/2026)
            t23 = tirer_t23(p, f"nouvel échange du {heure_p:%d/%m %H:%M}")
            resume += f" · évolution de son intention (T23) : {t23['issue']}, à jouer dans cette réponse"
            note += f" · T23 : {t23['issue']} (jet {t23['jet']:.1f}{', ' + ', '.join(t23['mods']) if t23['mods'] else ''})"
            res["T23"] = t23["issue"]
        aid, loc = programmer(p, t, canal, resume, note)
        res.update({"agenda": aid, "heure": f"{loc:%d/%m %H:%M} ({zone})"})
    elif r["issue"] == "bloque":
        m10 = mods_delai(p, quand)
        d = jet.tirer("T10", m10, f"{p['nom']} : délai avant le blocage ({table} : bloque)", pour=p["nom"])
        t = heure_apres_delai(p, quand, d["issue"])
        import actions
        if canal == "rencontres":
            actions.ajouter(t, zone, ["rencontres.py", "bloquer", p["id"]], origine=f"{table} : bloque (jet {r['jet']:.1f})")
        aid, loc = programmer(p, t, canal, f"{p['nom']} bloque William (discussion et profil disparaissent de l'application) : à "
                              "narrer quand William le voit, sans explication", f"{table} : bloque (jet {r['jet']:.1f}) · T10 : {d['issue']}")
        res.update({"agenda": aid, "heure": f"{loc:%d/%m %H:%M} ({zone})"})
    return res


def like(nom, quand, mods=(), simule=False):
    """« J'aime » de William sur l'application : T21a (M45 si l'intention cachée tourne autour de l'argent, M48 : profil de William
    remarqué), puis T10 et horaires de vie pour l'heure ; match → action programmée ; match et message → texte à écrire."""
    p = routines.personnage(nom)
    mods = list(mods)
    if intention(p) in ARGENT and "M45" not in mods:
        mods.append("M45")
    if "M48" not in mods:
        mods.append("M48")
    zone = routines.zone_de(p)
    heure_p = fuseaux.convertir(quand, zone)
    r = jet.tirer("T21a", mods[:3], f"{p['nom']} : réaction au « j'aime » de William du {heure_p:%d/%m %H:%M} ({zone})", pour=p["nom"],
                  simule=simule)
    res = {"pour": p["nom"], "table": "T21a", "issue": r["issue"], "jet": r["jet"], "mods": mods[:3]}
    if simule or r["issue"] in ("aucune_reponse", "vu_sans_suite"):
        return res
    import actions
    m10 = mods_delai(p, quand)
    d = jet.tirer("T10", m10, f"{p['nom']} : délai de sa réaction au « j'aime » (T21a : {r['issue']})", pour=p["nom"])
    t = heure_apres_delai(p, quand, d["issue"])
    if r["issue"] == "bloque":
        actions.ajouter(t, zone, ["rencontres.py", "bloquer", p["id"]], origine=f"T21a : bloque (jet {r['jet']:.1f})")
        res.update({"heure": f"{fuseaux.convertir(t, zone):%d/%m %H:%M} ({zone})"})
        return res
    actions.ajouter(t, zone, ["rencontres.py", "match", p["id"]], origine=f"T21a : {r['issue']} (jet {r['jet']:.1f}) · T10 : {d['issue']}")
    res["heure"] = f"{fuseaux.convertir(t, zone):%d/%m %H:%M} ({zone})"
    if r["issue"] == "match_et_message":
        t2 = t + dt.timedelta(minutes=random.SystemRandom().randint(1, 4))
        aid, _ = programmer(p, t2, "rencontres", f"Premier message de {p['nom'].split()[0]} à William après le match · {fiche_courte(p)}",
                            f"T21a : match_et_message (jet {r['jet']:.1f}) · T10 : {d['issue']}")
        res["agenda"] = aid
    return res


def delai(nom, quand, canal, resume, mods=(), programmer_ligne=True):
    """Délai d'une réponse décidée par ailleurs (contenu tiré dans une autre table ou d'après la fiche) : T10 + horaires de vie."""
    p = routines.personnage(nom)
    m10 = mods_delai(p, quand, mods)
    d = jet.tirer("T10", m10, f"{p['nom']} : délai ({resume[:80]})", pour=p["nom"])
    t = heure_apres_delai(p, quand, d["issue"])
    zone = routines.zone_de(p)
    res = {"pour": p["nom"], "T10": d["issue"], "jet": d["jet"], "heure": f"{fuseaux.convertir(t, zone):%d/%m %H:%M} ({zone})"}
    if programmer_ligne:
        aid, _ = programmer(p, t, canal, f"{resume} · {fiche_courte(p)}", f"T10 : {d['issue']} (jet {d['jet']:.1f}{', ' + ', '.join(m10) if m10 else ''})")
        res["agenda"] = aid
    return res


CANAUX_AGENT = {"linkedin", "facebook", "novojob", "educarriere", "coinafrique", "kosafi", "instagram", "reddit", "indeed", "courriel"}  # "courriel" : la messagerie professionnelle du projet, lue par le directeur general virtuel seul


def jouer(aid, texte, quand=None):
    """Écrit le texte d'une réaction programmée : enregistre le message dans l'application, à l'heure prévue, et clôt l'agenda."""
    import subprocess
    lignes = agenda.lire()
    l = next((x for x in lignes if x["id"] == aid), None)
    if l is None:
        sys.exit(f"Ligne d'agenda introuvable : {aid}")
    m = MARQUE.search(l["note"])
    if not m:
        sys.exit(f"{aid} n'est pas une réaction programmée (marque [reaction …] absente)")
    ident, canal = m.group(1), m.group(2)
    t = instant_txt(f"{l['date']} {l['heure']}", l["lieu"])
    if quand:
        t = instant_txt(quand, horloge_fuseau())
    t_horloge = fuseaux.convertir(t, horloge_fuseau())
    texte_propre = texte.replace(";", ",")
    if canal in CANAUX_AGENT:
        # canal lu par l'agent IA seul (annonces, LinkedIn, Facebook) : aucune conversation visible dans le téléphone de William (piège 95)
        cmd = None
    elif canal == "rencontres":
        cmd = [sys.executable, str(OUTILS / "rencontres.py"), "message", ident, "--auteur", "profil", "--texte", texte_propre,
               "--quand", f"{t_horloge:%Y-%m-%d %H:%M}"]
    else:
        p = routines.personnage(ident)
        cmd = [sys.executable, str(OUTILS / "whatsapp.py"), "message", "--avec", p["nom"], "--auteur", "contact", "--texte", texte_propre,
               "--quand", f"{t_horloge:%Y-%m-%d %H:%M}"]
    if cmd is not None:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode:
            sys.exit(r.stderr or r.stdout)
    l["statut"] = "fait"
    l["note"] = (l["note"] + f" | joué : « {texte_propre[:80]} »").replace(";", ",")
    agenda.ecrire(lignes)
    return f"{aid} joué : message de {l['qui']} à {t_horloge:%d/%m %H:%M} ({horloge_fuseau()})"


def horloge_fuseau():
    import horloge
    return horloge.lire()["fuseau"]


def en_attente():
    res = []
    for l in sorted(agenda.lire(), key=agenda.instant):
        if l["statut"] == "prevu" and MARQUE.search(l["note"]):
            res.append(agenda.afficher(l, horloge_fuseau()))
    return res


def quand_arg(texte):
    import horloge
    h = horloge.lire()
    return instant_txt(texte, h["fuseau"]) if texte else h["instant"]


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("message")
    p.add_argument("--pour", required=True)
    p.add_argument("--quand")
    p.add_argument("--acte", required=True)
    p.add_argument("--table", default="T21b")
    p.add_argument("--mod", action="append", default=[])
    p.add_argument("--canal", default="rencontres")
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("like")
    p.add_argument("--pour", required=True)
    p.add_argument("--quand")
    p.add_argument("--mod", action="append", default=[])
    p.add_argument("--simule", action="store_true")
    p = sp.add_parser("delai")
    p.add_argument("--pour", required=True)
    p.add_argument("--quand")
    p.add_argument("--canal", default="whatsapp")
    p.add_argument("--resume", required=True)
    p.add_argument("--mod", action="append", default=[])
    p.add_argument("--sans-agenda", action="store_true")
    p = sp.add_parser("jouer")
    p.add_argument("id")
    p.add_argument("--texte", required=True)
    p.add_argument("--quand")
    sp.add_parser("en-attente")
    p = sp.add_parser("rencontre")
    p.add_argument("--pour", required=True)
    p.add_argument("--quand", required=True)
    p.add_argument("--lieu", required=True)
    p.add_argument("--note", default="")
    p.add_argument("--simule", action="store_true")
    args = ap.parse_args()
    if args.cmd == "message":
        print(json.dumps(message(args.pour, quand_arg(args.quand), args.acte, args.table, args.mod, args.canal, args.simule), ensure_ascii=False))
    elif args.cmd == "like":
        print(json.dumps(like(args.pour, quand_arg(args.quand), args.mod, args.simule), ensure_ascii=False))
    elif args.cmd == "delai":
        print(json.dumps(delai(args.pour, quand_arg(args.quand), args.canal, args.resume, args.mod, not args.sans_agenda), ensure_ascii=False))
    elif args.cmd == "jouer":
        print(jouer(args.id, args.texte, args.quand))
    elif args.cmd == "rencontre":
        print(json.dumps(rencontre(args.pour, quand_arg(args.quand), args.lieu, args.note, args.simule), ensure_ascii=False))
    else:
        for l in en_attente():
            print(l)
    return 0


if __name__ == "__main__":
    sys.exit(main())
