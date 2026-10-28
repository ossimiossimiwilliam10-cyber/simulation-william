# Résumé d'état (généré le 28/10/2026 17:40 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : jeudi 15/08/2041 22:00 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 23:00 ; luxembourg 00:00 ; mindelo 21:00 ; casablanca 23:00 ; douala 23:00 ; addis 01:00 ; manille 06:00 ; paris 00:00 ; seoul 07:00 ; bresil 19:00
- **En attente de William** :
  - Réponse au message de Fatoumata et heure de rendez-vous CEPICI pour Coulibaly

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 355,59 €**
- Compte épargne (Spuerkeess) : **75 982,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **858 477,65 €**
- Prévu dans les 14 jours : 16/08 Box internet fibre et forfait mobile (-63,00 €) ; 16/08 Abonnement à l'agent IA de William (-24,30 €)

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (0)
- rien
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 13 informé(s) hors William ; fuite interne 39 %, externe 13 %
- affaire_projet_ci_art14 : 1 informé(s) hors William ; fuite interne 3 %, externe 1 %

## Fêtes et fériés dans les 30 jours
- jeu 15/08/2041 FR Assomption
- jeu 15/08/2041 LU Assomption
- mer 28/08/2041 -- ≈ début du Ramadan

## Routine du tour
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-08-15.md, 6 dernières lignes)
> - Tour en cours à 17h45, en attente de William : **Choix du profil à contacter (Mya ou Christelle) et formule proposée (créneau court début de soirée ou nuitée)**.
> - **17h45-19h30** (tour n° 90) : voir le texte exact du tour (journal/tours/).
> - Tour en cours à 19h30, en attente de William : **Choix pour la soirée du jeudi 15 août (dîner en suite ou sortie calme aux Vallons) et directives préalables pour vendredi matin**.
> - **19h30-22h00** (tour n° 91) : voir le texte exact du tour (journal/tours/).
> - Tirages du tour : T14 → information (85,58) ; T10 → dans_la_journee (68,49).
> - Tour en cours à 22h00, en attente de William : **Réponse au message de Fatoumata et heure de rendez-vous CEPICI pour Coulibaly**.
