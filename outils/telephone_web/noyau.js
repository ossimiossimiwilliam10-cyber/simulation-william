/* Noyau du téléphone de William : outils communs, écran d'accueil, ouverture des applications.
   Une application = un fichier de outils/telephone_web/ qui appelle appli({ id, nom, couleur, icone, badge?, ouvrir(main, ui) }),
   inscrit dans APPLIS de outils/telephone.py (ordre de l'écran d'accueil). Ses données sont dans D.applis[id]. */
"use strict";
const APPLIS = [];
function appli(def) { APPLIS.push(def); }

const MOIS_LONGS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];
const MOIS_COURTS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."];
const JOURS_LONGS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"];
const el = (tag, cls, txt) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt !== undefined && txt !== null) e.textContent = txt; return e; };
const euros = (n, dec = 2) => n.toLocaleString("fr-FR", { minimumFractionDigits: dec, maximumFractionDigits: dec }).replace(/ /g, " ") + " €";
const parseIso = s => { const [a, m, j] = s.split("-").map(Number); return new Date(a, m - 1, j); };
const isoDe = d => d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
const ajouterJours = (s, n) => { const d = parseIso(s); d.setDate(d.getDate() + n); return isoDe(d); };
const ecartJours = (a, b) => Math.round((parseIso(b) - parseIso(a)) / 86400000);
const jourSemaine = s => (parseIso(s).getDay() + 6) % 7; /* 0 = lundi, comme en Python */
const dateFr = s => { const d = parseIso(s); return JOURS_LONGS[jourSemaine(s)].slice(0, 3) + ". " + d.getDate() + " " + MOIS_COURTS[d.getMonth()]; };
const dateLongue = s => { const d = parseIso(s); return JOURS_LONGS[jourSemaine(s)] + " " + d.getDate() + " " + MOIS_LONGS[d.getMonth()] + " " + d.getFullYear(); };
const vide = (titre, texte) => { const v = el("div", "vide"); v.append(el("strong", "", titre), el("span", "", texte)); return v; };
const icone = code => { const s = document.createElement("span"); s.className = "pastille"; s.innerHTML = code; return s; }; /* SVG écrits dans ces fichiers */
const memoire = {
  lire(cle, defaut) { try { const v = localStorage.getItem("telephone-william-" + cle); return v === null ? defaut : JSON.parse(v); } catch (e) { return defaut; } },
  ecrire(cle, v) { try { localStorage.setItem("telephone-william-" + cle, JSON.stringify(v)); } catch (e) {} },
};
/* Copier un texte (réservation à coller dans la simulation) ; si le presse-papiers est refusé, le texte s'affiche sélectionné. */
function copier(texte, bouton, zone) {
  const repli = () => { const t = el("textarea", "copie"); t.readOnly = true; t.value = texte; zone.append(t); t.focus(); t.select(); bouton.textContent = "Texte sélectionné : copie-le"; };
  try {
    navigator.clipboard.writeText(texte).then(() => { bouton.textContent = "Copié : colle-le dans la simulation"; }, repli);
  } catch (e) { repli(); }
}

const ecran = {
  accueil: document.getElementById("accueil"), appli: document.getElementById("appli"), main: document.getElementById("contenu"),
  titre: document.getElementById("titre"), sous: document.getElementById("soustitre"),
};
const ui = { titre(t, s) { ecran.titre.textContent = t; ecran.sous.textContent = s || ""; } };
document.getElementById("heure").textContent = D.heure;
document.getElementById("date").textContent = D.date;
document.getElementById("reseau").textContent = "Réseau " + D.reseau;
document.getElementById("grande-heure").textContent = D.heure;
document.getElementById("date-longue").textContent = D.date_longue.charAt(0).toUpperCase() + D.date_longue.slice(1);
document.getElementById("meteo-mini").textContent = D.lieu + " · " + D.meteo.maintenant + " °C";

function accueil() {
  ecran.appli.hidden = true; ecran.accueil.hidden = false;
  const g = document.getElementById("grille-applis"); g.replaceChildren();
  APPLIS.forEach(a => {
    const b = el("button", "tuile"); b.type = "button";
    const p = icone(a.icone); p.style.background = a.couleur;
    const n = a.badge ? a.badge() : 0;
    if (n) p.append(el("span", "badge", String(n)));
    b.append(p, el("span", "nom", a.nom));
    b.setAttribute("aria-label", a.nom + (n ? " (" + n + ")" : ""));
    b.addEventListener("click", () => ouvrir(a.id));
    g.append(b);
  });
  memoire.ecrire("appli", "");
  try { history.replaceState(null, "", "#accueil"); } catch (e) {}
  window.scrollTo(0, 0);
}
function ouvrir(id) {
  const a = APPLIS.find(x => x.id === id);
  if (!a) return accueil();
  ecran.accueil.hidden = true; ecran.appli.hidden = false;
  ecran.main.replaceChildren(); ui.titre(a.nom, "");
  a.ouvrir(ecran.main, ui);
  memoire.ecrire("appli", id);
  try { history.replaceState(null, "", "#" + id); } catch (e) {}
  window.scrollTo(0, 0);
}
document.getElementById("retour").addEventListener("click", accueil);
document.getElementById("barre-accueil").addEventListener("click", accueil);
window.addEventListener("load", () => {
  const h = location.hash.slice(1);
  if (APPLIS.some(a => a.id === h)) ouvrir(h); else accueil();
});
