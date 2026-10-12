"""Résumé d'état généré : tout ce qu'il faut savoir en 3 minutes au début d'un tour (écrit dans `etat/resume.md`, jamais à la main).

    python outils/resume_etat.py              # écrit etat/resume.md et l'affiche
    python outils/resume_etat.py --sans-ecrire

Sources : etat/horloge.txt, etat/grand-livre.csv, etat/agenda.csv, etat/savoir.csv, outils/calendrier_2040.py, dernier journal.
Il COMPLÈTE la lecture des fichiers d'état exigée par CLAUDE.md §7 (règle 3 « Scan 5x ») ; il ne la remplace pas.
"""
import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import agenda  # noqa: E402
import calendrier_2040 as cal  # noqa: E402
import fuseaux  # noqa: E402
import grand_livre as gl  # noqa: E402
import horloge  # noqa: E402
import savoir  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "etat" / "resume.md"
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]


def construire():
    h = horloge.lire()
    t = h["instant"]
    fuseau = h["fuseau"]
    L = []
    L.append(f"# Résumé d'état (généré le {dt.datetime.now():%d/%m/%Y %H:%M} heure machine par outils/resume_etat.py : ne pas éditer à la main)")
    L.append("")
    L.append(f"## Horloge : {JOURS[t.weekday()]} {t:%d/%m/%Y %H:%M} ({fuseau}, {fuseaux.libelle_ecart(t)})")
    L.append(f"- **Lieu de William** : {h['lieu']}")
    L.append("- **Heure dans les autres lieux** : " + " ; ".join(
        f"{n} {fuseaux.convertir(t, n):%H:%M}" for n in fuseaux.ZONES if n != fuseau))
    if h["attentes"]:
        L.append("- **En attente de William** :")
        L += [f"  - {a}" for a in h["attentes"]]
    L.append("")

    naif = t.replace(tzinfo=None)
    s = gl.soldes(naif)
    L.append("## Argent (grand livre, calculé)")
    for c in ("courant", "projet", "etf", "osia_sgbci"):
        prop, dev, desc, _ = gl.COMPTES[c]
        L.append(f"- {desc} : **{gl.fmt(s[c], dev)}**")
    patri = sum(gl.vers_eur(s[c], gl.COMPTES[c][1]) for c in gl.COMPTES if gl.COMPTES[c][3])
    L.append(f"- Patrimoine net de William : **{gl.fmt(patri, 'EUR')}**")
    prevus = [l for l in sorted(gl.lire(), key=gl.quand) if l["type"] == "prevu" and naif < gl.quand(l) <= naif + dt.timedelta(days=14)]
    if prevus:
        L.append("- Prévu dans les 14 jours : " + " ; ".join(
            f"{l['date'][8:]}/{l['date'][5:7]} {l['libelle'].split(' (')[0][:52]} ({gl.fmt(float(l['montant']), gl.COMPTES[l['compte']][1])})"
            for l in prevus))
    L.append("")

    lignes = agenda.lire()
    ordre = sorted(lignes, key=agenda.instant)
    retards = [l for l in ordre if l["statut"] == "prevu" and agenda.instant(l) < t]
    if retards:
        L.append("## ÉCHÉANCES ÉCHUES NON CLOSES (jouer, reporter avec raison ou annuler : règle 14)")
        L += [f"- {agenda.afficher(l, fuseau)}" for l in retards]
        L.append("")
    dans_24 = [l for l in ordre if l["statut"] in ("prevu", "latent") and t <= agenda.instant(l) <= t + dt.timedelta(hours=24)]
    L.append(f"## Agenda : dans les 24 heures ({len(dans_24)})")
    L += [f"- {agenda.afficher(l, fuseau)}" for l in dans_24] or ["- rien"]
    suivants = [l for l in ordre if l["statut"] in ("prevu", "latent") and t + dt.timedelta(hours=24) < agenda.instant(l) <= t + dt.timedelta(days=7)]
    L.append(f"## Agenda : de J+1 à J+7 ({len(suivants)})")
    L += [f"- {agenda.afficher(l, fuseau)}" for l in suivants] or ["- rien"]
    L.append("(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)")
    L.append("")

    affaires = sorted({l["fait"] for l in savoir.lire() if l["fait"].startswith("affaire_")})
    L.append("## Affaires ouvertes (T4/T5 chaque dimanche soir)")
    for f in affaires:
        n = len(savoir.informes(f))
        inte, ext = savoir.pourcentages_t5(n)
        L.append(f"- {f} : {n} informé(s) hors William ; fuite interne {inte} %, externe {ext} %")
    L.append("")

    fin = t.date() + dt.timedelta(days=30)
    fetes = []
    for a in {t.year, fin.year}:
        for pays in ("ci", "lu", "cv"):
            for d, nom, approx in cal.fetes(a, pays):
                if t.date() <= d <= fin:
                    fetes.append((d, pays.upper(), nom, approx))
        deb, fi = cal.ramadan(a)
        if deb and t.date() <= deb <= fin:
            fetes.append((deb, "CI", "début du Ramadan", True))
    L.append("## Fêtes et fériés dans les 30 jours")
    L += [f"- {JOURS[d.weekday()][:3]} {d:%d/%m} {p} {'≈ ' if ap else ''}{nom}" for d, p, nom, ap in sorted(set(fetes))] or ["- aucun"]
    L.append("")

    demain = t.date() + dt.timedelta(days=1)
    rappels = []
    if t.weekday() == 6 or demain.weekday() == 0:
        rappels.append("lendemain = lundi : revue du lundi à présenter AVANT le reste (CLAUDE.md §12) ; dimanche soir : T4/T5 (savoir.py t5) et synthèse de semaine")
    if t.weekday() == 0:
        rappels.append("AUJOURD'HUI lundi : revue du lundi (audit_jets.py, tirage_aleas.py, vie hors d'Abidjan, monde, idées)")
    L.append("## Routine du tour")
    L += [f"- {r}" for r in rappels]
    L += ["- Début : `python outils/resume_etat.py`, `python outils/agenda.py dus --jusqua \"<heure de fin du tour>\"`, lecture des fichiers d'état concernés.",
          "- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14) ; fuseaux par `fuseaux.py` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.",
          "- Fin : `horloge.py --regler ...`, `agenda.py clore/ajouter/reporter`, journal, fils ouverts, WhatsApp, `chasse_tics.py --texte <brouillon>`, `controle_coherence.py`."]
    L.append("")

    journaux = sorted((RACINE / "journal").glob("*.md"))
    if journaux:
        dernier = journaux[-1]
        lignes_j = [x for x in dernier.read_text(encoding="utf-8").splitlines() if x.strip()]
        L.append(f"## Fin du dernier journal ({dernier.name}, 6 dernières lignes)")
        L += [f"> {x[:400]}" for x in lignes_j[-6:]]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sans-ecrire", action="store_true")
    args = ap.parse_args()
    texte = construire()
    if not args.sans_ecrire:
        SORTIE.write_bytes(texte.replace("\n", "\r\n").encode("utf-8"))
    print(texte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
