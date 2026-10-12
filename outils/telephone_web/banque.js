/* Banque : soldes, opérations, prélèvements à venir ; ordres permanents et virements que William configure lui-même
   (outils/banque.py). Les opérations préparées s'accumulent dans une file, se copient d'un coup et se collent dans la simulation ;
   chaque ligne porte une étiquette [banque: …] que le moteur applique en une commande. */
appli({
  id: "banque", nom: "Banque", couleur: "var(--app-banque)",
  icone: '<svg viewBox="0 0 24 24"><path d="M3 10h18M5 10v8M10 10v8M14 10v8M19 10v8M3 20h18M12 3l9 5H3z"/></svg>',
  ouvrir(main, ui) {
    const B = (D.applis && D.applis.banque) || { ordres: [], prelevements: [], comptes: {}, cartes: [], operations: [] };
    const cal = D.applis && D.applis.calendrier;
    let onglet = memoire.lire("banque-onglet", "comptes");
    let file = memoire.lire("banque-file", []);
    const sauver = () => { memoire.ecrire("banque-onglet", onglet); memoire.ecrire("banque-file", file); };
    const ajouter = (texte, etiquette) => { file.push(texte + " " + etiquette); sauver(); dessiner(); };
    const ligneOp = (titre, montant, sous) => { const g = el("div", "ligne");
      g.append(el("span", "titre", titre), el("span", "montant " + (montant >= 0 ? "credit" : "debit"), (montant >= 0 ? "+" : "") + euros(montant)), el("span", "sous", sous)); return g; };
    function champ(label, input) { const c = el("div", "champ"); const id = "b-" + Math.random().toString(36).slice(2, 8); input.id = id;
      const l = el("label", "", label); l.htmlFor = id; c.append(l, input); return c; }
    function selectComptes(avecExterne) { const s = el("select"); Object.entries(B.comptes).forEach(([k, v]) => { const o = el("option", "", v); o.value = k; s.append(o); });
      if (avecExterne) { const o = el("option", "", "Un tiers (autre personne)"); o.value = "externe"; s.append(o); } return s; }
    function barreFile() {
      if (!file.length) return null;
      const z = el("div", "carte");
      z.append(el("span", "etiquette", file.length + " opération(s) à envoyer dans la simulation"));
      const l = el("ul", "formalites"); file.forEach(x => l.append(el("li", "", x.replace(/\s\[banque:.*\]$/, "")))); z.append(l);
      const b = el("button", "bouton", "Copier les opérations"), v = el("button", "bouton discret", "Vider"); b.type = v.type = "button";
      b.addEventListener("click", () => copier("Dans l'application de la banque :\n" + file.map(x => "- " + x).join("\n"), b, z));
      v.addEventListener("click", () => { file = []; sauver(); dessiner(); });
      const r = el("div", "rangee"); r.append(b, v); z.append(r); return z;
    }
    function comptes() {
      const s = el("div", "soldes");
      D.banque.comptes.forEach(c => { const b = el("div", "carte solde"); b.append(el("span", "nom", c.nom), el("span", "chiffre", euros(c.solde))); s.append(b); });
      main.append(s, el("p", "note", "Placements (ETF), dernière valeur connue : " + euros(D.banque.placements)));
      if (cal) {
        const fin = ajouterJours(cal.aujourd_hui, 31);
        const avenir = cal.evenements.filter(e => e.type === "argent" && e.date >= cal.aujourd_hui && e.date <= fin);
        if (avenir.length) { main.append(el("h2", "sec", "À venir (31 jours)")); const l = el("div", "liste");
          avenir.forEach(o => l.append(ligneOp(o.titre, o.montant, dateFr(o.date) + " · " + o.detail))); main.append(l); }
      }
      main.append(el("h2", "sec", "Opérations passées"));
      if (!D.banque.operations.length) return main.append(vide("Aucune opération récente", "Les paiements, prélèvements et virements apparaîtront ici après leur date."));
      const l = el("div", "liste"); D.banque.operations.forEach(o => l.append(ligneOp(o.libelle, o.montant, dateFr(o.date) + " · " + o.compte))); main.append(l);
    }
    function virements() {
      main.append(el("h2", "sec", "Ordres permanents"));
      if (!B.ordres.length) main.append(el("p", "note", "Aucun ordre permanent."));
      B.ordres.forEach(o => {
        const c = el("div", "carte");
        const h = el("div", "haut-ligne"); h.append(el("strong", "", o.libelle), el("span", "montant debit", euros(o.montant)));
        c.append(h, el("span", "note", (o.statut === "suspendu" ? "Suspendu" : "Le " + o.jour + " de chaque mois · prochain : " + (o.prochaine ? dateFr(o.prochaine) : "—")) + (o.vers ? " · vers " + o.vers : "")));
        const f = el("div", "formulaire");
        const m = el("input"); m.type = "number"; m.min = "1"; m.step = "1"; m.value = String(Math.abs(o.montant));
        const j = el("input"); j.type = "number"; j.min = "1"; j.max = "28"; j.value = /^\d+$/.test(o.jour) ? o.jour : "2";
        f.append(champ("Montant (€)", m), champ("Jour du mois", j)); c.append(f);
        const r = el("div", "rangee");
        const mod = el("button", "bouton", "Modifier"), sus = el("button", "bouton discret", o.statut === "suspendu" ? "Reprendre" : "Suspendre");
        mod.type = sus.type = "button";
        mod.addEventListener("click", () => ajouter("Je modifie l'ordre « " + o.libelle + " » : " + euros(Number(m.value)) + " le " + j.value + " du mois",
          "[banque: ordre-modifier id=" + o.id + " montant=" + Number(m.value) + " jour=" + Number(j.value) + "]"));
        sus.addEventListener("click", () => ajouter((o.statut === "suspendu" ? "Je reprends" : "Je suspends") + " l'ordre « " + o.libelle + " »",
          "[banque: " + (o.statut === "suspendu" ? "ordre-reprendre" : "ordre-suspendre") + " id=" + o.id + "]"));
        r.append(mod, sus); c.append(r); main.append(c);
      });
      main.append(el("h2", "sec", "Prélèvements"));
      const l = el("div", "liste");
      B.prelevements.forEach(o => l.append(ligneOp(o.libelle, o.montant, (o.periodicite === "mensuel" ? "chaque mois, le " + o.jour : o.periodicite) + (o.prochaine ? " · prochain : " + dateFr(o.prochaine) : ""))));
      main.append(l, el("p", "note", "Un prélèvement se conteste ou s'arrête auprès du créancier (contrat, abonnement) : la banque ne fait que l'exécuter."));
    }
    function nouveau() {
      main.append(el("h2", "sec", "Virement ponctuel"));
      const f = el("div", "formulaire");
      const de = selectComptes(false), vers = selectComptes(true); vers.value = "projet";
      const m = el("input"); m.type = "number"; m.min = "1"; m.step = "1"; m.placeholder = "Montant";
      const d = el("input"); d.type = "date"; d.min = D.aujourdhui || ""; d.value = D.aujourdhui || "";
      const ben = el("input"); ben.type = "text"; ben.placeholder = "Nom du bénéficiaire (si tiers)";
      f.append(champ("De", de), champ("Vers", vers), champ("Montant (€)", m), champ("Date", d), champ("Bénéficiaire", ben));
      const b = el("button", "bouton", "Préparer le virement"); b.type = "button";
      b.addEventListener("click", () => {
        if (!(Number(m.value) > 0)) return m.focus();
        if (vers.value === de.value) return vers.focus();
        if (vers.value === "externe" && !ben.value.trim()) return ben.focus();
        const cible = vers.value === "externe" ? ben.value.trim() : B.comptes[vers.value];
        ajouter("Virement de " + euros(Number(m.value)) + " de " + B.comptes[de.value] + " vers " + cible + (d.value && d.value !== D.aujourdhui ? " le " + dateFr(d.value) : " maintenant"),
          "[banque: virement de=" + de.value + " vers=" + vers.value + " montant=" + Number(m.value) + (d.value ? " date=" + d.value : "") + (vers.value === "externe" ? " beneficiaire=\"" + ben.value.trim().replace(/"/g, "'") + "\"" : "") + "]");
      });
      main.append(f, b, el("h2", "sec", "Nouvel ordre permanent"));
      const f2 = el("div", "formulaire");
      const de2 = selectComptes(false), vers2 = selectComptes(true); vers2.value = "etf";
      const m2 = el("input"); m2.type = "number"; m2.min = "1"; m2.step = "1"; m2.placeholder = "Montant";
      const j2 = el("input"); j2.type = "number"; j2.min = "1"; j2.max = "28"; j2.value = "2";
      const deb = el("input"); deb.type = "date"; deb.min = D.aujourdhui || ""; deb.value = D.aujourdhui || "";
      f2.append(champ("De", de2), champ("Vers", vers2), champ("Montant (€)", m2), champ("Jour du mois", j2), champ("À partir du", deb));
      const b2 = el("button", "bouton", "Préparer l'ordre"); b2.type = "button";
      b2.addEventListener("click", () => {
        if (!(Number(m2.value) > 0)) return m2.focus();
        if (vers2.value === de2.value) return vers2.focus();
        ajouter("Nouvel ordre permanent : " + euros(Number(m2.value)) + " le " + j2.value + " de chaque mois, de " + B.comptes[de2.value] + " vers " + (B.comptes[vers2.value] || "un tiers") + ", à partir du " + dateFr(deb.value),
          "[banque: ordre-creer de=" + de2.value + " vers=" + vers2.value + " montant=" + Number(m2.value) + " jour=" + Number(j2.value) + " debut=" + deb.value + "]");
      });
      main.append(f2, b2);
    }
    /* Cartes (outils/cartes.py, 12/10/2026) : limite de la période, utilisé, disponible ; une carte de crédit est débitée au relevé. */
    function cartes() {
      const C = B.cartes || [];
      if (!C.length) return main.append(el("p", "note", "Aucune carte."));
      C.forEach(c => {
        const k = el("div", "carte");
        const h = el("div", "haut-ligne"); h.append(el("strong", "", c.nom), el("span", "note", c.type === "credit" ? "carte de crédit" : "carte de débit"));
        const s = el("div", "soldes");
        [["Disponible", c.disponible], ["Utilisé", c.utilise], ["Limite" + (c.temporaire ? " (temporaire)" : ""), c.limite]].forEach(([n, v]) => {
          const b = el("div", "solde"); b.append(el("span", "nom", n), el("span", "chiffre", euros(v))); s.append(b); });
        const barre = el("div", "jauge"); const rempli = el("span"); rempli.style.width = Math.min(100, Math.round(100 * c.utilise / Math.max(c.limite, 1))) + "%";
        barre.append(rempli);
        k.append(h, s, barre, el("span", "note", "Période du " + dateFr(c.debut) + " au " + dateFr(c.fin)
          + (c.type === "credit" ? " · relevé débité du compte courant le " + dateFr(c.debit) : " · débit immédiat du compte courant")));
        main.append(k);
      });
      main.append(el("h2", "sec", "Paiements par carte"));
      const ops = B.operations || [];
      if (!ops.length) return main.append(el("p", "note", "Aucun paiement par carte pour l'instant."));
      const noms = Object.fromEntries(C.map(c => [c.id, c.nom]));
      const l = el("div", "liste");
      ops.forEach(o => { const g = el("div", "ligne");
        g.append(el("span", "titre", o.marchand), el("span", "montant " + (o.statut === "refuse" ? "" : "debit"), (o.statut === "refuse" ? "" : "-") + euros(o.montant)),
          el("span", "sous", dateFr(o.date) + " " + o.heure + " · " + (noms[o.carte] || o.carte) + " · " + (o.statut === "refuse" ? "refusé" : o.debit ? "débité au relevé le " + dateFr(o.debit) : "débité"))); l.append(g); });
      main.append(l, el("p", "note", "Une hausse de limite se demande dans les réglages de la banque en ligne, ou au conseiller."));
    }
    function dessiner() {
      main.replaceChildren();
      ui.titre("Banque", "Comptes de William");
      const bf = barreFile(); if (bf) main.append(bf);
      const tabs = el("div", "onglets-appli");
      [["comptes", "Comptes"], ["cartes", "Cartes"], ["virements", "Ordres"], ["nouveau", "Nouveau"]].forEach(([id, n]) => {
        const b = el("button", "", n); b.type = "button"; b.setAttribute("aria-selected", String(onglet === id));
        b.addEventListener("click", () => { onglet = id; sauver(); dessiner(); }); tabs.append(b);
      });
      main.append(tabs);
      ({ comptes, cartes, virements, nouveau }[onglet] || comptes)();
    }
    dessiner();
  },
});
