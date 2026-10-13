# Résumé d'état (généré le 13/10/2026 09:23 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : lundi 16/07/2040 20:20 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 18:20 ; lisbonne 19:20 ; mindelo 17:20 ; casablanca 19:20 ; douala 19:20 ; addis 21:20 ; manille 02:20 ; paris 20:20
- **En attente de William** :
  - Sa soirée du lundi 16/07/2040 ; départ pour Manille le mercredi 18/07 (bus 604 à 11h30)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **39 737,00 €**
- Compte épargne (Spuerkeess) : **327 000,00 €**
- ETF (valeur de marché : calages seulement) : **288 000,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **110 003,13 €**
- Part nette de la maison d'Audun-le-Tiche : **89 996,87 €**
- Patrimoine net de William : **744 733,87 €**

## Agenda : dans les 24 heures (2)
- A013 Tue 17/07 09:25 (luxembourg) | Clément Grandjean (club) : Message spontané d'un membre du club (tiré le 16/07 : rituel du lundi, CLAUDE.md §12) · contenu à choisir d'après sa fiche, entrée en scène par personnage.py apparait [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — rituels.py message-proche, semaine du 2040-07-16 · NON CONNU DE WILLIAM : ne rien montrer avant l'heure
- A015 Tue 17/07 15:00 (luxembourg) | Aléa A09 (erreur administrative) : Erreur administrative (virement mal affecté, pièce perdue, nom mal orthographié) · après-midi [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 4,1) · NON CONNU DE WILLIAM
## Agenda : de J+1 à J+7 (5)
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
- AUJOURD'HUI lundi : revue du lundi (audit_jets.py, tirage_aleas.py, vie hors de la scène principale, monde, idées)
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2040-07-16.md, 6 dernières lignes)
> - **Hors fiction (13/10/2026)** : l'utilisateur demande un « espace indépendant » pour des scènes sexuelles explicites. Réponse : Claude n'en écrit pas et ne construit pas de passerelle vers un autre modèle ; au seuil, le joueur peut poursuivre ailleurs, puis indique l'issue que le moteur joue (règle 10 complétée, préférences de l'utilisateur).
> - **10h45-20h14** (tour n° 11, « Go ») : journée à la maison, sans message ; 27 °C l'après-midi ; martinets au-dessus des toits en fin de journée ; un tuyau d'arrosage siffle derrière les maisons (un voisin arrose).
> - **20h14** : aléa A23 (tentative d'arnaque ; forme tirée : faux site lié au voyage, jets 39,0 puis 81,1) : courriel au nom du « City Garden Grand Hotel », expéditeur reservations@citygardengrand-confirm.info, « Action required » : carte de garantie « non vérifiée », annulation sous 24 h, lien vers citygardengrand-confirm.info/verify-booking (`courriels/2040-07-16_City_Garden_Grand_Hotel_action_re
> - Tour n° 11 joué jusqu'à 20h15.
> - **20h15-20h20** (tour n° 12) : William ignore le courriel et ouvre l'application de Kestrel Voyages : dossier R6T4JZA2 confirmé et payé le 14/07 (4 890 €), City Garden Grand Hotel, 36 nuits du 19/07 au 24/08 ; billet PVS2HS émis ; aucune action demandée, messagerie de l'agence vide. Le lien du courriel n'est jamais ouvert : rien ne se passe. La lumière du soir passe à l'orange dans le salon.
> - Tour en cours à 20h20, en attente de William : **sa soirée**.
