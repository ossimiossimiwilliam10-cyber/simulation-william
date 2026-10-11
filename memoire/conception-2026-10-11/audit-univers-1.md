# Audit des erreurs de l'univers 1 et outils qui les auraient évitées

> Exploration rendue le 11/10/2026 (date réelle) par un agent du workflow « simulation-ameliorations-conception » (session interrompue par la limite d'utilisation). Texte conservé tel quel ; ce qui en a été installé ou proposé est dans `memoire/propositions-2026-10-11.md` et `outils/LISEZMOI.md`. Les dates « 1er juin 2040 » y renvoient à une demande de départ que l'utilisateur a ensuite remplacée par le samedi 14/07/2040.


## Constats

- Sources lues en lecture seule : corrections n° 1-45 (archives/univers-1/etat/corrections.md), n° 46-60 et audit du 09/08/2040 (archives/univers-1/session-outils/modifications-non-enregistrees.patch), n° 46-47 de la branche univers-1-continuation, pièges n° 1-82, les trois revues du lundi, 242 commits. Sondes lancées depuis le scratchpad sur l'archive : audit_jets.bilan() donne 253 tirages de table, 36 jets hérités et 164 dérogations, soit 39 % des jets non hérités tirés à une probabilité choisie par le moteur.
- Famille DATES ET JOURS. Erreurs : piège n° 30 (échéance du 30/12/2040, un dimanche) ; peu d'autres depuis controle_coherence.py (174 dates contrôlées le 23/07, 1 019 le 09/08, aucune erreur). Reste mal couvert : (a) le motif ne lit que « jour + JJ/MM », donc les en-têtes de tour écrits en toutes lettres (« Mardi 17 juillet 2040 ») ne sont pas contrôlés : 65 occurrences dans l'archive, justes par chance ; (b) ni les dates relatives (« demain », « lundi prochain », « sous huit jours ») ni les dates dans les PDF ; (c) aucune fonction de jours ouvrés : SWIFT en 2 à 5 jours ouvrés et virement du samedi (pièges 12, 26, 29) sont comptés de tête ; (d) aucun calendrier scolaire ni emploi du temps, alors que William est enseignant et que la reprise du vendredi 01/06/2040 tombe en période de cours ; calendrier_2040.py ne connaît que les fériés ; (e) passer au 01/06 touche 22 fichiers de données qui citent le 17/07 ou le 23/07 : §9 et §12 (« la prochaine : lundi 23/07/2040 »), agenda A001, calages du grand livre, horloge, resume.md, mémoire auto. Une partie de ces mentions est de l'historique de l'univers 1, à distinguer.
- Famille FUSEAUX. Erreurs : n° 48 (« 12h40 au Cap-Vert = 13h40 à Lisbonne » au lieu de 14h40, ce qui a aussi cassé l'ordre du journal) ; pièges 11, 23 et 70. Couverture : fuseaux.py (zoneinfo). Reste mal couvert : aucune vérification automatique des conversions écrites dans le texte. Ma sonde trouve 18 formes « HHhMM à X (HHhMM à Y) » dans l'archive, toutes justes aujourd'hui : le contrôle est faisable. Les lignes de journal mêlent les fuseaux sans le dire : 7 lignes restent hors de l'ordre chronologique dans les journaux archivés (22/07, 23/07, 25/07, 26/07, 30/07, 06/08, 09/08). Le piège n° 6 ne peut donc pas être contrôlé par un script.
- Famille ARGENT. Erreurs : n° 8 (onduleurs à 2 750 € jamais déduits) ; n° 9 (avances non tracées) ; n° 3-4 et piège 2 (net écrit à la place du brut) ; n° 46 et 54 (soldes d'en-tête périmés, « ≈ 6 130 € » écrit à la main contre 6 161,91 € recalculés) ; divergence des sessions (5 972,91 € dans l'une, « ≈ 5 940 € » dans l'autre pour la même nuit). Couverture : grand_livre.py (soldes calculés, prévus, conversion). Reste mal couvert : (a) aucun mouvement récurrent : traitement, mensualité de ≈ 940 €, eau, électricité, assurances (piège 77 le reconnaît) ; (b) le capital restant dû est estimé à la main (« ≈ 109 700 € »), sans amortissement ; (c) l'ETF est figé (288 000 €) ; (d) verifier() n'interdit ni un mouvement daté après l'horloge ni un solde négatif ; (e) rien ne vérifie qu'un montant payé dans le récit a sa ligne au grand livre, donc le n° 8 peut se reproduire ; (f) la paie (points × valeur du point) et la fiscalité France-Luxembourg (piège 17) ne sont pas calculées.
- Famille ÉTATS PÉRIMÉS ET DOUBLONS. Erreurs : n° 7 et 10 (fichiers datés de 3 jours) ; n° 39 (rappel au joueur « Kevin attend une réponse » alors qu'il avait répondu) ; n° 44 (message présent au journal mais absent de whatsapp/) ; n° 46-47 et piège 76 (en-têtes périmés) ; n° 50 (« demande en cours » déjà exécutée). Cause commune : un même fait est écrit dans jusqu'à 7 endroits (journal, whatsapp, fils-ouverts, calendrier, fiche, vies-privées, §9). Le §9 a pesé 157 Ko sur 183 Ko ; fils-ouverts a atteint ≈ 40 000 jetons pour 120 lignes ; le commit 0f6da92 a dû restaurer une ligne 103 cassée par une édition. Couverture : resume_etat.py, archivage du §9, agenda. Reste mal couvert : fils-ouverts, calendrier.md, personnes/ et whatsapp/ restent de la prose tenue à la main ; aucun contrôle de la date d'en-tête des fichiers d'état face à l'horloge ; aucun rapprochement entre whatsapp/ et le journal.
- Famille OUBLIS D'ÉVÉNEMENTS ET DE RITUELS DU MOTEUR. Erreurs : n° 4 et 12 (installation SécuTech, présentation d'Abdoul, revue juridique de Mariette disparues) ; n° 40 (fiche complète du 03/08 oubliée) ; n° 43 (rapport quotidien d'Aïcha du 06/08 omis) ; n° 45 (aucun tour du monde pour les 07-09/08) ; n° 47 de la branche continuation (monde vivant et vie propre oubliés au changement de session) ; fils restés en retard (fibre Orange, Bertin, M. Tanoh) ; revue n° 4 jamais tenue. Couverture : agenda.py dus et retards pour ce qui est daté ; avertissement des échéances échues dans controle_coherence. Reste mal couvert : (a) l'agenda n'a pas de récurrence : un rapport quotidien demande une ligne à écrire chaque jour ; (b) tirage_aleas.py et tour_du_monde.py n'écrivent pas leurs résultats dans l'agenda (connu = non) : le moteur doit les recopier ; (c) aucun échéancier pour les rituels du moteur (fiche courte chaque jour, fiche complète tous les 3 jours, tour du monde, T4 et T5 du dimanche, synthèse de semaine, revue, aléas et message spontané du lundi) ; (d) les promesses des personnages (« je vous envoie ça ce soir ») ne sont pas captées ; (e) une ligne « latent » ne revient jamais d'elle-même.
- Famille PERSONNAGES QUI SAVENT CE QU'ILS NE DEVRAIENT PAS SAVOIR. Erreurs : pièges 54 (Me Kouamé ne pouvait pas « deviner » le statut de fonctionnaire), 56 (secret professionnel) et 79 ; audit du 09/08 (organigramme, offre LinkedIn, hospitalisation de Me Kouamé) ; nombre d'informés tenu à la main (le 9e informé de l'affaire Grace n'a jamais été nommé : « inconnu_9e ») ; n° 39 (le joueur reçoit un fait faux). Couverture : savoir.csv et la commande `peut`. Reste mal couvert : rien n'appelle `peut` automatiquement (ni jet.py, ni tour_du_monde.py, ni chasse_tics.py) ; savoir.verifier() ne contrôle que le format (pas de date future, pas de personne inconnue) ; aucun contrôle n'empêche qu'un élément « connu = non » ou un fait ignoré de William passe dans le texte du joueur ; savoir.csv est vide dans l'univers 2.
- Famille REGISTRE, MORALISATION ET BIAIS DES PROBABILITÉS. Erreurs : n° 20 ; n° 22 (Mariette tutoie, parle à l'impératif) ; n° 23 (Aïcha ordonne, prononce « harcèlement », ultimatum tiré à 50 %) ; n° 25 (réactions de subordonnés à 50 % en moyenne, réactions réparatrices à 60-85 %) ; n° 26-27 (faits cachés inventés hors table) ; n° 35 (M04 mal appliqué, jet de 99,7) ; n° 36 et piège 65 (phrase du moteur attribuée à l'utilisateur) ; n° 38 (verrous) ; piège 69 (refus excessif). Couverture : T1-T14, refus des jets libres par jet.py, audit_jets.py, 9 tournures interdites dans controle_registre, règles 15-17. Reste mal couvert : (a) la garde REACTION_LIBRE et le contrôle du registre lisent les noms dans personnes/ et vies-propres.md. Testé aujourd'hui : PERSONNAGES = '(?!)', donc jet.py accepte n'importe quel jet libre sur une réaction et controle_registre ne voit rien. Les rôles (« le directeur », « une collègue ») ne déclenchent jamais la garde. (b) T1-T3, T7a-d, T9 et T12 sont écrites pour « le patron » face à un subordonné. Dans l'univers 2, William enseigne sans subordonnés, sous une hiérarchie (direction, ministère), parmi des pairs, des élèves mineurs et des parents : la plupart des interactions sortent des tables. Même après T10-T14, le dernier tour audité (09/08, 14h48-14h50) comptait 7 jets libres à probabilités choisies par le moteur (35, 70, 85, 50, 60, 30 et 25 %) pour 16 tirages de table. (c) Le registre de chaque personnage (tu ou vous, langue) n'est stocké nulle part, donc une erreur de tutoiement comme au n° 22 n'est pas détectable. La règle 15 est calibrée pour la Côte d'Ivoire, pas pour le Luxembourg ni la Lorraine.
- Famille INTÉGRITÉ DES TIRAGES. Erreurs : 36 jets hérités tirés hors table ; n° 26-27 ; n° 45 (jet lancé par erreur avec --simule, consigné à la main) ; recalibrages « avec le même dé » faits à la main (n° 35-36) ; bogue d'audit_jets (« du » et « au » des libellés T5 lus comme des issues, revue du 30/07) ; 7 issues frontales observées pour 3,1 attendues au 09/08, jamais examinées. Reste mal couvert : `jet.py --simule` tire et affiche un vrai résultat sans le consigner, et contourne la garde de la règle 17 (ligne 242) : on peut relancer un dé sans que personne ne le voie. memoire/tirages-aleas.md est du texte libre lu par expressions régulières ; les aléas et les initiatives tirés ne sont reliés à aucune échéance.
- Famille FAITS, DROIT ET DÉMARCHES. Erreurs : n° 17 (« faute grave » au lieu de « faute lourde ») ; n° 28 (notaire inventé) ; n° 29 (registre des parts) ; n° 32 (CNPS « 10 % par mois » au lieu de 10 % puis 2 % par mois) ; n° 34 (CDD au lieu de CDI pour la direction : 5 contrats et 4 documents régénérés, messages réécrits) ; n° 16 (banque générique) ; pièges 71 (vol joué avec une heure d'écart), 72-73 et 82. Reste mal couvert : les faits vérifiés vivent en prose dans pieges-connus.md, relu à chaque tour, mêlés aux leçons du moteur. 47 des 82 entrées (≈ 68 % du texte) visent l'univers 1 (Côte d'Ivoire, OSIA, Cap-Vert) et ne servent plus. Aucune source, date de vérification ni fiabilité n'est stockée de façon structurée, aucun outil de recherche n'existe, et INTERDITS ne contient que 2 motifs.
- Famille PRIX ET PROJECTION 2040. La règle 1 impose +30 à 40 %, mais aucune base ne garde le prix de référence ni le coefficient appliqué. Exemples : le tarif d'hôtel a été tiré en jet libre entre deux montants choisis par le moteur (168 ou 189 €, 60 %) ; la même nuit coûte 188 € (chambre 318) dans une session et 189 € (chambre 214) dans l'autre. Les tarifs LinkedIn joués le 06/08/2040 (Career 39,99 €, Business 69,99 €) reprennent les tarifs mensuels de 2026 en dollars donnés par des comparatifs tiers, sans projection traçable. Le vol RAM à 668 € et la nuit du Capitol à 95 000 FCFA n'ont pas de base de calcul consignée.
- Famille PERSONNAGES ET FICHES. Erreurs : n° 13 (4 fiches manquantes) ; n° 49 (M. Konan sans fiche, sans conversation, absent du tour du monde) ; n° 41 (mère de Sandra placée à Esch au lieu de Differdange) ; n° 46 de la branche continuation (Moussa, gardien de nuit, sollicité à midi) ; revue du 06/08 (quartier inventé pour la mère d'Aïcha) ; piège 75 (Konan, Ange-Michel Konan, Koné) ; piège 18 (rythme de nuit de Sandra). Reste mal couvert : les fiches sont en prose ; tour_du_monde.py n'y lit que les lignes de modificateurs. Aucun attribut structuré (domicile, employeur, horaires, registre, âge), aucun contrôle « nom récurrent sans fiche », aucune alerte d'homonymes, aucune disponibilité horaire.
- Famille PDF. Erreurs : n° 1-6 (accents absents, barème sans case pour 95, salaire tronqué, colonnes mélangées, net au lieu de brut, noms sans accents, clauses absentes, scripts rangés dans serveur/) ; n° 42 (coquille « fixé au le QG » répétée dans 5 contrats par le gabarit) ; n° 34 (régénérations en série) ; audit du 09/08 (diplôme remis sans relevés de notes). Couverture : pdf_base.py, verifier_pdf.py (texte extractible et 45 mots non accentués). Reste mal couvert : aucune comparaison entre le contenu et l'état (montants contre grand livre, noms contre fiches, jours de la semaine dans les PDF) ; aucune détection de coquilles (« au le », « de de ») ; aucune pièce obligatoire vérifiée (diplôme, donc relevés) ; un fichier non PDF dans courriels/ ou documents_william/ n'est pas signalé ; le dictionnaire d'accents vise OSIA (Aïcha, Diomandé, Touré, énergies) et ignore lycée, élève, épreuve, mathématiques.
- Famille DIVERGENCE DE SESSIONS ET RELAIS. Erreurs : l'audit Gemini → Claude n° 1-15 (21/07). Trois chronologies sont parties du 09/08 à 14h15 : (1) master ; (2) continuation-9f6d32, 11 commits jusqu'au 11/08 à 13h27 en HEAD détachée, jamais fusionnés ; (3) la session des outils, 48 fichiers modifiés jamais committés, sauvés dans un patch de 1 581 lignes et **toujours non committés aujourd'hui** dans .claude/worktrees/simulation-realistic-tools-d95e81. Au même instant, deux réalités se contredisent : dans l'une, restructuration abandonnée à 14h17, chambre 214 à 189 € ; dans l'autre, chambre 318 à 188 € et Aïcha nommée CEO le 10/08. Les corrections n° 46 et 47 existent deux fois avec des contenus différents. Reste mal couvert : ni verrou, ni compteur de tour, ni contrôle des autres worktrees au début d'une session (seulement une note de mémoire), ni fusion obligatoire à la fin ; pas de fichier AGENTS.md pour un agent de type Codex (seuls CLAUDE.md et GEMINI.md, synchronisés à la main à la ligne 3 près).
- Famille DICTÉE ET PAROLE DE WILLIAM. Erreurs : piège 59 (une pensée en « Je trouve que… » lue comme une parole) ; nombreuses lignes « texte reconstitué d'après la dictée » ; n° 34 a obligé à réécrire des messages de William ; n° 36 et piège 65 (une règle du moteur présentée comme celle de l'utilisateur). Reste mal couvert : les mots bruts dictés par William ne sont pas gardés à côté de leur reconstruction ; la provenance de chaque règle de CLAUDE.md (utilisateur ou moteur, date) n'est pas marquée de façon systématique ni contrôlée.
- Coût de contexte (cause transversale des états périmés et des oubls). Avant toute action, un tour relit ≈ 134 Ko : CLAUDE.md 33,7 Ko, pieges-connus.md 35,2 Ko, modele-pouvoir.md 37,8 Ko, le reste de etat/ ≈ 27 Ko. En fin d'univers 1, CLAUDE.md seul pesait 183 Ko. Plus ce texte grossit, plus la relecture « Scan 5x » laisse passer des éléments périmés sans que personne le voie. Les données structurées (CSV) restent lisibles par n'importe quel agent et se comparent ou se fusionnent dans git ; une base SQLite versionnée ne se fusionne pas et masquerait une divergence.

## Idées

### 1. Relais sûr : verrou de session, compteur de tour et fusion obligatoire (impact 5, effort M, règles/tables : False)
**probleme** : Le 09/08/2040 à 14h15, trois sessions ont continué la même partie : chambre 214 à 189 € dans l'une, chambre 318 à 188 € dans l'autre ; corrections n° 46 et 47 numérotées deux fois ; 48 fichiers de la session des outils toujours non committés. Rien n'a averti l'utilisateur.

**proposition** : Créer `outils/relais.py` avec deux sous-commandes. `debut` refuse de jouer (code 1) dans quatre cas : un autre worktree a des commits absents de master ; des fichiers modifiés non committés existent ailleurs ; le verrou `etat/session.json` est tenu par une autre session depuis moins de 24 h ; master a avancé depuis le commit de base. `--forcer "raison"` passe outre et consigne la raison. `fin` incrémente le numéro de tour, committe, fusionne en avance rapide dans master puis libère le verrou. Les numéros de correction sont attribués par l'outil (`relais.py correction`, maximum lu sur toutes les branches + 1). Ajouter un AGENTS.md identique à CLAUDE.md sauf la ligne 3, et étendre controle_maitres aux trois fichiers.

**mise_en_oeuvre** : Python standard et git en sous-processus (`git worktree list --porcelain`, `git log master..BRANCHE`, `git -C WT status --porcelain`). `etat/session.json` contient : session, agent (Claude, Gemini, Codex…), branche, tour n°, horloge, commit de base, heure machine. `etat/tour.txt` est un compteur committé : deux sessions qui l'incrémentent entrent en conflit à la fusion, ce qui rend la divergence visible. Appeler `debut` en tête du §7 et `fin` dans la checklist ; les deux lignes vont dans §10 et §13. Le premier `debut` signalera le worktree simulation-realistic-tools-d95e81, à archiver ou supprimer avec l'accord de l'utilisateur.

**cout_par_tour** : 2 commandes (début et fin), environ 5 à 10 secondes

### 2. Échéancier des rituels du moteur (impact 5, effort S, règles/tables : False)
**probleme** : Fiche complète du 03/08 oubliée (n° 40), rapport quotidien du 06/08 omis (n° 43), aucun tour du monde pour les 07-09/08 (n° 45), monde vivant oublié au changement de session (n° 47 de la continuation), revue n° 4 jamais tenue. Aucun outil ne sait ce que le moteur devait faire depuis le dernier tour.

**proposition** : Créer `outils/rituels.py dus` qui, d'après l'horloge, liste les rituels échus depuis leur dernière preuve : fiche courte chaque jour ; fiche complète tous les 3 jours ; tour du monde pour chaque jour simulé ; T4 et T5 le dimanche soir ; synthèse de semaine ; revue, aléas et message spontané le lundi. Chaque preuve est cherchée dans les fichiers : lignes « Tour du monde du JJ/MM » dans les tirages, existence de memoire/semaine-AAAA-WNN.md et de memoire/revue-lundi-*.md, marqueur « Fiche complète » dans le journal. controle_coherence lève une ERREUR quand un rituel dépasse sa période.

**mise_en_oeuvre** : `etat/rituels.csv` (rituel;periode;preuve_fichier;preuve_motif). Le script lit l'horloge, calcule les échéances et cherche les preuves ; aucune donnée nouvelle à saisir. Branché sur `relais.py debut` (affichage) et sur controle_coherence (blocage).

**cout_par_tour** : 0 commande en plus si l'outil est appelé par relais.py debut ; sinon 1

### 3. Agenda récurrent, alimenté par les tirages et par les promesses (impact 5, effort M, règles/tables : False)
**probleme** : Un rapport quotidien oublié (n° 43) ; des aléas et des initiatives tirés le lundi que le moteur doit recopier à la main (« non révélés, jouer au jour tiré ») ; des promesses comme « je vous envoie ça ce soir » (piège 8) perdues ; des lignes « latent » qui ne reviennent jamais.

**proposition** : 1. Ajouter à agenda.csv une colonne `recurrence` (quotidien_ouvre, hebdo:lun, mensuel:dernier_ouvre, mensuel:JJ), dépliée par `dus` et `retards`. 2. tirage_aleas.py et tour_du_monde.py (T14 et heure T10) écrivent eux-mêmes une ligne connu = non avec le jour et le créneau tirés. 3. Une ligne latent reçoit une date `revoir_le`. 4. `chasse_tics.py --texte` signale toute citation de personnage qui contient un marqueur de promesse (ce soir, demain, lundi, je vous envoie, je reviens vers vous) sans ligne d'agenda créée pendant ce tour.

**mise_en_oeuvre** : Modifier outils/agenda.py (expansion des récurrences, en lecture seule sur le CSV) ; ajouter une fonction `agenda.ajouter_ligne()` importée par tirage_aleas.py et tour_du_monde.py ; ajouter dans chasse_tics.py un motif de promesse, comparé aux lignes d'agenda dont la note porte la date du jour. Rétrocompatible : colonne vide = pas de récurrence.

**cout_par_tour** : 0 commande ; quelques lignes d'agenda écrites automatiquement

### 4. Grand livre complet : récurrents, amortissement, montants du récit (impact 4, effort M, règles/tables : False)
**probleme** : Onduleurs à 2 750 € jamais déduits (n° 8) ; mensualité de ≈ 940 €, eau et électricité absentes du grand livre (piège 77) ; capital restant dû estimé à la main (« ≈ 109 700 € ») ; verifier() accepte un mouvement daté après l'horloge et un solde négatif sans rien dire.

**proposition** : 1. `etat/recurrents.csv` (libelle;compte;montant;regle_date;debut;fin;indexation) et `grand_livre.py echeances --jusqua D`, qui crée les prévus (traitement, mensualité, factures, abonnements). 2. Une table d'amortissement (capital, taux, durée), dont le capital restant dû est calculé et non saisi. 3. verifier() : ERREUR pour un mouvement daté après l'horloge, avertissement pour un solde négatif (frais de découvert à jouer). 4. Dans controle_coherence, un avertissement pour tout montant en € ou FCFA du journal du jour placé près d'un verbe de paiement (payé, réglé, carte, virement, prélevé) sans ligne du même montant ce jour-là au grand livre.

**mise_en_oeuvre** : CSV en Python standard ; les paramètres du prêt (taux, durée, date de début) appartiennent à la biographie de William : à faire fixer par l'utilisateur avant l'écriture. `echeances` tourne à chaque fiche complète ; les fiches de finances citent `solde --projete`.

**cout_par_tour** : 0 commande par tour ; 1 commande à chaque fiche complète

### 5. Placements et salaire qui bougent : ETF tiré chaque mois, indexation (impact 3, effort M, règles/tables : True)
**probleme** : L'ETF reste à 288 000 € dans l'univers 2. Dans l'univers 1, sa valeur (290 271 €) avait été écrite à la main. Le traitement « ≈ 9 300 € » ne dérive ni des points ni d'une indexation : rien ne bouge sans que le moteur le décide.

**proposition** : Créer `outils/marche.py mois AAAA-MM` : il tire le rendement mensuel de l'ETF selon une loi dont les paramètres sont fixés par l'utilisateur, l'écrit au grand livre comme valeur, et le consigne au journal des tirages. Créer aussi `outils/paie.py` : points × valeur du point projetée, retenues, net, avec une ligne au grand livre via les récurrents.

**mise_en_oeuvre** : Un tirage par mois simulé, lancé par rituels.py le dernier jour ouvré. Paramètres dans `etat/economie.md` (moyenne, écart-type, krach rare). Valeur du point et retenues vérifiées par recherche web, puis projetées en 2040 et consignées dans la base des faits.

**cout_par_tour** : 1 commande par mois simulé

### 6. « Qui sait quoi » branché sur les tirages et sur le texte du joueur (impact 4, effort M, règles/tables : False)
**probleme** : Me Kouamé ne pouvait pas « deviner » le statut de William (piège 54) ; l'audit du 09/08 a relevé des risques sur l'organigramme, l'offre LinkedIn et l'hospitalisation ; le joueur a reçu un rappel faux (n° 39). Aujourd'hui, `savoir.py peut` n'est appelé par aucun outil.

**proposition** : 1. Ajouter à savoir.csv une colonne `mots_cles`. 2. Ajouter `--sur FAIT` à jet.py et à tour_du_monde.py : refus si le personnage ne connaît pas le fait, sauf fuite tirée en T5. 3. `chasse_tics.py --texte` signale les mots-clés d'un fait que William ignore, ou d'une ligne d'agenda connu = non, dans le texte destiné au joueur ; et ceux d'un fait ignoré par le personnage qui parle dans ses propres citations. 4. savoir.verifier() refuse une date postérieure à l'horloge et une personne sans fiche.

**mise_en_oeuvre** : Modifier savoir.py (colonne optionnelle, compatible avec l'existant), jet.py (argument facultatif), chasse_tics.py (lecture de savoir.csv et d'agenda.csv). Les citations sont attribuées par le format « **Nom** : « … » » déjà en usage dans les journaux.

**cout_par_tour** : 0 commande en plus (le contrôle du brouillon est déjà dans la routine)

### 7. Fiches de personnages structurées : attributs, disponibilités, registre (impact 5, effort M, règles/tables : False)
**probleme** : Mère de Sandra à Esch au lieu de Differdange (n° 41) ; Moussa, gardien de nuit, sollicité à midi (n° 46 de la continuation) ; M. Konan sans fiche (n° 49) ; homonymes Konan et Koné (piège 75) ; tutoiement de Mariette (n° 22) impossible à détecter.

**proposition** : En tête de chaque personnes/*.md, un bloc « clé : valeur » : nom complet, alias, rôle, âge, domicile, employeur, horaires par jour, registre avec William (tu ou vous, langue), table par défaut, proches. Créer `outils/personnes.py` avec : `dispo NOM "2040-06-04 12:00"` (au travail, dort, libre) ; `manquants` (nom vu au moins 3 fois dans journal/ et whatsapp/ sans fiche) ; `homonymes` (noms proches) ; `registre` (une citation d'un personnage au « vous » qui contient tu, te, toi, ton ou ta est signalée).

**mise_en_oeuvre** : Le bloc reste du Markdown lisible par tout agent. personnes.py en Python standard. jet.noms_personnages() lit aussi les alias et les rôles. controle_coherence appelle `manquants` et `registre` (avertissements). T11 peut lire les horaires pour placer les événements.

**cout_par_tour** : 0 commande (contrôles intégrés) ; une fiche remplie à chaque nouveau personnage récurrent

### 8. Garde de la règle 17 par rôle et non seulement par nom (correctif immédiat) (impact 4, effort S, règles/tables : False)
**probleme** : Testé aujourd'hui : sans fiche dans personnes/, PERSONNAGES vaut '(?!)'. jet.py accepte donc n'importe quel jet libre sur une réaction, et controle_registre ne voit rien. Même plus tard, « le directeur accepte » ou « une collègue en parle » ne déclenchent jamais la garde, car elle ne reconnaît que des noms.

**proposition** : Ajouter à REACTION_LIBRE un lexique de rôles (collègue, directeur, directrice, proviseur, voisin, voisine, parent d'élève, élève, inconnu, inconnue, serveur, banquier, propriétaire, mère, père, frère, sœur, ex, ami, amie…), en plus des noms. Ajouter un compteur de dérogations par tour : avertissement au-delà de 2, rappel dans audit_jets.

**mise_en_oeuvre** : Modifier outils/jet.py (une constante de rôles, unie à PERSONNAGES) et audit_jets.py (dérogations par tour, comptées à partir de l'heure simulée consignée). Tester avec `--blanc`.

**cout_par_tour** : 0 commande

### 9. Tables adaptées à l'univers 2 : pairs, hiérarchie au-dessus de William, inconnus, promesses, traces (impact 5, effort M, règles/tables : True)
**probleme** : T1-T3, T7a-d, T9 et T12 décrivent « le patron » face à un subordonné. William est maintenant enseignant, sans subordonnés. Dans l'univers 1, les dérogations sans table concernaient déjà les partenaires non hiérarchiques, les inconnues, les candidats, un artisan, la ponctualité, la tenue d'une promesse, les traces de vie propre et les règles commerciales d'un tiers ; au 09/08 il en restait 7 en un seul tour, à des probabilités de 25 à 85 % choisies par le moteur.

**proposition** : Proposer à la revue du lundi n° 1, pour validation par l'utilisateur seul : T15, réaction d'un pair (collègue, ami, partenaire de sport) ; T16, décision d'un supérieur de William (direction du lycée, ministère), à côté de T6 ; T17, première réaction d'un inconnu ou d'une rencontre (avec « réciproque » et « calcul ») ; T18, tenue d'une promesse et ponctualité d'un tiers ; T19, trace visible de vie propre (statut, photo). jet.py refuse T1, T9 et toute table relationnelle sur un personnage dont la fiche indique un âge inférieur à 18 ans (limite b du §11).

**mise_en_oeuvre** : Pourcentages proposés dans `etat/proposition-T15-T19.md` et calés sur les dérogations de l'univers 1 (catégories listées par audit_jets). Après validation : sections ajoutées dans etat/modele-pouvoir.md, `jet.py --liste` pour la validation, une ligne ajoutée à la règle 17 dans les deux fichiers maîtres. Mesurer la part de dérogations avant et après.

**cout_par_tour** : 0 en plus : remplace des jets libres par des tirages de table

### 10. Journal des tirages structuré, sans relance invisible (impact 4, effort M, règles/tables : False)
**probleme** : `jet.py --simule` tire et affiche un vrai résultat sans le consigner, et contourne la garde (ligne 242) : un dé peut être relancé sans trace. Un jet a été lancé par erreur en --simule (n° 45) ; les recalibrages « même dé » (n° 35-36) ont été faits à la main ; audit_jets a lu « du » et « au » comme des issues (revue du 30/07).

**proposition** : 1. Écrire chaque tirage dans `memoire/tirages.jsonl` : id, heure machine, heure simulée, table, modificateurs, distribution, valeur du dé, issue, libellé, statut (joué, caché, révélé, corrigé). memoire/tirages-aleas.md devient une vue générée. 2. `--simule` consigne aussi dans `memoire/simulations.jsonl` ; audit_jets signale un vrai tirage dont le libellé ressemble à une simulation antérieure. 3. `jet.py --corriger ID --mod …` recalcule l'issue avec la même valeur de dé et consigne la correction. 4. audit_jets lit le JSONL, plus d'expressions régulières.

**mise_en_oeuvre** : Modifier jet.py, tirage_aleas.py, tour_du_monde.py (une seule fonction consigner) et audit_jets.py ; ajouter un script de vue. Une ligne JSON par tirage reste fusionnable dans git, un tirage par ligne.

**cout_par_tour** : 0 commande en plus

### 11. Base des faits vérifiés, séparée des leçons du moteur (impact 4, effort M, règles/tables : False)
**probleme** : Faute grave au lieu de faute lourde (n° 17), notaire inventé (n° 28), registre des parts (n° 29), majoration CNPS (n° 32), CDD au lieu de CDI (n° 34, dizaine de pièces refaites). Les faits vivent dans pieges-connus.md (35 Ko relus à chaque tour), dont 47 entrées sur 82 ne concernent plus l'univers 2.

**proposition** : Créer `etat/faits.csv` (id;pays;domaine;enonce;source;date_verif;fiabilite primaire|secondaire|projection;projection_2040;motif_interdit;remplace) et `outils/faits.py` : `chercher "période d'essai" --pays lu` avant d'écrire, `ajouter` après une recherche web, `perimes` pour les faits à revérifier. controle_coherence construit INTERDITS à partir de la colonne motif_interdit. Scinder pieges-connus.md en leçons générales (courtes, relues à chaque tour) et en faits rangés par pays (consultés à la demande).

**mise_en_oeuvre** : Migration en une fois : les faits de l'univers 1 passent avec pays = ci, cv ou ma, et ne sont plus lus par défaut. Les leçons restent dans pieges-connus.md, sans en supprimer : déplacement avec renvoi, conformément au §7. faits.py en Python standard, recherche par mots et par pays.

**cout_par_tour** : 0 à 1 commande (une recherche quand un fait vérifiable intervient)

### 12. Base de prix projetés 2040 (impact 4, effort M, règles/tables : True)
**probleme** : Tarif d'hôtel tiré entre deux montants inventés (168 ou 189 €) ; la même nuit coûte 188 € dans une session et 189 € dans l'autre ; les tarifs LinkedIn joués en 2040 (39,99 et 69,99 €) reprennent ceux de 2026 sans projection ; aucun prix de référence n'est consigné.

**proposition** : Créer `etat/prix.csv` (article;lieu;unite;prix_ref;devise;annee_ref;source;date_releve;fourchette_basse;fourchette_haute) et `outils/prix.py "nuit hôtel Luxembourg-Ville juin"`. L'outil applique le coefficient de la règle 1 (ou un coefficient par pays à valider), tire une valeur dans la fourchette, consigne le tirage et renvoie un montant prêt pour `grand_livre.py ajouter --prix-ref ID`.

**mise_en_oeuvre** : CSV rempli au fil des recherches web (une ligne par prix utilisé). Le tirage dans la fourchette passe par la fonction de consignation commune de jet.py. Le coefficient par pays et la loi du tirage sont à valider par l'utilisateur.

**cout_par_tour** : 1 commande par achat notable (remplace une recherche et un jet libre)

### 13. Contrôle des dates étendu : toutes lettres, en-tête, jours ouvrés, calendrier scolaire (impact 4, effort M, règles/tables : False)
**probleme** : Les en-têtes de tour en toutes lettres (« Mardi 17 juillet 2040 », 65 occurrences dans l'archive) ne sont pas contrôlés ; SWIFT en jours ouvrés et virement du samedi calculés de tête (pièges 12, 26, 29) ; aucun calendrier scolaire alors que William enseigne et que la reprise du 01/06/2040 tombe en période de cours.

**proposition** : 1. controle_jours lit aussi « jour JJ mois [AAAA] » et vérifie que la dernière ligne d'en-tête du journal correspond à l'horloge (jour, heure, lieu). 2. `calendrier_2040.py ouvres --depuis D --jours N --pays lu` pour les délais. 3. Calendrier scolaire luxembourgeois 2039-2040 et 2040-2041 (congés, Pentecôte, examens), vérifié par recherche web et projeté, et `etat/emploi-du-temps.csv` (jour;heure;classe;salle) déplié en récurrences dans l'agenda. 4. Ce contrôle s'applique aussi au texte extrait des PDF.

**mise_en_oeuvre** : Modifier outils/controle_coherence.py (motif en toutes lettres, déjà testé sur l'archive : 65 dates, 0 erreur) et outils/calendrier_2040.py (fonction ouvres, données scolaires). L'emploi du temps appartient à la biographie de William : à faire valider par l'utilisateur.

**cout_par_tour** : 0 commande

### 14. Constantes de l'univers et outil de redatation (reprise au 01/06/2040) (impact 4, effort S, règles/tables : False)
**probleme** : Passer du 17/07 au 01/06 touche 22 fichiers de données : §9 et §12 (« la prochaine : lundi 23/07/2040 »), agenda A001, calages du grand livre, horloge, resume.md, mémoire. Chaque redémarrage se fait à la main, avec un risque de laisser des dates mortes.

**proposition** : Créer `etat/univers.json` (numéro d'univers, date et heure de départ, lieu, soldes initiaux, date de la première revue) et `outils/redater.py`. `--audit` liste toute mention de l'ancienne date de départ et des dates dérivées, en distinguant l'historique de l'univers 1 des données vivantes. `--appliquer` régénère l'horloge, les calages du grand livre, les lignes d'agenda de départ (revue n° 1 au lundi 04/06/2040) et resume.md.

**mise_en_oeuvre** : Python standard. Les fichiers maîtres sont modifiés avec le script CRLF habituel, en gardant l'égalité à la ligne 3 près. controle_coherence vérifie que l'horloge n'est pas antérieure à la date de départ et qu'aucune échéance vivante ne la précède.

**cout_par_tour** : 0 par tour ; 1 commande par redémarrage

### 15. Conversions horaires vérifiées et fuseau explicite dans le journal (impact 3, effort S, règles/tables : False)
**probleme** : « 12h40 au Cap-Vert = 13h40 à Lisbonne » au lieu de 14h40 (n° 48) ; 7 lignes de journal archivées restent hors de l'ordre chronologique, en partie parce que des heures d'Abidjan et de Lisbonne s'y mêlent sans le dire.

**proposition** : 1. controle_coherence repère les formes « HHhMM à X (HHhMM à Y) » et « … = … » et les vérifie avec fuseaux.py (sonde : 18 conversions dans l'archive). 2. Une ligne de journal dont l'heure n'est pas dans le fuseau de l'horloge porte son lieu (« 08h08 (Abidjan) »). 3. Le contrôle de l'ordre trie les lignes par instant UTC.

**mise_en_oeuvre** : Environ 40 lignes dans controle_coherence.py, en important fuseaux. Avertissement, non bloquant, pour l'ordre ; erreur pour une conversion fausse.

**cout_par_tour** : 0 commande

### 16. Source unique et vues générées : messages, fils ouverts, en-têtes (impact 5, effort L, règles/tables : False)
**probleme** : Un même fait est écrit dans jusqu'à 7 fichiers. Résultats : message absent de whatsapp/ (n° 44), rappel faux (n° 39), « demande en cours » restée ouverte (n° 50), ligne 103 de fils-ouverts cassée (commit 0f6da92). L'abandon du 09/08 a obligé à annoter à la main les fils 105, 108, 109, 113 et 114.

**proposition** : 1. `etat/messages.jsonl` : id, instant UTC, canal, de, à, texte, dictée brute, lu par William, connu. Les fichiers whatsapp/*.md deviennent des vues générées et le journal cite les id. 2. `etat/fils.csv` (id;titre;statut;echeance;depend_de;note) avec `fils.py`, qui propage une annulation vers les fils dépendants et les liste pour décision. 3. controle_coherence compare la date d'en-tête « (au JJ/MM) » de chaque fichier d'état à l'horloge : avertissement au-delà de 3 jours simulés. 4. Une base SQLite dérivée (`base.py construire` → etat/monde.sqlite, ignorée par git) sert aux requêtes ; les CSV et JSONL restent la source, parce qu'ils se comparent et se fusionnent dans git et que tout agent les lit.

**mise_en_oeuvre** : Migration progressive : d'abord les messages (le plus de doublons), puis les fils. Les vues Markdown restent identiques à l'œil pour le joueur et pour les autres agents. `vues.py` régénère les vues dans `relais.py fin`.

**cout_par_tour** : 1 commande par message ou fil (remplace 2 à 4 éditions de fichiers)

### 17. PDF contrôlés sur le fond : manifeste, coquilles, pièces liées (impact 3, effort M, règles/tables : False)
**probleme** : Coquille « fixé au le QG » reproduite dans 5 contrats (n° 42) ; net au lieu de brut et barème sans case pour 95 (n° 2-4) ; diplôme sans relevés ; 5 contrats et 4 documents régénérés après le n° 34. verifier_pdf ne contrôle que les accents, avec un dictionnaire conçu pour OSIA.

**proposition** : 1. Chaque générateur écrit une ligne dans `etat/pieces.csv` (fichier;type;montants;dates;personnes;source_des_donnees) et lit ses données dans les fichiers structurés, sans valeurs codées en dur. 2. verifier_pdf contrôle les montants contre le grand livre ou la fiche, les jours de la semaine dans le texte extrait, les mots doublés (au le, de de, le la), les pièces obligatoires (diplôme, donc relevés de M1 et M2) et les fichiers non PDF dans courriels/, documents_william/ et serveur/. 3. Le dictionnaire d'accents s'étend à l'univers 2 (lycée, élève, épreuve, mathématiques, ministère, Éducation, réglementaire).

**mise_en_oeuvre** : Modifier outils/verifier_pdf.py (pypdf déjà utilisé) et outils/pdf_base.py (méthode `manifeste()` appelée par `sauver()`). Réutiliser le contrôle des jours de controle_coherence.

**cout_par_tour** : 0 commande (verifier_pdf est déjà dans la routine)

### 18. Brouillon contrôlé contre l'issue tirée et le lexique moralisant (impact 4, effort M, règles/tables : False)
**probleme** : Une issue « rien » ou « évitement » glisse vers une phrase polie qui porte le message du moteur (piège 50) ; Aïcha prononce « harcèlement » (n° 23). controle_registre ne connaît que 9 tournures fixes, et seulement après coup, dans le journal.

**proposition** : 1. jet.py écrit la dernière issue tirée de chaque personnage dans `etat/issues-du-tour.csv`. 2. `chasse_tics.py --texte` signale, dans le brouillon, une citation de plus de N mots ou du lexique de confrontation pour un personnage dont l'issue est rien_*, evitement ou execute_sans_discuter. 3. Il signale aussi le lexique normatif dans la bouche d'un personnage (ce n'est pas normal, tu n'as pas le droit, inacceptable, harcèlement, consentement, abus de pouvoir), sauf pour un tiers T6. Le registre luxembourgeois et lorrain (tutoiement entre collègues, langues) est lu dans les fiches structurées.

**mise_en_oeuvre** : Modifier outils/chasse_tics.py et jet.py (une écriture CSV). Avertissements non bloquants, à relire avant l'envoi ; listes complétées à chaque revue du lundi.

**cout_par_tour** : 0 commande en plus (le contrôle du brouillon est déjà dans la routine)

### 19. Dictée brute conservée et provenance des règles contrôlée (impact 3, effort S, règles/tables : False)
**probleme** : Une pensée en « Je trouve que… » a été prise pour une parole (piège 59) ; des messages de William ont été « reconstitués » puis réécrits (n° 34) ; une phrase du moteur a été présentée comme une règle de l'utilisateur (n° 36, piège 65).

**proposition** : 1. Garder la dictée brute de William à côté du texte retenu (colonne `dictee_brute` des messages, ou citation dans le journal), avec un glossaire `etat/dictee.csv` (entendu;interprete;confirme_par_utilisateur). 2. Dans CLAUDE.md, chaque paragraphe de règle porte « (demande de l'utilisateur, date) » ou « (rédigé par le moteur, date) ». controle_coherence signale les paragraphes de règle sans provenance.

**mise_en_oeuvre** : Ajout d'une colonne ou d'un fichier CSV ; contrôle par expression régulière sur les §3, §5, §11 et §12 des deux fichiers maîtres. Le marquage des règles existantes se fait une fois, avec l'utilisateur pour les cas douteux.

**cout_par_tour** : 0 commande
