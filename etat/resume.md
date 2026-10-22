# Résumé d'état (généré le 22/10/2026 22:37 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 21/07/2041 12:05 (luxembourg, UTC+2)
- **Lieu de William** : Aéroport Paris-Charles de Gaulle, terminal 2E, salle d'embarquement
- **Heure dans les autres lieux** : abidjan 10:05 ; lisbonne 11:05 ; mindelo 09:05 ; casablanca 11:05 ; douala 11:05 ; addis 13:05 ; manille 18:05 ; paris 12:05 ; seoul 19:05 ; bresil 07:05
- **En attente de William** :
  - Embarquement du KE902 à 12h35 (décollage 13h20)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **9 781,00 €**
- Compte épargne (Spuerkeess) : **75 250,00 €**
- ETF (valeur de marché : calages seulement) : **670 380,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **102 621,78 €**
- Part nette de la maison d'Audun-le-Tiche : **97 378,22 €**
- Patrimoine net de William : **852 789,22 €**
- Prévu dans les 14 jours : 31/07 Traitement mensuel de William (9 320,00 €) ; 01/08 Minett Combat Club (-85,00 €) ; 01/08 Package bancaire Zebra Premium (-12,83 €) ; 02/08 Virement permanent vers le compte épargne (-732,00 €) ; 02/08 Virement permanent vers le compte épargne (732,00 €) ; 02/08 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/08 Virement permanent vers le compte-titres ETF (5 755,00 €)

## Agenda : dans les 24 heures (4)
- A008 Sun 21/07 13:20 (luxembourg) | Korean Air (Premium Economy) : Vol aller Paris → Séoul (KE 902…KE 902) · départ 13:20 de Paris-Charles-de-Gaulle, arrivée le 22/07 à 07:50 (heure locale) · réservation XLGTS3 [prevu]  — réservation R001 (etat/reservations.csv)
- A011 Mon 22/07 00:50 (luxembourg) | William : Rappel du joueur : écrire à Hye-won dès l'arrivée à Séoul (atterrissage du KE902) [prevu]  — intention du joueur du 21/07/2041 : il rédige lui-même le message
- A007 Mon 22/07 04:00 (luxembourg) | William : Installation et prise de possession de l'officetel meublé à Yeonnam-dong (Mapo-gu) [prevu]  — réservé le 20/07 (2 450 € pour 6 semaines du 22/07 au 02/09)
- A001 Mon 22/07 08:00 (luxembourg) | Moteur et utilisateur : Revue du lundi n° 1 de l'univers 3 (hors fiction, avant le premier tour du jour) ; adaptation des aléas et propositions [prevu]  — CLAUDE.md §12 | premier lundi de l'Univers 3 le 22/07/2041
## Agenda : de J+1 à J+7 (1)
- A006 Tue 23/07 07:00 (luxembourg) | Min-ji & William : Sortie barbecue coréen à Seongsu-dong (découverte du quartier et spécialités) [prevu]  — rendez-vous convenu le 19/07
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)

## Fêtes et fériés dans les 30 jours
- jeu 15/08/2041 FR Assomption
- jeu 15/08/2041 LU Assomption

## Routine du tour
- lendemain = lundi : revue du lundi à présenter AVANT le reste (CLAUDE.md §12) ; dimanche soir : T4/T5 (savoir.py t5) et synthèse de semaine
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-07-21.md, 6 dernières lignes)
> # Dimanche 21 juillet 2041 — univers 3, sixième jour
> - **00h00-12h05** (tour n° 10) : tour n° 10 : réveil 06h30, message de Hye-won à 07h17, départ 07h30 d'Audun, parking longue durée de Lorraine TGV à 08h46, TGV de 09h15 à l'heure, enregistrement Korean Air au terminal 2E, salle d'embarquement à 12h05
> - jets du matin (tous NON) : ralentissement sur l'A31 (8 %), retard du TGV (12 %), deuxième passage à l'enregistrement (30 %), retard du KE902 (12 %)
> - Tirages du tour : jet « A31 dimanche matin entre Thionville et Metz : ralentissement » → NON (50,88) ; jet « TGV INOUI Lorraine TGV - CDG de 09h15 : retard de plus de 10 » → NON (34,04) ; jet « Enregistrement Korean Air à CDG : deuxième passage demandé ( » → NON (86,82) ; jet « Korean Air KE902 : retard au départ de plus de 30 minutes » → NON (39,94) ; T14 Hye-won → information (90,07) ; T10 Hye
> - Tour en cours à 12h05, en attente de William : **Embarquement du KE902 à 12h35 (décollage 13h20)**.
