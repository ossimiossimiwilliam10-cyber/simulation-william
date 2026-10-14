/* Portefeuille : espèces en poche, taux du jour, convertisseur et distributeurs de la ville (outils/devises.py).
   Le calcul « par carte » est le même qu'en Python : montant / cours Visa + frais de la banque (pourcentage + fixe). */
appli({
  id: "portefeuille", nom: "Portefeuille", couleur: "var(--app-portefeuille)",
  icone: '<svg viewBox="0 0 24 24"><path d="M3 7h15a3 3 0 0 1 3 3v7a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3z"/><path d="M3 7l12-4v4"/><circle cx="16.5" cy="13.5" r="1"/></svg>',
  ouvrir(main, ui) {
    const P = D.applis.portefeuille;
    const pesos = n => Math.round(n).toLocaleString("fr-FR").replace(/ /g, " ") + " PHP";
    ui.titre("Portefeuille", "Espèces et change");
    const s = el("div", "soldes");
    const d = P.devises[0];
    const php = P.especes.PHP || 0, eur = P.especes.EUR || 0;
    const b1 = el("div", "carte solde"); b1.append(el("span", "nom", "Espèces en pesos"), el("span", "chiffre", pesos(php)));
    if (d) b1.append(el("span", "note", "≈ " + euros(php / d.taux)));
    s.append(b1);
    if (eur) { const b2 = el("div", "carte solde"); b2.append(el("span", "nom", "Espèces en euros"), el("span", "chiffre", euros(eur))); s.append(b2); }
    main.append(s);
    if (!d) return main.append(el("p", "note", "Pas de devise étrangère utile ici."));
    main.append(el("h2", "sec", "Taux du jour"));
    const c = el("div", "carte");
    c.append(el("strong", "", "1 € = " + d.taux.toLocaleString("fr-FR", { maximumFractionDigits: 2 }) + " " + d.code),
             el("span", "note", "Cours appliqué aux cartes Visa : " + d.cours_visa.toLocaleString("fr-FR", { maximumFractionDigits: 2 }) + " " + d.code));
    main.append(c, el("h2", "sec", "Convertir"));
    const f = el("div", "formulaire");
    const ent = el("input"); ent.type = "number"; ent.min = "0"; ent.step = "10"; ent.value = memoire.lire("portefeuille-montant", 1000); ent.id = "pf-montant";
    const lb = el("label", "", "Montant en pesos"); lb.htmlFor = "pf-montant";
    const ch = el("div", "champ"); ch.append(lb, ent); f.append(ch);
    const res = el("div", "carte");
    const frais = (carte, op, e) => { const x = (P.frais || []).find(y => y.carte === carte && y.operation === op); return x ? e * x.pourcentage / 100 + x.fixe : 0; };
    function calculer() {
      const m = Number(ent.value) || 0; memoire.ecrire("portefeuille-montant", m);
      const base = m / d.cours_visa;
      res.replaceChildren(el("span", "", pesos(m) + " ≈ " + euros(m / d.taux) + " au cours du jour"),
        el("span", "note", "Payé avec la Visa Debit : " + euros(base + frais("visa_debit", "paiement", base)) + " (frais de la banque compris)"));
    }
    ent.addEventListener("input", calculer); calculer();
    main.append(f, res);
    if (!(P.distributeurs || []).length) return;
    main.append(el("h2", "sec", "Distributeurs"));
    const l = el("div", "liste");
    P.distributeurs.forEach(x => { const g = el("div", "ligne");
      g.append(el("span", "titre", x.banque), el("span", "quand", x.frais ? "frais " + pesos(x.frais) : "sans frais"),
               el("span", "sous", x.lieu + " · " + pesos(x.plafond) + " au plus par retrait")); l.append(g); });
    main.append(l, el("p", "note", "Le distributeur affiche ses frais avant de valider ; la banque de la carte ajoute les siens."));
    const z = el("div", "carte");
    const sel = el("select"); P.distributeurs.forEach((x, i) => { const o = el("option", "", x.banque + " · " + x.lieu); o.value = String(i); sel.append(o); });
    const mt = el("input"); mt.type = "number"; mt.min = "100"; mt.step = "100"; mt.value = "5000";
    const ca = el("select"); [["visa_debit", "Visa Debit"], ["visa_premier", "Visa Premier"]].forEach(([v, t]) => { const o = el("option", "", t); o.value = v; ca.append(o); });
    const bt = el("button", "bouton", "Copier pour retirer"); bt.type = "button";
    bt.addEventListener("click", () => { const x = P.distributeurs[Number(sel.value)];
      copier("Je retire " + pesos(Number(mt.value)) + " au distributeur " + x.banque + " (" + x.lieu + ") avec la " + ca.options[ca.selectedIndex].text
        + " [portefeuille: retirer carte=" + ca.value + " montant=" + Math.round(Number(mt.value)) + " distributeur=" + x.id + "]", bt, z); });
    z.append(el("span", "etiquette", "Préparer un retrait"), sel, mt, ca, bt);
    main.append(z);
  },
});
