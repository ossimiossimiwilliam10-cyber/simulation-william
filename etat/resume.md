# Résumé d'état (généré le 28/10/2026 13:37 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : mardi 13/08/2041 15:30 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 16:30 ; luxembourg 17:30 ; mindelo 14:30 ; casablanca 16:30 ; douala 16:30 ; addis 18:30 ; manille 23:30 ; paris 17:30 ; seoul 00:30 ; bresil 12:30
- **En attente de William** :
  - Validation de l'étude de cadrage budgétaire d'installation (43 M FCFA) et attente du rapport d'étape de 17h00

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

## Fin du dernier journal (2041-08-13.md, 6 dernières lignes)
> - Tour en cours à 09h50, en attente de William : **Séance solennelle de signature notariée des statuts et du mandat DG chez Me Gnamien à 10h00, et validation des propositions P27 à P31 de la Revue du lundi n° 4**.
> - **09h50-12h45** (tour n° 81) : voir le texte exact du tour (journal/tours/).
> - Tirages du tour : T4 → aucune (0,26) ; T5 → fuite_interne (27,92) ; T4 → aucune (2,36) ; T5 → aucune (30,43).
> - Tour en cours à 12h45, en attente de William : **Arbitrage sur le dejeuner de travail et le calendrier des visites de villas QG pour mercredi apres-midi**.
> - **12h45-15h30** (tour n° 82) : voir le texte exact du tour (journal/tours/).
> - Tour en cours à 15h30, en attente de William : **Validation de l'étude de cadrage budgétaire d'installation (43 M FCFA) et attente du rapport d'étape de 17h00**.
