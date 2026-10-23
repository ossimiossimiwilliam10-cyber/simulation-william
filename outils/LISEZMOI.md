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
| `telephone.py` | Page « téléphone de William » : écran d'accueil et applications (`telephone_web/` : coque, noyau, une feuille JS par application ; CLAUDE.md §14) ; différences avec la dernière page publiée | (sans argument) ; `--json` ; `--diff [--code]` ; `--marquer-publie` |
| `voyages.py` | Application Voyages : vols (calendrier des prix), hôtels, forfaits vol + hôtel, formalités ; calcul déterministe partagé avec la page | `vols`, `mois`, `hotels`, `forfait`, `formalites`, `verifier` |
| `appli_calendrier.py` | Données de l'application Calendrier (fériés FR, LU, PH ; vacances, événements, rendez-vous connus, argent) | (sans argument : résumé) |
| `banque.py` | Banque : virements ponctuels (entre comptes ou vers un tiers), ordres permanents (créer, modifier, suspendre, reprendre), liste ; prévus recalculés | `virement`, `ordre-modifier`, `ordre-creer`, `ordre-suspendre`, `ordre-reprendre`, `liste` |
| `courriel.py` | Un courriel reçu par William devient un PDF dans `courriels/` (expéditeur, objet, texte), lu par l'application Courriels | `--de`, `--objet`, `--texte`, `--quand` |
| `etravel.py` | Inscription eTravel de William (Philippines) : contrôle de la fenêtre de 72 heures, confirmation en PDF avec code QR dans `courriels/` | `inscrire` |
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
