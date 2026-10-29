# Résumé d'état (généré le 29/10/2026 21:28 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 08/09/2041 09:00 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 07:00 ; lisbonne 08:00 ; mindelo 06:00 ; casablanca 07:00 ; douala 08:00 ; addis 10:00 ; manille 15:00 ; paris 09:00 ; seoul 16:00 ; bresil 04:00
- **En attente de William** :
  - Séance du dimanche : devis de Me Gnamien (295 000 FCFA TTC) ; devis informatique (3,9 M FCFA ou attendre)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **9 458,76 €**
- Compte épargne (Spuerkeess) : **46 786,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 366,28 €**
- Part nette de la maison d'Audun-le-Tiche : **98 633,72 €**
- Patrimoine net de William : **831 013,48 €**
- Prévu dans les 14 jours : 09/09 Visa Premier : relevé clos le 29/08/2041, débit du s (-2 341,72 €) ; 10/09 Électricité (-132,00 €) ; 10/09 Gaz naturel (-253,00 €) ; 16/09 Box internet fibre et forfait mobile (-63,00 €) ; 16/09 Abonnement à l'agent IA de William (-24,30 €) ; 20/09 Eau et assainissement (-187,50 €)

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (0)
- rien
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 14 informé(s) hors William ; fuite interne 40 %, externe 14 %
- affaire_projet_ci_art14 : 1 informé(s) hors William ; fuite interne 3 %, externe 1 %

## Fêtes et fériés dans les 30 jours
- aucun

## Routine du tour
- lendemain = lundi : revue du lundi à présenter AVANT le reste (CLAUDE.md §12) ; dimanche soir : T4/T5 (savoir.py t5) et synthèse de semaine
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-09-08.md, 6 dernières lignes)
> # Dimanche 8 septembre 2041 — univers 3, 55e jour
> - **00h00-09h00** (tour n° 141) : Avance hebdomadaire 02-08/09 : Lenny (A136) ; club lundi, mercredi, vendredi (raillerie au vestiaire après les confidences de Lenny) ; préparation des cours mardi et jeudi ; apport de 5 000 € parti le 02/09 ; courses 91,80 €. Société : reçu du dépôt obtenu le 05/09 (PDF courriels) ; T22 : H002 palier 2 (visite CIE reportée) ; monde social : tensions Mariam Brou/Co
> - Tirages du tour : T22 → un_segment (64,8) ; T22 → zero_segment (4,81) ; T22 → zero_segment (7,37) ; T22 → zero_segment (39,35) ; T10 Lenny → dans_la_journee (63,35) ; jet « Mohamed Coulibaly tient sa promesse : obtient le reçu du dép » → OUI (12,89) ; jet « Mohamed Coulibaly tient sa promesse : envoie son compte rend » → OUI (63,51) ; jet « Mohamed Coulibaly tient sa promesse : envoie son compte
> - Tour en cours à 09h00, en attente de William : **Séance du dimanche : devis de Me Gnamien (295 000 FCFA TTC) ; devis informatique (3,9 M FCFA ou attendre)**.
