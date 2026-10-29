# Résumé d'état (généré le 29/10/2026 10:46 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : vendredi 16/08/2041 13:00 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), residence hoteliere
- **Heure dans les autres lieux** : lisbonne 14:00 ; luxembourg 15:00 ; mindelo 12:00 ; casablanca 14:00 ; douala 14:00 ; addis 16:00 ; manille 21:00 ; paris 15:00 ; seoul 22:00 ; bresil 10:00
- **En attente de William** :
  - Choix DC (Kouadio vs Tanoh) a notifier a Coulibaly ; RIB SGCI a 13h30 pour virement CCA ; signature bail Vallons a 14h00

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 243,99 €**
- Compte épargne (Spuerkeess) : **75 982,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **858 366,05 €**

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (0)
- rien
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 13 informé(s) hors William ; fuite interne 39 %, externe 13 %
- affaire_projet_ci_art14 : 1 informé(s) hors William ; fuite interne 3 %, externe 1 %

## Fêtes et fériés dans les 30 jours
- mer 28/08/2041 -- ≈ début du Ramadan

## Routine du tour
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-08-16.md, 6 dernières lignes)
> - Tirages du tour : T14 → message_routine (48,18) ; T10 → rapide (30,75).
> - Tour en cours à 11h00, en attente de William : **Dossiers DC (Kouadio + Tanoh) recus a midi ; RIB SOLEIL B2B CI en attente pour virement CCA ; bail villa Vallons a 14h00**.
> - **12h15-12h15** (tour n° 94) : voir le texte exact du tour (journal/tours/).
> - Tour en cours à 12h15, en attente de William : **Scoring grille 5 questions pour Marc-Antoine Kouadio et Viviane Tanoh ; RIB SGCI a 13h30 pour virement CCA ; signature bail Vallons a 14h00**.
> - **13h00-13h00** (tour n° 95) : voir le texte exact du tour (journal/tours/).
> - Tour en cours à 13h00, en attente de William : **Choix DC (Kouadio vs Tanoh) a notifier a Coulibaly ; RIB SGCI a 13h30 pour virement CCA ; signature bail Vallons a 14h00**.
