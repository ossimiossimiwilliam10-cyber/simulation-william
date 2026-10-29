# Résumé d'état (généré le 29/10/2026 19:13 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : mardi 20/08/2041 10:06 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 11:06 ; luxembourg 12:06 ; mindelo 09:06 ; casablanca 11:06 ; douala 11:06 ; addis 13:06 ; manille 18:06 ; paris 12:06 ; seoul 19:06 ; bresil 07:06
- **En attente de William** :
  - Choix d'option du règlement (complément ≈ 1,76 M FCFA ou nouvel apport de 7 M FCFA), virement par William sur S-Net ; maillot de Lenny à acheter ; rapport 20h00

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **67 982,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **850 390,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €)

## Agenda : dans les 24 heures (1)
- A122 Tue 20/08 17:14 (abidjan) | Mohamed Coulibaly (WhatsApp) : accuse réception de la photo, transmise à l'agence · souci : contrat de travail qui se termine bientôt · objectif : acheter un logement (ou un plus grand) · foyer : en couple, avec enfants · défauts : mauvais conducteur qui se croit excellent / arrive souvent en retard et s'en excuse à peine [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · T10 : dans_la_journee (jet 69.1, M70, M73) · texte à écrire d'après la fiche (reactions.py jouer) [reaction pour=mohamed-coulibaly canal=whatsapp]
## Agenda : de J+1 à J+7 (5)
- A117 Wed 21/08 16:00 (abidjan) | Mohamed Coulibaly : Dépouillement des devis d'aménagement de la villa des Vallons (prix, délai de livraison des climatiseurs, références) [prevu]  — annoncé le 19/08 (DCE transmis par Coulibaly, P32) ; front H003 (avance par événement) à faire avancer au dépouillement
- A121 Thu 22/08 17:00 (abidjan) | Mohamed Coulibaly : Réponse de l'agence de gardiennage (via le bailleur) sur la prolongation du gardiennage de la villa en septembre ; copie du bail promise « dès qu'il repasse à la villa » [prevu]  — promesses du 20/08 09h55 ; T18 si manquement
- A120 Sun 25/08 10:00 (abidjan) | William : Acheter un maillot des Éléphants pour Lenny Nguyen (taille à recevoir de Lenny) avant le départ [prevu]  — promesse de William du 19/08 20h16
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

## Fin du dernier journal (2041-08-20.md, 6 dernières lignes)
> - **00h00-09h55** (tour n° 114) : Avance rapide : nuit (coucher 00h11, lever 07h51). Lenny donne sa taille (XL, A119). Coulibaly tient sa promesse (90 %) : William inscrit à l'agence de gardiennage, photo demandée ; T7c execute_partiellement sur les demandes du DGV : montant donné (7 M FCFA : dépôt 5,25 M + premier loyer 1,75 M au 01/09), copie du bail non envoyée, prolongation renvoyée à jeudi (A
> - Tirages du tour : jet « Mohamed Coulibaly tient sa promesse : passe à l'agence de ga » → OUI (10,34) ; T7c Mohamed → execute_partiellement (95,98) ; T10 Mohamed → rapide (39,57) ; procédure : coucher 00:11, lever 07:51 ; procédure : 09:55.
> - Tour en cours à 09h55, en attente de William : **Coulibaly demande une photo de William pour le cahier du poste ; annonce 7 M FCFA à régler au bailleur ; copie du bail à venir ; prolongation du gardiennage d'ici jeudi ; rapport final 20h00**.
> - **09h55-10h06** (tour n° 115) : Photo envoyée à Coulibaly (accusé caché à 17h14, A122). William demande au DGV d'enclencher le règlement de 7 M FCFA : le DGV demande l'option (complément ≈ 1,76 M FCFA = 2 683 € ou nouvel apport 7 M = 10 671,46 €, courant 8 268,29 €), virement à faire par William sur S-Net ; copie du bail toujours absente. Maillot : William ira l'acheter après (décision en attent
> - Tirages du tour : jet « Mohamed Coulibaly tient sa promesse : passe à l'agence de ga » → OUI (10,34) ; T7c Mohamed → execute_partiellement (95,98) ; T10 Mohamed → rapide (39,57) ; procédure : coucher 00:11, lever 07:51 ; procédure : 09:55 ; T10 Mohamed → dans_la_journee (69,1).
> - Tour en cours à 10h06, en attente de William : **Choix d'option du règlement (complément ≈ 1,76 M FCFA ou nouvel apport de 7 M FCFA), virement par William sur S-Net ; maillot de Lenny à acheter ; rapport 20h00**.
