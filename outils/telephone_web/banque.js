/* Banque : soldes, placements, opérations passées et prélèvements ou virements à venir (ceux que William a mis en place ou paie). */
appli({
  id: "banque", nom: "Banque", couleur: "var(--app-banque)",
  icone: '<svg viewBox="0 0 24 24"><path d="M3 10h18M5 10v8M10 10v8M14 10v8M19 10v8M3 20h18M12 3l9 5H3z"/></svg>',
  ouvrir(main, ui) {
    ui.titre("Banque", "Comptes de William");
    const s = el("div", "soldes");
    D.banque.comptes.forEach(c => { const b = el("div", "carte solde"); b.append(el("span", "nom", c.nom), el("span", "chiffre", euros(c.solde))); s.append(b); });
    main.append(s, el("p", "note", "Placements (ETF), dernière valeur connue : " + euros(D.banque.placements)));
    const cal = D.applis && D.applis.calendrier;
    if (cal) {
      const fin = ajouterJours(cal.aujourd_hui, 31);
      const avenir = cal.evenements.filter(e => e.type === "argent" && e.date >= cal.aujourd_hui && e.date <= fin);
      if (avenir.length) {
        main.append(el("h2", "sec", "À venir (31 jours)"));
        const l = el("div", "liste");
        avenir.forEach(o => {
          const g = el("div", "ligne");
          g.append(el("span", "titre", o.titre), el("span", "montant " + (o.montant >= 0 ? "credit" : "debit"), (o.montant >= 0 ? "+" : "") + euros(o.montant)),
            el("span", "sous", dateFr(o.date) + " · " + o.detail));
          l.append(g);
        });
        main.append(l);
      }
    }
    main.append(el("h2", "sec", "Opérations passées"));
    if (!D.banque.operations.length) return main.append(vide("Aucune opération récente", "Les paiements, prélèvements et virements apparaîtront ici après leur date."));
    const l = el("div", "liste");
    D.banque.operations.forEach(o => {
      const g = el("div", "ligne");
      g.append(el("span", "titre", o.libelle), el("span", "montant " + (o.montant >= 0 ? "credit" : "debit"), (o.montant >= 0 ? "+" : "") + euros(o.montant)),
        el("span", "sous", dateFr(o.date) + " · " + o.compte));
      l.append(g);
    });
    main.append(l);
  },
});
