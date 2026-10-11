"""Chasse aux tics d'écriture (CLAUDE.md §12 : « chasse aux tics », revue du lundi n° 2 et n° 3).

    python outils/chasse_tics.py                        # les 3 derniers journaux (journal/*.md)
    python outils/chasse_tics.py --jours 5              # plus de journaux
    python outils/chasse_tics.py --texte brouillon.txt  # un brouillon de tour avant de l'envoyer (aucun fichier du dépôt n'est lu)

Trois contrôles, tous de simples AVERTISSEMENTS (code de sortie 0) :
1. **Tics connus** : expressions déjà signalées par l'utilisateur ou par les revues (liste TICS), comptées sur la période ;
2. **Cascades** : « Bien, patron. » plus de 3 fois dans un même jour ; plus de 2 ouvertures de paragraphe identiques de suite ;
3. **Répétitions** : suites de 5 mots qui reviennent 4 fois ou plus dans la narration (hors dialogues entre « », hors métadonnées
   entre parenthèses ou astérisques), pour repérer les nouveaux tics avant qu'ils n'en deviennent.
La liste TICS se complète à la main à chaque revue du lundi.
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
TICS = [
    (r"la table voisine", "« la table voisine se retourne »"),
    (r"\bun temps\b", "« un temps » (silence)"),
    (r"reste sur le seuil|sur le seuil", "« elle reste sur le seuil »"),
    (r"coches? (?:passent?|deviennent?|virent?) au bleu", "« les coches passent au bleu »"),
    (r"clim(?:atisation)? (?:souffle|ronronne|bourdonne)", "« la clim souffle / ronronne »"),
    (r"ronronne", "« ronronne »"),
    (r"odeur de lessive", "« l'odeur de lessive »"),
    (r"valise (?:qui )?attend", "« la valise qui attend »"),
    (r"le message est lu\W+(?:pas de réponse|sans réponse)", "« le message est lu… pas de réponse »"),
    (r"(?:^|\n)\s*[-*]*\s*\**Dehors,", "ouverture « Dehors, … »"),
    (r"le regard (?:se )?(?:fixe|perd|accroche)", "regards qui se fixent / se perdent"),
    (r"(?:ses|les) mains? (?:se )?(?:serrent|crispent|tordent)", "mains qui se serrent / se tordent"),
    (r"un silence (?:s'installe|tombe|pèse)", "« un silence s'installe / tombe / pèse »"),
]
STOP = set("le la les de des du un une et à en au aux que qui il elle ils elles on se sa son ses ce cette ces dans pour par sur "
           "avec sans est a ne pas plus ou où mais donc car ni leur leurs lui y d l s n j qu c m t".split())


def narration(texte):
    """Retire dialogues « », parenthèses, astérisques, code, chiffres et lignes de protocole : ne garde que la narration."""
    texte = "\n".join(l for l in texte.splitlines()
                      if not re.match(r"\s*[-*]*\s*\**Tour (en cours|arrêté)", l) and "Tour arrêté" not in l)
    t = re.sub(r"«[^»]*»", " ", texte)
    t = re.sub(r"\([^)]*\)", " ", t)
    t = re.sub(r"`[^`]*`", " ", t)
    t = re.sub(r"[*_#>|\[\]]", " ", t)
    t = re.sub(r"\d+[h:]?\d*", " ", t)
    return t


def mots(texte):
    return re.findall(r"[a-zàâäçéèêëîïôöùûüÿœ'’-]+", texte.lower())


def lire_journaux(n):
    fichiers = sorted((RACINE / "journal").glob("*.md"))[-n:]
    return [(f.name, f.read_text(encoding="utf-8")) for f in fichiers]


def bilan(textes):
    """textes : [(nom, texte)] -> {'tics': {libellé: [(nom, n)]}, 'cascades': [str], 'repetitions': [(ngramme, n)]}"""
    tics = {}
    for nom, t in textes:
        for motif, libelle in TICS:
            n = len(re.findall(motif, t, flags=re.I))
            if n:
                tics.setdefault(libelle, []).append((nom, n))
    cascades = []
    for nom, t in textes:
        n = len(re.findall(r"Bien, patron\.", t))
        if n > 3:
            cascades.append(f"{nom} : « Bien, patron. » {n} fois")
        ouvertures = [re.sub(r"\W+", " ", ligne.strip())[:25].lower() for ligne in t.splitlines() if len(ligne.strip()) > 30]
        run = 1
        for a, b in zip(ouvertures, ouvertures[1:]):
            run = run + 1 if a == b and a else 1
            if run == 3:
                cascades.append(f"{nom} : trois paragraphes de suite ouverts par « {a} »")
    compte = Counter()
    for _, t in textes:
        m = [w for w in mots(narration(t)) if len(w) > 1]
        for i in range(len(m) - 4):
            gram = m[i:i + 5]
            if sum(w in STOP for w in gram) >= 4:
                continue
            compte[" ".join(gram)] += 1
    repetitions = [(g, n) for g, n in compte.most_common(40) if n >= 4][:10]
    return {"tics": tics, "cascades": cascades, "repetitions": repetitions}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--jours", type=int, default=3)
    ap.add_argument("--texte", help="fichier texte d'un brouillon de tour")
    args = ap.parse_args()
    if args.texte:
        textes = [(Path(args.texte).name, Path(args.texte).read_text(encoding="utf-8"))]
        portee = f"le brouillon {Path(args.texte).name}"
    else:
        textes = lire_journaux(args.jours)
        portee = "les journaux " + ", ".join(n for n, _ in textes)
    b = bilan(textes)
    print(f"Chasse aux tics sur {portee}")
    for libelle, lst in b["tics"].items():
        print(f"  TIC {libelle} : " + ", ".join(f"{n}× ({nom})" for nom, n in lst))
    for c in b["cascades"]:
        print(f"  CASCADE {c}")
    for g, n in b["repetitions"]:
        print(f"  RÉPÉTITION {n}× « {g} »")
    total = len(b["tics"]) + len(b["cascades"]) + len(b["repetitions"])
    print(f"  {total} avertissement(s) (non bloquants).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
