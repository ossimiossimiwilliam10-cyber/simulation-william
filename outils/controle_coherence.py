"""Contrôle de cohérence du dépôt de la simulation — À LANCER avant de clore un tour (checklist de CLAUDE.md §7).

    python outils/controle_coherence.py

Contrôles automatiques :
1. **Jours de la semaine** : toute mention « lundi 23/07 », « mer. 25/07 », « Dim. 29/07/2040 »… (jour + date JJ/MM)
   est vérifiée par calcul (année 2040 par défaut). Erreur = incohérence réelle dans l'état du monde.
2. **Fichiers maîtres** : `CLAUDE.md` et `GEMINI.md` doivent être identiques à la ligne 3 près.
3. **Expressions interdites** : formes déjà corrigées (« faute grave » à propos d'un CDD, « Net » dans les contrats…).
4. **PDF** : lance `verifier_pdf.py` (accents, texte extractible).
5. **Modèle de pouvoir** : tables de `etat/modele-pouvoir.md` (sommes, plafonds, modificateurs) et jets conformes à la règle 17.
6. **Données structurées** (installées le 09/08/2040) : horloge, agenda (`etat/agenda.csv`), grand livre (`etat/grand-livre.csv`),
   « qui sait quoi » (`etat/savoir.csv`) : fichiers lisibles et cohérents ; échéances échues non closes en avertissement.
7. **Chasse aux tics** (`outils/chasse_tics.py`) : avertissements non bloquants sur les trois derniers journaux.
8. **(11/10/2026)** Dates écrites en toutes lettres (« samedi 14 juillet 2040 », en-têtes de tour en majuscules) ; trois fichiers
   maîtres (CLAUDE.md, GEMINI.md, AGENTS.md : `outils/maitres.py`) ; colonnes de TOUS les CSV de `etat/` et `donnees/` ; cohérence
   croisée de la base de données (`outils/base.py verifier` : personnages, relations, savoir, météo, corps, échéancier, fronts,
   ordre du journal) ; rituels du moteur en retard (`outils/rituels.py`) ; dispositif de relais (`outils/relais.py verifier`).
   Les lignes qui commencent par « > » (citations du joueur, dictées) ne sont pas contrôlées pour les jours de la semaine.
Code de sortie 1 s'il y a au moins une erreur.
"""
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
JOURS = {"lun": 0, "mar": 1, "mer": 2, "jeu": 3, "ven": 4, "sam": 5, "dim": 6}
NOMS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOTIF = re.compile(
    r"\b(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche|lun\.?|mar\.|mer\.?|jeu\.?|ven\.?|sam\.?|dim\.?)\s+"
    r"(\d{1,2})/(\d{2})(?:/(\d{4}))?", re.IGNORECASE)
DOSSIERS = ["etat", "personnes", "journal", "memoire", "whatsapp", "serveur", "."]  # univers 1 : archives/univers-1 (non contrôlé)
MOIS_NOMS = {"janvier": 1, "février": 2, "fevrier": 2, "mars": 3, "avril": 4, "mai": 5, "juin": 6, "juillet": 7, "août": 8, "aout": 8,
             "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12, "decembre": 12}
MOTIF_LETTRES = re.compile(
    r"\b(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)\s+(1er|\d{1,2})\s+(" + "|".join(MOIS_NOMS) + r")(?:\s+(\d{4}))?",
    re.IGNORECASE)
EXCLUS = {".git", "outils", "__pycache__"}


def fichiers_md():
    vus = set()
    for d in DOSSIERS:
        base = RACINE / d
        if d == ".":
            candidats = [p for p in base.glob("*.md")]
        else:
            candidats = list(base.rglob("*.md"))
        for p in candidats:
            if any(x in p.parts for x in EXCLUS) or p in vus:
                continue
            vus.add(p)
            yield p


def controle_jours():
    erreurs, total = [], 0
    for p in fichiers_md():
        if any(x.startswith("conception-") for x in p.parts):
            continue  # notes de recherche du 11/10/2026 : dates réelles de 2026, pas des dates du monde
        for n, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if ligne.lstrip().startswith(">"):
                continue  # citation (message dicté du joueur, extrait) : pas un fait du moteur
            for m in MOTIF_LETTRES.finditer(ligne):
                jour_l, j_l, mois_l, annee_l = m.group(1).lower(), m.group(2).lower(), m.group(3).lower(), m.group(4)
                try:
                    d = dt.date(int(annee_l or 2040), MOIS_NOMS[mois_l], 1 if j_l == "1er" else int(j_l))
                except ValueError:
                    erreurs.append(f"{p.relative_to(RACINE)}:{n} date impossible « {m.group(0)} »")
                    continue
                total += 1
                if JOURS[jour_l[:3]] != d.weekday():
                    erreurs.append(f"{p.relative_to(RACINE)}:{n} « {m.group(0)} » : {d:%d/%m/%Y} est un {NOMS[d.weekday()]}")
            for m in MOTIF.finditer(ligne):
                jour, j, mois, annee = m.group(1).lower(), int(m.group(2)), int(m.group(3)), int(m.group(4) or 2040)
                try:
                    d = dt.date(annee, mois, j)
                except ValueError:
                    erreurs.append(f"{p.relative_to(RACINE)}:{n} date impossible « {m.group(0)} »")
                    continue
                total += 1
                attendu = d.weekday()
                lu = JOURS[jour[:3]]
                # « mar. » est ambigu avec « mars » mais le motif exige une date derrière : on le garde
                if lu != attendu:
                    erreurs.append(f"{p.relative_to(RACINE)}:{n} « {m.group(0)} » : {d:%d/%m/%Y} est un {NOMS[attendu]}")
    return erreurs, total


def controle_maitres():
    """CLAUDE.md, GEMINI.md et AGENTS.md identiques sauf la ligne 3 (outils/maitres.py)."""
    sys.path.insert(0, str(RACINE / "outils"))
    import maitres
    return maitres.verifier()


def controle_csv():
    """Toutes les lignes de chaque CSV de etat/ et donnees/ ont le nombre de colonnes de l'en-tête (un « ; » dans un champ décale
    tout : piège découvert le 11/10/2026)."""
    import csv
    erreurs, total = [], 0
    for base in (RACINE / "etat", RACINE / "donnees"):
        for p in sorted(base.rglob("*.csv")):
            with p.open(encoding="utf-8", newline="") as f:
                lignes = list(csv.reader(f, delimiter=";"))
            if not lignes:
                continue
            total += 1
            n = len(lignes[0])
            for i, l in enumerate(lignes[1:], 2):
                if l and len(l) != n:
                    erreurs.append(f"{p.relative_to(RACINE)}:{i} {len(l)} colonnes au lieu de {n} (un « ; » dans un champ ?)")
    return erreurs, total


def controle_base():
    """Cohérence croisée de la base reconstruite, rituels en retard, relais. Retourne (erreurs, avertissements)."""
    sys.path.insert(0, str(RACINE / "outils"))
    erreurs, aver = [], []
    try:
        import base
        e, a = base.verifier()
        erreurs += e
        aver += a
    except Exception as exc:  # noqa: BLE001
        erreurs.append(f"base de données : vérification impossible ({exc})")
    try:
        import rituels
        aver += [f"rituel {n} : {d}" for n, s, d, c in rituels.bilan() if s == "EN RETARD"]
    except Exception as exc:  # noqa: BLE001
        aver.append(f"rituels : bilan impossible ({exc})")
    try:
        import fronts
        aver += [f"front : {x}" for x in fronts.dus()]
    except Exception as exc:  # noqa: BLE001
        aver.append(f"fronts : lecture impossible ({exc})")
    try:  # prêts : capital restant dû calculé = calages du grand livre ; échéancier : comptes, contreparties, prêts (11/10/2026)
        import echeancier
        import prets
        import transports
        import voyages
        for module in (prets, echeancier, voyages, transports):
            e, a = module.verifier()
            erreurs += e
            aver += a
        import cartes  # cartes de William : types, jours de débit, opérations (12/10/2026)
        erreurs += cartes.verifier()
        import actualites  # 14/10/2026 : argent sur place, courses en ville, modèles de nouvelles
        import courses
        import devises
        for module in (devises, courses, actualites):
            erreurs += module.verifier()
    except Exception as exc:  # noqa: BLE001
        erreurs.append(f"prêts ou échéancier : vérification impossible ({exc})")
    for chemin, quoi in (("memoire/preferences-utilisateur.md", "préférences de l'utilisateur (relais)"),
                         ("etat/univers.json", "constantes de l'univers"), ("outils/LISEZMOI.md", "index des outils")):
        if not (RACINE / chemin).exists():
            erreurs.append(f"{chemin} absent ({quoi})")
    return erreurs, aver


INTERDITS = [
    (re.compile(r"faute grave[^.\n]{0,60}(CDD|rupture anticip)|(CDD|rupture anticip)[^.\n]{0,60}faute grave", re.I),
     "à propos d'un CDD, la loi dit « faute lourde » (art. 15.9)"),
    (re.compile(r"\bNet\b[^.\n]{0,20}FCFA\b"), "montant de contrat en « Net » (les salaires sont des bruts)"),
]


def controle_interdits():
    erreurs = []
    for p in fichiers_md():
        if p.name in ("corrections.md", "pieges-connus.md", "revue-lundi-2040-07-23.md"):
            continue  # ces fichiers citent volontairement les erreurs passées
        for n, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for motif, msg in INTERDITS:
                if motif.search(ligne):
                    erreurs.append(f"{p.relative_to(RACINE)}:{n} {msg} : {ligne.strip()[:110]}")
    return erreurs


REGISTRE = re.compile(
    r"ultimatum|je pars,? et je dis pourquoi|je veux les faits|je veux savoir ce que tu|"
    r"je (te|vous) demande (deux choses|de |d')|ferme la porte|le mot[^.]{0,40}c'est harcèlement|"
    r"ne t'a pas dit non parce que|ne vous a pas dit non parce que", re.I)
sys.path.insert(0, str(RACINE / "outils"))
import jet as _jet  # noqa: E402  (noms des personnages récurrents de l'univers en cours)
SUBORDONNES = re.compile(_jet.PERSONNAGES)
EXCLUS_REGISTRE = re.compile(r"avant\s*:|version corrigée|corrig|recalibr|tirage|jet\s|\bjets\b", re.I)


def controle_registre():
    """Avertissement NON bloquant : dialogues de subordonnés qui confrontent, menacent ou moralisent William
    (règles 15-16 de CLAUDE.md : registre hiérarchique). À relire à la main avant d'envoyer un tour."""
    avertissements = []
    for dossier in ("journal", "whatsapp"):
        for p in sorted((RACINE / dossier).glob("*.md")):
            for n, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                citations = re.findall(r"«([^»]*)»", ligne)  # on ne teste que ce qui est entre guillemets (paroles)
                if citations and SUBORDONNES.search(ligne) and any(REGISTRE.search(c) for c in citations) \
                        and not EXCLUS_REGISTRE.search(ligne):
                    avertissements.append(f"{p.relative_to(RACINE)}:{n} {ligne.strip()[:120]}")
    return avertissements


def controle_pouvoir():
    """Tables de pouvoir (etat/modele-pouvoir.md) : sommes, plafonds, modificateurs ; jets du régime des tables conformes à la
    règle 17 de CLAUDE.md. Retourne (erreurs, résumé)."""
    sys.path.insert(0, str(RACINE / "outils"))
    import audit_jets
    import jet
    tables, modifs = jet.charger()
    erreurs = jet.valider(tables, modifs)
    b = audit_jets.bilan()
    erreurs += [f"memoire/tirages-aleas.md:{x['ligne']} {x['probleme']}" for x in b["non_conformes"]]
    resume = (f"{len(tables)} table(s), {len(modifs)} modificateur(s) ; jets hérités {b['herites']}, tirages de table {b['tirages']}, "
              f"dérogations {len(b['derogations'])}")
    return erreurs, resume


def controle_donnees():
    """Horloge, agenda, grand livre, qui sait quoi. Retourne (erreurs, avertissements, résumé)."""
    sys.path.insert(0, str(RACINE / "outils"))
    import agenda
    import grand_livre
    import horloge
    import savoir
    erreurs, aver = [], []
    try:
        h = horloge.lire()
    except SystemExit as e:
        return [f"etat/horloge.txt : {e}"], [], "horloge illisible"
    erreurs += agenda.verifier()
    e_gl, retards_gl = grand_livre.verifier()
    erreurs += e_gl
    aver += [f"grand livre : prévu échu non réalisé {l['reference']} {l['date']} {l['libelle'][:60]}" for l in retards_gl]
    erreurs += savoir.verifier()
    retards = [l for l in agenda.lire() if l["statut"] == "prevu" and agenda.instant(l) < h["instant"]]
    aver += [f"agenda : échéance échue non close {l['id']} {l['date']} {l['quoi'][:70]}" for l in retards]
    resume = (f"horloge {h['instant']:%d/%m/%Y %H:%M} ({h['fuseau']}) ; agenda {len(agenda.lire())} lignes ; "
              f"grand livre {len(grand_livre.lire())} lignes ; savoir {len(savoir.lire())} lignes")
    return erreurs, aver, resume


def controle_tics():
    sys.path.insert(0, str(RACINE / "outils"))
    import chasse_tics
    b = chasse_tics.bilan(chasse_tics.lire_journaux(3))
    return [f"TIC {k}" for k in b["tics"]] + [f"CASCADE {c}" for c in b["cascades"]] + [f"RÉPÉTITION {n}× « {g} »" for g, n in b["repetitions"]]


def main():
    code = 0
    err, total = controle_jours()
    print(f"[Jours de la semaine] {total} dates vérifiées")
    for e in err:
        print("  ERREUR", e)
    code |= bool(err)
    err = controle_maitres()
    print("[Fichiers maîtres] " + ("CLAUDE.md, GEMINI.md et AGENTS.md synchronisés" if not err else "ERREUR"))
    for e in err:
        print("  ERREUR", e)
    code |= bool(err)
    err, total = controle_csv()
    print(f"[Fichiers CSV] {total} fichier(s), {len(err)} ligne(s) mal formée(s)")
    for e in err:
        print("  ERREUR", e)
    code |= bool(err)
    err, aver = controle_base()
    print(f"[Base, rituels, relais] {len(err)} erreur(s), {len(aver)} avertissement(s)")
    for e in err:
        print("  ERREUR", e)
    for a in aver:
        print("  RELIRE", a)
    code |= bool(err)
    err = controle_interdits()
    print(f"[Expressions interdites] {len(err)} problème(s)")
    for e in err:
        print("  ERREUR", e)
    code |= bool(err)
    aver = controle_registre()
    print(f"[Registre hiérarchique] {len(aver)} ligne(s) à relire (avertissement, non bloquant)")
    for a in aver:
        print("  RELIRE", a)
    err, resume = controle_pouvoir()
    print(f"[Modèle de pouvoir] {resume}")
    for e in err:
        print("  ERREUR", e)
    code |= bool(err)
    err, aver, resume = controle_donnees()
    print(f"[Données structurées] {resume}")
    for e in err:
        print("  ERREUR", e)
    for a in aver:
        print("  RELIRE", a)
    code |= bool(err)
    tics = controle_tics()
    print(f"[Tics d'écriture] {len(tics)} avertissement(s) sur les 3 derniers journaux (non bloquant)")
    for t in tics:
        print("  RELIRE", t)
    r = subprocess.run([sys.executable, str(RACINE / "outils" / "verifier_pdf.py")], capture_output=True, text=True, encoding="utf-8")
    sortie = [l for l in r.stdout.splitlines() if l.strip() and not l.startswith("[INFO]")]
    mauvais = [l for l in sortie if not l.startswith("[ OK  ]")]
    print(f"[PDF] {len(sortie) - len(mauvais)} OK sur {len(sortie)}")
    for l in mauvais:
        print("  ERREUR", l)
    code |= bool(mauvais)
    print("RÉSULTAT :", "des erreurs à corriger" if code else "aucune incohérence détectée")
    return 1 if code else 0


if __name__ == "__main__":
    sys.exit(main())
