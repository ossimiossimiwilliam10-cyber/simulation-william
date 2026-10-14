"""ACTUALITÉS DE LA SEMAINE (créé le 14/10/2026, demande de l'utilisateur : un univers « vivant », « indépendant », et une
simulation « surtout informatique ») : la section hebdomadaire de `etat/monde.md` (règle du monde vivant : trois à cinq nouvelles
par semaine) s'écrit seule, UNE fois, dès que l'horloge passe le lundi (`tour.py fin`), jamais rejouée.

    python outils/actualites.py semaine [--lundi AAAA-MM-JJ] [--ecrire]     # aperçu (ou écriture) de la section de la semaine
    python outils/actualites.py verifier

Sources de la section, dans l'ordre : événements publics de la semaine (`donnees/evenements.csv`), jours fériés (calendrier_2040),
tempêtes de la saison (`etat/tropiques.csv`, si William est aux Philippines), cours du peso (`etat/taux.csv`), puis nouvelles tirées
dans `donnees/actualites-modeles.csv` (pays où se trouve William d'abord, puis Luxembourg ou Lorraine) jusqu'à cinq lignes.
Les nouvelles ne nomment aucune personne réelle ; les chiffres viennent des intervalles des modèles (tirage consigné). Le moteur
s'en sert comme fond (télévision du hall, une de journal, conversation) ; il ne les montre que si William peut les voir ou entendre.
"""
import argparse
import datetime as dt
import random
import re
import sys

from commun import DONNEES, ETAT, OUTILS, lire_csv, lire_texte, ecrire_texte, maintenant_simule, utf8

sys.path.insert(0, str(OUTILS))
MODELES = DONNEES / "actualites-modeles.csv"
EVENEMENTS = DONNEES / "evenements.csv"
MONDE = ETAT / "monde.md"
NOMS_PAYS = {"ph": "Philippines (Manille)", "lu": "Luxembourg", "fr": "Lorraine (Audun-le-Tiche, Moselle)"}


def pays_de_william():
    import meteo
    return "ph" if meteo.station_courante() == "manille" else "lu"


def lundi_de(jour):
    return jour - dt.timedelta(days=jour.weekday())


def titre(lundi):
    dim = lundi + dt.timedelta(days=6)
    return f"## Semaine du {lundi.day} au {dim.day}/{dim:%m}/{dim.year}" if lundi.month == dim.month else \
        f"## Semaine du {lundi.day}/{lundi:%m} au {dim.day}/{dim:%m}/{dim.year}"


def deja(lundi):
    dim = lundi + dt.timedelta(days=6)
    return bool(re.search(rf"Semaine du 0?{lundi.day}(?:/{lundi:%m})? au 0?{dim.day}/{dim:%m}", lire_texte(MONDE)))


def _remplir(modele, variables, rng):
    valeurs = {}
    for v in [x for x in variables.split("&") if x.strip()]:
        nom, _, spec = v.partition("=")
        if ".." in spec:
            borne, _, dec = spec.partition(":")
            a, b = (float(x) for x in borne.split(".."))
            n = rng.uniform(a, b)
            d = int(dec or 0)
            valeurs[nom.strip()] = (f"{n:.{d}f}" if d else str(round(n))).replace(".", ",")
        else:
            valeurs[nom.strip()] = rng.choice(spec.split("|"))
    return modele.format(**valeurs)


def semaine(lundi, rng=None, tirer=False):
    """Lignes « - **Pays** : nouvelle » de la semaine (sans rien écrire ; `tirer` : taux du peso tirés s'ils manquent)."""
    import calendrier_2040 as cal
    rng = rng or random.SystemRandom()
    dim = lundi + dt.timedelta(days=6)
    ici = pays_de_william()
    ordre = [ici] + [p for p in ("lu", "fr") if p != ici]
    lignes, tires = [], []
    for e in lire_csv(EVENEMENTS):
        if e["pays"] in ordre and e["debut"] <= dim.isoformat() and e["fin"] >= lundi.isoformat():
            d = dt.date.fromisoformat(e["debut"])
            lignes.append((ordre.index(e["pays"]), f"- **{NOMS_PAYS.get(e['pays'], e['pays'])}** : {e['evenement']} ({d:%d/%m})."))
    for p in ordre:
        for d, nom, _ in cal.fetes(lundi.year, p):
            if lundi <= d <= dim:
                lignes.append((ordre.index(p), f"- **{NOMS_PAYS[p]}** : {d:%d/%m}, {nom} (jour férié)."))
    if ici == "ph":
        import tropiques
        for l in tropiques.lire():
            if not l["id"].startswith("TC") or l["effet"] == "passee":
                continue
            entree = l["entree_par"]
            if entree and lundi.isoformat() <= entree <= dim.isoformat():
                quoi = ("pluies de mousson renforcées sur Metro Manila" if l["effet"] == "mousson" else
                        f"signal n° {l['signal']} hissé sur Metro Manila" if l["signal"] else "sans effet attendu sur Metro Manila")
                lignes.append((0, f"- **{NOMS_PAYS['ph']}** : la PAGASA suit la tempête « {l['nom']} », entrée dans la zone de responsabilité "
                                  f"des Philippines le {dt.date.fromisoformat(entree):%d/%m} ({quoi})."))
        import devises
        lire_taux = devises.taux if tirer else (lambda j, c: devises.taux_connu(c, j))
        avant, apres = lire_taux(lundi - dt.timedelta(days=8), "PHP"), lire_taux(lundi - dt.timedelta(days=1), "PHP")
        sens = "s'affaiblit" if apres > avant else "se raffermit" if apres < avant else "ne bouge pas"
        v = lambda x: f"{x:.2f}".replace(".", ",")  # noqa: E731
        lignes.append((0, f"- **{NOMS_PAYS['ph']}** : sur la semaine écoulée, le peso {sens} face à l'euro : {v(apres)} PHP pour 1 € "
                          f"le dimanche {lundi - dt.timedelta(days=1):%d/%m}, contre {v(avant)} une semaine plus tôt."))
    modeles = [m for m in lire_csv(MODELES) if m["mois"] == "tous" or str(lundi.month) in m["mois"].split(",")]
    # au moins une nouvelle de chez William (Luxembourg ou Lorraine) quand il est ailleurs ; cinq lignes au plus
    maison = 1 if ici == "ph" else 0
    for p, n in ((ici, 2), (ordre[1], 1), (ordre[2], 1)):
        candidats = [m for m in modeles if m["pays"] == p]
        for _ in range(n):
            reserve = maison if p == ici else 0
            if not candidats or len(lignes) >= 5 - reserve:
                break
            m = rng.choices(candidats, weights=[float(x["poids"]) for x in candidats])[0]
            candidats.remove(m)
            texte = _remplir(m["modele"], m["variables"], rng)
            tires.append(m["id"])
            lignes.append((ordre.index(p), f"- **{NOMS_PAYS[p]}** : {texte}."))
    lignes.sort(key=lambda x: x[0])
    return [l for _, l in lignes[:6]], tires


def ecrire_semaine(lundi):
    if deja(lundi):
        return None
    lignes, tires = semaine(lundi, tirer=True)
    section = "\n".join([titre(lundi)] + lignes + [f"- *(écrit par outils/actualites.py le {dt.datetime.now():%d/%m/%Y} heure machine ; "
                                                     f"modèles tirés : {', '.join(tires) or 'aucun'} ; une nouvelle datée n'est connue qu'à sa date)*"])
    texte = lire_texte(MONDE).rstrip("\n") + "\n\n" + section + "\n"
    ecrire_texte(MONDE, texte)
    import jet
    jet.consigner(f"- Actualités de la semaine du {lundi:%d/%m/%Y} : modèles {', '.join(tires) or 'aucun'} [PROCÉDURE : outils/actualites.py]")
    jet.consigner_json({"mode": "procedure", "libelle": f"Actualités de la semaine du {lundi:%d/%m/%Y}", "valeur": ", ".join(tires),
                        "regle": "actualites.py"})
    return section


def assurer(jour):
    """Écrit la section de la semaine de `jour` si l'horloge a passé son lundi et qu'elle manque. Renvoie des messages."""
    lundi = lundi_de(jour)
    s = ecrire_semaine(lundi)
    return [f"actualités : section « {titre(lundi)[3:]} » écrite dans etat/monde.md"] if s else []


def verifier():
    erreurs = []
    for m in lire_csv(MODELES):
        if m["pays"] not in NOMS_PAYS:
            erreurs.append(f"actualites-modeles.csv : pays inconnu ({m['id']})")
        try:
            _remplir(m["modele"], m["variables"], random.Random(0))
        except (KeyError, ValueError, IndexError) as e:
            erreurs.append(f"actualites-modeles.csv : modèle illisible ({m['id']} : {e})")
    return erreurs


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("semaine")
    s.add_argument("--lundi")
    s.add_argument("--ecrire", action="store_true")
    sub.add_parser("verifier")
    a = ap.parse_args()
    if a.cmd == "semaine":
        lundi = dt.date.fromisoformat(a.lundi) if a.lundi else lundi_de(maintenant_simule().date())
        if a.ecrire:
            s = ecrire_semaine(lundi)
            print(s or f"{titre(lundi)[3:]} : déjà écrite (jamais rejouée)")
        else:
            lignes, tires = semaine(lundi, random.Random(f"apercu-{lundi}"))
            print(titre(lundi) + "  (APERÇU : rien d'écrit ; l'écriture tirera de nouveau)")
            print("\n".join(lignes))
    elif a.cmd == "verifier":
        e = verifier()
        print("\n".join(e) if e else "actualités : OK")
        return 1 if e else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
