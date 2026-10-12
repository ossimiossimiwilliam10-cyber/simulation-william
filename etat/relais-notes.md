# Notes de passation entre agents (à la main ; une ligne datée par note ; les plus récentes en bas)

> Ce que le prochain agent doit savoir et qui n'est écrit nulle part ailleurs : travail hors fiction en cours, promesses faites à
> l'utilisateur, validations attendues. `relais.py entree` affiche ce fichier ; `relais.py sortie --note "…"` y ajoute une ligne.
> Une note réglée se barre (« ~~…~~ réglé le … »), elle ne s'efface pas.

- ~~(11/10/2026 22:30, Claude Opus 5.5) Redémarrage de l'univers 2 redaté au samedi 14/07/2040, 08h37 (premier vrai jour de vacances,
  demande de l'utilisateur). Le premier tour n'est PAS encore joué : il attend les réponses de l'utilisateur aux questions de
  biographie (etat/fils-ouverts.md, C) et sa décision sur les propositions (memoire/propositions-2026-10-11.md).~~ Réglé le
  12/10/2026 : réponses appliquées ; les propositions seront présentées à la revue n° 1 (lundi 16/07/2040).
- (11/10/2026 22:30, Claude Opus 5.5) Infrastructure installée le 11/10/2026 : relais (relais.py, maitres.py, AGENTS.md,
  préférences dans memoire/preferences-utilisateur.md, dernier tour dans etat/dernier-tour.md), base de données (base.py),
  orchestrateur (tour.py), météo, lieux, faits, prix, échéancier, corps, fronts, générateur de personnages, rituels,
  téléphone de William (telephone.py). Index : outils/LISEZMOI.md.
- (11/10/2026 22:35, Claude Opus 5.5) Page « Téléphone de William » publiée (privée) : https://claude.ai/artifact/VJkYBmpJTrVarDVTs24MsS
  (adresse aussi dans etat/relais-config.json) ; la republier au même endroit après `python outils/telephone.py` (fin de journée ou à la demande).
- (12/10/2026, Claude Opus 5.5) Réponses de biographie appliquées : prêt PR1 (`outils/prets.py`), échéancier complet,
  virements permanents, Minett Combat Club, entourage de 43 personnes en statut `pre_genere` : à faire entrer en scène par
  `personnage.py apparait`, JAMAIS nommé ni listé au joueur avant (préférence de l'utilisateur). Précisions facultatives pour la
  revue n° 1 : etat/fils-ouverts.md, C2.
- (12/10/2026, Claude Opus 5.5) Nouvelle règle §14 (demande de l'utilisateur) : à chaque besoin qui a demandé des recherches, créer une application du téléphone (données dans donnees/, calcul déterministe dans outils/, affichage dans outils/telephone_web/). En place : Calendrier et Voyages (vols, hôtels, forfaits, formalités vers Yaoundé). Une réservation copiée depuis l'application se joue avec `voyages.py` (même prix), puis grand livre et agenda. Page republiée à chaque tour.
- (12/10/2026, Claude Opus 5.5) Hors fiction : l'utilisateur annonce que William part à Manille pour du tourisme sexuel (femmes majeures). Réponse donnée : le moteur le joue (§11) avec ses limites (règle 10 et limites a à f : jamais de mineure, scènes jusqu'au seuil puis ellipse, aucun mode d'emploi réel, lieux fictifs) ; faits F055 à F057 ; table T20 proposée (memoire/propositions-2026-10-11.md, P15) : à valider par l'utilisateur AVANT la première scène de ce type.
- (12/10/2026, Claude Opus 5.5) T20a et T20b validées par l'utilisateur et installées (`jet.py --table T20a --pour "Nom"`). Avant la première scène à Manille : ajouter les données de population des Philippines au générateur (zone, prénoms, noms, contexte « rencontre_manille » avec des âges de 18 ans au moins), pour que chaque personne soit tirée, inscrite et datée.
- (12/10/2026, Claude Opus 5.5) **PASSATION DU 12/10/2026 (fin de la session Claude)** : l'utilisateur change d'agent (limite
  d'utilisation). La partie est au samedi 14/07/2040, 10h20, chez William (tour n° 4 joué) : rien n'est réservé pour Manille
  (vols 20/07 – 31/08 comparés dans l'application Voyages ; séjour de 41 nuits : prolongation au-delà de 30 jours). Ce qui a
  été construit pour toi : applications du téléphone (Banque configurable, Rencontres, Santé, Météo multi-stations, Voyages avec
  Manille), `outils/etiquettes.py` (APPLIQUE les textes copiés depuis le téléphone : lance-le dès qu'un message du joueur contient
  « [voyages: … », « [banque: … » ou « [rencontres: … »), population des Philippines pour `personnage.py` (contextes
  appli_rencontre_manille, rencontre_manille, commerce_manille), 24 profils de rencontre tirés à Manille (intention cachée
  dans `etat/rencontres.csv`), fériés philippins, météo de Manille (`etat/meteo-manille.csv` se remplit à l'arrivée : régler
  l'horloge avec `--fuseau manille`). À VALIDER par l'utilisateur avant de jouer un « j'aime » : T21a et T21b
  (`memoire/propositions-2026-10-11.md`, P16) ; sans validation, ne pas tirer de match à l'intuition (règle 17) : demander.
  Revue du lundi n° 1 le 16/07/2040 : propositions P01 à P21. Le téléphone : `python outils/telephone.py` (fait par
  `tour.py fin`) ; un agent autre que Claude ne peut pas le publier sur claude.ai : envoyer `sorties/telephone/index.html` au joueur
  s'il le demande.
