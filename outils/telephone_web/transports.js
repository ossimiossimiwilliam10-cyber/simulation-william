/* Transports : itinéraires en transports en commun (bus, train, tram) entre Audun-le-Tiche, Esch, Luxembourg et l'aéroport.
   Données : D.applis.transports (outils/transports.py) ; le calcul est le MÊME qu'en Python (départs depuis le premier passage,
   fréquence selon le type de jour, correspondances minimales), pour que le moteur retrouve les horaires affichés. */
appli({
  id: "transports", nom: "Transports", couleur: "var(--app-transports)",
  icone: '<svg viewBox="0 0 24 24"><path d="M6 4h12a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM4 11h16M8 21l2-4M16 21l-2-4"/><circle cx="8" cy="14" r=".6"/><circle cx="16" cy="14" r=".6"/></svg>',
  ouvrir(main, ui) {
    const T = D.applis.transports;
    const A = Object.fromEntries(T.arrets.map(a => [a.id, a]));
    const L = Object.fromEntries(T.lignes.map(l => [l.id, l]));
    const dates = Object.keys(T.jours).sort();
    const st = Object.assign({ de: T.defaut.de, vers: T.defaut.vers, date: T.aujourdhui, heure: T.heure, sens: "depart" }, memoire.lire("transports", {}));
    if (!T.jours[st.date]) st.date = T.aujourdhui;
    if (!A[st.de]) st.de = T.defaut.de;
    if (!A[st.vers]) st.vers = T.defaut.vers;
    const kr = () => A[st.de].pays === "kr";
    const reseau = () => A[st.de].pays === "kr";
    const sauver = () => memoire.ecrire("transports", st);
    const min = s => { const [h, m] = s.split(":").map(Number); return h * 60 + m; };
    const hh = n => String(Math.floor(n / 60) % 24).padStart(2, "0") + ":" + String(n % 60).padStart(2, "0");
    const NOMS_JOURS = { semaine: "jour de semaine", vacances: "vacances scolaires", samedi: "samedi", dimanche: "dimanche ou jour férié" };
    const tousArrets = () => T.arrets;
    function frequence(l, typ, m) {
      if (typ === "samedi") return Number(l.freq_samedi);
      if (typ === "dimanche") return Number(l.freq_dimanche);
      if (typ === "semaine") for (const p of (l.pointe || "").split(",")) {
        if (!p.includes("-")) continue; const [a, b] = p.split("-"); if (min(a) <= m && m < min(b)) return Number(l.freq_pointe);
      }
      return Number(l.freq_creuse);
    }
    function departs(l, typ) {
      const res = []; let m = min(l.premier); const fin = min(l.dernier);
      while (m <= fin) { const f = frequence(l, typ, m); if (f <= 0) return res; res.push(m); m += f; }
      return res;
    }
    function suivre(route, t0, typ) {
      let t = t0; const tr = [];
      for (let i = 0; i < route.length; i++) {
        const l = L[route[i]];
        if (i > 0) t += Number(A[l.de].correspondance_min);
        const dep = departs(l, typ).find(d => d >= t);
        if (dep === undefined) return null;
        tr.push({ l, depart: dep, arrivee: dep + Number(l.duree) }); t = dep + Number(l.duree);
      }
      return tr;
    }
    function options() {
      const typ = (kr() ? T.jours_kr : T.jours)[st.date]; const cible = min(st.heure); const res = [];
      T.itineraires.filter(it => it.de === st.de && it.vers === st.vers).forEach(it => {
        let tr = null;
        if (st.sens === "depart") tr = suivre(it.troncons, cible, typ);
        else for (const d of departs(L[it.troncons[0]], typ).slice().reverse()) {
          const e = suivre(it.troncons, d, typ); if (e && e[e.length - 1].arrivee <= cible) { tr = e; break; }
        }
        if (tr) res.push({ it, tr, depart: tr[0].depart, arrivee: tr[tr.length - 1].arrivee, krw: it.prix_krw,
          prix: it.troncons.some(x => L[x].tarif === "regiozone") ? T.prix_regiozone : 0 });
      });
      res.sort(st.sens === "depart" ? (a, b) => a.arrivee - b.arrivee : (a, b) => b.depart - a.depart);
      return { typ, res };
    }
    function champ(label, input) { const c = el("div", "champ"); const id = "t-" + label.toLowerCase().replace(/[^a-z]/g, "");
      input.id = id; const lb = el("label", "", label); lb.htmlFor = id; c.append(lb, input); return c; }
    const groupe = a => a.pays === "kr" ? "kr" : "eu";
    function selectArret(cle, label) {
      const s = el("select"); T.arrets.filter(a => cle === "de" || groupe(a) === groupe(A[st.de])).forEach(a => { const o = el("option", "", a.nom); o.value = a.id; s.append(o); });
      s.value = st[cle]; s.addEventListener("change", () => { st[cle] = s.value;
        if (groupe(A[st.vers]) !== groupe(A[st.de])) st.vers = (T.arrets.find(a => a.id !== st.de && groupe(a) === groupe(A[st.de])) || {}).id;
        sauver(); dessiner(); }); return champ(label, s);
    }
    function dessiner() {
      main.replaceChildren();
      ui.titre("Transports", kr() ? "Métro et AREX" : "Bus, train et tram");
      const f = el("div", "formulaire");
      const d = el("input"); d.type = "date"; d.min = dates[0]; d.max = dates[dates.length - 1]; d.value = st.date;
      d.addEventListener("change", () => { if (T.jours[d.value]) { st.date = d.value; sauver(); dessiner(); } });
      const h = el("input"); h.type = "time"; h.value = st.heure; h.addEventListener("change", () => { if (h.value) { st.heure = h.value; sauver(); dessiner(); } });
      const s = el("select"); [["depart", "Partir à partir de"], ["arrivee", "Arriver au plus tard à"]].forEach(([v, t]) => { const o = el("option", "", t); o.value = v; s.append(o); });
      s.value = st.sens; s.addEventListener("change", () => { st.sens = s.value; sauver(); dessiner(); });
      f.append(selectArret("de", "Départ"), selectArret("vers", "Arrivée"), champ("Date", d), champ("Heure", h), champ("Sens", s));
      main.append(f);
      if (st.de === st.vers) return main.append(el("p", "note", "Choisis deux arrêts différents."));
      const { typ, res } = options();
      main.append(el("h2", "sec", dateLongue(st.date) + " · " + (NOMS_JOURS[typ] || typ)));
      if (!res.length) return main.append(vide("Aucun trajet", "Pas de correspondance possible ce jour-là à cette heure."));
      res.forEach(r => {
        const c = el("div", "carte vol");
        const hd = el("div", "haut"); hd.append(el("span", "compagnie", hh(r.depart) + " → " + hh(r.arrivee)), el("span", "prix", r.krw ? r.krw.toLocaleString("fr-FR") + " KRW" : r.prix ? euros(r.prix) : "Gratuit"));
        c.append(hd, el("span", "note", (r.arrivee - r.depart) + " min · " + r.tr.length + (r.tr.length > 1 ? " étapes" : " étape")));
        const t = el("div", "trajet");
        r.tr.forEach(x => {
          t.append(el("span", "sens", x.l.mode), el("span", "h", hh(x.depart) + " " + A[x.l.de].nom + " → " + hh(x.arrivee) + " " + A[x.l.vers].nom + " · " + x.l.nom));
        });
        c.append(t); main.append(c);
      });
      main.append(el("p", "note", kr() ? "Séoul : carte T-money (à recharger) ou billet à usage unique ; le métro se paie à la distance, correspondances comprises. Horaires théoriques, sous réserve de perturbations."
        : "Transports gratuits au Luxembourg. Partie française du trajet : billet RegioZone de 2 heures, à acheter dans l'application CFL go ou aux automates (plus de vente à bord). Horaires théoriques, sous réserve de perturbations."));
    }
    dessiner();
  },
});
