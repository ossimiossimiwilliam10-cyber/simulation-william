# Résumé d'état (généré le 29/10/2026 19:55 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : mercredi 21/08/2041 08:49 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 09:49 ; luxembourg 10:49 ; mindelo 07:49 ; casablanca 09:49 ; douala 09:49 ; addis 11:49 ; manille 16:49 ; paris 10:49 ; seoul 17:49 ; bresil 05:49
- **En attente de William** :
  - Réponse de Coulibaly sur la signature de Viviane Tanoh ; dépouillement 16h00 ; rapport 20h00

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **65 299,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **847 707,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €)

## Agenda : dans les 24 heures (2)
- A117 Wed 21/08 16:00 (abidjan) | Mohamed Coulibaly : Dépouillement des devis d'aménagement de la villa des Vallons (prix, délai de livraison des climatiseurs, références) [prevu]  — annoncé le 19/08 (DCE transmis par Coulibaly, P32) ; front H003 (avance par événement) à faire avancer au dépouillement
- A126 Wed 21/08 17:10 (abidjan) | Mohamed Coulibaly : Répond au courriel de l'équipe du projet sur la signature du contrat de Viviane Tanoh [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — T7c execute_sans_discuter, T10 immediat calé sur ses horaires (fin de travail 17h10) : signature reportée, Viviane Tanoh retenue par son employeur actuel (préavis) ; nouvelle date proposée vendredi 23/08 à 10h00 à la villa ; le DGV relaie à William
## Agenda : de J+1 à J+7 (4)
- A121 Thu 22/08 17:00 (abidjan) | Mohamed Coulibaly : Réponse de l'agence de gardiennage (via le bailleur) sur la prolongation du gardiennage de la villa en septembre ; copie du bail promise « dès qu'il repasse à la villa » [prevu]  — promesses du 20/08 09h55 ; T18 si manquement
- A125 Fri 23/08 23:59 (abidjan) | SOLEIL B2B CI (Mohamed Coulibaly) : Échéance du dépôt de garantie de 5 250 000 FCFA au bailleur (article 6 du bail) [prevu]  — bail signé le 16/08, copie reçue le 21/08 ; à défaut, suspension possible de la remise des lieux
- A111 Sun 25/08 12:00 (abidjan) | Résidence hôtelière (Cocody Deux-Plateaux) : Départ de la résidence et règlement du séjour du 12 au 25 août : 1 690 € (empreinte de la Visa Premier prise à l'arrivée) ; bagages gardés à la réception jusqu'au soir [prevu]  — U3-19 : la résidence n'avait jamais été réglée ; le jour dit : python outils/cartes.py payer --carte visa_premier --montant 1690 --marchand "Résidence hôtelière Deux-Plateaux" --quand "2041-08-25 12:00"
- A112 Sun 25/08 22:15 (abidjan) | Air France : Vol retour AF703 Abidjan (FHB) → Paris-CDG (arrivée le 26/08 vers 05h45), puis correspondance vers Luxembourg-Findel ; billet aller-retour réglé le 27/07 (1 285 €) [prevu]  — U3-19 : le retour n'était pas à l'agenda ; horaire d'après l'AF703 de 2026 (départ vers 22h15, F119) ; quitter la résidence vers 19h00 (trajet et contrôles)
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

## Fin du dernier journal (2041-08-21.md, 6 dernières lignes)
> - **06h42-08h41** (tour n° 122) : Petit-déjeuner room service (10,80 €). Coulibaly tient sa promesse (90 %) : copie du bail reçue à 08h41 sur direction@ (D038 dans Gestion ; courriels/2041-08-21_Bail_commercial_Villa_des_Vallons_copie.pdf). Bailleur tiré : Yannick Bamba. Clauses : dépôt de 5 250 000 FCFA au plus tard le 23/08 (agenda), travaux soumis à accord écrit, gardiennage du bailleur jusqu'a
> - Tirages du tour : T7c Mohamed → execute_sans_discuter (32,07) ; T10 Mohamed → immediat (2,42) ; jet « Mohamed Coulibaly tient sa promesse : envoie la copie du bai » → OUI (47,79) ; procédure : 08:41.
> - Tour en cours à 08h41, en attente de William : **Bail reçu (dépôt de garantie dû au plus tard le 23/08) ; dépouillement 16h00 ; rapport 20h00**.
> - **08h41-08h49** (tour n° 123) : Nouveau courriel du DGV à Coulibaly (08h47) sur la signature de Viviane Tanoh. T7c execute_sans_discuter, T10 immediat calé à 17h10 (fin de travail) : réponse cachée A126.
> - Tirages du tour : procédure : 08:41 ; T7c Mohamed → execute_sans_discuter (5,93) ; T10 Mohamed → immediat (7,09).
> - Tour en cours à 08h49, en attente de William : **Réponse de Coulibaly sur la signature de Viviane Tanoh ; dépouillement 16h00 ; rapport 20h00**.
