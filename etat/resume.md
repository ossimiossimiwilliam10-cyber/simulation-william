# Résumé d'état (généré le 12/10/2026 18:08 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : samedi 14/07/2040 10:46 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 08:46 ; lisbonne 09:46 ; mindelo 07:46 ; casablanca 09:46 ; douala 09:46 ; addis 11:46 ; manille 16:46 ; paris 10:46
- **En attente de William** :
  - Sa journée du samedi 14/07/2040 (premier jour des vacances d'été ; Fête nationale française)
  - Départ pour Manille le mercredi 18/07 à 15h40 (forfait réservé : R003-R004) ; eTravel dès le lundi 16/07 10h30

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **39 800,00 €**
- Compte épargne (Spuerkeess) : **327 000,00 €**
- ETF (valeur de marché : calages seulement) : **288 000,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **110 003,13 €**
- Part nette de la maison d'Audun-le-Tiche : **89 996,87 €**
- Patrimoine net de William : **744 796,87 €**
- Prévu dans les 14 jours : 16/07 Box internet fibre et forfait mobile (-63,00 €)

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (4)
- A001 Mon 16/07 08:00 (luxembourg) | Moteur et utilisateur : Revue du lundi n° 1 de l'univers 2 (hors fiction, avant le premier tour du jour) ; validation des pourcentages de T12 à T14 et adaptation du pack d'aléas [prevu]  — CLAUDE.md §12 | reporté de 2040-07-23 08:00 : départ de l'univers 2 redaté au samedi 14/07/2040 (demande de l'utilisateur du 11/10/2026) : premier lundi le 16/07
- A010 Mon 16/07 10:30 (luxembourg) | Philippines (eTravel) : eTravel : inscription en ligne gratuite possible à partir de maintenant, 72 heures avant l'arrivée à Manille (jeudi 19/07 à 16h30, heure locale) · code QR à montrer à l'immigration [prevu]  — F051 · arrivée du vol PVS2HS (R004) · 16h30 à Manille = 10h30 au Luxembourg
- A008 Wed 18/07 15:40 (luxembourg) | Lufthansa + Qatar Airways : Vol aller Luxembourg → Manille (LH 391…QR 932) · départ 15:40 de Luxembourg-Findel, arrivée le 19/07 à 16:30 (heure locale) · réservation PVS2HS [prevu]  — réservation R004 (etat/reservations.csv)
- A007 Thu 19/07 08:00 (luxembourg) | City Garden Grand Hotel : Arrivée à l'hôtel City Garden Grand Hotel (Manille), 36 nuit(s) · réservation R6T4JZA2 [prevu]  — réservation R003 (etat/reservations.csv)
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)

## Fêtes et fériés dans les 30 jours
- sam 14/07 FR Fête nationale

## Routine du tour
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2040-07-14.md, 6 dernières lignes)
> - **Hors fiction (12/10/2026, date réelle)** : reprise par une nouvelle session (Claude Opus 5.5) ; audit d'entrée (U2-19) ; téléphone de William republié à une nouvelle adresse (l'ancienne n'existait plus) ; la situation de 10h20 est remontrée deux fois au joueur, sans avance de l'horloge. Puis, à la demande du joueur : âge minimum des rencontres à Manille ramené de 21 à 18 ans, la majorité (U2-2
> - **10h20-10h35** (tour n° 5) : depuis le téléphone, William vire 30 000 € du compte épargne vers le compte courant (10h25, exécuté aussitôt : friction tirée à 30 %, jet 91,8 → non ; courant 39 800 €, épargne 327 000 €). Puis il ouvre le forfait de l'application Voyages chez Kestrel Voyages : Lufthansa + Qatar Airways au départ de Findel le mercredi 18/07 à 15h40 (arrivée à Manille le jeudi 19/07 
> - Tour n° 5 joué jusqu'à 10h35.
> - **Hors fiction (12/10/2026)** : le message du joueur est arrivé deux fois, traité comme une seule réservation ; outil `cartes.py` créé (plafonds des cartes, relevé différé de la carte de crédit, F063) et branché sur l'application Voyages (choix de la carte) et la Banque (onglet Cartes).
> - **10h35-10h46** (tour n° 6) : William revient à l'application Voyages et choisit un autre forfait, toujours Lufthansa + Qatar Airways, mais avec le City Garden Grand Hotel (Makati) et un retour le vendredi 24/08 : 4 890 € (prix de `voyages.py`, identique à la page). Paiement avec la Visa Premier à 10h44, confirmé dans l'application de la banque : autorisé (friction tirée à 30 %, jet 44,1 → non ;
> - Tour en cours à 10h46, en attente de William : **sa journée** (départ pour Manille le mercredi 18/07 à 15h40).
