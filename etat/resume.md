# Résumé d'état (généré le 01/11/2026 11:05 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : samedi 26/10/2041 08:35 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 06:35 ; lisbonne 07:35 ; mindelo 05:35 ; casablanca 07:35 ; douala 07:35 ; addis 09:35 ; manille 14:35 ; paris 08:35 ; seoul 15:35 ; bresil 03:35
- **En attente de William** :
  - Conseiller : William doit exposer son nouveau système

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **5 613,13 €**
- Compte épargne (Spuerkeess) : **8 273,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **100 735,78 €**
- Part nette de la maison d'Audun-le-Tiche : **99 264,22 €**
- Patrimoine net de William : **789 285,35 €**
- Prévu dans les 14 jours : 31/10 Traitement mensuel de William (9 320,00 €) ; 04/11 Minett Combat Club (-85,00 €) ; 04/11 Package bancaire Zebra Premium (-12,83 €) ; 04/11 Virement permanent vers le compte épargne (-1 487,00 €) ; 04/11 Virement permanent vers le compte épargne (1 487,00 €) ; 04/11 Virement permanent vers SOLEIL B2B CI (-5 000,00 €) ; 05/11 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/11 Prêt immobilier de la maison d'Audun-le-Tiche (-632,34 €) ; 05/11 Part nette du bien financé : + capital remboursé (632,34 €) ; 05/11 Assurance habitation (-45,00 €) ; 05/11 Voiture électrique : assurance tous risques (-107,00 €)

## ÉCHÉANCES ÉCHUES NON CLOSES (jouer, reporter avec raison ou annuler : règle 14)
- A143 Thu 24/10 19:00 (luxembourg) | Mariam Brou : Synthèse des trois offres de gardiennage (report du 20/10) [prevu]  — T18 report_excuse ; contrat du bailleur jusqu'au 31/10

## Agenda : dans les 24 heures (1)
- A153 Sat 26/10 09:12 (luxembourg) | Thiago Alves : Répond au oui de William (adresse et heure du dîner du 2/11) [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — T10 dans_la_journee (tiré le 25/10), décalé au réveil (routines)
## Agenda : de J+1 à J+7 (1)
- A156 Mon 28/10 09:00 (luxembourg) | conseiller → Mohamed Coulibaly : Informer Coulibaly que le financement jusqu'à Pâques est assuré (sans chiffres) [prevu]  — annoncé par le conseiller le 25/10 à 22h02
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 15 informé(s) hors William ; fuite interne 40 %, externe 15 %
- affaire_projet_ci_art14 : 2 informé(s) hors William ; fuite interne 6 %, externe 2 %

## Fêtes et fériés dans les 30 jours
- ven 01/11/2041 FR Toussaint
- ven 01/11/2041 LU Toussaint
- lun 11/11/2041 FR Armistice 1918

## Routine du tour
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-10-26.md, 6 dernières lignes)
> # Samedi 26 octobre 2041 — univers 3, 103e jour
> - **00h00-08h35** (tour n° 171) : 08h35 — Règle de financement adoptée (A147 close, A154, A155, A156 ; EVAL003 71/100) ; nuit perturbée par la fête du voisin de droite jusqu'à 01h00 (aléa A24) ; samedi 26, William s'installe pour travailler avec le conseiller.
> - Tour en cours à 08h35, en attente de William : **Conseiller : William doit exposer son nouveau système**.
