> Note de relais GÉNÉRÉE par `python outils/relais.py sortie` (ou `tour.py fin`) : ne pas éditer à la main. Les notes libres vont dans `etat/relais-notes.md`.

# Relais de la simulation — briefing généré le 13/10/2026 15:48 (heure machine) pour Claude Opus 5.5

## Alertes
- aucune

## Où en est la partie
- Horloge : jeudi 19 juillet 2040, 23h25 (manille) ; tour n° 27
- Lieu de William : Manille, aéroport Ninoy-Aquino (NAIA), terminal 3, hall des arrivées
- En attente de William : Message de Julia (envoyé à 17h25, reçu à l'atterrissage) : « When do you arrive? »
- En attente de William : Trajet jusqu'au City Garden Grand Hotel (Makati), arrivée prévue le 19/07 à partir de 14h (A007)

## Dernier tour montré au joueur (etat/dernier-tour.md)
# Dernier tour montré au joueur

> Tour n° 27 ; horloge 18/07/2040 13:08 -> 19/07/2040 23:25 ; enregistré le 13/10/2026 15:47 (heure machine) par tour.py fin. Ce fichier est remplacé à chaque tour ; l'historique complet est dans journal/tours/.

## Message du joueur

> Je passe en mode auto jusqu'à mon arrivé à Manille (dépense max autorisé : 500 euros) GO !

## Texte envoyé au joueur

**JEUDI 19 JUILLET 2040 — 23h25 (heure de Manille) — Aéroport Ninoy-Aquino, terminal 3, hall des arrivées**

Le contrôle de sûreté de Findel passe vite. Tu déjeunes au restaurant panoramique, face aux pistes : un plat du jour et une grande eau, 31,40 € sur la Visa Debit. Le LH 391 part à l'heure et se pose à Francfort à 16h28.

Qatar Airways n'est pas au terminal 1 : il faut prendre le SkyLine, le petit train sans conducteur, jusqu'au nouveau terminal 3. Au comptoir, l'agente regarde ton billet, puis son écran. « Your flight to Doha is delayed, sir. Air traffic control restrictions. New departure at 19:15. You won't make your connection to Manila… I've moved you to tomorrow morning's flight: Doha 07:55, Manila 22:20. Your bag will follow you. » Elle imprime les deux cartes d'embarquement. Le contrôle des passeports et la sûreté te prennent vingt-sept minutes de file. Le QR 68 décolle à 19h13.

Dîner à bord, puis une heure et demie d'un sommeil haché. À Doha, il est 2h15 : le vol de Manille de 2h20 est parti sans toi. Au comptoir de transfert, on te remet un bon de repas. Tu manges dans une aérogare presque vide, puis tu dors un peu plus de deux heures dans une salle de repos, entre des voyageurs allongés sous des couvertures grises. À 7h55, le QR 928 décolle pour Manille : neuf heures et demie de vol, deux repas, un film, une heure vingt de sommeil.

L'avion se pose à 22h20. Dans la passerelle, l'air est lourd, presque aussi chaud qu'en plein jour : il fait encore 32 °C. À un guichet, on scanne ton code eTravel ; la file de l'immigration avance lentement. Trente et une minutes après la passerelle, l'agent feuillette ton passeport, regarde son écran et tamponne sans un mot : 19 juillet. Ton sac sort sur le tapis, l'étiquette « MNL » encore sur la poignée. Pendant que tu attends, ton téléphone accroche le Wi-Fi gratuit de l'aéroport, une adresse électronique suffit, et les messages arrivent. Julia, à 17h25 : « Hi William! So sorry for the very late reply 🙏 Crazy week, night shift every day 😩 Haha a guide? I'm not a pro but I know Manila well, almost 10 years here. Coffee first, as friends, then we see 😊 When do you arrive? Tip: use Grab only, not the taxis outside the malls, and don't drink the tap water ha »

À 23h25, les portes coulissantes s'ouvrent sur le hall des arrivées : des familles massées derrière une barrière, des chauffeurs avec des pancartes, des comptoirs de cartes SIM et de change, une file devant le guichet des taxis. Le trajet t'a coûté 31,40 €.

**Réponses attendues**
- **Julia** (application de rencontre, message de 17h25) : elle s'excuse du retard et propose « un café d'abord, en amis ». Elle te demande quand tu arrives, te conseille Grab plutôt que les taxis et de ne pas boire l'eau du robinet.

**À faire / à fournir avant le tour suivant**
- Rejoindre le City Garden Grand Hotel, à Makati : réservation au nom de William, 36 nuits, arrivée prévue à partir de 14h le 19/07.

**Quêtes secondaires**
- Rien de nouveau.

Que veux-tu faire ?

## Échéances : retards et prochaines 24 h (les lignes NON CONNU sont pour le moteur seul)
- A026 Thu 19/07 23:45 (manille) | Shane Lopez (application de rencontre) : Répond enfin au message de William du 17/07 à 17h41 : « Hi William! Sorry for the late reply, work + traffic here are killing me 😅 So you're already here? Welcome to Manila 🙂 How was the flight? » (T21b : repond_tard, jet 56,7, sans modificateur · jour : surlendemain, jet 91,5 · heure fixée selon sa vie : après son service, comme le 17/07) · rencontres.py message shane-lopez --auteur profil [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · 17h45 au Luxembourg · William sera à Manille depuis 16h30 · texte à ajuster si William lui écrit de nouveau d'ici là
- A007 Fri 20/07 00:30 (manille) | City Garden Grand Hotel : Arrivée à l'hôtel City Garden Grand Hotel (Manille), 36 nuit(s) · réservation R6T4JZA2 [prevu]  — réservation R003 (etat/reservations.csv) | reporté de 2040-07-19 14:00 : correspondance manquée à Doha : arrivée à l'aéroport de Manille à 22h20 au lieu de 16h30 · heure d'arrivée à l'hôtel selon le trajet choisi par William
- A016 Fri 20/07 09:00 (manille) | Aléa A07 (panne réseau) : Panne réseau (Wi-Fi de l'hôtel, données mobiles) ou banque en ligne indisponible · matin, à Manille [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 4,3) · NON CONNU DE WILLIAM
- A027 Fri 20/07 14:46 (manille) | Kiara Reyes (application de rencontre) : Répond au message de William du 18/07 à 11h54 : « Hi William! Sorry, I was so busy 😩 I have a boy, he's 3 🥰 Saturday is ok! City Garden in Makati, I know it. What time? Maybe 3pm? Then we can go to Poblacion, lots of good food there 😋 » (T21b : repond_tard, jet 66,7, M46 · jour : surlendemain, jet 69,1 · heure : 13h00 + 35,3 × 3 min · enfant : un garçon (jet 88,9) de 3 ans (jet 41,9)) · rencontres.py message kiara-reyes --auteur profil [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · 08h46 au Luxembourg · William sera à Manille · texte à ajuster si William lui écrit de nouveau d'ici là

## Rituels du moteur dus (rituels.py)
- rien

## Décisions en attente de William (etat/fils-ouverts.md, A)
| 1 | **Sa journée du mercredi 18/07/2040** (départ pour Manille) | Jour du départ (avant : « Sa journée du mardi 17/07/2040 », veille du départ ; plus tôt : « Sa journée du lundi 16/07/2040 ») ; eTravel fait le 16/07 à 10h42 ; départ pour Manille le mercredi 18/07 à 15h40, en transports en commun (décidé à 07h45) *(avant : « Sa journée du samedi 14/07/2040 » → maintenant : lundi 16/07, après l'avance rapide du tour n° 8)* | — |
| 2 | **Voyage à Manille** (ouvert le 14/07/2040) | **PARTI le 18/07** : maison fermée vers 11h18, billet RegioZone acheté à 11h25 (4,05 €, Visa Debit), bus 604 direct à 11h30, à l'heure *(avant : départ prévu → maintenant : en route)* ; Hamilius 12h25, tram de 12h33, Findel à 12h55 ; **enregistrement (12h58)** : tarif Economy Classic, 25 kg en soute (F069), sac de 17,4 kg ; l'agent relève le retour du 24/08 (36 jours, au-delà des 30 jours sans visa) et demande s'il a un visa ou une prolongation prévue *(avant : réponse de William attendue → maintenant : « je prolongerai sur place, au Bureau de l'immigration » ; vérification tirée : **décharge à signer** (entrée possiblement refusée, retour et frais à sa charge) ; l'agent conseille un billet bon marché pour Hong Kong ou Bangkok ; signature de William attendue → maintenant : **déclaration signée à 13h05** ; sac enregistré jusqu'à Manille ; carte du LH 391 seule, cartes de Qatar Airways à retirer au comptoir de transfert de Francfort, A028 ; embarquement à 15h10)* ; **voyage fait (mode automatique, 31,40 € dépensés)** : LH 391 à l'heure ; QR 68 retardé de 78 min (contrôle aérien) ; correspondance de Doha manquée, réacheminé sur le QR 928 ; **arrivé à Manille le 19/07 à 22h20** (5 h 50 de retard) ; tampon d'entrée du 19/07, fin des 30 jours le 18/08 (A011) ; sac arrivé ; **pour le moteur** : indemnisation de 600 € possible au titre du règlement CE 261/2004 (F074) si William la réclame à Qatar Airways, refus probable (cause tirée : contrôle aérien, circonstance extraordinaire) ; **RÉSERVÉ le 14/07 à 10h44** (R003 et R004, Kestrel Voyages, 4 890 € sur la Visa Premier, débités au relevé du 07/08) : vol Lufthansa + Qatar Airways PVS2HS, aller mer. 18/07 15h40 de Findel (LH 391, QR 68, QR 932) → Manille jeu. 19/07 16h30 ; retour ven. 24/08 18h30 (QR 933, QR 69, LH 390) → Luxembourg sam. 25/08 10h05 ; City Garden Grand Hotel (Makati), 36 nuits du 19/07 au 24/08 (R6T4JZA2) ; confirmations PDF dans `courriels/` ; agenda A007 à A011. Restent : ~~eTravel~~ **fait le 16/07 à 10h42** (ETR-0080546756, code QR dans `courriels/` ; tentative du 14/07 à 11h20 refusée : trop tôt, F064), prolongation de séjour avant la fin des 30 jours sans visa (vers le 17/08), trajet vers Findel le 18/07 : **en transports en commun, la voiture reste à Audun** (décision du 16/07 à 07h45 ; trajet choisi : bus 604 direct à 11h30 de la mairie, tram à 12h33 depuis Hamilius, aéroport à 12h55 ; billet RegioZone de 4,05 € à acheter avant de monter ; agenda A018) *(avant : « rien de prévu »)* ; Visa Premier : 110 € disponibles jusqu'au 30/07. Bagage : un seul sac de voyage, fait le 14/07 (poids non mesuré) ; **pour le moteur** : la franchise de bagages du tarif (vols.csv : « selon le tarif choisi ») est à établir par recherche avant l'enregistrement du 18/07. *(Avant : « Rien de réservé : paiement refusé » → maintenant : réservé, 14/07 10h44.)* ~~Rien de réservé : paiement refusé.~~ Le 14/07 à 10h33, William a tenté de payer le forfait Lufthansa + Qatar Airways (Findel mer. 18/07 15h40 → Manille jeu. 19/07 16h30 ; retour mer. 05/09 18h30 → Luxembourg jeu. 06/09 10h05) + 48 nuits au Makati Shangri-La (19/07 – 05/09) : 10 741 € chez Kestrel Voyages, avec sa Visa Premier : refusé, limite mensuelle de 5 000 € dépassée (Visa Debit : 2 500 €/mois) ; panier resté ouvert sur le site ; rien de débité (R002). 30 000 € virés de l'épargne vers le compte courant à 10h25. À décider par William : moyen de payer (hausse de limite dans S-Net, autre combinaison, autre agence…). Séjour de 48 jours : prolongation au Bureau de l'immigration au-delà de 30 jours ; eTravel dans les 72 h avant l'arrivée. *(Avant : « Rien de réservé. Dates envisagées : aller ven. 20/07, retour ven. 31/08 ; vol et hôtel à choisir » → maintenant : forfait choisi, paiement refusé, 14/07 10h33.)* *(Avant : « Voyage à Yaoundé » avec un vol réservé → maintenant : Manille, correction hors fiction U2-18 du 12/10/2026.)* ~~Ancienne ligne : **Vol réservé et payé le 14/07 à 10h04** (R001, CYNERS : aller ven. 20/07 18h30, retour ven. 31/08, 2 179 €). À faire : e-visa (réponse en 72 h ouvrées ou 24 h en express), certificat de fièvre jaune (biographie : question posée à l'utilisateur le 12/10/2026), hébergement à Yaoundé (rien de réservé), trajet vers Findel. *(Avant : « recherches faites, rien de réservé » → maintenant : vol réservé, 14/07 10h04.)*~~ | — |
| 3 | ~~**Courriel « City Garden Grand Hotel » (16/07, 20h14)**~~ **CLOS le 16/07 à 20h20** : William ignore le courriel et vérifie dans l'application de Kestrel Voyages : forfait confirmé et payé, aucune action demandée, aucun message de l'hôtel ; lien jamais ouvert | Demande de « vérifier » la carte de garantie sous 24 h via un lien (citygardengrand-confirm.info), faute de quoi la réservation serait annulée ; **pour le moteur** : hameçonnage (aléa A23), la réservation R003 est en réalité confirmée et payée ; si William saisit sa carte sur le lien, les fraudeurs la tentent (plafonds : Visa Premier 110 € disponibles, Visa Debit 2 500 €), puis friction et opposition à jouer | — |
| 4 | **Application de rencontre** (inscrit le 17/07 à 08h58) | Abonnement Plus, mode voyage sur Manille (24,99 €/mois, Visa Debit, E016) ; 17/07 à 09h05 : dix « j'aime », quinze profils passés ; **match avec Kiara Reyes à 09h16** *(avant : discussion ouverte, vide → maintenant : William lui écrit à 09h17 « Hi Kiara, how are you? » ; réponse tardive tirée : le 18/07 à 11h12, A022, non connue → maintenant : reçue le 18/07 à 11h12 : « … How about you? Where are you from? »)* ; William lui répond à 11h14 (Luxembourg, arrivée demain, veut la rencontrer, « Maybe it's destiny », « an excellent situation », « why not change our lives ») ; réponse de Kiara à 11h52 : elle veut le rencontrer, **mère célibataire**, travaille de nuit, **libre samedi**, demande où il loge ; William lui répond à 11h54 (garçon ou fille ?, d'accord pour samedi, son hôtel : City Garden Grand Hotel, Makati, rendez-vous à l'hôtel puis ville et repas) ; réponse tardive tirée : vendredi 20/07 vers 14h46 à Manille, A027, non connue ; **match avec Julia Dimaculangan à 09h22** et premier message de Julia (« Hi William! 😊 … Is it your first time here? ») *(avant : à venir, A019 → maintenant : joué)* ; William lui répond à 09h23 : « Yes it is my first time and I am looking for a guide too . Why not you haha » ; réponse tardive tirée : jeudi 19/07 à 17h25 à Manille (11h25 au Luxembourg ; William aura atterri), A023, non connue → maintenant : envoyée à 17h25, William en vol, reçue à l'atterrissage (« Coffee first, as friends… When do you arrive? ») ; **match avec Hannah De Leon à 12h50** *(avant : discussion ouverte, vide → maintenant : William lui écrit à 17h42 « Hi Hannah, how are you ? » ; réponse tirée à 18h27, A025, non connue → maintenant : reçue à 18h27 : « … how's your day? Are you already here in Manila? »)* *(avant : en discussion → maintenant : William lui écrit à 18h30 (arrivée jeudi, WhatsApp demandé, « I've totally fallen for your charm », première personne qu'il veut voir à Manille) ; **elle le bloque à 18h33**, discussion et profil disparus ; T21b : bloque)* *(avant : à venir, A020 → maintenant : joué)* ; **match avec Shane Lopez à 17h40** et premier message de Shane (« … When will you be in Manila? ») *(avant : à venir, A021 → maintenant : joué)* ; William lui répond à 17h41 : « I arrive in Manila on Thursday. » ; réponse tardive tirée : jeudi 19/07 vers 23h45 à Manille (17h45 au Luxembourg), A026, non connue ; sans suite : Yuna, Zia, Angel, Chloe, Samantha, Danica ; réactions à un « j'aime » ou à un message : T21a et T21b (validées), toujours `--pour` ; intentions cachées dans `etat/rencontres.csv` | — |
| 5 | ~~**WhatsApp de Clément Grandjean, du club** (17/07, 09h25)~~ **CLOS le 17/07 à 09h37** : William décline (« déjà en vacances », pas disponible, « je pars justement d'ici jeudi », destination non dite) ; Clément : « Pas de souci… On se refait un sparring à ton retour 👊 » | Partenaire de sparring : il a remarqué l'absence de William au sparring de samedi et au MMA de lundi (« t'es déjà en vacances ou quoi ? ») ; il demande un coup de main **jeudi 19/07 en fin d'après-midi** pour monter des plaques de placo à l'étage, contre bières et pizzas ; **pour le moteur** : jeudi, William sera dans l'avion puis à Manille (arrivée à 16h30, heure locale) ; Clément ignore le voyage (aucune ligne dans `etat/savoir.csv`) | jeudi 19/07 |

## Notes de passation (etat/relais-notes.md)
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
- ~~(12/10/2026 10:45, Claude Opus 5.5) **Téléphone de William republié à une NOUVELLE adresse** : https://claude.ai/artifact/9j5a5bgQy9De1sxL7LZ27z
  (l'ancienne, VJkYBmpJTrVarDVTs24MsS, affichait « Page not found » sur le téléphone du joueur et n'apparaissait plus dans la
  liste de ses artefacts : cause inconnue). Adresse aussi dans etat/relais-config.json. À chaque tour : `tour.py fin` régénère
  sorties/telephone/index.html ; Claude republie au même URL (paramètre url) après avoir relu la page en entier.~~
  Réglé le 13/10/2026 : cette adresse est introuvable ; nouvelle adresse dans la note du 13/10/2026, 09h59, ci-dessous.
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
  poursuivre ailleurs puis donne l'issue. Téléphone : ~~https://claude.ai/artifact/9j5a5bgQy9De1sxL7LZ27z~~ *(introuvable le 13/10/2026 → maintenant : https://claude.ai/artifact/P5BeHqT2s6n5aewPEWyK6P)* (seul Claude republie ;
  un autre agent envoie `sorties/telephone/index.html` si le joueur le demande).
- (13/10/2026 09:59, Claude Opus 5.5) **Téléphone de William publié à une NOUVELLE adresse** : https://claude.ai/artifact/P5BeHqT2s6n5aewPEWyK6P
  (l'ancienne, 9j5a5bgQy9De1sxL7LZ27z, est introuvable : lecture refusée « artifact not found », galerie d'artefacts du compte
  vide ; le joueur ne voyait plus le téléphone dans la conversation). Adresse aussi dans etat/relais-config.json. À chaque tour :
  `tour.py fin` régénère sorties/telephone/index.html ; Claude republie au même URL (paramètre url) après avoir relu la page
  en entier ; si l'adresse est de nouveau introuvable, publier à une nouvelle adresse et la consigner ici.

## Préférences de l'utilisateur (memoire/preferences-utilisateur.md : à lire en entier)
- Format du tour : récit fluide, puis « Réponses attendues », « À faire », « Quêtes secondaires », « Que veux-tu faire ? ».
- Aucune explication, aucun conseil, aucun jet ni source montrés ; pas de morale ; William décide seul (règles 6, 13, 16).
- « 📌 Vraie vie : … » = hors fiction ; il dicte : interpréter les erreurs de dictée et le signaler en une ligne.
- Il joue parfois depuis son téléphone : lui envoyer les fichiers demandés dans la conversation.

## Routine
- Lire le fichier maître (CLAUDE.md, GEMINI.md ou AGENTS.md), puis memoire/preferences-utilisateur.md et outils/LISEZMOI.md.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, rituels, météo, corps, relais).
- Fin de tour : `python outils/tour.py fin --jusqua "AAAA-MM-JJ HH:MM" --lieu "…" --attente "…" --texte <brouillon>`.
- Avant de passer la main : `python outils/relais.py sortie --note "…" --commit "…" --fusionner`.

## État git détaillé
- branche courante : claude/simulation-realistic-tools-d95e81 ; master : 6f2041b ; avance 0, retard 0
- worktree simulation-william : branche master ; 0 commit(s) absents de master ; 0 fichier(s) modifié(s)
- worktree continuation-9f6d32 : branche claude/simulation-realistic-agent-handoff-3deabc ; 0 commit(s) absents de master ; 0 fichier(s) modifié(s)
- worktree eloquent-mirzakhani-73acb9 : branche claude/eloquent-mirzakhani-73acb9 ; 0 commit(s) absents de master ; 0 fichier(s) modifié(s)
- worktree life-simulation-resume-892e7a (ICI) : branche claude/simulation-realistic-tools-d95e81 ; 0 commit(s) absents de master ; 27 fichier(s) modifié(s) ; ARCHIVÉ : univers 1 : branche de la session des outils (cf66dbb, déjà contenue dans master), conservée après la suppression du worktree (12/10/2026)

