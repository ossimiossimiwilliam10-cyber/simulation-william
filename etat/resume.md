# Résumé d'état (généré le 29/10/2026 21:37 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 08/09/2041 10:21 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 08:21 ; lisbonne 09:21 ; mindelo 07:21 ; casablanca 08:21 ; douala 09:21 ; addis 11:21 ; manille 16:21 ; paris 10:21 ; seoul 17:21 ; bresil 05:21
- **En attente de William** :
  - Option pour le mois non rémunéré de Coulibaly ; validation des six tâches ; programme de la semaine

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
> - Tour en cours à 09h00, en attente de William : **Séance du dimanche : devis de Me Gnamien (295 000 FCFA TTC) ; devis informatique (3,9 M FCFA ou attendre)**.
> - **09h00-09h52** (tour n° 142) : Devis acceptés : Me Gnamien (295 000 FCFA TTC) et informatique (3,9 M FCFA) ; engagements mis à jour. Rapport « Charge et tâches du directeur général » (PDF) : en suspens les conditions du bailleur, mobilier, pickup, niveaux 3-4 ; personne ne porte assurance, comptabilité, prospection, moyens de paiement SGCI ; Coulibaly non rémunéré depuis le 26/08 (convention, a
> - Tirages du tour : procédure : 01/09 22:34-07:10 ; 02/09 22:50-05:52 ; 03/09 22:32-06:10 ; 04/09 22:53-06:52 ; 05/09 22:44-06:04 ; 06/09 23:26-06:34 ; 07/09 23:26-07:45 ; procédure : LU04, LU01, FR01.
> - Tour en cours à 09h52, en attente de William : **Tâches à confier à Coulibaly ; indemnité de septembre ; programme de la semaine**.
> - **09h52-10h21** (tour n° 143) : Question de William sur le risque juridique du mois non rémunéré de Coulibaly : avis du conseiller (mandat gratuit convenu ; risque de requalification si tâches sous direction ; trois options ; avis : indemnité forfaitaire de 1 000 000 FCFA avec reconnaissance écrite, via Me Gnamien).
> - Tour en cours à 10h21, en attente de William : **Option pour le mois non rémunéré de Coulibaly ; validation des six tâches ; programme de la semaine**.
