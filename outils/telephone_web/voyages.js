/* Voyages : vols, hôtels, forfaits vol + hôtel et formalités. Données : D.applis.voyages (outils/voyages.py) ; les prix sont
   calculés ici EXACTEMENT comme dans outils/voyages.py (même base précalculée, mêmes facteurs, même arrondi), pour que le moteur
   retrouve le prix affiché quand le joueur réserve. Réserver = copier le texte et le coller dans la simulation. */
appli({
  id: "voyages", nom: "Voyages", couleur: "var(--app-voyages)",
  icone: '<svg viewBox="0 0 24 24"><path d="M10.5 3.5 13 10l6 2.5c1 .4 1 1.6 0 2L13 17l-2.5 4.5h-1L10 15l-4.5 1.5-1.5 2H3l1-4-1-4h1l1.5 2L10 9.5 9.5 3.5z"/></svg>',
  ouvrir(main, ui) {
    const V = D.applis.voyages;
    const premier = ajouterJours(V.jour, 1), dernier = ajouterJours(V.jour, V.horizon);
    const st = Object.assign({ onglet: "vols", de: V.departs[0], vers: V.destinations[0].code, aller: "", retour: "", voyageurs: 1,
      duree: V.duree_defaut, mois: V.jour.slice(0, 7) }, memoire.lire("voyages", {}));
    if (!V.departs.includes(st.de)) st.de = V.departs[0];
    if (!V.destinations.some(d => d.code === st.vers)) st.vers = V.destinations[0].code;
    if (st.aller && (st.aller < premier || st.aller > dernier)) { st.aller = ""; st.retour = ""; }
    if (st.retour && (!st.aller || st.retour <= st.aller || ecartJours(st.aller, st.retour) > V.sejour_max)) st.retour = "";
    if (st.mois < V.jour.slice(0, 7) || st.mois > dernier.slice(0, 7)) st.mois = V.jour.slice(0, 7);
    const sauver = () => memoire.ecrire("voyages", st);
    const dest = () => V.destinations.find(d => d.code === st.vers);
    const ent = x => x.toLocaleString("fr-FR").replace(/ /g, " ") + " €";
    const JC = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"];
    const dans = (x, a, b) => a <= b ? (x >= a && x <= b) : (x >= a || x <= b);
    const fDuree = n => { for (const [a, b, f] of V.duree) if (n >= a && n <= b) return f; return null; };
    const fRetour = (dd, r) => { const x = r.slice(5); for (const [a, b, f] of dd.retours) if (dans(x, a, b)) return f; return 1; };
    function prixVol(v, dd, aller, retour) {
      const n = ecartJours(aller, retour), i = ecartJours(V.jour, aller);
      if (n < 1 || n > V.sejour_max || i < 1 || i > V.horizon) return null;
      if (!v.jours.includes(jourSemaine(aller)) || !v.jours.includes(jourSemaine(retour))) return null;
      const f = fDuree(n); if (f === null) return null;
      return Math.floor(v.base[i] * f * fRetour(dd, retour) + 0.5);
    }
    const options = (dd, a, r) => dd.vols.filter(v => v.de === st.de).map(v => ({ v, p: prixVol(v, dd, a, r) })).filter(o => o.p !== null).sort((x, y) => x.p - y.p);
    function sejour(h, a, r) {
      const n = ecartJours(a, r), i0 = ecartJours(V.jour, a); let total = 0;
      for (let k = 0; k < n; k++) { const p = h.nuits[i0 + k]; if (p === undefined) return null; total += p; }
      return { total, n };
    }
    const trajet = v => v.via === "direct" ? "Vol direct" : (v.escales === 1 ? "1 escale" : v.escales + " escales") + " · " + v.via;
    const couleur = (dd, p) => p <= dd.seuils[0] ? "vert" : p <= dd.seuils[1] ? "orange" : "rouge";

    function champ(label, input, large) {
      const c = el("div", "champ" + (large ? " large" : "")); const id = "v-" + label.toLowerCase().replace(/[^a-z]/g, "") + "-" + Math.random().toString(36).slice(2, 7);
      input.id = id; const l = el("label", "", label); l.htmlFor = id; c.append(l, input); return c;
    }
    function selectDe() {
      const s = el("select"); V.departs.forEach(c => { const o = el("option", "", V.aeroports[c] + " (" + c + ")"); o.value = c; s.append(o); });
      s.value = st.de; s.addEventListener("change", () => { st.de = s.value; sauver(); dessiner(); }); return champ("Départ", s);
    }
    function selectVers() {
      const s = el("select"); V.destinations.forEach(d => { const o = el("option", "", d.ville + " (" + d.code + ")"); o.value = d.code; s.append(o); });
      s.value = st.vers; s.addEventListener("change", () => { st.vers = s.value; sauver(); dessiner(); }); return champ("Destination", s);
    }
    function dates(l1, l2) {
      const a = el("input"); a.type = "date"; a.min = premier; a.max = dernier; a.value = st.aller;
      a.addEventListener("change", () => {
        st.aller = a.value;
        if (st.aller && (!st.retour || st.retour <= st.aller || ecartJours(st.aller, st.retour) > V.sejour_max)) st.retour = ajouterJours(st.aller, st.duree);
        if (st.aller) st.mois = st.aller.slice(0, 7);
        sauver(); dessiner();
      });
      const r = el("input"); r.type = "date"; r.min = st.aller ? ajouterJours(st.aller, 1) : premier;
      r.max = st.aller ? ajouterJours(st.aller, V.sejour_max) : ajouterJours(dernier, V.sejour_max); r.value = st.retour;
      r.addEventListener("change", () => { st.retour = r.value; sauver(); dessiner(); });
      return [champ(l1, a), champ(l2, r)];
    }
    function selectVoyageurs() {
      const s = el("select"); for (let n = 1; n <= 6; n++) { const o = el("option", "", n + (n > 1 ? " voyageurs" : " voyageur")); o.value = String(n); s.append(o); }
      s.value = String(st.voyageurs); s.addEventListener("change", () => { st.voyageurs = Number(s.value); sauver(); dessiner(); }); return champ("Voyageurs", s);
    }
    function boutonCopie(texte) {
      const z = el("div"); const b = el("button", "bouton discret", "Copier pour réserver"); b.type = "button";
      b.addEventListener("click", () => copier(texte, b, z)); z.prepend(b); return z;
    }

    function vols(dd) {
      const f = el("div", "formulaire"); f.append(selectDe(), selectVers(), ...dates("Aller", "Retour"), selectVoyageurs());
      main.append(f);
      /* calendrier des prix (vue « mois entier ») */
      const [a, m] = st.mois.split("-").map(Number);
      const nav = el("div", "cal-nav");
      const prec = el("button", "", "‹"), suiv = el("button", "", "›"); prec.type = suiv.type = "button";
      prec.setAttribute("aria-label", "Mois précédent"); suiv.setAttribute("aria-label", "Mois suivant");
      prec.disabled = st.mois <= V.jour.slice(0, 7); suiv.disabled = st.mois >= dernier.slice(0, 7);
      const decaler = n => { st.mois = isoDe(new Date(a, m - 1 + n, 1)).slice(0, 7); sauver(); dessiner(); };
      prec.addEventListener("click", () => decaler(-1)); suiv.addEventListener("click", () => decaler(1));
      const duree = el("select"); [7, 14, 21, 30, 45, 60].forEach(n => { const o = el("option", "", n + " j"); o.value = String(n); duree.append(o); });
      duree.value = String(st.duree); duree.setAttribute("aria-label", "Durée du séjour");
      duree.addEventListener("change", () => { st.duree = Number(duree.value); sauver(); dessiner(); });
      nav.append(prec, el("span", "mois", MOIS_LONGS[m - 1] + " " + a), suiv, duree);
      main.append(el("h2", "sec", "Prix les plus bas, aller-retour par personne"), nav);
      const g = el("div", "cal-grille prix-grille");
      ["L", "M", "M", "J", "V", "S", "D"].forEach(j => g.append(el("span", "cal-jsem", j)));
      for (let i = 0; i < jourSemaine(st.mois + "-01"); i++) g.append(el("span"));
      const nb = new Date(a, m, 0).getDate();
      for (let j = 1; j <= nb; j++) {
        const d = st.mois + "-" + String(j).padStart(2, "0");
        const r = ajouterJours(d, st.duree);
        const o = d >= premier && d <= dernier ? options(dd, d, r) : [];
        const b = el("button", "cal-jour"); b.type = "button";
        b.append(el("span", "num", String(j)));
        if (o.length) { b.classList.add(couleur(dd, o[0].p)); b.append(el("span", "p", o[0].p.toLocaleString("fr-FR").replace(/ /g, " "))); }
        else { b.classList.add("sans"); b.disabled = true; }
        if (d === st.aller) b.classList.add("choisi");
        b.setAttribute("aria-label", dateLongue(d) + (o.length ? " : à partir de " + ent(o[0].p) : " : pas de vol"));
        b.addEventListener("click", () => { st.aller = d; st.retour = r; sauver(); dessiner(); });
        g.append(b);
      }
      main.append(g, el("p", "note", "Départ de " + V.aeroports[st.de] + ", retour " + st.duree + " jours plus tard. Vert : bon prix ; orange : moyen ; rouge : cher."));
      if (!st.aller || !st.retour) return main.append(el("p", "note", "Choisis un jour dans le calendrier des prix, ou des dates ci-dessus."));
      const res = options(dd, st.aller, st.retour);
      main.append(el("h2", "sec", "Du " + dateFr(st.aller) + " au " + dateFr(st.retour) + " · " + ecartJours(st.aller, st.retour) + " jours"));
      if (!res.length) {
        main.append(el("p", "note", "Aucun vol ces jours-là au départ de " + V.aeroports[st.de] + "."));
        dd.vols.filter(v => v.de === st.de).forEach(v => main.append(el("p", "note", v.compagnies + " : vols le " + v.jours.map(x => JC[x]).join(", ") + ".")));
        return;
      }
      res.forEach(({ v, p }) => {
        const c = el("div", "carte vol");
        const h = el("div", "haut"); h.append(el("span", "compagnie", v.compagnies), el("span", "prix", ent(p)));
        const t = el("div", "trajet");
        t.append(el("span", "sens", "Aller"), el("span", "h", v.aller[0] + " → " + v.aller[1] + " · " + v.aller[2]),
          el("span", "sens", "Retour"), el("span", "h", v.retour[0] + " → " + v.retour[1] + " · " + v.retour[2]));
        const total = p * st.voyageurs;
        c.append(h, el("span", "note", trajet(v) + " · prix par personne" + (st.voyageurs > 1 ? " · total " + ent(total) : "")), t);
        c.append(boutonCopie("Je réserve le vol " + v.compagnies + " (" + (v.via === "direct" ? "direct" : "par " + v.via) + "), " + V.aeroports[st.de] +
          " → " + dd.ville + ", aller le " + dateLongue(st.aller) + " (" + v.aller[0] + " → " + v.aller[1] + "), retour le " + dateLongue(st.retour) +
          " (" + v.retour[0] + " → " + v.retour[1] + "), " + st.voyageurs + (st.voyageurs > 1 ? " voyageurs" : " voyageur") + " : " + ent(total) + " au total."));
        main.append(c);
      });
      main.append(el("p", "note", "Horaires d'été, heures locales. Prix aller-retour en classe économique, taxes comprises."));
    }

    function hotels(dd) {
      const f = el("div", "formulaire"); f.append(selectVers(), el("span"), ...dates("Arrivée", "Départ"));
      main.append(f);
      const avecDates = st.aller && st.retour;
      const liste = dd.hotels.map(h => ({ h, s: avecDates ? sejour(h, st.aller, st.retour) : null }));
      if (avecDates) liste.sort((x, y) => (x.s ? x.s.total : 1e9) - (y.s ? y.s.total : 1e9));
      main.append(el("h2", "sec", avecDates ? dd.ville + " · du " + dateFr(st.aller) + " au " + dateFr(st.retour) : dd.ville + " · " + dd.hotels.length + " hébergements"));
      liste.forEach(({ h, s }) => {
        const c = el("div", "carte vol");
        const hd = el("div", "haut"); hd.append(el("span", "compagnie", h.nom), el("span", "prix", s ? ent(s.total) : "dès " + ent(h.des)));
        c.append(hd, el("span", "note", [h.categorie, h.quartier].filter(Boolean).join(" · ") + (s ? " · " + s.n + " nuit" + (s.n > 1 ? "s" : "") + " · dès " + ent(h.des) + " la nuit" : " · par nuit")));
        if (s) c.append(boutonCopie("Je réserve à " + h.nom + ", " + dd.ville + ", du " + dateLongue(st.aller) + " au " + dateLongue(st.retour) + " (" + s.n + " nuit" + (s.n > 1 ? "s" : "") + ") : " + ent(s.total) + "."));
        main.append(c);
      });
      main.append(el("p", "note", "Prix d'une chambre, taxes comprises."));
    }

    function forfait(dd) {
      const f = el("div", "formulaire"); f.append(selectDe(), selectVers(), ...dates("Aller", "Retour"), selectVoyageurs());
      main.append(f);
      if (!st.aller || !st.retour) return main.append(vide("Choisis tes dates", "Les prix des forfaits vol + hôtel s'affichent une fois la date de départ et la date de retour choisies."));
      const o = options(dd, st.aller, st.retour);
      if (!o.length) return main.append(vide("Aucun vol ces jours-là", "Change de dates ou d'aéroport de départ."));
      const best = o[0];
      const lignes = dd.hotels.map(h => { const s = sejour(h, st.aller, st.retour); if (!s) return null;
        const separe = best.p * st.voyageurs + s.total; return { h, s, separe, prix: Math.floor(separe * (1 - V.remise) + 0.5) }; }).filter(Boolean).sort((x, y) => x.prix - y.prix);
      main.append(el("h2", "sec", "Vol " + best.v.compagnies + " + hôtel · " + ecartJours(st.aller, st.retour) + " nuits"));
      lignes.forEach(x => {
        const c = el("div", "carte vol");
        const hd = el("div", "haut"); hd.append(el("span", "compagnie", x.h.nom), el("span", "prix", ent(x.prix)));
        c.append(hd, el("span", "note", "Au lieu de " + ent(x.separe) + " réservés séparément · " + st.voyageurs + (st.voyageurs > 1 ? " voyageurs" : " voyageur") + " · " + trajet(best.v)));
        c.append(boutonCopie("Je réserve le forfait vol + hôtel : " + best.v.compagnies + " (" + (best.v.via === "direct" ? "direct" : "par " + best.v.via) + ") au départ de " +
          V.aeroports[st.de] + " et " + x.h.nom + " à " + dd.ville + ", du " + dateLongue(st.aller) + " au " + dateLongue(st.retour) + ", " + st.voyageurs +
          (st.voyageurs > 1 ? " voyageurs" : " voyageur") + " : " + ent(x.prix) + "."));
        main.append(c);
      });
    }

    function formalites(dd) {
      main.append(el("h2", "sec", "Entrer au " + dd.pays + " avec un passeport luxembourgeois"));
      const l = el("ul", "formalites"); dd.formalites.forEach(x => l.append(el("li", "", x))); main.append(l);
    }

    function dessiner() {
      main.replaceChildren();
      const dd = dest();
      ui.titre("Voyages", "Vols, hôtels et séjours · " + dd.ville);
      const tabs = el("div", "onglets-appli"); tabs.setAttribute("role", "tablist");
      [["vols", "Vols"], ["hotels", "Hôtels"], ["forfait", "Vol + Hôtel"], ["formalites", "Formalités"]].forEach(([id, nom]) => {
        const b = el("button", "", nom); b.type = "button"; b.setAttribute("role", "tab"); b.setAttribute("aria-selected", String(st.onglet === id));
        b.addEventListener("click", () => { st.onglet = id; sauver(); dessiner(); }); tabs.append(b);
      });
      main.append(tabs);
      ({ vols, hotels, forfait, formalites })[st.onglet](dd);
    }
    dessiner();
  },
});
