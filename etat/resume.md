# Résumé d'état (généré le 28/10/2026 12:56 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 11/08/2041 21:30 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez toi
- **Heure dans les autres lieux** : abidjan 19:30 ; lisbonne 20:30 ; mindelo 18:30 ; casablanca 20:30 ; douala 20:30 ; addis 22:30 ; manille 03:30 ; paris 21:30 ; seoul 04:30 ; bresil 16:30
- **En attente de William** :
  - Validation du depart matinal pour Findel (reveil 04h15, vol AF1233 a 06h50, atterrissage Abidjan 18h25)

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 740,59 €**
- Compte épargne (Spuerkeess) : **75 982,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **858 862,65 €**
- Prévu dans les 14 jours : 12/08 Électricité (-132,00 €) ; 12/08 Gaz naturel (-253,00 €) ; 16/08 Box internet fibre et forfait mobile (-63,00 €) ; 16/08 Abonnement à l'agent IA de William (-24,30 €)

## Agenda : dans les 24 heures (2)
- A101 Mon 12/08 06:00 (luxembourg) | Air France : Départ mission Abidjan vol AF702 via Paris CDG (arrivée 18h10 FHB) [prevu]  — Mission Abidjan du 12 au 25 août 2041
- A003 Mon 12/08 (sans heure) (luxembourg) | Minett Combat Club : Fermeture estivale du club du lundi 12/08 au dimanche 25/08/2041 · reprise le lundi 26/08 [prevu]  — fermeture annuelle estivale habituelle de deux semaines
## Agenda : de J+1 à J+7 (1)
- A102 Tue 13/08 12:00 (luxembourg) | Cabinet Me Ismaël Gnamien : Séance solennelle de signature des statuts SASU et convention mandat DG avec Mohamed Coulibaly [prevu]  — Signature des 5 originaux sous chemise notariale et dépôt CEPICI pour immatriculation RCCM
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 13 informé(s) hors William ; fuite interne 39 %, externe 13 %
- affaire_projet_ci_art14 : 1 informé(s) hors William ; fuite interne 3 %, externe 1 %

## Fêtes et fériés dans les 30 jours
- jeu 15/08/2041 FR Assomption
- jeu 15/08/2041 LU Assomption
- mer 28/08/2041 -- ≈ début du Ramadan

## Routine du tour
- lendemain = lundi : revue du lundi à présenter AVANT le reste (CLAUDE.md §12) ; dimanche soir : T4/T5 (savoir.py t5) et synthèse de semaine
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-08-11.md, 6 dernières lignes)
> # Dimanche 11 août 2041 — univers 3, 27e jour
> - **00h00-21h30** (tour n° 78) : voir le texte exact du tour (journal/tours/).
> - Tour en cours à 21h30, en attente de William : **Validation du depart matinal pour Findel (reveil 04h15, vol AF1233 a 06h50, atterrissage Abidjan 18h25)**.
