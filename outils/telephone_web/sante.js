/* Santé : ce que montrerait une montre connectée (outils/corps.py) : sommeil, entraînements, poids. */
appli({
  id: "sante", nom: "Santé", couleur: "var(--app-sante)",
  icone: '<svg viewBox="0 0 24 24"><path d="M3 12h4l2-5 4 10 2-5h6"/></svg>',
  ouvrir(main, ui) {
    const S = D.applis.sante;
    ui.titre("Santé", "Sommeil et entraînements");
    const s = el("div", "soldes");
    [["Dette de sommeil (7 nuits)", S.dette_7j.toLocaleString("fr-FR") + " h"], ["Entraînements (7 jours)", S.seances_7j + " · " + S.minutes_7j + " min"],
     ["Poids", S.poids.toLocaleString("fr-FR") + " kg"]].forEach(([n, v]) => { const b = el("div", "carte solde"); b.append(el("span", "nom", n), el("span", "chiffre", v)); s.append(b); });
    main.append(s, el("h2", "sec", "Sommeil, 14 dernières nuits"));
    if (!S.nuits.length) main.append(el("p", "note", "Aucune nuit enregistrée."));
    else {
      const max = Math.max(10, ...S.nuits.map(n => n.heures));
      const g = el("div", "barres"), a = el("div", "axe");
      for (let i = 0; i < 14 - S.nuits.length; i++) { g.append(el("span")); a.append(el("span")); }
      S.nuits.forEach(n => { const b = el("span", n.heures < S.besoin ? "court" : ""); b.style.height = Math.round(100 * n.heures / max) + "%";
        b.title = dateFr(n.date) + " : " + n.heures.toLocaleString("fr-FR") + " h"; g.append(b); a.append(el("span", "", n.date.slice(8))); });
      main.append(g, a, el("p", "note", "En orange : moins de " + S.besoin.toLocaleString("fr-FR") + " h."));
    }
    main.append(el("h2", "sec", "Entraînements récents"));
    if (!S.seances.length) return main.append(el("p", "note", "Aucun entraînement enregistré."));
    const l = el("div", "liste");
    S.seances.slice().reverse().forEach(x => { const g = el("div", "ligne"); g.append(el("span", "titre", x.note || "Entraînement"), el("span", "quand", x.minutes + " min"), el("span", "sous", dateFr(x.date))); l.append(g); });
    main.append(l);
  },
});
