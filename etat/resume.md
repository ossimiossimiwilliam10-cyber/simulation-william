# Résumé d'état (généré le 13/10/2026 09:30 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : mardi 17/07/2040 09:00 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 07:00 ; lisbonne 08:00 ; mindelo 06:00 ; casablanca 08:00 ; douala 08:00 ; addis 10:00 ; manille 15:00 ; paris 09:00
- **En attente de William** :
  - Sa journée du mardi 17/07/2040 (veille du départ pour Manille ; inscrit sur l'application de rencontre)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **39 712,01 €**
- Compte épargne (Spuerkeess) : **327 000,00 €**
- ETF (valeur de marché : calages seulement) : **288 000,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **110 003,13 €**
- Part nette de la maison d'Audun-le-Tiche : **89 996,87 €**
- Patrimoine net de William : **744 708,88 €**

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
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2040-07-17.md, 6 dernières lignes)
> # Mardi 17 juillet 2040 — univers 2, quatrième jour (veille du départ pour Manille)
> - **Nuit du 16 au 17/07** : coucher à 23h20, réveil à 8h45, sans réveil (heures tirées au dé).
> - **08h45** : réveil ; grand soleil, 27 °C annoncés ; aucun message. Fin de l'avance rapide (tour n° 13).
> - **08h45-09h00** (tour n° 14) : William s'inscrit sur l'application de rencontre : abonnement Plus avec le mode voyage sur Manille (24,99 € par mois, premier mois payé sur la Visa Debit à 08h58, opération K003 ; renouvellement le 17 de chaque mois, échéancier E016) ; présentation : « Just a kind man looking for love. let's meet in real life for better presentation. » ; recherche : femmes de 18 à 
> - Tour en cours à 09h00, en attente de William : **sa journée** (veille du départ).
