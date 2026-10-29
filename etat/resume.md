# Résumé d'état (généré le 29/10/2026 20:36 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 25/08/2041 07:18 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 08:18 ; luxembourg 09:18 ; mindelo 06:18 ; casablanca 07:18 ; douala 08:18 ; addis 10:18 ; manille 15:18 ; paris 09:18 ; seoul 16:18 ; bresil 04:18
- **En attente de William** :
  - Jour du départ : règlement de la résidence avant midi, vol AF703 à 22h15

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **45 299,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **827 707,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €) ; 05/09 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/09 Prêt immobilier de la maison d'Audun-le-Tiche (-628,66 €) ; 05/09 Part nette du bien financé : + capital remboursé (628,66 €) ; 05/09 Assurance habitation (-45,00 €) ; 05/09 Voiture électrique : assurance tous risques (-107,00 €)

## Agenda : dans les 24 heures (2)
- A111 Sun 25/08 12:00 (abidjan) | Résidence hôtelière (Cocody Deux-Plateaux) : Départ de la résidence et règlement du séjour du 12 au 25 août : 1 690 € (empreinte de la Visa Premier prise à l'arrivée) ; bagages gardés à la réception jusqu'au soir [prevu]  — U3-19 : la résidence n'avait jamais été réglée ; le jour dit : python outils/cartes.py payer --carte visa_premier --montant 1690 --marchand "Résidence hôtelière Deux-Plateaux" --quand "2041-08-25 12:00"
- A112 Sun 25/08 22:15 (abidjan) | Air France : Vol retour AF703 Abidjan (FHB) → Paris-CDG (arrivée le 26/08 vers 05h45), puis correspondance vers Luxembourg-Findel ; billet aller-retour réglé le 27/07 (1 285 €) [prevu]  — U3-19 : le retour n'était pas à l'agenda ; horaire d'après l'AF703 de 2026 (départ vers 22h15, F119) ; quitter la résidence vers 19h00 (trajet et contrôles)
## Agenda : de J+1 à J+7 (1)
- A121 Mon 26/08 17:00 (abidjan) | Mohamed Coulibaly : Réponse de l'agence de gardiennage (via le bailleur) sur la prolongation du gardiennage de la villa en septembre ; copie du bail promise « dès qu'il repasse à la villa » [prevu]  — promesses du 20/08 09h55 ; T18 si manquement | reporté de 2041-08-22 17:00 : T12 temporise : le bailleur veut en parler en début de semaine prochaine (courrier de l'agence du 22/08) ; copie du bail déjà reçue le 21/08
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

## Fin du dernier journal (2041-08-25.md, 6 dernières lignes)
> # Dimanche 25 août 2041 — univers 3, 41e jour
> - **00h00-07h18** (tour n° 132) : Avance : samedi calme à la résidence (lever 08h35, trois repas room service K026-K028), rapport de 20h00 sans décision (PDF). Nuit 23h29-07h18. Dimanche 25/08 : jour du départ.
> - Tirages du tour : procédure : coucher 00:26, lever 08:35 ; procédure : coucher 23:29, lever 07:18.
> - Tour en cours à 07h18, en attente de William : **Jour du départ : règlement de la résidence avant midi, vol AF703 à 22h15**.
