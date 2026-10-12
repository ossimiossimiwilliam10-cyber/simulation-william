# Résumé d'état (généré le 12/10/2026 18:28 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : lundi 16/07/2040 07:40 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 05:40 ; lisbonne 06:40 ; mindelo 04:40 ; casablanca 06:40 ; douala 06:40 ; addis 08:40 ; manille 13:40 ; paris 07:40
- **En attente de William** :
  - Décisions de l'utilisateur sur la revue du lundi n° 1 (puis tirage des aléas de la semaine)
  - Sa journée du lundi 16/07/2040 : eTravel possible dès 10h30 ; départ pour Manille le mercredi 18/07 à 15h40 (R003-R004) ; trajet vers Findel non prévu

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **39 737,00 €**
- Compte épargne (Spuerkeess) : **327 000,00 €**
- ETF (valeur de marché : calages seulement) : **288 000,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **110 003,13 €**
- Part nette de la maison d'Audun-le-Tiche : **89 996,87 €**
- Patrimoine net de William : **744 733,87 €**

## Agenda : dans les 24 heures (2)
- A010 Mon 16/07 10:30 (luxembourg) | Philippines (eTravel) : eTravel : inscription en ligne gratuite possible à partir de maintenant, 72 heures avant l'arrivée à Manille (jeudi 19/07 à 16h30, heure locale) · code QR à montrer à l'immigration [prevu]  — F051 · arrivée du vol PVS2HS (R004) · 16h30 à Manille = 10h30 au Luxembourg
- A012 Mon 16/07 10:30 (luxembourg) | William (rappel du téléphone) : Rappel : remplir l'eTravel (ouverture 72 heures avant l'arrivée à Manille) [prevu]  — rappel créé par William le samedi 14/07 à 11h27 · voir A010
## Agenda : de J+1 à J+7 (3)
- A013 Tue 17/07 09:25 (luxembourg) | Clément Grandjean (club) : Message spontané d'un membre du club (tiré le 16/07 : rituel du lundi, CLAUDE.md §12) · contenu à choisir d'après sa fiche, entrée en scène par personnage.py apparait [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — rituels.py message-proche, semaine du 2040-07-16 · NON CONNU DE WILLIAM : ne rien montrer avant l'heure
- A008 Wed 18/07 15:40 (luxembourg) | Lufthansa + Qatar Airways : Vol aller Luxembourg → Manille (LH 391…QR 932) · départ 15:40 de Luxembourg-Findel, arrivée le 19/07 à 16:30 (heure locale) · réservation PVS2HS [prevu]  — réservation R004 (etat/reservations.csv)
- A007 Thu 19/07 08:00 (luxembourg) | City Garden Grand Hotel : Arrivée à l'hôtel City Garden Grand Hotel (Manille), 36 nuit(s) · réservation R6T4JZA2 [prevu]  — réservation R003 (etat/reservations.csv)
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
> # Lundi 16 juillet 2040 — univers 2, troisième jour
> - **Nuit du 15 au 16/07** : coucher à 23h15, réveil à 7h40, sans réveil (heures tirées au dé).
> - **06h00** : prélèvement de la box internet et du forfait mobile (63 €, E005 : dû le 15, un dimanche, passé au jour ouvré suivant).
> - **07h40** : réveil ; grand soleil, 16 °C dehors (27 °C annoncés) ; aucun message. Fin de l'avance rapide (tour n° 8).
> - **Revue du lundi n° 1 de l'univers 2** (hors fiction, avant le premier tour du jour) : présentée au joueur ; compte rendu dans `memoire/revue-lundi-2040-07-16.md` ; décisions et tirage des aléas de la semaine en attente de sa réponse. Message spontané d'un proche de la semaine tiré (moteur seulement : agenda A013).
> - Tour en cours à 07h40, en attente de William : **sa journée** et **ses décisions sur la revue n° 1**.
