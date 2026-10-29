# Résumé d'état (généré le 29/10/2026 19:02 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : lundi 19/08/2041 20:17 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière
- **Heure dans les autres lieux** : lisbonne 21:17 ; luxembourg 22:17 ; mindelo 19:17 ; casablanca 21:17 ; douala 21:17 ; addis 23:17 ; manille 04:17 ; paris 22:17 ; seoul 05:17 ; bresil 17:17
- **En attente de William** :
  - Taille de maillot attendue de Lenny Nguyen ; rapport final demain 20h00

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **67 982,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **850 390,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €)

## Agenda : dans les 24 heures (2)
- A119 Tue 20/08 05:21 (abidjan) | Lenny Nguyen (WhatsApp) : donne sa taille de maillot · souci : dettes de jeu · objectif : rembourser ses dettes · foyer : vit seul(e) · défauts : rigide sur les horaires et les règles, au point d'agacer / exagère ses histoires jusqu'au mensonge [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · T10 : dans_la_journee (jet 74.2) · texte à écrire d'après la fiche (reactions.py jouer) [reaction pour=lenny-nguyen canal=whatsapp]
- A114 Tue 20/08 09:00 (abidjan) | Mohamed Coulibaly : Passe à l'agence de gardiennage du bailleur pour inscrire William sur la liste des personnes autorisées à la villa des Vallons (promesse du 19/08, 12h25) [prevu]  — promesse : lenteur.py promesse --pour "Mohamed Coulibaly" au moment dit (oubli 10 %), puis T18 si manquement
## Agenda : de J+1 à J+7 (4)
- A117 Wed 21/08 16:00 (abidjan) | Mohamed Coulibaly : Dépouillement des devis d'aménagement de la villa des Vallons (prix, délai de livraison des climatiseurs, références) [prevu]  — annoncé le 19/08 (DCE transmis par Coulibaly, P32) ; front H003 (avance par événement) à faire avancer au dépouillement
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
- AUJOURD'HUI lundi : revue du lundi (audit_jets.py, tirage_aleas.py, vie hors de la scène principale, monde, idées)
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-08-19.md, 6 dernières lignes)
> - **20h00-20h10** (tour n° 112) : William valide les deux décisions du rapport (courriel du DGV à Coulibaly à 20h08 : copie du bail et montant exact ; prolongation du gardiennage). Message à Lenny (félicitations, projet en Côte d'Ivoire ; savoir : Lenny l'apprend) ; réponse immédiate de Lenny (A118).
> - Tirages du tour : T10 Lenny → immediat (2,0).
> - Tour en cours à 20h10, en attente de William : **Lenny Nguyen demande si William monte une boîte en Côte d'Ivoire ; suivi des demandes à Coulibaly au rapport de demain 20h00**.
> - **20h10-20h17** (tour n° 113) : William promet un maillot des Éléphants à Lenny (A120, avant le départ) et le rassure sur la boîte ; Lenny répondra demain à 07h21 heure de Luxembourg (A119, T10 dans_la_journee). William décide d'oublier Fatoumata Gnagne : retirée des quêtes secondaires (décision du joueur, 19/08 20h17).
> - Tirages du tour : T10 Lenny → immediat (2,0) ; T10 Lenny → dans_la_journee (74,18).
> - Tour en cours à 20h17, en attente de William : **Taille de maillot attendue de Lenny Nguyen ; rapport final demain 20h00**.
