/* Messages : conversations de William (whatsapp/), seulement les messages déjà envoyés ou reçus à l'heure du jeu. */
appli({
  id: "messages", nom: "Messages", couleur: "var(--app-messages)",
  icone: '<svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg>',
  badge: () => 0,
  ouvrir(main, ui) {
    const liste = () => {
      main.replaceChildren();
      ui.titre("Messages", D.conversations.length ? D.conversations.length + " conversation(s)" : "Aucune conversation");
      if (!D.conversations.length) return main.append(vide("Aucun message pour l'instant", "Les conversations de William apparaîtront ici dès le premier échange."));
      const l = el("div", "liste");
      D.conversations.forEach((c, i) => {
        const dernier = c.messages[c.messages.length - 1];
        const b = el("button"); b.type = "button"; const g = el("div", "ligne");
        const titre = el("span", "titre", c.nom); if (c.epingle) titre.append(" ", el("span", "puce", "Épinglée"));
        g.append(titre, el("span", "quand", dateFr(dernier.date) + " " + dernier.heure),
          el("span", "sous", (dernier.moi ? "Vous : " : "") + dernier.texte.slice(0, 90)));
        b.append(g); b.addEventListener("click", () => fil(i)); l.append(b);
      });
      main.append(l);
    };
    const fil = i => {
      const c = D.conversations[i]; main.replaceChildren(); ui.titre(c.nom, c.messages.length + " message(s)");
      const r = el("button", "retour", "‹ Conversations"); r.type = "button"; r.addEventListener("click", liste); main.append(r);
      const f = el("div", "fil"); let jourPrec = "";
      c.messages.forEach(m => {
        if (m.date !== jourPrec) { f.append(el("div", "jour-sep", dateFr(m.date))); jourPrec = m.date; }
        const b = el("div", "bulle" + (m.moi ? " moi" : ""), m.texte); b.append(el("small", "", m.heure)); f.append(b);
      });
      main.append(f);
    };
    liste();
  },
});
