"""Contrôle de cohérence du dépôt de la simulation — À LANCER avant de clore un tour (checklist de CLAUDE.md §7).

    python outils/controle_coherence.py

Contrôles automatiques :
1. **Jours de la semaine** : toute mention « lundi 23/07 », « mer. 25/07 », « Dim. 29/07/2040 »… (jour + date JJ/MM)
   est vérifiée par calcul (année 2040 par défaut). Erreur = incohérence réelle dans l'état du monde.
2. **Fichiers maîtres** : `CLAUDE.md` et `GEMINI.md` doivent être identiques à la ligne 3 près.
3. **Expressions interdites** : formes déjà corrigées (« faute grave » à propos d'un CDD, « Net » dans les contrats…).
4. **PDF** : lance `verifier_pdf.py` (accents, texte extractible).
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
DOSSIERS = ["etat", "osia", "personnes", "journal", "memoire", "whatsapp", "serveur", "."]
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
        for n, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
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
    a = (RACINE / "CLAUDE.md").read_text(encoding="utf-8").splitlines()
    b = (RACINE / "GEMINI.md").read_text(encoding="utf-8").splitlines()
    if len(a) != len(b):
        return [f"CLAUDE.md ({len(a)} lignes) et GEMINI.md ({len(b)} lignes) n'ont pas la même longueur"]
    diff = [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y]
    return [] if diff == [3] else [f"CLAUDE.md et GEMINI.md diffèrent aux lignes {diff} (attendu : 3 seulement)"]


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


def main():
    code = 0
    err, total = controle_jours()
    print(f"[Jours de la semaine] {total} dates vérifiées")
    for e in err:
        print("  ERREUR", e)
    code |= bool(err)
    err = controle_maitres()
    print("[Fichiers maîtres] " + ("synchronisés" if not err else "ERREUR"))
    for e in err:
        print("  ERREUR", e)
    code |= bool(err)
    err = controle_interdits()
    print(f"[Expressions interdites] {len(err)} problème(s)")
    for e in err:
        print("  ERREUR", e)
    code |= bool(err)
    r = subprocess.run([sys.executable, str(RACINE / "outils" / "verifier_pdf.py")], capture_output=True, text=True, encoding="utf-8")
    sortie = [l for l in r.stdout.splitlines() if l.strip()]
    mauvais = [l for l in sortie if not l.startswith("[ OK  ]")]
    print(f"[PDF] {len(sortie) - len(mauvais)} OK sur {len(sortie)}")
    for l in mauvais:
        print("  ERREUR", l)
    code |= bool(mauvais)
    print("RÉSULTAT :", "des erreurs à corriger" if code else "aucune incohérence détectée")
    return 1 if code else 0


if __name__ == "__main__":
    sys.exit(main())
