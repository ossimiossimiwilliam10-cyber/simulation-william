# Outils du moteur — index, architecture et démarrage à froid

> Mis à jour le 11/10/2026 et le 14/10/2026 (dates réelles). Pour TOUT agent (Claude Code, Gemini CLI / Antigravity, Codex, autre) : ce fichier
> suffit pour savoir quoi lancer et où sont les données. Chaque outil a une aide : `python outils/<outil>.py --help`.
> Conventions : Python 3 ; fichiers en UTF-8 avec fins de ligne CRLF ; CSV séparés par « ; » (jamais de « ; » dans un champ :
> utiliser « · ») ; dates AAAA-MM-JJ ; heures HH:MM dans le fuseau de l'horloge. Sous Windows, si les accents s'affichent mal
> dans la console, lancer avec `PYTHONIOENCODING=utf-8` (le fichier, lui, est juste).

## 1. Démarrage à froid (un agent qui ne connaît rien)
1. `python outils/relais.py entree --agent "<nom de l'agent>"` : briefing complet (alertes de sessions parallèles, horloge,
   dernier tour montré au joueur, échéances, rituels dus, notes de passation, préférences, routine) ; pose le verrou.
2. Lire le fichier maître (CLAUDE.md = GEMINI.md = AGENTS.md, sauf la ligne 3), puis `memoire/preferences-utilisateur.md`,
   puis les fichiers listés au §7 du fichier maître.
3. `python outils/tour.py debut` : la fiche moteur du tour (météo, soleil, fériés, échéances, argent, corps, lieu, rituels).
4. Jouer le tour (règles du fichier maître ; réactions tirées avec `jet.py --table`).
5. Écrire le texte du tour dans un fichier brouillon, puis
   `python outils/tour.py fin --jusqua "AAAA-MM-JJ HH:MM" --lieu "…" --attente "…" --texte <brouillon> --message "<message du joueur>"`.
6. Avant de passer la main : `python outils/relais.py sortie --note "…" --commit "…" --fusionner`.

## 2. Où est quoi
| Dossier | Contenu | Nature |
|---|---|---|
| `etat/` | État du monde : horloge, agenda, grand livre, échéancier, savoir, personnages, relations, météo tirée, corps, fronts, fichiers d'état en Markdown, note de relais, dernier tour | change à chaque tour |
| `donnees/` | Référentiels sourcés : faits vérifiés, prix, lieux et ambiances, climat de Findel, calendrier scolaire, événements publics, délais, population (générateur de personnages) | change rarement, après recherche web |
| `journal/` | Un journal par jour simulé ; `journal/tours/` : texte EXACT de chaque tour et message du joueur | ajout seulement |
| `memoire/` | Préférences de l'utilisateur, pièges connus, synthèses, revues, tirages (texte et JSONL), journal des sessions, propositions | ajout seulement |
| `personnes/`, `whatsapp/`, `courriels/`, `documents_william/` | Fiches, conversations, pièces reçues, pièces de William (PDF) | |
| `sorties/` | Généré, ignoré par git : base SQLite `monde.sqlite`, page `telephone/index.html` | reconstruit à volonté |
| `archives/` | Univers 1 et faux départ de l'univers 2 : lecture seule, aucun fait pour l'univers en cours | figé |

## 3. Les outils
| Outil | Rôle | Commandes principales |
|---|---|---|
| `relais.py` | Relais entre agents : briefing, sessions parallèles, verrou, note de relais, journal des sessions, commit et fusion | `entree`, `sortie`, `verifier`, `git`, `verrou`, `liberer` |
| `maitres.py` | CLAUDE.md, GEMINI.md, AGENTS.md identiques sauf la ligne 3 | `verifier`, `synchroniser --depuis CLAUDE.md` |
| `tour.py` | Orchestrateur : début et fin de tour, aperçu d'une avance rapide ; `fin` exécute aussi les actions programmées, fait avancer le monde vivant, écrit les actualités du lundi, les fiches courtes et complètes, le journal (`--journal`), les notes de fils (`--fil`), l'entrée du §9 (`--resume`), régénère le téléphone (avec ses différences) et enregistre (`--enregistrer` : commit et fusion) | `debut`, `fin`, `apercu` |
| `base.py` | Base de données SQLite reconstruite depuis les fichiers ; SQL en lecture ; recherche plein texte | `construire`, `requete`, `cherche`, `schema`, `vues`, `verifier` |
| `horloge.py` | Heure du monde, lieu de William, attentes, numéro du tour | `--regler`, `--tour +1` |
| `agenda.py` | Rendez-vous, échéances, promesses (règle 14) | `dus`, `retards`, `ajouter`, `clore`, `reporter` |
| `grand_livre.py` | Argent : soldes calculés, prévus, mouvements | `solde`, `ajouter`, `realiser`, `journal` |
| `echeancier.py` | Mouvements récurrents (traitement, factures, virements permanents avec contrepartie, échéances de prêt) écrits au grand livre | `liste`, `prevoir`, `realiser`, `budget`, `verifier` |
| `prets.py` | Prêts de William : tableau d'amortissement calculé (prêt PR1 de la maison), capital restant dû, contrôle des calages | `liste`, `tableau`, `crd`, `verifier` |
| `savoir.py` | Qui sait quoi ; décomptes de fuite (T5) | `qui`, `peut`, `ajouter`, `t5` |
| `jet.py` | Tirages (libres ou dans les tables T1-T14) ; garde de la règle 17 ; garde « mineurs » (`--pour`) | `--table Tn`, `--liste` |
| `tour_du_monde.py` | Ancien tour du monde ; depuis le 14/10/2026, passe par `monde_vivant.py` (`--ancien` : ancien tirage par les fiches) | `JJ/MM` |
| `monde_vivant.py` | Vie des personnages : chaque jour pour ceux en lien avec William, une fois par semaine pour les autres (T11, T13) ; initiatives envers William (T14, heure en T10, texte programmé) ; états des liens ; fiches régénérées dans `etat/vies-propres.md` ; lancé par `tour.py fin` | `avancer --jusqua`, `jour`, `semaine`, `liens`, `lien`, `vies`, `fiches` |
| `routines.py` | Horaires de vie tirés selon le métier (sommeil, travail, trajets, repos, vacances : `donnees/population/routines.csv`) : qui est joignable à quelle heure | `voir`, `etat`, `prochaine` |
| `reactions.py` | Réactions automatiques : « j'aime » (T21a), message reçu (T21b), délai (T10) ; heure selon la routine ; réponse programmée à l'agenda (NON CONNUE, marque `[reaction …]`) puis jouée avec son texte ; évolution d'une intention cachée liée à l'argent (T23) après un jour sans échange ou une rencontre en personne | `message`, `like`, `delai`, `jouer`, `en-attente`, `rencontre` |
| `actions.py` | Actions programmées (liste blanche : match, blocage…) exécutées quand l'horloge passe leur heure | `liste`, `ajouter`, `executer`, `annuler` |
| `whatsapp.py`, `traces.py`, `fils.py` | Écriture d'un message dans `whatsapp/` (trace automatique pour William) ; ajout au dossier des traces ; notes et clôture des fils ouverts | `message`, `voir` ; `ajouter` ; `noter`, `clore`, `ajouter`, `liste` |
| `tropiques.py` | Tempêtes tropicales de l'année (noms PAGASA de 2040, climatologie mensuelle) et mousson renforcée ; force la météo de Manille ; alertes publiques | `assurer`, `liste`, `jour` |
| `devises.py` | Argent sur place : taux du jour (tiré une fois), paiement par carte en devise (cours Visa + frais de la banque), retrait au distributeur (frais, plafond), espèces au grand livre (`especes_php`) ; application Portefeuille | `taux`, `convertir`, `payer`, `retirer`, `depenser`, `especes`, `distributeurs`, `verifier` |
| `courses.py` | Courses en ville à Manille : Grab et taxis (ordinaires, jaunes, à coupon) ; prix, attente et durée selon l'heure, le jour et la pluie ; installation de Grab, carte enregistrée, commande payée à l'arrivée ; aléa A33 à chaque course (T24a : compteur, prix fixe demandé, détour ; T24b : chauffeur VTC qui annule) ; application Courses | `options`, `installer`, `carte`, `commander`, `accepter`, `annuler`, `lieux`, `ici`, `verifier` |
| `actualites.py` | Section hebdomadaire de `etat/monde.md` écrite seule le lundi (événements publics, fériés, tempêtes, cours du peso, nouvelles tirées dans `donnees/actualites-modeles.csv`) | `semaine [--ecrire]`, `verifier` |
| `tirage_aleas.py` | Aléas de la semaine (le lundi) | `AAAA-MM-JJ` |
| `personnage.py` | Générateur de personnages tirés selon la démographie réelle ; registre ; entourage pré-généré (jamais montré avant son apparition) ; noms sans homonymes ; audit des biais | `nouveau`, `reseau`, `apparait`, `promouvoir`, `completer` (personnage écrit à la main : tire ce qui manque), `liste --statut`, `audit` ; zones : Luxembourg, Audun, Manille, Séoul, Brésil |
| `meteo.py` | Météo tirée sur les normales de la station du lieu où se trouve William (Findel, Manille : `donnees/stations-meteo.csv`) ; prévisions vues par William | `jour`, `heure`, `prevision`, `mois` |
| `calendrier_2040.py` | Fériés (LU, FR avec droit local, CI, CV), Pâques, Ramadan, lune, soleil, calendrier scolaire, événements, jours ouvrés | `--soleil`, `--scolaire`, `--evenements`, `--ouvres` |
| `lieux.py` | Lieux : ouvert ou fermé (fériés selon le pays, congés annuels), accès, prix ; ambiances tournantes contre les tics | `voir`, `ouverts`, `liste` |
| `faits.py` | Faits vérifiés (source, date, fiabilité, projection 2040) : à consulter AVANT une recherche web | `cherche`, `ajouter`, `perimes` |
| `prix.py` | Prix 2026 sourcés et projetés en 2040 (× 1,35 fixe) ; tirage dans une fourchette | `cherche`, `tirer`, `ajouter` |
| `corps.py` | Sommeil, entraînements, repas, poids, maladies de William ; état à montrer | `nuit`, `seance`, `noter`, `etat` |
| `fronts.py` | Menaces, occasions, projets en segments avec paliers écrits d'avance | `creer`, `avancer`, `liste`, `clore` |
| `rituels.py` | Ce que le moteur doit faire (fiches, tour du monde, synthèses, revue, aléas) | `dus`, `liste` |
| `telephone.py` | Page « téléphone de William » : écran d'accueil et applications (`telephone_web/` : coque, noyau, une feuille JS par application ; CLAUDE.md §14) ; différences avec la dernière page publiée ; application **Fichiers** (27/10/2026) : les PDF de `documents_william/` et `courriels/` datés d'aujourd'hui ou d'avant, copiés dans `sorties/telephone/fichiers/` et publiés avec la page | (sans argument) ; `--json` ; `--diff [--code]` ; `--fichiers` ; `--marquer-publie` |
| `voyages.py` | Application Voyages : vols (calendrier des prix), hôtels, forfaits vol + hôtel, formalités ; calcul déterministe partagé avec la page | `vols`, `mois`, `hotels`, `forfait`, `formalites`, `verifier` |
| `appli_calendrier.py` | Données de l'application Calendrier (fériés FR, LU, PH ; vacances, événements, rendez-vous connus, argent) | (sans argument : résumé) |
| `banque.py` | Banque : virements ponctuels (entre comptes ou vers un tiers), ordres permanents (créer, modifier, suspendre, reprendre), liste ; prévus recalculés | `virement`, `ordre-modifier`, `ordre-creer`, `ordre-suspendre`, `ordre-reprendre`, `liste` |
| `courriel.py` | Un courriel reçu par William devient un PDF dans `courriels/` (expéditeur, objet, texte), lu par l'application Courriels | `--de`, `--objet`, `--texte`, `--quand` |
| `etravel.py` | Inscription eTravel de William (Philippines) : contrôle de la fenêtre de 72 heures, confirmation en PDF avec code QR dans `courriels/` | `inscrire` |
| `gestion.py` | Application Gestion du téléphone (27/10/2026 ; installée le 19/07/2041) : budget d'API plafonné à 1 000 € par mois, pôles (RH actif ; juridique, finance, technique, commercial à venir), sources officielles, candidats rapportés par l'agent IA, documents des collaborateurs reçus puis analysés par le pôle concerné | `etat`, `recevoir`, `analyser`, `candidat`, `verifier` |
| `telephone_serveur.py` | Sert la page du téléphone depuis le PC et le Wi-Fi, SANS Claude (27/10/2026) : `ouvrir-telephone.bat` à la racine ; les PDF de `documents_william/` et `courriels/` en lecture seule | `--ouvrir`, `--local`, `--essai` |
| `piece.py` | Un PDF (règle 4) à partir d'un texte simple : en-tête titre, sous-titre, auteur, pied, dossier, fichier, meta ; corps en « # » titres, paragraphes, « - » puces, « | » tableaux (29/10/2026 : remplace le script Python écrit à chaque tour) | `piece.py sorties/brouillons/x.txt [--simule]`, puis `verifier_pdf.py` ; exemple : `donnees/exemples/piece-exemple.txt` |
| `monde_social.py` | Vie sociale entre personnages (P37, 29/10/2026) : chaque jour, pour chaque paire d'un même groupe (`etat/groupes.csv`), un contact a lieu ou non (force du groupe) et son issue est TIRÉE (rien, banal, information, tension, service) ; une information ne passe que si le personnage est bavard (traits) et s'écrit dans `etat/savoir.csv` ; journal `etat/monde-social.csv` (moteur seul : William n'en voit que des traces) ; lancé par `tour.py fin` | `avancer [--jusqua] [--simule]`, `voir` |
| `lenteur.py` | Lenteur réelle des affaires (P38) : chaque lundi, T22 fait avancer de 0, 1 ou 2 segments chaque front « temps » (démarches, travaux, menaces des concurrents) ; un palier atteint se joue au tour suivant ; `promesse` tire si une personne tient une promesse (« oubli N % » de ses traits) ; lancé par `tour.py fin` | `semaine [--jusqua] [--simule]`, `promesse --pour "Nom" --libelle "…"` |
| `tresorerie.py` | Trésorerie de SOLEIL B2B CI (P41) : apports, dépenses engagées, charge mensuelle (salaires chargés, loyer), autonomie, montants à confirmer, d'après `etat/societe-engagements.csv` ; le directeur général virtuel (pôle finance) cite ces chiffres | `[--au AAAA-MM-JJ]` |
| `verifier_texte_joueur.py` | Contrôle du texte montré au joueur (28/10/2026, après l'audit du travail de Gemini) : identifiants internes (D038, A106, (I1)), mécanismes cachés (tirages, fuites, T4/T5), aléas annoncés d'avance, format du tour, récit en liste de jours, discours structuré, avance de plus de 36 h ; avertissements non bloquants, lus par `tour.py fin` (« RELIRE (texte joueur) ») et `controle_coherence.py` | `--texte brouillon.md`, `--dernier`, `--essai` |
| `entretien.py` | Un message de l'agent à un candidat en une commande (20/07/2041) : tire T17, programme la réponse (T10, agenda NON CONNU), journal et fiche ; refuse un envoi entre 23h et 7h chez le destinataire, un nom ou un numéro dans le texte | `envoyer --pour --canal --quand --decalage --texte`, `repondre Axxx --texte` |
| `annonces.py` | Annonces publiques de William (27/10/2026) : réponses tirées par plateforme et par heure, répondants créés par le générateur (zone Abidjan : contexte `candidat_annonce_abidjan` ; diaspora et monde entier : contexte `candidat_diaspora`, ville de résidence tirée, depuis le 19/07/2041), tri A/B/C et arnaques aux frais d'avance ; fichiers `etat/annonces.csv` et `etat/reponses-annonce.csv` (moteur seul) | `liste`, `tirer --jusqua`, `reponses`, `reseau "Nom"` (réseau en clients potentiels d'un répondant, noté sur 100 : demande de William du 18/07/2041), `voir-reseau`, `verifier` |
| `pieces_2041_07_16.py` | Pièces du 16/07/2041 (tour n° 4) : courriel de William au ministère (article 14), confirmation d'abonnement à l'agent IA, annonce et règles de l'agent IA : 3 PDF ; modèle pour un courriel de William ou une pièce reçue d'un service en ligne | `courriel-ministere`, `abonnement`, `annonce`, `regles-v2`, `tout` |
| `etude_ia_2041.py` | Rapports de l'agent IA de William du 16/07/2041 (opportunités d'investissement : Brésil, puis Côte d'Ivoire) : 2 PDF de 4 pages dans `documents_william/`, chiffres 2025-2026 (faits F096 à F108) ; modèle pour tout rapport d'étude demandé à l'agent IA | `bresil`, `cote-ivoire` |
| `e_arrival.py` | Carte d'arrivée électronique de Corée du Sud : contrôle de la fenêtre de 72 heures (F089), confirmation en PDF avec code QR dans `courriels/` (modèle de `etravel.py`) | `soumettre` |
| `transports.py` | Application Transports : itinéraires en bus, train et tram (Audun, Esch, Luxembourg, aéroport) selon le type de jour ; billet RegioZone pour la partie française ; calcul partagé avec la page | `options`, `arrets`, `lignes`, `verifier` |
| `cartes.py` | Cartes de William (Visa Debit, Visa Premier) : plafond de la période, utilisé, disponible ; paiement autorisé ou refusé ; carte de crédit débitée au relevé (prévu « C-… ») ; branché sur `voyages.py --carte`, la Banque et les Voyages du téléphone | `liste`, `payer`, `limite`, `verifier` |
| `rencontres.py` | Application de rencontre : profils tirés (Manille, 18 ans au moins : majorité, garde absolue), inscription de William, j'aime, matchs, messages ; intention réelle cachée ; vivier complété si une tranche d'âge s'ouvre après coup ; depuis le 14/10/2026 : « j'aime » reçus chaque jour (T21c ; un « j'aime » en retour fait un match immédiat), pile « à découvrir » tenue à 12 profils, matchs sans échange retirés (T21d) | `generer`, `completer`, `inscription`, `aimer`, `passer`, `match`, `message`, `liste`, `voir`, `likes-recus`, `pile`, `menage` |
| `etiquettes.py` | Applique les actions copiées depuis le téléphone (étiquettes [voyages|banque|rencontres|portefeuille|courses: …]) : la commande exacte, à l'heure du jeu | `--texte "…"`, `--simule` |
| `resume_etat.py` | `etat/resume.md` : l'essentiel en trois minutes | `--silencieux` |
| `controle_coherence.py` | Contrôle de fin de tour (dates, maîtres, CSV, base, rituels, tables, PDF, tics) | (sans argument) |
| `audit_jets.py`, `chasse_tics.py`, `fuseaux.py`, `archiver_point_de_reprise.py`, `pdf_base.py`, `verifier_pdf.py` | Audit des probabilités, tics d'écriture, fuseaux horaires, archivage du §9, PDF | voir `--help` |
| `tests_moteur.py` | Essais automatiques de tous les outils sur une COPIE du dépôt | (sans argument) |
| `mobile.py` | Téléphone en Corée : eSIM, SIM de l'aéroport, pass journalier d'itinérance (prix projetés, paiement par carte ou sur facture) ; affiché dans Portefeuille | `options`, `acheter`, `etat`, `verifier` ; étiquette `[mobile: acheter option=… carte=…]` |

## 4. Base de données
- **Source de vérité** : les fichiers texte (CSV, Markdown, JSONL) versionnés par git. **Base** : `sorties/monde.sqlite`,
  reconstruite à la demande (`python outils/base.py construire`, environ une seconde), ignorée par git. Pourquoi : git fusionne
  des lignes de texte, jamais un fichier binaire ; tout agent lit les fichiers même sans Python ; la base n'est qu'un index.
- Tables : horloge, attentes, agenda, grand_livre, comptes, soldes, echeancier, prets, savoir, personnages, relations, lieux,
  ambiances, faits, prix, climat, meteo, corps, fronts, evenements_publics, calendrier_scolaire, delais, journal (lignes
  horodatées), tours (textes des tours), messages (WhatsApp), fiches (personnes/), documents (PDF, texte extrait), tirages
  (JSONL), tirages_md (ancien journal), recherche (plein texte, accents ignorés), meta.
- Vues : `python outils/base.py vues` (agenda à venir, agenda connu de William, retards, prévus, personnages avec âge et
  minorité, qui sait quoi, messages, journal, météo, tirages, documents).
- Exemples : `python outils/base.py requete "SELECT date, type, tmax FROM v_meteo"` ;
  `python outils/base.py cherche "boulangerie"`.

## 5. Tour économe (14/10/2026 : « une simulation surtout informatique, avec un contrôle de l'IA »)
Le programme fait avancer le monde ; le moteur interprète, vérifie et écrit. Pendant un tour :
1. `python outils/tour.py debut [--jusqua …]` : tout ce qui est dû, la météo, les liens, l'argent ; lire en plus seulement les
   fichiers que le tour touche (fiche du personnage en scène, conversation, fil ouvert).
2. Étiquettes collées par le joueur : `python outils/etiquettes.py --texte "…"` (la commande exacte, à l'heure du jeu).
3. Message de William à un personnage : `reactions.py message` (ou `rencontres.py message`) : table, modificateurs, heure de la
   réponse selon la routine du personnage et ligne d'agenda NON CONNUE, sans jet à la main ; à l'heure dite,
   `reactions.py jouer Axxx --texte "…"` (le moteur n'écrit que le texte).
4. Argent et déplacements : `devises.py` (pesos, distributeurs, espèces), `cartes.py`, `courses.py`, `transports.py`, `voyages.py`.
5. Fin : `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message "…" --journal "…" --fil "4: …"
   --resume "…" --enregistrer` : horloge, argent échu, actions, monde vivant, actualités, fiches, journal, §9, téléphone (avec
   ses différences : `telephone.py --diff`), contrôle de cohérence, commit et fusion.
6. Téléphone : republier seulement si `telephone.py --diff` montre un changement, puis `telephone.py --marquer-publie`.

## 6. Ce que les outils ne font pas (et qui reste au moteur)
Écrire le récit, le journal, les WhatsApp, les fiches et les fils ouverts ; tirer les réactions des personnages dans les tables ;
vérifier sur le web un fait nouveau (puis l'ajouter avec `faits.py ajouter`) ; décider quoi que ce soit à la place de William.

## 7. Reprise par un moteur moins puissant (Gemini / Antigravity quand la limite d'utilisation de Claude est atteinte, 27/10/2026)
L'utilisateur l'a annoncé : quand Claude s'arrête (limite atteinte), il continue avec Gemini dans Antigravity, qui peut se tromper plus
souvent. La partie doit repartir sans perte ; Claude, à son retour, audite le travail (CLAUDE.md §10 A).
1. **Entrée** : `python outils/relais.py entree --agent "Gemini"`. Une alerte « session parallèle » ou « fichiers non enregistrés » au nom
   d'un worktree `claude/…` est NORMALE (la session de Claude s'est coupée). Voir `git -C <worktree> status` : s'il reste des fichiers non
   enregistrés, les enregistrer là-bas (`git add -A`, `git commit`), fusionner la branche en avance rapide dans `master`
   (`git -C <dossier principal> merge --ff-only <branche>`), puis `python outils/relais.py liberer`. Ne rien supprimer.
2. **Lire** : `etat/relais-notes.md` (la dernière « PASSATION »), `etat/dernier-tour.md` (texte exact du dernier tour et dernier message
   du joueur), `etat/fils-ouverts.md`, puis `python outils/tour.py debut` (tout ce qui est dû, météo, argent, corps, lieu).
3. **Les erreurs d'un moteur moins puissant, et le remède** :
   - personnage nouveau : `personnage.py nouveau` (jamais écrit à la main) ; un figurant de l'entourage entre par `personnage.py apparait` ;
   - réaction d'un personnage à William : `jet.py --table Tn --pour "Nom"` ou `reactions.py message / delai`, puis `reactions.py jouer Axxx --texte "…"` ;
     jamais de probabilité choisie à la main (règle 17) ;
   - **état caché** : les lignes d'agenda `connu=non`, `etat/reponses-annonce.csv`, `etat/reseaux-repondants.csv`, les secrets des fiches de
     `personnes/` et `etat/savoir.csv` ne passent JAMAIS dans le texte du joueur ni dans `whatsapp/` ; après chaque réponse de candidat,
     `python outils/telephone.py --json` ne doit lister que les conversations que William peut lire (aujourd'hui : `claude-agent-ia`) ;
   - William décide seul (règle 13) : s'arrêter à la première vraie décision ou au premier message important ;
   - format du tour §5 (récit en prose, puis réponses attendues, à faire, quêtes secondaires, « Que veux-tu faire ? ») ; aucun conseil, aucun jet,
     aucune source montrés ; « 📌 Vraie vie » seulement pour un échange hors simulation ;
   - dates et fuseaux : `fuseaux.py` et `calendrier_2040.py`, jamais de tête (le 19/07/2041 est un vendredi) ;
   - fichiers CSV : jamais de « ; » dans un champ, fins de ligne CRLF conservées ;
   - `tour.py fin` : ne pas régler l'horloge à la main avant ; `--fil` prend l'IDENTIFIANT d'un fil (« I21 »), pas un numéro ; si la commande
     échoue en route, vérifier `etat/horloge.txt` avant de la relancer (sinon le compteur de tours avance deux fois) ;
   - fin de chaque tour : `python outils/controle_coherence.py` (« aucune incohérence détectée »), `python outils/tests_moteur.py`, puis
     `tour.py fin … --enregistrer` (commit et fusion en avance rapide dans `master`) : l'état ne reste jamais seulement dans un worktree.
4. **Dans la fiction, « Claude » est l'agent IA de William** (son pôle ressources humaines virtuel, abonnement Claude Pro, conversation
   épinglée `whatsapp/claude-agent-ia.md`, règles dans `documents_william/`) : le moteur, quel qu'il soit, joue ce personnage sous ce nom,
   ainsi que l'« agent central » de Gestion (conversation `whatsapp/agent-central.md`, double IA du directeur général : avis et chiffres, jamais de décision à la place de William), avec leurs limites (ils ne signent, ne paient et ne promettent rien ; il ne donne jamais le nom de William sans sa décision ; au-dessus du seuil de 70 il
   fournit le numéro de William au candidat sans que le texte du tour en écrive un seul chiffre).
5. **Téléphone** : `sorties/telephone/index.html` est publié par Claude (outil Artifact, adresse dans `etat/relais-config.json`). Sans Claude, c'est
   `ouvrir-telephone.bat` (ou `python outils/telephone_serveur.py --ouvrir`) qui l'affiche dans le navigateur du PC, et sur le vrai téléphone du joueur
   (même Wi-Fi) à l'adresse du réseau affichée au démarrage ; `tour.py fin` régénère la page à chaque tour, le joueur recharge l'onglet. Ne lancer
   `telephone.py --marquer-publie` qu'après une vraie publication sur claude.ai. Le message de reprise à coller dans Antigravity : `etat/message-reprise-gemini.md`.
6. **Texte du joueur propre** (28/10/2026) : le texte d'un tour ne contient JAMAIS d'identifiant du moteur (D038, A106, « (I1) », « (A09, … ») ni de mécanisme caché (tirage hebdomadaire, fuite interne, escalade externe, tables T4/T5) ni d'aléa annoncé d'avance ; les pièces se citent par leur titre (« le rapport quotidien du 3 août »), pas par leur code. Un avancement de plusieurs jours se raconte d'un trait, en prose, sans paragraphes « Le samedi… Le dimanche… ». Les personnages parlent comme des personnes (courtes phrases, hésitations, intérêts propres), jamais en « Premièrement… Deuxièmement… » ; leurs défauts et leurs soucis tirés se voient dans leurs actes. `python outils/verifier_texte_joueur.py --texte brouillon.md` avant `tour.py fin` ; ce dernier relit le texte et signale « RELIRE (texte joueur) ».
7. **Hygiène et argent** (audit du 29/10/2026) : les brouillons de tour et les messages du joueur vont dans `sorties/brouillons/` (ignoré par git), jamais dans `etat/` ni `outils/` ; un PDF se fabrique avec `python outils/piece.py <texte>` (plus de script Python par tour) ; une échéance de l'échéancier (abonnement, loyer, assurance) est débitée par `tour.py fin` : ne JAMAIS la ressaisir à la main ; TOUTE dépense de William s'inscrit le jour même (`cartes.py payer` pour une carte, `grand_livre.py ajouter` sinon) : hôtel ou résidence, repas, taxis et VTC, frais ; un départ, un retour ou un règlement prévu est inscrit à l'agenda (règle 14). La revue du lundi propose des MÉCANISMES du simulateur (aléas, règles, outils, immersion), pas des décisions d'affaires de William : celles-ci passent par le directeur général virtuel. `controle_coherence.py` signale « RELIRE (hygiène) ».
8. **Univers vivant** (P37 à P41, validées le 29/10/2026) : `tour.py fin` fait vivre les groupes (`monde_social.py`) et, le lundi, avancer les fronts « temps » (`lenteur.py`, T22) ; un palier atteint (`fronts.py liste`, ligne « DÛ ») se joue au tour suivant, d'après sa description, sans l'annoncer d'avance ; les menaces des concurrents (`etat/concurrents.csv`, fronts cachés) ne se montrent que par leurs effets (rumeur, devis moins cher cité par un prospect, approche d'un salarié). À Abidjan : `courses.py options --de … --vers …` (Yango, taxi compteur, en FCFA), `devises.py` (XOF, parité fixe), aléas A01, A04 à A06 et A37 à A39 actifs. Trésorerie de la société : `tresorerie.py`.
8. **Quand un tour dépasse ce que le moteur sait faire sûrement** : faire le plus simple et le plus exact, puis écrire une ligne datée dans
   `etat/relais-notes.md` (ce qui reste, ce dont il doute) ; ne jamais effacer d'information (« avant → maintenant »). Claude corrigera.
