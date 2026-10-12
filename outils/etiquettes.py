"""ÉTIQUETTES DU TÉLÉPHONE (créé le 12/10/2026) : le joueur prépare ses actions dans les applications du téléphone (Voyages, Banque,
Rencontres), les copie et les colle dans la simulation ; chaque ligne porte une étiquette « [appli: commande clé=valeur …] ».
Cet outil les lit et lance la commande exacte, avec l'heure de l'horloge : n'importe quel agent applique ainsi la décision du joueur
sans la réinterpréter (CLAUDE.md §14).

    python outils/etiquettes.py --texte "<texte collé par le joueur>" [--quand "AAAA-MM-JJ HH:MM"] [--simule]
    python outils/etiquettes.py --fichier message.txt

Étiquettes reconnues :
  [voyages: reserver vol=V3 aller=… retour=… voyageurs=1]          → voyages.py reserver
  [voyages: reserver-hotel hotel=M4 arrivee=… depart=…]            → voyages.py reserver-hotel
  [voyages: reserver-forfait vol=W2 hotel=M4 aller=… retour=… voyageurs=1 carte=visa_premier] → voyages.py reserver-forfait
      (carte= depuis le 12/10/2026 : plafond contrôlé par cartes.py ; sans carte, débit direct du compte courant, ancien comportement)
  [banque: virement de=courant vers=projet montant=500 date=… beneficiaire="…"] → banque.py virement
  [banque: ordre-modifier id=E012 montant=3000 jour=2]             → banque.py ordre-modifier
  [banque: ordre-creer de=… vers=… montant=… jour=… debut=…]      → banque.py ordre-creer
  [banque: ordre-suspendre id=E014]  /  [banque: ordre-reprendre id=E014]
  [rencontres: inscription abonnement=plus ville=MNL bio="…"]       → rencontres.py inscription
  [rencontres: aimer id=…]  /  [rencontres: passer id=…]            → rencontres.py aimer / passer (puis T21 pour la réaction)
  [rencontres: message id=… texte="…"]                             → rencontres.py message --auteur william
Le récit reste à écrire par le moteur (ce que William voit, les réactions tirées) ; l'outil n'invente rien.
"""
import argparse
import os
import re
import shlex
import subprocess
import sys

from commun import OUTILS, maintenant_simule, utf8

ETIQUETTE = re.compile(r"\[(voyages|banque|rencontres):\s*([a-z-]+)((?:\s+[a-z_]+=(?:\"[^\"]*\"|\S+?))*)\s*\]")
CLE_VALEUR = re.compile(r"([a-z_]+)=(\"[^\"]*\"|\S+)")
# (appli, commande) → (script, sous-commande, argument positionnel éventuel, options acceptées)
TABLE = {
    ("voyages", "reserver"): ("voyages.py", "reserver", None, {"vol", "aller", "retour", "voyageurs", "carte"}),
    ("voyages", "reserver-hotel"): ("voyages.py", "reserver-hotel", None, {"hotel", "arrivee", "depart", "carte"}),
    ("voyages", "reserver-forfait"): ("voyages.py", "reserver-forfait", None, {"vol", "hotel", "aller", "retour", "voyageurs", "carte"}),
    ("banque", "virement"): ("banque.py", "virement", None, {"de", "vers", "montant", "date", "beneficiaire", "libelle"}),
    ("banque", "ordre-modifier"): ("banque.py", "ordre-modifier", "id", {"montant", "jour"}),
    ("banque", "ordre-creer"): ("banque.py", "ordre-creer", None, {"de", "vers", "montant", "jour", "debut", "libelle"}),
    ("banque", "ordre-suspendre"): ("banque.py", "ordre-suspendre", "id", set()),
    ("banque", "ordre-reprendre"): ("banque.py", "ordre-reprendre", "id", set()),
    ("rencontres", "inscription"): ("rencontres.py", "inscription", None, {"abonnement", "ville", "bio", "recherche"}),
    ("rencontres", "aimer"): ("rencontres.py", "aimer", "id", set()),
    ("rencontres", "passer"): ("rencontres.py", "passer", "id", set()),
    ("rencontres", "message"): ("rencontres.py", "message", "id", {"texte"}),
}


def commandes(texte, quand):
    res = []
    for m in ETIQUETTE.finditer(texte):
        appli, cmd, reste = m.group(1), m.group(2), m.group(3)
        cle = (appli, cmd)
        if cle not in TABLE:
            res.append((m.group(0), None, f"étiquette inconnue : {appli}: {cmd}"))
            continue
        script, sous, positionnel, permises = TABLE[cle]
        valeurs = {k: v.strip('"') for k, v in CLE_VALEUR.findall(reste)}
        args = [sys.executable, str(OUTILS / script), sous]
        if positionnel:
            if positionnel not in valeurs:
                res.append((m.group(0), None, f"{positionnel}= manquant"))
                continue
            args.append(valeurs.pop(positionnel))
        inconnues = set(valeurs) - permises
        if inconnues:
            res.append((m.group(0), None, f"clé(s) inconnue(s) : {', '.join(sorted(inconnues))}"))
            continue
        for k, v in valeurs.items():
            args += [f"--{k}", v]
        if cle == ("rencontres", "message"):
            args += ["--auteur", "william"]
        args += ["--quand", quand]
        res.append((m.group(0), args, ""))
    return res


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--texte")
    ap.add_argument("--fichier")
    ap.add_argument("--quand", help="heure du jeu (par défaut : l'horloge)")
    ap.add_argument("--simule", action="store_true", help="affiche les commandes sans les lancer")
    args = ap.parse_args()
    texte = args.texte or (open(args.fichier, encoding="utf-8").read() if args.fichier else sys.stdin.read())
    quand = args.quand or f"{maintenant_simule():%Y-%m-%d %H:%M}"
    liste = commandes(texte, quand)
    if not liste:
        print("Aucune étiquette [voyages|banque|rencontres: …] trouvée.")
        return 1
    code = 0
    for brut, cmd, erreur in liste:
        if erreur:
            print(f"IGNORÉE {brut} : {erreur}")
            code = 1
            continue
        lisible = " ".join(shlex.quote(x) for x in cmd[1:])
        if args.simule:
            print(f"(essai) python {lisible}")
            continue
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                           env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        print(f"→ python {lisible}\n  " + (r.stdout.strip() or r.stderr.strip()).replace("\n", "\n  "))
        code |= r.returncode
    return code


if __name__ == "__main__":
    sys.exit(main())
