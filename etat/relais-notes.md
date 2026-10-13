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
- ~~(11/10/2026 22:35, Claude Opus 5.5) Page « Téléphone de William » publiée (privée) : https://claude.ai/artifact/VJkYBmpJTrVarDVTs24MsS
  (adresse aussi dans etat/relais-config.json) ; la republier au même endroit après `python outils/telephone.py` (fin de journée ou à la demande).~~
  Réglé le 12/10/2026 : cette adresse n'existe plus (« Page not found ») ; nouvelle adresse dans la note du 12/10/2026, 10h45, ci-dessous.
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
- (12/10/2026 10:45, Claude Opus 5.5) **Téléphone de William republié à une NOUVELLE adresse** : https://claude.ai/artifact/9j5a5bgQy9De1sxL7LZ27z
  (l'ancienne, VJkYBmpJTrVarDVTs24MsS, affichait « Page not found » sur le téléphone du joueur et n'apparaissait plus dans la
  liste de ses artefacts : cause inconnue). Adresse aussi dans etat/relais-config.json. À chaque tour : `tour.py fin` régénère
  sorties/telephone/index.html ; Claude republie au même URL (paramètre url) après avoir relu la page en entier.
- (13/10/2026, Claude Opus 5.5) **PASSATION DU 13/10/2026 (fin de la session Claude, limite d'utilisation)** : partie au
  **mardi 17/07/2040, 09h16**, chez William (tour n° 15) ; il vient d'avoir un **match avec Kiara Reyes** sur l'application de
  rencontre (discussion ouverte, vide) : attendre son action. Depuis le 12/10 : forfait Manille réservé (vol PVS2HS, City Garden
  Grand Hotel, 18/07 – 24/08, 4 890 € sur la Visa Premier débités au relevé du 07/08), eTravel fait (code QR dans `courriels/`),
  inscription sur l'application de rencontre (Plus, Visa Debit, E016), revue n° 1 TOUT VALIDÉE (tables T15 à T22 installées,
  aléas A19 à A32 actifs).
  **Événements déjà tirés, NON CONNUS de William, à jouer à leur heure (agenda)** : A019 Julia (match et premier message, 17/07
  09h22) ; A013 Clément Grandjean, du club (message spontané, 17/07 09h25 : contenu d'après sa fiche, `personnage.py apparait`) ;
  A015 aléa A09 erreur administrative (17/07 après-midi) ; A020 Hannah (match ≈ 12h50 ; intention cachée : arnaque) ; A021 Shane
  (match et message ≈ 17h40) ; A016 aléa A07 panne réseau (20/07 matin, à Manille) ; A017 aléa A22 courrier administratif par
  courriel (22/07 matin). Intentions permanentes du joueur (`etat/fils-ouverts.md`, A2) : aller à l'aéroport (bus 604 à 11h30 le
  18/07, A018), acheter le billet RegioZone (4,05 € sur la Visa Debit), montrer le code QR, prolonger le séjour vers le 17/08 :
  les exécuter SANS les redemander ; ne plus rappeler les échéances notées (I5).
  **À faire par le moteur avant que ça compte** : franchise de bagages du tarif (recherche avant l'enregistrement du 18/07) ; P19,
  I1, I2 et I3 avant l'arrivée du 19/07 (frais à l'étranger sur les cartes en pesos, caution d'hôtel, décalage horaire de 6 h dans
  `corps.py`, carte SIM, change, taxis ; régler l'horloge avec `--fuseau manille` à l'arrivée) ; P18 dépenses courantes ; P10 paie
  calculée et P17 ETF avant le 31/07 ; revue n° 2 le lundi 23/07 (P14 : audit du casting, faits périmés ; idée I5 : « j'aime »
  spontanés reçus).
  **Outils créés le 12-13/10** : `cartes.py` (plafonds, relevé différé ; voyages et rencontres paient par lui), `transports.py`
  (application Transports), `etravel.py`, `courriel.py` (tout courriel reçu devient un PDF), `rituels.py message-proche`,
  `rencontres.py completer` (âge minimum 18 ans, U2-20). Règle 10 complétée : pas de scène explicite ; au seuil, le joueur peut
  poursuivre ailleurs puis donne l'issue. Téléphone : https://claude.ai/artifact/9j5a5bgQy9De1sxL7LZ27z (seul Claude republie ;
  un autre agent envoie `sorties/telephone/index.html` si le joueur le demande).
