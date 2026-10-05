"""Jet de dé pour une décision aléatoire ponctuelle (friction administrative, délai, refus, etc.).

    python outils/jet.py "Capitol : attestation prête à l'heure" 70
    python outils/jet.py "Banque : deuxième passage demandé" 30 --simule

Tire un nombre entre 0 et 100 avec un vrai hasard ; le résultat est « OUI » si le jet est strictement inférieur
à la probabilité donnée (en %). Consigné dans `memoire/tirages-aleas.md` sauf avec --simule.
Règle de friction administrative (CLAUDE.md §12) : pour toute démarche à enjeu, jet « deuxième passage demandé »
(par défaut 30 %), sauf si le réalisme impose un autre taux ; ne pas rejouer un jet.
"""
import argparse
import datetime as dt
import random
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("libelle")
    ap.add_argument("proba", type=float, help="probabilité de OUI, en %%")
    ap.add_argument("--simule", action="store_true")
    args = ap.parse_args()
    jet = random.SystemRandom().uniform(0, 100)
    oui = jet < args.proba
    ligne = f"- Jet « {args.libelle} » : probabilité {args.proba:g} %, jet {jet:5.1f} → **{'OUI' if oui else 'NON'}**"
    print(ligne)
    if not args.simule:
        journal = RACINE / "memoire" / "tirages-aleas.md"
        if not journal.exists():
            journal.write_text("# Journal des tirages d'aléas (ne jamais effacer, ne jamais rejouer)\n\n", encoding="utf-8")
        with journal.open("a", encoding="utf-8") as f:
            f.write(f"\n{ligne} (enregistré le {dt.datetime.now():%d/%m/%Y %H:%M} heure machine)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
