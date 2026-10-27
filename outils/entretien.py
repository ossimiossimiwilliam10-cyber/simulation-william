"""ENTRETIENS DU PÔLE RH VIRTUEL (créé le 27/10/2026) : un message de l'agent à un candidat, sa réaction TIRÉE, son heure, et tout l'enregistrement.

Avant : pour chaque message, quatre commandes à la main (jet T17, reactions.py delai, ligne d'agenda, fiche) : source d'oublis pour un moteur moins
puissant. Maintenant, une commande :

    python outils/entretien.py envoyer --pour "Cédric Soro" --canal facebook --quand "2041-07-20 14:00" --texte "Bonjour Monsieur Soro, …"
    python outils/entretien.py repondre A047 --texte "Bonsoir, merci pour votre message …"     # joue la réponse prévue (canal de l'agent : rien de visible)

`envoyer` : tire T17 (`jet.py --table T17 --pour`), puis, sauf « ignore », programme la réponse (`reactions.py delai`, heure T10 selon la routine du candidat),
inscrit le message envoyé dans l'agenda (NON CONNU de William) et dans la fiche du candidat. Le texte suit la règle I30 : humain, signé « L'équipe du projet »,
jamais de nom de William, jamais de numéro de téléphone, aucun envoi entre 23h et 7h chez le destinataire (l'outil refuse).
`repondre` : `reactions.py jouer` (aucune conversation visible pour un canal de l'agent) et la ligne dans la fiche.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
FUSEAU_CANAL = {"abidjan": 0, "luxembourg": 2}  # décalage par rapport à Abidjan (UTC+0) : Luxembourg est en avance de 2 h en été
RESUME = {
    "poli_bref": "réponse polie et brève",
    "conversation": "réponse détaillée qui engage la conversation",
    "mefiance": "réponse prudente : il ou elle demande qui porte le projet, quelle société, quelles garanties",
    "refus_net": "refus net, sans discours",
    "reciproque": "réponse chaleureuse, intérêt réel, propose un échange",
    "calcul": "réponse intéressée par l'avantage (argent, statut)",
}


def sans_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def slug(nom):
    return re.sub(r"[^a-z0-9]+", "-", sans_accents(nom).lower()).strip("-")


def lancer(*args):
    r = subprocess.run([sys.executable, *args], capture_output=True, text=True, encoding="utf-8", cwd=str(RACINE))
    if r.returncode:
        sys.exit((r.stderr or r.stdout).strip())
    return r.stdout.strip()


def fiche_ajouter(nom, ligne):
    p = RACINE / "personnes" / f"{slug(nom)}.md"
    if p.is_file():
        b = p.read_bytes().decode("utf-8")
        crlf = "\r\n" in b
        t = b.replace("\r\n", "\n").rstrip("\n") + "\n" + ligne + "\n"
        p.write_bytes((t.replace("\n", "\r\n") if crlf else t).encode("utf-8"))


def envoyer(nom, canal, quand, texte, heure_locale_decalage):
    instant = dt.datetime.strptime(quand, "%Y-%m-%d %H:%M")
    locale = instant - dt.timedelta(hours=heure_locale_decalage)
    if locale.hour >= 23 or locale.hour < 7:
        sys.exit(f"Refusé (I30) : {quand} serait {locale:%H:%M} chez le destinataire ; aucun envoi entre 23h et 7h.")
    for interdit in ("William Ossimi", "Ossimi", "intelligence artificielle", "assistant virtuel", " IA "):
        if interdit.lower() in texte.lower():
            sys.exit(f"Refusé (I22 et I30) : le texte contient « {interdit} ».")
    if re.search(r"\+?\d[\d .]{8,}", texte):
        sys.exit("Refusé (I27) : le texte contient un numéro de téléphone.")
    lancer("outils/jet.py", "--table", "T17", "--pour", nom, f"{nom} face au message de l'agent IA du {quand} ({texte[:60]}…)")
    derniere = json.loads(Path(RACINE / "memoire" / "tirages.jsonl").read_text(encoding="utf-8").strip().splitlines()[-1])
    issue = derniere.get("issue") or derniere.get("resultat")
    # journal du message envoyé (agenda, NON CONNU de William)
    lancer("outils/agenda.py", "ajouter", "--date", quand[:10], "--heure", quand[11:], "--lieu", "luxembourg", "--qui", "Claude (pôle RH virtuel)", "--connu", "non", "--statut", "fait",
           "--quoi", f"Message de l'agent à {nom} ({canal}) : « {texte[:200]} » ; relu par le directeur général virtuel ; T17 : {issue}",
           "--note", "I30 : humain, signé « L'équipe du projet »")
    fiche_ajouter(nom, f"- {quand[8:10]}/{quand[5:7]}/{quand[:4]}, {quand[11:]} : message de l'agent IA (T17 : {issue}) : « {texte} »")
    if issue == "ignore":
        print(json.dumps({"pour": nom, "T17": issue, "reponse": None}, ensure_ascii=False))
        return
    resume = f"réponse de {nom} au message de l'agent du {quand} (T17 : {issue}) : {RESUME.get(issue, issue)}"
    sortie = lancer("outils/reactions.py", "delai", "--pour", nom, "--quand", quand, "--canal", canal, "--resume", resume)
    print(sortie)


def repondre(aid, texte):
    print(lancer("outils/reactions.py", "jouer", aid, "--texte", texte))
    sys.path.insert(0, str(RACINE / "outils"))
    import agenda
    l = next((x for x in agenda.lire() if x["id"] == aid), None)
    if l:
        m = re.search(r"reaction pour=([a-z0-9-]+)", l["note"])
        if m:
            p = RACINE / "personnes" / f"{m.group(1)}.md"
            if p.is_file():
                nom = re.search(r"^# (.+?) —", p.read_text(encoding="utf-8"), re.M)
                fiche_ajouter(nom.group(1) if nom else m.group(1), f"- {l['date'][8:10]}/{l['date'][5:7]}/{l['date'][:4]}, {l['heure']} : sa réponse à l'agent IA : « {texte} »")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    e = sp.add_parser("envoyer")
    e.add_argument("--pour", required=True)
    e.add_argument("--canal", required=True)
    e.add_argument("--quand", required=True, help="AAAA-MM-JJ HH:MM, heure de Luxembourg")
    e.add_argument("--texte", required=True)
    e.add_argument("--decalage", type=int, default=0, help="heures À RETRANCHER de l'heure de Luxembourg pour avoir l'heure du destinataire (Abidjan : 2 ; Atlanta : 6 ; Paris : 0)")
    r = sp.add_parser("repondre")
    r.add_argument("id")
    r.add_argument("--texte", required=True)
    a = ap.parse_args()
    if a.cmd == "envoyer":
        envoyer(a.pour, a.canal, a.quand, a.texte, a.decalage)
    else:
        repondre(a.id, a.texte)


if __name__ == "__main__":
    main()
