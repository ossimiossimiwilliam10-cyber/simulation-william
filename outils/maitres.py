"""Fichiers maîtres : CLAUDE.md (Claude Code), GEMINI.md (Gemini CLI / Antigravity), AGENTS.md (Codex et la plupart des autres
agents). Ils sont IDENTIQUES sauf la ligne 3 (en-tête propre à chaque agent). Créé le 11/10/2026 pour le relais entre agents.

    python outils/maitres.py verifier                       # contrôle (intégré à controle_coherence.py)
    python outils/maitres.py synchroniser --depuis CLAUDE.md # recopie le fichier modifié vers les deux autres (ligne 3 gardée)
    python outils/maitres.py entetes                         # affiche la ligne 3 de chaque fichier

Règle : on modifie UN fichier maître (celui de son agent), puis on lance `synchroniser --depuis <ce fichier>` ; jamais deux
fichiers modifiés à la main en parallèle. Le script refuse de synchroniser si les deux autres fichiers ont divergé entre eux
(signe de deux modifications concurrentes) : il faut alors fusionner à la main.
"""
import argparse
import sys

from commun import RACINE, utf8

MAITRES = ("CLAUDE.md", "GEMINI.md", "AGENTS.md")
ENTETES = {
    "CLAUDE.md": "> Fichier maître lu automatiquement au début de chaque session.",
    "GEMINI.md": "> Fichier maître (Gemini CLI / Antigravity) lu automatiquement au début de chaque session.",
    "AGENTS.md": "> Fichier maître (Codex et autres agents qui lisent AGENTS.md) lu automatiquement au début de chaque session.",
}


def lire(nom):
    p = RACINE / nom
    if not p.exists():
        return None
    # fins de ligne CRLF (Windows) ou LF (dépôt extrait sous Linux ou macOS) : les deux sont acceptées
    return p.read_bytes().decode("utf-8").replace("\r\n", "\n").split("\n")


def ecrire(nom, lignes):
    (RACINE / nom).write_bytes("\r\n".join(lignes).encode("utf-8"))


def verifier():
    """Liste des erreurs (vide si les trois fichiers sont identiques sauf la ligne 3)."""
    erreurs = []
    contenus = {n: lire(n) for n in MAITRES}
    for n, c in contenus.items():
        if c is None:
            erreurs.append(f"{n} absent (python outils/maitres.py synchroniser --depuis CLAUDE.md)")
    presents = [n for n in MAITRES if contenus[n] is not None]
    if len(presents) < 2:
        return erreurs
    ref = presents[0]
    for n in presents[1:]:
        a, b = contenus[ref], contenus[n]
        if len(a) != len(b):
            erreurs.append(f"{ref} ({len(a)} lignes) et {n} ({len(b)} lignes) n'ont pas la même longueur")
            continue
        diff = [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y]
        if diff not in ([], [3]):
            erreurs.append(f"{ref} et {n} diffèrent aux lignes {diff[:12]} (attendu : 3 seulement)")
    return erreurs


def synchroniser(source):
    if source not in MAITRES:
        sys.exit(f"Source inconnue : {source} ({', '.join(MAITRES)})")
    src = lire(source)
    if src is None:
        sys.exit(f"{source} introuvable")
    autres = [n for n in MAITRES if n != source]
    contenus = {n: lire(n) for n in autres}
    a, b = contenus[autres[0]], contenus[autres[1]]
    if a is not None and b is not None:
        corps_a = a[:2] + a[3:]
        corps_b = b[:2] + b[3:]
        if corps_a != corps_b:
            sys.exit(f"{autres[0]} et {autres[1]} ont divergé entre eux : deux modifications concurrentes ? Fusionner à la main, "
                     "puis relancer.")
    for n in autres:
        lignes = list(src)
        entete = (contenus[n][2] if contenus[n] is not None and len(contenus[n]) > 2 else ENTETES[n])
        if len(lignes) > 2:
            lignes[2] = entete
        ecrire(n, lignes)
        print(f"{n} synchronisé depuis {source} (ligne 3 : {entete[:70]}…)")
    err = verifier()
    for e in err:
        print("ERREUR", e)
    return 1 if err else 0


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("verifier")
    p = sp.add_parser("synchroniser")
    p.add_argument("--depuis", required=True)
    sp.add_parser("entetes")
    args = ap.parse_args()
    if args.cmd == "verifier":
        err = verifier()
        for e in err:
            print("ERREUR", e)
        print("Fichiers maîtres :", "synchronisés (identiques sauf la ligne 3)" if not err else "à corriger")
        return 1 if err else 0
    if args.cmd == "synchroniser":
        return synchroniser(args.depuis)
    for n in MAITRES:
        c = lire(n)
        print(f"{n:10s} ligne 3 : {c[2] if c and len(c) > 2 else '(absent)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
