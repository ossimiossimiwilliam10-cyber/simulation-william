# Résumé d'état (généré le 30/10/2026 18:50 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 06/10/2041 09:00 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 07:00 ; lisbonne 08:00 ; mindelo 06:00 ; casablanca 08:00 ; douala 08:00 ; addis 10:00 ; manille 15:00 ; paris 09:00 ; seoul 16:00 ; bresil 04:00
- **En attente de William** :
  - Séance du dimanche : enveloppe d'approvisionnement (3,5 M FCFA), suite de Vridi ; programme de la semaine du 7 octobre

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 808,21 €**
- Compte épargne (Spuerkeess) : **8 273,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 366,28 €**
- Part nette de la maison d'Audun-le-Tiche : **98 633,72 €**
- Patrimoine net de William : **791 849,93 €**
- Prévu dans les 14 jours : 07/10 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 07/10 Prêt immobilier de la maison d'Audun-le-Tiche (-630,50 €) ; 07/10 Part nette du bien financé : + capital remboursé (630,50 €) ; 07/10 Assurance habitation (-45,00 €) ; 07/10 Voiture électrique : assurance tous risques (-107,00 €) ; 10/10 Électricité (-132,00 €) ; 10/10 Gaz naturel (-253,00 €) ; 15/10 Box internet fibre et forfait mobile (-63,00 €) ; 15/10 Taxe foncière (-1 190,00 €) ; 16/10 Abonnement à l'agent IA de William (-24,30 €)

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (0)
- rien
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 14 informé(s) hors William ; fuite interne 40 %, externe 14 %
- affaire_projet_ci_art14 : 2 informé(s) hors William ; fuite interne 6 %, externe 2 %

## Fêtes et fériés dans les 30 jours
- ven 01/11/2041 FR Toussaint
- ven 01/11/2041 LU Toussaint

## Routine du tour
- lendemain = lundi : revue du lundi à présenter AVANT le reste (CLAUDE.md §12) ; dimanche soir : T4/T5 (savoir.py t5) et synthèse de semaine
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-10-06.md, 6 dernières lignes)
> # Dimanche 6 octobre 2041 — univers 3, 83e jour
> - **00h00-09h00** (tour n° 149) : Réunion close à 18h04 (A137). Semaine 02-06/10 : apport de 5 000 € ; climatiseurs livrés partiellement (H003 palier 4), solde payé ; Viviane Tanoh oublie Vridi (T18 oubli complet, moral 54) ; Coulibaly (T7c execute_sans_discuter) propose l'enveloppe de 3,5 M FCFA ; compte rendu du vendredi en retard (T18). William : huit heures de sommeil, club mercredi et samedi,
> - Tirages du tour : T7c Mohamed → execute_sans_discuter (33,42) ; T15 Sam → decline (94,91) ; jet « Mohamed Coulibaly tient sa promesse : envoie son compte rend » → OUI (16,46) ; jet « Mohamed Coulibaly tient sa promesse : envoie son compte rend » → NON (98,9) ; jet « Viviane Tanoh tient sa promesse : tient le rendez-vous de Vr » → NON (91,66) ; T18 Mohamed → retard (12,44) ; T18 Viviane → oubli_c
> - Tour en cours à 09h00, en attente de William : **Séance du dimanche : enveloppe d'approvisionnement (3,5 M FCFA), suite de Vridi ; programme de la semaine du 7 octobre**.
