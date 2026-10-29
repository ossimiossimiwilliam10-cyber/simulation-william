# Résumé d'état (généré le 29/10/2026 19:41 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : mardi 20/08/2041 20:07 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 21:07 ; luxembourg 22:07 ; mindelo 19:07 ; casablanca 21:07 ; douala 21:07 ; addis 23:07 ; manille 04:07 ; paris 22:07 ; seoul 05:07 ; bresil 17:07
- **En attente de William** :
  - Réponse de Coulibaly à la relance (copie du bail, contrat de Viviane Tanoh)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **65 299,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **847 707,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €)

## Agenda : dans les 24 heures (2)
- A123 Wed 21/08 06:01 (abidjan) | Mohamed Coulibaly : Répond au courriel de relance de l'équipe du projet (copie du bail, contrat de Viviane Tanoh) [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — T7c frontal_refus (jet du 20/08 20h06) puis T10 dans_la_journee : refus en deux lignes de transmettre le bail et les contrats à l'adresse de l'équipe du projet (pièces de la société : il ne les envoie qu'à M. Ossimi, direction@soleil-b2b.ci) ; rien sur Viviane Tanoh. Intérêt : sa responsabilité de mandataire face à une adresse non identifiée. Le DGV le rapporte à William.
- A117 Wed 21/08 16:00 (abidjan) | Mohamed Coulibaly : Dépouillement des devis d'aménagement de la villa des Vallons (prix, délai de livraison des climatiseurs, références) [prevu]  — annoncé le 19/08 (DCE transmis par Coulibaly, P32) ; front H003 (avance par événement) à faire avancer au dépouillement
## Agenda : de J+1 à J+7 (3)
- A121 Thu 22/08 17:00 (abidjan) | Mohamed Coulibaly : Réponse de l'agence de gardiennage (via le bailleur) sur la prolongation du gardiennage de la villa en septembre ; copie du bail promise « dès qu'il repasse à la villa » [prevu]  — promesses du 20/08 09h55 ; T18 si manquement
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
> - **11h11-20h00** (tour n° 118) : Avance jusqu'à 20h00 : déjeuner room service (12 000 FCFA, 18,29 €, K019) ; Coulibaly confirme la transmission de la photo (A122, 17h14) ; rapport de 20h00 sans décision (PDF documents_william/2041-08-20_Rapport_quotidien_Directeur_General_virtuel.pdf). Fiche courte du 20/08 : courant 8 268,29 €, épargne 65 299 €, complément CCA de 2 683 € en route, maillot acheté
> - Tirages du tour : T24b → arrive (12,54).
> - Tour en cours à 20h00, en attente de William : **Rien en attente ce soir ; dépouillement des devis demain 16h00 ; rapport final demain 20h00**.
> - **20h00-20h07** (tour n° 119) : William fait relancer Coulibaly par le DGV (courriel 20h06 : copie du bail, contrat de Viviane Tanoh). T7c frontal_refus : réponse cachée le 21/08 à 06h01 (refus de transmettre les pièces à l'adresse de l'équipe du projet, A123 non connu).
> - Tirages du tour : T7c Mohamed → frontal_refus (98,19) ; T10 Mohamed → dans_la_journee (73,65).
> - Tour en cours à 20h07, en attente de William : **Réponse de Coulibaly à la relance (copie du bail, contrat de Viviane Tanoh)**.
