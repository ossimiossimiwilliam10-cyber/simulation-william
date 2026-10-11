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
Ce que l'orchestrateur ne fait PAS : écrire le journal, les WhatsApp, les fils ouverts, les fiches ; tirer les réactions
(jet.py --table) ; décider à la place de William. Ces étapes restent celles du §7 de CLAUDE.md.
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
    lev, cou = cal.soleil(jour, "audun")
    l_meteo = [f"- Vérité du jour : {v['description']} (type {v['type']})",
               f"- Maintenant : environ {meteo.temperature_a(v, naif):.0f} °C ; soleil levé à {lev:%H:%M}, couché à {cou:%H:%M}"]
    prev = [meteo.prevision(jour + dt.timedelta(days=i), jour) for i in (1, 2)]
    l_meteo.append("- Prévision vue par William : " + " ; ".join(
        f"{'demain' if p['echeance'] == 1 else 'après-demain'} {p['ciel']}, {p['tmin']}/{p['tmax']} °C, pluie {p['risque_pluie']} %"
        for p in prev))
    section("Météo (meteo.py)", l_meteo)
    # calendrier
    l_cal = []
    for pays in ("fr", "lu"):
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
    faits = echeancier.realiser()
    for l in faits:
        print(f"  argent réalisé : {l['date']} {float(l['montant']):+.2f} € {l['libelle']}")
    ajouts = echeancier.prevoir(apres["instant"].date() + dt.timedelta(days=60))
    if ajouts:
        print(f"  {len(ajouts)} mouvement(s) prévu(s) ajouté(s) au grand livre (60 jours)")
    meteo.assurer(apres["instant"].date() + dt.timedelta(days=3))
    if args.texte:
        texte = lire_texte(args.texte)
        message = lire_texte(args.joueur) if args.joueur else (args.message or "")
        f = enregistrer_tour(texte, message, avant["instant"], apres["instant"], apres["tour"])
        print(f"Texte du tour enregistré : etat/dernier-tour.md et {f.relative_to(RACINE).as_posix()}")
        r = lancer(OUTILS / "chasse_tics.py", "--texte", args.texte)
        avert = [l for l in r.stdout.splitlines() if l.strip().startswith(("TIC", "CASCADE", "RÉPÉTITION"))]
        for l in avert:
            print("  RELIRE (tic) :", l.strip())
    else:
        print("(pas de --texte : le texte du tour n'est pas enregistré ; le prochain agent ne le verra pas)")
    lancer(OUTILS / "resume_etat.py", "--silencieux")
    lancer(OUTILS / "base.py", "construire", "--silencieux")
    relais.ecrire_note(relais.agent_nom(args.agent))
    r = lancer(OUTILS / "controle_coherence.py")
    lignes = [l for l in r.stdout.splitlines() if "ERREUR" in l or l.startswith("RÉSULTAT")]
    for l in lignes:
        print(l)
    code = 1 if r.returncode else 0
    if args.commit:
        sys.argv = ["relais.py"]
        r2 = lancer(OUTILS / "relais.py", "sortie", "--agent", relais.agent_nom(args.agent), "--commit", args.commit,
                    *(["--co-auteur", args.co_auteur] if args.co_auteur else []), *(["--fusionner"] if args.fusionner else []),
                    silencieux=False)
        code |= r2.returncode
    return code


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
        lev, cou = cal.soleil(jour, "audun")
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
    p.set_defaults(f=cmd_fin)
    p = sp.add_parser("apercu")
    p.add_argument("--jusqua", required=True)
    p.set_defaults(f=cmd_apercu)
    args = ap.parse_args()
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())
