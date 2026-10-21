# Résumé d'état (généré le 13/10/2026 15:55 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : jeudi 19/07/2040 23:32 (manille, UTC+8)
- **Lieu de William** : Manille, aéroport Ninoy-Aquino (NAIA), terminal 3, sortie des arrivées
- **Heure dans les autres lieux** : abidjan 15:32 ; lisbonne 16:32 ; luxembourg 17:32 ; mindelo 14:32 ; casablanca 16:32 ; douala 16:32 ; addis 18:32 ; paris 17:32
- **En attente de William** :
  - Moyen de rejoindre le City Garden Grand Hotel (Makati) : aucun peso ; taxi à coupon (850 pesos), taxis jaunes au compteur, Grab

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **39 676,56 €**
- Compte épargne (Spuerkeess) : **327 000,00 €**
- ETF (valeur de marché : calages seulement) : **288 000,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **110 003,13 €**
- Part nette de la maison d'Audun-le-Tiche : **89 996,87 €**
- Patrimoine net de William : **744 673,43 €**
- Prévu dans les 14 jours : 01/08 Minett Combat Club (-85,00 €) ; 01/08 Package bancaire Zebra Premium (-12,83 €) ; 02/08 Virement permanent vers le compte épargne (-2 850,00 €) ; 02/08 Virement permanent vers le compte épargne (2 850,00 €) ; 02/08 Virement permanent vers le compte-titres ETF (-2 850,00 €) ; 02/08 Virement permanent vers le compte-titres ETF (2 850,00 €)

## Agenda : dans les 24 heures (4)
- A026 Thu 19/07 23:45 (manille) | Shane Lopez (application de rencontre) : Répond enfin au message de William du 17/07 à 17h41 : « Hi William! Sorry for the late reply, work + traffic here are killing me 😅 So you're already here? Welcome to Manila 🙂 How was the flight? » (T21b : repond_tard, jet 56,7, sans modificateur · jour : surlendemain, jet 91,5 · heure fixée selon sa vie : après son service, comme le 17/07) · rencontres.py message shane-lopez --auteur profil [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · 17h45 au Luxembourg · William sera à Manille depuis 16h30 · texte à ajuster si William lui écrit de nouveau d'ici là
- A007 Fri 20/07 00:30 (manille) | City Garden Grand Hotel : Arrivée à l'hôtel City Garden Grand Hotel (Manille), 36 nuit(s) · réservation R6T4JZA2 [prevu]  — réservation R003 (etat/reservations.csv) | reporté de 2040-07-19 14:00 : correspondance manquée à Doha : arrivée à l'aéroport de Manille à 22h20 au lieu de 16h30 · heure d'arrivée à l'hôtel selon le trajet choisi par William
- A016 Fri 20/07 09:00 (manille) | Aléa A07 (panne réseau) : Panne réseau (Wi-Fi de l'hôtel, données mobiles) ou banque en ligne indisponible · matin, à Manille [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 4,3) · NON CONNU DE WILLIAM
- A027 Fri 20/07 14:46 (manille) | Kiara Reyes (application de rencontre) : Répond au message de William du 18/07 à 11h54 : « Hi William! Sorry, I was so busy 😩 I have a boy, he's 3 🥰 Saturday is ok! City Garden in Makati, I know it. What time? Maybe 3pm? Then we can go to Poblacion, lots of good food there 😋 » (T21b : repond_tard, jet 66,7, M46 · jour : surlendemain, jet 69,1 · heure : 13h00 + 35,3 × 3 min · enfant : un garçon (jet 88,9) de 3 ans (jet 41,9)) · rencontres.py message kiara-reyes --auteur profil [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · 08h46 au Luxembourg · William sera à Manille · texte à ajuster si William lui écrit de nouveau d'ici là
## Agenda : de J+1 à J+7 (2)
- A029 Sat 21/07 17:46 (manille) | Julia Dimaculangan (application de rencontre) : Répond au message de William du 19/07 à 23h27 : « Oh… okay. Sorry if I said something wrong. Take care, William, and enjoy Manila 🙂 » (T21b : repond_tard, jet 64,6 · jour : surlendemain, jet 64,0 · heure : 13h00 + 95,3 × 3 min) · rencontres.py message julia-dimaculangan --auteur profil [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · attachement anxieux de sa fiche : polie, blessée · texte à ajuster si William lui écrit de nouveau d'ici là
- A017 Sun 22/07 09:00 (manille) | Aléa A22 (courrier administratif) : Courrier administratif (impôts, CNS, mairie, banque) : par courriel, William étant à Manille (pas de distribution du courrier le dimanche) · matin [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 6,3) · NON CONNU DE WILLIAM
(Les lignes « NON CONNU DE WILLIAM » servent au moteur : ne jamais les montrer au joueur avant le jour dit.)

## Affaires ouvertes (T4/T5 chaque dimanche soir)

## Fêtes et fériés dans les 30 jours
- mer 15/08 FR Assomption
- mer 15/08 LU Assomption

## Routine du tour
- Session : `python outils/relais.py entree --agent "<nom>"` au début ; `python outils/relais.py sortie --note … --commit … --fusionner` à la fin.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, météo, soleil, argent, corps, lieu, rituels), lecture des fichiers d'état concernés.
- Pendant : réactions et négociations par `jet.py --table Tn` (T1 à T14 ; `--pour` pour un personnage) ; personnages nouveaux par `personnage.py nouveau` ; faits et prix par `faits.py` et `prix.py` ; lieux par `lieux.py voir` ; révélations dans `savoir.py ajouter` ; argent dans `grand_livre.py ajouter`.
- Fin de tour : journal, fils ouverts, WhatsApp, fiches ; puis `python outils/tour.py fin --jusqua … --lieu … --attente … --texte <brouillon> --message …` (horloge, argent échu, météo, texte du tour, tics, résumé, base, note de relais, contrôle).

## Fin du dernier journal (2040-07-19.md, 6 dernières lignes)
> - *Finances* : courant 39 676,56 € ; épargne 327 000 € ; ETF 288 000 € ; prêt 110 003,13 € ; patrimoine net 744 673,43 € ; Visa Debit : 60,44 € utilisés en juillet (abonnement 24,99 €, billet RegioZone 4,05 €, déjeuner à Findel 31,40 €), 2 439,56 € disponibles ; Visa Premier : 4 890 € utilisés sur 5 000 € (relevé débité le 07/08) ; prochains mouvements : traitement + 9 300 € attendu le 31/07 (*mot
> - *Travail et projets* : vacances d'été jusqu'au 16/09 ; séjour à Manille du 19/07 au 24/08 (City Garden Grand Hotel, Makati) ; prolongation au Bureau de l'immigration avant le 18/08 (A011, intention permanente).
> - *Relations* : application de rencontre : Kiara (mère d'un garçon de 3 ans, rendez-vous proposé par William le samedi 21/07 à son hôtel ; réponse tirée pour vendredi), Julia (« coffee first, as friends », message de 17h25 sans réponse), Shane (« When will you be in Manila? » : réponse tirée pour 23h45), Hannah (l'a bloqué le 17/07) ; Clément Grandjean, du club (coup de main refusé, sans rancune).
> - *Calendrier* : sam. 21/07 rendez-vous possible avec Kiara ; ven. 17/08 abonnement de l'application ; sam. 18/08 fin des 30 jours sans visa ; ven. 24/08 vol retour (QR 933, 18h30) ; sam. 25/08 arrivée à Luxembourg (10h05) ; lun. 17/09 rentrée. Fichiers d'état mis à jour le même jour (finances, calendrier, william, fils ouverts, traces, agenda).
> - **23h25-23h32** (tour n° 28) : à 23h27, William écrit à Julia : « It's okay, I'm not interested anymore. Not interested at all. » (dicté en français). Réaction tirée en T21b sans modificateur : réponse tardive (jet 64,6), le samedi 21/07 (jet 64,0) à 17h46 (13h00 + 95,3 × 3 min ; A029, non connue). William sort du terminal : taxis à coupon (« MAKATI — ₱ 850 », PX053 : 630 pesos en 2026 × 1,35), 
> - Tour en cours à 23h32, en attente de William : **le moyen de rejoindre l'hôtel**.
