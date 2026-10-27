/* Courriels : pièces reçues par William (courriels/), à leur date. */
appli({
  id: "courriels", nom: "Courriels", couleur: "var(--app-courriels)",
  icone: '<svg viewBox="0 0 24 24"><path d="M3 6h18v12H3z"/><path d="m3 7 9 6 9-6"/></svg>',
  ouvrir(main, ui) {
    ui.titre("Courriels", D.courriels.length ? D.courriels.length + " message(s) reçu(s)" : "Boîte de réception vide");
    if (!D.courriels.length) return main.append(vide("Boîte de réception vide", "Les courriers et courriels reçus par William apparaîtront ici."));
    const l = el("div", "liste");
    D.courriels.forEach(c => {
      const g = el(c.url ? "a" : "div", "ligne");
      if (c.url) { g.href = c.url; g.target = "_blank"; g.rel = "noopener"; }
      g.append(el("span", "titre", c.objet), el("span", "quand", dateFr(c.date)), el("span", "sous", "Pièce jointe : " + c.fichier + (c.url ? " · ouvrir" : "")));
      l.append(g);
    });
    main.append(l);
  },
});
