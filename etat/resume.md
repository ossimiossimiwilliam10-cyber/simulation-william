# Résumé d'état (généré le 11/10/2026 22:17 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : samedi 14/07/2040 08:37 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 06:37 ; lisbonne 07:37 ; mindelo 05:37 ; casablanca 07:37 ; douala 07:37 ; paris 08:37
- **En attente de William** :
  - Sa journée du samedi 14/07/2040 (premier jour des vacances d'été ; Fête nationale française)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **9 800,00 €**
- Compte épargne « Projet » (Spuerkeess) : **357 000,00 €**
- ETF (valeur de marché : calages seulement) : **288 000,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **110 000,00 €**
- Part nette de la maison d'Audun-le-Tiche : **90 000,00 €**
- Patrimoine net de William : **744 800,00 €**
- Prévu dans les 14 jours : 16/07 Box internet fibre et forfait mobile (-63,00 €)

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (1)
- A001 Mon 16/07 08:00 (luxembourg) | Moteur et utilisateur : Revue du lundi n° 1 de l'univers 2 (hors fiction, avant le premier tour du jour) ; validation des pourcentages de T12 à T14 et adaptation du pack d'aléas [prevu]  — CLAUDE.md §12 | reporté de 2040-07-23 08:00 : départ de l'univers 2 redaté au samedi 14/07/2040 (demande de l'utilisateur du 11/10/2026) : premier lundi le 16/07
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
> > de classe : vendredi 13/07 ; rentrée : lundi 17/09 ; projection fondée sur le règlement grand-ducal du 3 juin 2026, voir
> > `donnees/faits.csv` F001). Le faux départ du mardi 17/07/2040 (un tour, sans action de William) est archivé :
> > `archives/univers-2-faux-depart/`.
> - **Nuit du 13 au 14/07** : coucher vers 23h20 (tiré au dé : `memoire/tirages-aleas.md`) ; environ 9 h de sommeil.
> - **08h37** : réveil spontané, sans réveil (tiré au dé), chez lui, à Audun-le-Tiche. Départ de l'univers 2.
> - Tour en cours à 08h37, en attente de William : **sa journée**.
