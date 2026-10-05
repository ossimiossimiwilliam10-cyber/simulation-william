"""Audit des jets du moteur — détecte la dérive des probabilités (biais moralisateur, règle 17 de CLAUDE.md).

    python outils/audit_jets.py             # audit complet de memoire/tirages-aleas.md
    python outils/audit_jets.py --seuil 40  # seuil des jets « hérités » à forte probabilité

Trois blocs :
1. **Jets hérités** (avant le régime des tables, probabilités choisies à la main) : ceux qui portent sur une réaction de subordonné
   et dont la probabilité dépasse le seuil, avec la probabilité moyenne déclarée.
2. **Régime des tables** (après le marqueur « RÉGIME DES TABLES DE POUVOIR » de memoire/tirages-aleas.md) : issues observées contre
   issues attendues par table, et part des issues frontales (confrontation, signalement, démission) observée contre attendue.
3. **Non-conformités** : jet libre sur une réaction sans table ni dérogation (code de sortie 1) ; liste des dérogations.
À lancer chaque lundi (revue du lundi, CLAUDE.md §12) et à la demande de l'utilisateur.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jet  # noqa: E402  (définit REACTION_LIBRE, source unique du vocabulaire de réaction)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

JOURNAL = jet.JOURNAL
MARQUEUR = "## RÉGIME DES TABLES DE POUVOIR"
LIBRE = re.compile(r"Jet « (.+?) » : probabilité ([\d.,]+) %, jet\s+([\d.,]+) → \*\*(OUI|NON)\*\*(?: \[DÉROGATION : (.+?)\])?")
TABLE = re.compile(r"Tirage \[(T\w+)\] « (.+?) » : (.+?) ; modificateurs : (.*?) ; jet\s+([\d.,]+) → \*\*(\w+)\*\*")


def analyser(fichier=JOURNAL):
    herites, tirages, libres = [], [], []
    regime = False
    for n, ligne in enumerate(Path(fichier).read_text(encoding="utf-8").splitlines(), 1):
        if ligne.startswith(MARQUEUR):
            regime = True
            continue
        m = TABLE.search(ligne)
        if m:
            repartition = {c: float(p) for c, p in re.findall(r"(\w+) ([\d.]+)", m.group(3))}
            tirages.append({"ligne": n, "table": m.group(1), "libelle": m.group(2), "repartition": repartition,
                            "mods": m.group(4), "issue": m.group(6)})
            continue
        m = LIBRE.search(ligne)
        if m:
            j = {"ligne": n, "libelle": m.group(1), "proba": float(m.group(2).replace(",", ".")),
                 "oui": m.group(4) == "OUI", "derogation": m.group(5)}
            (libres if regime else herites).append(j)
    return herites, tirages, libres


def bilan(fichier=JOURNAL):
    herites, tirages, libres = analyser(fichier)
    non_conformes = [{"ligne": j["ligne"], "probleme": f"jet libre sur une réaction sans table ni dérogation : « {j['libelle'][:70]} »"}
                     for j in libres if jet.REACTION_LIBRE.search(j["libelle"]) and not j["derogation"]]
    return {"herites": len(herites), "tirages": len(tirages), "non_conformes": non_conformes,
            "derogations": [j for j in libres if j["derogation"]], "_herites": herites, "_tirages": tirages}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichier", default=str(JOURNAL))
    ap.add_argument("--seuil", type=float, default=50.0)
    args = ap.parse_args()
    b = bilan(args.fichier)

    print(f"== 1. Jets hérités (probabilités choisies à la main) : {b['herites']} jets ==")
    reac = [j for j in b["_herites"] if jet.REACTION_LIBRE.search(j["libelle"])]
    for j in reac:
        if j["proba"] >= args.seuil:
            print(f"  {j['proba']:5.1f} % -> {'OUI' if j['oui'] else 'NON'}  {j['libelle'][:100]}")
    if reac:
        moy = sum(j["proba"] for j in reac) / len(reac)
        oui = sum(j["oui"] for j in reac)
        print(f"  Réactions de subordonnés : {len(reac)} jets, probabilité moyenne déclarée {moy:.1f} %, "
              f"{oui} OUI observés pour {sum(j['proba'] for j in reac) / 100:.1f} attendus")

    print(f"\n== 2. Régime des tables : {b['tirages']} tirages ==")
    par_table = {}
    for t in b["_tirages"]:
        par_table.setdefault(t["table"], []).append(t)
    frontal_obs = frontal_att = 0.0
    for tid, lst in sorted(par_table.items()):
        obs, att = {}, {}
        for t in lst:
            obs[t["issue"]] = obs.get(t["issue"], 0) + 1
            for c, p in t["repartition"].items():
                att[c] = att.get(c, 0) + p / 100
        print(f"  {tid} ({len(lst)} tirages) : " + " ; ".join(f"{c} {obs.get(c, 0)}/{att[c]:.1f}" for c in att))
        frontal_obs += sum(v for c, v in obs.items() if c.startswith("frontal_"))
        frontal_att += sum(v for c, v in att.items() if c.startswith("frontal_"))
    if b["tirages"]:
        print(f"  Issues frontales : {frontal_obs:.0f} observées pour {frontal_att:.1f} attendues (écart durable = dérive à examiner)")

    print("\n== 3. Non-conformités et dérogations ==")
    for x in b["non_conformes"]:
        print(f"  NON CONFORME ligne {x['ligne']} : {x['probleme']}")
    for j in b["derogations"]:
        print(f"  dérogation ligne {j['ligne']} : « {j['libelle'][:70]} » — {j['derogation']}")
    print(f"  {len(b['non_conformes'])} non-conformité(s), {len(b['derogations'])} dérogation(s)")
    return 1 if b["non_conformes"] else 0


if __name__ == "__main__":
    sys.exit(main())
