# Résumé d'état (généré le 29/10/2026 15:31 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : lundi 19/08/2041 18:07 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), résidence hôtelière (chambre, réveil de la sieste)
- **Heure dans les autres lieux** : lisbonne 19:07 ; luxembourg 20:07 ; mindelo 17:07 ; casablanca 19:07 ; douala 19:07 ; addis 21:07 ; manille 02:07 ; paris 20:07 ; seoul 03:07 ; bresil 15:07
- **En attente de William** :
  - Message de Coulibaly (12h25 : gardien du bailleur, inscription demain matin) ; message de Lenny Nguyen (17h10 : retour au club) ; rapport final ce soir à 20h00

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **67 982,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **850 390,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €)

## Agenda : dans les 24 heures (1)
- A114 Tue 20/08 09:00 (abidjan) | Mohamed Coulibaly : Passe à l'agence de gardiennage du bailleur pour inscrire William sur la liste des personnes autorisées à la villa des Vallons (promesse du 19/08, 12h25) [prevu]  — promesse : lenteur.py promesse --pour "Mohamed Coulibaly" au moment dit (oubli 10 %), puis T18 si manquement
## Agenda : de J+1 à J+7 (2)
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
> - **10h05-10h17** (tour n° 109) : William félicite le gardien (T17 ignore : à peine un « mm ») et rentre en Yango commandé par la réception (T24b arrive ; Wilfried Boni, tiré ; 1 279 FCFA sur la note). Message au directeur général virtuel : informer Coulibaly, intermédiaires qui ne le connaissent pas ; courriel du projet à Coulibaly à 10h11 (accès, liste des personnes autorisées, clés, qui paie le
> - Tirages du tour : T17 Brice → ignore (52,6) ; T24b → arrive (33,37).
> - Tour en cours à 10h17, en attente de William : **Mohamed Coulibaly n'a pas répondu (courriel du directeur général virtuel à 10h11) ; rapport final ce soir à 20h00**.
> - **10h17-18h07** (tour n° 110) : Séance de 2 h au club du Sofitel Hôtel Ivoire (pass journée 61 €, Visa Premier, K016) ; aller en Yango (T24b arrive, Hervé Ouattara, 3 028 FCFA), retour (T24b annule puis Yannick Kouamé, 2 825 FCFA), sur la note. Rappel de Coulibaly à 12h22 manqué (téléphone au casier), WhatsApp 12h25 (T7c execute_a_contrecoeur : gardien de la société du bailleur jusqu'à fin août,
> - Tirages du tour : T24b → arrive (24,66) ; T24b → annule (93,55) ; T7c Mohamed → execute_a_contrecoeur (79,78) ; procédure : après 4 min ; procédure : endormi 14:12, réveil 18:07 (235 min).
> - Tour en cours à 18h07, en attente de William : **Message de Coulibaly (12h25 : gardien du bailleur, inscription demain matin) ; message de Lenny Nguyen (17h10 : retour au club) ; rapport final ce soir à 20h00**.
