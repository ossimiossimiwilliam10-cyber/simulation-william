/* Fichiers : les PDF que William a en main (documents rédigés ou gardés, pièces reçues), classés par date ; un appui ouvre le PDF DANS la page
   (lecteur pdf.js : le fichier publié avec la page est lu par la page, sans changer d'adresse). Les fichiers sont publiés avec la page
   (telephone.py --fichiers) ; seuls ceux datés d'aujourd'hui ou d'avant sont listés. */
function lecteurPdf(main, ui, f, retour, libelleRetour) {
  main.replaceChildren(); ui.titre(f.nom, f.dossier + " · " + dateFr(f.date));
  const r = el("button", "retour", "‹ " + libelleRetour); r.type = "button"; r.addEventListener("click", retour); main.append(r);
  const outils = el("div", "outils-lecteur"), zone = el("div", "lecteur");
  const etat = el("span", "sous", "Ouverture du fichier…");
  let zoom = 1; const toiles = [];
  const regler = () => toiles.forEach(c => { c.style.width = (100 * zoom) + "%"; });
  const bouton = (txt, fn) => { const b = el("button", "bouton discret", txt); b.type = "button"; b.addEventListener("click", fn); return b; };
  outils.append(bouton("− Réduire", () => { zoom = Math.max(1, zoom - 0.5); regler(); }), bouton("+ Agrandir", () => { zoom = Math.min(4, zoom + 0.5); regler(); }), etat);
  main.append(outils, zone);
  const echec = msg => { zone.replaceChildren(vide("Ce fichier ne s'ouvre pas ici", msg + " Demande-le dans la conversation : « envoie-moi " + f.fichier + " ».")); etat.textContent = ""; };
  (async () => {
    try {
      if (!window.pdfjsLib) throw new Error("lecteur indisponible");
      pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";
      const rep = await fetch(f.url);
      if (!rep.ok) throw new Error("fichier introuvable (" + rep.status + ")");
      const pdf = await pdfjsLib.getDocument({ data: await rep.arrayBuffer() }).promise;
      const largeur = Math.max(280, Math.min(zone.clientWidth || 360, 900));
      const densite = Math.min(window.devicePixelRatio || 1, 2) * 2; /* net jusqu'à un agrandissement x2 */
      zone.replaceChildren();
      for (let n = 1; n <= pdf.numPages; n++) {
        const page = await pdf.getPage(n);
        const base = page.getViewport({ scale: 1 });
        const v = page.getViewport({ scale: (largeur / base.width) * densite });
        const toile = document.createElement("canvas"); toile.width = Math.round(v.width); toile.height = Math.round(v.height);
        toile.setAttribute("role", "img"); toile.setAttribute("aria-label", f.nom + ", page " + n);
        toiles.push(toile); zone.append(toile); regler();
        await page.render({ canvasContext: toile.getContext("2d"), viewport: v }).promise;
        etat.textContent = "Page " + n + " sur " + pdf.numPages;
      }
      etat.textContent = pdf.numPages + " page(s)";
    } catch (e) { echec("(" + (e && e.message ? e.message : "erreur") + ")"); }
  })();
}

appli({
  id: "fichiers", nom: "Fichiers", couleur: "var(--app-fichiers)",
  icone: '<svg viewBox="0 0 24 24"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>',
  ouvrir(main, ui) {
    const tous = D.fichiers || [];
    const choix = [["tous", "Tous"], ["Documents", "Documents"], ["Reçus", "Reçus"]];
    let dossier = memoire.lire("fichiers-dossier", "tous");
    if (!choix.some(c => c[0] === dossier)) dossier = "tous";
    const liste = () => {
      main.replaceChildren();
      ui.titre("Fichiers", tous.length ? tous.length + " fichier(s)" : "Aucun fichier");
      if (!tous.length) return main.append(vide("Aucun fichier", "Les documents de William et les pièces reçues apparaîtront ici."));
      const onglets = el("div", "onglets-appli onglets-3"), zone = el("div", "");
      const dessiner = () => {
        onglets.replaceChildren();
        choix.forEach(([id, nom]) => {
          const b = el("button", "", nom); b.type = "button"; b.setAttribute("aria-selected", String(dossier === id));
          b.addEventListener("click", () => { dossier = id; memoire.ecrire("fichiers-dossier", id); dessiner(); });
          onglets.append(b);
        });
        zone.replaceChildren();
        const lignes = tous.filter(f => dossier === "tous" || f.dossier === dossier);
        if (!lignes.length) return zone.append(vide("Rien dans ce dossier", "Aucun fichier de ce type pour le moment."));
        const l = el("div", "liste");
        lignes.forEach(f => {
          const b = el("button"); b.type = "button"; const g = el("div", "ligne");
          g.append(el("span", "titre", f.nom), el("span", "quand", dateFr(f.date)), el("span", "sous", f.dossier + " · PDF · " + f.ko + " Ko"));
          b.append(g); b.addEventListener("click", () => lecteurPdf(main, ui, f, liste, "Fichiers")); l.append(b);
        });
        zone.append(l);
      };
      main.append(onglets, zone);
      dessiner();
    };
    liste();
  },
});
