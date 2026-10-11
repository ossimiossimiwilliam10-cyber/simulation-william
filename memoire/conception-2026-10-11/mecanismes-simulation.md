# Mécanismes de simulation : temps, corps, horloges, économie, avance rapide

> Exploration rendue le 11/10/2026 (date réelle) par un agent du workflow « simulation-ameliorations-conception » (session interrompue par la limite d'utilisation). Texte conservé tel quel ; ce qui en a été installé ou proposé est dans `memoire/propositions-2026-10-11.md` et `outils/LISEZMOI.md`. Les dates « 1er juin 2040 » y renvoient à une demande de départ que l'utilisateur a ensuite remplacée par le samedi 14/07/2040.


## Constats

- Le vendredi 1er juin 2040 (semaine ISO 22) est un jour de classe au Luxembourg. Pâques tombe le 01/04/2040 et Pentecôte le 20/05 (calendrier_2040.py), donc le congé de Pentecôte est fini, et l'année scolaire se termine vers la mi-juillet (mercredi 15/07 en 2026, règlement grand-ducal du 18/07/2025). Or tous les fichiers d'état (william.md, horloge.txt, agenda A001-A003, calendrier.md, journal du 17/07) décrivent encore les vacances d'été du 17/07.
- Échéances réelles qui tombent dès le début du jeu : (1) la déclaration de revenus française d'un résident de Moselle, avec une date limite en ligne au jeudi 4 juin en 2026 pour les départements 55 à 976 et une pénalité de 10 % en cas de retard ; (2) la veille de la Fête nationale, le vendredi 22/06/2040 (retraite aux flambeaux, feu d'artifice tiré du pont Adolphe), puis le samedi 23/06 férié ; (3) la fin de l'année scolaire luxembourgeoise : en 2025, les écrits de l'examen de fin d'études secondaires ont commencé le 19 mai, puis viennent les corrections, les conseils de classe et les bulletins.
- Métier : la tâche de base d'un professeur de lycée est de 22 leçons par semaine. Les décharges d'ancienneté commencent à 45 ans (barème de 2007, modifié en 2023, à reconfirmer). Une leçon dure 50 minutes (45 dans certaines sections). Exemple d'horaire réel, à l'Athénée : longues après-midi jusqu'à 15h40 les lundis, mercredis et vendredis, courtes journées jusqu'à 12h40 les mardis et jeudis. Avec ses 3 leçons supplémentaires, William fait environ 25 leçons. Aucune grille horaire n'existe dans les fichiers.
- Transports : la ligne CFL transfrontalière Audun-le-Tiche – Esch-sur-Alzette existe. Elle a déjà été suspendue faute de personnel (5 jours en février 2024) et remplacée par des bus pendant des travaux à la gare d'Esch. Les trajets de William ne sont modélisés nulle part.
- Argent : à Audun-le-Tiche, le taux de taxe foncière (bâti) était de 49,22 % en 2025, plus 13,65 % de TEOM. L'indexation automatique luxembourgeoise (tranche de 2,5 %) a été déclenchée au 1er juin 2026. Le jour de versement du traitement est encore « à établir » (A002). Dans finances.md, les autres charges sont « à établir au fil du jeu » : le compte courant reste figé tant que le récit ne parle pas d'argent.
- Corps : la seule trace est une ligne de prose (« réveillé à 07h05, reposé ») et le seul effet vient d'A17 (5 % par semaine). Repère réel : environ 1,4 blessure pour 1 000 heures de pratique du MMA (étude rétrospective de 2025, 112 pratiquants). À 7-8 heures par semaine, cela fait environ une blessure tous les deux ans.
- Météo : normales de Findel pour juin (1991-2020) : 16,7 °C en moyenne, maxima d'environ 21,7 °C, environ 75 mm de pluie. Aujourd'hui, la météo est écrite à l'intuition, sans continuité d'un tour à l'autre.
- Droit local d'Alsace-Moselle : il est en principe interdit d'employer des salariés le dimanche dans le commerce (exceptions limitées, dans la limite de 5 heures). Les horaires des lieux de Moselle et du Luxembourg ne sont pas les mêmes, et aucun registre de lieux n'existe.
- Rythme de l'univers 1 : 24 jours simulés (du 17/07 au 09/08) en 4 jours réels (du 05 au 08/10/2026), environ 217 commits « feat », soit à peu près 9 tours par jour simulé. Cela a produit 425 Ko de journaux (environ 18 Ko par jour) et un §9 gonflé à 157 Ko. Au même rythme, une année simulée ferait environ 3 300 tours et 6,5 Mo de journaux : la règle « lire tous les fichiers avant chaque tour » devient intenable sans données structurées ni résumé généré.
- Coût actuel d'un tour : environ 8 commandes (resume_etat, agenda dus, horloge --regler, grand_livre ajouter, savoir ajouter, agenda clore, chasse_tics --texte, controle_coherence), plus la lecture de tous les fichiers. La table T10 a été créée après 135 dérogations (jets libres sur des délais) : tout mécanisme sans table ni formule retombe sur des choix libres du moteur.
- Le monde est vide : aucun personnage récurrent, et personnes/, vies-propres.md, vies-privees.md, savoir.csv et traces.md sont vides. Le tour du monde (T11, T13, T14) ne tire donc rien. Le pack d'aléas actif vise Abidjan (A01 paludisme, A03 enfants de Sandra, A04 délestages, A06 fournisseurs) : dans l'univers 2, il produira surtout des « sans objet ».
- Les états clés sont en prose que les outils ne savent pas lire : fils-ouverts.md, vies-propres.md (seules les lignes de modificateurs sont lues par regex dans tour_du_monde.py), traces.md, le corps dans william.md. T10 ne donne qu'une catégorie de délai : l'heure exacte reste un choix libre du moteur.
- La plupart des élèves de lycée sont mineurs. La limite du §11 (b) n'est garantie que par le texte des règles : ni jet.py ni controle_coherence.py ne connaissent l'âge des personnages.
- Sessions parallèles : trois worktrees existent (continuation-9f6d32 en HEAD détaché, simulation-realistic-tools-d95e81 à cf66dbb, et celui-ci), et l'univers 1 a divergé en trois chronologies. Les données actuelles (CSV et Markdown) se fusionnent ligne à ligne. Une base binaire (SQLite) versionnée dans git rendrait ces fusions impossibles.

## Idées

### 1. Un tour en deux commandes : orchestrateur tour.py (début, fin, go) (impact 5, effort M, règles/tables : False)
**probleme** : Un tour coûte déjà environ 8 commandes en plus de la lecture de tous les fichiers. Chaque mécanisme proposé ci-dessous en ajouterait 1 à 3 et serait oublié un tour sur deux. Exemples de l'univers 1 : fiche complète du 03/08 oubliée (correction 40), en-têtes de finances et de profil périmés (piège 76), horloge non réglée en fin de tour (piège 78).

**proposition** : Un point d'entrée unique, outils/tour.py. Il appelle les outils existants comme bibliothèques et accueille chaque mécanisme nouveau comme une « étape » ajoutée au registre. 1) « tour.py debut » écrit une fiche moteur de 30 lignes au plus, jamais montrée au joueur : heure et lieu, météo, corps en bandes, qui est où selon les routines, ce qui est dû (agenda, prélèvements, paliers d'horloges, initiatives pré-tirées avec leur heure concrète), deux détails d'ambiance non utilisés récemment, alertes (garde « mineurs », tics). 2) « tour.py fin » applique en une fois le corps, l'échéancier, l'avance des horloges, horloge.txt, la clôture des lignes automatiques, un squelette de ligne de journal et le contrôle rapide. 3) « tour.py go » lance l'avance rapide (idée dédiée). Un mécanisme nouveau ne coûte ainsi aucune commande de plus.

**mise_en_oeuvre** : Fichier : outils/tour.py, avec les registres ETAPES_DEBUT et ETAPES_FIN (fonctions f(etat, args) qui renvoient des lignes de fiche).
Arguments de fin de tour :
- --jusqua "AAAA-MM-JJ HH:MM" ;
- --activites "HH:MM-HH:MM type[:détail]; …", avec les types sommeil, cours, trajet, sport, repas, ecran, social, travail_maison, libre ;
- --depense "compte:montant:libellé", répétable (appelle grand_livre.py) ;
- --revele "fait:personne:canal" (appelle savoir.py) ;
- --souvenir et --attente (remplace horloge.py --regler).
Sortie : etat/fiche-tour.md, régénérable. Option --simule partout. Les commandes actuelles restent utilisables seules. À mettre à jour : routine du §7, §13 et LISEZMOI.md (texte de procédure, aucune probabilité modifiée).

**cout_par_tour** : 2 commandes par tour au lieu d'environ 8 ; quelques secondes d'exécution. Les jets de table restent ponctuels.

### 2. Casting de départ tiré au hasard, avec frontière de la biographie et garde « mineurs » (impact 5, effort M, règles/tables : True)
**probleme** : Le vendredi 1er juin 2040, William est en classe, mais aucun personnage n'existe. Le premier tour obligerait le moteur à inventer en direct collègues, direction, classes, coach et voisins, au moment où son biais est le plus fort : personnages commodes, bienveillants ou attirants, « dévoués sans raison », ce que proscrit la règle 2. Les élèves étant en majorité mineurs, la limite du §11 (b) ne repose aujourd'hui que sur la mémoire du moteur.

**proposition** : Un générateur qui tire, rôle par rôle, des personnages ordinaires :
- âge ;
- nationalité et langues, selon des proportions sourcées (corps enseignant public, club, voisinage d'Audun, communautés portugaise et camerounaise) ;
- deux traits ;
- un intérêt matériel principal (le test d'intérêt est prêt d'avance) ;
- un souci, un secret, une routine ;
- une opinion de départ sur William ;
- un registre de langue (luxembourgeois, français, allemand, portugais : règle 9).
Rôles initiaux : département de mathématiques et physique (4-5), direction et secrétariat (3), cinq classes avec 2-3 élèves notables, coach et 4 partenaires d'entraînement, 3 voisins, 1-2 membres de la communauté camerounaise.
Frontière : ce qui relève du monde est tiré et joué. Ce qui toucherait la biographie (ami de longue date, ex, frère, état exact des liens avec les parents, montant du soutien) est demandé à l'utilisateur hors fiction et n'existe qu'avec son accord.
Garde : date de naissance obligatoire. jet.py refuse T1, T9 et toute table relationnelle ou intime pour une personne mineure, et controle_coherence.py le vérifie.

**mise_en_oeuvre** : - etat/tables-casting.md : tables C1 à C6 (traits, intérêts, soucis, secrets, opinion de départ, langue), à valider, lues par jet.py comme les autres tables.
- outils/casting.py --role "collègue de physique" [--nombre 3] [--simule] écrit : personnes/<nom>.md (physique, caractère, lien, historique, champ « Né(e) le ») ; la fiche de vies-propres.md avec ses lignes de modificateurs T11/T13/T14 ; ses lignes de routine ; ses cercles.
- jet.py lit « Né(e) le » pour la garde.
- Une séance de casting avant la reprise (environ 20 personnages), puis un appel à chaque nouveau personnage récurrent.

**cout_par_tour** : 0 par tour ; 1 commande par nouveau personnage récurrent.

### 3. Emploi du temps de William, calendrier scolaire et trajets réels de juin-juillet 2040 (impact 5, effort M, règles/tables : False)
**probleme** : Juin est le mois des corrections, des épreuves de fin d'études, des conseils de classe et des bulletins, puis l'année se termine vers la mi-juillet. Pourtant rien ne dit quelles classes William a, à quelle heure, dans quelle salle. Sans grille, un « Go » jusqu'au mardi peut sauter cinq leçons ou laisser William libre un mardi à 10 h. Les trajets (voiture par Esch et l'A4, ou train Audun-le-Tiche → Esch → Luxembourg) ne sont pas modélisés non plus, alors que la ligne Audun–Esch a déjà été suspendue faute de personnel et pour travaux.

**proposition** : 1) Une grille hebdomadaire de William : 25 leçons de 50 minutes (tâche de base de 22, aucune décharge avant 45 ans, plus ses 3 leçons supplémentaires), sur le modèle d'un lycée réel de la capitale (longues et courtes journées, surveillances, réunions de département). On y ajoute ses plages fixes : sommeil habituel, entraînement cinq soirs, repas. Le moteur la propose et l'utilisateur la valide, car c'est son métier.
2) Un calendrier des périodes 2039-2040, projeté et sourcé : fin des écrits et corrections, oraux, conseils de classe, bulletins, dernier jour, veille de la Fête nationale (22/06), rentrée.
3) Des trajets avec durée minimale, habituelle et maximale par créneau, et un jet libre de perturbation (non moral, autorisé).
La routine conforme aux intentions déclarées de William se narre (règle 13) ; tout écart est une décision de William.

**mise_en_oeuvre** : Données :
- etat/routines.csv (qui;jour;debut;fin;lieu;activite;detail;souplesse fixe|souple|libre;valide_du;valide_au), partagé avec les personnages ;
- etat/periodes.csv (du;au;periode;effet;source;projection) ;
- etat/trajets.csv (de;a;mode;creneau;min;habituel;max;proba_perturbation;source).
Outils :
- outils/routine.py (ou --quand, semaine, trajet) ;
- calendrier_2040.py --scolaire lit periodes.csv ;
- tour.py debut affiche le créneau en cours et le suivant ; tour.py go s'en sert.
Installation : environ 30 minutes et 3-4 recherches. La grille 2040-2041 (410 points) est refaite à la rentrée.

**cout_par_tour** : 0 commande par tour (lu par tour.py).

### 4. Économie quotidienne : échéancier automatique et imprévu du mois (impact 5, effort M, règles/tables : True)
**probleme** : Le compte courant ne bouge que si le récit parle d'argent. Un ménage réel a pourtant 15 à 25 mouvements automatiques par mois : crédit d'environ 940 €, énergie, eau, internet et mobile, assurances, carburant, club, abonnements, soutien aux parents. Il a aussi des échéances annuelles, comme la taxe foncière d'Audun-le-Tiche (49,22 % plus 13,65 % de TEOM en 2025). Exemple : au 30 juin simulé, le solde serait encore de 9 800 € moins les seuls achats racontés. L'indexation luxembourgeoise de 2,5 % et le jour de versement du traitement ne sont suivis nulle part.

**proposition** : 1) Un échéancier : libellé, compte, montant ou fourchette, périodicité (mensuel au jour J, trimestriel, annuel à date, à la consommation), décalage bancaire au jour ouvré suivant, saisonnalité, source et date de vérification. Les montants de 2026 sont vérifiés puis projetés en 2040 avec les coefficients de la base de faits. Les postes biographiques (soutien aux parents, voiture, abonnements) sont demandés une seule fois à l'utilisateur.
2) Les dépenses de consommation découlent des routines (repas au lycée ou en ville, carburant par trajet, courses hebdomadaires), avec un jet libre de montant dans une fourchette vérifiée.
3) Une table T17 « imprévu du mois » à valider : rien (environ 60 %), électroménager, voiture, amende, santé, cadeau ou cotisation, maison ; montant tiré dans une fourchette vérifiée.
4) L'habitude de William (45 % ETF, 45 % épargne, 10 % plaisir) s'exécute seule le lendemain du traitement, comme un ordre permanent.
5) L'indexation devient une horloge « monde », nourrie par les nouvelles du lundi.

**mise_en_oeuvre** : - etat/echeancier.csv (id E###;libelle;compte;montant_min;montant_max;periodicite;jour;decalage;saison;source;verifie_le;statut).
- outils/echeancier.py : bibliothèque, plus « previsions --mois 2040-06 ».
- tour.py fin écrit au grand livre chaque échéance passée (type mouvement, référence E###) et, si William a l'application bancaire, une notification visible.
- T17 rejoint les tables (lue par jet.py) et se tire le premier lundi de chaque mois, pendant la revue.
- controle_coherence.py signale toute échéance passée absente du grand livre.
- Installation : environ 1 heure avec les recherches.

**cout_par_tour** : 0 commande par tour (automatique) ; 1 jet par mois.

### 5. Horloges et fronts : menaces, occasions et projets qui avancent seuls (impact 5, effort M, règles/tables : True)
**probleme** : Les menaces et les occasions n'avancent que si le moteur s'en souvient : fils-ouverts.md est un tableau de prose, sans mécanique d'avance. Dans l'univers 1, la déclaration de l'investissement étranger (« vers le 31/08 »), l'offre écrite promise à Estelle et la fibre du QG ont été suivies à la main. Les conséquences arrivaient soit tout de suite, soit jamais. Exemple de l'univers 2 : la déclaration de revenus française de William tombe dès la première semaine de jeu (en 2026, date limite en ligne au jeudi 4 juin pour la Moselle, pénalité de 10 %). Si William ne s'en occupe pas, rien ne la fait mûrir.

**proposition** : Une horloge a :
- un nom et un type (menace, occasion, projet de William, personnage, monde) ;
- 4, 6 ou 8 segments et un nombre de segments remplis ;
- une visibilité (connue de William ou cachée) ;
- un mode d'avance : soit par le temps, avec un jet par jour ou par semaine dans une table T16 à valider (par exemple 0 segment 55 %, 1 segment 35 %, 2 segments 10 %), soit par événement (« si William ne fait pas X avant J, +2 ») ;
- des paliers écrits dès la création, par exemple « 2/6 rappel par courriel ; 4/6 avis de majoration ; 6/6 taxation d'office », pour qu'aucune conséquence ne s'invente au dernier moment ;
- une échéance éventuelle et des liens (personne, fait de savoir.csv, agenda).
Un front regroupe des horloges autour d'un but (ce que la menace « veut ») et de présages. Les occasions se ferment : si William n'agit pas avant le dernier segment, elles passent à quelqu'un d'autre. Un projet que William lance devient une horloge de progression aux durées réelles.

**mise_en_oeuvre** : - etat/horloges.csv (id;nom;type;segments;rempli;visibilite;avance;table;paliers;echeance;liens;statut;historique).
- outils/horloges.py : creer, avancer H03 +1 --raison, liste, tick --jusqua.
- tour.py fin fait avancer les horloges « temps » échues et remonte les paliers atteints dans la fiche moteur (règle 14 : à jouer, reporter ou annuler).
- controle_coherence.py signale un palier atteint sans ligne de journal.
- La section B de fils-ouverts.md devient peu à peu une vue générée.

**cout_par_tour** : 0 commande en général (avance automatique dans tour.py fin) ; 1 commande pour créer ou avancer une horloge après un acte.

### 6. Avance rapide pilotée par interruptions (le « Go » sûr) (impact 5, effort L, règles/tables : True)
**probleme** : Établir un profil sur environ une année simulée suppose de traverser les journées ordinaires. Au rythme de l'univers 1 (24 jours en environ 217 tours), une année demanderait environ 3 300 tours. Aujourd'hui, le « Go » est narré à la main, avec deux risques : jouer William à sa place (règle 13) ou sauter un événement dû (règle 14). Exemple : un « Go jusqu'à lundi » depuis le vendredi soir doit faire passer l'entraînement du samedi, les courses, le prélèvement du 5, et s'arrêter si un collègue écrit pour demander un remplacement.

**proposition** : « tour.py go --jusqua … » déroule heure par heure la routine de William et des personnages. Il applique le corps, l'échéancier, les horloges, la météo et le tour du monde.
Il s'arrête au premier déclencheur d'une liste fermée, à valider :
- initiative d'un personnage de type demande, information ou tension ;
- palier d'horloge connue de William ;
- échéance connue de l'agenda ;
- seuil du corps (blessure, maladie) ;
- aléa déclenché ;
- rencontre tirée dans un lieu fréquenté ;
- plage « libre » où un choix est nécessaire.
Il rend un relevé factuel des heures écoulées, qui sert de base au récit fluide, et l'heure d'arrêt. Il ne tranche jamais une dépense hors routine ni une réponse à un message.

**mise_en_oeuvre** : - Sous-commande de tour.py : « go --jusqua … [--max-interruptions 1] [--simule] ».
- Une ligne de journal par bloc de routine, puis la fiche moteur au point d'arrêt.
- La liste des déclencheurs vit dans etat/regles-avance.md : l'utilisateur la valide et peut l'élargir ou la resserrer.
- Dépend des idées routines, horloges, échéancier et corps (chaque module absent est simplement ignoré).

**cout_par_tour** : 1 commande par avance rapide, qui remplace plusieurs tours.

### 7. Corps de William : besoins suivis, effets mesurables, jamais affichés en chiffres (impact 4, effort M, règles/tables : True)
**probleme** : Le corps de William tient en une ligne de prose (« réveillé à 07h05, reposé ») et seule A17 (5 % par semaine) a un effet. En juin, un professeur qui corrige tard, fait la navette et s'entraîne cinq fois par semaine (MMA avec sparring) accumule une dette de sommeil, et la blessure existe (environ 1,4 pour 1 000 heures de pratique du MMA). Rien de cela ne pèse aujourd'hui. Exemple : trois nuits de 5 h 30 avant un conseil de classe ne laissent aucune trace dans les scènes.

**proposition** : Cinq variables calculées, jamais montrées en chiffres au joueur :
- dette de sommeil (heures sur 7 jours glissants, besoin de 7 h minimum) ;
- fatigue (0-100 : monte avec les cours, les trajets et l'entraînement, baisse avec le sommeil et le repos) ;
- faim (heures depuis le dernier repas ; besoin énergétique d'un homme de 100 kg très actif, à sourcer) ;
- forme (séances sur 7 jours par rapport à l'habitude de 5 ; poids hebdomadaire selon l'apport) ;
- stress (copies en retard, échéances administratives, conflits ouverts, solde bas).
Effets à trois niveaux :
1) couleur obligatoire de la scène au-delà d'un seuil (bâillements, irritabilité, allure) ;
2) jets sur les seules performances de William (oubli, retard au réveil, erreur de correction, somnolence au volant), dans une table T15 « défaillance de William » à valider. Exemple, dette de plus de 6 h : rien 80 %, oubli 8 %, retard 6 %, erreur 4 %, somnolence 2 % ;
3) risques physiques : blessure par séance (environ 0,2 % pour 1 h 30 en moyenne, plus en sparring) et maladie saisonnière (rhume de l'adulte : 2 à 4 par an), qui précisent A17.
Aucun effet sur les réactions des autres, sauf modificateur validé (option : « William visiblement épuisé » pour T8 et T12).

**mise_en_oeuvre** : - etat/corps.csv (horodatage;variable;valeur;cause), alimenté par l'argument --activites de tour.py fin.
- outils/corps.py (bibliothèque).
- etat/corps-regles.md : seuils, effets et sources ; T15 est lue par jet.py et consignée.
- tour.py debut affiche une ligne du type « Corps : dette 3 h, fatigue haute, forme bonne → montrer : yeux lourds en fin d'après-midi ».
- La section « Corps » de william.md devient une vue générée.

**cout_par_tour** : 0 commande (un argument dans la fin de tour) ; un jet de temps en temps.

### 8. Routines et disponibilité des personnages : qui est où, qui peut répondre (impact 4, effort M, règles/tables : True)
**probleme** : T10 tire une catégorie de délai, pas une heure plausible. Dans l'univers 1, il a fallu écrire à la main que Sandra travaillait de nuit (piège 18), et 135 dérogations de délais se sont accumulées avant T10. Un collègue qui dort, un coach en cours ou un parent au Cameroun (une heure de moins que le Luxembourg en été) ne répondent pas à l'heure tirée. De même, une scène « au club, mardi 19 h » ne sait pas qui s'y trouve.

**proposition** : Chaque personnage récurrent reçoit des lignes de routine (même fichier que William) et un état calculé : sommeil, travail, trajet, libre ou injoignable.
Règle d'application, à valider :
- l'heure issue de T10 se place dans la prochaine plage où la personne est éveillée et disponible (une urgence passe outre) ;
- la routine dit qui est présent dans un lieu à un créneau (club, salle des professeurs, rue) ;
- aucune issue de table n'est modifiée : seule l'heure se déplace.
Un écart à la routine (rendez-vous médical, enfant malade, sortie) se tire en jet libre, environ 10 % par jour. Son contenu vient de la fiche ou de T13c. L'humeur du jour suit le résultat de T11 (le ton seulement).

**mise_en_oeuvre** : - etat/routines.csv, colonne « qui ».
- routine.py dispo "Nom" --quand … ; routine.py presents --lieu club_mma --quand ….
- tour_du_monde.py convertit le résultat de T10 en heure concrète (minute tirée dans la plage disponible, fuseau par fuseaux.py) et écrit l'initiative dans agenda.csv avec connu=non : tour.py debut la fait remonter le moment venu.
- La création de la routine fait partie du casting.

**cout_par_tour** : 0 commande en jeu courant ; 1 à 2 minutes à la création de chaque fiche.

### 9. Lieux vivants : horaires vérifiés, fréquentation, ambiance tournante (impact 4, effort S, règles/tables : False)
**probleme** : Chaque lieu est inventé au moment de la scène : horaires non vérifiés, détails sensoriels répétés. Les revues de l'univers 1 ont relevé « l'odeur de lessive » trois tours de suite, « la clim souffle » et des ouvertures en « Dehors, … ». Autre risque : en Moselle, le droit local interdit en principe l'emploi de salariés le dimanche dans le commerce. Un supermarché d'Audun ouvert un dimanche après-midi serait faux, alors qu'à Luxembourg-Ville les règles diffèrent.

**proposition** : Un registre de lieux, chacun vérifié une seule fois à sa création par une recherche web :
- type, commune, fuseau ;
- horaires par jour et par jour férié, français et luxembourgeois distincts ;
- fréquentation par créneau (faible, moyenne, forte), croisée avec les routines ;
- prix repères et accès (durée depuis la maison) ;
- habitués.
Chaque lieu a aussi un réservoir de 8 à 15 détails d'ambiance par saison et par moment : sons, odeurs, lumière, matières, langues entendues (luxembourgeois, portugais, français, allemand ; règle 9). L'outil propose deux détails non utilisés depuis dix tours et note leur usage. La variété devient mécanique et la chasse aux tics, préventive.

**mise_en_oeuvre** : - etat/lieux.csv (id;nom;type;commune;fuseau;horaires;feries;frequentation;acces;prix;source;verifie_le).
- etat/ambiances.csv (lieu;saison;moment;detail;dernier_usage).
- outils/lieu.py voir club_mma --quand … : ouvert ou non, qui est là, deux détails.
- tour.py debut l'appelle pour le lieu courant.
- Lieux de départ : maison et rue, gares d'Audun et d'Esch, lycée et salle des professeurs, club de MMA, supermarché, boulangerie, station-service luxembourgeoise, Belval.

**cout_par_tour** : 0 commande (dans tour.py) ; environ 5 minutes et une recherche pour créer un lieu, une seule fois.

### 10. Mémoire des personnages et opinion qui s'efface avec le temps (impact 4, effort M, règles/tables : True)
**probleme** : Ce qu'un personnage pense de William vit dans la prose des journaux : 425 Ko en 24 jours, ingérables sur un an. On observe deux défauts opposés : l'oubli (promesses perdues, correction 39) et la sur-utilisation (« l'ex ressorti comme argument à chaque scène », tic proscrit par la règle 5). Dans la vraie vie, un petit froissement s'efface en quelques semaines, une humiliation dure des années, et chacun garde sa propre version.

**proposition** : Une mémoire par personnage. Chaque souvenir a :
- une date, un fait et la version retenue par le personnage ;
- un type (gratitude, dette, rancune, honte, peur, attirance, confiance) ;
- une intensité de 1 à 3 ;
- une demi-vie : 2 semaines, 3 mois, 2 ans ou permanente ;
- la date du dernier rappel.
Deux vues calculées : une opinion (somme décroissante des souvenirs) et un carnet des services rendus et dus.
Avant une scène avec X, l'outil sort les trois souvenirs actifs les plus lourds. Un souvenir déjà évoqué dans les deux scènes précédentes est signalé (anti-tic).
Les sentiments restent libres (règle 17) : l'opinion colore le ton et guide le choix des modificateurs existants dont la condition est remplie (M15, M07…). Option à valider : 2 ou 3 modificateurs nouveaux « opinion très basse / très haute » pour T8, T12 et T14.

**mise_en_oeuvre** : - etat/souvenirs.csv (personne;date;fait;version;type;intensite;demi_vie;dernier_rappel;source), relié à savoir.csv par l'identifiant de fait.
- outils/memoire_pnj.py X : trois souvenirs, opinion, dettes.
- Saisie après une scène qui compte : tour.py fin --souvenir "X:fait:type:intensité".
- tour.py debut affiche la mémoire des personnages présents selon les routines.

**cout_par_tour** : 0 à 1 argument par tour, seulement après une scène marquante.

### 11. Vies des personnages cumulatives : objectifs et soucis en horloges, manœuvres envers William (impact 4, effort S, règles/tables : True)
**probleme** : Le tour du monde tire une catégorie (T11 puis T13), mais le détail est choisi par le moteur et rien ne s'accumule : dix « avancee_objectif » ne mènent à aucun aboutissement. Un personnage qui veut quelque chose de William (argent, appui, place, attention) n'a pas de mécanique de manœuvre propre, seulement des initiatives isolées en T14.

**proposition** : Chaque fiche de vies-propres.md reçoit une horloge d'objectif (6 segments) et une horloge de souci (4 segments) :
- « avancee_objectif » en T11 avance l'objectif d'un segment ;
- « coup_dur » avance le souci d'un segment ;
- « tournant » avance l'une ou l'autre de deux segments (tirée).
Quand une horloge est pleine, l'issue écrite à sa création arrive : promotion, déménagement, rupture, dette exigible.
Un personnage qui a un intérêt envers William reçoit en plus une horloge de manœuvre, avancée par ses « demandes » en T14. Pleine, elle le fait passer à l'acte : demande directe, service rendu pour créer une dette, alliance avec un tiers. Toujours dans le respect des règles 15 à 17.

**mise_en_oeuvre** : - Horloges de type « pnj » dans etat/horloges.csv, liées à la fiche.
- tour_du_monde.py appelle horloges.py avancer selon l'issue tirée.
- La correspondance entre issues et segments est écrite dans etat/modele-pouvoir.md, à valider.
- Chaque fiche affiche par exemple « Objectif 3/6, souci 1/4, manœuvre 2/4 ».

**cout_par_tour** : 0 commande (dans le tour du monde existant).

### 12. Pack d'aléas de l'univers 2 (Lorraine, Luxembourg, juin-juillet) avec contexte requis (impact 4, effort S, règles/tables : True)
**probleme** : Le pack actif vise Abidjan (paludisme, délestages, enfants de Sandra, fournisseurs de Vridi) : la plupart des tirages seront « sans objet », et le monde sera plus calme que la réalité. Manquent des aléas réels d'ici : ligne Audun–Esch suspendue (bus de substitution), bouchons de l'A4, orages de juin et canicule de juillet, rhume ou gastro, panne de voiture, courrier fiscal français ou luxembourgeois, collègue absent à remplacer, réunion convoquée, parent d'élève qui écrit, fraude détectée à une évaluation, colis perdu, SMS frauduleux, travaux chez un voisin.

**proposition** : Un pack de 12 à 15 aléas propres à l'univers 2, avec des taux de base réels et sourcés (par exemple le rhume de l'adulte, 2 à 4 par an, soit environ 5 % par semaine). S'y ajoutent des aléas saisonniers activés par la date : fin d'année scolaire, Fête nationale, soldes, canicule, Schueberfouer, rentrée. Les anciens aléas restent au catalogue avec le statut « univers 1 ». Chaque ligne reçoit un « contexte requis », pour que l'outil ne tire jamais un aléa sans objet. Pas de conteur adaptatif à la RimWorld (menaces indexées sur la réussite de William) : ce serait une justice narrative, contraire à la règle 7. La densité vient des taux réels et des horloges.

**mise_en_oeuvre** : - etat/aleas.md : nouvelles lignes A19 à A35 et colonnes « contexte » et « saison ».
- tirage_aleas.py filtre par contexte (personnes, lieux et objets existants) et par saison.
- Validation par l'utilisateur avant la reprise du 01/06 (il demande les idées maintenant), sinon à la revue du lundi 04/06/2040.

**cout_par_tour** : 0 par tour (le tirage du lundi existe déjà).

### 13. Conséquences différées : catalogue de délais réels et suites pré-tirées (impact 4, effort S, règles/tables : False)
**probleme** : Dans la vraie vie, les conséquences arrivent tard : avis de contravention après un radar, remboursement d'un soin, réponse d'une administration luxembourgeoise, avis d'impôt, rendez-vous chez un spécialiste en Moselle à plusieurs mois. Sans référence, le moteur les fait arriver trop vite ou les oublie. agenda.py --connu non existe, mais le délai y est choisi à la main.

**proposition** : Un catalogue de délais réels. Pour chaque type d'événement : délai minimal, habituel et maximal (jours ouvrés ou calendaires), probabilité que la suite existe (par exemple avoir été flashé), source et date de vérification. Une commande unique tire, au moment même de l'acte, la survenue et le délai (loi triangulaire), puis écrit la ligne d'agenda cachée. La conséquence est fixée avant d'être connue, jamais inventée après coup (même principe que traces.md). Le catalogue grossit à chaque recherche et sert à tout agent.

**mise_en_oeuvre** : - etat/delais.csv (type;min;habituel;max;unite;proba_survenue;source;verifie_le).
- outils/differe.py "Excès de vitesse sur l'A31" --type radar_fr fait un jet libre consigné (non moral, autorisé par la procédure de modele-pouvoir.md) et ajoute une ligne à agenda.csv (connu=non, note « differe:D012 »).
- tour.py debut la fait remonter le jour venu.

**cout_par_tour** : 1 commande, seulement quand un acte a une suite différée.

### 14. Base de faits vérifiés et coefficients de prix 2040 partagés par tous les agents (impact 4, effort S, règles/tables : True)
**probleme** : Les faits vérifiés (date limite fiscale, horaires CFL, taux de taxe foncière, durée d'une leçon) sont dispersés dans pieges-connus.md, dont les 82 entrées mêlent leçons et faits, ou perdus dans un journal. Un autre agent (Gemini, une autre session) refait la recherche et peut trouver un autre chiffre. Et la projection « +30 à 40 % » varie d'une scène à l'autre : le même café coûte +30 % un jour et +40 % le lendemain.

**proposition** : Une base de faits. Chaque fait a : un identifiant, un énoncé, une valeur et son unité, un lieu, une source (URL), une date de vérification, une validité (jusqu'à quand le fait reste fiable), une fiabilité (source primaire ou secondaire) et sa projection en 2040. S'y ajoutent des coefficients de projection fixes par catégorie (alimentation, énergie, logement, transports, services, salaires indexés), validés une fois par l'utilisateur. Avant toute recherche web, le moteur consulte la base. Un fait périmé cité dans un tour ressort en avertissement.

**mise_en_oeuvre** : - etat/faits.csv.
- outils/faits.py : cherche "taxe foncière", ajouter, prix 3.20 alimentation (→ valeur 2040), perimes.
- Migration progressive des faits de pieges-connus.md, qui ne garde que les leçons.
- tour.py debut affiche les faits liés aux lieux et aux échéances du tour.
- controle_coherence.py vérifie les dates de validité.

**cout_par_tour** : 0 à 1 commande par tour ; épargne des recherches web répétées.

### 15. Réputation par cercles et rumeurs qui ne traversent que par des ponts (impact 3, effort M, règles/tables : True)
**probleme** : T5 compte les personnes informées d'une affaire sans savoir dans quels milieux elles vivent. Or la salle des professeurs, les élèves et leurs parents, le club de MMA, la rue d'Audun, la communauté camerounaise et la famille de William sont des mondes séparés, reliés par quelques personnes. Exemple : une rumeur de salle des professeurs, souvent en luxembourgeois (langue que William ne parle pas), n'atteint le club que si un collègue s'y entraîne.

**proposition** : 1) Des cercles (professeurs, élèves et parents, direction, club, voisinage, communauté, famille, réseaux en ligne).
2) L'appartenance de chaque personne, les « ponts » étant les personnes membres de deux cercles.
3) Une réputation de William par cercle, faite d'étiquettes adossées à une preuve de traces.md (fiable, distant, généreux, dur, séduisant, « ne parle pas luxembourgeois »).
4) Une propagation : quand T5 donne une fuite dans un cercle, un jet par pont dans une table T18 à valider décide si elle traverse (par exemple : non 70 %, déformée 20 %, fidèle 10 %).
5) Une première impression : un nouveau personnage arrive avec l'étiquette dominante de son cercle (un sentiment, jamais un acte).

**mise_en_oeuvre** : - etat/cercles.csv (cercle;personne;role;pont).
- Nouvelle colonne « cercle » dans savoir.csv ; savoir.py t5 sort une commande T5 par cercle et les jets de pont.
- etat/reputation.csv (cercle;etiquette;preuve;depuis).
- Tout se calcule le dimanche soir, avec T4 et T5, comme prévu au §12.

**cout_par_tour** : 0 commande par tour ; 1 à 3 jets de plus le dimanche.

### 16. Météo tirée de la climatologie et calendrier des événements publics (impact 3, effort S, règles/tables : True)
**probleme** : La météo est écrite à l'intuition (« 17 °C, 26 °C annoncés »), sans continuité d'un tour à l'autre, et elle ne pèse ni sur le sommeil, ni sur les trajets, ni sur la fréquentation des lieux. Les grands rendez-vous publics (veille de la Fête nationale le vendredi 22/06/2040, fête de la musique, soldes d'été en France, Schueberfouer) ne figurent dans aucune donnée.

**proposition** : Un générateur de météo quotidienne à persistance (chaîne de Markov : beau, variable, pluie, orage, chaleur). Il est calé sur les normales de Findel (juin : 16,7 °C en moyenne, maxima d'environ 21,7 °C, environ 75 mm), relevées d'un décalage de réchauffement à fixer et à sourcer pour 2040. Le tirage a lieu une fois par jour et il est consigné. William voit une prévision légèrement bruitée, jamais le vrai temps à l'avance. Effets : un orage déclenche un jet de perturbation des transports, la chaleur pèse sur le sommeil, la pluie modifie la fréquentation des lieux. Ce générateur recoupe A05 et le remplace. Les événements publics, projetés et sourcés, deviennent une liste interrogeable.

**mise_en_oeuvre** : - etat/meteo.csv (date;type;tmin;tmax;pluie_mm;prevision_veille).
- etat/meteo-parametres.md : matrice de transition et sources (annuaire climatologique MeteoLux).
- outils/meteo.py : tirage du jour et prévision à 3 jours.
- tour.py l'appelle au premier tour de chaque jour.
- etat/evenements-publics.csv (date;lieu;evenement;source;projection), lu par calendrier_2040.py --evenements.

**cout_par_tour** : 0 commande (automatique).

### 17. Journal d'événements en texte et base SQLite reconstruite (substrat des autres mécanismes) (impact 4, effort L, règles/tables : False)
**probleme** : Ajouter une dizaine de fichiers CSV et Markdown multiplie les lectures exigées par la règle « Scan 5x ». Une base SQLite unique serait facile à interroger, mais elle est binaire : impossible à fusionner entre sessions parallèles (l'univers 1 a divergé en trois chronologies) et illisible pour un agent qui n'a pas l'outil.

**proposition** : La vérité devient un journal d'événements en texte : une ligne JSON par fait (avance du temps, jet, mouvement d'argent, révélation, souvenir, avance d'horloge), ajoutée et jamais réécrite. Rien ne disparaît par construction. Les fichiers de référence (lieux, routines, échéancier, faits) restent en CSV. Une commande reconstruit à partir d'eux une base SQLite, ignorée par git, avec des vues : qui est où, soldes, horloges, opinions, échéances. Les outils interrogent la base, mais les fusions git se font sur des lignes de texte, et un agent sans Python peut encore tout lire.

**mise_en_oeuvre** : - etat/evenements.jsonl (id, heure simulée, heure réelle, session et agent, type, données).
- outils/base.py : reconstruire, requete, verifier.
- Une fonction commune ecrire_evenement() utilisée par tous les outils.
- tour.py reconstruit la base en début de tour (environ 1 seconde).
- .gitignore : etat/monde.sqlite.
- Migration : les CSV existants (agenda, grand livre, savoir) sont rejoués comme événements initiaux.

**cout_par_tour** : 0 commande (intégré à tour.py).

### 18. Le téléphone de William : page de lecture pour le joueur (impact 3, effort M, règles/tables : False)
**probleme** : Le joueur joue souvent depuis son téléphone et reçoit tout en prose. Il ne peut pas ouvrir ses messages, consulter son solde ou son agenda, ni relire un courriel, alors que la vraie vie passe par ces écrans. Les « quêtes secondaires » de fin de tour compensent en rappelant ce qu'il a oublié.

**proposition** : Une page HTML privée qui imite un téléphone générique, sans marque :
- conversations (whatsapp/) et courriels reçus (courriels/) ;
- notifications bancaires (seulement ce que la banque montrerait) ;
- agenda connu (lignes connu=oui uniquement) ;
- météo annoncée et notes.
Elle est générée à partir des données, jamais avec un jet, une issue cachée ou une ligne inconnue de William, et mise à jour à la fin de chaque journée simulée ou à la demande (« ouvre mon téléphone »).

**mise_en_oeuvre** : - outils/exporter_telephone.py produit telephone/index.html et ses données JSON.
- Publication par l'outil Artifact, toujours sur la même URL.
- Filtre strict connu=oui, et contrôle automatique qu'aucun identifiant de table (T1 à T18, Mxx, Cx) ni aucun libellé de jet ne figure dans la page.

**cout_par_tour** : 0 par tour ; 1 à 2 commandes par jour simulé ou à la demande.
