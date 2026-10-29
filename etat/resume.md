# Résumé d'état (généré le 29/10/2026 20:06 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : mercredi 21/08/2041 21:00 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 22:00 ; luxembourg 23:00 ; mindelo 20:00 ; casablanca 22:00 ; douala 22:00 ; addis 00:00 ; manille 05:00 ; paris 23:00 ; seoul 06:00 ; bresil 18:00
- **En attente de William** :
  - Validation du calendrier de la première tranche (20 000 € le 26/08, 40 000 € le 25/09)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **65 299,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **847 707,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €)

## Agenda : dans les 24 heures (1)
- A121 Thu 22/08 17:00 (abidjan) | Mohamed Coulibaly : Réponse de l'agence de gardiennage (via le bailleur) sur la prolongation du gardiennage de la villa en septembre ; copie du bail promise « dès qu'il repasse à la villa » [prevu]  — promesses du 20/08 09h55 ; T18 si manquement
## Agenda : de J+1 à J+7 (4)
- A127 Fri 23/08 10:00 (abidjan) | Viviane Tanoh · Mohamed Coulibaly : Signature du contrat de niveau 2 de Viviane Tanoh à la villa des Vallons (reportée du lundi 19/08 : préavis chez son employeur actuel) [prevu]  — annoncé par Coulibaly le 21/08 17h10
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
> - **08h57-20h00** (tour n° 125) : Signature « William Ossimi » choisie. Déjeuner room service (19,06 €). Coulibaly (A126, 17h10) : signature de Viviane Tanoh reportée au 23/08 10h00 (préavis), A127. Dépouillement (A117) : compte rendu à 17h23 (D039, PDF courriels) : Froid Lagune Services 6,92 M FCFA proposé, accord écrit du bailleur non demandé (art. 7) ; front H003 palier 1. Rapport de 20h00 : de
> - Tirages du tour : T10 Mohamed → immediat (3,38).
> - Tour en cours à 20h00, en attente de William : **Deux décisions du rapport de 20h00 (accord écrit du bailleur avant commande ; calendrier de la première tranche)**.
> - **20h00-21h00** (tour n° 126) : Remarque de William : Coulibaly n'avait pas signalé lundi la non-signature de Viviane Tanoh (vérifié : rien lundi) ; notée dans l'évaluation du DG réel. Règle durable : le conseiller d'abord (préférences + CLAUDE §14). Décision 1 : courriel à Coulibaly 20h15 (aucune commande avant accord écrit du bailleur) ; T7c execute_a_contrecoeur : accusé à 20h58, prix de Froi
> - Tirages du tour : T7c Mohamed → execute_a_contrecoeur (75,18) ; T10 Mohamed → dans_l_heure (65,45).
> - Tour en cours à 21h00, en attente de William : **Validation du calendrier de la première tranche (20 000 € le 26/08, 40 000 € le 25/09)**.
