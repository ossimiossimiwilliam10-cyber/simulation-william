# Résumé d'état (généré le 29/10/2026 21:41 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 15/09/2041 09:00 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 07:00 ; lisbonne 08:00 ; mindelo 06:00 ; casablanca 07:00 ; douala 08:00 ; addis 10:00 ; manille 15:00 ; paris 09:00 ; seoul 16:00 ; bresil 04:00
- **En attente de William** :
  - Séance du dimanche : signature des actes, report des niveaux 3-4, prospection ; entraînement du dimanche ; programme de la rentrée

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **6 637,94 €**
- Compte épargne (Spuerkeess) : **46 786,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 366,28 €**
- Part nette de la maison d'Audun-le-Tiche : **98 633,72 €**
- Patrimoine net de William : **828 192,66 €**
- Prévu dans les 14 jours : 16/09 Box internet fibre et forfait mobile (-63,00 €) ; 16/09 Abonnement à l'agent IA de William (-24,30 €) ; 20/09 Eau et assainissement (-187,50 €)

## Agenda : dans les 24 heures (1)
- A002 Mon 16/09 08:00 (luxembourg) | Lycée de William : Rentrée scolaire 2041-2042 (reprise des cours, 22 leçons normales + 3 leçons sup) [latent]  — rentrée officielle fixée au lundi 16 septembre 2041 (MENJE)
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

## Fin du dernier journal (2041-09-15.md, 6 dernières lignes)
> # Dimanche 15 septembre 2041 — univers 3, 62e jour
> - **00h00-09h00** (tour n° 144) : Option 2 (indemnité de 1 M FCFA) et six tâches confiées. Avance 09-15/09 : club lundi, mercredi, vendredi ; relevé Visa Premier débité le 09/09 ; cours prêts ; courses 94,10 €. Coulibaly : T12 concede_beaucoup (accepte l'indemnité) ; T7c execute_a_contrecoeur sur les six tâches (bailleur fait, un devis d'assurance 820 000 FCFA/an, un devis comptable 180 000 FCFA/m
> - Tirages du tour : T22 → zero_segment (36,7) ; T22 → zero_segment (30,41) ; T22 → zero_segment (16,51) ; T22 → zero_segment (38,18) ; T7c Mohamed → execute_a_contrecoeur (78,73) ; T12 Mohamed → concede_beaucoup (57,93) ; T10 Ismaël → rapide (28,6) ; procédure : 08/09 23:24-06:27 ; 09/09 22:58-07:27 ; 10/09 23:14-07:53 ; 11/09 22:35-05:40 ; 12/09 22:51-07:20 ; 13/09 22:42-06:19 ; 14/09 23:02-06:08
> - Tour en cours à 09h00, en attente de William : **Séance du dimanche : signature des actes, report des niveaux 3-4, prospection ; entraînement du dimanche ; programme de la rentrée**.
