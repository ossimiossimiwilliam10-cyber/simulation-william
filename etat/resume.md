# Résumé d'état (généré le 30/10/2026 19:02 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 13/10/2041 09:00 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 07:00 ; lisbonne 08:00 ; mindelo 06:00 ; casablanca 08:00 ; douala 08:00 ; addis 10:00 ; manille 15:00 ; paris 09:00 ; seoul 16:00 ; bresil 04:00
- **En attente de William** :
  - Séance du dimanche : offre écrite à Vridi, objectifs de Viviane Tanoh, retards de Coulibaly ; programme de la semaine du 14 octobre

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **7 007,53 €**
- Compte épargne (Spuerkeess) : **8 273,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **100 735,78 €**
- Part nette de la maison d'Audun-le-Tiche : **99 264,22 €**
- Patrimoine net de William : **790 679,75 €**
- Prévu dans les 14 jours : 15/10 Box internet fibre et forfait mobile (-63,00 €) ; 15/10 Taxe foncière (-1 190,00 €) ; 16/10 Abonnement à l'agent IA de William (-24,30 €)

## ÉCHÉANCES ÉCHUES NON CLOSES (jouer, reporter avec raison ou annuler : règle 14)
- A142 Tue 08/10 19:00 (luxembourg) | Mohamed Coulibaly : Point écrit sur le rendez-vous manqué de Vridi (demande de William du 06/10) [prevu]  — à lier au compte rendu du mardi ; fiabilité de Coulibaly au moment dit

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (0)
- rien
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 15 informé(s) hors William ; fuite interne 40 %, externe 15 %
- affaire_projet_ci_art14 : 2 informé(s) hors William ; fuite interne 6 %, externe 2 %

## Fêtes et fériés dans les 30 jours
- ven 01/11/2041 FR Toussaint
- ven 01/11/2041 LU Toussaint
- lun 11/11/2041 FR Armistice 1918

## Routine du tour
- lendemain = lundi : revue du lundi à présenter AVANT le reste (CLAUDE.md §12) ; dimanche soir : T4/T5 (savoir.py t5) et synthèse de semaine
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-10-13.md, 6 dernières lignes)
> # Dimanche 13 octobre 2041 — univers 3, 90e jour
> - **00h00-09h00** (tour n° 151) : Notation : grille validée, interne, pas de correction ; branchée sur la rubrique existante « Équipes et notes » de Gestion (outils/notation.py, etat/gestion-collaborateurs.csv). Avance 07-13/10 (même programme) : rituels du lundi (revue n° 10, P54-P56 ; aléas A19, A26, A37 ; T22 : H005 palier 3 (Éric approché, caché), H006 palier 4 ; prospects : rien), point écrit
> - Tirages du tour : T22 → zero_segment (53,4) ; T22 → un_segment (89,82) ; T22 → un_segment (83,2) ; T15 Sam → accepte_volontiers (33,79) ; jet « Mohamed Coulibaly tient sa promesse : envoie le point écrit  » → NON (93,87) ; jet « Mohamed Coulibaly tient sa promesse : envoie son compte rend » → NON (95,32) ; jet « Viviane Tanoh tient sa promesse : obtient un nouveau rendez- » → NON (91,09) ; procé
> - Tour en cours à 09h00, en attente de William : **Séance du dimanche : offre écrite à Vridi, objectifs de Viviane Tanoh, retards de Coulibaly ; programme de la semaine du 14 octobre**.
