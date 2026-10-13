# Résumé d'état (généré le 13/10/2026 10:56 heure machine par outils/resume_etat.py : ne pas éditer à la main)

## Horloge : mercredi 18/07/2040 11:52 (luxembourg, UTC+2)
- **Lieu de William** : Bus 604 (direct), entre Audun-le-Tiche et Luxembourg-Hamilius
- **Heure dans les autres lieux** : abidjan 09:52 ; lisbonne 10:52 ; mindelo 08:52 ; casablanca 10:52 ; douala 10:52 ; addis 12:52 ; manille 17:52 ; paris 11:52
- **En attente de William** :
  - Message de Kiara sur l'application de rencontre (11h52) : « Where will you stay? »
  - Suite du trajet vers l'aéroport (Hamilius 12h25, tram 12h33, Findel 12h55) puis enregistrement du vol LH 391 de 15h40

## Argent (grand livre, calculé)
- Compte courant (Spuerkeess) : **39 707,96 €**
- Compte épargne (Spuerkeess) : **327 000,00 €**
- ETF (valeur de marché : calages seulement) : **288 000,00 €**
- Prêt logement : solde restant dû (passif, déjà déduit de la part de maison) : **110 003,13 €**
- Part nette de la maison d'Audun-le-Tiche : **89 996,87 €**
- Patrimoine net de William : **744 704,83 €**
- Prévu dans les 14 jours : 01/08 Minett Combat Club (-85,00 €) ; 01/08 Package bancaire Zebra Premium (-12,83 €)

## Agenda : dans les 24 heures (3)
- A008 Wed 18/07 15:40 (luxembourg) | Lufthansa + Qatar Airways : Vol aller Luxembourg → Manille (LH 391…QR 932) · départ 15:40 de Luxembourg-Findel, arrivée le 19/07 à 16:30 (heure locale) · réservation PVS2HS [prevu]  — réservation R004 (etat/reservations.csv)
- A007 Thu 19/07 08:00 (luxembourg) | City Garden Grand Hotel : Arrivée à l'hôtel City Garden Grand Hotel (Manille), 36 nuit(s) · réservation R6T4JZA2 [prevu]  — réservation R003 (etat/reservations.csv)
- A023 Thu 19/07 11:25 (luxembourg) | Julia Dimaculangan (application de rencontre) : Répond enfin au message de William du 17/07 à 09h23 : « Hi William! So sorry for the very late reply 🙏 Crazy week, night shift every day 😩 Haha a guide? I'm not a pro but I know Manila well, almost 10 years here. Coffee first, as friends, then we see 😊 When do you arrive? Tip: use Grab only, not the taxis outside the malls, and don't drink the tap water ha » (T21b : repond_tard, jet 56,1, sans modificateur · jour : surlendemain, jet 94,8 · heure : 13h00 + 88,4 × 3 min) · rencontres.py message julia-dimaculangan --auteur profil [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · 11h25 au Luxembourg (William aura atterri à 16h30, heure de Manille) · texte à ajuster si William lui écrit de nouveau d'ici là
## Agenda : de J+1 à J+7 (3)
- A026 Thu 19/07 17:45 (luxembourg) | Shane Lopez (application de rencontre) : Répond enfin au message de William du 17/07 à 17h41 : « Hi William! Sorry for the late reply, work + traffic here are killing me 😅 So you're already here? Welcome to Manila 🙂 How was the flight? » (T21b : repond_tard, jet 56,7, sans modificateur · jour : surlendemain, jet 91,5 · heure fixée selon sa vie : après son service, comme le 17/07) · rencontres.py message shane-lopez --auteur profil [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · 17h45 au Luxembourg · William sera à Manille depuis 16h30 · texte à ajuster si William lui écrit de nouveau d'ici là
- A016 Fri 20/07 03:00 (luxembourg) | Aléa A07 (panne réseau) : Panne réseau (Wi-Fi de l'hôtel, données mobiles) ou banque en ligne indisponible · matin, à Manille [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 4,3) · NON CONNU DE WILLIAM
- A017 Sun 22/07 03:00 (luxembourg) | Aléa A22 (courrier administratif) : Courrier administratif (impôts, CNS, mairie, banque) : par courriel, William étant à Manille (pas de distribution du courrier le dimanche) · matin [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — tirage_aleas.py 2040-07-16 (jet 6,3) · NON CONNU DE WILLIAM
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

## Fin du dernier journal (2040-07-18.md, 6 dernières lignes)
> # Mercredi 18 juillet 2040 — univers 2, cinquième jour (départ pour Manille)
> - **Nuit du 17 au 18/07** : coucher à 23h20, réveil à 7h40, sans réveil (heures tirées au dé : jets 62,7 et 32,5).
> - **07h40-11h12** (tour n° 22, fin du « Go ») : grand soleil (20 °C au réveil, 30 °C annoncés) ; matinée à la maison. À 11h12 (17h12 à Manille), Kiara répond enfin au message de la veille (A022 joué ; T21b : repond_tard, M46) : « Hi William! Sorry for the late reply, I was on shift and so tired 😅 I'm good, thanks! How about you? Where are you from? »
> - Tour en cours à 11h12, en attente de William : **le message de Kiara** ; départ à exécuter sans le redemander (intentions permanentes, `etat/fils-ouverts.md` A2) : bus 604 à 11h30 à la mairie, billet RegioZone avant de monter.
> - **11h12-11h52** (tour n° 23) : à 11h14, William répond à Kiara (dicté en français ; « Chiara » compris comme Kiara) : « No worries, I understand. I'm fine, thanks! I'm from Luxembourg. I arrive in Manila tomorrow and I would really love to meet you, so we can get to know each other. Maybe it's destiny. I have a good situation, even an excellent one. So why not change our lives, both of us? » Réa
> - Tour en cours à 11h52, en attente de William : **le message de Kiara** ; suite du trajet à exécuter (Hamilius 12h25, tram 12h33, aéroport 12h55, enregistrement).
