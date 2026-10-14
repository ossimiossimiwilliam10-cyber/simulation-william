"""Archive le §9 (POINT DE REPRISE) des fichiers maîtres : le §9 était devenu un journal de 157 Ko sur 183 Ko, relu à chaque session.

    python outils/archiver_point_de_reprise.py                    # essai : tailles et entrées conservées, rien n'est écrit
    python outils/archiver_point_de_reprise.py --garder 8 --ecrire

Principe (CLAUDE.md §7 : « ne supprime jamais une information ») :
1. le §9 COMPLET est copié tel quel dans `memoire/archive-point-de-reprise-AAAA-MM-JJ.md` (date de la simulation lue dans etat/horloge.txt) ;
2. dans les trois fichiers maîtres (CLAUDE.md, GEMINI.md et AGENTS.md ; AGENTS.md ajouté le 13/10/2026), le §9 est remplacé par : une note de renvoi, le paragraphe d'introduction, et les N entrées les plus
   récentes (une entrée = un paragraphe commençant par « ** », la plus récente en tête) ;
3. les trois fichiers restent identiques à la ligne 3 près (contrôle intégré, comme `outils/maitres.py verifier`).
L'état courant se lit ensuite dans `etat/resume.md` (outils/resume_etat.py), `etat/horloge.txt`, `etat/fils-ouverts.md`, `etat/agenda.csv`.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import horloge  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
MAITRES = tuple(m for m in ("CLAUDE.md", "GEMINI.md", "AGENTS.md") if (RACINE / m).exists())  # avant : CLAUDE.md et GEMINI.md seuls


def lire(nom):
    return (RACINE / nom).read_bytes().decode("utf-8").split("\r\n")


def bornes(lignes):
    debut = next(i for i, l in enumerate(lignes) if l.startswith("## 9."))
    fin = next(i for i, l in enumerate(lignes) if l.startswith("## 10."))
    return debut, fin


def entrees(corps):
    """[(premiere_ligne_index, [lignes])] : une entrée commence par « ** » en début de ligne ; les lignes suivantes qui n'y
    commencent pas lui sont rattachées."""
    blocs = []
    for i, l in enumerate(corps):
        if l.startswith("**") or not blocs:
            blocs.append([l])
        else:
            blocs[-1].append(l)
    return blocs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--garder", type=int, default=8, help="nombre d'entrées récentes conservées (hors introduction)")
    ap.add_argument("--ecrire", action="store_true")
    ap.add_argument("--force", action="store_true", help="écrase une archive du même jour")
    args = ap.parse_args()

    h = horloge.lire()["instant"]
    archive = RACINE / "memoire" / f"archive-point-de-reprise-{h:%Y-%m-%d}.md"
    originaux = {m: lire(m) for m in MAITRES}
    d, f = bornes(originaux["CLAUDE.md"])
    corps = [l for l in originaux["CLAUDE.md"][d + 1:f]]
    while corps and corps[-1] == "":
        corps.pop()
    blocs = entrees(corps)
    intro, recents = blocs[0], blocs[1:1 + args.garder]
    octets = lambda ls: sum(len(x.encode("utf-8")) + 2 for x in ls)
    avant = octets(corps)
    conserve = octets(intro) + sum(octets(b) for b in recents)
    print(f"§9 actuel : {len(blocs)} blocs, {avant} octets ; conservés : introduction + {len(recents)} entrées ({conserve} octets).")
    print(f"Archive : {archive.relative_to(RACINE)} ({'existe déjà' if archive.exists() else 'à créer'}).")
    if not args.ecrire:
        print("Essai : rien n'est écrit (ajouter --ecrire).")
        return 0
    if archive.exists() and not args.force:  # 14/10/2026 : plusieurs archives le même jour simulé, sans rien écraser
        n = 2
        while (RACINE / "memoire" / f"archive-point-de-reprise-{h:%Y-%m-%d}-{n}.md").exists():
            n += 1
        archive = RACINE / "memoire" / f"archive-point-de-reprise-{h:%Y-%m-%d}-{n}.md"
    entete = [f"# Archive du point de reprise (§9 des fichiers maîtres) au {h:%d/%m/%Y %H:%M}",
              "",
              "> Copie intégrale, mot pour mot, du §9 avant sa compression (outils/archiver_point_de_reprise.py). Ne rien supprimer ici.",
              "> Les entrées sont classées de la plus récente à la plus ancienne ; les entrées « hors ordre » (corrections, pause du 25/07,",
              "> levée des verrous…) sont à leur place d'origine.",
              ""]
    archive.write_bytes("\r\n".join(entete + corps).encode("utf-8") + b"\r\n")
    note = ("**(Compression du §9, " + f"{h:%d/%m/%Y}" + ")** Le journal détaillé des tours précédents est archivé tel quel dans "
            f"`memoire/{archive.name}` ; ce §9 ne garde que l'introduction et les {len(recents)} entrées les plus récentes. "
            "État courant : `python outils/resume_etat.py` (écrit `etat/resume.md`), `etat/horloge.txt`, `etat/fils-ouverts.md`, `etat/agenda.csv`. "
            "À chaque tour : ajouter l'entrée EN TÊTE de ce §9 ; au-delà de 12 entrées : `python outils/archiver_point_de_reprise.py --garder 8 --ecrire`.**")
    intro = [l for l in intro if not l.startswith("**(Compression du §9")]  # les anciennes notes restent dans les archives
    nouveau_corps = [note] + intro + [x for b in recents for x in b]
    for m in MAITRES:
        l = originaux[m]
        dm, fm = bornes(l)
        sortie = l[:dm + 1] + nouveau_corps + [""] + l[fm:]
        (RACINE / m).write_bytes("\r\n".join(sortie).encode("utf-8"))
    a = lire("CLAUDE.md")
    code = 0
    for m in MAITRES[1:]:
        b = lire(m)
        ecart = [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y]
        print(f"Écrit. CLAUDE.md : {len('\r\n'.join(a).encode('utf-8'))} octets ; écarts avec {m} : lignes {ecart} (attendu : [3]).")
        if ecart != [3] or len(a) != len(b):
            code = 1
    return code


if __name__ == "__main__":
    sys.exit(main())
