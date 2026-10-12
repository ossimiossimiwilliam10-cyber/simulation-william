/* Calendrier : fériés (France et Luxembourg), vacances scolaires, événements publics, rendez-vous connus, prélèvements et virements.
   Données : D.applis.calendrier (outils/appli_calendrier.py). */
appli({
  id: "calendrier", nom: "Calendrier", couleur: "var(--app-calendrier)",
  icone: '<svg viewBox="0 0 24 24"><path d="M4 6h16v14H4zM4 10h16M8 3v5M16 3v5"/><path d="M8 14h2M12 14h2M16 14h0M8 17h2"/></svg>',
  ouvrir(main, ui) {
    const C = D.applis.calendrier;
    const index = {};
    const ajouter = (d, e) => { (index[d] = index[d] || []).push(e); };
    C.evenements.forEach(e => {
      if (e.fin && e.fin > e.date) { for (let d = e.date; d <= e.fin && d <= C.fin; d = ajouterJours(d, 1)) ajouter(d, e); }
      else ajouter(e.date, e);
    });
    const TYPES = { ferie: "Jour férié", vacances: "Vacances", ecole: "École", public: "Événement", rdv: "Rendez-vous", argent: "Argent" };
    let mois = memoire.lire("calendrier-mois", C.aujourd_hui.slice(0, 7));
    if (mois < C.debut.slice(0, 7) || mois > C.fin.slice(0, 7)) mois = C.aujourd_hui.slice(0, 7);
    let choisi = C.aujourd_hui;
    const ligne = e => {
      const g = el("div", "ligne");
      g.append(el("span", "titre", e.titre));
      if (e.type === "argent") g.append(el("span", "montant " + (e.montant >= 0 ? "credit" : "debit"), (e.montant >= 0 ? "+" : "") + euros(e.montant)));
      else g.append(el("span", "quand", e.heure ? e.heure : (e.fin && e.fin > e.date ? "jusqu'au " + dateFr(e.fin) : "")));
      g.append(el("span", "sous", TYPES[e.type] + (e.detail ? " · " + e.detail : "")));
      return g;
    };
    const dessiner = () => {
      main.replaceChildren();
      const [a, m] = mois.split("-").map(Number);
      ui.titre("Calendrier", "Aujourd'hui : " + dateLongue(C.aujourd_hui));
      const nav = el("div", "cal-nav");
      const prec = el("button", "", "‹"), suiv = el("button", "", "›"), auj = el("button", "", "Aujourd'hui");
      [prec, suiv, auj].forEach(b => { b.type = "button"; });
      prec.setAttribute("aria-label", "Mois précédent"); suiv.setAttribute("aria-label", "Mois suivant");
      prec.disabled = mois <= C.debut.slice(0, 7); suiv.disabled = mois >= C.fin.slice(0, 7);
      const decaler = n => { const d = new Date(a, m - 1 + n, 1); mois = isoDe(d).slice(0, 7); memoire.ecrire("calendrier-mois", mois); dessiner(); };
      prec.addEventListener("click", () => decaler(-1)); suiv.addEventListener("click", () => decaler(1));
      auj.addEventListener("click", () => { mois = C.aujourd_hui.slice(0, 7); choisi = C.aujourd_hui; memoire.ecrire("calendrier-mois", mois); dessiner(); });
      nav.append(prec, el("span", "mois", MOIS_LONGS[m - 1] + " " + a), suiv, auj);
      const grille = el("div", "cal-grille");
      ["L", "M", "M", "J", "V", "S", "D"].forEach(j => grille.append(el("span", "cal-jsem", j)));
      const premier = mois + "-01";
      for (let i = 0; i < jourSemaine(premier); i++) grille.append(el("span"));
      const nb = new Date(a, m, 0).getDate();
      for (let j = 1; j <= nb; j++) {
        const d = mois + "-" + String(j).padStart(2, "0");
        const evs = index[d] || [];
        const b = el("button", "cal-jour"); b.type = "button";
        if (evs.some(e => e.type === "vacances")) b.classList.add("vacances");
        if (evs.some(e => e.type === "ferie")) b.classList.add("ferie");
        if (d < C.aujourd_hui) b.classList.add("passe");
        if (d === C.aujourd_hui) b.classList.add("auj");
        if (d === choisi) b.classList.add("choisi");
        b.append(el("span", "num", String(j)));
        const pts = el("span", "points");
        ["rdv", "public", "ecole", "argent"].forEach(t => { if (evs.some(e => e.type === t)) pts.append(el("i", "pt " + t)); });
        b.append(pts);
        b.setAttribute("aria-label", dateLongue(d) + (evs.length ? " : " + evs.map(e => e.titre).join(", ") : ""));
        b.addEventListener("click", () => { choisi = d; dessiner(); });
        grille.append(b);
      }
      const leg = el("div", "legende");
      [["rdv", "Rendez-vous"], ["public", "Événement"], ["ecole", "École"], ["argent", "Argent"]].forEach(([t, n]) => {
        const s = el("span"); s.append(el("i", "pt " + t), document.createTextNode(n)); leg.append(s);
      });
      const vac = el("span"); vac.append(el("i", "bande"), document.createTextNode("Vacances")); leg.append(vac);
      const fer = el("span", "puce", "Férié"); leg.append(fer);
      main.append(nav, grille, leg);
      if (choisi.slice(0, 7) === mois) {
        main.append(el("h2", "sec", dateLongue(choisi)));
        const evs = index[choisi] || [];
        if (!evs.length) main.append(el("p", "note", "Rien ce jour-là."));
        else { const l = el("div", "liste"); evs.forEach(e => l.append(ligne(e))); main.append(l); }
      }
      main.append(el("h2", "sec", "En " + MOIS_LONGS[m - 1]));
      const vus = new Set(), duMois = [];
      for (let j = 1; j <= nb; j++) {
        const d = mois + "-" + String(j).padStart(2, "0");
        (index[d] || []).forEach(e => { if (!vus.has(e)) { vus.add(e); duMois.push([d, e]); } });
      }
      if (!duMois.length) return main.append(el("p", "note", "Rien de prévu ce mois-ci."));
      const l = el("div", "liste");
      duMois.forEach(([d, e]) => { const g = ligne(e); g.querySelector(".sous").textContent = dateFr(d) + " · " + g.querySelector(".sous").textContent; l.append(g); });
      main.append(l);
    };
    dessiner();
  },
});
