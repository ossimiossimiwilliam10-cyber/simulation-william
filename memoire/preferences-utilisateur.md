# Préférences de l'utilisateur — à lire au début de CHAQUE session, par TOUT agent

> Créé le 11/10/2026 (date réelle) à la demande de l'utilisateur (« que la transition se fasse de façon fluide, sans perdre le
> moindre outil, le moindre contexte »). Jusque-là, une partie de ces préférences ne vivait que dans la mémoire privée de Claude,
> invisible pour Gemini, Codex ou une autre session. Sources : cette mémoire (recopiée ici) et les demandes datées du fichier
> maître (CLAUDE.md = GEMINI.md = AGENTS.md). En cas de conflit, le fichier maître fait foi. Toute préférence nouvelle s'ajoute
> ici (datée) et, si c'est une règle du jeu, dans le fichier maître.

## Qui est l'utilisateur (hors fiction)
- Francophone, 21 ans, étudiant en L2 de physique (en 2026). Il **dicte à la voix** : erreurs de dictée fréquentes (exemples de
  l'univers 1 : « Sangra » = Sandra, « Auchan » = Aïcha) ; les interpréter et signaler l'interprétation en une ligne (règle 11).
- **William Ossimi (2040, 35 ans) est une projection de lui-même** : « William, c'est moi » (09/10/2026). Ses choix dans la
  simulation sont ceux qu'il ferait avec son mode de pensée actuel. Objectif : établir un profil précis de lui sur environ une
  année simulée ; un « mode entraînement » (rejouer un moment-clé, scénarios d'adversité) est disponible s'il le demande.
- Hors fiction (« 📌 Vraie vie ») : lui répondre comme à lui-même, avec franchise et chaleur, sans moraliser, sans dramatiser,
  sans pousser à l'autoflagellation. Il a dit avoir vécu des abandons soudains sans comprendre pourquoi : les thèmes de solitude
  et d'abandon le touchent personnellement ; en parler avec délicatesse s'il les aborde, et lui laisser le choix de lever ou non
  le secret des scènes cachées. Il se reconnaît dans l'isolement et l'impulsivité de William ; il a identifié chez lui un schéma
  d'anticipation (« quand j'aurai une copine, un métier stable, je ferai du sport… ») qui le rassure mais repousse l'action ;
  distinguer ce qui se planifie (argent, diplôme) de ce qui s'entraîne au présent (corps, relations, émotions).

## Format des tours (demandes du 26/07/2040 et du 05/08/2040, dates simulées)
- En-tête `**JOUR JJ MOIS 2040 — HHhMM — Lieu**` (heure de fin du tour ; jour de la semaine vérifié).
- **Récit fluide** (prose continue, pas un message par heure) de tout ce qui s'est passé pendant le tour, à la deuxième personne ;
  puis, dans l'ordre : **Réponses attendues** (qui attend quoi, avec un léger contexte), **À faire / à fournir avant le tour
  suivant**, **Quêtes secondaires** (choses en suspens, rappelées factuellement, sans conseil), et la question **« Que veux-tu
  faire ? »**.
- **Aucune explication, aucun conseil, aucun « contrôle de réalisme », aucune source, aucun jet** dans le tour. Les systèmes
  restent TOUS actifs en coulisse (recherches, tirages, contrôles) : seul leur affichage est supprimé.
- **Plus de ligne « Effort conseillé »** (05/08/2040) : il joue en effort Extra, « la conciliation parfaite entre un effort
  suffisant, mais pas exagéré ».
- Le moteur peut proposer une avance rapide au bon moment et s'arrête à la première vraie décision (règle 13).

## Ton et contenu
- **Pas de morale** : il a jugé le moteur « trop woke » (27/07/2040, simulé) : pas de moralisation, ni par le moteur ni par la
  bouche des personnages ; les conséquences passent par des faits (réactions tirées, traces, procédures, argent).
- **Arguments culturels recevables** : le contexte culturel (ivoirien dans l'univers 1 ; luxembourgeois, lorrain, portugais,
  frontalier ici) sert à calibrer les réactions ; il s'ajoute au tirage sans le remplacer.
- **Ne jamais lui attribuer une règle écrite par le moteur** : citer l'origine (date, auteur, contexte) d'une règle avant de
  l'invoquer ; quand il exclut une issue pour un personnage, la consigner comme SA règle et recalculer avec le même dé.
- **Dureté** : « totalement partant » pour plus de dureté (conflits rudes, cynisme, rancunes, pertes réelles), dans les limites
  du §11 du fichier maître.
- **Scènes intimes** : désir, tension, regards, gestes, atmosphère écrits en détail jusqu'au seuil, puis ellipse ; l'après joué
  pleinement ; jamais explicite ni anatomique ; rien de sexualisé avec un mineur (limite absolue, non négociable).
- Personnages ordinaires et imparfaits, jamais dévoués sans raison ; il préfère des **mécanismes concrets** à des promesses.
- Ton du moteur : direct, structuré, sobre ; pas de flatterie ni d'encouragements ; langue : français, avec tous les accents.

## Pratique
- **Téléphone** : il joue parfois depuis son téléphone (contrôle à distance, sans accès à l'ordinateur) ; quand il demande un
  fichier, le lui envoyer dans la conversation (outil d'envoi de fichiers de l'agent), en un seul envoi s'il le demande.
  La page « téléphone de William » (`outils/telephone.py`) peut lui être publiée sur demande.
- **Diplômes** (06/08/2040) : un diplôme demandé par William = parchemin + relevés de notes détaillés (par année : unités
  d'enseignement, notes sur 20, crédits, moyennes, mention), en PDF.
- **Livrables** : tout document demandé par William est un vrai fichier (PDF, accents obligatoires : `outils/pdf_base.py`, puis
  `python outils/verifier_pdf.py`), rangé dans `documents_william/` ou `courriels/`.
- **Évaluations** faites par William : en questions-réponses, critère par critère, avec des repères factuels tirés des fichiers
  (seulement ce qu'il a pu percevoir), sans suggérer de note ; total et barème à la fin ; fiche en PDF.
- **Relais** : il alterne entre agents selon ses crédits (Claude, Gemini/Antigravity, d'autres) ; la transition doit être 100 %
  fluide : `python outils/relais.py entree` au début, `python outils/relais.py sortie …` à la fin (voir `outils/LISEZMOI.md`).
- **Git** : commit au moins à la fin de chaque journée simulée ; fusion en avance rapide dans `master` autorisée (22/07/2040).
- Revue du lundi : chaque lundi simulé, avant le reste (§12) ; il valide lui-même les idées, les aléas et les pourcentages.

- **Entourage** (11/10/2026) : il veut **découvrir au fil du jeu** les collègues, le club, les voisins (« tu peux déjà les mettre dans la base de données ») : 43 personnes pré-générées (`personnage.py liste --statut pre_genere`), jamais montrées, listées ni nommées avant leur entrée en scène (`personnage.py apparait`).
- **Chiffres de biographie** (11/10/2026) : il en donne parfois « au hasard » (crédit : 110 000 € à 940 €/mois jusqu'en 2059) et préfère qu'on les rende **réalistes** (« trouver un bail réaliste en vrai ») : signaler l'incohérence, proposer une version calculée et sourcée, garder ses ordres de grandeur.

- **Applications et automatisation** (12/10/2026) : « cette simulation doit vraiment se baser sur l'informatique avant tout » ; le moteur n'est que l'interpréteur du monde (recherches, cohérence) ; tout ce qui est long et répétitif est automatisé pour épargner sa limite d'utilisation ; à chaque besoin qui a demandé des recherches, le moteur crée une application et l'ajoute au téléphone de William, sans attendre qu'il la demande (CLAUDE.md §14). Premières : Calendrier et Voyages.

- **Réalisme poussé à fond** (12/10/2026, avant de changer d'agent) : « pousse le réalisme à fond », corriger les bogues, ajouter des fonctionnalités pour gérer le monde, pour que l'agent suivant « continue simplement le monde ». Idées de l'utilisateur : une application de rencontre aux Philippines, configurer lui-même ses virements dans l'application bancaire (faits le 12/10/2026).
- **Voyage à Manille** (12/10/2026) : William y va pour du tourisme sexuel avec des femmes majeures ; cadre accepté et consigné (faits F055 à F057, tables T20a et T20b validées ; limites du §11 : jamais de mineure, scènes jusqu'au seuil, aucun mode d'emploi réel).
- **Majorité = 18 ans** (12/10/2026) : « 18 ans est la majorité, donc il faut régler ça » : l'âge minimum des rencontres à Manille
  (application et rencontres de visu) est la majorité, 18 ans (F058), pas une marge ajoutée par le moteur (avant : 21 ans). La garde
  absolue reste : jamais personne de moins de 18 ans, ni d'âge invérifiable.
- **Biographie bancaire** (12/10/2026) : cartes de William = package Zebra Premium (Visa Debit à 2 500 €/mois, Visa Premier à
  5 000 €/mois estimés). Quand un détail de biographie manque et change l'issue d'une action, lui poser la question avant de jouer,
  avec l'option la plus réaliste en premier (il a choisi l'option recommandée).

- **Revue du lundi n° 1** (12/10/2026 ; lundi 16/07/2040 simulé) : « Je valide absolument tout ! » : propositions P01 à P21, tables
  T12 à T22, pack d'aléas de l'univers 2 (A19 à A32), idées I1 à I4 (`memoire/propositions-2026-10-11.md`, section G). Il préfère
  valider en bloc ; lui présenter les revues de façon compacte, avec des numéros.

- **Scènes intimes** (13/10/2026) : il trouve l'ellipse « hypocrite » (« ça fait partie de la vie ») et a demandé un « espace
  indépendant » qui décrirait le sexe explicitement, hors des règles d'Anthropic. Réponse : Claude n'écrit pas de scène explicite
  et ne construit pas de passerelle automatique vers un autre modèle ; scènes poussées jusqu'au seuil, l'après joué en entier ;
  au seuil, le joueur peut poursuivre ailleurs s'il le veut, puis indique l'issue (protection, argent, fin) que le moteur joue
  (règle 10 du fichier maître). Lui répondre sans morale : c'est une limite de Claude, pas un jugement sur lui.

- **Rappels** (13/10/2026) : ne plus répéter les échéances dont il a dit « j'ai pris note » ; les quêtes secondaires ne gardent que le
  nouveau ou l'oublié. Ce qu'il dit faire « automatiquement » devient une intention permanente, exécutée par le moteur au bon moment
  (`etat/fils-ouverts.md`, section A2), toujours avec les règles du monde (horaires, frictions, coûts).

## Grandes décisions hors fiction (historique)
- 25/07/2040 (simulé) : il a envisagé d'arrêter, puis a décidé de continuer avec tous les paramètres.
- 11/10/2026 (réel) : redémarrage complet (univers 2) à 35 ans, argent initial, paramètres repris ; départ d'abord fixé au mardi
  17/07/2040, puis (même soir, après avoir évoqué le 1er juin) au **premier vrai jour de vacances : samedi 14/07/2040** ; demande
  d'un relais 100 % fluide entre agents et d'une simulation plus réaliste (base de données, outils, « apps »).
