# Résumé d'état (généré le 29/10/2026 21:17 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 01/09/2041 09:00 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 07:00 ; lisbonne 08:00 ; mindelo 06:00 ; casablanca 07:00 ; douala 08:00 ; addis 10:00 ; manille 15:00 ; paris 09:00 ; seoul 16:00 ; bresil 04:00
- **En attente de William** :
  - Séance du dimanche : trois décisions (gardiennage d'octobre, avenant des jalons, reçu du dépôt)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **17 236,67 €**
- Compte épargne (Spuerkeess) : **45 299,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **836 675,73 €**
- Prévu dans les 14 jours : 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-1 487,00 €) ; 02/09 Virement permanent vers le compte épargne (1 487,00 €) ; 02/09 Virement permanent vers SOLEIL B2B CI (-5 000,00 €) ; 05/09 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/09 Prêt immobilier de la maison d'Audun-le-Tiche (-628,66 €) ; 05/09 Part nette du bien financé : + capital remboursé (628,66 €) ; 05/09 Assurance habitation (-45,00 €) ; 05/09 Voiture électrique : assurance tous risques (-107,00 €) ; 09/09 Visa Premier : relevé clos le 29/08/2041, débit du s (-2 341,72 €) ; 10/09 Électricité (-132,00 €) ; 10/09 Gaz naturel (-253,00 €)

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

## Fin du dernier journal (2041-09-01.md, 6 dernières lignes)
> # Dimanche 1er septembre 2041 — univers 3, 48e jour
> - **00h00-09h00** (tour n° 139) : P42-P44 validées et installées (Rapports archivés dans Gestion ; A40, A41). Règle : semaine programmée → avance hebdomadaire. Semaine du 26/08 : retour à Findel (parking 255,22 €), club lundi (Lenny, T15 en_parle_a_d_autres : maillot montré, Thiago Alves apprend le projet), mercredi, vendredi ; rhume fini mardi ; courses 96,40 €. Société : 20 000 € crédités lundi 
> - Tirages du tour : T22 → zero_segment (15,85) ; T22 → un_segment (55,42) ; T22 → zero_segment (29,76) ; T22 → zero_segment (8,69) ; procédure : LU03, LU04, FR01 ; procédure : lundi 26/08 16:10 ; jet « Mohamed Coulibaly tient sa promesse : confirme Froid Lagune  » → OUI (35,94) ; jet « Mohamed Coulibaly tient sa promesse : dépose les demandes CI » → OUI (25,44) ; jet « Mohamed Coulibaly tient sa p
> - Tour en cours à 09h00, en attente de William : **Séance du dimanche : trois décisions (gardiennage d'octobre, avenant des jalons, reçu du dépôt)**.
