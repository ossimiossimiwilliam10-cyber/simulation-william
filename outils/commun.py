"""Fonctions communes aux outils du moteur (créé le 11/10/2026, date réelle, pour le relais entre agents et la base de données).

Conventions du dépôt, valables pour TOUS les agents (Claude, Gemini, Codex…) :
- fichiers texte en UTF-8, fins de ligne CRLF ; CSV séparés par « ; » avec une ligne d'en-tête ;
- dates AAAA-MM-JJ, heures HH:MM, dans le fuseau indiqué (par défaut celui de l'horloge, `etat/horloge.txt`) ;
- la console Windows affiche parfois mal les accents : `utf8()` force la sortie en UTF-8 (le fichier, lui, est juste).

    from commun import RACINE, utf8, lire_csv, ecrire_csv, date_fr
"""
import csv
import datetime as dt
import hashlib
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
OUTILS = RACINE / "outils"
ETAT = RACINE / "etat"
DONNEES = RACINE / "donnees"
MEMOIRE = RACINE / "memoire"
JOURNAL = RACINE / "journal"
SORTIES = RACINE / "sorties"

JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre",
        "décembre"]


def utf8():
    """Sortie console en UTF-8 (Windows)."""
    for flux in (sys.stdout, sys.stderr):
        if hasattr(flux, "reconfigure"):
            try:
                flux.reconfigure(encoding="utf-8")
            except (ValueError, OSError):
                pass


# ---------------------------------------------------------------- fichiers
def lire_texte(chemin):
    p = Path(chemin)
    return p.read_text(encoding="utf-8") if p.exists() else ""


def ecrire_texte(chemin, texte):
    """Écrit en UTF-8 avec des fins de ligne CRLF (convention du dépôt)."""
    p = Path(chemin)
    p.parent.mkdir(parents=True, exist_ok=True)
    texte = texte.replace("\r\n", "\n").replace("\n", "\r\n")
    p.write_bytes(texte.encode("utf-8"))


def ajouter_texte(chemin, texte):
    p = Path(chemin)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("ab") as f:
        f.write(texte.replace("\r\n", "\n").replace("\n", "\r\n").encode("utf-8"))


def lire_csv(chemin):
    p = Path(chemin)
    if not p.exists():
        return []
    with p.open(encoding="utf-8", newline="") as f:
        return [dict(l) for l in csv.DictReader(f, delimiter=";")]


def colonnes_csv(chemin):
    p = Path(chemin)
    if not p.exists():
        return []
    with p.open(encoding="utf-8", newline="") as f:
        return next(csv.reader(f, delimiter=";"), [])


def ecrire_csv(chemin, lignes, colonnes):
    p = Path(chemin)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=colonnes, delimiter=";", lineterminator="\r\n", extrasaction="ignore")
        w.writeheader()
        for l in lignes:
            w.writerow({c: ("" if l.get(c) is None else l.get(c)) for c in colonnes})


def empreinte(*chemins):
    """Empreinte SHA-1 courte d'un ensemble de fichiers (détection de changements)."""
    h = hashlib.sha1()
    for c in chemins:
        p = Path(c)
        if p.is_file():
            h.update(str(p).encode())
            h.update(p.read_bytes())
    return h.hexdigest()[:12]


# ---------------------------------------------------------------- dates
def date_fr(d, annee=True, jour=True):
    """samedi 14 juillet 2040"""
    if isinstance(d, dt.datetime):
        d = d.date()
    t = f"{d.day} {MOIS[d.month - 1]}" + (f" {d.year}" if annee else "")
    if d.day == 1:
        t = "1er" + t[1:]
    return (JOURS[d.weekday()] + " " + t) if jour else t


def heure_fr(t):
    """08h05"""
    return f"{t.hour:02d}h{t.minute:02d}"


def jour_court(d):
    return JOURS[d.weekday()][:3]


def analyser_date(texte):
    """AAAA-MM-JJ ou JJ/MM[/AAAA] (année 2040 par défaut) -> date."""
    t = texte.strip()
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", t)
    if m:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})(?:/(\d{4}))?", t)
    if m:
        return dt.date(int(m.group(3) or 2040), int(m.group(2)), int(m.group(1)))
    raise ValueError(f"Date illisible : {texte} (attendu AAAA-MM-JJ ou JJ/MM[/AAAA])")


def analyser_instant_naif(texte):
    """« AAAA-MM-JJ HH:MM » -> datetime naïf."""
    d, h = texte.strip().split()
    hh, mm = re.fullmatch(r"(\d{1,2})[:h](\d{2})", h).groups()
    return dt.datetime.combine(analyser_date(d), dt.time(int(hh), int(mm)))


def maintenant_simule():
    """Instant de l'horloge (datetime aware) ; None si l'horloge est illisible."""
    sys.path.insert(0, str(OUTILS))
    try:
        import horloge
        return horloge.lire()["instant"]
    except SystemExit:
        return None


def age(naissance, au):
    """Âge révolu à la date `au`."""
    if isinstance(naissance, str):
        naissance = dt.date.fromisoformat(naissance)
    if isinstance(au, dt.datetime):
        au = au.date()
    return au.year - naissance.year - ((au.month, au.day) < (naissance.month, naissance.day))


# ---------------------------------------------------------------- texte
def slug(texte):
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def sans_accents(texte):
    return unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()


# ---------------------------------------------------------------- git
def git(*args, cwd=RACINE, defaut=None):
    """Lance git ; renvoie la sortie (str, sans espace final) ou `defaut` en cas d'échec."""
    try:
        r = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return defaut
    if r.returncode != 0:
        return defaut
    return r.stdout.rstrip()


def dossier_git_commun():
    """Dossier .git partagé par tous les worktrees (pour un verrou visible de toutes les sessions)."""
    d = git("rev-parse", "--git-common-dir")
    if not d:
        return None
    p = Path(d)
    return p if p.is_absolute() else (RACINE / p).resolve()


def tableau_md(entetes, lignes):
    """Petit tableau Markdown."""
    out = ["| " + " | ".join(entetes) + " |", "|" + "|".join("---" for _ in entetes) + "|"]
    for l in lignes:
        out.append("| " + " | ".join(str(x).replace("|", "/") for x in l) + " |")
    return "\n".join(out)
