# Résumé d'état (généré le 13/10/2026 09:11 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : lundi 16/07/2040 10:45 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 08:45 ; lisbonne 09:45 ; mindelo 07:45 ; casablanca 09:45 ; douala 09:45 ; addis 11:45 ; manille 16:45 ; paris 10:45
- **En attente de William** :
  - Sa journée du lundi 16/07/2040 : départ pour Manille le mercredi 18/07 (bus 604 à 11h30 de la mairie, vol LH 391 à 15h40) ; eTravel fait

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **39 737,00 €**
- Compte épargne (Spuerkeess) : **327 000,00 €**
- ETF (valeur de marché : calages seulement) : **288 000,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **110 003,13 €**
- Part nette de la maison d'Audun-le-Tiche : **89 996,87 €**
- Patrimoine net de William : **744 733,87 €**

## Agenda : dans les 24 heures (2)
- A014 Mon 16/07 20:00 (luxembourg) | Aléa A23 (tentative d'arnaque) : Tentative d'arnaque (SMS de faux colis, faux conseiller bancaire ou faux site) · soir [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 2,3) · NON CONNU DE WILLIAM
- A013 Tue 17/07 09:25 (luxembourg) | Clément Grandjean (club) : Message spontané d'un membre du club (tiré le 16/07 : rituel du lundi, CLAUDE.md §12) · contenu à choisir d'après sa fiche, entrée en scène par personnage.py apparait [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — rituels.py message-proche, semaine du 2040-07-16 · NON CONNU DE WILLIAM : ne rien montrer avant l'heure
## Agenda : de J+1 à J+7 (6)
- A015 Tue 17/07 15:00 (luxembourg) | Aléa A09 (erreur administrative) : Erreur administrative (virement mal affecté, pièce perdue, nom mal orthographié) · après-midi [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 4,1) · NON CONNU DE WILLIAM
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
> - **Hors fiction (13/10/2026)** : application Transports créée (`outils/transports.py`, proposition P21 validée) : itinéraires en bus, train et tram entre Audun, Esch, Luxembourg et l'aéroport ; faits F065 et F066 ; prix PX051 (billet RegioZone de 2 h : 4,05 € en 2040).
> - **07h40-07h50** (tour n° 9) : William décide d'aller à l'aéroport en transports en commun le mercredi 18/07 et de laisser sa voiture à Audun. Dans l'application Transports, pour le mercredi (vacances scolaires : bus toutes les 30 min) : trois itinéraires de 1 h 25 à 1 h 30 (bus 604 direct jusqu'à Hamilius puis tram ; bus jusqu'à Esch, train, puis tram ou bus 29) ; billet RegioZone de 2 h pour la
> - Tour n° 9 joué jusqu'à 07h50.
> - **07h50** (tour n° 10, « Go ») : William garde dans l'application Transports le trajet du mercredi 18/07 : bus 604 direct à 11h30 de la mairie, Hamilius à 12h25, tram à 12h33, aéroport à 12h55 ; billet RegioZone de 2 h (4,05 €) à acheter avant de monter (agenda A018). Avance rapide jusqu'au rappel de 10h30 : matinée à la maison, sans message. Traces : le sac de sport près de l'entrée sent les ga
> - **10h30-10h45** : le rappel sonne ; William remplit l'eTravel sur le portail officiel (friction tirée à 30 %, jet 37,8 → non) : identité, passeport, vol QR 932 du 19/07, City Garden Grand Hotel à Makati, vacances, déclarations de santé et de douane ; envoyé à 10h42 ; code QR affiché et reçu par courriel (ETR-0080546756, `courriels/2040-07-16_Confirmation_eTravel_Philippines.pdf`). Agenda A010 et
> - Tour en cours à 10h45, en attente de William : **sa journée** (départ le mercredi 18/07 à 11h30 de la mairie).
