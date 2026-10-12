# Idées et propositions pour l'univers 2 (11/10/2026, date réelle) — à valider par l'utilisateur

> Rédigé par le moteur (Claude Opus 5.5) à partir des trois explorations de l'agent précédent (`memoire/conception-2026-10-11/`)
> et de ses recherches. **Rien de ce qui suit n'est en vigueur** tant que l'utilisateur ne l'a pas validé (règle 17 : seul
> l'utilisateur modifie les tables ; la biographie de William lui appartient). Présentation prévue : revue du lundi n° 1
> (lundi 16/07/2040), ou avant si l'utilisateur le demande. Une proposition validée passe dans le fichier concerné
> (`etat/modele-pouvoir.md`, `etat/aleas.md`, `etat/echeancier.csv`…) avec la date de validation ; une proposition refusée reste
> ici, barrée, avec la date.

## A. Déjà installé le 11/10/2026 (aucune règle ni probabilité changée)
- **Relais 100 % fluide** : `outils/relais.py` (briefing d'entrée, sessions parallèles, verrou partagé, note de relais, journal
  des sessions, commit et fusion), `outils/maitres.py` + `AGENTS.md` (Codex et autres), préférences de l'utilisateur dans le dépôt
  (`memoire/preferences-utilisateur.md`), texte exact de chaque tour (`etat/dernier-tour.md`, `journal/tours/`), crochet de
  démarrage pour Claude Code (`.claude/settings.json`).
- **Base de données** : `outils/base.py` (SQLite reconstruite depuis les fichiers, SQL en lecture, recherche plein texte).
- **Orchestrateur** : `outils/tour.py` (deux commandes par tour au lieu d'une dizaine ; aperçu d'avance rapide).
- **Réalisme** : météo tirée sur les normales officielles de Findel ; lever et coucher du soleil ; calendrier scolaire et
  événements publics ; jours ouvrés ; lieux avec horaires et fermetures selon le droit local (14 juillet chômé en Moselle) ;
  ambiances tournantes contre les tics ; 40 faits vérifiés et 18 prix sourcés (projection 2040 fixe × 1,35) ; échéancier des
  mouvements d'argent (prélèvements décalés au jour ouvré) ; suivi du corps ; fronts à paliers écrits d'avance ; générateur de
  personnages selon la démographie réelle (Luxembourg-Ville, Esch, Audun) ; rituels du moteur ; téléphone de William.
- **Intégrité** : journal des tirages en JSON, essais `--simule` tracés, garde de la règle 17 qui reconnaît les rôles, garde
  « mineurs » (`jet.py --pour` refuse T1, T1b et T9), contrôle des dates en toutes lettres, des CSV, de la base.

## B. Propositions qui changent une table ou une règle (validation requise)

### P01 — Quatre tables pour la vie de William au Luxembourg et en Lorraine
Dans l'univers 2, William est enseignant : pas de subordonnés, une hiérarchie au-dessus de lui, des pairs, des élèves mineurs,
des voisins et des inconnus. Les tables T1-T3, T7 et T9 parlent du « patron » : la plupart des scènes à venir n'ont pas de table,
et le moteur retomberait sur des jets libres (dans l'univers 1, jusqu'à 7 par tour, à des probabilités choisies par lui).
Brouillons (format de `etat/modele-pouvoir.md`, pourcentages à corriger librement) :

**T15 — Un pair (collègue, partenaire de club, ami, voisin) face à un acte ordinaire de William** (demande, remarque, service, pique, invitation)
| Issue | % | En scène |
|---|---|---|
| rien_laisse_passer | 30 | Il ou elle encaisse ou accepte sans relief ; rien ne change en apparence. |
| accepte_volontiers | 18 | Dit oui, rend le service, accepte l'invitation. |
| garde_distance | 14 | Répond poliment mais se tient un peu à l'écart les jours suivants. |
| en_parle_a_d_autres | 12 | En parle à un tiers (salle des profs, club, rue) : l'information circule (T5). |
| rend_la_pareille | 10 | Répond du tac au tac, ou rend un service équivalent plus tard. |
| demande_explication | 8 | Pose une question directe, sans hostilité. |
| decline | 6 | Refuse poliment, avec une raison vraie ou commode. |
| frontal_conflit | 2 | Confrontation ouverte : jouer l'acte, pas un discours. |

**T16 — Un supérieur de William (direction du lycée, ministère) face à une demande, un retard ou un écart de William**
| Issue | % | En scène |
|---|---|---|
| laisse_passer | 30 | Rien : ni remarque ni trace. |
| accorde | 18 | Accorde la demande (congé, aménagement, matériel), parfois avec délai. |
| rappel_oral | 18 | Une remarque brève, dans le couloir ou en fin de réunion. |
| demande_ecrite | 12 | Exige une demande ou une explication par écrit. |
| refuse_poliment | 12 | Refus motivé par le règlement ou le budget. |
| note_au_dossier | 6 | Une trace écrite au dossier de William. |
| convocation | 3 | Entretien formel. |
| frontal_saisine | 1 | Transmission au ministère (procédure disciplinaire du statut : recherche web obligatoire avant de la jouer). |

**T17 — Un inconnu ou une rencontre adulte face à une approche de William** (conversation, compliment, invitation)
| Issue | % | En scène |
|---|---|---|
| poli_bref | 30 | Répond poliment, sans prolonger. |
| conversation | 22 | La conversation prend ; rien n'est acquis. |
| ignore | 14 | Ne répond pas, ou à peine (écouteurs, téléphone, pressé). |
| reciproque | 10 | Intérêt réel, retour d'invitation ou de numéro. |
| mefiance | 10 | Méfiance visible (taille, voix, contexte), recul. |
| refus_net | 9 | Refus clair, sans discours. |
| calcul | 5 | Intérêt intéressé (argent, statut, service attendu). |
Modificateurs proposés : « physique remarqué (1,96 m, voix grave) » : conversation +4, reciproque +3, ignore -4, poli_bref -3 ;
« lieu hostile ou heure tardive » : mefiance +6, ignore +4, conversation -6, reciproque -4.

**T18 — Un tiers tient-il une promesse, un rendez-vous, un délai ?** (artisan, collègue, administration, ami)
Proposition : pas de table fixe ; on tire au **taux d'oubli tiré à la création du personnage** (`etat/personnages.csv`, de 3 à
30 % selon sa conscienciosité) ; pour un service ou une administration sans fiche, `donnees/delais.csv`. Issues en cas d'échec :
retard (50 %), report avec excuse (30 %), oubli complet (20 %).

### P02 — Pack d'aléas de l'univers 2 (remplace les aléas d'Abidjan)
Le pack actif vise Abidjan (A01 équipe, A03 enfants de Sandra, A04 délestages, A06 fournisseurs, A05 pluies tropicales) : il ne
produira que des « sans objet ». Proposition : passer A01, A03, A04, A05, A06 au statut « univers 1 » et activer :
| ID | Événement | Probabilité par semaine | Repère |
|---|---|---|---|
| A19 | Rhume, angine ou gastro de William | 5 % | un adulte attrape 2 à 4 rhumes par an |
| A20 | Perturbation des trajets frontaliers (bus en retard, A4 ou N4 bouchée, travaux) | 20 % (semaines de travail) | travaux fréquents en 2025-2026 (F029) |
| A21 | Panne domestique (chauffe-eau, électroménager, fuite) | 4 % | maison ancienne |
| A22 | Courrier administratif (impôts français ou luxembourgeois, CNS, mairie, banque) | 10 % | frontalier : deux administrations |
| A23 | Tentative d'arnaque (SMS de faux colis, faux conseiller bancaire) | 15 % | très courant |
| A24 | Souci de voisinage (bruit, travaux, haie, stationnement) | 5 % | maison mitoyenne |
| A25 | Blessure légère à l'entraînement (entorse, côte, doigt) | 1 % | ≈ 1,4 blessure pour 1 000 h de MMA (étude de 2025) |
| A26 | Imprévu d'argent (amende, réparation, cadeau, cotisation) | 6 % | |
| A27 | Signe d'un ancien (collègue, élève devenu adulte, connaissance) | 8 % | réseau d'un homme de 35 ans |
| A28 | Courriel ou appel du lycée pendant les vacances (réunion de rentrée, ajournements, emploi du temps) | 10 % (juillet), 30 % (fin août) | |
| A29 | Contrôle routier ou radar (si William a une voiture) | 3 % | |
| A30 | Occasion inattendue (proposition de cours particuliers, invitation, bon plan) | 8 % | |
A02, A07, A09, A12, A13, A17, A18 restent actifs (ils valent partout).

### P03 — Météo : remplacer A05 par le générateur, valider la projection
Le générateur est installé (tirage consigné, prévisions bruitées). À valider : le décalage 2040 de +1,5 °C sur les normales
1991-2020 (`donnees/meteo-parametres.csv`), et le fait qu'un orage ou une canicule tirés par la météo produisent leurs effets
(transports, sommeil) sans passer par A05.

### P04 — Effets du corps (fatigue) sur les actes de William
Proposition de seuils : dette de sommeil > 3 h sur 7 jours = fatigue visible ; > 6 h = épuisement ; et une table T19
« défaillance de William fatigué » tirée seulement au-delà de 6 h : rien 80, oubli 8, retard 6, erreur 4, somnolence au volant 2.
Aucun effet sur les réactions des autres sans modificateur validé.

### P05 — Relations chiffrées et modificateurs automatiques
Pour chaque paire de personnages (et avec William) : affinité, confiance, tension, familiarité en heures passées ensemble (copain
au-delà de 50 h, ami au-delà de 90 h, proche au-delà de 200 h : Hall, 2018), dette de service ; décroissance sans contact.
Les chiffres ne décident jamais d'un acte ; ils rendraient AUTOMATIQUE le choix de modificateurs existants (ex. M72 si tension
≥ 40, M86 si affinité ≥ 50) au lieu d'un choix du moteur. Fichier prêt : `etat/relations.csv` (vide).

### P06 — Fronts qui avancent avec le temps
Les fronts installés n'avancent qu'après un acte ou une échéance manquée. Proposition : une table d'avance hebdomadaire pour les
fronts « temps » (0 segment 55 %, 1 segment 35 %, 2 segments 10 %).

### P07 — Fréquence du tour du monde selon la proximité (cercles)
Avec un vrai entourage (30 à 60 personnes), tirer T11 pour chacun chaque jour rendrait le tour du monde interminable. Proposition :
cercle 1 (5 proches) chaque jour ; cercle 2 (15) le lundi et le jeudi ; cercle 3 (50) le lundi ; figurants jamais.

## C. Biographie de William (seul l'utilisateur décide)
- **P08 — Réseau existant** : générer pour validation, lien par lien, les collègues du département de mathématiques et physique,
  la direction, les réguliers et l'entraîneur du club, les voisins mitoyens (familiarité calculée d'après les années partagées).
  Sinon : chacun apparaît au fil du jeu, tiré par `personnage.py`.
- **P09 — Questions ouvertes** : voiture ? chauffage ? soutien aux parents (montant, fréquence) ? club (où) ? crédit (taux, fin :
  110 000 € à 940 €/mois = 8 % jusqu'en 2059, ou fin vers 2052 à 3,5 %) ? répartition automatique du surplus ?
- **P10 — Paie calculée** : remplacer l'approximation « ≈ 9 300 € net » par un calcul (points × valeur du point projetée en 2040,
  retenues du régime des fonctionnaires, impôt en classe U), et chiffrer le 13e mois.

## D. Idées pour plus tard (immersion)
- **P11 — Application de rencontre** (profils tirés dans un rayon de 30 km, tables de réponse à valider) si William s'inscrit.
- **P12 — Placements vivants** : la valeur de l'ETF tirée chaque mois (rendement moyen et volatilité à fixer par l'utilisateur,
  krach rare).
- **P13 — Téléphone publié** à la fin de chaque journée simulée (page privée, même adresse), pour consulter messages, banque,
  agenda et météo depuis son propre téléphone.
- **P14 — Revue du lundi enrichie** : audit du casting (`personnage.py audit` : origines, âges, sexes contre la démographie
  réelle), rituels oubliés, faits périmés (`faits.py perimes`).

## E. Proposition du 12/10/2026 (à valider par l'utilisateur, règle 17)

### P15 — T20 : proposition d'argent contre un rapport, faite par William à une femme adulte (voyage à Manille) — **VALIDÉE le 12/10/2026** (« Je valide avec validation ! ») : installée dans `etat/modele-pouvoir.md` (T20a, T20b)
Contexte : l'utilisateur annonce (12/10/2026, hors fiction) que William part à Manille pour du tourisme sexuel avec des femmes
majeures. Le moteur le joue (§11) dans ses limites : scènes jusqu'au seuil puis ellipse (règle 10) ; JAMAIS de mineure, ni
d'âge ambigu (limite b : toute femme concernée est une adulte tirée par `personnage.py`) ; rien d'explicite ni de violence
sexuelle détaillée ; aucun mode d'emploi réel (lieux fictifs, ni adresses, ni prix, ni méthodes réelles). Faits : F055 à F057.
| Issue | Lieu où ce commerce se pratique | Ailleurs (rue, café, application) |
|---|---|---|
| accepte (prix annoncé ou fixé par un intermédiaire) | 50 | 8 |
| négocie (puis T12) | 15 | 12 |
| refuse ou ignore | 15 | 62 |
| refuse et alerte (entourage, sécurité, police : T4 ou T6) | 3 | 10 |
| arnaque (vol, chantage, faux tarif) | 10 | 6 |
| piège ou descente de police (T6) | 7 | 2 |

### P16 — T21 : réaction d'un profil de l'application de rencontre (à valider par l'utilisateur, 12/10/2026)
Profils tirés par `outils/rencontres.py` (femmes de 21 ans au moins, Manille) ; leur INTENTION réelle (serieux, aventure, amitie,
aide_financiere, travail_sexuel, arnaque) est tirée à la création et cachée. Toujours `jet.py --pour "Nom"` (adulte inscrite, datée).
**T21a — réaction à un « j'aime » de William**
| Issue | % | En scène |
|---|---|---|
| aucune_reponse | 40 | Rien : le profil ne le voit pas, ou passe. |
| match | 35 | Elle l'aime aussi : la discussion s'ouvre (`rencontres.py match`). |
| match_et_message | 12 | Elle l'aime aussi et écrit la première (heure en T10). |
| vu_sans_suite | 10 | Elle a vu son profil, ne donne pas suite. |
| bloque | 3 | Elle le bloque ou le signale (photo, âge, étranger, rien de précis). |
**T21b — réponse à un message de William après un match**
| Issue | % | En scène |
|---|---|---|
| repond | 50 | Elle répond (heure en T10) ; le ton suit sa fiche et son intention. |
| repond_tard | 20 | Elle répond un ou deux jours plus tard. |
| ignore | 22 | Pas de réponse. |
| bloque | 8 | Elle le bloque (message déplacé, insistance, rien de précis). |
Modificateurs proposés : intention « aide_financiere », « travail_sexuel » ou « arnaque » : match +15, match_et_message +8,
aucune_reponse −23 (T21a) ; repond +15, ignore −15 (T21b) ; message à caractère sexuel ou proposition d'argent d'emblée (hors
intention travail_sexuel) : bloque +15, ignore +10, repond −25 ; profil de William remarqué (1,96 m, sportif, Européen) : match +5,
aucune_reponse −5.

## F. Autres idées pour la revue n° 1 (12/10/2026)
- **P17 — Placements vivants** : valeur des ETF tirée chaque fin de mois (rendement moyen et volatilité à fixer), pour que le
  patrimoine bouge comme dans la vie (krach rare compris).
- **P18 — Dépenses de la vie courante** : un forfait journalier (courses, carburant, sorties) débité automatiquement quand le récit
  ne mentionne pas d'achat, pour que le compte courant reste vraisemblable sur les longues avances rapides.
- **P19 — Arrivée à Manille** : carte SIM locale (forfait prépayé), change d'euros en pesos (taux et commission), taxis par
  application, embouteillages, coupures de courant et inondations par fortes pluies, typhons tirés pendant la saison (signal de
  tempête qui fige la ville).
- **P20 — Vieillissement et mortalité** des personnages (tables de l'INSEE, du STATEC et de la PSA) pour les longues avances.
- **P21 — Trajets** : application Transports (Luxembourg gratuit, bus RegioZone, embouteillages tirés aux heures de pointe).

## G. Décisions de la revue du lundi n° 1 (12/10/2026, date réelle ; lundi 16/07/2040, date simulée)
L'utilisateur : « Je valide absolument tout ! ». Tout ce qui précède est VALIDÉ (P01 à P21, T12 à T14, la pondération du message
spontané d'un proche, les précisions facultatives C2 et les idées I1 à I4 de la revue). État de l'application :
- **En vigueur le jour même** : P01 (T15 à T18) et P04 (T19) et P16 (T21a, T21b) dans `etat/modele-pouvoir.md` ; T12 à T14
  confirmées ; P02 (pack d'aléas de l'univers 2, A19 à A30) et I4 (A31 diarrhée du voyageur, A32 dengue) dans `etat/aleas.md`,
  tirés pour la semaine du 16/07 ; P03 (météo +1,5 °C, effets sans A05) ; P06 (T22, avance hebdomadaire d'un front « temps ») ;
  pondération du message spontané (`rituels.py message-proche`) ; P11 et P13 (déjà en place) ; C2 : virements de 2 × 2 850 € gardés,
  maison d'environ 75 m², les parents n'écrivent pas.
- **À appliquer par le moteur avant que cela compte** (fils ouverts, B) : P21 application Transports (trajet vers Findel, avant le
  18/07) ; P19 arrivée à Manille, I1 frais à l'étranger, I2 caution d'hôtel, I3 décalage horaire (avant le 19/07) ; P18 dépenses
  courantes forfaitaires (dès que possible) ; P10 paie calculée et P17 ETF vivants (avant le 31/07) ; P05 relations chiffrées, P07 tour
  du monde par cercles (dès le premier personnage récurrent) ; P14 revue enrichie (revue n° 2, 23/07) ; P20 vieillissement (avances
  rapides longues).
- **Reste ouvert** : modèle de la voiture (aucune proposition faite : sans effet tant qu'elle ne tombe pas en panne).
