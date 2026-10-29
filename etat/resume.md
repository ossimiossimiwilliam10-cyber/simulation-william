# Résumé d'état (généré le 29/10/2026 12:19 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 18/08/2041 21:30 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 22:30 ; luxembourg 23:30 ; mindelo 20:30 ; casablanca 22:30 ; douala 22:30 ; addis 00:30 ; manille 05:30 ; paris 23:30 ; seoul 06:30 ; bresil 18:30
- **En attente de William** :
  - Revue du lundi 19 août au matin et validation du suivi des devis d'aménagement de la villa des Vallons

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 243,99 €**
- Compte épargne (Spuerkeess) : **67 982,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **850 366,05 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €)

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
- lendemain = lundi : revue du lundi à présenter AVANT le reste (CLAUDE.md §12) ; dimanche soir : T4/T5 (savoir.py t5) et synthèse de semaine
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-08-18.md, 6 dernières lignes)
> - **00h00-16h30** (tour n° 103) : Footing dominical 5 km ; enquête terrain micro-commerces et délestage à Deux-Plateaux et Anono (Yéo méfiance, Camara conversation, Bamba poli_bref) ; note terrain PDF générée ; modèle B2B conforté
> - Tirages du tour : T17 Wilfried → mefiance (82,55) ; T17 Safiatou → conversation (38,19) ; T17 Kader → poli_bref (17,13).
> - Tour en cours à 16h30, en attente de William : **Programme de la soirée du dimanche 18 août et directives pour la semaine du lundi 19 août**.
> - **16h30-21h30** (tour n° 104) : Rapport enquête terrain transmis à Coulibaly via Gestion ; réponse par courriel officiel de Coulibaly (orientation PAYG et microfinance à moyen terme, sanctuarisation B2B pour septembre, devis Vallons lancés lundi 08h00) ; dîner room-service K014 (20,50 €) ; synthèse semaine W33 rédigée
> - Tirages du tour : T4 → aucune (33,5) ; T5 → fuite_interne (28,95) ; T4 → aucune (76,27) ; T5 → aucune (65,23) ; T7c → execute_sans_discuter (52,81) ; T10 → dans_la_journee (74,5).
> - Tour en cours à 21h30, en attente de William : **Revue du lundi 19 août au matin et validation du suivi des devis d'aménagement de la villa des Vallons**.
