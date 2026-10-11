"""RELAIS ENTRE AGENTS (créé le 11/10/2026 à la demande de l'utilisateur : « que la transition se fasse de façon 100 % fluide, sans
perdre le moindre outil, le moindre contexte », quel que soit l'agent : Claude Code, Gemini CLI / Antigravity, Codex…).

    python outils/relais.py entree                 # PREMIÈRE COMMANDE de toute session : briefing complet + contrôles + verrou
    python outils/relais.py entree --court         # briefing compact, sans verrou (crochet de démarrage de Claude Code)
    python outils/relais.py sortie --note "…"      # avant de passer la main : contrôles, note de relais, journal des sessions
    python outils/relais.py sortie --commit "message" --fusionner   # + commit et fusion en avance rapide dans master
    python outils/relais.py verifier               # le dispositif de relais est-il complet ?
    python outils/relais.py git                    # worktrees, branches non fusionnées, avance/retard sur master
    python outils/relais.py verrou | liberer       # qui joue en ce moment (verrou partagé par tous les worktrees)

Ce que l'entrée garantit à un agent qui ne connaît rien :
1. **Sessions parallèles** : liste des worktrees et des branches qui ont des commits absents de master ou des fichiers non
   enregistrés (incident de l'univers 1 : trois chronologies divergentes) ; verrou partagé (dossier .git commun) : qui joue ?
2. **Contexte** : horloge, lieu, attentes, numéro de tour, TEXTE EXACT du dernier tour montré au joueur et son dernier message
   (`etat/dernier-tour.md`), échéances des 24 h (cachées comprises, signalées), rituels du moteur dus, notes de passation
   (`etat/relais-notes.md`), préférences de l'utilisateur (`memoire/preferences-utilisateur.md`).
3. **Routine** : les deux commandes de tour (`tour.py debut` / `tour.py fin`) et les fichiers à lire.
La sortie écrit `etat/relais.md` (la même note, lisible sans Python) et `memoire/sessions.csv` (journal des sessions).
"""
import argparse
import datetime as dt
import json
import os
import platform
import re
import subprocess
import sys

from commun import (ETAT, MEMOIRE, OUTILS, RACINE, ajouter_texte, date_fr, dossier_git_commun, ecrire_csv, ecrire_texte, git,
                    heure_fr, lire_csv, lire_texte, utf8)

NOTE = ETAT / "relais.md"
NOTES_MANUELLES = ETAT / "relais-notes.md"
DERNIER_TOUR = ETAT / "dernier-tour.md"
PREFERENCES = MEMOIRE / "preferences-utilisateur.md"
SESSIONS = MEMOIRE / "sessions.csv"
CONFIG = ETAT / "relais-config.json"
COL_SESSIONS = ["debut", "fin", "agent", "branche", "worktree", "horloge_debut", "horloge_fin", "tour_debut", "tour_fin",
                "commit", "note"]
VERROU_NOM = "simulation-verrou.json"
VERROU_DUREE_H = 12


# ---------------------------------------------------------------- configuration
def config():
    try:
        return json.loads(lire_texte(CONFIG) or "{}")
    except json.JSONDecodeError:
        return {}


def agent_nom(args_agent=None):
    return args_agent or os.environ.get("SIMULATION_AGENT") or config().get("agent_par_defaut", "agent inconnu")


# ---------------------------------------------------------------- git
def worktrees():
    """[{chemin, branche, head}] (le premier est le dossier principal)."""
    sortie = git("worktree", "list", "--porcelain")
    if not sortie:
        return []
    res, cur = [], {}
    for l in sortie.splitlines():
        if l.startswith("worktree "):
            if cur:
                res.append(cur)
            cur = {"chemin": l[9:].strip(), "branche": "", "head": ""}
        elif l.startswith("HEAD "):
            cur["head"] = l[5:].strip()
        elif l.startswith("branch "):
            cur["branche"] = l[7:].strip().replace("refs/heads/", "")
        elif l.strip() == "detached":
            cur["branche"] = "(HEAD détachée)"
    if cur:
        res.append(cur)
    return res


def branche_principale():
    for b in ("master", "main"):
        if git("rev-parse", "--verify", "--quiet", b):
            return b
    return None


def etat_git():
    """Résumé de l'état git, avec les alertes de sessions parallèles."""
    if not git("rev-parse", "--is-inside-work-tree"):
        return {"git": False, "alertes": ["pas de dépôt git ici : aucun contrôle de sessions parallèles possible"], "lignes": []}
    archives = config().get("archives", {})
    principale = branche_principale()
    courante = git("rev-parse", "--abbrev-ref", "HEAD") or "?"
    ici = str(RACINE.resolve()).replace("\\", "/").lower()
    alertes, lignes = [], []
    avance = retard = 0
    if principale and courante not in (principale, "HEAD"):
        compte = git("rev-list", "--left-right", "--count", f"{principale}...HEAD")
        if compte:
            retard, avance = (int(x) for x in compte.split())
        if retard and not avance:
            alertes.append(f"la branche courante a {retard} commit(s) de retard sur {principale} : la mettre à jour AVANT de jouer "
                           f"(git merge --ff-only {principale}, ou l'outil de synchronisation de l'application)")
        elif retard and avance:
            alertes.append(f"la branche courante et {principale} ont DIVERGÉ ({avance} commit(s) d'avance, {retard} de retard) : "
                           "fusionner avec soin avant de jouer (une autre session a avancé la partie)")
    lignes.append(f"branche courante : {courante} ; {principale or '?'} : {git('rev-parse', '--short', principale) if principale else '?'}"
                  f" ; avance {avance}, retard {retard}")
    for w in worktrees():
        chemin = w["chemin"].replace("\\", "/")
        nom = chemin.rstrip("/").split("/")[-1]
        est_ici = chemin.lower() == ici
        statut = git("-C", w["chemin"], "status", "--porcelain", defaut="") or ""
        sales = len([l for l in statut.splitlines() if l.strip()])
        en_avance = 0
        if principale and w["branche"] and not w["branche"].startswith("(") and w["branche"] != principale:
            n = git("rev-list", "--count", f"{principale}..{w['branche']}")
            en_avance = int(n) if n and n.isdigit() else 0
        raison = archives.get(nom) or archives.get(w["branche"])
        marque = " (ICI)" if est_ici else ""
        lignes.append(f"worktree {nom}{marque} : branche {w['branche'] or '?'} ; {en_avance} commit(s) absents de master ; "
                      f"{sales} fichier(s) modifié(s)" + (f" ; ARCHIVÉ : {raison}" if raison else ""))
        if est_ici or raison:
            continue
        if en_avance:
            alertes.append(f"le worktree {nom} (branche {w['branche']}) a {en_avance} commit(s) absents de master : une autre "
                           "session a peut-être joué ; fusionner ou archiver AVANT de jouer")
        if sales:
            alertes.append(f"le worktree {nom} a {sales} fichier(s) modifié(s) non enregistrés : session interrompue ? "
                           "Vérifier avant de jouer (ne rien supprimer)")
    autres = git("branch", "--no-merged", principale, defaut="") if principale else ""
    for b in (autres or "").splitlines():
        b = b.strip().lstrip("*+ ").strip()
        if not b or b == courante or b in archives:
            continue
        if any(b == w["branche"] for w in worktrees()):
            continue  # déjà signalé avec son worktree
        alertes.append(f"la branche {b} n'est pas fusionnée dans {principale} (et n'a pas de worktree) : à examiner ou à archiver "
                       "(etat/relais-config.json)")
    return {"git": True, "principale": principale, "courante": courante, "avance": avance, "retard": retard,
            "alertes": alertes, "lignes": lignes}


# ---------------------------------------------------------------- verrou
def chemin_verrou():
    d = dossier_git_commun()
    return (d / VERROU_NOM) if d else (ETAT / ".verrou-session.json")


def lire_verrou():
    p = chemin_verrou()
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def poser_verrou(agent):
    v = {"agent": agent, "worktree": str(RACINE), "branche": git("rev-parse", "--abbrev-ref", "HEAD") or "?",
         "depuis": dt.datetime.now().isoformat(timespec="minutes"), "machine": platform.node()}
    chemin_verrou().write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    return v


def alerte_verrou():
    v = lire_verrou()
    if not v:
        return None
    try:
        age_h = (dt.datetime.now() - dt.datetime.fromisoformat(v["depuis"])).total_seconds() / 3600
    except (KeyError, ValueError):
        age_h = 0
    if os.path.normcase(v.get("worktree", "")) == os.path.normcase(str(RACINE)):
        return None
    if age_h > VERROU_DUREE_H:
        return f"verrou ancien ({age_h:.0f} h) laissé par {v.get('agent')} dans {v.get('worktree')} : session sans sortie propre ?"
    return (f"SESSION PARALLÈLE POSSIBLE : {v.get('agent')} joue depuis {v.get('depuis')} dans {v.get('worktree')} "
            f"(branche {v.get('branche')}). Demander à l'utilisateur avant de jouer.")


# ---------------------------------------------------------------- contenu du briefing
def bloc(titre, lignes):
    return [f"## {titre}"] + (lignes or ["- rien"]) + [""]


def extrait_dernier_tour(max_lignes=40):
    t = lire_texte(DERNIER_TOUR)
    if not t.strip():
        return ["- aucun tour enregistré dans etat/dernier-tour.md (premier tour, ou tour joué avant le 11/10/2026)"]
    lignes = [l for l in t.splitlines()]
    if len(lignes) > max_lignes:
        lignes = lignes[:max_lignes] + [f"… (suite dans etat/dernier-tour.md, {len(t.splitlines())} lignes)"]
    return lignes


def sections_fils():
    """Lignes du tableau A de etat/fils-ouverts.md (décisions en attente de William)."""
    t = lire_texte(ETAT / "fils-ouverts.md")
    m = re.search(r"## A\.[^\n]*\n(.*?)(?=\n## )", t, re.S)
    if not m:
        return []
    return [l for l in m.group(1).splitlines() if l.startswith("|") and not l.startswith("|---") and "Sujet" not in l][:10]


def briefing(court=False, agent="?"):
    sys.path.insert(0, str(OUTILS))
    L = []
    maintenant = dt.datetime.now()
    L.append(f"# Relais de la simulation — briefing généré le {maintenant:%d/%m/%Y %H:%M} (heure machine) pour {agent}")
    L.append("")
    # 1. git et verrou
    g = etat_git()
    alertes = list(g["alertes"])
    av = alerte_verrou()
    if av:
        alertes.insert(0, av)
    L += bloc("ALERTES (à régler avant de jouer)" if alertes else "Alertes", [f"- ⚠ {a}" for a in alertes] or ["- aucune"])
    # 2. horloge
    try:
        import horloge
        h = horloge.lire()
        t = h["instant"]
        L += bloc("Où en est la partie", [
            f"- Horloge : {date_fr(t)}, {heure_fr(t)} ({h['fuseau']}) ; tour n° {h.get('tour', 0)}",
            f"- Lieu de William : {h['lieu']}",
            *[f"- En attente de William : {a}" for a in h["attentes"]],
        ])
    except SystemExit as e:
        L += bloc("Où en est la partie", [f"- HORLOGE ILLISIBLE : {e}"])
        t = None
    # 3. dernier tour
    L += bloc("Dernier tour montré au joueur (etat/dernier-tour.md)", extrait_dernier_tour(18 if court else 60))
    # 4. échéances et rituels
    if t is not None:
        try:
            import agenda
            fin = t + dt.timedelta(hours=24)
            dus = [l for l in sorted(agenda.lire(), key=agenda.instant)
                   if l["statut"] in ("prevu", "latent") and t <= agenda.instant(l) <= fin]
            retards = [l for l in agenda.lire() if l["statut"] == "prevu" and agenda.instant(l) < t]
            lignes = [f"- {agenda.afficher(l, h['fuseau'])}" for l in retards + dus]
            if retards:
                lignes.insert(0, f"- ⚠ {len(retards)} échéance(s) échue(s) non close(s) (règle 14)")
            L += bloc("Échéances : retards et prochaines 24 h (les lignes NON CONNU sont pour le moteur seul)", lignes)
        except Exception as e:  # noqa: BLE001
            L += bloc("Échéances", [f"- agenda illisible : {e}"])
        try:
            import rituels
            r = [x for x in rituels.bilan(t) if x[1] != "sans objet"]
            L += bloc("Rituels du moteur dus (rituels.py)", [f"- [{s}] {n} : {d}" + (f" -> {c}" if c else "") for n, s, d, c in r])
        except Exception as e:  # noqa: BLE001
            L += bloc("Rituels du moteur", [f"- rituels illisibles : {e}"])
    # 5. décisions en attente et notes de passation
    L += bloc("Décisions en attente de William (etat/fils-ouverts.md, A)", sections_fils())
    notes = [l for l in lire_texte(NOTES_MANUELLES).splitlines() if l.strip() and not l.startswith(("#", ">"))]
    L += bloc("Notes de passation (etat/relais-notes.md)", notes[: (15 if court else 80)])
    # 6. préférences et routine
    L += bloc("Préférences de l'utilisateur (memoire/preferences-utilisateur.md : à lire en entier)", [
        "- Format du tour : récit fluide, puis « Réponses attendues », « À faire », « Quêtes secondaires », « Que veux-tu faire ? ».",
        "- Aucune explication, aucun conseil, aucun jet ni source montrés ; pas de morale ; William décide seul (règles 6, 13, 16).",
        "- « 📌 Vraie vie : … » = hors fiction ; il dicte : interpréter les erreurs de dictée et le signaler en une ligne.",
        "- Il joue parfois depuis son téléphone : lui envoyer les fichiers demandés dans la conversation.",
    ])
    L += bloc("Routine", [
        "- Lire le fichier maître (CLAUDE.md, GEMINI.md ou AGENTS.md), puis memoire/preferences-utilisateur.md et outils/LISEZMOI.md.",
        "- Début de tour : `python outils/tour.py debut` (résumé, échéances, rituels, météo, corps, relais).",
        "- Fin de tour : `python outils/tour.py fin --jusqua \"AAAA-MM-JJ HH:MM\" --lieu \"…\" --attente \"…\" --texte <brouillon>`.",
        "- Avant de passer la main : `python outils/relais.py sortie --note \"…\" --commit \"…\" --fusionner`.",
    ])
    if not court:
        L += bloc("État git détaillé", [f"- {x}" for x in g["lignes"]])
    return "\n".join(L), alertes


# ---------------------------------------------------------------- journal des sessions
def noter_session_debut(agent):
    sys.path.insert(0, str(OUTILS))
    import horloge
    h = horloge.lire()
    lignes = lire_csv(SESSIONS)
    lignes.append({"debut": dt.datetime.now().isoformat(timespec="minutes"), "fin": "", "agent": agent,
                   "branche": git("rev-parse", "--abbrev-ref", "HEAD") or "?", "worktree": RACINE.name,
                   "horloge_debut": f"{h['instant']:%Y-%m-%d %H:%M}", "horloge_fin": "", "tour_debut": h.get("tour", 0),
                   "tour_fin": "", "commit": git("rev-parse", "--short", "HEAD") or "", "note": ""})
    ecrire_csv(SESSIONS, lignes, COL_SESSIONS)


def noter_session_fin(agent, note):
    sys.path.insert(0, str(OUTILS))
    import horloge
    h = horloge.lire()
    lignes = lire_csv(SESSIONS)
    ouvertes = [l for l in lignes if not l.get("fin") and l.get("worktree") == RACINE.name]
    cible = ouvertes[-1] if ouvertes else None
    if cible is None:
        cible = {"debut": "", "agent": agent, "branche": git("rev-parse", "--abbrev-ref", "HEAD") or "?",
                 "worktree": RACINE.name, "horloge_debut": "", "tour_debut": ""}
        lignes.append(cible)
    cible.update({"fin": dt.datetime.now().isoformat(timespec="minutes"), "horloge_fin": f"{h['instant']:%Y-%m-%d %H:%M}",
                  "tour_fin": h.get("tour", 0), "commit": git("rev-parse", "--short", "HEAD") or "", "note": note or ""})
    ecrire_csv(SESSIONS, lignes, COL_SESSIONS)


# ---------------------------------------------------------------- commandes
def cmd_entree(args):
    agent = agent_nom(args.agent)
    texte, alertes = briefing(court=args.court, agent=agent)
    print(texte)
    if not args.court and not args.sans_verrou:
        poser_verrou(agent)
        try:
            noter_session_debut(agent)
        except SystemExit:
            pass
        print(f"(Verrou posé pour {agent} ; session notée dans memoire/sessions.csv. En fin de session : python outils/relais.py sortie)")
    return 0


def ecrire_note(agent):
    texte, _ = briefing(court=False, agent=agent)
    entete = ("> Note de relais GÉNÉRÉE par `python outils/relais.py sortie` (ou `tour.py fin`) : ne pas éditer à la main. "
              "Les notes libres vont dans `etat/relais-notes.md`.\n\n")
    ecrire_texte(NOTE, entete + texte + "\n")


def cmd_sortie(args):
    agent = agent_nom(args.agent)
    sys.path.insert(0, str(OUTILS))
    code = 0
    if args.note:
        horodatage = dt.datetime.now().strftime("%d/%m/%Y %H:%M")
        ajouter_texte(NOTES_MANUELLES, f"- ({horodatage}, {agent}) {args.note}\n")
    r = subprocess.run([sys.executable, str(OUTILS / "controle_coherence.py")], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", cwd=str(RACINE))
    resultat = [l for l in r.stdout.splitlines() if l.startswith("RÉSULTAT")]
    print("Contrôle de cohérence :", resultat[0] if resultat else "(sortie illisible)")
    if r.returncode:
        print("  -> des erreurs restent : les corriger avant de passer la main si possible (voir controle_coherence.py).")
        code = 1
    subprocess.run([sys.executable, str(OUTILS / "resume_etat.py"), "--silencieux"], capture_output=True, cwd=str(RACINE))
    subprocess.run([sys.executable, str(OUTILS / "base.py"), "construire", "--silencieux"], capture_output=True, cwd=str(RACINE))
    ecrire_note(agent)
    print("Note de relais écrite : etat/relais.md")
    try:
        noter_session_fin(agent, args.note)
    except SystemExit:
        pass
    if args.commit:
        git("add", "-A")
        msg = args.commit + (f"\n\nCo-Authored-By: {args.co_auteur}" if args.co_auteur else "")
        res = subprocess.run(["git", "commit", "-m", msg], cwd=str(RACINE), capture_output=True, text=True, encoding="utf-8",
                             errors="replace")
        print("Commit :", (res.stdout.strip().splitlines() or ["rien à enregistrer"])[0])
    if args.fusionner:
        code |= fusionner()
    v = lire_verrou()
    if v and os.path.normcase(v.get("worktree", "")) == os.path.normcase(str(RACINE)):
        chemin_verrou().unlink(missing_ok=True)
        print("Verrou libéré.")
    return code


def fusionner():
    """Fusion en avance rapide de la branche courante dans la branche principale (autorisée par l'utilisateur, CLAUDE.md §10.B)."""
    principale = branche_principale()
    courante = git("rev-parse", "--abbrev-ref", "HEAD")
    ws = worktrees()
    if not principale or not courante or not ws:
        print("Fusion impossible : dépôt ou branche introuvable.")
        return 1
    if courante == principale:
        print(f"Déjà sur {principale} : rien à fusionner.")
        return 0
    dossier_principal = next((w["chemin"] for w in ws if w["branche"] == principale), None)
    if not dossier_principal:
        print(f"Aucun worktree n'a {principale} extraite : fusion à faire à la main.")
        return 1
    if git("-C", dossier_principal, "status", "--porcelain", defaut="x"):
        print(f"Le dossier principal ({dossier_principal}) a des modifications non enregistrées : fusion refusée (ne rien écraser).")
        return 1
    r = subprocess.run(["git", "-C", dossier_principal, "merge", "--ff-only", courante], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode:
        print(f"Fusion en avance rapide refusée ({principale} a avancé de son côté) : intégrer {principale} dans {courante} "
              f"(git merge {principale}), relancer les contrôles, puis refusionner.\n{r.stderr.strip()}")
        return 1
    print(f"{principale} avancé jusqu'à {git('rev-parse', '--short', 'HEAD')} (fusion en avance rapide depuis {courante}).")
    return 0


def cmd_verifier(args):
    sys.path.insert(0, str(OUTILS))
    import maitres
    erreurs, aver = [], []
    erreurs += maitres.verifier()
    for p, quoi in ((PREFERENCES, "préférences de l'utilisateur"), (OUTILS / "LISEZMOI.md", "index des outils"),
                    (ETAT / "univers.json", "constantes de l'univers"), (CONFIG, "configuration du relais")):
        if not p.exists():
            erreurs.append(f"{p.relative_to(RACINE)} absent ({quoi})")
    if not DERNIER_TOUR.exists():
        aver.append("etat/dernier-tour.md absent : le prochain agent ne verra pas le texte du dernier tour")
    g = etat_git()
    aver += g["alertes"]
    for e in erreurs:
        print("ERREUR", e)
    for a in aver:
        print("RELIRE", a)
    print("Relais :", "complet" if not erreurs else "incomplet", f"({len(aver)} avertissement(s))")
    return 1 if erreurs else 0


def cmd_git(args):
    g = etat_git()
    for l in g["lignes"]:
        print(l)
    for a in g["alertes"]:
        print("ALERTE", a)
    return 0


def cmd_verrou(args):
    v = lire_verrou()
    print(json.dumps(v, ensure_ascii=False, indent=1) if v else "Aucun verrou : personne n'est déclaré en train de jouer.")
    return 0


def cmd_liberer(args):
    chemin_verrou().unlink(missing_ok=True)
    print("Verrou supprimé.")
    return 0


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("entree")
    p.add_argument("--agent")
    p.add_argument("--court", action="store_true", help="briefing compact, sans verrou (crochet de démarrage)")
    p.add_argument("--sans-verrou", action="store_true")
    p.set_defaults(f=cmd_entree)
    p = sp.add_parser("sortie")
    p.add_argument("--agent")
    p.add_argument("--note", help="note de passation ajoutée à etat/relais-notes.md")
    p.add_argument("--commit", help="message de commit (git add -A puis commit)")
    p.add_argument("--co-auteur", help="ligne Co-Authored-By à ajouter au commit (ex. « Claude Opus 5.5 <noreply@anthropic.com> »)")
    p.add_argument("--fusionner", action="store_true", help="fusion en avance rapide dans master")
    p.set_defaults(f=cmd_sortie)
    for nom, f in (("verifier", cmd_verifier), ("git", cmd_git), ("verrou", cmd_verrou), ("liberer", cmd_liberer)):
        sp.add_parser(nom).set_defaults(f=f)
    args = ap.parse_args()
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())
