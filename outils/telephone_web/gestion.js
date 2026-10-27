/* Gestion : l'application de gestion de William (outils/gestion.py) : budget d'API, pôles, pôle RH (poste, annonces, candidats), documents reçus et analysés. */
appli({
  id: "gestion", nom: "Gestion", couleur: "var(--app-gestion)",
  icone: '<svg viewBox="0 0 24 24"><path d="M4 7h16v12H4z"/><path d="M9 7V5h6v2"/><path d="M4 12h16"/></svg>',
  ouvrir(main, ui) {
    const G = D.applis.gestion;
    let onglet = memoire.lire("gestion-onglet", "tableau");
    if (!["tableau", "rh", "documents"].includes(onglet)) onglet = "tableau";
    ui.titre("Gestion", "Version " + G.version + (G.agents.length ? " · pôle RH connecté à Claude" : " · pôle RH actif"));
    const euro = n => n.toLocaleString("fr-FR", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " €";
    const chip = (txt, cls) => { const c = el("span", "puce" + (cls ? " " + cls : ""), txt); return c; };
    const ligne = (titre, quand, sous) => { const g = el("div", "ligne"); g.append(el("span", "titre", titre), el("span", "quand", quand || "")); if (sous) { const s = el("span", "sous", sous); s.style.whiteSpace = "pre-line"; g.append(s); } return g; };

    const tableau = z => {
      const part = Math.min(100, 100 * G.depense / G.plafond);
      const b = el("div", "carte solde"); b.append(el("span", "nom", "Budget d'API du mois (plafond " + euro(G.plafond).replace(",00", "") + ")"),
        el("span", "chiffre", euro(G.depense) + " dépensés"));
      const barre = el("div", ""); barre.style.cssText = "height:8px;border-radius:4px;background:var(--accent-doux);overflow:hidden;margin-top:6px";
      const rempli = el("div", ""); rempli.style.cssText = "height:100%;background:var(--accent);width:" + part.toFixed(1) + "%";
      barre.append(rempli); b.append(barre, el("span", "sous", "Reste " + euro(G.restant) + (G.estimation ? " · dont " + euro(G.estimation) + " estimés (agents connectés)" : "") + " · modèle : " + G.modele));
      z.append(b, el("h2", "sec", "Pôles"));
      const l = el("div", "liste");
      G.poles.forEach(p => { const g = ligne(p.nom, p.statut === "actif" ? "Actif" : "À venir", p.description); l.append(g); });
      z.append(l);
      if (G.agents.length) {
        z.append(el("h2", "sec", "Agents"));
        const ag = el("div", "liste");
        G.agents.forEach(a => ag.append(ligne(a.pole, a.statut === "connecté" ? "Connecté" : "À créer", a.agent ? a.agent + (a.note ? " : " + a.note : "") : "Agent du pôle à créer")));
        z.append(ag, el("p", "note", "Un agent par pôle ; l'agent central examine toutes les réponses avant qu'elles te parviennent."));
      }
      z.append(el("h2", "sec", "Sources officielles"));
      const s = el("div", "liste");
      G.sources.forEach(x => s.append(ligne(x.titre, "", x.reference)));
      z.append(s, el("p", "note", "Un document reçu est envoyé au pôle concerné, comparé à ces sources, puis résumé : est-ce clair, peut-on faire mieux, que répondre. Messagerie de dépôt et pôles à venir : prochaines versions."));
    };

    const rh = z => {
      z.append(el("h2", "sec", "Poste ouvert"));
      const p = el("div", "liste"); p.append(ligne(G.poste.intitule, "Recherche ouverte", "Forme sociale : " + G.poste.forme)); z.append(p, el("h2", "sec", "Annonces"));
      const a = el("div", "liste"); G.annonces.forEach(x => a.append(ligne(x.nom, x.etat))); z.append(a, el("h2", "sec", "Candidats"));
      if (!G.candidats.length) return z.append(el("p", "note", "Aucun candidat pour l'instant."));
      const c = el("div", "liste");
      G.candidats.forEach(x => c.append(ligne(x.nom + " · " + x.niveau, x.note ? x.note + " / 100" : x.etat, x.resume + (x.note ? " · " + x.etat : "") + " · " + x.plateforme)));
      z.append(c);
    };

    const documents = z => {
      if (!G.documents.length) return z.append(vide("Aucun document", "Les documents envoyés par les collaborateurs apparaîtront ici avec le retour du pôle concerné."));
      const l = el("div", "liste");
      G.documents.forEach(d => l.append(ligne(d.objet, dateFr(d.date), d.expediteur + " · pôle " + d.pole + " · " + (d.statut === "analysé" ? "analysé (" + euro(d.cout) + ")" : "reçu") + (d.retour ? "\n" + d.retour : ""))));
      z.append(l);
    };

    const tabs = el("div", "onglets-appli onglets-3"), zone = el("div", "");
    const dessiner = () => {
      tabs.replaceChildren();
      [["tableau", "Tableau"], ["rh", "RH"], ["documents", "Documents"]].forEach(([id, nom]) => {
        const b = el("button", "", nom); b.type = "button"; b.setAttribute("aria-selected", String(onglet === id));
        b.addEventListener("click", () => { onglet = id; memoire.ecrire("gestion-onglet", id); dessiner(); }); tabs.append(b);
      });
      zone.replaceChildren(); zone.style.display = "grid"; zone.style.gap = "14px";
      ({ tableau, rh, documents }[onglet])(zone);
    };
    main.append(tabs, zone);
    dessiner();
  },
});
