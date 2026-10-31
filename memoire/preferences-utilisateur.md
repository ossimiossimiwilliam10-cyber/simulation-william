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

- **Description physique exhaustive (demande de l'utilisateur, 21/10/2026)** : dès qu'un personnage adulte apparaît pour la première fois ou qu'une photo est reçue/consultée (application de rencontre, réseaux, vis-à-vis), le moteur DOIT donner dans la narration une description physique complète et vivante (visage, traits, teint, regard, bouche, cheveux, morphologie, silhouette, proportions poitrine/taille/hanches, style vestimentaire, allure) pour que l'utilisateur puisse se représenter fidèlement la personne dans la vraie vie (cf. Piège n° 69 : décrire la silhouette n'est pas une scène sexuelle ; la limite absolue reste : pas de détail génital, aucun acte sexuel explicite, rien de sexualisé pour un mineur). La description est immédiatement consignée dans sa fiche de personnage (personnes/<prenom-nom>.md) et dans tat/personnages.csv.

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

- **Mode auto** (13/10/2026) : « Je passe en mode auto jusqu'à … (dépense max autorisée : N euros) GO ! » : le moteur joue alors
  lui-même les choix routiniers de William (repas, attentes, trajets, formalités) jusqu'au point indiqué, dans le plafond de
  dépenses, avec les règles du monde (jets, frictions, retards) ; il ne décide pas à sa place d'un message personnel ni d'un
  choix important, s'arrête au point indiqué et indique la somme dépensée. Premier usage : trajet Findel-Manille du 18-19/07/2040
  (500 € au plus, 31,40 € dépensés).

- **Univers vivant et automatisé** (14/10/2026) : « rendre l'univers le plus vivant et réaliste que possible », « indépendant »,
  « réaliste, pas moral », « pas de trucs woke, des réalités » ; et « configurer des outils pour limiter la dépense d'utilisation »,
  la simulation étant « surtout informatique, avec un contrôle de l'IA ». En pratique : le monde avance seul entre deux messages
  (vie des personnages, réponses à l'heure de leur routine, actualités, météo, typhons, change, prix des courses) ; le moteur
  interprète et écrit ; toute tâche répétitive devient un outil (outils/LISEZMOI.md, « tour économe »).

- **Modèle financier Solo et Entrepreneuriat (Luxembourg)** (21/10/2026) : en mathématiques, William est célibataire sans enfant (Classe U). Il assume 3 leçons supplémentaires hebdomadaires dès sa titularisation à 28 ans (25 leçons au total, décharges d'âge converties). Formule d'allocation : socle vital fixe 2 000 €/mois, budget vacances 833 €/mois (10 000 €/an), sécurité liquide 10 % de l'excédent net total après socle vital, et solde versé en ETF Monde (~90 % du surplus net). À 35 ans : net lissé de 8 980 € (698 € sécurité, 5 449 € ETF). Entrepreneuriat (Statut général, art. 14) : activité accessoire autorisée par le MENJE (EdTech, logiciel, édition) ou associé non-gérant d'une société de capitaux ; fenêtre optimale à 30-32 ans, bascule possible à 36-38 ans (temps partiel ou congé sans traitement). Toujours utiliser `python outils/carriere.py` (`etat/carriere.md`).

- **Visuels et planches photos des personnages (demande de l'utilisateur, 21/10/2026)** : toute planche visuelle, portrait ou composition de photos d'un personnage transmise ou créée est systématiquement archivée dans personnes/images/<prenom-nom>-planche.jpg et liée directement en tête de sa fiche markdown (personnes/<prenom-nom>.md). Le moteur s'appuie sur ces références graphiques pour préserver une cohérence absolue des scènes (traits, morphologie, tenues de travail, lieux habituels).

- **Limite d'utilisation de Claude et relais vers Gemini** (27/10/2026) : « il y a de fortes chances que ma limite d'utilisation soit atteinte avec toi » ; il continue alors avec Gemini dans Antigravity, « pas aussi puissant », qui « peut faire des erreurs » : la reprise doit se faire « le mieux possible » (procédure : `outils/LISEZMOI.md` §7 ; note de passation : `etat/relais-notes.md`). À chaque tour, tout est enregistré dans `master`.

- **Revues du lundi automatiques quoi qu'il arrive** (28/10/2026 réel ; 13/08/2041 simulé) : les revues du lundi doivent être présentées automatiquement chaque lundi matin, sans exception. Même en cas de « Go » ou d'avance rapide qui franchit un lundi, le moteur DOIT marquer impérativement un arrêt au lundi matin pour afficher la Revue du lundi (§12) et recueillir la validation des propositions et aléas avant de poursuivre.

- **Génération systématique de population locale et monde vivant chaque lundi** (28/10/2026 réel ; 14/08/2041 simulé) : chaque lundi matin lors de la revue hebdomadaire, le moteur DOIT générer automatiquement un contingent de nouveaux personnages pré-générés (statut pre_genere, 20 à 50 personnages via outils/generer_population_locale.py) représentatifs du lieu où réside William (ex : Abidjan, Luxembourg, etc.), même s'il y réside depuis plusieurs semaines. Le moteur tisse et met à jour leurs interactions aléatoires (outils/interactions_sociales.py : liens de travail, voisinage, amitié, rumeurs), rendant l'univers social organique, réaliste et indépendant sans artifice de fiction télévisuelle.

## Grandes décisions hors fiction (historique)
- 25/07/2040 (simulé) : il a envisagé d'arrêter, puis a décidé de continuer avec tous les paramètres.
- 11/10/2026 (réel) : redémarrage complet (univers 2) à 35 ans, argent initial, paramètres repris ; départ d'abord fixé au mardi
  17/07/2040, puis (même soir, après avoir évoqué le 1er juin) au **premier vrai jour de vacances : samedi 14/07/2040** ; demande
  d'un relais 100 % fluide entre agents et d'une simulation plus réaliste (base de données, outils, « apps »).
- 21/10/2026 (réel) : validation de la maquette financière intégrale Solo sans enfant (Classe U, 410-625 pts, 8 980 € net à 35 ans) et du cadre d'entrepreneuriat à distance (art. 14) pour l'Univers 3.
- 27/10/2026 (réel) : reboot de l'univers 3 « dès le premier jour » (16/07/2041, 08h37) ; il a choisi le « reboot propre » : état de départ, règles, tables et outils gardés, partie jouée archivée (Min-ji, Hye-won, Thiago, etc. ne sont pas gardés).
- 27/10/2026 (réel) : il veut ses fichiers (PDF des documents et pièces reçues) accessibles directement depuis son téléphone, « avec une application fichier » : application Fichiers du téléphone (CLAUDE.md §14), publiée avec la page ; en plus, envoi dans la conversation des PDF produits à sa demande.
- **Le conseiller d'abord** (29/10/2026 réel ; 21/08/2041 20h10 simulé) : quand William parle de l'entreprise ou de sa vie professionnelle, il s'adresse d'abord à son équipe virtuelle (le directeur général virtuel, devenu « son conseiller ») ; le moteur le suppose sans qu'il le précise. Le conseiller décide ensuite d'informer untel ou d'agir (courriels depuis direction@soleil-b2b.ci, signés William Ossimi), sans jamais décider à la place de William un choix important.
- **Veille « faute lourde »** (29/10/2026 réel ; 21/08/2041 simulé) : William demande que le conseiller (directeur général virtuel) lui signale, dans les mois et années à venir, toute occasion de révoquer Mohamed Coulibaly pour faute lourde, pièce à l'appui (seuil réel : article 5 de la convention de mandat, indemnité de non-concurrence due hors faute lourde). Rubrique « Veille faute lourde » dans chaque rapport de 20h00.
- **Rapports archivés, séance du dimanche** (29/10/2026 réel ; 25/08/2041 simulé) : le rapport quotidien de 20h00 du conseiller est écrit et archivé (PDF) mais n'est plus montré à William ; le dimanche, séance de travail (bilan de la semaine, ordre du jour, décisions) ; en semaine, seulement les urgences. Le moteur ne cite plus les rapports quotidiens dans les tours (sauf si William les ouvre).
- **Semaine programmée, avance hebdomadaire** (29/10/2026 réel ; 26/08/2041 simulé) : quand William programme sa semaine, le moteur avance en mode automatique jusqu'au point fixé (séance du dimanche), arrêt seulement sur un événement exceptionnel qui exige son intervention ; sans programmation, pas d'avance hebdomadaire.
- **Réponses automatiques en mode semaine** (29/10/2026 réel ; 01/09/2041 simulé) : pendant une avance hebdomadaire, le moteur répond aux messages ordinaires adressés à William comme il y répondrait d'après ses échanges précédents (ex. Lenny : « Mercredi même heure ? » → oui) ; il ne s'arrête que pour un événement important qui exige l'intervention de William, ce jour-là et à cette heure-là. Sans cette règle avant le 01/09, le message de Lenny du 26/08 est resté sans réponse (non réécrit).
- **William au lycée (mode automatique)** (29/10/2026 réel ; 15/09/2041 simulé) : au travail, toujours irréprochable ; aucune relation personnelle avec les élèves ; aucune vie privée évoquée au travail ; image nette. Le moteur joue ses semaines de cours dans ce sens sans le lui redemander.
- **Fin des avances hebdomadaires** (30/10/2026 réel ; 20/10/2041 simulé) : « on reprend le rythme d'avant, on arrête les longs sauts pour la semaine » : retour au tour par tour, avance rapide seulement sur « Go » et par petits pas.
- **RYTHME DE BIEN AVANT (30/10/2026 réel ; 22/10/2041 simulé)** : « arrête vraiment d'avancer, tu as niqué mon interaction avec Kim, on revient au rythme de bien avant ». Tour par tour ; « Go » = petite avance jusqu'au prochain événement ; arrêt dès qu'une personne s'adresse à William ; le moteur ne répond jamais à sa place (règles « semaine programmée » et « réponses automatiques » supprimées). L'avance du tour 156 a été annulée : reprise au mardi 22/10, au moment où Kim Schmitz lui parle.
