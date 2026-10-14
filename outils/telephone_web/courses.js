/* Courses : VTC (Grab) et taxis de la ville où se trouve William (outils/courses.py). Prix calculés par le même module que
   le moteur, pour l'heure de la dernière mise à jour du téléphone (créneau de 15 minutes, pluie du jour). */
appli({
  id: "courses", nom: "Courses", couleur: "var(--app-courses)",
  icone: '<svg viewBox="0 0 24 24"><path d="M5 16V11l2-5h10l2 5v5M5 16h14M5 16v3M19 16v3M7 11h10"/><circle cx="8" cy="14" r=".7"/><circle cx="16" cy="14" r=".7"/></svg>',
  ouvrir(main, ui) {
    const C = D.applis.courses;
    const pesos = n => Math.round(n).toLocaleString("fr-FR").replace(/ /g, " ") + " PHP";
    ui.titre("Courses", "VTC et taxis");
    if (!C.ville) return main.append(vide("Rien ici", "Les courses en VTC ou en taxi s'affichent dans une ville couverte."));
    const L = Object.fromEntries(C.lieux.map(l => [l.id, l]));
    const st = Object.assign({ de: C.ici || C.lieux[0].id, vers: "" }, memoire.lire("courses", {}));
    if (C.ici) st.de = memoire.lire("courses-ici", "") === C.ici ? st.de : C.ici;
    memoire.ecrire("courses-ici", C.ici);
    if (!L[st.de]) st.de = C.lieux[0].id;
    if (!L[st.vers] || st.vers === st.de) st.vers = C.lieux.find(l => l.id !== st.de).id;
    const installe = C.compte.installe === "oui";
    function dessiner() {
      main.replaceChildren(); ui.titre("Courses", "VTC et taxis");
      const z = el("div", "carte");
      if (!installe) {
        z.append(el("strong", "", "Grab n'est pas installé"), el("span", "note", "Inscription avec le numéro de téléphone (code par SMS)."));
        const b = el("button", "bouton", "Copier pour installer Grab"); b.type = "button";
        b.addEventListener("click", () => copier("J'installe Grab sur mon téléphone [courses: installer]", b, z)); z.append(b);
      } else if (!C.compte.carte) {
        z.append(el("strong", "", "Grab : paiement en espèces"), el("span", "note", "Aucune carte enregistrée."));
        [["visa_debit", "Visa Debit"], ["visa_premier", "Visa Premier"]].forEach(([v, t]) => { const b = el("button", "bouton discret", "Copier : enregistrer la " + t); b.type = "button";
          b.addEventListener("click", () => copier("J'enregistre ma " + t + " dans Grab [courses: carte carte=" + v + "]", b, z)); z.append(b); });
      } else z.append(el("strong", "", "Grab : carte enregistrée"), el("span", "note", C.compte.carte === "visa_premier" ? "Visa Premier" : "Visa Debit"));
      main.append(z);
      const f = el("div", "formulaire");
      const choix = (cle, label) => { const s = el("select"); C.lieux.forEach(l => { const o = el("option", "", l.nom); o.value = l.id; s.append(o); });
        s.value = st[cle]; s.id = "co-" + cle; s.addEventListener("change", () => { st[cle] = s.value; if (st.de === st.vers) st.vers = C.lieux.find(l => l.id !== st.de).id;
        memoire.ecrire("courses", st); dessiner(); });
        const c = el("div", "champ"); const lb = el("label", "", label); lb.htmlFor = s.id; c.append(lb, s); return c; };
      f.append(choix("de", "Départ"), choix("vers", "Arrivée")); main.append(f);
      const liste = C.courses[st.de + ">" + st.vers] || [];
      main.append(el("h2", "sec", "Maintenant (" + C.heure + ")"));
      if (!liste.length) return main.append(vide("Aucune course", "Pas de service entre ces deux lieux."));
      liste.forEach(e => {
        const c = el("div", "carte vol");
        const hd = el("div", "haut"); hd.append(el("span", "compagnie", e.nom), el("span", "prix", pesos(e.prix)));
        c.append(hd, el("span", "note", "≈ " + euros(e.prix / C.taux) + " · " + (e.type === "vtc" ? "chauffeur dans " + e.attente + " min" : "file d'attente : ≈ " + e.attente + " min")
          + " · trajet ≈ " + e.minutes + " min · " + e.km.toLocaleString("fr-FR") + " km · " + e.paiement));
        if (e.majoration >= 1.2) c.append(el("span", "etiquette", "Forte demande : prix plus élevés que d'habitude"));
        const r = el("div", "rangee");
        const ajouter = (texte, paiement) => { const b = el("button", "bouton", texte); b.type = "button";
          b.addEventListener("click", () => copier("Je prends : " + e.nom + ", de " + L[st.de].nom + " à " + L[st.vers].nom + " (paiement : " + (paiement === "carte" ? "carte" : "espèces") + ")"
            + " [courses: commander service=" + e.service + " de=" + st.de + " vers=" + st.vers + " paiement=" + paiement + "]", b, c)); r.append(b); };
        if (e.type === "vtc") { if (installe) { if (C.compte.carte) ajouter("Copier : commander (carte)", "carte"); ajouter("Copier : commander (espèces)", "especes"); } }
        else ajouter("Copier : prendre ce taxi", "especes");
        c.append(r); main.append(c);
      });
      main.append(el("p", "note", "Prix indicatifs au moment de la mise à jour ; un VTC peut changer de prix d'un quart d'heure à l'autre."));
    }
    dessiner();
  },
});
