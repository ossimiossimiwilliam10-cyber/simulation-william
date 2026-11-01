# Résumé d'état (généré le 01/11/2026 11:37 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : dimanche 27/10/2041 09:31 (luxembourg, UTC+1)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 08:31 ; lisbonne 08:31 ; mindelo 07:31 ; casablanca 09:31 ; douala 09:31 ; addis 11:31 ; manille 16:31 ; paris 09:31 ; seoul 17:31 ; bresil 05:31
- **En attente de William** :
  - rien d'urgent ; consignes envoyées à Coulibaly demain 07h00 Abidjan

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **5 613,13 €**
- Compte épargne (Spuerkeess) : **8 273,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **100 735,78 €**
- Part nette de la maison d'Audun-le-Tiche : **99 264,22 €**
- Patrimoine net de William : **789 285,35 €**
- Prévu dans les 14 jours : 31/10 Traitement mensuel de William (9 320,00 €) ; 04/11 Minett Combat Club (-85,00 €) ; 04/11 Package bancaire Zebra Premium (-12,83 €) ; 04/11 Virement permanent vers le compte épargne (-1 487,00 €) ; 04/11 Virement permanent vers le compte épargne (1 487,00 €) ; 04/11 Virement permanent vers SOLEIL B2B CI (-5 000,00 €) ; 05/11 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/11 Prêt immobilier de la maison d'Audun-le-Tiche (-632,34 €) ; 05/11 Part nette du bien financé : + capital remboursé (632,34 €) ; 05/11 Assurance habitation (-45,00 €) ; 05/11 Voiture électrique : assurance tous risques (-107,00 €) ; 07/11 Visa Premier : relevé clos le 30/10/2041, débit du s (-150,00 €)

## Agenda : dans les 24 heures (1)
- A156 Mon 28/10 09:00 (luxembourg) | conseiller → Mohamed Coulibaly : Informer Coulibaly que le financement jusqu'à Pâques est assuré (sans chiffres) [prevu]  — annoncé par le conseiller le 25/10 à 22h02
## Agenda : de J+1 à J+7 (7)
- A168 Mon 28/10 19:00 (luxembourg) | Mariam Brou : Confirmation écrite du prix TTC de l'offre B de gardiennage [prevu]  — consigne du 27/10 transmise le 28/10 07h00
- A157 Tue 29/10 18:00 (luxembourg) | Mariam Brou : Premier tableau de trésorerie sur treize semaines [prevu]  — plan d'action du 26/10/2041
- A164 Wed 30/10 19:00 (luxembourg) | Viviane Tanoh · Éric Koffi Yao : Visite technique de l'entrepôt frigorifique de Port-Bouët [prevu]  — consigne du 27/10 transmise le 28/10 07h00
- A165 Wed 30/10 19:00 (luxembourg) | Mohamed Coulibaly · Mariam Brou : Résiliation du prestataire de gardiennage du bailleur (fin au 30/11), lettre remise contre décharge [prevu]  — consigne du 27/10 transmise le 28/10 07h00
- A166 Thu 31/10 19:00 (luxembourg) | Viviane Tanoh : Relance de l'usine d'emballage de Vridi (garanties, maintenance, délais) [prevu]  — consigne du 27/10 transmise le 28/10 07h00
- A148 Sat 02/11 09:00 (luxembourg) | Olivier Schneider : Élagage de la haie mitoyenne par le paysagiste ; part de William : 143 € [prevu]  — accord du 20/10
- A152 Sat 02/11 19:30 (luxembourg) | Thiago Alves : Dîner chez Thiago Alves (feijoada, gars du club, Lenny) : accepté par William le 25/10 à 21h23 [prevu]  — aléa A30 du 25/10 (invitation reçue à 21h20) ; heure indicative
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

## Fin du dernier journal (2041-10-27.md, 6 dernières lignes)
> # Dimanche 27 octobre 2041 — univers 3, 104e jour
> - **00h00-09h00** (tour n° 174) : 09h00 — Samedi consacré au plan (le tirage « habitué au club samedi » est sans objet : William ne va pas au club, week-end de travail annoncé) ; nuit 22h40-06h50. Séance du 27/10 : bilan, notes (72, 71, 60, 65), trois nouvelles d'Abidjan, note de gardiennage de Mariam (D043, erreur HT/TTC relevée), décision demandée.
> - Tirages du tour : jet « Un habitué du club (Lenny Nguyen) est là le samedi 26/10 ver » → OUI (29,86).
> - Tour en cours à 09h00, en attente de William : **Conseiller : offre B de gardiennage, oui ou non**.
> - **09h00-09h31** (tour n° 175) : 09h31 — Séance : William exige le devis de Port-Bouët ; consignes du conseiller (visite technique au plus tard le 30/10, devis au plus tard le 04/11, veille tarifs MT, option batteries, relance Vridi avant jeudi) ; Lagune : client différent (logisticien) ; gardiennage : offre B au 01/12 (A164-A168).
> - Tour en cours à 09h31, en attente de William : **rien d'urgent ; consignes envoyées à Coulibaly demain 07h00 Abidjan**.
