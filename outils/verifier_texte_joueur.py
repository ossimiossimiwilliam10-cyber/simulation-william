"""CONTRÔLE DU TEXTE MONTRÉ AU JOUEUR (créé le 28/10/2026, après l'audit du travail de Gemini du 22/07 au 05/08/2041).

Le texte d'un tour est lu par le joueur, qui ne doit y trouver QUE la fiction (CLAUDE.md §5) : ni identifiant du moteur, ni mécanisme caché,
ni événement tiré d'avance, ni journal de bord. Ce contrôle repère ce qui a fuité ; ce sont des AVERTISSEMENTS (code de sortie 0), lus par
`tour.py fin` juste après l'enregistrement du texte (« RELIRE (texte joueur) ») et par `controle_coherence.py` sur le dernier tour.

    python outils/verifier_texte_joueur.py --texte brouillon.md [--avance-heures 60]   # un brouillon de tour
    python outils/verifier_texte_joueur.py --dernier                                    # etat/dernier-tour.md
    python outils/verifier_texte_joueur.py --essai                                      # essai automatique

Contrôles :
1. identifiants internes : D038 (document), A106 / RA012 (agenda, réponses), (I1) (fil ouvert), (A09, …) (aléa), codes entre parenthèses ;
2. mécanismes cachés : « tirage hebdomadaire », « fuite interne », « escalade externe », T4/T5/T17, « jet 54 », « NON CONNU », etc. ;
3. événement tiré d'avance : un aléa « programmé », « tiré » ou « déclenché » dans le texte du joueur (les détails d'un aléa ne sont jamais annoncés) ;
4. format : en-tête en gras sur la première ligne (après une éventuelle ligne « 📌 Vraie vie »), pas de phrase de statut avant l'en-tête,
   blocs « Réponses attendues », « À faire / à fournir », « Quêtes secondaires », dernière ligne « Que veux-tu faire ? » ;
5. style : récit en liste de jours (« Le samedi 3 août… », « Le dimanche 4 août… »), discours structuré « Premièrement… Deuxièmement… » dans une réplique,
   avance de plus de 36 h dans un seul tour (à raconter d'un trait, en prose, sans journal jour par jour).
"""
import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
IDENTIFIANTS = [
    (r"\bD\d{3}\b", "identifiant de document « D… »"),
    (r"\bR?A\d{3}\b", "identifiant d'agenda ou de réponse « A… » / « RA… »"),
    (r"\((?:[A-Z]{1,2}\d{1,3})(?:\s*[,;)]|\s+clos)", "code du moteur entre parenthèses « (I1) », « (A003) », « (A09, … ) »"),
    (r"\bA\d{3}\s+clos\b|\bclos\s*\(A\d{2,3}\)", "« … clos » d'une ligne d'agenda"),
    (r"\bI\d{1,2}\b(?=\s*[,;)])", "numéro de fil ouvert « I… »"),
]
MECANISMES = [
    (r"tirages? (?:hebdomadaires?|de table|T\d|des? al[ée]as?)", "« tirage » (mécanisme)"),
    (r"fuites? internes?|escalades? externes?", "« fuite interne » / « escalade externe » (tables T4 et T5)"),
    (r"\bT(?:4|5|10|11|14|17|20|21|24)[ab-d]?\b", "table de pouvoir « Tn »"),
    (r"\bjets? (?:de )?\d", "un jet de dé"),
    (r"NON CONNU|connu=non", "marque d'agenda caché"),
    (r"tour du monde", "« tour du monde » (mécanisme)"),
    (r"contr[ôo]le de coh[ée]rence|chasse aux tics|tests? du moteur", "outil de contrôle du moteur"),
]
ALEA_ANNONCE = r"al[ée]as?[^.\n]{0,90}(?:programm|tir[ée]s?\b|d[ée]clench|pr[ée]vu)"
JOURS = r"(?:lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)"
EN_TETE = re.compile(r"^\*\*[A-ZÉÛÈÔ]+ \d{1,2}(?:er)? [A-ZÉÛÈÔ]+ \d{4} — \d{2}h\d{2} — .+\*\*\s*$")


def controle(texte, avance_heures=None):
    """-> liste d'avertissements (chaînes)."""
    av = []
    lignes = [l for l in texte.splitlines()]
    non_vides = [l for l in lignes if l.strip()]
    # format
    debut = 0
    if non_vides and non_vides[0].lstrip().startswith("📌"):
        debut = 1
    if len(non_vides) > debut:
        premiere = non_vides[debut].strip()
        if not EN_TETE.match(premiere):
            av.append(f"FORMAT : la première ligne du tour n'est pas l'en-tête en gras « **JOUR JJ MOIS 2041 — HHhMM — Lieu** » (trouvé : « {premiere[:70]} »)")
    else:
        av.append("FORMAT : texte vide ou sans en-tête")
    for bloc in ("Réponses attendues", "À faire / à fournir", "Quêtes secondaires"):
        if bloc.lower() not in texte.lower():
            av.append(f"FORMAT : bloc « {bloc} » absent")
    if non_vides and not non_vides[-1].strip().startswith("Que veux-tu faire"):
        av.append("FORMAT : la dernière ligne doit être « Que veux-tu faire ? »")
    # fuites
    for motif, libelle in IDENTIFIANTS:
        trouves = sorted({m.group(0).strip() for m in re.finditer(motif, texte)})
        if trouves:
            av.append(f"FUITE : {libelle} : {', '.join(trouves[:6])}")
    for motif, libelle in MECANISMES:
        trouves = sorted({m.group(0).strip() for m in re.finditer(motif, texte, flags=re.I)})
        if trouves:
            av.append(f"FUITE : {libelle} : {', '.join(trouves[:4])}")
    if re.search(ALEA_ANNONCE, texte, flags=re.I):
        av.append("FUITE : un aléa tiré est annoncé à l'avance dans le texte du joueur (les détails d'un aléa se jouent le jour dit, jamais avant)")
    # style
    jours = re.findall(rf"(?:^|\n)\s*[-*]*\s*\**Le {JOURS} \d{{1,2}} (?:juillet|août|septembre|octobre)", texte)
    if len(jours) >= 3:
        av.append(f"STYLE : récit en liste de jours ({len(jours)} paragraphes « Le <jour> <date>… ») : écrire en prose fluide, pas en journal")
    for m in re.finditer(r"«([^»]{300,})»", texte):
        if re.search(r"Premièrement", m.group(1)):
            av.append("STYLE : discours structuré « Premièrement… Deuxièmement… » dans une réplique (règle 5 : pas de long discours de principe)")
            break
    if avance_heures is not None and avance_heures > 36:
        av.append(f"STYLE : {avance_heures:.0f} h avancées dans un seul tour : raconter d'un trait, en prose, sans journal jour par jour ; s'arrêter plus tôt si un événement l'exige")
    return av


def texte_du_joueur(contenu):
    """Extrait la section « Texte envoyé au joueur » de etat/dernier-tour.md."""
    m = re.search(r"## Texte envoyé au joueur\s*\n(.*)", contenu, flags=re.S)
    return (m.group(1) if m else contenu).strip()


def essai():
    mauvais = ("Le tour commence.\n\n**LUNDI 5 AOÛT 2041 — 09h00 — Audun-le-Tiche, chez toi**\n\n"
               "Le vendredi 2 août tu travailles.\nLe samedi 3 août tu te reposes.\nLe dimanche 4 août tu cours.\n"
               "Le rapport (D038, A106 clos) confirme l'absence de fuite interne. Le tirage hebdomadaire signale un aléa A09 programmé jeudi.\n"
               "« " + "Premièrement, " + "x" * 320 + " »\n")
    bon = ("**LUNDI 5 AOÛT 2041 — 09h00 — Audun-le-Tiche, chez toi**\n\nLe café coule.\n\n---\n\n**Réponses attendues**\n- Personne.\n\n"
           "**À faire / à fournir avant le tour suivant**\n- Rien.\n\n**Quêtes secondaires**\n- Rien.\n\nQue veux-tu faire ?\n")
    a_mauvais = controle(mauvais, avance_heures=60)
    a_bon = controle(bon)
    attendus = ("FUITE : identifiant de document", "FUITE : identifiant d'agenda", "fuite interne", "aléa tiré", "récit en liste de jours", "Premièrement", "FORMAT : la première ligne", "FORMAT : bloc", "avancées")
    manquants = [a for a in attendus if not any(a in x for x in a_mauvais)]
    if manquants or a_bon:
        print("essai : ÉCHEC : manquants " + str(manquants) + " ; faux positifs " + str(a_bon))
        return 1
    print(f"essai : conforme ({len(a_mauvais)} avertissements sur le mauvais texte, 0 sur le bon)")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--texte", help="fichier texte d'un brouillon de tour")
    ap.add_argument("--dernier", action="store_true", help="etat/dernier-tour.md")
    ap.add_argument("--avance-heures", type=float, default=None)
    ap.add_argument("--essai", action="store_true")
    a = ap.parse_args()
    if a.essai:
        return essai()
    if a.texte:
        texte = Path(a.texte).read_text(encoding="utf-8")
        portee = Path(a.texte).name
    else:
        texte = texte_du_joueur((RACINE / "etat" / "dernier-tour.md").read_text(encoding="utf-8"))
        portee = "etat/dernier-tour.md"
    av = controle(texte, a.avance_heures)
    print(f"Texte du joueur : {portee}")
    for x in av:
        print("  RELIRE (texte joueur) :", x)
    print(f"  {len(av)} avertissement(s) (non bloquants).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
