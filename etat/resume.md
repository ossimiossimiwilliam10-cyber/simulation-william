# Résumé d'état (généré le 29/10/2026 15:10 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : lundi 19/08/2041 10:02 (abidjan, UTC+0)
- **Lieu de William** : Abidjan (Cocody Deux-Plateaux), devant la villa QG des Vallons
- **Heure dans les autres lieux** : lisbonne 11:02 ; luxembourg 12:02 ; mindelo 09:02 ; casablanca 11:02 ; douala 11:02 ; addis 13:02 ; manille 18:02 ; paris 12:02 ; seoul 19:02 ; bresil 07:02
- **En attente de William** :
  - Le gardien de la villa des Vallons attend derrière le portail fermé que William dise qui il vient voir ; rapport final ce soir à 20h00

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **67 982,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **850 390,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €)

## Agenda : dans les 24 heures (0)
- rien
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
> - Hors fiction : audit d'entrée de Claude (U3-19 à U3-21), station météo d'Abidjan, propositions P37 à P41 ; caché : message de Lenny Nguyen le 19/08 vers 19h10 (heure de Luxembourg)
> - Tirages du tour : procédure : LU02, LU04, FR02 ; T24b → arrive (41,95) ; jet « Mohamed Coulibaly se trouve à la villa des Vallons ce lundi  » → NON (72,9) ; T17 Brice → ignore (61,27).
> - Tour en cours à 10h00, en attente de William : **Le gardien de la villa des Vallons reste assis derrière le portail fermé ; rapport final ce soir à 20h00 ; propositions P37 à P41 (univers plus vivant) en attente de l'utilisateur**.
> - **10h00-10h02** (tour n° 107) : William appelle le gardien à travers la grille ; Brice Yao (T17 poli_bref) vient au portail sans l'ouvrir et lui demande qui il vient voir. Hors fiction : P37 à P41 validées par l'utilisateur et installées (monde_social, lenteur, trésorerie, concurrents tirés, courses et FCFA à Abidjan, aléas A01, A04-A06, A37-A39 ; correction U3-23).
> - Tirages du tour : T17 Brice → poli_bref (15,75) ; T22 → zero_segment (31,94) ; T22 → un_segment (62,53) ; T22 → un_segment (60,57) ; T22 → un_segment (75,63).
> - Tour en cours à 10h02, en attente de William : **Le gardien de la villa des Vallons attend derrière le portail fermé que William dise qui il vient voir ; rapport final ce soir à 20h00**.
