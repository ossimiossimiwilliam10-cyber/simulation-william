# Résumé d'état (généré le 01/11/2026 10:39 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : vendredi 25/10/2041 21:54 (luxembourg, UTC+2)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 19:54 ; lisbonne 20:54 ; mindelo 18:54 ; casablanca 20:54 ; douala 20:54 ; addis 22:54 ; manille 03:54 ; paris 21:54 ; seoul 04:54 ; bresil 16:54
- **En attente de William** :
  - Conseiller : plafond (165 000 € nets ou moins) et premier versement de survie début décembre

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
## Agenda : de J+1 à J+7 (0)
- rien
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

## Fin du dernier journal (2041-10-25.md, 6 dernières lignes)
> - Tour en cours à 21h20, en attente de William : **Thiago Alves : dîner du samedi 2 novembre**.
> - **21h20-21h36** (tour n° 169) : 21h36 — Oui à Thiago (dîner du 2/11, A152 ; sa réponse tirée pour demain 09h12, A153). William soumet au conseiller l'idée d'injecter une partie de l'ETF après un premier contrat ; analyse chiffrée (survie ~65 k€ jusqu'à Pâques, BFR Vridi ~62 k€, Port-Bouët ~99 k€, PFU 31,4 %, avance sur marché SGCI, trois règles).
> - Tirages du tour : T10 Thiago → dans_la_journee (57,57).
> - Tour en cours à 21h36, en attente de William : **Conseiller : prix de revient de l'ETF ; tableau pour dimanche**.
> - **21h36-21h54** (tour n° 170) : 21h54 — William envoie son prix de revient (538 243 €) ; recommandation du conseiller (survie 65 k€ au fil du besoin, contrat 100 k€ sous trois conditions, plafond 165 k€ nets, butoir 31/03/2042). Aléa A24 commencé : musique chez le voisin de droite.
> - Tour en cours à 21h54, en attente de William : **Conseiller : plafond (165 000 € nets ou moins) et premier versement de survie début décembre**.
