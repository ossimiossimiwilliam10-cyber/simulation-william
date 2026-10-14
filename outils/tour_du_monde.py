"""Tour du monde : tire la journée de chaque personnage récurrent (vie propre, T11), la catégorie du contenu (T13a-d) et son
initiative envers William (T14, puis l'heure en T10), d'après `etat/vies-propres.md`.

Mécanisme validé par l'utilisateur le 09/08/2040 (T11) ; T13 et T14 installées le 09/08/2040 sur « applique tout cela ».
À lancer à chaque fin de journée simulée et à chaque « Go » :
    python outils/tour_du_monde.py 10/08                    # tire et consigne (memoire/tirages-aleas.md)
    python outils/tour_du_monde.py 10/08 --simule           # essai, rien n'est consigné
    python outils/tour_du_monde.py 10/08 --sans-initiatives # T11 + T13 seulement
Chaque fiche (« ### Nom ») porte des lignes « - **Modificateurs T11** : M80, M81 » (ou « — »), « - **Modificateurs T13** : M95 » (ou « — »)
et « - **Modificateurs T14** : M84 » (« — » = pas d'initiative envers William ; « aucun » = tirage sans modificateur).
Les tirages passent par `outils/jet.py`, qui consigne lui-même. Le DÉTAIL de chaque événement se choisit ensuite d'après la fiche
(test d'intérêt) ; ce qui touche William ou OSIA se tire dans les tables existantes (T1-T10, T12).
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))
import jet  # noqa: E402

FICHES = RACINE / "etat" / "vies-propres.md"
for flux in (sys.stdout, sys.stderr):
    if hasattr(flux, "reconfigure"):
        flux.reconfigure(encoding="utf-8")

CONTENU = {"coup_dur": "T13a", "tournant": "T13b", "petit_evenement": "T13c", "avancee_objectif": "T13d"}
LIGNE_MODS = re.compile(r"\*\*Modificateurs T(11|13|14)\*\* : (.*)")


def lire_fiches():
    personnages, courant = [], None
    for ligne in FICHES.read_text(encoding="utf-8").splitlines():
        if ligne.startswith("### "):
            courant = {"nom": ligne[4:].strip(), "T11": [], "T13": [], "T14": None}
            personnages.append(courant)
        elif courant and (m := LIGNE_MODS.search(ligne)):
            table, reste = m.group(1), m.group(2).strip()
            codes = re.findall(r"M\d{2,3}", reste)
            if table == "14":
                courant["T14"] = None if reste.startswith("—") else codes
            else:
                courant["T" + table] = codes
        elif ligne.startswith("## ") and courant:
            courant = None
    return personnages


def tirer(table, mods, libelle, simule, tables, modifs):
    """Lance jet.py --table ; retourne l'issue ou un message d'erreur."""
    cmd = [sys.executable, str(RACINE / "outils" / "jet.py"), "--table", table]
    for m in mods:
        if table in modifs.get(m, {}).get("tables", []):
            cmd += ["--mod", m]
    if simule:
        cmd.append("--simule")
    cmd.append(libelle)
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    sortie = [l for l in res.stdout.splitlines() if l.startswith("- Tirage")]
    if not sortie:
        return "ERREUR : " + (res.stderr.strip() or res.stdout.strip())
    return re.search(r"→ \*\*(\w+)\*\*", sortie[0]).group(1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("date", help="jour simulé, JJ/MM")
    ap.add_argument("--simule", action="store_true", help="ne consigne rien")
    ap.add_argument("--sans-initiatives", action="store_true", help="ne tire pas T14")
    ap.add_argument("--ancien", action="store_true", help="ancien tirage d'après les fiches (avant le 14/10/2026)")
    args = ap.parse_args()
    if not args.ancien:  # 14/10/2026 : le tour du monde passe par outils/monde_vivant.py (cadences, liens, routines)
        import datetime as dt
        import horloge
        import monde_vivant
        j, m = (int(x) for x in args.date.split("/")[:2])
        jour = dt.date(horloge.lire()["instant"].year, m, j)
        for l in monde_vivant.avancer(jour, simule=args.simule) or ["(rien à tirer : journée déjà tirée)"]:
            print(l)
        return
    tables, modifs = jet.charger()
    initiatives = []
    for p in lire_fiches():
        issue = tirer("T11", p["T11"], f"Tour du monde du {args.date} : {p['nom']}", args.simule, tables, modifs)
        ligne = f"{p['nom']} : {issue}"
        if issue in CONTENU:
            t13 = CONTENU[issue]
            categorie = tirer(t13, p["T13"], f"Contenu ({issue}) du {args.date} : {p['nom']}", args.simule, tables, modifs)
            ligne += f" → contenu {t13} : {categorie}"
        print(ligne)
        if not args.sans_initiatives and p["T14"] is not None:
            ini = tirer("T14", p["T14"], f"Initiative envers William du {args.date} : {p['nom']}", args.simule, tables, modifs)
            if ini != "aucune" and not ini.startswith("ERREUR"):
                mod_heure = ["M71"] if ini in ("demande", "information") else ["M74"]
                heure = tirer("T10", mod_heure, f"Heure de l'initiative ({ini}) du {args.date} : {p['nom']}", args.simule, tables, modifs)
                initiatives.append(f"  INITIATIVE {p['nom']} : {ini} ; heure {heure}")
            elif ini.startswith("ERREUR"):
                initiatives.append(f"  {p['nom']} : {ini}")
    if not args.sans_initiatives:
        print("Initiatives envers William :" if initiatives else "Initiatives envers William : aucune ce jour-là.")
        for i in initiatives:
            print(i)


if __name__ == "__main__":
    main()
