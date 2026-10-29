"""ORCHESTRATEUR DE TOUR (créé le 11/10/2026) : un tour = deux commandes au lieu d'une dizaine, pour que rien ne soit oublié et
que n'importe quel agent joue de la même façon.

    python outils/tour.py debut                                   # fiche moteur : tout ce qu'il faut savoir avant d'écrire
    python outils/tour.py debut --jusqua "2040-07-14 12:00"       # + ce qui tombe d'ici l'heure de fin prévue du tour
    python outils/tour.py fin --jusqua "2040-07-14 09:40" --lieu "Audun-le-Tiche, chez William" \\
        --attente "Sa matinée" --texte brouillon.md --message "texte dicté par le joueur"
    python outils/tour.py fin ... --commit "feat: samedi 14/07 09h40 ..." --co-auteur "Claude Opus 5.5 <noreply@anthropic.com>" --fusionner
    python outils/tour.py apercu --jusqua "2040-07-16 08:00"      # avance rapide (« Go ») : tout ce qui tombe d'ici là, jour par jour

`debut` (lecture, sauf la météo du jour et des 3 jours suivants qu'il tire si besoin) : alertes de relais (sessions parallèles,
verrou), horloge, météo réelle et prévision, soleil, fériés, vacances et événements, échéances (cachées comprises, signalées),
paliers de fronts, mouvements d'argent prévus, rituels du moteur dus, corps de William, lieu courant (ouvert ? deux détails
d'ambiance non utilisés récemment), personnages récurrents ; puis il régénère etat/resume.md et la base de données.
`fin` : règle l'horloge (et le compteur de tours), réalise les mouvements d'argent échus et prévoit ceux des 60 jours suivants,
tire la météo jusqu'à la nouvelle date, enregistre le TEXTE EXACT du tour et le message du joueur (etat/dernier-tour.md et
journal/tours/AAAA-MM-JJ.md : le prochain agent reprend dans la même voix), passe le brouillon à la chasse aux tics, régénère
le résumé, la base et la note de relais, lance le contrôle de cohérence, puis committe et fusionne si demandé.
Depuis le 14/10/2026 (univers vivant, simulation surtout informatique), `fin` fait aussi : les actions programmées échues
(actions.py : matchs, blocages…), la vie des personnages (monde_vivant.py : journées, semaines, initiatives envers William), les
fiches courtes des jours clos et la fiche complète due (d'après les données), les lignes du journal (--journal, tirages du tour,
attente), les notes des fils ouverts (--fil "4: texte"), l'entrée du §9 (--resume, archivage et synchronisation des fichiers
maîtres), le résumé des changements du téléphone, et l'enregistrement git à chaque tour (--enregistrer, sans libérer le verrou).
Tour économe : `tour.py fin --jusqua … --texte brouillon --joueur message --resume "…" --journal "…" --enregistrer`.
Ce que l'orchestrateur ne fait PAS : écrire le texte du tour et des messages des personnages, décider à la place de William.
"""
import argparse
import datetime as dt
import subprocess
import sys

from commun import (ETAT, JOURNAL, OUTILS, RACINE, ajouter_texte, date_fr, ecrire_texte, heure_fr, lire_csv, lire_texte, utf8)

sys.path.insert(0, str(OUTILS))
DERNIER_TOUR = ETAT / "dernier-tour.md"


def lancer(*args, silencieux=True):
    r = subprocess.run([sys.executable, *[str(a) for a in args]], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", cwd=str(RACINE))
    if not silencieux:
        print(r.stdout, end="")
    return r


def section(titre, lignes):
    print(f"\n## {titre}")
    for l in lignes or ["- rien"]:
        print(l if l.startswith(("-", " ", "|")) else f"- {l}")


def lieu_courant(texte_lieu):
    import lieux
    tl = texte_lieu.lower()
    if "chez william" in tl or "maison" in tl and "audun" in tl:
        return "maison_william"
    meilleur = None
    for i, l in lieux.lire().items():
        mots = [m for m in l["nom"].lower().replace("(", " ").replace(")", " ").replace(",", " ").split() if len(m) > 4]
        score = sum(m in tl for m in mots)
        if score >= 2 and (meilleur is None or score > meilleur[0]):
            meilleur = (score, i)
    return meilleur[1] if meilleur else None


def cmd_debut(args):
    import agenda
    import calendrier_2040 as cal
    import corps
    import echeancier
    import fronts
    import horloge
    import lieux
    import meteo
    import relais
    import rituels
    h = horloge.lire()
    t = h["instant"]
    naif = t.replace(tzinfo=None)
    jour = t.date()
    fin = t + dt.timedelta(hours=24)
    if args.jusqua:
        d, hh = args.jusqua.split()
        fin = max(fin, agenda.fuseaux.analyser_instant(d, hh, h["fuseau"]))
    print(f"# Fiche moteur — {date_fr(t)}, {heure_fr(t)} ({h['fuseau']}) — tour n° {h.get('tour', 0) + 1} à jouer")
    print("(Pour le moteur seul : ni chiffres, ni jets, ni lignes cachées dans le texte du joueur.)")
    g = relais.etat_git()
    alertes = list(g["alertes"])
    av = relais.alerte_verrou()
    if av:
        alertes.insert(0, av)
    if alertes:
        section("⚠ ALERTES DE RELAIS (régler avant de jouer)", [f"- {a}" for a in alertes])
    section("Situation", [f"- Lieu : {h['lieu']}"] + [f"- En attente de William : {a}" for a in h["attentes"]])
    # météo et ciel
    meteo.assurer(jour + dt.timedelta(days=3))
    v = meteo.lire()[jour.isoformat()]
    lev, cou = cal.soleil(jour, meteo.lieu_affichage())
    l_meteo = [f"- Vérité du jour : {v['description']} (type {v['type']})",
               f"- Maintenant : environ {meteo.temperature_a(v, naif):.0f} °C ; soleil levé à {lev:%H:%M}, couché à {cou:%H:%M}"]
    prev = [meteo.prevision(jour + dt.timedelta(days=i), jour) for i in (1, 2)]
    l_meteo.append("- Prévision vue par William : " + " ; ".join(
        f"{'demain' if p['echeance'] == 1 else 'après-demain'} {p['ciel']}, {p['tmin']}/{p['tmax']} °C, pluie {p['risque_pluie']} %"
        for p in prev))
    section("Météo (meteo.py)", l_meteo)
    # calendrier
    l_cal = []
    for pays in (("ph", "lu", "fr") if h["fuseau"] == "manille" else ("kr", "lu", "fr") if h["fuseau"] == "seoul" else ("fr", "lu")):
        for d, nom, _ in cal.fetes(jour.year, pays):
            if d == jour:
                l_cal.append(f"- Aujourd'hui férié ({pays.upper()}) : {nom}")
    ps = cal.periode_scolaire(jour, "lu")
    if ps:
        l_cal.append(f"- Calendrier scolaire (LU) : {ps['periode']} du {ps['debut']} au {ps['fin']} [{ps['statut']}]")
    psf = cal.periode_scolaire(jour, "fr")
    if psf:
        l_cal.append(f"- Calendrier scolaire (FR, zone B) : {psf['periode']} jusqu'au {psf['fin']} [{psf['statut']}]")
    for e in cal.lire_donnees("evenements.csv"):
        if e["debut"] <= (jour + dt.timedelta(days=7)).isoformat() and e["fin"] >= jour.isoformat():
            l_cal.append(f"- Événement : {e['debut']} -> {e['fin']} {e['lieu']} : {e['evenement'][:120]} [{e['fiabilite']}]")
    section("Calendrier", l_cal)
    # échéances
    ordre = sorted(agenda.lire(), key=agenda.instant)
    retards = [l for l in ordre if l["statut"] == "prevu" and agenda.instant(l) < t]
    dus = [l for l in ordre if l["statut"] in ("prevu", "latent") and t <= agenda.instant(l) <= fin]
    section("Échéances (règle 14 : jouer, reporter avec raison ou annuler)",
            [f"- RETARD : {agenda.afficher(l, h['fuseau'])}" for l in retards] + [f"- {agenda.afficher(l, h['fuseau'])}" for l in dus]
            + [f"- FRONT : {x}" for x in fronts.dus()])
    import grand_livre as gl
    mouvements = [l for l in sorted(gl.lire(), key=gl.quand) if l["type"] == "prevu"
                  and naif < gl.quand(l) <= fin.replace(tzinfo=None) + dt.timedelta(days=7)]
    section("Argent : mouvements prévus d'ici 7 jours (échéancier)",
            [f"- {l['date']} {l['heure']} {float(l['montant']):+.2f} € ({l['compte']}) {l['libelle']}" for l in mouvements])
    r = [x for x in rituels.bilan(t) if x[1] != "sans objet"]
    section("Rituels du moteur", [f"- [{s}] {n} : {d}" + (f" -> {c}" if c else "") for n, s, d, c in r])
    section("Corps de William (corps.py)", [f"- {corps.ligne_etat(corps.bilan(naif))}"])
    lid = lieu_courant(h["lieu"])
    if lid:
        l = lieux.lire()[lid]
        ouv, raison = lieux.ouvert(l, naif)
        section(f"Lieu courant : {l['nom']}", [f"- {raison}", "- Ambiance (non utilisée récemment) : "
                                               + " / ".join(lieux.details(lid, naif, marquer=not args.simule))])
    persos = [p for p in lire_csv(ETAT / "personnages.csv") if p.get("statut") == "recurrent"]
    section("Personnages récurrents", [f"- {p['nom']} ({p['role']})" for p in persos] or ["- aucun pour l'instant"])
    # résumé et base
    lancer(OUTILS / "resume_etat.py", "--silencieux")
    lancer(OUTILS / "base.py", "construire", "--silencieux")
    print("\n(etat/resume.md et la base sorties/monde.sqlite sont à jour ; texte du dernier tour : etat/dernier-tour.md)")
    return 0


def enregistrer_tour(texte, message, h_avant, h_apres, numero):
    maintenant = dt.datetime.now()
    entete = (f"# Dernier tour montré au joueur\n\n> Tour n° {numero} ; horloge {h_avant:%d/%m/%Y %H:%M} -> {h_apres:%d/%m/%Y %H:%M} ; "
              f"enregistré le {maintenant:%d/%m/%Y %H:%M} (heure machine) par tour.py fin. Ce fichier est remplacé à chaque tour ; "
              f"l'historique complet est dans journal/tours/.\n\n")
    corps = "## Message du joueur\n\n" + ("\n".join("> " + x for x in message.strip().splitlines()) if message.strip() else "> (non enregistré)")
    corps += "\n\n## Texte envoyé au joueur\n\n" + texte.strip() + "\n"
    ecrire_texte(DERNIER_TOUR, entete + corps)
    fichier = JOURNAL / "tours" / f"{h_apres:%Y-%m-%d}.md"
    if not fichier.exists():
        ecrire_texte(fichier, f"# Tours joués le {date_fr(h_apres)} (texte exact envoyé au joueur et ses messages)\n\n")
    ajouter_texte(fichier, f"## Tour n° {numero} — {heure_fr(h_apres)} (horloge) — enregistré le {maintenant:%d/%m/%Y %H:%M}\n\n"
                  "### Message du joueur\n\n" + ("\n".join("> " + x for x in message.strip().splitlines()) if message.strip() else "> (non enregistré)")
                  + "\n\n### Texte envoyé au joueur\n\n" + texte.strip() + "\n\n")
    return fichier


def aleas_chaleur(avant, apres):
    """A34 (validé le 22/10/2026) : coup de chaleur ou déshydratation, 6 % chaque jour où le maximum de Séoul atteint 35 °C ; tiré une
    fois par jour, consigné ; l'événement est ajouté à l'agenda (non connu de William) et se joue à son heure."""
    import agenda
    import jet
    import meteo
    sortie = []
    jour, fin = avant["instant"].date(), apres["instant"].date()
    journal = lire_texte(RACINE / "memoire" / "tirages-aleas.md")
    while jour <= fin:
        ligne = meteo.lire("seoul").get(jour.isoformat()) if "seoul" in meteo.stations() else None
        etait_a_seoul = meteo.station_du_jour(jour) == "seoul"
        marque = f"A34 coup de chaleur du {jour:%d/%m/%Y}"
        if ligne and etait_a_seoul and float(ligne["tmax"]) >= 35 and marque not in journal:
            r = jet.tirer_libre(f"Aléa {marque} (maximum de {float(ligne['tmax']):.0f} °C ; 6 %)", 6)
            sortie.append(f"A34 {jour:%d/%m} : {'DÉCLENCHÉ' if r['oui'] else 'non'}")
            if r["oui"]:
                import random
                h = random.SystemRandom().choice(["12:40", "13:30", "14:15", "15:05", "16:20"])
                lignes = agenda.lire()
                lignes.append({"id": agenda.prochain_id(lignes), "date": jour.isoformat(), "heure": h, "lieu": "seoul", "qui": "William",
                               "quoi": "A34 : coup de chaleur ou déshydratation de William (malaise léger, une demi-journée perdue)",
                               "statut": "prevu", "connu": "non",
                               "note": f"NON CONNU DE WILLIAM avant l'heure · aléa A34, maximum de {float(ligne['tmax']):.0f} °C"})
                agenda.ecrire(lignes)
        jour += dt.timedelta(days=1)
    return sortie


def decalage_a_noter(avant, apres):
    """R1 : une arrivée avec au moins 3 h de décalage horaire est notée dans corps.py (trois nuits perturbées)."""
    try:
        ecart = abs((apres["instant"].utcoffset() - avant["instant"].utcoffset()).total_seconds()) / 3600
    except (AttributeError, TypeError):
        return None
    if avant["fuseau"] == apres["fuseau"] or ecart < 3:
        return None
    return ecart


def cmd_fin(args):
    import echeancier
    import horloge
    import meteo
    import relais
    avant = horloge.lire()
    cmd = [OUTILS / "horloge.py", "--regler", args.jusqua]
    if args.fuseau:
        cmd += ["--fuseau", args.fuseau]
    if args.lieu:
        cmd += ["--lieu", args.lieu]
    for a in args.attente or []:
        cmd += ["--attente", a]
    if not args.sans_tour:
        cmd += ["--tour", "+1"]
    r = lancer(*cmd)
    if r.returncode:
        sys.exit("Horloge non réglée : " + r.stderr.strip())
    apres = horloge.lire()
    print(f"Horloge : {date_fr(apres['instant'])}, {heure_fr(apres['instant'])} ; tour n° {apres['tour']}")
    deca = decalage_a_noter(avant, apres)
    if deca:
        lancer(OUTILS / "corps.py", "decalage", "--heures", f"{deca:g}", "--quand", f"{apres['instant']:%Y-%m-%d %H:%M}")
        print(f"  décalage horaire de {deca:g} h noté (corps.py : trois nuits perturbées)")
    faits = echeancier.realiser()
    for l in faits:
        print(f"  argent réalisé : {l['date']} {float(l['montant']):+.2f} € {l['libelle']}")
    ajouts = echeancier.prevoir(apres["instant"].date() + dt.timedelta(days=60))
    if ajouts:
        print(f"  {len(ajouts)} mouvement(s) prévu(s) ajouté(s) au grand livre (60 jours)")
    meteo.assurer(apres["instant"].date() + dt.timedelta(days=3))
    try:
        for x in aleas_chaleur(avant, apres):
            print(f"  {x}")
    except (SystemExit, KeyError, ValueError) as exc:
        print(f"  RELIRE aléa de chaleur : {exc}")
    depuis = derniere_heure_machine()
    import actions
    for ident, commande, sortie in actions.executer(apres["instant"]):
        print(f"  action {ident} exécutée : {commande} → {sortie}")
    try:
        import monde_vivant
        vie = monde_vivant.avancer(apres["instant"].date())
        notables = [x for x in vie if "initiative" in x or "aime le profil" in x or "T21d" in x or "inscrite" in x]
        if vie:
            print(f"  monde vivant : {len(vie)} événement(s) de vie tiré(s)" + (" ; " + " ; ".join(notables) if notables else ""))
    except SystemExit as exc:
        print(f"  RELIRE monde vivant : {exc}")
    try:  # 29/10/2026 (P37) : contacts tirés entre membres d'un même groupe ; William n'en voit que des traces
        import monde_social
        contacts = monde_social.avancer(apres["instant"].date())
        if contacts:
            print(f"  monde social : {len(contacts)} contact(s) notable(s) entre personnages (etat/monde-social.csv)")
    except SystemExit as exc:
        print(f"  RELIRE monde social : {exc}")
    try:  # 29/10/2026 (P38) : chaque lundi, T22 fait avancer (ou non) chaque front « temps »
        import lenteur
        for l in lenteur.semaine(apres["instant"].date()):
            print(f"  lenteur : {l}")
    except SystemExit as exc:
        print(f"  RELIRE lenteur : {exc}")
    try:  # 14/10/2026 : nouvelles du monde de la semaine, écrites une fois dès que l'horloge passe le lundi
        import actualites
        for l in actualites.assurer(apres["instant"].date()):
            print(f"  {l}")
    except SystemExit as exc:
        print(f"  RELIRE actualités : {exc}")
    for x in fiches_auto(avant, apres):
        print(f"  {x}")
    for note in args.fil or []:
        import fils
        ident, _, texte_fil = note.partition(":")
        fils.noter(ident.strip(), texte_fil.strip())
        print(f"  fil {ident.strip()} : note ajoutée")
    if args.texte or args.journal:
        fj = ecrire_journal(args, avant, apres, depuis)
        print(f"  journal : {fj.relative_to(RACINE).as_posix()} complété")
    try:  # téléphone de William régénéré à chaque tour (CLAUDE.md §14) ; Claude le republie au même endroit
        import telephone
        chemin_tel, _ = telephone.construire()
        print(f"  téléphone : {chemin_tel.relative_to(RACINE).as_posix()} régénéré (à republier : outil Artifact, même adresse)")
        for l in telephone.diff_publie()[:12]:
            print(f"    {l}")
    except SystemExit as exc:
        print(f"  RELIRE téléphone : page non régénérée ({exc})")
    if args.texte:
        texte = lire_texte(args.texte)
        message = lire_texte(args.joueur) if args.joueur else (args.message or "")
        f = enregistrer_tour(texte, message, avant["instant"], apres["instant"], apres["tour"])
        print(f"Texte du tour enregistré : etat/dernier-tour.md et {f.relative_to(RACINE).as_posix()}")
        r = lancer(OUTILS / "chasse_tics.py", "--texte", args.texte)
        avert = [l for l in r.stdout.splitlines() if l.strip().startswith(("TIC", "CASCADE", "RÉPÉTITION"))]
        for l in avert:
            print("  RELIRE (tic) :", l.strip())
        r2 = lancer(OUTILS / "verifier_texte_joueur.py", "--texte", args.texte,
                    "--avance-heures", f"{(apres['instant'] - avant['instant']).total_seconds() / 3600:.1f}")
        for l in r2.stdout.splitlines():
            if l.strip().startswith("RELIRE (texte joueur)"):
                print(" ", l.strip())
    else:
        print("(pas de --texte : le texte du tour n'est pas enregistré ; le prochain agent ne le verra pas)")
    if args.resume:
        entree, code_m = point_de_reprise(args.resume, apres)
        print("  §9 : entrée ajoutée en tête" + (" (RELIRE la synchronisation des fichiers maîtres)" if code_m else ""))
    lancer(OUTILS / "resume_etat.py", "--silencieux")
    lancer(OUTILS / "base.py", "construire", "--silencieux")
    relais.ecrire_note(relais.agent_nom(args.agent))
    r = lancer(OUTILS / "controle_coherence.py")
    lignes = [l for l in r.stdout.splitlines() if "ERREUR" in l or l.startswith("RÉSULTAT")]
    for l in lignes:
        print(l)
    code = 1 if r.returncode else 0
    if args.enregistrer:
        code |= enregistrer_git(f"tour n° {apres['tour']} : {date_fr(apres['instant'])} {heure_fr(apres['instant'])} "
                                f"({(args.resume or apres['lieu'])[:140]})", args.co_auteur)
    if args.commit:
        sys.argv = ["relais.py"]
        r2 = lancer(OUTILS / "relais.py", "sortie", "--agent", relais.agent_nom(args.agent), "--commit", args.commit,
                    *(["--co-auteur", args.co_auteur] if args.co_auteur else []), *(["--fusionner"] if args.fusionner else []),
                    silencieux=False)
        code |= r2.returncode
    return code


# ---------------------------------------------------------------- automatisation de la fin de tour (14/10/2026)
ORDINAUX = ["premier", "deuxième", "troisième", "quatrième", "cinquième", "sixième", "septième", "huitième", "neuvième", "dixième",
            "onzième", "douzième", "treizième", "quatorzième", "quinzième", "seizième", "dix-septième", "dix-huitième", "dix-neuvième",
            "vingtième"]


def numero_jour(jour):
    import json
    try:
        depart = dt.date.fromisoformat(json.loads(lire_texte(ETAT / "univers.json") or "{}")["depart"][:10])
    except (KeyError, ValueError):
        depart = dt.date(2040, 7, 14)
    n = (jour - depart).days + 1
    return ORDINAUX[n - 1] if 1 <= n <= len(ORDINAUX) else f"{n}e"


def fichier_journal(jour):
    f = JOURNAL / f"{jour:%Y-%m-%d}.md"
    if not f.exists():
        import json
        u_num = json.loads(lire_texte(ETAT / "univers.json") or "{}").get("univers", 3)
        ecrire_texte(f, f"# {date_fr(jour).capitalize()} — univers {u_num}, {numero_jour(jour)} jour\n\n")
    return f


def eur(x, signe=False):
    t = f"{x:+,.2f}" if signe else f"{x:,.2f}"
    return t.replace(",", " ").replace(".", ",") + " €"


def heure_courte(t):
    return f"{t:%H}h{t:%M}"


def derniere_heure_machine():
    """Heure machine du tour précédent (en-tête de etat/dernier-tour.md), pour retrouver les tirages faits depuis."""
    import re
    m = re.search(r"enregistré le (\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2})", lire_texte(DERNIER_TOUR))
    if not m:
        return None
    j, mo, a, h, mi = (int(x) for x in m.groups())
    return dt.datetime(a, mo, j, h, mi)


def tirages_depuis(depuis):
    """Résumé compact des tirages consignés depuis l'heure machine `depuis` (hors journées de masse du monde vivant)."""
    import json
    f = RACINE / "memoire" / "tirages.jsonl"
    if not f.exists() or depuis is None:
        return []
    res = []
    for l in f.read_text(encoding="utf-8").splitlines():
        try:
            o = json.loads(l)
        except ValueError:
            continue
        if o.get("simule") or dt.datetime.fromisoformat(o["enregistre"]) < depuis:
            continue
        lib = o.get("libelle", "")
        if lib.startswith(("Vie de ", "Contenu (")):
            continue
        qui = (o.get("pour") or "").split(" ")[0]
        if o.get("mode") == "table":
            if o.get("table") == "T14" and o.get("issue") == "aucune":
                continue
            res.append(f"{o['table']}{(' ' + qui) if qui else ''} → {o['issue']} ({str(o.get('jet', '')).replace('.', ',')})")
        elif o.get("mode") == "libre":
            res.append(f"jet{(' ' + qui) if qui else ''} « {lib[:60]} » → {o['issue']} ({str(o.get('jet', '')).replace('.', ',')})")
        elif o.get("mode") == "procedure":
            res.append(f"procédure{(' ' + qui) if qui else ''} : {o.get('valeur', '')}")
    return res


def ecrire_journal(args, avant, apres, depuis):
    """Lignes du tour dans journal/AAAA-MM-JJ.md : les lignes données (--journal), les tirages du tour, l'attente."""
    t0, t1 = avant["instant"], apres["instant"]
    f = fichier_journal(t1.date())
    lignes = list(args.journal or [])
    debut = heure_courte(t0) if t0.date() == t1.date() else "00h00"
    tete = f"- **{debut}-{heure_courte(t1)}** (tour n° {apres['tour']}) : "
    texte = tete + (lignes[0] if lignes else "voir le texte exact du tour (journal/tours/).") + "\n"
    for l in lignes[1:]:
        texte += f"- {l}\n"
    tir = tirages_depuis(depuis)
    if tir:
        texte += "- Tirages du tour : " + " ; ".join(tir) + ".\n"
    if apres["attentes"]:
        texte += f"- Tour en cours à {heure_courte(t1)}, en attente de William : " + " ; ".join(f"**{a}**" for a in apres["attentes"]) + ".\n"
    ajouter_texte(f, texte)
    return f


def fiches_auto(avant, apres):
    """Jour clos (l'horloge a passé minuit) : fiche courte générée d'après les données si le journal du jour n'en a pas ;
    fiche complète (données) si le rituel est dû. Le moteur peut les compléter ; elles ne manquent plus jamais."""
    import grand_livre as gl
    import rituels
    j0, j1 = avant["instant"].date(), apres["instant"].date()
    jour = j0
    sortie = []
    while jour < j1:
        f = fichier_journal(jour)
        if "Fiche courte du" not in lire_texte(f):
            debut = gl.soldes(dt.datetime.combine(jour, dt.time(0, 0)))
            fin = gl.soldes(dt.datetime.combine(jour, dt.time(23, 59)))
            delta = fin["courant"] - debut["courant"]
            msgs = [m for m in lire_csv(ETAT / "rencontres-messages.csv") if m["date"] == jour.isoformat()]
            import base
            wa = [m for m in base.lire_messages() if m["date"] == jour.isoformat()]
            env = sum(1 for m in msgs if m["auteur"] == "william") + sum(1 for m in wa if m["auteur"] == "William")
            rec = len(msgs) + len(wa) - env
            import agenda
            faits = [l for l in agenda.lire() if l["statut"] == "fait" and l["date"] == jour.isoformat()]
            sommeil = [c for c in lire_csv(ETAT / "corps.csv") if c["date"] == (jour + dt.timedelta(days=1)).isoformat() and c["type"] == "sommeil"]
            texte = (f"\n**Fiche courte du {date_fr(jour)}** (générée par tour.py d'après les données) : messages envoyés {env}, reçus {rec} ; "
                     f"échéances jouées {len(faits)} ; argent : courant {eur(fin['courant'])} ({eur(delta, signe=True)})"
                     + (f" ; nuit suivante : {float(sommeil[0]['valeur']):.1f} h".replace(".", ",") if sommeil else "") + ".\n")
            ajouter_texte(f, texte)
            sortie.append(f"fiche courte du {jour:%d/%m} générée")
        jour += dt.timedelta(days=1)
    if j1 > j0:
        dus = [x for x in rituels.bilan(apres["instant"]) if x[0] == "fiche_complete" and ("DÛ" in x[1].upper() or "RETARD" in x[1].upper())]
        if dus:
            import monde_vivant
            s = gl.soldes(apres["instant"].replace(tzinfo=None))
            liens = []
            ech, fixes = monde_vivant.derniers_echanges(), monde_vivant.liens_fixes()
            for p in monde_vivant.personnages():
                e, c = monde_vivant.etat_lien(p, j1, ech, fixes)
                if e not in ("aucun",):
                    liens.append(f"{p['nom']} ({e})")
            import agenda
            prochains = [agenda.afficher(l, apres["fuseau"]).split(" | ", 1)[-1].split(" [")[0][:90]
                         for l in sorted(agenda.lire(), key=agenda.instant)
                         if l["statut"] in ("prevu", "latent") and l["connu"] == "oui" and agenda.instant(l) >= apres["instant"]][:6]
            f = fichier_journal(j1 - dt.timedelta(days=1))
            ajouter_texte(f, f"\n**Fiche complète du {date_fr(j1 - dt.timedelta(days=1))}** (générée par tour.py d'après les données) :\n"
                             f"- *Finances* : courant {eur(s['courant'])} ; épargne {eur(s['projet'])} ; ETF {eur(s['etf'])} ; prêt {eur(s['pret'])}.\n"
                             + f"- *Relations* : {', '.join(liens) or 'aucun lien actif'}.\n"
                             + f"- *Calendrier connu* : {' ; '.join(prochains) or 'rien'}.\n")
            sortie.append("fiche complète générée (données)")
    return sortie


def point_de_reprise(resume, apres):
    """Entrée du §9 de CLAUDE.md, en tête ; archivage au-delà de 12 entrées ; fichiers maîtres synchronisés."""
    t = apres["instant"]
    zone = "" if apres["fuseau"] == "luxembourg" else f" (heure de {apres['fuseau'].capitalize()})"
    attente = " ; ".join(f"**{a}**" for a in apres["attentes"]) or "**sa suite**"
    entree = (f"**{date_fr(t).capitalize()}, {heure_fr(t)}{zone} — {apres['lieu']} : tour n° {apres['tour']} joué ({resume.strip().rstrip('.')}) ; "
              f"en attente : {attente}.**")
    f = RACINE / "CLAUDE.md"
    lignes = lire_texte(f).split("\n")
    d = next(i for i, l in enumerate(lignes) if l.startswith("## 9."))
    fin = next(i for i, l in enumerate(lignes) if l.startswith("## 10."))
    premiere = next((i for i in range(d + 1, fin) if lignes[i].startswith("**") and not lignes[i].startswith("**(Compression")), None)
    if premiere is None:
        premiere = fin - 1
    lignes.insert(premiere, entree)
    ecrire_texte(f, "\n".join(lignes))
    nb = sum(1 for i in range(d + 1, fin + 1) if lignes[i].startswith("**") and not lignes[i].startswith("**(Compression"))
    if nb > 12:
        lancer(OUTILS / "archiver_point_de_reprise.py", "--garder", "8", "--ecrire")
    r = lancer(OUTILS / "maitres.py", "synchroniser", "--depuis", "CLAUDE.md")
    return entree, r.returncode


def enregistrer_git(message, co_auteur):
    """Commit (tout) et fusion en avance rapide dans la branche principale, sans libérer le verrou (enregistrement à chaque tour)."""
    import relais
    from commun import git
    git("add", "-A")
    msg = message + (f"\n\nCo-Authored-By: {co_auteur}" if co_auteur else "")
    r = subprocess.run(["git", "commit", "-q", "-m", msg], cwd=str(RACINE), capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("  enregistrement :", (r.stdout.strip() or r.stderr.strip() or "commit fait").splitlines()[0][:120])
    return relais.fusionner()


def cmd_apercu(args):
    import agenda
    import calendrier_2040 as cal
    import echeancier
    import fronts
    import grand_livre as gl
    import horloge
    import meteo
    h = horloge.lire()
    t = h["instant"]
    d, hh = args.jusqua.split()
    fin = agenda.fuseaux.analyser_instant(d, hh, h["fuseau"])
    print(f"# Aperçu de l'avance rapide : du {date_fr(t)} {heure_fr(t)} au {date_fr(fin)} {heure_fr(fin)}")
    print("(Le moteur narre le routinier cohérent avec les intentions déclarées de William et S'ARRÊTE à la première vraie "
          "décision ou au premier événement qui demande une réaction : règle 13.)")
    meteo.assurer(fin.date() + dt.timedelta(days=1))
    echeancier.prevoir(fin.date() + dt.timedelta(days=60), simule=True)
    tirages = lire_texte(RACINE / "memoire" / "tirages-aleas.md")
    jour = t.date()
    while jour <= fin.date():
        v = meteo.lire()[jour.isoformat()]
        lev, cou = cal.soleil(jour, meteo.lieu_affichage())
        print(f"\n### {date_fr(jour)} — {v['description']} ; soleil {lev:%H:%M}-{cou:%H:%M}")
        for pays in ("fr", "lu"):
            for dd, nom, _ in cal.fetes(jour.year, pays):
                if dd == jour:
                    print(f"- férié {pays.upper()} : {nom}")
        for l in sorted(agenda.lire(), key=agenda.instant):
            i = agenda.instant(l)
            if l["statut"] in ("prevu", "latent") and i.date() == jour and t <= i <= fin:
                print(f"- {'ARRÊT POSSIBLE : ' if l['connu'] == 'oui' else ''}{agenda.afficher(l, h['fuseau'])}")
        for l in gl.lire():
            if l["type"] == "prevu" and l["date"] == jour.isoformat():
                print(f"- argent : {float(l['montant']):+.2f} € {l['libelle']}")
        for ligne in tirages.splitlines():
            if "DÉCLENCHÉ" in ligne and f"{jour:%d/%m}" in ligne:
                print(f"- ALÉA TIRÉ (à jouer ce jour-là) : {ligne.strip()[:160]}")
        for e in cal.lire_donnees("evenements.csv"):
            if e["debut"] <= jour.isoformat() <= e["fin"]:
                print(f"- événement : {e['lieu']} : {e['evenement'][:110]}")
        jour += dt.timedelta(days=1)
    for x in fronts.dus():
        print(f"- FRONT : {x}")
    print("\nAvant d'écrire : tour du monde de chaque jour clos (tour_du_monde.py), fiches courtes, et revue si un lundi est traversé.")
    return 0


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("debut")
    p.add_argument("--jusqua")
    p.add_argument("--simule", action="store_true", help="ne marque pas les détails d'ambiance comme utilisés")
    p.set_defaults(f=cmd_debut)
    p = sp.add_parser("fin")
    p.add_argument("--jusqua", required=True, help="nouvelle heure de l'horloge, « AAAA-MM-JJ HH:MM »")
    p.add_argument("--fuseau")
    p.add_argument("--lieu")
    p.add_argument("--attente", action="append")
    p.add_argument("--texte", help="fichier contenant le texte EXACT envoyé au joueur")
    p.add_argument("--joueur", help="fichier contenant le message du joueur (sinon --message)")
    p.add_argument("--message", help="message du joueur (texte)")
    p.add_argument("--sans-tour", action="store_true", help="n'avance pas le compteur de tours (correction, réglage)")
    p.add_argument("--agent")
    p.add_argument("--commit")
    p.add_argument("--co-auteur")
    p.add_argument("--fusionner", action="store_true")
    p.add_argument("--journal", action="append", help="ligne du journal du jour (la première porte l'heure et le numéro du tour)")
    p.add_argument("--fil", action="append", help="note d'un fil ouvert : « 4: texte »")
    p.add_argument("--resume", help="résumé d'une phrase : entrée du §9 de CLAUDE.md (archivage et synchronisation compris)")
    p.add_argument("--enregistrer", action="store_true", help="commit et fusion en avance rapide, sans libérer le verrou")
    p.set_defaults(f=cmd_fin)
    p = sp.add_parser("apercu")
    p.add_argument("--jusqua", required=True)
    p.set_defaults(f=cmd_apercu)
    args = ap.parse_args()
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())
