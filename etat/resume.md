# Résumé d'état (généré le 13/10/2026 10:00 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : mardi 17/07/2040 09:22 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 07:22 ; lisbonne 08:22 ; mindelo 06:22 ; casablanca 08:22 ; douala 08:22 ; addis 10:22 ; manille 15:22 ; paris 09:22
- **En attente de William** :
  - Premier message de Julia sur l'application de rencontre (09h22) : « Is it your first time here? »
  - Sa journée du mardi 17/07/2040 (veille du départ pour Manille)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **39 712,01 €**
- Compte épargne (Spuerkeess) : **327 000,00 €**
- ETF (valeur de marché : calages seulement) : **288 000,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **110 003,13 €**
- Part nette de la maison d'Audun-le-Tiche : **89 996,87 €**
- Patrimoine net de William : **744 708,88 €**

## Agenda : dans les 24 heures (4)
- A013 Tue 17/07 09:25 (luxembourg) | Clément Grandjean (club) : Message spontané d'un membre du club (tiré le 16/07 : rituel du lundi, CLAUDE.md §12) · contenu à choisir d'après sa fiche, entrée en scène par personnage.py apparait [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — rituels.py message-proche, semaine du 2040-07-16 · NON CONNU DE WILLIAM : ne rien montrer avant l'heure
- A020 Tue 17/07 12:50 (luxembourg) | Hannah De Leon (application de rencontre) : Match en retour de Hannah (T21a : match, jet 59,9 · T10 : dans la journée, jet 82,3) · rencontres.py match [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · intention cachée : arnaque
- A015 Tue 17/07 15:00 (luxembourg) | Aléa A09 (erreur administrative) : Erreur administrative (virement mal affecté, pièce perdue, nom mal orthographié) · après-midi [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 4,1) · NON CONNU DE WILLIAM
- A021 Tue 17/07 17:40 (luxembourg) | Shane Lopez (application de rencontre) : Match en retour puis premier message de Shane (T21a : match_et_message, jet 85,7 · T10 : le soir ou le lendemain, jet 81,6 ; 23h40 à Manille, après son service) · rencontres.py match puis message --auteur profil [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure
## Agenda : de J+1 à J+7 (6)
- A022 Wed 18/07 11:12 (luxembourg) | Kiara Reyes (application de rencontre) : Répond enfin au message de William du 17/07 à 09h17 : « Hi William! Sorry for the late reply, I was on shift and so tired 😅 I'm good, thanks! How about you? Where are you from? » (T21b : repond_tard, jet 72,6, M46 · jour : lendemain, jet 30,7 · heure : 13h00 + 83,9 × 3 min) · rencontres.py message kiara-reyes --auteur profil [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · 11h12 au Luxembourg
- A018 Wed 18/07 11:30 (luxembourg) | William (trajet prévu) : Trajet vers l'aéroport : bus 604 direct 11h30 Audun-le-Tiche, Mairie → 12h25 Luxembourg, Hamilius · tram ligne 1 12h33 → 12h55 Findel, Luxembourg Airport · billet RegioZone de 2 h (4,05 €) à acheter avant de monter (application CFL go ou automate) [prevu]  — itinéraire choisi par William le 16/07 dans l'application Transports (transports.py options --de AUD --vers FDL --quand '2040-07-18 11:30')
- A008 Wed 18/07 15:40 (luxembourg) | Lufthansa + Qatar Airways : Vol aller Luxembourg → Manille (LH 391…QR 932) · départ 15:40 de Luxembourg-Findel, arrivée le 19/07 à 16:30 (heure locale) · réservation PVS2HS [prevu]  — réservation R004 (etat/reservations.csv)
- A007 Thu 19/07 08:00 (luxembourg) | City Garden Grand Hotel : Arrivée à l'hôtel City Garden Grand Hotel (Manille), 36 nuit(s) · réservation R6T4JZA2 [prevu]  — réservation R003 (etat/reservations.csv)
- A016 Fri 20/07 03:00 (luxembourg) | Aléa A07 (panne réseau) : Panne réseau (Wi-Fi de l'hôtel, données mobiles) ou banque en ligne indisponible · matin, à Manille [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 4,3) · NON CONNU DE WILLIAM
- A017 Sun 22/07 03:00 (luxembourg) | Aléa A22 (courrier administratif) : Courrier administratif (impôts, CNS, mairie, banque) : par courriel, William étant à Manille (pas de distribution du courrier le dimanche) · matin [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 6,3) · NON CONNU DE WILLIAM
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)

## Fêtes et fériés dans les 30 jours
- mer 15/08 FR Assomption
- mer 15/08 LU Assomption

## Routine du tour
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2040-07-17.md, 6 dernières lignes)
> - **Hors fiction (13/10/2026)** : l'abonnement Plus est noté par le joueur (ne plus le rappeler) ; la file copiée depuis le téléphone contenait encore l'inscription de 08h58 : non refaite (garde ajoutée à `rencontres.py`).
> - **09h00-09h16** (tour n° 15) : William fait défiler les 25 profils : « j'aime » à Yuna, Zia, Julia, Angel, Shane, Hannah, Chloe, Samantha, Kiara et Danica ; il passe les quinze autres. Réactions tirées en T21a (M48 pour tous ; M45 pour Zia, Hannah, Chloe et Kiara, d'après leur intention cachée) : aucune réponse pour Yuna, Angel, Samantha et Danica ; vus sans suite pour Zia et Chloe ; match pour 
> - Tour en cours à 09h16, en attente de William : **le match avec Kiara** et **sa journée**.
> - **Hors fiction (13/10/2026)** : reprise de la session (Claude Opus 5.5, entrée du relais sans alerte) ; le joueur demande que la page du téléphone apparaisse dans la conversation : régénérée par `tour.py fin` *(avant : « et republiée à la même adresse » → maintenant :)* ; l'ancienne adresse (https://claude.ai/artifact/9j5a5bgQy9De1sxL7LZ27z) est introuvable et la galerie d'artefacts du compte es
> - **09h16-09h22** (tour n° 16) : à 09h17, William écrit à Kiara : « Hi Kiara, how are you? » (dicté en français, « Salut Kiara, comment ça va ? » ; envoyé en anglais, langue de sa présentation dans l'application et de Kiara). Réponse tirée en T21b (M46 : intention cachée aide_financiere) : réponse tardive (jet 72,6), le lendemain (jet 30,7), à 17h12 à Manille, 11h12 au Luxembourg (agenda A022, non
> - Tour en cours à 09h22, en attente de William : **le message de Julia** et **sa journée**.
