# Résumé d'état (généré le 01/11/2026 12:20 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : lundi 28/10/2041 20:15 (luxembourg, UTC+1)
- **Lieu de William** : Audun-le-Tiche (Moselle), chez William
- **Heure dans les autres lieux** : abidjan 19:15 ; lisbonne 19:15 ; mindelo 18:15 ; casablanca 20:15 ; douala 20:15 ; addis 22:15 ; manille 03:15 ; paris 20:15 ; seoul 04:15 ; bresil 16:15
- **En attente de William** :
  - rien d'urgent

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **5 613,13 €**
- Compte épargne (Spuerkeess) : **8 273,00 €**
- ETF (valeur de marché : calages seulement) : **676 135,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **100 735,78 €**
- Part nette de la maison d'Audun-le-Tiche : **99 264,22 €**
- Patrimoine net de William : **789 285,35 €**
- Prévu dans les 14 jours : 31/10 Traitement mensuel de William (9 320,00 €) ; 04/11 Minett Combat Club (-85,00 €) ; 04/11 Package bancaire Zebra Premium (-12,83 €) ; 04/11 Virement permanent vers le compte épargne (-1 487,00 €) ; 04/11 Virement permanent vers le compte épargne (1 487,00 €) ; 04/11 Virement permanent vers SOLEIL B2B CI (-5 000,00 €) ; 05/11 Mensualité du prêt immobilier et assurance emprunteu (-949,28 €) ; 05/11 Prêt immobilier de la maison d'Audun-le-Tiche (-632,34 €) ; 05/11 Part nette du bien financé : + capital remboursé (632,34 €) ; 05/11 Assurance habitation (-45,00 €) ; 05/11 Voiture électrique : assurance tous risques (-107,00 €) ; 07/11 Visa Premier : relevé clos le 30/10/2041, débit du s (-150,00 €) ; 11/11 Électricité (-132,00 €) ; 11/11 Gaz naturel (-253,00 €)

## ÉCHÉANCES ÉCHUES NON CLOSES (jouer, reporter avec raison ou annuler : règle 14)
- A168 Mon 28/10 19:00 (luxembourg) | Mariam Brou : Confirmation écrite du prix TTC de l'offre B de gardiennage [prevu]  — consigne du 27/10 transmise le 28/10 07h00

## Agenda : dans les 24 heures (0)
- rien
## Agenda : de J+1 à J+7 (7)
- A165 Wed 30/10 19:00 (luxembourg) | Mohamed Coulibaly · Mariam Brou : Résiliation du prestataire de gardiennage du bailleur (fin au 30/11), lettre remise contre décharge [prevu]  — consigne du 27/10 transmise le 28/10 07h00
- A170 Thu 31/10 16:00 (luxembourg) | Mohamed Coulibaly · Mariam Brou : Passation écrite de Mariam Brou (dossiers, tableau de trésorerie, originaux, lettre de résiliation du gardiennage) puis retrait de ses accès le soir [prevu]  — décision de William du 28/10
- A166 Thu 31/10 19:00 (luxembourg) | Viviane Tanoh : Relance de l'usine d'emballage de Vridi (garanties, maintenance, délais) [prevu]  — consigne du 27/10 transmise le 28/10 07h00
- A164 Thu 31/10 20:00 (luxembourg) | Viviane Tanoh · Éric Koffi Yao : Visite technique de l'entrepôt frigorifique de Port-Bouët [prevu]  — consigne du 27/10 transmise le 28/10 07h00 | reporté de 2041-10-30 18:00 : le responsable maintenance du client est en congé jusqu'au mercredi 30 (Coulibaly, 28/10 07h04 ; T7c execute_a_contrecoeur)
- A148 Sat 02/11 09:00 (luxembourg) | Olivier Schneider : Élagage de la haie mitoyenne par le paysagiste ; part de William : 143 € [prevu]  — accord du 20/10
- A152 Sat 02/11 19:30 (luxembourg) | Thiago Alves : Dîner chez Thiago Alves (feijoada, gars du club, Lenny) : accepté par William le 25/10 à 21h23 [prevu]  — aléa A30 du 25/10 (invitation reçue à 21h20) ; heure indicative
- A144 Mon 04/11 10:00 (luxembourg) | Mohamed Coulibaly : Objectifs écrits de novembre pour chaque dirigeant (P54) [prevu]  — premier lundi du mois
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)
- affaire_projet_ci_annonce : 15 informé(s) hors William ; fuite interne 40 %, externe 15 %
- affaire_projet_ci_art14 : 2 informé(s) hors William ; fuite interne 6 %, externe 2 %

## Fêtes et fériés dans les 30 jours
- ven 01/11/2041 FR Toussaint
- ven 01/11/2041 LU Toussaint
- lun 11/11/2041 FR Armistice 1918

## Routine du tour
- AUJOURD'HUI lundi : revue du lundi (audit_jets.py, tirage_aleas.py, vie hors de la scène principale, monde, idées)
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2041-10-28.md, 6 dernières lignes)
> - **17h10-18h47** (tour n° 181) : 18h47 — Club du lundi : Lenny absent (tiré NON) ; Thiago Alves en salle (tiré OUI, fiche créée, description complète) demande ce que William ne mange pas pour la feijoada.
> - Tirages du tour : jet « Lenny Nguyen vient au club le lundi 28/10 vers 18h40 » → NON (89,14) ; jet « Thiago Alves est en salle le lundi 28/10 entre 18h30 et 20h  » → OUI (47,79).
> - Tour en cours à 18h47, en attente de William : **Thiago Alves : ce que William ne mange pas (feijoada de samedi)**.
> - **18h47-20h15** (tour n° 182) : 20h15 — Réponse à Thiago (T15 garde_distance : bref, retour au bureau) ; fin de séance, retour, dîner.
> - Tirages du tour : T15 Thiago → garde_distance (55,19).
> - Tour en cours à 20h15, en attente de William : **rien d'urgent**.
