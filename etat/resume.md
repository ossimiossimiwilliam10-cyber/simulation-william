# Résumé d'état (généré le 29/10/2026 20:48 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 25/08/2041 15:47 (abidjan, UTC+0)
- **Lieu de William** : Abidjan, aéroport Félix-Houphouët-Boigny (hall des départs)
- **Heure dans les autres lieux** : lisbonne 16:47 ; luxembourg 17:47 ; mindelo 14:47 ; casablanca 15:47 ; douala 16:47 ; addis 18:47 ; manille 23:47 ; paris 17:47 ; seoul 00:47 ; bresil 12:47
- **En attente de William** :
  - Choix des leviers de trésorerie ; enregistrement du vol AF703 en soirée

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **8 268,29 €**
- Compte épargne (Spuerkeess) : **45 299,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **101 994,94 €**
- Part nette de la maison d'Audun-le-Tiche : **98 005,06 €**
- Patrimoine net de William : **827 707,35 €**
- Prévu dans les 14 jours : 30/08 Traitement mensuel de William (9 320,00 €) ; 02/09 Minett Combat Club (-85,00 €) ; 02/09 Package bancaire Zebra Premium (-12,83 €) ; 02/09 Virement permanent vers le compte épargne (-732,00 €) ; 02/09 Virement permanent vers le compte épargne (732,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (-5 755,00 €) ; 02/09 Virement permanent vers le compte-titres ETF (5 755,00 €) ; 05/09 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/09 Prêt immobilier de la maison d'Audun-le-Tiche (-628,66 €) ; 05/09 Part nette du bien financé : + capital remboursé (628,66 €) ; 05/09 Assurance habitation (-45,00 €) ; 05/09 Voiture électrique : assurance tous risques (-107,00 €)

## Agenda : dans les 24 heures (1)
- A112 Sun 25/08 22:15 (abidjan) | Air France : Vol retour AF703 Abidjan (FHB) → Paris-CDG (arrivée le 26/08 vers 05h45), puis correspondance vers Luxembourg-Findel ; billet aller-retour réglé le 27/07 (1 285 €) [prevu]  — U3-19 : le retour n'était pas à l'agenda ; horaire d'après l'AF703 de 2026 (départ vers 22h15, F119) ; quitter la résidence vers 19h00 (trajet et contrôles)
## Agenda : de J+1 à J+7 (3)
- A121 Mon 26/08 17:00 (abidjan) | Mohamed Coulibaly : Réponse de l'agence de gardiennage (via le bailleur) sur la prolongation du gardiennage de la villa en septembre ; copie du bail promise « dès qu'il repasse à la villa » [prevu]  — promesses du 20/08 09h55 ; T18 si manquement | reporté de 2041-08-22 17:00 : T12 temporise : le bailleur veut en parler en début de semaine prochaine (courrier de l'agence du 22/08) ; copie du bail déjà reçue le 21/08
- A132 Wed 28/08 17:00 (abidjan) | Mohamed Coulibaly : Confirme seul Froid Lagune Services et verse l'acompte de 2 768 000 FCFA dès le crédit du versement de 20 000 € (prix garanti jusqu'au 28/08) [prevu]  — décision de William, séance du 25/08
- A133 Fri 30/08 17:00 (abidjan) | Mohamed Coulibaly : Dépose lui-même les demandes d'abonnement CIE et SODECI de la villa (Mariam Brou n'arrive que le 1er octobre) [prevu]  — décision de William, séance du 25/08 ; fait avancer le front H002 quand c'est fait
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 13 informé(s) hors William ; fuite interne 39 %, externe 13 %
- affaire_projet_ci_art14 : 1 informé(s) hors William ; fuite interne 3 %, externe 1 %

## Fêtes et fériés dans les 30 jours
- mer 28/08/2041 -- ≈ début du Ramadan

## Routine du tour
- lendemain = lundi : revue du lundi à présenter AVANT le reste (CLAUDE.md §12) ; dimanche soir : T4/T5 (savoir.py t5) et synthèse de semaine
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-08-25.md, 6 dernières lignes)
> - Tour en cours à 07h18, en attente de William : **Jour du départ : règlement de la résidence avant midi, vol AF703 à 22h15**.
> - **07h18-15h00** (tour n° 133) : Nouvelle règle de William (07h38) : rapport de 20h00 archivé et non envoyé ; séance de travail le dimanche ; urgences seulement (CLAUDE §14, préférences, mémoire). Résidence réglée à 12h05 : 1 720,06 € Visa Premier (K029 : séjour 1 690 € + 19 716 FCFA d'extras ; A111 clos, fil 8 clos). Yango vers l'aéroport (T24b annule, puis Daniel Öztürk, tiré). Arrivée au termi
> - Tirages du tour : T24b → annule (98,49) ; procédure : après 4 min.
> - Tour en cours à 15h00, en attente de William : **Séance du dimanche avec le conseiller : trois décisions (gardiennage, CIE-SODECI, Froid Lagune) ; vol AF703 22h15**.
> - **15h00-15h47** (tour n° 134) : Séance du dimanche : trois décisions (prolonger le gardiennage du bailleur, prix à obtenir ; CIE-SODECI à la charge de Coulibaly cette semaine, A133 ; Coulibaly confirme seul Froid Lagune, A132) envoyées à 15h10. Analyse de trésorerie (PDF documents_william/2041-08-25_Analyse_Tresorerie_Soleil_B2B_CI.pdf) : charge fixe ≈ 17 200 €/mois (coût employeur ≈ 1,4 × net, 
> - Tour en cours à 15h47, en attente de William : **Choix des leviers de trésorerie ; enregistrement du vol AF703 en soirée**.
