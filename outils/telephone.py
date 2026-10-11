"""TÉLÉPHONE DE WILLIAM (créé le 11/10/2026) : une page HTML autonome qui montre ce que l'écran du téléphone de William
afficherait à l'heure de l'horloge : messages, courriels reçus, banque, agenda, météo. Pensée pour le joueur, qui joue parfois
depuis son propre téléphone : il « ouvre son téléphone » au lieu de relire le récit.

    python outils/telephone.py                 # écrit sorties/telephone/index.html (+ telephone.json) et contrôle la page
    python outils/telephone.py --json          # affiche seulement les données

STRICTEMENT ce que William sait : jamais une ligne d'agenda « connu = non », jamais un tirage, une table, un modificateur, une
note du moteur, un fait caché ; seulement les mouvements d'argent déjà passés ; la météo vue sous forme de PRÉVISION. Un contrôle
automatique refuse d'écrire la page si un mot du moteur s'y glisse (tirage, jet, T1…T14, M01…, « non connu »…).
Publication : Claude peut publier le fichier comme page privée (outil Artifact, toujours au même endroit) ; tout autre agent
peut ouvrir le fichier localement ou l'envoyer au joueur. Aucun nom de marque (banque, messagerie) n'apparaît.
"""
import argparse
import datetime as dt
import json
import re
import sys

from commun import ETAT, OUTILS, RACINE, SORTIES, JOURS, MOIS, ecrire_texte, lire_csv, utf8

sys.path.insert(0, str(OUTILS))
INTERDITS = re.compile(r"\btirage|\bjet\b|\bjets\b|\bT\d{1,2}[a-d]?\b|\bM\d{2}\b|non connu|NON CONNU|moteur|dérogation|projection|"
                       r"modificateur|connu=non|\bE\d{3}-\d{8}\b|fait caché|secret_", re.I)
COMPTES_VISIBLES = {"courant": "Compte courant", "projet": "Épargne « Projet »"}


def jour_court(d):
    return f"{JOURS[d.weekday()][:3]}. {d.day} {MOIS[d.month - 1][:4].rstrip('.')}{'.' if len(MOIS[d.month - 1]) > 4 else ''}"


def donnees():
    import agenda
    import base
    import calendrier_2040 as cal
    import grand_livre as gl
    import horloge
    import meteo
    h = horloge.lire()
    t = h["instant"]
    naif = t.replace(tzinfo=None)
    jour = t.date()
    reseau = "LU" if re.search(r"luxembourg|esch|belval|findel|lux\b", h["lieu"], re.I) else "FR"
    # messages
    convs = {}
    for m in base.lire_messages():
        if f"{m['date']} {m['heure']}" > f"{naif:%Y-%m-%d %H:%M}":
            continue
        convs.setdefault(m["conversation"], []).append({"date": m["date"], "heure": m["heure"], "auteur": m["auteur"],
                                                        "texte": m["texte"], "moi": m["auteur"].split()[0] == "William"})
    conversations = sorted(({"nom": k.replace("_", " ").replace("-", " ").title(), "messages": v} for k, v in convs.items()),
                           key=lambda c: c["messages"][-1]["date"] + c["messages"][-1]["heure"], reverse=True)
    # courriels
    courriels = [{"date": d["date"], "objet": d["objet"][:1].upper() + d["objet"][1:], "fichier": d["fichier"]}
                 for d in base.lire_documents() if d["dossier"] == "courriels" and d["date"] <= jour.isoformat()]
    courriels.sort(key=lambda c: c["date"], reverse=True)
    # banque
    soldes = gl.soldes(naif)
    mouvements = [l for l in sorted(gl.lire(), key=gl.quand, reverse=True)
                  if l["type"] in ("mouvement", "prevu_realise") and gl.quand(l) <= naif and l["compte"] in COMPTES_VISIBLES]
    banque = {"comptes": [{"nom": n, "solde": round(soldes.get(c, 0.0), 2)} for c, n in COMPTES_VISIBLES.items()],
              "placements": round(soldes.get("etf", 0.0), 2),
              "operations": [{"date": l["date"], "libelle": re.sub(r"\s*\(.*?\)\s*$", "", l["libelle"]).strip(),
                              "montant": float(l["montant"]), "compte": COMPTES_VISIBLES[l["compte"]]} for l in mouvements[:40]]}
    # agenda (connu de William, hors fiction exclu) + fériés + événements publics
    evts = []
    for l in agenda.lire():
        if l["connu"] != "oui" or l["statut"] not in ("prevu", "latent") or "moteur" in l["qui"].lower():
            continue
        i = agenda.instant(l).astimezone(t.tzinfo)
        if i >= t:
            titre = re.sub(r"\s*\((?:projection|estimation)[^)]*\)", "", l["quoi"].split(" ; ")[0]).strip()
            evts.append({"date": i.date().isoformat(), "heure": f"{i:%H:%M}" if l["heure"] else "", "titre": titre, "type": "rdv"})
    fin = jour + dt.timedelta(days=75)
    for pays, nom_pays in (("fr", "France"), ("lu", "Luxembourg")):
        for annee in {jour.year, fin.year}:
            for d, nom, approx in cal.fetes(annee, pays):
                if jour <= d <= fin:
                    evts.append({"date": d.isoformat(), "heure": "", "titre": f"{nom.split(' (')[0]} (férié, {nom_pays})", "type": "ferie"})
    for e in cal.lire_donnees("evenements.csv"):
        if e["type"] in ("festival", "foire", "commerce") and jour.isoformat() <= e["debut"] <= fin.isoformat():
            evts.append({"date": e["debut"], "heure": "", "titre": e["evenement"].split(" : ")[0].split(",")[0], "type": "public"})
    evts.sort(key=lambda e: (e["date"], e["heure"]))
    # météo vue par William
    vraie = meteo.assurer(jour + dt.timedelta(days=4))[jour.isoformat()]
    maintenant_c = round(meteo.temperature_a(vraie, naif))
    previsions = []
    for i in range(0, 4):
        p = meteo.prevision(jour + dt.timedelta(days=i), jour)
        previsions.append({"jour": "Aujourd'hui" if i == 0 else "Demain" if i == 1 else JOURS[(jour + dt.timedelta(days=i)).weekday()].capitalize(),
                           "ciel": p["ciel"], "min": p["tmin"], "max": p["tmax"], "pluie": p["risque_pluie"]})
    lev, cou = cal.soleil(jour, "audun")
    return {
        "genere": dt.datetime.now().isoformat(timespec="minutes"),
        "heure": f"{t:%H:%M}", "date": jour_court(jour), "date_longue": f"{JOURS[jour.weekday()]} {jour.day} {MOIS[jour.month - 1]} {jour.year}",
        "reseau": reseau, "lieu": h["lieu"].split(",")[0].split(" (")[0],
        "meteo": {"maintenant": maintenant_c, "previsions": previsions, "lever": f"{lev:%H:%M}", "coucher": f"{cou:%H:%M}"},
        "conversations": conversations, "courriels": courriels, "banque": banque, "agenda": evts[:40],
    }


GABARIT = r"""<title>Téléphone de William</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Mise en page : une colonne de téléphone (430 px au plus) centrée ; barre d'état en haut, contenu défilant, onglets en bas. */
:root {
  --fond: #e9eeec; --ecran: #fbfcfc; --encre: #17201f; --gris: #5b6a67; --trait: #d5dddb; --carte: #ffffff;
  --accent: #0b6e6a; --accent-doux: #d8eeeb; --bulle-moi: #d4ece8; --bulle-eux: #ffffff;
  --credit: #1c7a3c; --debit: #9a2b2b; --ferie: #8a5a00;
  --ui: "Figtree", "Segoe UI", system-ui, -apple-system, sans-serif;
  --chiffres: "IBM Plex Mono", ui-monospace, "Cascadia Mono", Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --fond: #0b1110; --ecran: #111918; --encre: #e4ecea; --gris: #92a29f; --trait: #23302e; --carte: #172120;
  --accent: #46b9b0; --accent-doux: #173533; --bulle-moi: #1c3a37; --bulle-eux: #1a2524;
  --credit: #6fcf8e; --debit: #f08d8d; --ferie: #e0b45a; color-scheme: dark } }
:root[data-theme="dark"] {
  --fond: #0b1110; --ecran: #111918; --encre: #e4ecea; --gris: #92a29f; --trait: #23302e; --carte: #172120;
  --accent: #46b9b0; --accent-doux: #173533; --bulle-moi: #1c3a37; --bulle-eux: #1a2524;
  --credit: #6fcf8e; --debit: #f08d8d; --ferie: #e0b45a; color-scheme: dark }
html, body { height: 100%; }
body { background: var(--fond); color: var(--encre); font-family: var(--ui); font-size: 15px; line-height: 1.45; }
.telephone { max-width: 430px; margin-inline: auto; min-height: 100%; background: var(--ecran); display: flex; flex-direction: column;
  border-inline: 1px solid var(--trait); }
.etat { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 2; background: var(--ecran); display: flex; justify-content: space-between;
  align-items: center; padding: 10px 16px 8px; font-family: var(--chiffres); font-size: 13px; border-bottom: 1px solid var(--trait); gap: 12px; }
.etat .reseau { color: var(--gris); letter-spacing: .04em; }
.entete { padding: 18px 16px 6px; display: grid; gap: 2px; }
.entete h1 { margin: 0; font-size: 24px; font-weight: 700; text-wrap: balance; }
.entete p { margin: 0; color: var(--gris); font-size: 14px; }
main { flex: 1; padding: 6px 16px 96px; display: grid; gap: 14px; align-content: start; min-width: 0; }
.onglets { position: sticky; bottom: 0; display: grid; grid-template-columns: repeat(5, 1fr); background: var(--ecran);
  border-top: 1px solid var(--trait); padding-bottom: env(safe-area-inset-bottom, 0px); }
.onglets button { appearance: none; border: 0; background: none; color: var(--gris); font: 600 12px var(--ui); padding: 10px 2px 12px;
  display: grid; justify-items: center; gap: 4px; cursor: pointer; }
.onglets button svg { width: 22px; height: 22px; fill: none; stroke: currentColor; stroke-width: 1.8; }
.onglets button[aria-selected="true"] { color: var(--accent); }
.onglets button:focus-visible, .liste button:focus-visible, .retour:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.badge { font-family: var(--chiffres); font-size: 11px; background: var(--accent); color: var(--ecran); border-radius: 9px; padding: 0 6px; }
.liste { display: grid; border-top: 1px solid var(--trait); }
.liste > * { border-bottom: 1px solid var(--trait); }
.liste button { appearance: none; border: 0; background: none; color: inherit; text-align: left; font: inherit; width: 100%; cursor: pointer; }
.ligne { display: grid; grid-template-columns: 1fr auto; gap: 2px 12px; padding: 12px 2px; min-width: 0; }
.ligne .titre { font-weight: 600; overflow-wrap: anywhere; }
.ligne .sous { color: var(--gris); font-size: 14px; grid-column: 1 / -1; overflow-wrap: anywhere; }
.ligne .quand, .montant, .temp { font-family: var(--chiffres); font-variant-numeric: tabular-nums; font-size: 13px; color: var(--gris); white-space: nowrap; }
.montant.credit { color: var(--credit); } .montant.debit { color: var(--debit); }
.vide { color: var(--gris); padding: 28px 4px; text-align: center; display: grid; gap: 6px; }
.vide strong { color: var(--encre); font-size: 16px; }
.solde { background: var(--carte); border: 1px solid var(--trait); border-radius: 14px; padding: 16px; display: grid; gap: 4px; }
.solde .chiffre { font-family: var(--chiffres); font-size: 26px; font-weight: 500; font-variant-numeric: tabular-nums; }
.solde .nom { color: var(--gris); font-size: 13px; text-transform: uppercase; letter-spacing: .06em; }
.soldes { display: grid; gap: 10px; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); }
.maintenant { display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; }
.maintenant .grand { font-family: var(--chiffres); font-size: 54px; font-weight: 500; line-height: 1; }
.previsions { display: grid; border-top: 1px solid var(--trait); }
.prev { display: grid; grid-template-columns: 7.5em 1fr auto auto; gap: 10px; align-items: center; padding: 11px 2px; border-bottom: 1px solid var(--trait); }
.prev .pluie { font-family: var(--chiffres); font-size: 12px; color: var(--accent); }
.fil { display: grid; gap: 8px; }
.bulle { max-width: 82%; padding: 8px 11px; border-radius: 14px; background: var(--bulle-eux); border: 1px solid var(--trait); overflow-wrap: anywhere; white-space: pre-wrap; }
.bulle.moi { justify-self: end; background: var(--bulle-moi); border-color: transparent; }
.bulle small { display: block; font-family: var(--chiffres); font-size: 11px; color: var(--gris); margin-top: 3px; }
.jour-sep { justify-self: center; font-size: 12px; color: var(--gris); text-transform: uppercase; letter-spacing: .06em; }
.retour { appearance: none; border: 0; background: none; color: var(--accent); font: 600 15px var(--ui); padding: 4px 0; cursor: pointer; justify-self: start; }
.puce { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--ferie); }
.puce.public { color: var(--accent); }
.note { color: var(--gris); font-size: 12px; }
@media (prefers-reduced-motion: no-preference) { main > * { animation: entree .18s ease-out both; } }
@keyframes entree { from { opacity: .4; transform: translateY(3px); } to { opacity: 1; transform: none; } }
</style>
<div class="telephone">
  <div class="etat" role="status"><span id="heure"></span><span id="date"></span><span class="reseau" id="reseau"></span></div>
  <div class="entete"><h1 id="titre"></h1><p id="soustitre"></p></div>
  <main id="contenu" tabindex="-1"></main>
  <nav class="onglets" role="tablist" aria-label="Applications">
    <button role="tab" id="t-messages" data-vue="messages"><svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg>Messages</button>
    <button role="tab" id="t-courriels" data-vue="courriels"><svg viewBox="0 0 24 24"><path d="M3 6h18v12H3z"/><path d="m3 7 9 6 9-6"/></svg>Courriels</button>
    <button role="tab" id="t-banque" data-vue="banque"><svg viewBox="0 0 24 24"><path d="M3 10h18M5 10v8M10 10v8M14 10v8M19 10v8M3 20h18M12 3l9 5H3z"/></svg>Banque</button>
    <button role="tab" id="t-agenda" data-vue="agenda"><svg viewBox="0 0 24 24"><path d="M4 6h16v14H4zM4 10h16M8 3v5M16 3v5"/></svg>Agenda</button>
    <button role="tab" id="t-meteo" data-vue="meteo"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"/></svg>Météo</button>
  </nav>
</div>
<script>
const D = __DONNEES__;
const euros = n => n.toLocaleString("fr-FR", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " €";
const dateFr = iso => { const [a, m, j] = iso.split("-").map(Number); return new Date(a, m - 1, j).toLocaleDateString("fr-FR", { weekday: "short", day: "numeric", month: "short" }); };
const el = (tag, cls, txt) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt !== undefined) e.textContent = txt; return e; };
const vide = (titre, texte) => { const v = el("div", "vide"); v.append(el("strong", "", titre), el("span", "", texte)); return v; };
document.getElementById("heure").textContent = D.heure;
document.getElementById("date").textContent = D.date;
document.getElementById("reseau").textContent = "Réseau " + D.reseau;
const main = document.getElementById("contenu");
const vues = {
  messages() {
    titre("Messages", D.conversations.length ? D.conversations.length + " conversation(s)" : "Aucune conversation");
    if (!D.conversations.length) return main.append(vide("Aucun message pour l'instant", "Les conversations de William apparaîtront ici dès le premier échange."));
    const l = el("div", "liste");
    D.conversations.forEach((c, i) => {
      const dernier = c.messages[c.messages.length - 1];
      const b = el("button"); const g = el("div", "ligne");
      g.append(el("span", "titre", c.nom), el("span", "quand", dateFr(dernier.date) + " " + dernier.heure), el("span", "sous", (dernier.moi ? "Vous : " : "") + dernier.texte.slice(0, 90)));
      b.append(g); b.addEventListener("click", () => fil(i)); l.append(b);
    });
    main.append(l);
  },
  courriels() {
    titre("Courriels", D.courriels.length ? D.courriels.length + " message(s) reçu(s)" : "Boîte de réception vide");
    if (!D.courriels.length) return main.append(vide("Boîte de réception vide", "Les courriers et courriels reçus par William apparaîtront ici."));
    const l = el("div", "liste");
    D.courriels.forEach(c => { const g = el("div", "ligne"); g.append(el("span", "titre", c.objet), el("span", "quand", dateFr(c.date)), el("span", "sous", "Pièce jointe : " + c.fichier)); l.append(g); });
    main.append(l);
  },
  banque() {
    titre("Banque", "Comptes de William");
    const s = el("div", "soldes");
    D.banque.comptes.forEach(c => { const b = el("div", "solde"); b.append(el("span", "nom", c.nom), el("span", "chiffre", euros(c.solde))); s.append(b); });
    main.append(s);
    main.append(el("p", "note", "Placements (ETF), dernière valeur connue : " + euros(D.banque.placements)));
    if (!D.banque.operations.length) return main.append(vide("Aucune opération récente", "Les paiements, prélèvements et virements apparaîtront ici après leur date."));
    const l = el("div", "liste");
    D.banque.operations.forEach(o => { const g = el("div", "ligne"); g.append(el("span", "titre", o.libelle), el("span", "montant " + (o.montant >= 0 ? "credit" : "debit"), (o.montant >= 0 ? "+" : "") + euros(o.montant)), el("span", "sous", dateFr(o.date) + " · " + o.compte)); l.append(g); });
    main.append(l);
  },
  agenda() {
    titre("Agenda", "À venir");
    if (!D.agenda.length) return main.append(vide("Rien de prévu", "Les rendez-vous de William s'afficheront ici."));
    const l = el("div", "liste");
    D.agenda.forEach(e => { const g = el("div", "ligne"); const t = el("span", "titre", e.titre);
      g.append(t, el("span", "quand", dateFr(e.date) + (e.heure ? " " + e.heure : "")));
      if (e.type !== "rdv") g.append(el("span", "sous puce " + (e.type === "public" ? "public" : ""), e.type === "ferie" ? "Jour férié" : "Événement"));
      l.append(g); });
    main.append(l);
  },
  meteo() {
    titre("Météo", D.lieu + " · " + D.date_longue);
    const m = el("div", "maintenant"); m.append(el("span", "grand", D.meteo.maintenant + "°"), el("span", "", "Lever " + D.meteo.lever + " · coucher " + D.meteo.coucher));
    main.append(m);
    const p = el("div", "previsions");
    D.meteo.previsions.forEach(x => { const r = el("div", "prev"); r.append(el("span", "titre", x.jour), el("span", "", x.ciel), el("span", "pluie", x.pluie + " %"), el("span", "temp", x.min + "° / " + x.max + "°")); p.append(r); });
    main.append(p, el("p", "note", "Prévisions : elles peuvent se tromper, surtout à trois jours."));
  },
};
function titre(t, s) { document.getElementById("titre").textContent = t; document.getElementById("soustitre").textContent = s; }
function fil(i) {
  const c = D.conversations[i]; main.replaceChildren(); titre(c.nom, c.messages.length + " message(s)");
  const r = el("button", "retour", "‹ Messages"); r.addEventListener("click", () => montrer("messages")); main.append(r);
  const f = el("div", "fil"); let jourPrec = "";
  c.messages.forEach(m => { if (m.date !== jourPrec) { f.append(el("div", "jour-sep", dateFr(m.date))); jourPrec = m.date; }
    const b = el("div", "bulle" + (m.moi ? " moi" : ""), m.texte); b.append(el("small", "", m.heure)); f.append(b); });
  main.append(f);
}
function montrer(vue) {
  main.replaceChildren();
  document.querySelectorAll(".onglets button").forEach(b => b.setAttribute("aria-selected", String(b.dataset.vue === vue)));
  vues[vue]();
  try { localStorage.setItem("telephone-william-vue", vue); } catch (e) {}
}
document.querySelectorAll(".onglets button").forEach(b => b.addEventListener("click", () => montrer(b.dataset.vue)));
let depart = "messages";
try { const v = localStorage.getItem("telephone-william-vue"); if (v && vues[v]) depart = v; } catch (e) {}
if (/^#(messages|courriels|banque|agenda|meteo)$/.test(location.hash)) depart = location.hash.slice(1);
montrer(depart);
</script>
"""


def construire():
    d = donnees()
    brut = json.dumps(d, ensure_ascii=False)
    fautes = sorted(set(m.group(0) for m in INTERDITS.finditer(brut)))
    if fautes:
        sys.exit("REFUSÉ : la page montrerait des éléments du moteur au joueur : " + ", ".join(fautes[:10]))
    html = GABARIT.replace("__DONNEES__", brut.replace("</", "<\\/"))
    dossier = SORTIES / "telephone"
    ecrire_texte(dossier / "index.html", html)
    ecrire_texte(dossier / "telephone.json", json.dumps(d, ensure_ascii=False, indent=1))
    return dossier / "index.html", d


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if args.json:
        print(json.dumps(donnees(), ensure_ascii=False, indent=1))
        return 0
    chemin, d = construire()
    print(f"Page écrite : {chemin.relative_to(RACINE).as_posix()} ({len(d['conversations'])} conversation(s), {len(d['courriels'])} "
          f"courriel(s), {len(d['banque']['operations'])} opération(s), {len(d['agenda'])} entrée(s) d'agenda)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
