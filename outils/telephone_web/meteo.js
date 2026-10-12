/* Météo : température du moment et prévisions vues par William (les prévisions peuvent se tromper). */
appli({
  id: "meteo", nom: "Météo", couleur: "var(--app-meteo)",
  icone: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"/></svg>',
  ouvrir(main, ui) {
    ui.titre("Météo", D.lieu + " · " + D.date_longue);
    const m = el("div", "maintenant");
    m.append(el("span", "grand", D.meteo.maintenant + "°"), el("span", "", "Lever " + D.meteo.lever + " · coucher " + D.meteo.coucher));
    main.append(m);
    const p = el("div", "previsions");
    D.meteo.previsions.forEach(x => {
      const r = el("div", "prev");
      r.append(el("span", "titre", x.jour), el("span", "", x.ciel), el("span", "pluie", x.pluie + " %"), el("span", "temp", x.min + "° / " + x.max + "°"));
      p.append(r);
    });
    main.append(p, el("p", "note", "Prévisions : elles peuvent se tromper, surtout à trois jours."));
  },
});
