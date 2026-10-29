# Résumé d'état (généré le 29/10/2026 20:32 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : vendredi 23/08/2041 23:40 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 00:40 ; luxembourg 01:40 ; mindelo 22:40 ; casablanca 00:40 ; douala 00:40 ; addis 02:40 ; manille 07:40 ; paris 01:40 ; seoul 08:40 ; bresil 20:40
- **En attente de William** :
  - Rien ; départ dimanche 25/08

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **45 299,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **827 707,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €) ; 05/09 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/09 Prêt immobilier de la maison d'Audun-le-Tiche (-628,66 €) ; 05/09 Part nette du bien financé : + capital remboursé (628,66 €) ; 05/09 Assurance habitation (-45,00 €) ; 05/09 Voiture électrique : assurance tous risques (-107,00 €)

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (3)
- A111 Sun 25/08 12:00 (abidjan) | Résidence hôtelière (Cocody Deux-Plateaux) : Départ de la résidence et règlement du séjour du 12 au 25 août : 1 690 € (empreinte de la Visa Premier prise à l'arrivée) ; bagages gardés à la réception jusqu'au soir [prevu]  — U3-19 : la résidence n'avait jamais été réglée ; le jour dit : python outils/cartes.py payer --carte visa_premier --montant 1690 --marchand "Résidence hôtelière Deux-Plateaux" --quand "2041-08-25 12:00"
- A112 Sun 25/08 22:15 (abidjan) | Air France : Vol retour AF703 Abidjan (FHB) → Paris-CDG (arrivée le 26/08 vers 05h45), puis correspondance vers Luxembourg-Findel ; billet aller-retour réglé le 27/07 (1 285 €) [prevu]  — U3-19 : le retour n'était pas à l'agenda ; horaire d'après l'AF703 de 2026 (départ vers 22h15, F119) ; quitter la résidence vers 19h00 (trajet et contrôles)
- A121 Mon 26/08 17:00 (abidjan) | Mohamed Coulibaly : Réponse de l'agence de gardiennage (via le bailleur) sur la prolongation du gardiennage de la villa en septembre ; copie du bail promise « dès qu'il repasse à la villa » [prevu]  — promesses du 20/08 09h55 ; T18 si manquement | reporté de 2041-08-22 17:00 : T12 temporise : le bailleur veut en parler en début de semaine prochaine (courrier de l'agence du 22/08) ; copie du bail déjà reçue le 21/08
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

## Fin du dernier journal (2041-08-23.md, 6 dernières lignes)
> # Vendredi 23 août 2041 — univers 3, 39e jour
> - **00h00-20h00** (tour n° 130) : Nuit 23h26-07h42. A131 : Coulibaly sur les niveaux 3 et 4 (aucune fiche, entretiens semaine du 02/09). Viviane Tanoh signe à 10h20 (fiabilité 91 % : oui ; D041, 1 600 000 FCFA nets, 01/10). Complément crédité à 15h00 (A130) ; Coulibaly paie le dépôt de garantie à 15h42 (fiabilité 90 % : oui), reçu attendu. Repas room service. Rapport de 20h00 sans décision.
> - Tirages du tour : T7c Mohamed → execute_sans_discuter (20,47) ; T10 Mohamed → le_soir_ou_lendemain (84,89) ; jet « Viviane Tanoh tient sa promesse : signe son contrat de nivea » → OUI (37,07) ; jet « Mohamed Coulibaly tient sa promesse : paie le dépôt de garan » → OUI (4,26) ; procédure : coucher 23:26, lever 07:42.
> - Tour en cours à 20h00, en attente de William : **Rien ce soir ; départ dimanche 25/08**.
> - **20h00-23h40** (tour n° 131) : Soirée : William refait l'application Gestion (version 3.0 à 23h30) : écran simple par défaut (conseiller, situation financière de la société, derniers documents, à venir) avec liens vers Messages (conversation du conseiller), Banque, Fichiers et Calendrier ; anciens onglets sous « Toutes les options ». Hors fiction : gestion.py (finances_societe, a_venir, version
> - Tour en cours à 23h40, en attente de William : **Rien ; départ dimanche 25/08**.
