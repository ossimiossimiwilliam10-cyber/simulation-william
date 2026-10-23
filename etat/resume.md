# Résumé d'état (généré le 23/10/2026 05:45 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : lundi 22/07/2041 08:12 (seoul, UTC+9)
- **Lieu de William** : Aéroport international d'Incheon, piste d'atterrissage (KE902)
- **Heure dans les autres lieux** : abidjan 23:12 ; lisbonne 00:12 ; luxembourg 01:12 ; mindelo 22:12 ; casablanca 00:12 ; douala 00:12 ; addis 02:12 ; manille 07:12 ; paris 01:12 ; bresil 20:12
- **En attente de William** :
  - Écrire à Hye-won (rappel du joueur) et formalités d'arrivée à Séoul

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **9 781,00 €**
- Compte épargne (Spuerkeess) : **75 250,00 €**
- ETF (valeur de marché : calages seulement) : **670 380,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **102 621,78 €**
- Part nette de la maison d'Audun-le-Tiche : **97 378,22 €**
- Patrimoine net de William : **852 789,22 €**
- Prévu dans les 14 jours : 31/07 Traitement mensuel de William (9 320,00 €) ; 01/08 Minett Combat Club (-85,00 €) ; 01/08 Package bancaire Zebra Premium (-12,83 €) ; 02/08 Virement permanent vers le compte épargne (-732,00 €) ; 02/08 Virement permanent vers le compte épargne (732,00 €) ; 02/08 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/08 Virement permanent vers le compte-titres ETF (5 755,00 €) ; 05/08 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/08 Prêt immobilier de la maison d'Audun-le-Tiche (-626,84 €) ; 05/08 Part nette du bien financé : + capital remboursé (626,84 €) ; 05/08 Assurance habitation (-45,00 €) ; 05/08 Voiture électrique : assurance tous risques (-107,00 €)

## ÉCHÉANCES ÉCHUES NON CLOSES (jouer, reporter avec raison ou annuler : règle 14)
- A008 Sun 21/07 20:20 (seoul) | Korean Air (Premium Economy) : Vol aller Paris → Séoul (KE 902…KE 902) · départ 13:20 de Paris-Charles-de-Gaulle, arrivée le 22/07 à 07:50 (heure locale) · réservation XLGTS3 [prevu]  — réservation R001 (etat/reservations.csv)
- A011 Mon 22/07 07:50 (seoul) | William : Rappel du joueur : écrire à Hye-won dès l'arrivée à Séoul (atterrissage du KE902) [prevu]  — intention du joueur du 21/07/2041 : il rédige lui-même le message

## Agenda : dans les 24 heures (3)
- A007 Mon 22/07 11:00 (seoul) | William : Installation et prise de possession de l'officetel meublé à Yeonnam-dong (Mapo-gu) [prevu]  — réservé le 20/07 (2 450 € pour 6 semaines du 22/07 au 02/09)
- A001 Mon 22/07 15:00 (seoul) | Moteur et utilisateur : Revue du lundi n° 1 de l'univers 3 (hors fiction, avant le premier tour du jour) ; adaptation des aléas et propositions [prevu]  — CLAUDE.md §12 | premier lundi de l'Univers 3 le 22/07/2041
- A012 Mon 22/07 21:17 (seoul) | Thiago Rocha (courriel) : Thiago Rocha envoie la data room par courriel (promesse du vendredi 19/07 : lundi matin , SolarGIS, baux notariés, autorisations CEMIG : PDF à générer par courriel.py au moment voulu) · souci : mal de dos chronique · objectif : acheter un logement (ou un plus grand) · foyer : en couple, sans enfant · défauts : boit trop le week-end et le minimise / donneur de leçons sur la santé, l'argent ou l'éducation [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · T10 : dans_l_heure (jet 50.3) · texte à écrire d'après la fiche (reactions.py jouer) [reaction pour=thiago-rocha-br canal=courriel]
## Agenda : de J+1 à J+7 (1)
- A006 Tue 23/07 14:00 (seoul) | Min-ji & William : Sortie barbecue coréen à Seongsu-dong (découverte du quartier et spécialités) [prevu]  — rendez-vous convenu le 19/07
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)

## Fêtes et fériés dans les 30 jours
- jeu 15/08/2041 FR Assomption
- jeu 15/08/2041 KR Fête de la Libération (Gwangbokjeol)
- jeu 15/08/2041 LU Assomption

## Routine du tour
- AUJOURD'HUI lundi : revue du lundi (audit_jets.py, tirage_aleas.py, vie hors de la scène principale, monde, idées)
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-07-22.md, 6 dernières lignes)
> # Lundi 22 juillet 2041 — univers 3, septième jour
> - **08h12-08h12** (tour n° 11) : tour n° 11 : remerciement à Hye-won à 12h10 (sans réponse), embarquement 12h35, décollage 13h29, 4 h 30 de sommeil, atterrissage à Incheon à 08h12 (22 minutes de retard)
> - jets du vol : sommeil de 4 h 30 (OUI), arrivée en avance (NON), retard de 15 minutes ou plus (OUI), valise retardée (NON), file d'immigration de plus de 45 minutes (NON) ; réponse de Hye-won au remerciement : T21b ignore
> - Tirages du tour : T21b Hye-won → ignore (88,24) ; jet « KE902 : William dort au moins 4 h pendant le vol (OUI : 4 h  » → OUI (39,04) ; jet « KE902 : atterrissage en avance d'au moins 10 minutes » → NON (91,44) ; jet « KE902 : atterrissage en retard d'au moins 15 minutes (si pas » → OUI (4,71) ; jet « Valise de soute non arrivée à Incheon (bagage retardé) » → NON (28,92) ; jet « Incheon, contrôle
> - Tour en cours à 08h12, en attente de William : **Écrire à Hye-won (rappel du joueur) et formalités d'arrivée à Séoul**.
