"""BASE DE DONNÉES DU MONDE (SQLite), créée le 11/10/2026 à la demande de l'utilisateur (« mettre en place un système de bases de
données »). Elle rassemble en un seul endroit interrogeable TOUT l'état de la simulation : horloge, agenda, grand livre, qui sait
quoi, personnages, relations, lieux, faits vérifiés, prix, climat, météo tirée, corps de William, échéancier, fronts, journal,
messages, textes des tours, tirages, pièces PDF.

    python outils/base.py construire                  # (re)construit sorties/monde.sqlite à partir des fichiers (≈ 1 s)
    python outils/base.py requete "SELECT * FROM v_agenda_a_venir"      # SQL en lecture seule
    python outils/base.py requete "SELECT nom, age, mineur FROM v_personnages" --format csv
    python outils/base.py cherche "boulangerie dimanche"                 # recherche plein texte, accents ignorés
    python outils/base.py cherche "Rui" --source messages,journal
    python outils/base.py schema | vues | etat
    python outils/base.py verifier                    # intégrité croisée (intégré à controle_coherence.py)

POURQUOI une base RECONSTRUITE et non une base « source » : la vérité reste dans des fichiers texte (CSV « ; », Markdown, JSONL)
versionnés par git. (1) Git compare et fusionne des lignes de texte, jamais un fichier binaire : deux sessions parallèles restent
visibles et réparables. (2) Tout agent, même sans Python, peut lire et corriger les fichiers. (3) La base n'est qu'un index :
on peut la supprimer à tout moment, `construire` la refait à l'identique. Elle est ignorée par git (`sorties/`).
Les commandes `requete` et `cherche` reconstruisent la base d'elles-mêmes si un fichier source a changé.
"""
import argparse
import csv
import datetime as dt
import io
import json
import re
import sqlite3
import sys

from commun import DONNEES, ETAT, JOURNAL, MEMOIRE, OUTILS, RACINE, SORTIES, lire_csv, lire_texte, utf8

sys.path.insert(0, str(OUTILS))
BASE = SORTIES / "monde.sqlite"
SOURCES_CSV = {
    # table : (fichier, colonnes numériques)
    "agenda": (ETAT / "agenda.csv", ()),
    "savoir": (ETAT / "savoir.csv", ()),
    "personnages": (ETAT / "personnages.csv", ()),
    "relations": (ETAT / "relations.csv", ("affinite", "confiance", "tension", "familiarite_h", "attirance", "dette")),
    "meteo": (ETAT / "meteo.csv", ("tmin", "tmax", "pluie_mm", "soleil_h")),
    "corps": (ETAT / "corps.csv", ("valeur",)),
    "echeancier": (ETAT / "echeancier.csv", ("montant",)),
    "fronts": (ETAT / "fronts.csv", ("segments", "rempli")),
    "lieux": (DONNEES / "lieux.csv", ()),
    "ambiances": (DONNEES / "ambiances.csv", ()),
    "faits": (DONNEES / "faits.csv", ()),
    "prix": (DONNEES / "prix.csv", ("prix_2026", "coef")),
    "evenements_publics": (DONNEES / "evenements.csv", ()),
    "calendrier_scolaire": (DONNEES / "calendrier-scolaire.csv", ()),
    "delais": (DONNEES / "delais.csv", ("min", "habituel", "max", "proba_survenue")),
}
# colonnes des tables quand le fichier n'existe pas encore (début d'univers) : les vues et les contrôles restent valides
DEFAUTS = {
    "agenda": ["id", "date", "heure", "lieu", "qui", "quoi", "statut", "connu", "note"],
    "savoir": ["fait", "personne", "canal", "date", "note"],
    "personnages": ["id", "nom", "alias", "sexe", "naissance", "nationalite", "origine", "langues", "langue_avec_william", "registre",
                    "commune", "metier", "employeur", "role", "contexte", "cercle", "statut", "fiche", "cree_le", "traits", "notes"],
    "relations": ["de", "vers", "niveau", "affinite", "confiance", "tension", "familiarite_h", "attirance", "dette",
                  "dernier_contact", "note"],
    "meteo": ["date", "type", "tmin", "tmax", "pluie_mm", "orage", "soleil_h", "brouillard", "description", "anomalie", "tire_le"],
    "corps": ["date", "heure", "type", "valeur", "unite", "note"],
    "echeancier": ["id", "libelle", "compte", "montant", "periodicite", "jour", "mois", "heure", "debut", "fin", "statut", "source",
                   "note"],
    "fronts": ["id", "nom", "type", "segments", "rempli", "visibilite", "avance", "paliers", "echeance", "liens", "statut",
               "historique"],
    "lieux": ["id", "nom", "type", "commune", "pays", "fuseau", "horaires", "feries", "acces", "prix", "statut", "notes", "source",
              "verifie_le"],
    "ambiances": ["lieu", "saison", "moment", "detail", "dernier_usage"],
    "faits": ["id", "pays", "domaine", "enonce", "valeur", "source", "date_verif", "fiabilite", "projection_2040", "valable_jusqua"],
    "prix": ["id", "article", "lieu", "pays", "categorie", "prix_2026", "unite", "source", "date_releve", "fiabilite", "coef", "note"],
    "evenements_publics": ["debut", "fin", "lieu", "pays", "evenement", "type", "source", "fiabilite", "note"],
    "calendrier_scolaire": ["pays", "zone", "annee_scolaire", "periode", "debut", "fin", "source", "statut"],
    "delais": ["type", "description", "min", "habituel", "max", "unite", "proba_survenue", "source", "verifie_le"],
}
VUES = {
    "v_agenda_a_venir": ("Échéances prévues ou latentes après l'horloge (connues ou non de William)",
                         "SELECT a.* FROM agenda a, horloge h WHERE a.statut IN ('prevu','latent') AND a.instant_utc >= h.instant_utc "
                         "ORDER BY a.instant_utc"),
    "v_agenda_connu": ("Ce que William sait de son agenda (pour le joueur et le téléphone)",
                       "SELECT * FROM v_agenda_a_venir WHERE connu = 'oui'"),
    "v_retards": ("Échéances échues non closes (règle 14)",
                  "SELECT a.* FROM agenda a, horloge h WHERE a.statut = 'prevu' AND a.instant_utc < h.instant_utc ORDER BY a.instant_utc"),
    "v_prevus": ("Mouvements d'argent attendus (grand livre, type prevu)",
                 "SELECT * FROM grand_livre WHERE type = 'prevu' ORDER BY horodatage"),
    "v_personnages": ("Personnages avec âge à l'horloge et marqueur de minorité",
                      "SELECT p.*, CAST((julianday(substr(h.instant_local,1,10)) - julianday(p.naissance)) / 365.2425 AS INTEGER) AS age, "
                      "CASE WHEN p.naissance != '' AND (julianday(substr(h.instant_local,1,10)) - julianday(p.naissance)) / 365.2425 < 18 "
                      "THEN 'oui' ELSE 'non' END AS mineur FROM personnages p, horloge h"),
    "v_qui_sait": ("Qui sait quoi, avec le statut du personnage",
                   "SELECT s.fait, s.personne, s.canal, s.date, s.note, p.role, p.statut FROM savoir s "
                   "LEFT JOIN personnages p ON p.nom = s.personne ORDER BY s.fait, s.date"),
    "v_messages": ("Messages écrits (whatsapp/), dans l'ordre", "SELECT * FROM messages ORDER BY date, heure, ligne"),
    "v_journal": ("Lignes horodatées des journaux", "SELECT * FROM journal ORDER BY date, ligne"),
    "v_meteo": ("Météo tirée, jour par jour", "SELECT * FROM meteo ORDER BY date"),
    "v_tirages": ("Tirages structurés (memoire/tirages.jsonl)", "SELECT * FROM tirages ORDER BY enregistre"),
    "v_documents": ("Pièces PDF reçues ou gardées par William", "SELECT dossier, fichier, date, objet FROM documents ORDER BY date"),
}


# ---------------------------------------------------------------- utilitaires
def sources():
    """Tous les fichiers qui alimentent la base (pour l'empreinte)."""
    fichiers = [ETAT / "horloge.txt", ETAT / "grand-livre.csv", MEMOIRE / "tirages.jsonl", MEMOIRE / "tirages-aleas.md",
                DONNEES / "climat-findel.csv"]
    fichiers += [f for f, _ in SOURCES_CSV.values()]
    for motif in ("journal/*.md", "journal/tours/*.md", "whatsapp/*.md", "personnes/*.md", "etat/*.md", "memoire/*.md",
                  "courriels/*.pdf", "documents_william/*.pdf"):
        fichiers += sorted(RACINE.glob(motif))
    return [f for f in fichiers if f.exists()]


def signature():
    morceaux = []
    for f in sources():
        s = f.stat()
        morceaux.append(f"{f.relative_to(RACINE)}:{s.st_size}:{int(s.st_mtime)}")
    import hashlib
    return hashlib.sha1("\n".join(morceaux).encode()).hexdigest()[:16]


def nombre(x):
    try:
        return float(str(x).replace(",", ".")) if str(x).strip() != "" else None
    except ValueError:
        return None


def creer_table(cx, nom, colonnes, lignes, numeriques=()):
    cols = [re.sub(r"\W", "_", c) or "col" for c in colonnes]
    defs = ", ".join(f'"{c}" {"REAL" if c in numeriques else "TEXT"}' for c in cols)
    cx.execute(f'CREATE TABLE "{nom}" ({defs})')
    if lignes:
        marques = ", ".join("?" for _ in cols)
        cx.executemany(f'INSERT INTO "{nom}" VALUES ({marques})',
                       [[nombre(l.get(c)) if c in numeriques else l.get(o, "") for c, o in zip(cols, colonnes)] for l in lignes])


def colonnes_de(chemin, defaut=("id",)):
    if not chemin.exists():
        return list(defaut)
    with chemin.open(encoding="utf-8", newline="") as f:
        return next(csv.reader(f, delimiter=";"), list(defaut))


# ---------------------------------------------------------------- analyse des fichiers Markdown
LIGNE_JOURNAL = re.compile(r"^\s*-\s+\*\*(\d{1,2})h(\d{2})(?:\s*[-–]\s*\d{1,2}h\d{2})?(?:\s*\(([^)]*)\))?\*\*\s*:?\s*(.*)$")
LIGNE_MESSAGE = re.compile(r"^\*\*\[(\d{2})/(\d{2})/(\d{4})\s*-\s*(\d{1,2}):(\d{2})(?:\s*\(([^)]*)\))?\]\s*([^:*]+?)\s*:\*\*\s*(.*)$")


def lire_journaux():
    res = []
    for p in sorted(JOURNAL.glob("*.md")):
        try:
            d = dt.date.fromisoformat(p.stem)
        except ValueError:
            continue
        for n, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            m = LIGNE_JOURNAL.match(ligne)
            if m:
                res.append({"date": d.isoformat(), "heure": f"{int(m.group(1)):02d}:{m.group(2)}", "lieu": m.group(3) or "",
                            "texte": m.group(4).strip(), "fichier": p.name, "ligne": n})
    return res


def lire_tours():
    """journal/tours/AAAA-MM-JJ.md : sections « ## Tour n° N — HHhMM »."""
    res = []
    for p in sorted((JOURNAL / "tours").glob("*.md")):
        texte = p.read_text(encoding="utf-8")
        for m in re.finditer(r"^## Tour n° (\d+)[^\n]*?(\d{1,2})h(\d{2})[^\n]*\n(.*?)(?=^## Tour n° |\Z)", texte, re.S | re.M):
            corps = m.group(4)
            joueur = re.search(r"### Message du joueur\s*\n(.*?)(?=^### |\Z)", corps, re.S | re.M)
            envoye = re.search(r"### Texte envoyé au joueur\s*\n(.*?)(?=^### |\Z)", corps, re.S | re.M)
            res.append({"date": p.stem, "numero": int(m.group(1)), "heure": f"{int(m.group(2)):02d}:{m.group(3)}",
                        "message_joueur": (joueur.group(1).strip() if joueur else ""),
                        "texte": (envoye.group(1).strip() if envoye else corps.strip()), "fichier": p.name})
    return res


def lire_messages():
    res = []
    for p in sorted((RACINE / "whatsapp").glob("*.md")):
        if p.name.upper().startswith("LISEZMOI"):
            continue
        courant = None
        for n, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            m = LIGNE_MESSAGE.match(ligne.strip())
            if m:
                j, mo, a, hh, mi, lieu, auteur, texte = m.groups()
                courant = {"conversation": p.stem, "date": f"{a}-{mo}-{j}", "heure": f"{int(hh):02d}:{mi}", "lieu": lieu or "",
                           "auteur": auteur.strip(), "texte": texte.strip(), "fichier": p.name, "ligne": n}
                res.append(courant)
            elif courant and ligne.strip() and not ligne.startswith("#"):
                courant["texte"] += "\n" + ligne.strip()
    return res


def lire_fiches():
    res = []
    for p in sorted((RACINE / "personnes").glob("*.md")):
        if p.name.upper().startswith("LISEZMOI"):
            continue
        t = p.read_text(encoding="utf-8")
        titre = next((l.lstrip("# ").strip() for l in t.splitlines() if l.startswith("# ")), p.stem)
        res.append({"fichier": p.name, "titre": titre, "texte": t})
    return res


def lire_documents():
    res = []
    try:
        from pypdf import PdfReader
    except ImportError:
        PdfReader = None
    for dossier in ("courriels", "documents_william"):
        for p in sorted((RACINE / dossier).glob("*.pdf")):
            m = re.match(r"(\d{4}-\d{2}-\d{2})_(.*)", p.stem)
            texte = ""
            if PdfReader:
                try:
                    texte = "\n".join((pg.extract_text() or "") for pg in PdfReader(str(p)).pages)
                except Exception:  # noqa: BLE001
                    texte = ""
            res.append({"dossier": dossier, "fichier": p.name, "date": m.group(1) if m else "",
                        "objet": (m.group(2) if m else p.stem).replace("_", " "), "texte": texte})
    return res


def lire_tirages_jsonl():
    res = []
    for n, ligne in enumerate(lire_texte(MEMOIRE / "tirages.jsonl").splitlines(), 1):
        if not ligne.strip():
            continue
        try:
            o = json.loads(ligne)
        except json.JSONDecodeError:
            continue
        o.setdefault("ligne", n)
        res.append(o)
    return res


# ---------------------------------------------------------------- construction
def construire(silencieux=False):
    import agenda as ag
    import grand_livre as gl
    import horloge as hl
    SORTIES.mkdir(parents=True, exist_ok=True)
    tmp = BASE.with_suffix(".tmp")
    if tmp.exists():
        tmp.unlink()
    cx = sqlite3.connect(str(tmp))
    cx.execute("PRAGMA journal_mode = OFF")
    # horloge
    h = hl.lire()
    t = h["instant"]
    utc = t.astimezone(dt.timezone.utc)
    cx.execute("CREATE TABLE horloge (instant_local TEXT, fuseau TEXT, lieu TEXT, tour INTEGER, instant_utc TEXT)")
    cx.execute("INSERT INTO horloge VALUES (?,?,?,?,?)", (f"{t:%Y-%m-%d %H:%M}", h["fuseau"], h["lieu"], h.get("tour", 0),
                                                          f"{utc:%Y-%m-%d %H:%M}"))
    cx.execute("CREATE TABLE attentes (texte TEXT)")
    cx.executemany("INSERT INTO attentes VALUES (?)", [(a,) for a in h["attentes"]])
    # CSV simples
    for table, (fichier, num) in SOURCES_CSV.items():
        lignes = lire_csv(fichier)
        cols = colonnes_de(fichier) if fichier.exists() else DEFAUTS.get(table, ["vide"])
        if table == "agenda":
            cols = cols + ["instant_utc", "jour_semaine"]
            for l in lignes:
                try:
                    i = ag.instant(l).astimezone(dt.timezone.utc)
                    l["instant_utc"] = f"{i:%Y-%m-%d %H:%M}"
                    l["jour_semaine"] = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"][
                        dt.date.fromisoformat(l["date"]).weekday()]
                except (SystemExit, ValueError):
                    l["instant_utc"], l["jour_semaine"] = "", ""
        creer_table(cx, table, cols, lignes, num)
    # grand livre, comptes, soldes
    gll = gl.lire()
    for n, l in enumerate(gll, 2):
        l["n"] = n
        l["horodatage"] = f"{l['date']} {l['heure'] or '12:00'}"
    creer_table(cx, "grand_livre", ["n", "date", "heure", "compte", "montant", "type", "libelle", "reference", "horodatage"],
                gll, ("montant", "n"))
    cx.execute("CREATE TABLE comptes (compte TEXT PRIMARY KEY, proprietaire TEXT, devise TEXT, description TEXT, patrimoine INTEGER)")
    cx.executemany("INSERT INTO comptes VALUES (?,?,?,?,?)", [(c, *v[:3], int(v[3])) for c, v in gl.COMPTES.items()])
    s = gl.soldes(t.replace(tzinfo=None))
    cx.execute("CREATE TABLE soldes (compte TEXT, solde REAL, au TEXT)")
    cx.executemany("INSERT INTO soldes VALUES (?,?,?)", [(c, v, f"{t:%Y-%m-%d %H:%M}") for c, v in s.items()])
    # climat (format long)
    cx.execute("CREATE TABLE climat (parametre TEXT, unite TEXT, description TEXT, mois INTEGER, valeur REAL, source TEXT)")
    mois_cols = ["jan", "fev", "mar", "avr", "mai", "juin", "juil", "aout", "sep", "oct", "nov", "dec"]
    for l in lire_csv(DONNEES / "climat-findel.csv"):
        for i, mc in enumerate(mois_cols, 1):
            cx.execute("INSERT INTO climat VALUES (?,?,?,?,?,?)", (l.get("parametre"), l.get("unite"), l.get("description"), i,
                                                                    nombre(l.get(mc)), l.get("source")))
    # Markdown analysés
    creer_table(cx, "journal", ["date", "heure", "lieu", "texte", "fichier", "ligne"], lire_journaux())
    creer_table(cx, "tours", ["date", "numero", "heure", "message_joueur", "texte", "fichier"], lire_tours())
    creer_table(cx, "messages", ["conversation", "date", "heure", "lieu", "auteur", "texte", "fichier", "ligne"], lire_messages())
    fiches = lire_fiches()
    creer_table(cx, "fiches", ["fichier", "titre", "texte"], fiches)
    docs = lire_documents()
    creer_table(cx, "documents", ["dossier", "fichier", "date", "objet", "texte"], docs)
    tir = lire_tirages_jsonl()
    cles = ["id", "enregistre", "horloge", "mode", "table", "libelle", "pour", "modificateurs", "distribution", "jet", "issue",
            "proba", "derogation", "simule", "ligne"]
    for o in tir:
        for k in ("modificateurs", "distribution"):
            if isinstance(o.get(k), (list, dict)):
                o[k] = json.dumps(o[k], ensure_ascii=False)
    creer_table(cx, "tirages", cles, tir, ("jet", "proba"))
    # anciens tirages (texte libre), via audit_jets
    try:
        import audit_jets
        herites, tirages_md, libres = audit_jets.analyser()
        anciens = [{"ligne": x["ligne"], "type": "table", "table": x["table"], "libelle": x["libelle"], "issue": x["issue"],
                    "proba": ""} for x in tirages_md]
        anciens += [{"ligne": x["ligne"], "type": "libre", "table": "", "libelle": x["libelle"],
                     "issue": "OUI" if x["oui"] else "NON", "proba": x["proba"]} for x in herites + libres]
    except Exception:  # noqa: BLE001
        anciens = []
    creer_table(cx, "tirages_md", ["ligne", "type", "table", "libelle", "issue", "proba"], anciens, ("proba",))
    # recherche plein texte (accents ignorés)
    cx.execute("CREATE VIRTUAL TABLE recherche USING fts5(source, ref, date, texte, tokenize = 'unicode61 remove_diacritics 2')")
    lignes_fts = []
    lignes_fts += [("journal", f"{l['fichier']}:{l['ligne']}", l["date"], f"{l['heure']} {l['texte']}") for l in lire_journaux()]
    lignes_fts += [("messages", f"{m['fichier']}:{m['ligne']}", m["date"], f"{m['auteur']} : {m['texte']}") for m in lire_messages()]
    lignes_fts += [("tours", f"{x['fichier']} tour {x['numero']}", x["date"], x["message_joueur"] + "\n" + x["texte"]) for x in lire_tours()]
    lignes_fts += [("fiches", f["fichier"], "", f["texte"]) for f in fiches]
    lignes_fts += [("documents", d["fichier"], d["date"], d["objet"] + "\n" + d["texte"]) for d in docs]
    for l in lire_csv(DONNEES / "faits.csv"):
        lignes_fts.append(("faits", l.get("id", ""), l.get("date_verif", ""), " ".join(str(v) for v in l.values())))
    for l in lire_csv(DONNEES / "lieux.csv"):
        lignes_fts.append(("lieux", l.get("id", ""), "", " ".join(str(v) for v in l.values())))
    for dossier in ("etat", "memoire"):
        for p in sorted((RACINE / dossier).glob("*.md")):
            for n, bloc in enumerate(re.split(r"\n(?=## )", p.read_text(encoding="utf-8"))):
                lignes_fts.append((dossier, f"{p.name}§{n}", "", bloc))
    cx.executemany("INSERT INTO recherche VALUES (?,?,?,?)", lignes_fts)
    # vues
    for nom, (_, sql) in VUES.items():
        cx.execute(f"CREATE VIEW {nom} AS {sql}")
    cx.execute("CREATE TABLE meta (cle TEXT PRIMARY KEY, valeur TEXT)")
    cx.executemany("INSERT INTO meta VALUES (?,?)", [("signature", signature()),
                                                     ("construite", dt.datetime.now().isoformat(timespec="seconds")),
                                                     ("horloge", f"{t:%Y-%m-%d %H:%M}")])
    cx.commit()
    cx.close()
    if BASE.exists():
        BASE.unlink()
    tmp.rename(BASE)
    if not silencieux:
        print(f"Base reconstruite : {BASE.relative_to(RACINE)} ({len(lignes_fts)} entrées de recherche ; horloge {t:%d/%m/%Y %H:%M})")
    return BASE


def ouvrir(lecture_seule=True):
    """Connexion à la base, reconstruite d'abord si un fichier source a changé."""
    a_jour = False
    if BASE.exists():
        try:
            cx = sqlite3.connect(f"file:{BASE.as_posix()}?mode=ro", uri=True)
            a_jour = cx.execute("SELECT valeur FROM meta WHERE cle='signature'").fetchone()[0] == signature()
            cx.close()
        except sqlite3.Error:
            a_jour = False
    if not a_jour:
        construire(silencieux=True)
    if lecture_seule:
        return sqlite3.connect(f"file:{BASE.as_posix()}?mode=ro", uri=True)
    return sqlite3.connect(str(BASE))


def afficher(curseur, fmt="table", large=False):
    noms = [d[0] for d in curseur.description] if curseur.description else []
    lignes = curseur.fetchall()
    if fmt == "csv":
        out = io.StringIO()
        w = csv.writer(out, delimiter=";", lineterminator="\n")
        w.writerow(noms)
        w.writerows(lignes)
        print(out.getvalue(), end="")
        return len(lignes)
    if fmt == "json":
        print(json.dumps([dict(zip(noms, l)) for l in lignes], ensure_ascii=False, indent=1))
        return len(lignes)
    maxi = 400 if large else 60
    cellules = [[("" if v is None else str(v)).replace("\n", " ⏎ ")[:maxi] for v in l] for l in lignes]
    largeurs = [max([len(n)] + [len(c[i]) for c in cellules]) for i, n in enumerate(noms)]
    print(" | ".join(n.ljust(w) for n, w in zip(noms, largeurs)))
    print("-+-".join("-" * w for w in largeurs))
    for c in cellules:
        print(" | ".join(x.ljust(w) for x, w in zip(c, largeurs)))
    print(f"({len(lignes)} ligne(s))")
    return len(lignes)


# ---------------------------------------------------------------- vérification croisée
def verifier():
    """(erreurs, avertissements) : intégrité entre les tables. Intégré à controle_coherence.py."""
    erreurs, aver = [], []
    cx = ouvrir()
    q = lambda sql: cx.execute(sql).fetchall()  # noqa: E731
    horloge_utc, horloge_loc = q("SELECT instant_utc, instant_local FROM horloge")[0]
    # personnages
    ids = q("SELECT id, nom, naissance, statut, fiche FROM personnages")
    vus = set()
    for pid, nom, naiss, statut, fiche in ids:
        if pid in vus:
            erreurs.append(f"personnages.csv : identifiant en double {pid}")
        vus.add(pid)
        if naiss:
            try:
                dt.date.fromisoformat(naiss)
            except ValueError:
                erreurs.append(f"personnages.csv : date de naissance illisible pour {nom} ({naiss})")
        else:
            aver.append(f"personnages.csv : {nom} sans date de naissance (garde « mineurs » impossible)")
        if statut == "recurrent" and fiche and not (RACINE / fiche).exists():
            aver.append(f"personnages.csv : fiche absente pour {nom} ({fiche})")
    noms = {n for _, n, *_ in ids} | {"William"}
    alias = set()
    for (a,) in q("SELECT alias FROM personnages"):
        alias |= {x.strip() for x in (a or "").split(",") if x.strip()}
    prenoms = {n.split()[0] for n in noms if n}
    connus = noms | alias | prenoms
    # relations
    for de, vers in q("SELECT de, vers FROM relations"):
        for x in (de, vers):
            if x not in connus:
                erreurs.append(f"relations.csv : personne inconnue « {x} » (absente de etat/personnages.csv)")
    # savoir
    for (p,) in q("SELECT DISTINCT personne FROM savoir"):
        if p not in connus and not p.startswith("proche_de_") and not p.startswith("inconnu"):
            aver.append(f"savoir.csv : « {p} » n'est pas dans etat/personnages.csv")
    # messages : auteurs connus
    for (a,) in q("SELECT DISTINCT auteur FROM messages"):
        if a not in connus and a.split()[0] not in prenoms and a != "William":
            aver.append(f"whatsapp/ : auteur « {a} » absent de etat/personnages.csv")
    # météo : continuité
    dates = [dt.date.fromisoformat(d) for (d,) in q("SELECT date FROM meteo ORDER BY date")]
    for a, b in zip(dates, dates[1:]):
        if (b - a).days != 1:
            erreurs.append(f"meteo.csv : trou ou doublon entre le {a} et le {b}")
    # corps : rien après l'horloge
    for d, hre, typ in q("SELECT date, heure, type FROM corps"):
        if f"{d} {hre or '00:00'}" > horloge_loc:
            erreurs.append(f"corps.csv : entrée datée après l'horloge ({d} {hre} {typ})")
    # journal : ordre chronologique dans chaque fichier
    for fichier, in q("SELECT DISTINCT fichier FROM journal"):
        heures = q(f"SELECT heure, ligne FROM journal WHERE fichier = '{fichier}' ORDER BY ligne")
        for (h1, l1), (h2, l2) in zip(heures, heures[1:]):
            if h2 < h1:
                aver.append(f"journal/{fichier}:{l2} heure {h2} après {h1} (ligne {l1}) : ordre chronologique ?")
    # échéancier
    for eid, comp, statut in q("SELECT id, compte, statut FROM echeancier"):
        if statut not in ("actif", "a_valider", "suspendu", "termine"):
            erreurs.append(f"echeancier.csv : statut inconnu « {statut} » ({eid})")
        if comp not in {c for (c,) in q("SELECT compte FROM comptes")}:
            erreurs.append(f"echeancier.csv : compte inconnu « {comp} » ({eid})")
    # fronts
    for fid, seg, rempli in q("SELECT id, segments, rempli FROM fronts"):
        if seg is not None and rempli is not None and rempli > seg:
            erreurs.append(f"fronts.csv : {fid} rempli ({rempli:g}) > segments ({seg:g})")
    cx.close()
    return erreurs, aver


# ---------------------------------------------------------------- commandes
def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("construire")
    p.add_argument("--silencieux", action="store_true")
    p = sp.add_parser("requete")
    p.add_argument("sql")
    p.add_argument("--format", choices=("table", "csv", "json"), default="table")
    p.add_argument("--large", action="store_true", help="cellules longues non tronquées")
    p = sp.add_parser("cherche")
    p.add_argument("mots")
    p.add_argument("--source", help="journal, messages, tours, fiches, documents, faits, lieux, etat, memoire (séparés par des virgules)")
    p.add_argument("--limite", type=int, default=20)
    sp.add_parser("schema")
    sp.add_parser("vues")
    sp.add_parser("etat")
    sp.add_parser("verifier")
    args = ap.parse_args()
    if args.cmd == "construire":
        construire(args.silencieux)
        return 0
    if args.cmd == "requete":
        if re.match(r"\s*(insert|update|delete|drop|alter|create|replace|attach|pragma)\b", args.sql, re.I):
            sys.exit("Lecture seule : la base se reconstruit depuis les fichiers ; modifier les fichiers sources (outils dédiés).")
        cx = ouvrir()
        try:
            afficher(cx.execute(args.sql), args.format, args.large)
        except sqlite3.Error as e:
            sys.exit(f"Erreur SQL : {e}")
        return 0
    if args.cmd == "cherche":
        cx = ouvrir()
        mots = " ".join(f'"{m}"*' if not re.search(r'[*"]', m) else m for m in args.mots.split())
        sql = ("SELECT source, ref, date, snippet(recherche, 3, '[', ']', ' … ', 18) FROM recherche WHERE recherche MATCH ? ")
        params = [mots]
        if args.source:
            srcs = [s.strip() for s in args.source.split(",")]
            sql += f"AND source IN ({','.join('?' for _ in srcs)}) "
            params += srcs
        sql += "ORDER BY rank LIMIT ?"
        params.append(args.limite)
        try:
            lignes = cx.execute(sql, params).fetchall()
        except sqlite3.Error as e:
            sys.exit(f"Recherche impossible : {e}")
        for src, ref, date, extrait in lignes:
            print(f"[{src}] {ref} {date} : {extrait}")
        print(f"({len(lignes)} résultat(s))")
        return 0
    if args.cmd == "schema":
        cx = ouvrir()
        for nom, typ in cx.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table','view') AND name NOT LIKE "
                                   "'recherche_%' ORDER BY type, name"):
            cols = [r[1] for r in cx.execute(f'PRAGMA table_info("{nom}")')]
            print(f"{typ:5s} {nom} : {', '.join(cols)}")
        return 0
    if args.cmd == "vues":
        for nom, (desc, _) in VUES.items():
            print(f"{nom:20s} {desc}")
        return 0
    if args.cmd == "etat":
        cx = ouvrir()
        for (nom,) in cx.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'recherche%' ORDER BY name"):
            n = cx.execute(f'SELECT COUNT(*) FROM "{nom}"').fetchone()[0]
            print(f"{nom:22s} {n:6d} ligne(s)")
        print("construite le", cx.execute("SELECT valeur FROM meta WHERE cle='construite'").fetchone()[0])
        return 0
    if args.cmd == "verifier":
        err, aver = verifier()
        for e in err:
            print("ERREUR", e)
        for a in aver:
            print("RELIRE", a)
        print("Base :", "cohérente" if not err else "incohérences à corriger", f"({len(aver)} avertissement(s))")
        return 1 if err else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
