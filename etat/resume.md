# Résumé d'état (généré le 31/10/2026 23:56 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : mardi 22/10/2041 10:06 (luxembourg, UTC+2)
- **Lieu de William** : Luxembourg-Ville, lycée, salle des professeurs
- **Heure dans les autres lieux** : abidjan 08:06 ; lisbonne 09:06 ; mindelo 07:06 ; casablanca 09:06 ; douala 09:06 ; addis 11:06 ; manille 16:06 ; paris 10:06 ; seoul 17:06 ; bresil 05:06
- **En attente de William** :
  - rien d'urgent ; compte rendu de Coulibaly à 17h00

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **5 613,13 €**
- Compte épargne (Spuerkeess) : **8 273,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **100 735,78 €**
- Part nette de la maison d'Audun-le-Tiche : **99 264,22 €**
- Patrimoine net de William : **789 285,35 €**
- Prévu dans les 14 jours : 31/10 Traitement mensuel de William (9 320,00 €) ; 04/11 Minett Combat Club (-85,00 €) ; 04/11 Package bancaire Zebra Premium (-12,83 €) ; 04/11 Virement permanent vers le compte épargne (-1 487,00 €) ; 04/11 Virement permanent vers le compte épargne (1 487,00 €) ; 04/11 Virement permanent vers SOLEIL B2B CI (-5 000,00 €) ; 05/11 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/11 Prêt immobilier de la maison d'Audun-le-Tiche (-632,34 €) ; 05/11 Part nette du bien financé : + capital remboursé (632,34 €) ; 05/11 Assurance habitation (-45,00 €) ; 05/11 Voiture électrique : assurance tous risques (-107,00 €)

## ÉCHÉANCES ÉCHUES NON CLOSES (jouer, reporter avec raison ou annuler : règle 14)
- A142 Tue 08/10 19:00 (luxembourg) | Mohamed Coulibaly : Point écrit sur le rendez-vous manqué de Vridi (demande de William du 06/10) [prevu]  — à lier au compte rendu du mardi ; fiabilité de Coulibaly au moment dit

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (2)
- A143 Thu 24/10 19:00 (luxembourg) | Mariam Brou : Synthèse des trois offres de gardiennage (report du 20/10) [prevu]  — T18 report_excuse ; contrat du bailleur jusqu'au 31/10
- A146 Sat 26/10 10:00 (luxembourg) | William : Réserver les billets pour Abidjan, séjour du samedi 21 décembre au samedi 4 janvier (avant : « samedi 3 janvier », erreur du conseiller corrigée le 21/10 : le 3 janvier 2042 est un vendredi) [prevu]  — engagement de William du 20/10 (estimation 1 600 à 2 000 €)
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

## Fin du dernier journal (2041-10-22.md, 6 dernières lignes)
> - **00h00-10h01** (tour n° 157) : 10h01 — Tour 156 annulé (U3-27) ; reprise : lundi 21 (message correctif du conseiller 07h10, orage, club 18h30), mardi 22 : Kim Schmitz (physique) apparaît en salle des professeurs et demande à William s'il a monté une affaire en Afrique (Sam Ries en a parlé, P47 : en parle à d'autres) ; arrêt sur sa question.
> - Tirages du tour : procédure : 20/10 21:50-06:05 ; 21/10 22:10-06:02 ; 22/10 21:54-06:00 ; 23/10 22:04-06:05 ; 24/10 21:53-06:01 ; 26/10 01:32-08:27 ; procédure : LU01, LU03, FR01.
> - Tour en cours à 10h01, en attente de William : **Kim Schmitz attend la réponse de William (affaire en Afrique)**.
> - **10h01-10h06** (tour n° 158) : 10h06 — P60 à P62 validées et installées ; revue désormais mensuelle (premier lundi du mois). William confirme à Kim Schmitz son affaire, dit chercher des investisseurs et propose en riant un voyage ; T15 garde_distance : elle esquive poliment et part préparer son TP.
> - Tirages du tour : T15 Kim → garde_distance (56,65).
> - Tour en cours à 10h06, en attente de William : **rien d'urgent ; compte rendu de Coulibaly à 17h00**.
