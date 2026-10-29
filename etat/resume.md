# Résumé d'état (généré le 29/10/2026 20:17 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : jeudi 22/08/2041 20:00 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 21:00 ; luxembourg 22:00 ; mindelo 19:00 ; casablanca 21:00 ; douala 21:00 ; addis 23:00 ; manille 04:00 ; paris 22:00 ; seoul 05:00 ; bresil 17:00
- **En attente de William** :
  - Décision sur l'acompte de Froid Lagune Services (prolongation du prix ou versement 1 avancé)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **65 299,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **847 707,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €) ; 05/09 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/09 Prêt immobilier de la maison d'Audun-le-Tiche (-628,66 €) ; 05/09 Part nette du bien financé : + capital remboursé (628,66 €) ; 05/09 Assurance habitation (-45,00 €) ; 05/09 Voiture électrique : assurance tous risques (-107,00 €)

## Agenda : dans les 24 heures (1)
- A127 Fri 23/08 10:00 (abidjan) | Viviane Tanoh · Mohamed Coulibaly : Signature du contrat de niveau 2 de Viviane Tanoh à la villa des Vallons (reportée du lundi 19/08 : préavis chez son employeur actuel) [prevu]  — annoncé par Coulibaly le 21/08 17h10
## Agenda : de J+1 à J+7 (5)
- A125 Fri 23/08 23:59 (abidjan) | SOLEIL B2B CI (Mohamed Coulibaly) : Échéance du dépôt de garantie de 5 250 000 FCFA au bailleur (article 6 du bail) [prevu]  — bail signé le 16/08, copie reçue le 21/08 ; à défaut, suspension possible de la remise des lieux
- A111 Sun 25/08 12:00 (abidjan) | Résidence hôtelière (Cocody Deux-Plateaux) : Départ de la résidence et règlement du séjour du 12 au 25 août : 1 690 € (empreinte de la Visa Premier prise à l'arrivée) ; bagages gardés à la réception jusqu'au soir [prevu]  — U3-19 : la résidence n'avait jamais été réglée ; le jour dit : python outils/cartes.py payer --carte visa_premier --montant 1690 --marchand "Résidence hôtelière Deux-Plateaux" --quand "2041-08-25 12:00"
- A112 Sun 25/08 22:15 (abidjan) | Air France : Vol retour AF703 Abidjan (FHB) → Paris-CDG (arrivée le 26/08 vers 05h45), puis correspondance vers Luxembourg-Findel ; billet aller-retour réglé le 27/07 (1 285 €) [prevu]  — U3-19 : le retour n'était pas à l'agenda ; horaire d'après l'AF703 de 2026 (départ vers 22h15, F119) ; quitter la résidence vers 19h00 (trajet et contrôles)
- A128 Mon 26/08 08:00 (abidjan) | William : Première tranche, versement 1 : 20 000 € depuis l'épargne Projet vers SOLEIL B2B CI (SGCI), par S-Net (virement interne puis international) [prevu]  — calendrier validé le 21/08/2041 21h05
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

## Fin du dernier journal (2041-08-22.md, 6 dernières lignes)
> # Jeudi 22 août 2041 — univers 3, 38e jour
> - **00h00-20h00** (tour n° 128) : Pas de consultation. Veille « faute lourde » confiée au conseiller (durable). Contrats : déjà dans les documents (convention de mandat et contrats N2 du 07/08, expédition notariée du 13/08) : courriel à Coulibaly sans objet ; le conseiller corrige son erreur (« maquette seulement »). Pièces : statuts muets sur la révocation, art. 5 indemnité de non-concurrence 1 M
> - Tirages du tour : T7c Mohamed → execute_sans_discuter (17,45) ; T10 Mohamed → immediat (7,98) ; T12 Yannick → temporise (96,19) ; T10 Yannick → dans_l_heure (53,52) ; procédure : vendredi 23/08 15:00 ; T12 Yannick → concede_un_peu (36,61) ; procédure : coucher 23:19, lever 07:41 ; procédure : sans objet.
> - Tour en cours à 20h00, en attente de William : **Décision sur l'acompte de Froid Lagune Services (prolongation du prix ou versement 1 avancé)**.
