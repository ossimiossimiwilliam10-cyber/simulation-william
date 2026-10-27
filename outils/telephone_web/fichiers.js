/* Fichiers : les PDF que William a en main (documents rédigés ou gardés, pièces reçues), classés par date ; un appui ouvre le PDF dans le lecteur du téléphone.
   Les fichiers sont publiés avec la page (telephone.py --fichiers) ; seuls ceux datés d'aujourd'hui ou d'avant sont listés. */
appli({
  id: "fichiers", nom: "Fichiers", couleur: "var(--app-fichiers)",
  icone: '<svg viewBox="0 0 24 24"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>',
  ouvrir(main, ui) {
    const tous = D.fichiers || [];
    ui.titre("Fichiers", tous.length ? tous.length + " fichier(s)" : "Aucun fichier");
    if (!tous.length) return main.append(vide("Aucun fichier", "Les documents de William et les pièces reçues apparaîtront ici."));
    const choix = [["tous", "Tous"], ["Documents", "Documents"], ["Reçus", "Reçus"]];
    let dossier = memoire.lire("fichiers-dossier", "tous");
    if (!choix.some(c => c[0] === dossier)) dossier = "tous";
    const onglets = el("div", "onglets-appli onglets-3");
    const zone = el("div", "");
    const dessiner = () => {
      onglets.replaceChildren();
      choix.forEach(([id, nom]) => {
        const b = el("button", "", nom); b.type = "button"; b.setAttribute("aria-selected", String(dossier === id));
        b.addEventListener("click", () => { dossier = id; memoire.ecrire("fichiers-dossier", id); dessiner(); });
        onglets.append(b);
      });
      zone.replaceChildren();
      const liste = tous.filter(f => dossier === "tous" || f.dossier === dossier);
      if (!liste.length) return zone.append(vide("Rien dans ce dossier", "Aucun fichier de ce type pour le moment."));
      const l = el("div", "liste");
      liste.forEach(f => {
        const a = el("a", "ligne"); a.href = f.url; a.target = "_blank"; a.rel = "noopener";
        a.append(el("span", "titre", f.nom), el("span", "quand", dateFr(f.date)), el("span", "sous", f.dossier + " · PDF · " + f.ko + " Ko"));
        l.append(a);
      });
      zone.append(l);
    };
    main.append(onglets, zone);
    dessiner();
  },
});
