"""Jet de dé du moteur — deux modes.

1. Jet à probabilité libre (événements non moraux : délais, friction administrative, livraisons…) :
       python outils/jet.py "Capitol : attestation prête à l'heure" 70
2. Tirage dans une TABLE DE POUVOIR (réaction d'un personnage à un acte de William, manœuvre de William, escalade,
   fuite). Les pourcentages sont lus dans `etat/modele-pouvoir.md` : le moteur ne les choisit pas.
       python outils/jet.py --table T1 --mod M02 "Grace : réaction 48 h au geste du 23/07 (collègue proche au QG)"
       python outils/jet.py --table T5 --informes 3 "Fuite de l'affaire : semaine du 30/07"
       python outils/jet.py --table T1 --blanc 20000     # statistiques à blanc, rien n'est consigné
       python outils/jet.py --liste                      # tables et modificateurs chargés, avec validation

Garde-fous (règle 17 de CLAUDE.md) :
- un jet libre dont le libellé décrit la réaction d'un subordonné (confidence, signalement, ultimatum, démission,
  interdiction, capture, soutien…) est REFUSÉ, sauf `--derogation "raison"` (consignée et auditée) ;
- 3 modificateurs au maximum par tirage, pris dans la liste fermée de `etat/modele-pouvoir.md` ;
- issues `frontal_*` plafonnées (10 % en table, 15 % après modificateurs, 40 % pour T4) ; `succes_net` plafonné dans les tables
  `[contentieux]` (35 % en table, 45 % après modificateurs) ; l'inaction (`rien_*`) doit peser au moins 15 % dans T1-T3.
Tout est consigné dans `memoire/tirages-aleas.md` (texte, lu par audit_jets.py) ET dans `memoire/tirages.jsonl` (une ligne JSON
par tirage, lue par la base de données) ; ne jamais rejouer un tirage. Depuis le 11/10/2026 : les essais `--simule` sont consignés
à part (`memoire/simulations.jsonl`) pour qu'aucun dé ne soit relancé en cachette ; `--pour "Nom"` rattache le tirage à un
personnage de `etat/personnages.csv` et REFUSE les tables T1, T1b et T9 pour un mineur (limite (b) du §11) ; la garde de la
règle 17 reconnaît aussi les RÔLES (« la voisine », « le directeur »…), pas seulement les noms des fiches.
Règle de friction administrative (CLAUDE.md §12) : jet « deuxième passage demandé » à 30 % pour toute démarche à enjeu.
Depuis le 14/10/2026 (univers vivant, simulation surtout informatique) : les autres outils tirent sans passer par la ligne de
commande, avec les mêmes garde-fous et la même consignation (`jet.tirer(...)`, `jet.tirer_libre(...)`) ; un SOUS-TIRAGE DE
PROCÉDURE (`--procedure "T21b/T10 : jour de la réponse tardive"`) applique une issue déjà tirée selon la règle écrite de la
table ou de l'outil (jour d'une réponse tardive, minute dans une fenêtre de disponibilité) : il n'est pas une dérogation, il est
consigné avec l'étiquette [PROCÉDURE : …] et compté à part par `audit_jets.py`.
"""
import argparse
import csv
import datetime as dt
import json
import random
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TABLES_MD = RACINE / "etat" / "modele-pouvoir.md"
JOURNAL = RACINE / "memoire" / "tirages-aleas.md"
JOURNAL_JSON = RACINE / "memoire" / "tirages.jsonl"
SIMULATIONS_JSON = RACINE / "memoire" / "simulations.jsonl"
PERSONNAGES_CSV = RACINE / "etat" / "personnages.csv"
TABLES_INTERDITES_MINEURS = ("T1", "T1b", "T9", "T17", "T20a", "T20b", "T21a", "T21b")
# T20a et T20b (12/10/2026) : la personne doit être nommée (--pour), inscrite, avec sa date de naissance, et majeure
# T17, T21a et T21b (12/10/2026, revue n° 1) : même garde (rencontre adulte, application de rencontre)
TABLES_ADULTE_VERIFIE = ("T17", "T20a", "T20b", "T21a", "T21b")
for flux in (sys.stdout, sys.stderr):
    if hasattr(flux, 'reconfigure'):
        flux.reconfigure(encoding='utf-8')

# Garde-fous, en %
PLAFOND_TABLE_FRONTAL = 10
PLAFOND_TIRAGE_FRONTAL = 15
PLAFOND_TABLE_SUCCES = 35
PLAFOND_TIRAGE_SUCCES = 45
PLANCHER_RIEN = 15
TABLES_REACTION = ("T1", "T2", "T3")
MAX_MODIFICATEURS = 3
FUITE_INTERNE = (3, 40)   # T5 : points par personne informée (William exclu), plafond
FUITE_EXTERNE = (1, 15)

def noms_personnages():
    """Noms des personnages récurrents de l'univers en cours (univers 2 depuis le 11/10/2026) : titres des fiches de
    `personnes/` (« # Prénom Nom — … ») et de `etat/vies-propres.md` (« ### Prénom Nom (…) »). Prénom et nom sont pris séparément."""
    noms = set()
    sources = list((RACINE / "personnes").glob("*.md"))
    vp = RACINE / "etat" / "vies-propres.md"
    for p in sources + ([vp] if vp.exists() else []):
        for ligne in p.read_text(encoding="utf-8").splitlines():
            if (p == vp and ligne.startswith("### ")) or (p != vp and ligne.startswith("# ")):
                titre = re.split(r"\s[—(-]\s?", ligne.lstrip("# ").strip())[0]
                noms.update(m for m in re.findall(r"[A-ZÀ-Ý][\wÀ-ÿ'-]{2,}", titre) if m not in ("Mme", "Me", "Dr", "Fiche"))
                if p != vp:
                    break
    return sorted(noms)


# Rôles reconnus par la garde de la règle 17 même sans fiche (univers 2 : collègues, voisins, inconnus, famille…), en plus des noms.
ROLES = ("collègue|directeur|directrice|direction|proviseur|secrétaire|voisin|voisine|parent d'élève|élève|inconnu|inconnue|"
         "serveur|serveuse|vendeur|vendeuse|banquier|banquière|conseiller|conseillère|propriétaire|médecin|coach|entraîneur|"
         "partenaire|copine|copain|petite amie|amie|ami|mère|père|frère|sœur|cousin|cousine|oncle|tante|ex|patron|patronne|chef|"
         "subordonné|subordonnée|stagiaire|policier|policière|gendarme|douanier|douanière|agent|employé|employée")
PERSONNAGES = "|".join(re.escape(n) for n in noms_personnages()) or "(?!)"
PERSONNES_OU_ROLES = (PERSONNAGES + "|" if noms_personnages() else "") + r"\b(?:" + ROLES + r")\b"
VERBES_REACTION = ("confie|informe|préviens|prévient|en parle|parle à|parlera|signale|dénonce|plainte|ultimatum|menace|"
                   "démission|quitte|interdit|exige|représailles|capture|sauvegarde|témoign|confronte|soutien|avocat|"
                   "Inspection|police|syndicat|réagit|réaction|se tait|raconte|avoue")
REACTION_LIBRE = re.compile(f"(?=.*(?:{PERSONNES_OU_ROLES}))(?=.*(?:{VERBES_REACTION}))", re.I | re.S)

ENTETE = re.compile(r"^###\s+(T\d+[a-z]?)\s+—\s+(.*)$")
PLAFOND_TAG = re.compile(r"\[plafond_frontal=(\d+)\]")
EFFET = re.compile(r"\s*([a-z_0-9]+)\s*([+-]\d+(?:[.,]\d+)?)\s*")


def charger(md=TABLES_MD):
    """Lit les tables et les modificateurs de `etat/modele-pouvoir.md`."""
    tables, modifs = {}, {}
    courant, section_modif = None, False
    for ligne in Path(md).read_text(encoding="utf-8").splitlines():
        if ligne.startswith("#"):
            m = ENTETE.match(ligne)
            if m:
                titre = m.group(2)
                p = PLAFOND_TAG.search(titre)
                courant, section_modif = m.group(1), False
                tables[courant] = {
                    "titre": titre, "issues": [],
                    "plafond_frontal": int(p.group(1)) if p else PLAFOND_TIRAGE_FRONTAL,
                    "contentieux": "[contentieux]" in titre,
                    "sans_tirage": "[sans_tirage]" in titre or "[formule]" in titre,
                }
            else:
                courant, section_modif = None, ligne.startswith("### Modificateurs")
            continue
        if not ligne.startswith("|"):
            continue
        cases = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if courant and len(cases) >= 2 and re.fullmatch(r"[a-z_0-9]+", cases[0]) \
                and re.fullmatch(r"\d+(?:[.,]\d+)?", cases[1]):
            tables[courant]["issues"].append((cases[0], float(cases[1].replace(",", ".")), cases[2] if len(cases) > 2 else ""))
        elif section_modif and len(cases) >= 4 and re.fullmatch(r"M\d{2}", cases[0]):
            effet = []
            for morceau in cases[2].split(";"):
                e = EFFET.fullmatch(morceau)
                if e:
                    effet.append((e.group(1), float(e.group(2).replace(",", "."))))
            modifs[cases[0]] = {"tables": [t.strip() for t in cases[1].split(",")], "effet": effet, "quand": cases[3]}
    return tables, modifs


def valider(tables, modifs):
    """Contrôle les tables : sommes, plafonds, inaction au menu, modificateurs équilibrés. Retourne la liste des erreurs."""
    erreurs = []
    for tid, t in tables.items():
        if t["sans_tirage"]:
            continue
        if not t["issues"]:
            erreurs.append(f"{tid} : aucune issue lue")
            continue
        codes = [c for c, _, _ in t["issues"]]
        total = sum(p for _, p, _ in t["issues"])
        if abs(total - 100) > 0.01:
            erreurs.append(f"{tid} : total {total:g} % (attendu 100)")
        if len(set(codes)) != len(codes):
            erreurs.append(f"{tid} : issue en double")
        frontal = sum(p for c, p, _ in t["issues"] if c.startswith("frontal_"))
        if frontal > PLAFOND_TABLE_FRONTAL:
            erreurs.append(f"{tid} : issues frontal_* à {frontal:g} % (plafond {PLAFOND_TABLE_FRONTAL} %)")
        if t["contentieux"]:
            net = sum(p for c, p, _ in t["issues"] if c == "succes_net")
            if net > PLAFOND_TABLE_SUCCES:
                erreurs.append(f"{tid} : succes_net à {net:g} % (plafond {PLAFOND_TABLE_SUCCES} %)")
        if tid in TABLES_REACTION:
            rien = sum(p for c, p, _ in t["issues"] if c.startswith("rien_"))
            if rien < PLANCHER_RIEN:
                erreurs.append(f"{tid} : l'inaction (rien_*) ne pèse que {rien:g} % (plancher {PLANCHER_RIEN} %)")
    for code, m in modifs.items():
        if not m["effet"]:
            erreurs.append(f"{code} : effet illisible")
        if abs(sum(d for _, d in m["effet"])) > 0.01:
            erreurs.append(f"{code} : effets non équilibrés (somme {sum(d for _, d in m['effet']):+g})")
        for tid in m["tables"]:
            if tid not in tables:
                erreurs.append(f"{code} : table inconnue {tid}")
                continue
            codes = {c for c, _, _ in tables[tid]["issues"]}
            for issue, _ in m["effet"]:
                if issue not in codes:
                    erreurs.append(f"{code} : l'issue {issue} n'existe pas dans {tid}")
    return erreurs


def distribution(args, tables, modifs):
    """Répartition finale (issues → %) après modificateurs, avec les plafonds de tirage."""
    tid = args.table
    if tid not in tables:
        sys.exit(f"Table inconnue : {tid} (connues : {', '.join(tables)})")
    t = tables[tid]
    if tid == "T5":
        if args.informes is None:
            sys.exit("T5 : préciser --informes N (nombre de personnes qui connaissent l'affaire, William exclu)")
        if args.mod:
            sys.exit("T5 n'accepte pas de modificateur")
        n = max(args.informes, 0)
        ext = float(min(FUITE_EXTERNE[1], FUITE_EXTERNE[0] * n))
        inte = float(min(FUITE_INTERNE[1], FUITE_INTERNE[0] * n))
        return {"fuite_externe": ext, "fuite_interne": inte, "aucune": 100.0 - ext - inte}
    if t["sans_tirage"]:
        sys.exit(f"{tid} : règles de rôle, pas de tirage (voir etat/modele-pouvoir.md)")
    issues = {c: p for c, p, _ in t["issues"]}
    if len(args.mod) > MAX_MODIFICATEURS:
        sys.exit(f"{MAX_MODIFICATEURS} modificateurs au maximum par tirage")
    if len(set(args.mod)) != len(args.mod):
        sys.exit("Un modificateur ne s'applique qu'une fois")
    for code in args.mod:
        m = modifs.get(code)
        if not m:
            sys.exit(f"Modificateur inconnu : {code}")
        if tid not in m["tables"]:
            sys.exit(f"{code} n'est pas autorisé pour {tid} (tables : {', '.join(m['tables'])})")
        for issue, delta in m["effet"]:
            issues[issue] += delta
    negatifs = [c for c, p in issues.items() if p < -1e-9]
    if negatifs:
        sys.exit(f"Modificateurs impossibles : {', '.join(negatifs)} passerait sous 0 % (en choisir d'autres)")
    frontal = sum(p for c, p in issues.items() if c.startswith("frontal_"))
    if frontal > t["plafond_frontal"] + 1e-9:
        sys.exit(f"Plafond dépassé : issues frontal_* à {frontal:g} % (maximum {t['plafond_frontal']} % pour {tid})")
    if t["contentieux"] and issues.get("succes_net", 0) > PLAFOND_TIRAGE_SUCCES + 1e-9:
        sys.exit(f"Plafond dépassé : succes_net à {issues['succes_net']:g} % (maximum {PLAFOND_TIRAGE_SUCCES} %)")
    return issues


def choisir(issues, jet):
    cumul, dernier = 0.0, None
    for code, p in issues.items():
        cumul += p
        if p > 0:
            dernier = code
        if jet < cumul:
            return code
    return dernier


def consigner(ligne):
    if not JOURNAL.exists():
        JOURNAL.write_text("# Journal des tirages d'aléas (ne jamais effacer, ne jamais rejouer)\n\n", encoding="utf-8")
    with JOURNAL.open("a", encoding="utf-8") as f:
        f.write(f"\n{ligne} (enregistré le {dt.datetime.now():%d/%m/%Y %H:%M} heure machine)\n")


def horloge_texte():
    """Heure simulée de etat/horloge.txt (« AAAA-MM-JJ HH:MM fuseau »), ou chaîne vide."""
    p = RACINE / "etat" / "horloge.txt"
    if not p.exists():
        return ""
    cles = dict(l.split(":", 1) for l in p.read_text(encoding="utf-8").splitlines() if ":" in l and not l.startswith("#"))
    return f"{cles.get('horloge', '').strip()} {cles.get('fuseau', '').strip()}".strip()


def consigner_json(objet, simule=False):
    """Une ligne JSON par tirage (memoire/tirages.jsonl) ; les essais --simule vont dans memoire/simulations.jsonl."""
    cible = SIMULATIONS_JSON if simule else JOURNAL_JSON
    maintenant = dt.datetime.now()
    o = {"id": f"{'S' if simule else 'J'}{maintenant:%Y%m%d%H%M%S%f}", "enregistre": maintenant.isoformat(timespec="seconds"),
         "horloge": horloge_texte(), "simule": simule}
    o.update(objet)
    with cible.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")


def fiche_personnage(nom):
    """Ligne de etat/personnages.csv (par nom complet, prénom, alias ou identifiant), ou None."""
    if not nom or not PERSONNAGES_CSV.exists():
        return None
    with PERSONNAGES_CSV.open(encoding="utf-8", newline="") as f:
        for l in csv.DictReader(f, delimiter=";"):
            noms = {l.get("id", ""), l.get("nom", ""), (l.get("nom") or " ").split()[0]}
            noms |= {a.strip() for a in (l.get("alias") or "").split(",") if a.strip()}
            if nom.strip().lower() in {x.lower() for x in noms if x}:
                return l
    return None


def est_mineur(fiche):
    """True si le personnage a moins de 18 ans à l'horloge (date de naissance dans etat/personnages.csv)."""
    if not fiche or not fiche.get("naissance"):
        return False
    h = horloge_texte()
    try:
        jour = dt.date.fromisoformat(h[:10]) if h else dt.date.today()
        n = dt.date.fromisoformat(fiche["naissance"])
    except ValueError:
        return False
    return (jour.year - n.year - ((jour.month, jour.day) < (n.month, n.day))) < 18


def garde_pour(args):
    """Contrôle --pour : personnage connu ; tables relationnelles interdites pour un mineur ; pour T20a et T20b, personne
    obligatoirement nommée, inscrite, datée et majeure. Renvoie la fiche (ou None)."""
    table = args.table or ""
    if table in TABLES_ADULTE_VERIFIE and not getattr(args, "pour", None):
        sys.exit(f"REFUSÉ : la table {table} exige --pour \"Nom\" (une adulte inscrite dans etat/personnages.csv avec sa date de "
                 "naissance : personnage.py nouveau d'abord).")
    if not getattr(args, "pour", None):
        return None
    fiche = fiche_personnage(args.pour)
    if fiche is None:
        if table in TABLES_ADULTE_VERIFIE:
            sys.exit(f"REFUSÉ : « {args.pour} » n'est pas dans etat/personnages.csv : âge invérifiable (personnage.py nouveau d'abord).")
        print(f"(avertissement : « {args.pour} » n'a pas de ligne dans etat/personnages.csv ; personnage.py nouveau, s'il est récurrent)")
        return None
    if table in TABLES_ADULTE_VERIFIE and not fiche.get("naissance"):
        sys.exit(f"REFUSÉ : {fiche.get('nom')} n'a pas de date de naissance : âge invérifiable (§11, limite b).")
    if est_mineur(fiche) and (args.table or "") in TABLES_INTERDITES_MINEURS:
        sys.exit(f"REFUSÉ (§11, limite b) : {fiche.get('nom')} est mineur(e) ; les tables {', '.join(TABLES_INTERDITES_MINEURS)} "
                 "ne s'appliquent jamais à un mineur. Aucune scène sexuelle, romantique ou sexualisée avec un mineur.")
    return fiche


def _tirer_table(args, tables, modifs, texte=True):
    """Tire une issue (garde-fous compris), la consigne (sauf --simule) et renvoie le résultat ; n'affiche rien."""
    issues = distribution(args, tables, modifs)
    tid = args.table
    if not args.libelle:
        sys.exit("Libellé obligatoire : jet.py --table Tn [--mod Mxx] \"personnage : situation\"")
    fiche = garde_pour(args)
    jet = random.SystemRandom().uniform(0, 100)
    issue = choisir(issues, jet)
    repartition = " / ".join(f"{c} {p:g}" for c, p in issues.items())
    mods = ", ".join(args.mod) if args.mod else "aucun"
    ligne = f"- Tirage [{tid}] « {args.libelle} » : {repartition} ; modificateurs : {mods} ; jet {jet:5.1f} → **{issue}**"
    scene = next((s for c, _, s in tables[tid]["issues"] if c == issue), "")
    objet = {"mode": "table", "table": tid, "libelle": args.libelle, "pour": (fiche or {}).get("nom", args.pour or ""),
             "modificateurs": args.mod, "distribution": issues, "jet": round(jet, 2), "issue": issue}
    if not args.simule and texte:
        consigner(ligne)
    consigner_json(objet, simule=args.simule)
    return {"issue": issue, "jet": round(jet, 2), "distribution": issues, "ligne": ligne, "scene": scene,
            "pour": (fiche or {}).get("nom", args.pour or "")}


def tirer(table, mods=(), libelle="", pour=None, simule=False, informes=None, texte=True):
    """Tirage dans une table depuis un autre outil (14/10/2026) : mêmes garde-fous et même consignation que la ligne de
    commande. Renvoie {issue, jet, distribution, ligne, scene, pour}. Une garde non respectée lève SystemExit.
    texte=False : tirage de masse du monde vivant (journées des personnages), consigné seulement dans memoire/tirages.jsonl
    et dans etat/vies.csv, pour ne pas noyer le journal lisible des tirages."""
    global _CACHE
    if _CACHE is None:
        _CACHE = charger()
    tables, modifs = _CACHE
    args = argparse.Namespace(table=table, mod=list(mods), libelle=libelle, pour=pour, simule=simule, informes=informes,
                              blanc=None, derogation=None, procedure=None, proba=None, liste=False)
    return _tirer_table(args, tables, modifs, texte=texte)


_CACHE = None


def tirage_table(args, tables, modifs):
    issues = distribution(args, tables, modifs)
    tid = args.table
    rng = random.SystemRandom()
    if args.blanc:
        compte = {c: 0 for c in issues}
        for _ in range(args.blanc):
            compte[choisir(issues, rng.uniform(0, 100))] += 1
        print(f"[{tid}] {args.blanc} tirages à blanc (rien n'est consigné)")
        for c, p in issues.items():
            print(f"  {c:26s} attendu {p:5.1f} %   observé {100 * compte[c] / args.blanc:5.1f} %")
        return 0
    r = _tirer_table(args, tables, modifs)
    print(r["ligne"])
    if r["scene"]:
        print(f"En scène : {r['scene']}")
    print("Règle 17 : sentiments libres, actes tirés ; test d'intérêt ; test de la phrase ; l'issue banale peut clore la scène.")
    return 0


def _jet_libre(args):
    """Jet libre (garde-fous compris), consigné sauf --simule ; renvoie {oui, jet, ligne} sans rien afficher."""
    if not args.libelle or args.proba is None:
        sys.exit("Usage : jet.py \"libellé\" proba   |   jet.py --table Tn [--mod Mxx] \"libellé\"   |   jet.py --liste")
    procedure = getattr(args, "procedure", None)
    if REACTION_LIBRE.search(args.libelle) and not args.derogation and not procedure and not args.simule:
        sys.exit("REFUSÉ (règle 17) : ce libellé décrit la réaction d'un personnage à un acte de William. Tirer dans une table "
                 "(--table Tn ; etat/modele-pouvoir.md), appliquer une issue déjà tirée (--procedure \"règle\") ou justifier une "
                 "exception (--derogation \"raison\", consignée et auditée).")
    garde_pour(args)
    jet = random.SystemRandom().uniform(0, 100)
    oui = jet < args.proba
    ligne = f"- Jet « {args.libelle} » : probabilité {args.proba:g} %, jet {jet:5.1f} → **{'OUI' if oui else 'NON'}**"
    if args.derogation:
        ligne += f" [DÉROGATION : {args.derogation}]"
    if procedure:
        ligne += f" [PROCÉDURE : {procedure}]"
    if not args.simule:
        consigner(ligne)
    consigner_json({"mode": "libre", "libelle": args.libelle, "pour": args.pour or "", "proba": args.proba, "jet": round(jet, 2),
                    "issue": "OUI" if oui else "NON", "derogation": args.derogation or "", "procedure": procedure or ""},
                   simule=args.simule)
    return {"oui": oui, "jet": round(jet, 2), "ligne": ligne}


def tirer_libre(libelle, proba, pour=None, procedure=None, derogation=None, simule=False):
    """Jet libre depuis un autre outil (14/10/2026). `procedure` : sous-tirage qui applique une issue déjà tirée selon une
    règle écrite (jour d'une réponse tardive, minute dans une fenêtre de disponibilité) ; renvoie {oui, jet, ligne}."""
    args = argparse.Namespace(libelle=libelle, proba=float(proba), pour=pour, procedure=procedure, derogation=derogation,
                              simule=simule, table=None, mod=[], informes=None, blanc=None, liste=False)
    return _jet_libre(args)


def jet_libre(args):
    if not args.libelle or args.proba is None:
        sys.exit("Usage : jet.py \"libellé\" proba   |   jet.py --table Tn [--mod Mxx] \"libellé\"   |   jet.py --liste")
    if REACTION_LIBRE.search(args.libelle) and not args.derogation and not getattr(args, "procedure", None) and not args.simule:
        sys.exit("REFUSÉ (règle 17) : ce libellé décrit la réaction d'un personnage à un acte de William. Tirer dans une table "
                 "(--table T1, T1b, T2, T3, T4, T5, T7a, T7b, T7c, T7d, T8, T9, T10, T11, T12, T13a-d, T14, T20a-b ; etat/modele-pouvoir.md) ou justifier une exception avec "
                 "--derogation \"raison\" (consignée et auditée).")
    r = _jet_libre(args)
    print(r["ligne"])
    return 0


def afficher(tables, modifs):
    for tid, t in tables.items():
        etiquette = " (sans tirage)" if t["sans_tirage"] else ""
        print(f"{tid} — {t['titre']}{etiquette}")
        for c, p, _ in t["issues"]:
            print(f"    {c:26s} {p:5.1f} %")
    print(f"\n{len(modifs)} modificateurs : " + ", ".join(f"{c} ({'/'.join(m['tables'])})" for c, m in modifs.items()))
    print(f"T5 (formule) : interne {FUITE_INTERNE[0]} pt/personne (plafond {FUITE_INTERNE[1]} %), "
          f"externe {FUITE_EXTERNE[0]} pt/personne (plafond {FUITE_EXTERNE[1]} %)")


def main():
    ap = argparse.ArgumentParser(description="Jet de dé du moteur (probabilité libre ou table de pouvoir)")
    ap.add_argument("libelle", nargs="?")
    ap.add_argument("proba", nargs="?", type=float, help="probabilité de OUI, en %% (jet libre)")
    ap.add_argument("--table", help="table de pouvoir : T1, T1b, T2, T3, T4, T5, T7a, T7b, T7c, T7d, T8, T9, T10 (délais), T11 (vie propre), T12 (négociation), T13a-d (contenu T11), T14 (initiatives), T20a-b (proposition d'argent à une adulte, avec --pour)")
    ap.add_argument("--mod", action="append", default=[], help="modificateur (M01…), 3 au maximum")
    ap.add_argument("--informes", type=int, help="T5 : personnes qui connaissent l'affaire, William exclu")
    ap.add_argument("--derogation", help="justification d'un jet libre portant sur une réaction (consignée, auditée)")
    ap.add_argument("--procedure", help="sous-tirage qui applique une issue déjà tirée selon une règle écrite (jour d'une réponse "
                    "tardive, minute dans une fenêtre de disponibilité) : consigné [PROCÉDURE : …], compté à part par l'audit")
    ap.add_argument("--simule", action="store_true",
                    help="essai : rien dans le journal des tirages (trace dans memoire/simulations.jsonl)")
    ap.add_argument("--pour", help="personnage concerné (etat/personnages.csv) : garde « mineurs » et rattachement du tirage")
    ap.add_argument("--blanc", type=int, help="statistiques à blanc sur N tirages (rien n'est consigné)")
    ap.add_argument("--liste", action="store_true", help="affiche et valide les tables et modificateurs")
    args = ap.parse_args()
    tables, modifs = charger()
    if args.liste:
        afficher(tables, modifs)
        erreurs = valider(tables, modifs)
        for e in erreurs:
            print("ERREUR", e)
        print("Validation :", "des erreurs à corriger" if erreurs else "tables et modificateurs conformes")
        return 1 if erreurs else 0
    if args.table:
        return tirage_table(args, tables, modifs)
    return jet_libre(args)


if __name__ == "__main__":
    sys.exit(main())
