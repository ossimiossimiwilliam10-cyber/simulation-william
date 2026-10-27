/* Gestion : l'application de gestion de William (outils/gestion.py) v1.0.
   Refonte ergonomique complète : 4 onglets structurés (Tableau, RH, Juridique, Documents),
   liens directs vers les PDF physiques (ouverture nouvel onglet / lecteur intégré),
   gouvernance en 3 niveaux de contrats et suivi temps réel du budget et des candidatures. */
appli({
  id: "gestion", nom: "Gestion", couleur: "var(--app-gestion)",
  icone: '<svg viewBox="0 0 24 24"><path d="M4 7h16v12H4z"/><path d="M9 7V5h6v2"/><path d="M4 12h16"/></svg>',
  ouvrir(main, ui) {
    const G = D.applis.gestion;
    const choix = [["tableau", "Tableau"], ["rh", "RH"], ["juridique", "Juridique"], ["documents", "Documents"]];
    let onglet = memoire.lire("gestion-onglet", "tableau");
    if (!choix.some(c => c[0] === onglet)) onglet = "tableau";
    ui.titre("Gestion", "Version " + G.version + " · Projet Solaire B2B Abidjan");
    const euro = n => n.toLocaleString("fr-FR", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " €";
    const ligne = (titre, quand, sous) => {
      const g = el("div", "ligne");
      g.append(el("span", "titre", titre), el("span", "quand", quand || ""));
      if (sous) { const s = el("span", "sous", sous); s.style.whiteSpace = "pre-line"; g.append(s); }
      return g;
    };

    // TAB 1: TABLEAU DE BORD & VUE D'ENSEMBLE
    const tableau = z => {
      // Carte d'identité de l'entreprise
      const idCard = el("div", "carte");
      idCard.append(
        el("span", "etiquette", "Entreprise en formation"),
        el("span", "chiffre", "Projet Solaire B2B Abidjan"),
        el("span", "sous", "SAS de droit OHADA · Capital 1 000 000 FCFA · Investissement 300 000 € sur 3 ans\nAssocié unique : William Ossimi (Associé non-gérant / Investisseur, +352)")
      );
      z.append(idCard);

      // Carte de budget d'API
      const part = Math.min(100, 100 * G.depense / G.plafond);
      const b = el("div", "carte solde");
      b.append(
        el("span", "nom", "Budget d'API IA mensuel (plafond " + euro(G.plafond).replace(",00", "") + ")"),
        el("span", "chiffre", euro(G.depense) + " consommés")
      );
      const barre = el("div", "");
      barre.style.cssText = "height:8px;border-radius:4px;background:var(--accent-doux);overflow:hidden;margin-top:6px";
      const rempli = el("div", "");
      rempli.style.cssText = "height:100%;background:var(--accent);width:" + part.toFixed(1) + "%";
      barre.append(rempli);
      b.append(barre, el("span", "sous", "Reste " + euro(G.restant) + (G.estimation ? " · dont " + euro(G.estimation) + " estimés (agents connectés)" : "") + " · Modèle : " + G.modele));
      z.append(b);

      // Section Pôles d'activité
      z.append(el("h2", "sec", "Pôles d'activité"));
      const lp = el("div", "liste");
      G.poles.forEach(p => {
        const statutLabel = p.statut === "actif" ? "Actif" : "En constitution";
        lp.append(ligne(p.nom, statutLabel, p.description));
      });
      z.append(lp);

      // Section Agents IA connectés
      if (G.agents.length) {
        z.append(el("h2", "sec", "Organisation virtuelle (Agents IA)"));
        const ag = el("div", "liste");
        G.agents.forEach(a => {
          ag.append(ligne(a.pole, a.statut === "connecté" ? "Connecté" : "À créer", (a.agent || "Agent à créer") + (a.note ? "\n" + a.note : "")));
        });
        z.append(ag, el("p", "note", "Supervision globale par la Direction Générale virtuelle. Rapport quotidien unique adressé à William à 20h00."));
      }
    };

    // TAB 2: RESSOURCES HUMAINES & RECRUTEMENT
    const rh = z => {
      // Carte du poste
      const postCard = el("div", "carte");
      postCard.append(
        el("span", "etiquette", "Poste stratégique ouvert"),
        el("span", "chiffre", G.poste.intitule),
        el("span", "sous", "Forme : " + G.poste.forme + "\nRémunération : Formule 1 (Fixe 2 M FCFA net + variable 2,5 % CA encaissé + prime 5 M FCFA / 500 kWc)\nRévocation : Caducité automatique sur seuils trimestriels (Option C)\nProtection : Non-concurrence 12 mois sans indemnité + clause pénale 12 mois de fixe (Option A)")
      );
      z.append(postCard);

      // Annonces en ligne
      z.append(el("h2", "sec", "Canaux de diffusion de l'annonce"));
      const la = el("div", "liste");
      G.annonces.forEach(x => la.append(ligne(x.nom, x.etat, "Diffusion ciblée Côte d'Ivoire et diaspora")));
      z.append(la);

      // Candidatures
      z.append(el("h2", "sec", "Vivier de candidatures (" + G.candidats.length + " profils)"));
      if (!G.candidats.length) {
        z.append(el("p", "note", "Aucun candidat pour l'instant."));
      } else {
        const lc = el("div", "liste");
        const tries = [...G.candidats].sort((a, b) => (parseFloat(b.note) || 0) - (parseFloat(a.note) || 0));
        tries.forEach(x => {
          const noteStr = x.note ? x.note + " / 100" : "En cours";
          const badgeType = parseFloat(x.note) >= 80 ? " [Élite]" : (parseFloat(x.note) >= 70 ? " [Qualifié]" : "");
          lc.append(ligne(
            x.nom + " · " + x.niveau + badgeType,
            noteStr,
            (x.etat ? "Statut : " + x.etat + "\n" : "") + x.resume + "\nCanal : " + x.plateforme + " · Reçu le " + dateFr(x.date)
          ));
        });
        z.append(lc);
      }
    };

    // TAB 3: JURIDIQUE, GOUVERNANCE & SOURCES
    const juridique = z => {
      // Carte Gouvernance
      const govCard = el("div", "carte");
      govCard.append(
        el("span", "etiquette", "Cadrage juridique & Gouvernance"),
        el("span", "chiffre", G.gouvernance.forme_sociale),
        el("span", "sous", "Associé unique : " + G.gouvernance.associe_unique + "\nConseil juridique : " + G.gouvernance.avocat_conseil + " (devis 2,1 M FCFA HT validé)\nJuridiction compétente : " + G.gouvernance.tribunal)
      );
      z.append(govCard);

      // Pyramide des 3 types de contrats
      z.append(el("h2", "sec", "Architecture pyramidale des contrats"));
      const lContrats = el("div", "liste");
      lContrats.append(
        ligne("Niveau 1 : Directeur Général", "Mandat social pur", "Convention de mandat social OHADA (19 articles rédigés). Révocabilité ad nutum, caducité sur objectifs stricts, clause de non-concurrence 12 mois sans indemnité. Mis en place directement par l'associé unique.\nMaquette PDF disponible dans l'onglet Documents."),
        ligne("Niveau 2 : Directeurs de pôle", "Cadres dirigeants", "Directeur Technique, Directeur Commercial B2B, Responsable Financier. Contrats de travail de cadres salariés (Code du travail ivoirien). Maquette générale à soumettre par le Directeur Général recruté."),
        ligne("Niveau 3 : Collaborateurs & Techniciens", "Salariés d'exécution", "Techniciens solaires toiture, monteurs électriciens, commerciaux terrain. Contrats de travail adaptés (sécurité toiture, commissions). Maquettes sectorielles élaborées par chaque directeur de pôle.")
      );
      z.append(lContrats);

      // Sources officielles de référence
      z.append(el("h2", "sec", "Textes et sources de conformité"));
      const ls = el("div", "liste");
      G.sources.forEach(x => ls.append(ligne(x.titre, "Pôle " + x.pole, x.reference)));
      z.append(ls);
    };

    // TAB 4: DOCUMENTS & PREUVES PDF
    const documents = z => {
      z.append(el("h2", "sec", "Documents d'entreprise & Preuves PDF (" + G.documents.length + " pièces)"));
      if (!G.documents.length) {
        return z.append(vide("Aucun document", "Les documents envoyés par les collaborateurs et validés apparaîtront ici."));
      }

      // Filtres par pôle
      let filtrePole = memoire.lire("gestion-doc-pole", "tous");
      const polesDispo = ["tous", ...new Set(G.documents.map(d => d.pole))];
      const barreFiltres = el("div", "outils-lecteur");
      barreFiltres.style.marginBottom = "6px";
      polesDispo.forEach(p => {
        const label = p === "tous" ? "Tous" : (p.charAt(0).toUpperCase() + p.slice(1));
        const b = el("button", "bouton" + (filtrePole === p ? "" : " discret"), label);
        b.type = "button";
        b.style.padding = "4px 10px";
        b.style.fontSize = "12px";
        b.addEventListener("click", () => {
          filtrePole = p;
          memoire.ecrire("gestion-doc-pole", p);
          dessiner();
        });
        barreFiltres.append(b);
      });
      z.append(barreFiltres);

      const l = el("div", "");
      l.style.display = "grid";
      l.style.gap = "10px";
      const docsFiltres = G.documents.filter(d => filtrePole === "tous" || d.pole === filtrePole);
      if (!docsFiltres.length) {
        z.append(vide("Aucun document dans ce pôle", "Aucune pièce répertoriée pour ce filtre."));
        return;
      }

      docsFiltres.forEach(d => {
        const item = el("div", "carte");
        item.style.display = "grid";
        item.style.gap = "6px";

        const haut = el("div", "ligne");
        haut.style.padding = "0";
        haut.append(
          el("span", "titre", d.objet),
          el("span", "quand", dateFr(d.date))
        );
        item.append(haut);

        const sous = el("span", "sous", "Émetteur : " + d.expediteur + " · Pôle : " + d.pole + " · Statut : " + d.statut + (d.cout ? " (" + euro(d.cout) + ")" : ""));
        item.append(sous);

        if (d.retour) {
          const analyseBox = el("div", "carte");
          analyseBox.style.background = "var(--fond)";
          analyseBox.style.padding = "8px 10px";
          analyseBox.style.fontSize = "13px";
          analyseBox.style.borderLeft = "3px solid var(--accent)";
          analyseBox.append(el("span", "", d.retour));
          item.append(analyseBox);
        }

        // Actions PDF
        if (d.lien || d.url) {
          const actionBox = el("div", "outils-lecteur");
          actionBox.style.marginTop = "4px";

          // Lien direct pour ouvrir le fichier dans un nouvel onglet
          const lienDirect = el("a", "bouton", "📄 Ouvrir le PDF (" + (d.ko ? d.ko + " Ko" : "PDF") + ")");
          lienDirect.href = typeof adresseFichier === "function" ? adresseFichier(d.lien) : d.lien;
          lienDirect.target = "_blank";
          lienDirect.rel = "noopener";
          lienDirect.style.textDecoration = "none";
          lienDirect.style.padding = "6px 12px";
          lienDirect.style.fontSize = "13px";
          actionBox.append(lienDirect);

          // Bouton pour visionner dans le lecteur intégré de l'app si disponible
          if (typeof lecteurPdf === "function") {
            const btnLecteur = el("button", "bouton discret", "👁 Aperçu dans l'app");
            btnLecteur.type = "button";
            btnLecteur.style.padding = "6px 12px";
            btnLecteur.style.fontSize = "13px";
            btnLecteur.addEventListener("click", () => {
              const fileObj = {
                nom: d.objet,
                fichier: d.fichier,
                dossier: d.dossier || "Documents",
                date: d.date,
                url: d.url || ("fichiers/documents_william/" + d.fichier)
              };
              lecteurPdf(main, ui, fileObj, () => {
                ouvrir("gestion");
              }, "Gestion");
            });
            actionBox.append(btnLecteur);
          }

          item.append(actionBox);
        } else {
          item.append(el("span", "note", "Pièce textuelle enregistrée au registre."));
        }

        l.append(item);
      });
      z.append(l);
    };

    const tabs = el("div", "onglets-appli"), zone = el("div", "");
    const dessiner = () => {
      tabs.replaceChildren();
      choix.forEach(([id, nom]) => {
        const b = el("button", "", nom);
        b.type = "button";
        b.setAttribute("aria-selected", String(onglet === id));
        b.addEventListener("click", () => {
          onglet = id;
          memoire.ecrire("gestion-onglet", id);
          dessiner();
        });
        tabs.append(b);
      });
      zone.replaceChildren();
      zone.style.display = "grid";
      zone.style.gap = "14px";
      ({ tableau, rh, juridique, documents }[onglet])(zone);
    };
    main.append(tabs, zone);
    dessiner();
  },
});
