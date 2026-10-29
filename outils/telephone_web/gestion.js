/* Gestion : l'application de gestion de William (outils/gestion.py) v3.0 (23/08/2041 : écran simple par défaut : conseiller, finances,
   documents, à venir, avec liens vers Messages, Banque, Fichiers et Calendrier ; les onglets ci-dessous sont sous « Toutes les options »).
   Avant : v2.0.
   Refonte ergonomique complète : 6 onglets structurés :
   1. Tableau (Dashboard, budget API, pôles, Open Banking Spuerkeess)
   2. Équipes & Notes (Fiches collaborateurs, suivi dynamique, historique et alertes d'érosion)
   3. Évaluation William (Module souverain miroir, confidentiel, note globale et recommandations)
   4. Candidatures (Vivier RH, annonces et candidats)
   5. Juridique (Gouvernance, pyramide des 3 niveaux de contrats, conformité)
   6. Documents (Preuves PDF physiques, visualiseur intégré et téléchargement) */
appli({
  id: "gestion", nom: "Gestion", couleur: "var(--app-gestion)",
  icone: '<svg viewBox="0 0 24 24"><path d="M4 7h16v12H4z"/><path d="M9 7V5h6v2"/><path d="M4 12h16"/></svg>',
  ouvrir(main, ui) {
    const G = D.applis.gestion;
    const choix = [
      ["simple", "Accueil"],
      ["tableau", "Tableau"],
      ["collaborateurs", "Équipes & Notes"],
      ["souverain", "Évaluation William"],
      ["rh", "Candidatures"],
      ["juridique", "Juridique"],
      ["documents", "Documents"]
    ];
    let onglet = memoire.lire("gestion-onglet", G.simple ? "simple" : "tableau");
    if (!choix.some(c => c[0] === onglet) || (onglet === "simple" && !G.simple)) onglet = G.simple ? "simple" : "tableau";
    ui.titre("Gestion", "Version " + G.version + " · Pilotage Stratégique SOLEIL B2B CI");
    const euro = n => n.toLocaleString("fr-FR", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " €";
    const ligne = (titre, quand, sous) => {
      const g = el("div", "ligne");
      g.append(el("span", "titre", titre), el("span", "quand", quand || ""));
      if (sous) { const s = el("span", "sous", sous); s.style.whiteSpace = "pre-line"; g.append(s); }
      return g;
    };

    // ACCUEIL SIMPLE (version 3.0, 23/08/2041) : le conseiller, les documents, la situation financière, ce qui vient
    const fcfa = n => Math.round(n).toLocaleString("fr-FR").replace(/[  ]/g, " ") + " FCFA";
    const bouton = (texte, action) => { const b = el("button", "bouton", texte); b.type = "button"; b.addEventListener("click", action); return b; };
    const simple = z => {
      const conv = (D.conversations || []).find(c => c.nom === "Agent central");
      const cc = el("div", "carte");
      cc.append(el("span", "etiquette", "Mon conseiller"));
      if (conv && conv.messages.length) {
        const m = [...conv.messages].reverse().find(x => !x.moi) || conv.messages[conv.messages.length - 1];
        cc.append(el("span", "quand", dateFr(m.date) + " " + m.heure), el("span", "sous", m.texte.length > 420 ? m.texte.slice(0, 420) + "…" : m.texte));
      } else cc.append(el("span", "sous", "Aucun échange pour l'instant."));
      cc.append(bouton("Écrire à mon conseiller", () => { memoire.ecrire("messages-ouvrir", "Agent central"); ouvrir("messages"); }));
      z.append(cc);

      const F = G.finances;
      const cf = el("div", "carte solde");
      cf.append(el("span", "etiquette", "Situation financière de SOLEIL B2B CI"));
      if (F) {
        cf.append(el("span", "chiffre", fcfa(F.reste)), el("span", "sous", "≈ " + euros(F.reste / F.eur, 0) + " disponibles après les engagements connus"));
        const l = el("div", "liste");
        l.append(ligne("Apports reçus", fcfa(F.apports)), ligne("Dépenses engagées", fcfa(F.depenses)),
          ligne("Charge mensuelle prévue", fcfa(F.mensuel), "salaires chargés et loyer, une fois l'équipe en poste"));
        F.prevus.forEach(p => l.append(ligne(p.poste, dateFr(p.date), fcfa(p.montant))));
        if (F.a_confirmer.length) l.append(ligne("À confirmer", "", F.a_confirmer.join("\n")));
        cf.append(l);
      } else cf.append(el("span", "sous", "Situation indisponible."));
      cf.append(bouton("Voir mes comptes (Banque)", () => ouvrir("banque")));
      z.append(cf);

      const cd = el("div", "carte");
      cd.append(el("span", "etiquette", "Derniers documents"));
      const ld = el("div", "liste");
      (G.documents || []).slice(0, 5).forEach(d => {
        const g = ligne(d.objet, d.date, d.expediteur);
        if (d.url || d.lien) { const a = el("a"); a.href = d.url || d.lien; a.target = "_blank"; a.rel = "noopener"; a.append(g); ld.append(a); } else ld.append(g);
      });
      if (!(G.documents || []).length) ld.append(el("span", "sous", "Aucun document."));
      cd.append(ld, bouton("Tous mes fichiers", () => ouvrir("fichiers")));
      z.append(cd);

      const cv = el("div", "carte");
      cv.append(el("span", "etiquette", "À venir"));
      const lv = el("div", "liste");
      (G.a_venir || []).forEach(a => lv.append(ligne(a.quoi, dateFr(a.date) + (a.heure ? " " + a.heure : ""), a.qui)));
      if (!(G.a_venir || []).length) lv.append(el("span", "sous", "Rien de prévu."));
      cv.append(lv, bouton("Ouvrir le calendrier", () => ouvrir("calendrier")));
      z.append(cv);

      const plus = bouton("Toutes les options", () => { memoire.ecrire("gestion-onglet", "tableau"); onglet = "tableau"; dessiner(); });
      plus.classList.add("discret");
      z.append(plus);
    };

    // TAB 1: TABLEAU DE BORD & VUE D'ENSEMBLE
    const tableau = z => {
      // Carte d'identité de l'entreprise
      const idCard = el("div", "carte");
      idCard.append(
        el("span", "etiquette", "Entreprise en formation"),
        el("span", "chiffre", "SOLEIL B2B CÔTE D'IVOIRE SASU"),
        el("span", "sous", "SASU de droit OHADA · Capital 10 000 000 FCFA (15 245 €)\nAssocié unique : William Ossimi (Associé non-gérant / Investisseur, +352)\nPrésident-Directeur Général : Mohamed Coulibaly")
      );
      z.append(idCard);

      // Carte Open Banking Spuerkeess
      if (G.open_banking) {
        const obCard = el("div", "carte");
        obCard.append(
          el("span", "etiquette", "Supervision Financière & Open Banking"),
          el("span", "chiffre", G.open_banking.statut),
          el("span", "sous", "Mode : " + G.open_banking.mode + "\nComptes agrégés : Banque Spuerkeess (Zebra Premium & Livret Projet)\nSanctuarisation : Zéro cautionnement personnel · Responsabilité limitée à la souscription initiale")
        );
        z.append(obCard);
      }

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
      if (G.agents && G.agents.length) {
        z.append(el("h2", "sec", "Organisation virtuelle (Agents IA)"));
        const ag = el("div", "liste");
        G.agents.forEach(a => {
          ag.append(ligne(a.pole, a.statut === "connecté" ? "Connecté" : "À créer", (a.agent || "Agent à créer") + (a.note ? "\n" + a.note : "")));
        });
        z.append(ag, el("p", "note", "Supervision globale par la Direction Générale virtuelle. Rapport quotidien unique adressé à William à 20h00."));
      }
    };

    // TAB 2: ÉQUIPES & FICHES COLLABORATEURS
    const collaborateurs = z => {
      const introCard = el("div", "carte");
      introCard.append(
        el("span", "etiquette", "Gouvernance des Talents & Performance"),
        el("span", "chiffre", "Fiches Collaborateurs & Suivi Dynamique"),
        el("span", "sous", "Actualisation hebdomadaire par les rapports de direction (mardi & vendredi)\nBarème sur 100 points · Alerte automatique en cas d'érosion de note")
      );
      z.append(introCard);

      z.append(el("h2", "sec", "Membres de l'entreprise & Postes (" + (G.collaborateurs ? G.collaborateurs.length : 0) + ")"));
      if (!G.collaborateurs || !G.collaborateurs.length) {
        z.append(vide("Aucun collaborateur", "Les profils de direction et d'équipe apparaîtront ici."));
        return;
      }

      const lc = el("div", "liste");
      G.collaborateurs.forEach(col => {
        const item = el("div", "carte");
        item.style.cssText = "display:grid;gap:6px;cursor:pointer;margin-bottom:8px";

        const haut = el("div", "ligne");
        haut.style.padding = "0";

        let noteBadge = "";
        let badgeStyle = "padding:2px 8px;border-radius:10px;font-size:12px;font-weight:600;";
        if (col.note > 0) {
          if (col.variation === "baisse") {
            badgeStyle += "background:#fee2e2;color:#b91c1c;";
            noteBadge = " ▼ " + col.note + " / 100 [Alerte Érosion]";
          } else if (col.variation === "hausse") {
            badgeStyle += "background:#dcfce7;color:#15803d;";
            noteBadge = " ▲ " + col.note + " / 100 [Progression]";
          } else {
            badgeStyle += "background:var(--accent-doux);color:var(--accent);";
            noteBadge = " = " + col.note + " / 100 [Stable]";
          }
        } else {
          badgeStyle += "background:#f1f5f9;color:#64748b;";
          noteBadge = " [En sourcing]";
        }

        const bEl = el("span", "", noteBadge);
        bEl.style.cssText = badgeStyle;

        haut.append(
          el("span", "titre", col.nom),
          bEl
        );
        item.append(haut);

        const sous = el("span", "sous", col.role + " · " + col.pole + " (" + col.niveau + ")\nStatut : " + col.statut);
        item.append(sous);

        // Section détaillée
        const detailBox = el("div", "carte");
        detailBox.style.cssText = "background:var(--fond);padding:10px;margin-top:4px;display:grid;gap:8px;font-size:13px;border-left:3px solid var(--accent);";

        const accBox = el("div", "");
        accBox.append(
          el("strong", "", "Accomplissements récents : "),
          el("span", "", col.accomplissements || "En cours de déploiement.")
        );

        const vigBox = el("div", "");
        vigBox.append(
          el("strong", "", "Points de vigilance & axes de progrès : "),
          el("span", "", col.points_vigilance || "Aucun manquement signalé.")
        );

        const dateBox = el("div", "note", "Dernière révision : " + (col.date_maj || "Août 2041") + " · Source : direction & pôle virtuel");

        detailBox.append(accBox, vigBox, dateBox);
        item.append(detailBox);

        lc.append(item);
      });
      z.append(lc);
    };

    // TAB 3: ÉVALUATION SOUVERAINE DE L'ASSOCIÉ UNIQUE (WILLIAM OSSIMI)
    const souverain = z => {
      const secCard = el("div", "carte");
      secCard.style.cssText = "background:linear-gradient(135deg, rgba(20,83,45,0.08), rgba(30,58,138,0.08));border:1px solid var(--accent);";
      secCard.append(
        el("span", "etiquette", "Accès Exclusif & Confidentiel · Associé Unique"),
        el("span", "chiffre", "Évaluation Miroir de la Gouvernance"),
        el("span", "sous", "Système d'évaluation autonome piloté par le pôle virtuel souverain.\nDonnées strictement privées · Inaccessibles aux équipes d'Abidjan et aux tiers.")
      );
      z.append(secCard);

      if (!G.evaluation_william) {
        z.append(vide("Évaluation en cours", "Le pôle virtuel compile les premières métriques de gouvernance."));
        return;
      }

      const ev = G.evaluation_william;

      // Carte note globale
      const noteCard = el("div", "carte solde");
      noteCard.append(
        el("span", "nom", "Note Stratégique Globale de William Ossimi"),
        el("span", "chiffre", ev.note_globale + " / 100")
      );

      const barre = el("div", "");
      barre.style.cssText = "height:10px;border-radius:5px;background:var(--accent-doux);overflow:hidden;margin-top:6px";
      const rempli = el("div", "");
      rempli.style.cssText = "height:100%;background:#16a34a;width:" + ev.note_globale + "%";
      barre.append(rempli);
      noteCard.append(barre, el("span", "sous", "Mention : Excellence Managériale & Rigueur Patrimoniale · Mise à jour le " + dateFr(ev.date)));
      z.append(noteCard);

      // Détail des sous-scores
      z.append(el("h2", "sec", "Piliers d'évaluation du dirigeant-investisseur"));
      const lScores = el("div", "liste");
      lScores.append(
        ligne("Gouvernance & Clarté des Ordres", ev.score_gouvernance + " / 100", "Qualité du cadrage des 3 maquettes, respect de l'autorité déléguée au PDG, absence d'immixtion fautive."),
        ligne("Gestion Financière & Étanchéité", ev.score_finances + " / 100", "Liaison Open Banking Spuerkeess, plafonnement strict au capital de 10 M FCFA, zéro caution personnelle."),
        ligne("Anticipation Stratégique & Risque", ev.score_strategie + " / 100", "Intégration d'un analyste quantitatif au pôle finance, scoring PPA, préparation de la mission terrain.")
      );
      z.append(lScores);

      // Accomplissements
      z.append(el("h2", "sec", "Accomplissements de l'Associé Unique"));
      const accCard = el("div", "carte");
      accCard.style.cssText = "border-left:3px solid #16a34a;background:var(--fond);";
      accCard.append(el("span", "sous", ev.accomplissements));
      z.append(accCard);

      // Recommandation corrective
      z.append(el("h2", "sec", "Recommandation stratégique corrective"));
      const recCard = el("div", "carte");
      recCard.style.cssText = "border-left:3px solid #f59e0b;background:var(--fond);";
      recCard.append(el("span", "sous", ev.recommandation_corrective));
      z.append(recCard);
    };

    // TAB 4: CANDIDATURES & RECRUTEMENT
    const rh = z => {
      // Carte du poste
      const postCard = el("div", "carte");
      postCard.append(
        el("span", "etiquette", "Poste stratégique pourvu"),
        el("span", "chiffre", G.poste.intitule),
        el("span", "sous", "Forme : " + G.poste.forme + "\nTitulaire désigné : Mohamed Coulibaly (Signature notariée 13/08)\nRémunération : Formule 1 (Fixe 2 M FCFA net + variable 2,5 % CA encaissé + prime 5 M FCFA / 500 kWc)\nRévocation : Caducité automatique sur seuils trimestriels (Option C)\nProtection : Non-concurrence 12 mois sans indemnité + clause pénale 12 mois de fixe (Option A)")
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

    // TAB 5: JURIDIQUE, GOUVERNANCE & SOURCES
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
        ligne("Niveau 1 : Directeur Général", "Mandat social pur", "Convention de mandat social OHADA (19 articles rédigés). Révocabilité ad nutum, caducité sur objectifs stricts, clause de non-concurrence 12 mois sans indemnité. Mis en place directement par l'associé unique.\nPièce officielle signée chez Me Gnamien le 13/08."),
        ligne("Niveau 2 : Directeurs de pôle", "Cadres dirigeants", "Directeur Technique (Éric Yao validé), Directrice Administrative et Financière (Mariam Brou validée), Directeur Commercial B2B (en sourcing > 80). Contrats de travail de cadres salariés (Code du travail ivoirien)."),
        ligne("Niveau 3 : Collaborateurs & Techniciens", "Salariés d'exécution", "Chef d'équipe travaux (N3 >= 80), techniciens installateurs toiture et commerciaux juniors (N4 jeunes < 30 ans, 75-85 avec fort potentiel). Contrats de travail adaptés (sécurité toiture, commissions).")
      );
      z.append(lContrats);

      // Sources officielles de référence
      z.append(el("h2", "sec", "Textes et sources de conformité"));
      const ls = el("div", "liste");
      G.sources.forEach(x => ls.append(ligne(x.titre, "Pôle " + x.pole, x.reference)));
      z.append(ls);
    };

    // TAB 6: DOCUMENTS & PREUVES PDF
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
      choix.filter(([id]) => id !== "simple" || G.simple).forEach(([id, nom]) => {
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
      tabs.hidden = onglet === "simple";
      ({ simple, tableau, collaborateurs, souverain, rh, juridique, documents }[onglet])(zone);
    };
    main.append(tabs, zone);
    dessiner();
  },
});
