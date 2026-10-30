# Résumé d'état (généré le 30/10/2026 19:07 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 20/10/2041 09:00 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 07:00 ; lisbonne 08:00 ; mindelo 06:00 ; casablanca 08:00 ; douala 08:00 ; addis 10:00 ; manille 15:00 ; paris 09:00 ; seoul 16:00 ; bresil 04:00
- **En attente de William** :
  - Séance du dimanche : gardiennage de novembre, consultation du régulateur ; haie du voisin ; programme de la semaine du 21 octobre ; P57-P59

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **5 613,13 €**
- Compte épargne (Spuerkeess) : **8 273,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **100 735,78 €**
- Part nette de la maison d'Audun-le-Tiche : **99 264,22 €**
- Patrimoine net de William : **789 285,35 €**
- Prévu dans les 14 jours : 31/10 Traitement mensuel de William (9 320,00 €)

## ÉCHÉANCES ÉCHUES NON CLOSES (jouer, reporter avec raison ou annuler : règle 14)
- A142 Tue 08/10 19:00 (luxembourg) | Mohamed Coulibaly : Point écrit sur le rendez-vous manqué de Vridi (demande de William du 06/10) [prevu]  — à lier au compte rendu du mardi ; fiabilité de Coulibaly au moment dit

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (1)
- A143 Thu 24/10 19:00 (luxembourg) | Mariam Brou : Synthèse des trois offres de gardiennage (report du 20/10) [prevu]  — T18 report_excuse ; contrat du bailleur jusqu'au 31/10
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 15 informé(s) hors William ; fuite interne 40 %, externe 15 %
- affaire_projet_ci_art14 : 2 informé(s) hors William ; fuite interne 6 %, externe 2 %

## Fêtes et fériés dans les 30 jours
- ven 01/11/2041 FR Toussaint
- ven 01/11/2041 LU Toussaint
- lun 11/11/2041 FR Armistice 1918

## Routine du tour
- lendemain = lundi : revue du lundi à présenter AVANT le reste (CLAUDE.md §12) ; dimanche soir : T4/T5 (savoir.py t5) et synthèse de semaine
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-10-20.md, 6 dernières lignes)
> # Dimanche 20 octobre 2041 — univers 3, 97e jour
> - **00h00-09h00** (tour n° 152) : Consignes du 13/10 : Viviane (T7c à contrecœur) envoie l'offre de Vridi vendredi ; Coulibaly fixe les objectifs (sans discuter) ; rappel (à contrecœur, « Bien noté »), comptes rendus à l'heure. P54-P56 installées (A43, objectifs mensuels A144, bulletin). Rituels du 14/10 : revue n° 11 (P57-P59), aléas A04, A23, A24 (Olivier Schneider, haie 143 €), A26 (cagnotte 20
> - Tirages du tour : procédure : LU03, LU04, FR01 ; T22 → zero_segment (43,33) ; T22 → zero_segment (42,28) ; T22 → zero_segment (10,12) ; T15 Sam → rien_laisse_passer (22,62) ; T7c Viviane → execute_a_contrecoeur (87,71) ; T7c Mohamed → execute_sans_discuter (8,59) ; T7c Mohamed → execute_a_contrecoeur (86,57) ; jet « Mohamed Coulibaly tient sa promesse : envoie son compte rend » → OUI (56,54) ; j
> - Tour en cours à 09h00, en attente de William : **Séance du dimanche : gardiennage de novembre, consultation du régulateur ; haie du voisin ; programme de la semaine du 21 octobre ; P57-P59**.
