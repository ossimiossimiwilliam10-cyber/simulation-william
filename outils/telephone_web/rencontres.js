/* Rencontres : application de rencontre (outils/rencontres.py). Tant que William n'est pas inscrit, seul l'écran d'inscription
   s'affiche. Les actions (inscription, j'aime, passer, message) s'accumulent dans une file et se copient d'un coup pour être collées
   dans la simulation ; chaque ligne porte une étiquette [rencontres: …] que le moteur applique avec outils/rencontres.py. */
appli({
  id: "rencontres", nom: "Rencontres", couleur: "var(--app-rencontres)",
  icone: '<svg viewBox="0 0 24 24"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
  badge: () => { const R = D.applis.rencontres; return R && R.inscrit ? R.profils.filter(p => p.statut === "match").length : 0; },
  ouvrir(main, ui) {
    const R = D.applis.rencontres;
    let onglet = memoire.lire("rencontres-onglet", "decouvrir");
    let file = memoire.lire("rencontres-file", []);
    const sauver = () => { memoire.ecrire("rencontres-onglet", onglet); memoire.ecrire("rencontres-file", file); };
    const couleurs = ["#c2410c", "#0e7490", "#6d3fd1", "#2f8f5b", "#b42318", "#3b63c4", "#8a5a00"];
    const avatar = p => { let h = 0; for (const c of p.id) h = (h * 31 + c.charCodeAt(0)) % 997; const a = el("span", "avatar", p.prenom.charAt(0));
      a.style.background = couleurs[h % couleurs.length]; return a; };
    const ajouter = (texte, etiquette) => { file.push(texte + " " + etiquette); sauver(); dessiner(); };
    const guillemets = s => s.replace(/"/g, "'").replace(/\n/g, " ");
    function barreFile() {
      if (!file.length) return null;
      const z = el("div", "carte");
      z.append(el("span", "etiquette", file.length + " action(s) à envoyer dans la simulation"));
      const l = el("ul", "formalites"); file.forEach(x => l.append(el("li", "", x.replace(/\s\[rencontres:.*\]$/, "")))); z.append(l);
      const b = el("button", "bouton", "Copier les actions"); b.type = "button";
      const v = el("button", "bouton discret", "Vider"); v.type = "button";
      b.addEventListener("click", () => copier("Dans l'application de rencontre :\n" + file.map(x => "- " + x).join("\n"), b, z));
      v.addEventListener("click", () => { file = []; sauver(); dessiner(); });
      const r = el("div", "rangee"); r.append(b, v); z.append(r);
      return z;
    }
    function carte(p, actions) {
      const c = el("div", "carte profil");
      const h = el("div", "profil-tete"); const n = el("div");
      n.append(el("strong", "", p.prenom + ", " + p.age + (p.verifie ? " ✓" : "")), el("span", "note", p.quartier + " · " + p.distance + " km · " + p.connexion));
      h.append(avatar(p), n); c.append(h, el("p", "bio", p.bio), el("span", "puce", p.cherche));
      if (actions) c.append(actions);
      return c;
    }
    function inscription() {
      ui.titre("Rencontres", "Crée ton profil pour commencer");
      const f = el("div", "formulaire");
      const bio = el("textarea", "copie"); bio.placeholder = "Ta présentation (en anglais ou en français)"; bio.id = "r-bio";
      const lb = el("label", "", "Présentation"); lb.htmlFor = "r-bio";
      const cb = el("div", "champ large"); cb.append(lb, bio);
      const ab = el("select"); ab.id = "r-ab";
      [["plus", "Plus, mode voyage (" + euros(R.prix_plus) + " par mois)"], ["gratuit", "Gratuit (profils autour de toi)"]].forEach(([v, t]) => { const o = el("option", "", t); o.value = v; ab.append(o); });
      const la = el("label", "", "Abonnement"); la.htmlFor = "r-ab"; const ca = el("div", "champ large"); ca.append(la, ab);
      f.append(cb, ca);
      main.append(el("p", "note", "Recherche : femmes de 18 à 40 ans · ville : Manille. Voir une autre ville que la sienne demande le mode voyage (abonnement Plus)."), f);
      const b = el("button", "bouton", "Préparer l'inscription"); b.type = "button";
      b.addEventListener("click", () => {
        if (!bio.value.trim()) { bio.focus(); return; }
        ajouter("Je m'inscris (" + (ab.value === "plus" ? "abonnement Plus, mode voyage sur Manille" : "gratuit") + "), présentation : « " + bio.value.trim() + " »",
          "[rencontres: inscription abonnement=" + ab.value + " ville=MNL bio=\"" + guillemets(bio.value.trim()) + "\"]");
      });
      main.append(b);
    }
    function decouvrir() {
      const liste = R.profils.filter(p => p.statut === "nouveau" || p.statut === "vu");
      if (R.likes_recus) main.append(el("p", "note", "♥ " + R.likes_recus + (R.likes_recus > 1 ? " personnes t'ont aimé" : " personne t'a aimé")
        + " : un « j'aime » en retour fait un match immédiat. Leurs profils sont parmi ceux à découvrir."));
      if (!liste.length) return main.append(vide("Plus personne pour l'instant", "Reviens plus tard : de nouveaux profils arrivent."));
      liste.forEach(p => {
        const enFile = file.some(x => x.includes("id=" + p.id + "]"));
        const r = el("div", "rangee");
        const oui = el("button", "bouton", enFile ? "Ajouté" : "J'aime"), non = el("button", "bouton discret", "Passer");
        oui.type = non.type = "button"; oui.disabled = non.disabled = enFile;
        oui.addEventListener("click", () => ajouter("J'aime le profil de " + p.prenom + " (" + p.age + " ans, " + p.quartier + ")", "[rencontres: aimer id=" + p.id + "]"));
        non.addEventListener("click", () => ajouter("Je passe le profil de " + p.prenom, "[rencontres: passer id=" + p.id + "]"));
        r.append(oui, non); main.append(carte(p, r));
      });
    }
    function aimes() {
      const liste = R.profils.filter(p => p.statut === "aime" || p.statut === "match");
      if (!liste.length) return main.append(vide("Aucun « j'aime » pour l'instant", "Les profils que tu aimes apparaîtront ici, avec les matchs."));
      liste.forEach(p => main.append(carte(p, el("span", p.statut === "match" ? "puce match" : "note", p.statut === "match" ? "C'est un match : tu peux lui écrire" : "En attente"))));
    }
    function discussions() {
      const liste = R.profils.filter(p => p.statut === "match" || p.statut === "conversation");
      if (!liste.length) return main.append(vide("Aucune discussion", "Après un match, la conversation s'ouvre ici."));
      liste.forEach(p => {
        const fil = R.discussions[p.id] || [];
        const c = carte(p, null);
        const f = el("div", "fil");
        fil.forEach(m => { const b = el("div", "bulle" + (m.moi ? " moi" : ""), m.texte); b.append(el("small", "", dateFr(m.date) + " " + m.heure)); f.append(b); });
        const t = el("textarea", "copie"); t.placeholder = "Écrire à " + p.prenom;
        const b = el("button", "bouton", "Préparer le message"); b.type = "button";
        b.addEventListener("click", () => { if (!t.value.trim()) return t.focus();
          ajouter("Message à " + p.prenom + " : « " + t.value.trim() + " »", "[rencontres: message id=" + p.id + " texte=\"" + guillemets(t.value.trim()) + "\"]"); });
        c.append(f, t, b); main.append(c);
      });
    }
    function profil() {
      const c = R.compte;
      main.append(el("h2", "sec", "Ton profil"), el("p", "", c.bio), el("p", "note", "Inscrit le " + c.inscrit_le + " · " + (c.abonnement === "plus" ? "abonnement Plus (mode voyage)" : "gratuit") + " · " + c.recherche));
    }
    function dessiner() {
      main.replaceChildren();
      const bf = barreFile(); if (bf) main.append(bf);
      if (!R.inscrit) return inscription();
      ui.titre("Rencontres", "Manille · " + R.profils.filter(p => p.statut === "nouveau" || p.statut === "vu").length + " profils à découvrir"
        + (R.likes_recus ? " · ♥ " + R.likes_recus + " j'aime reçu" + (R.likes_recus > 1 ? "s" : "") : ""));
      const tabs = el("div", "onglets-appli");
      [["decouvrir", "Découvrir"], ["aimes", "J'aime"], ["discussions", "Discussions"], ["profil", "Profil"]].forEach(([id, nom]) => {
        const b = el("button", "", nom); b.type = "button"; b.setAttribute("aria-selected", String(onglet === id));
        b.addEventListener("click", () => { onglet = id; sauver(); dessiner(); }); tabs.append(b);
      });
      main.append(tabs);
      ({ decouvrir, aimes, discussions, profil })[onglet]();
    }
    dessiner();
  },
});
