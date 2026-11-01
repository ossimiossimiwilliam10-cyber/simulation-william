# Vies propres des personnages — fiches vivantes (univers 3 ; état au 16/07/2041, 08h37)

> **Mécanisme validé par l'utilisateur le 09/08/2040 (univers 1), repris dans l'univers 3** : chaque personnage récurrent vit
> indépendamment de William.
> - **Fiche** (une par personnage récurrent, titre « ### Prénom Nom (rôle) ») : objectif du moment, souci en cours, alliés et
>   tensions, agenda de la semaine, secret (faits déjà établis seulement), puis trois lignes de modificateurs lues par
>   `outils/tour_du_monde.py` :
>   - « - **Modificateurs T11** : M80, M81 » (ou « — ») ;
>   - « - **Modificateurs T13** : M95 » (ou « — ») ;
>   - « - **Modificateurs T14** : M84 » (« — » = pas d'initiative envers William ; « aucun » = tirage sans modificateur).
> - **Tour du monde** : à chaque fin de journée simulée et à chaque « Go », `python outils/tour_du_monde.py JJ/MM` tire la journée
>   de chaque personnage (T11), la catégorie du contenu (T13a-d) et son initiative envers William (T14, puis l'heure en T10) ; le
>   détail se choisit d'après la fiche (test d'intérêt) ; ce qui touche William se tire ensuite dans les tables existantes.
> - **Échos visibles** : chaque tour montre une ou deux traces de la vie des autres que William peut percevoir (statut, photo,
>   rumeur, ton qui change), sans explication.
> - **Mise à jour** : les fiches évoluent à chaque tour du monde (« avant → maintenant »).
> - **Univers 3** : les fiches des univers 1 et 2 sont archivées ; aucun de ces
>   personnages n'est actif au départ. Une fiche se crée quand un personnage devient récurrent (deuxième apparition, ou lien durable).
> - **Depuis le 11/10/2026** : un personnage nouveau se crée avec `python outils/personnage.py nouveau --contexte … --role …`
>   (tirage selon la démographie réelle ; il écrit lui-même la fiche ci-dessous, `personnes/` et `etat/personnages.csv`).

## Fiches

> Section RÉGÉNÉRÉE par `python outils/monde_vivant.py fiches` (appelé par `tour.py fin`) : ne pas éditer à la main ; les événements complets sont dans `etat/vies.csv`.

### Max Rocha (directeur du lycée)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : rembourser ses dettes ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : parent isolé
- **Secret (moteur seulement)** : fume en cachette alors qu'il dit avoir arrêté (gravité 1)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +19 min ; travail 09:19-17:49 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:49-07:19
- **Derniers événements** : 06/10 avancee_objectif (somme reçue, économisée ou investie pour son objectif : rembourser ses dettes); 13/10 sans_histoire; 19/10 petit_evenement (querelle courte); 23/10 sans_histoire; 28/10 avancee_objectif (démarche pour son objectif : rembourser ses dettes)

### Emma Gómez (secrétaire du lycée)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : tension avec la belle-famille ; **foyer** : en couple, enfants en bas âge
- **Secret (moteur seulement)** : prend des antidépresseurs (gravité 1)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +2 min ; travail 09:02-17:32 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:32-07:02
- **Derniers événements** : 05/10 petit_evenement (dépense imprévue (cotisation imprévue)); 08/10 sans_histoire; 20/10 sans_histoire; 21/10 petit_evenement (croisement, visite ou conversation de voisinage); 30/10 sans_histoire

### Sam Ries (professeur de mathématiques)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : couple en crise ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : a fait une demande de crédit refusée (gravité 1)
- **Horaires** : règle « enseignant », fuseau luxembourg, décalage +19 min ; travail 08:19-16:19 (lun, mar, mer, jeu, ven), trajet 45 min ; sommeil 23:19-06:49
- **Derniers événements** : 05/10 sans_histoire; 12/10 petit_evenement (querelle courte); 18/10 sans_histoire; 24/10 sans_histoire; 30/10 petit_evenement (service rendu ou reçu)

### Kim Schmitz (professeure de physique)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : dispute avec un frère ou une sœur pour un héritage ; **foyer** : en colocation
- **Secret (moteur seulement)** : est amoureux d'un collègue ou d'une collègue (gravité 1)
- **Horaires** : règle « enseignant », fuseau luxembourg, décalage +24 min ; travail 08:24-16:24 (lun, mar, mer, jeu, ven), trajet 45 min ; sommeil 23:24-06:54
- **Derniers événements** : 01/10 avancee_objectif (somme reçue, économisée ou investie pour son objectif : changer de métier); 12/10 avancee_objectif (démarche pour son objectif : changer de métier); 18/10 petit_evenement (croisement, visite ou conversation de voisinage); 21/10 sans_histoire; 01/11 petit_evenement (bus en retard)

### Ruben Gomes (entraîneur de grappling)
- **Lien avec William** : contact_recent (whatsapp)
- **Objectif** : obtenir une promotion ou un poste plus stable ; **souci** : mal de dos chronique ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : prend des antidépresseurs (gravité 1)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage -15 min ; travail 08:45-17:15 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:15-06:45
- **Derniers événements** : 30/09 petit_evenement (dépense imprévue (frais de scolarité)); 13/10 sans_histoire; 20/10 petit_evenement (service rendu ou reçu); 22/10 sans_histoire; 30/10 sans_histoire

### Thiago Alves (coach de musculation du club)
- **Lien avec William** : contact_recent (whatsapp)
- **Objectif** : voyager loin une fois dans sa vie ; **souci** : mal de dos chronique ; **foyer** : parent isolé
- **Secret (moteur seulement)** : consulte un psychologue (gravité 1)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +3 min ; travail 09:03-17:33 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:33-07:03
- **Derniers événements** : 01/10 sans_histoire; 08/10 sans_histoire; 15/10 sans_histoire; 24/10 sans_histoire; 02/11 sans_histoire

### Lenny Nguyen (membre régulier du club (sparring))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : rembourser ses dettes ; **souci** : dettes de jeu ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : a un problème d'alcool qu'il cache (gravité 2)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +18 min ; travail 09:18-17:48 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:48-07:18
- **Derniers événements** : 05/10 sans_histoire; 12/10 petit_evenement (dépense imprévue (réparation de la moto)); 20/10 sans_histoire; 23/10 sans_histoire; 03/11 avancee_objectif (démarche pour son objectif : rembourser ses dettes)

### Mariana Oliveira (membre régulière du club (sparring))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : obtenir la nationalité luxembourgeoise ; **souci** : contrat de travail qui se termine bientôt ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : fume en cachette alors qu'il dit avoir arrêté (gravité 1)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage -17 min ; travail 08:43-17:13 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:13-06:43
- **Derniers événements** : 06/10 sans_histoire; 12/10 petit_evenement (service rendu ou reçu); 18/10 sans_histoire; 25/10 sans_histoire; 01/11 avancee_objectif (somme reçue, économisée ou investie pour son objectif : obtenir la nationalité luxembourgeoise)

### Clément Grandjean (membre régulier du club (sparring))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : couple en crise ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : se renseigne pour partir s'installer ailleurs (gravité 1)
- **Horaires** : règle « etudiant », fuseau luxembourg, décalage +25 min ; travail 09:25-17:25 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:55-08:55
- **Derniers événements** : 01/10 sans_histoire; 12/10 petit_evenement (dépense imprévue (facture d'électricité plus lourde)); 20/10 petit_evenement (service rendu ou reçu); 22/10 coup_dur (dispute sérieuse ou mauvaise nouvelle dans la famille); 29/10 petit_evenement (achat (petit électroménager))

### Arthur Kieffer (membre régulier du club (sparring))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : trouver quelqu'un et se poser ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : prend des antidépresseurs (gravité 1)
- **Horaires** : règle « etudiant », fuseau luxembourg, décalage +4 min ; travail 09:04-17:04 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:34-08:34
- **Derniers événements** : 06/10 petit_evenement (chantier d'été qui bloque la rue); 10/10 sans_histoire; 18/10 petit_evenement (croisement, visite ou conversation de voisinage); 25/10 sans_histoire; 28/10 petit_evenement (dépense imprévue (cotisation imprévue))

### Olivier Schneider (voisin mitoyen (côté gauche))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : tension avec la belle-famille ; **foyer** : en couple
- **Secret (moteur seulement)** : a perdu beaucoup d'argent au jeu ou en bourse (gravité 2)
- **Horaires** : règle « sans_travail », fuseau luxembourg, décalage +0 min ; pas d'horaires de travail ; sommeil 23:00-07:00
- **Derniers événements** : 03/10 avancee_objectif (rendez-vous obtenu ou tenu pour son objectif : finir de rénover sa maison); 12/10 sans_histoire; 15/10 sans_histoire; 26/10 tournant (déménagement, bail ou proche hébergé); 02/11 sans_histoire

### Aurélie Martin (voisine de la rue)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : apprendre le luxembourgeois ; **souci** : voisin bruyant ; **foyer** : parent isolé
- **Secret (moteur seulement)** : fume en cachette alors qu'il dit avoir arrêté (gravité 1)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage -23 min ; travail 08:37-17:07 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:07-06:37
- **Derniers événements** : 06/10 sans_histoire; 11/10 sans_histoire; 17/10 sans_histoire; 27/10 avancee_objectif (démarche pour son objectif : apprendre le luxembourgeois); 29/10 sans_histoire

### Eugène Doumbia (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : faire croître son bureau d'études avec des clients internationaux ; **souci** : voisin bruyant ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : cherche un autre travail en cachette (gravité 1)
- **Horaires** : règle « commerce_abidjan », fuseau abidjan, décalage +11 min ; travail 08:41-19:11 (lun, mar, mer, jeu, ven, sam), trajet 30 min ; sommeil 23:11-06:11
- **Derniers événements** : 01/10 sans_histoire; 13/10 sans_histoire; 14/10 sans_histoire; 27/10 sans_histoire; 03/11 sans_histoire

### Nadège Kouamé (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : burn-out qui couve ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage +1 min ; travail 09:01-17:31 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:31-07:01
- **Derniers événements** : 04/10 sans_histoire; 12/10 petit_evenement (service rendu ou reçu); 16/10 avancee_objectif (somme reçue, économisée ou investie pour son objectif : changer de métier); 27/10 sans_histoire; 02/11 sans_histoire

### Jean-Baptiste Tuo (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : obtenir un poste de direction dans une grande entreprise ; **souci** : dettes de jeu ; **foyer** : en couple, enfants partis
- **Secret (moteur seulement)** : —
- **Horaires** : règle « commerce_abidjan », fuseau abidjan, décalage -7 min ; travail 08:23-18:53 (lun, mar, mer, jeu, sam, dim), trajet 30 min ; sommeil 22:53-05:53
- **Derniers événements** : 01/10 coup_dur (dispute sérieuse ou mauvaise nouvelle dans la famille); 09/10 sans_histoire; 14/10 petit_evenement (dépense imprévue (réparation du téléphone)); 25/10 avancee_objectif (somme reçue, économisée ou investie pour son objectif : obtenir un poste de direction dans une grande entreprise); 30/10 sans_histoire

### Sandrine Cissé (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : faire croître son bureau d'études avec des clients internationaux ; **souci** : un parent âgé dont la santé décline ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : fume en cachette alors qu'il dit avoir arrêté (gravité 1)
- **Horaires** : règle « bureau », fuseau abidjan, décalage -28 min ; travail 08:32-17:02 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:02-06:32
- **Derniers événements** : 04/10 sans_histoire; 08/10 petit_evenement (gbaka en panne sur le boulevard); 19/10 avancee_objectif (formation, lecture ou conseil utile : faire croître son bureau d'études avec des clients internationaux); 24/10 sans_histoire; 31/10 avancee_objectif (démarche pour son objectif : faire croître son bureau d'études avec des clients internationaux)

### Hervé Touré (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : se faire une place dans le milieu (club, lycée, quartier) ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « commerce_abidjan », fuseau abidjan, décalage +18 min ; travail 08:48-19:18 (lun, mar, mer, ven, sam, dim), trajet 30 min ; sommeil 23:18-06:18
- **Derniers événements** : 02/10 petit_evenement (nouvelle de la famille ou des amis); 08/10 coup_dur (prêt à un proche jamais rendu); 17/10 tournant (départ, retour ou projet de voyage); 24/10 sans_histoire; 31/10 petit_evenement (achat (vêtements))

### Franck Konan (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un terrain et construire sa maison à Abidjan ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage +14 min ; travail 09:14-17:44 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:44-07:14
- **Derniers événements** : 02/10 sans_histoire; 12/10 petit_evenement (rumeur entendue ou colportée); 15/10 tournant (rencontre qui compte (amicale, amoureuse ou professionnelle)); 22/10 sans_histoire; 29/10 sans_histoire

### Yannick N'Guessan (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : fin de mois difficile, découvert bancaire ; **foyer** : parent isolé
- **Secret (moteur seulement)** : —
- **Horaires** : règle « sans_travail », fuseau abidjan, décalage -13 min ; pas d'horaires de travail ; sommeil 22:47-06:47
- **Derniers événements** : 04/10 avancee_objectif (rendez-vous obtenu ou tenu pour son objectif : finir de rénover sa maison); 10/10 petit_evenement (querelle courte); 19/10 sans_histoire; 24/10 sans_histoire; 03/11 sans_histoire

### Solange Gnagne (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : trouver quelqu'un et se poser ; **souci** : embouteillages et trajets de deux heures entre Abidjan et son travail ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage +24 min ; travail 09:24-17:54 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:54-07:24
- **Derniers événements** : 05/10 petit_evenement (nouvelle de la famille ou des amis); 09/10 sans_histoire; 19/10 sans_histoire; 27/10 petit_evenement (rumeur entendue ou colportée); 29/10 petit_evenement (service rendu ou reçu)

### Jonathan Ouattara (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : un parent âgé dont la santé décline ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +1 min ; travail 09:01-17:31 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:31-07:01
- **Derniers événements** : 01/10 sans_histoire; 09/10 coup_dur (malade (dengue légère)); 19/10 petit_evenement (service rendu ou reçu); 26/10 petit_evenement (bus en retard); 02/11 petit_evenement (nouvelle de la famille ou des amis)

### Mohamed Coulibaly (répondant à l'annonce)
- **Lien avec William** : contact_recent (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : contrat de travail qui se termine bientôt ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage -21 min ; travail 07:39-17:09 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:09-05:39
- **Derniers événements** : 30/09 sans_histoire; 11/10 sans_histoire; 20/10 sans_histoire; 27/10 petit_evenement (dépense imprévue (réparation du téléphone)); 03/11 sans_histoire

### Maïmouna Koné (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : obtenir une promotion ou un poste plus stable ; **souci** : voisin bruyant ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « enseignant », fuseau luxembourg, décalage -15 min ; travail 07:45-15:45 (lun, mar, mer, jeu, ven), trajet 45 min ; sommeil 22:45-06:15
- **Derniers événements** : 04/10 avancee_objectif (démarche pour son objectif : obtenir une promotion ou un poste plus stable); 13/10 sans_histoire; 16/10 tournant (rencontre qui compte (amicale, amoureuse ou professionnelle)); 22/10 tournant (proposition d'emploi ou de collaboration ailleurs); 01/11 sans_histoire

### Brice Tapé (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : passer plus de temps avec ses enfants ; **souci** : problème de santé qu'il refuse de faire examiner ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage -21 min ; travail 08:39-17:09 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:09-06:39
- **Derniers événements** : 04/10 petit_evenement (querelle courte); 08/10 petit_evenement (chantier d'été qui bloque la rue); 15/10 sans_histoire; 22/10 sans_histoire; 01/11 sans_histoire

### Kader Assi (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : préparer une compétition ou un examen ; **souci** : loyer qui augmente ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +30 min ; travail 09:30-18:00 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 00:00-07:30
- **Derniers événements** : 01/10 sans_histoire; 08/10 sans_histoire; 16/10 sans_histoire; 24/10 petit_evenement (croisement, visite ou conversation de voisinage); 31/10 sans_histoire

### Boubacar Sylla (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : monter ou diriger une entreprise au pays ; **souci** : loyer qui augmente ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : a menti sur son diplôme ou son expérience (gravité 2)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +9 min ; travail 09:09-17:39 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:39-07:09
- **Derniers événements** : 30/09 sans_histoire; 09/10 petit_evenement (dépense imprévue (cotisation imprévue)); 14/10 sans_histoire; 23/10 sans_histoire; 30/10 petit_evenement (dépense imprévue (frais de scolarité))

### Cédric Soro (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : contrat de travail qui se termine bientôt ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage -5 min ; travail 07:55-17:25 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:25-05:55
- **Derniers événements** : 04/10 tournant (déménagement, bail ou proche hébergé); 13/10 coup_dur (panne, coupure ou souci de logement); 19/10 petit_evenement (croisement, visite ou conversation de voisinage); 25/10 sans_histoire; 01/11 sans_histoire

### Landry Aka (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : préparer une compétition ou un examen ; **souci** : famille installée à l'étranger qui hésite à rentrer ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +28 min ; travail 09:28-17:58 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:58-07:28
- **Derniers événements** : 06/10 sans_histoire; 13/10 sans_histoire; 20/10 sans_histoire; 21/10 sans_histoire; 30/10 sans_histoire

### Fabrice Koffi (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : mettre de l'argent de côté pour ses vieux jours ; **souci** : mal de dos chronique ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage +12 min ; travail 08:12-17:42 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:42-06:12
- **Derniers événements** : 04/10 sans_histoire; 13/10 avancee_objectif (décision prise pour son objectif : mettre de l'argent de côté pour ses vieux jours); 17/10 avancee_objectif (démarche pour son objectif : mettre de l'argent de côté pour ses vieux jours); 23/10 sans_histoire; 03/11 sans_histoire

### Aboubacar Kouassi (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : dettes de jeu ; **foyer** : parent isolé
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage -19 min ; travail 08:41-17:11 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:11-06:41
- **Derniers événements** : 01/10 petit_evenement (querelle courte); 07/10 coup_dur (dettes de jeu); 20/10 sans_histoire; 27/10 avancee_objectif (démarche pour son objectif : changer de métier); 01/11 sans_histoire

### Ousmane Yéo (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : faire croître son bureau d'études avec des clients internationaux ; **souci** : coupures de courant et facture d'électricité lourde pour son activité ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « commerce_abidjan », fuseau abidjan, décalage +20 min ; travail 08:50-19:20 (lun, mer, jeu, ven, sam, dim), trajet 30 min ; sommeil 23:20-06:20
- **Derniers événements** : 05/10 sans_histoire; 07/10 avancee_objectif (rendez-vous obtenu ou tenu pour son objectif : faire croître son bureau d'études avec des clients internationaux); 19/10 sans_histoire; 26/10 sans_histoire; 29/10 petit_evenement (nouvelle de la famille ou des amis)

### Mariam Brou (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : embouteillages et trajets de deux heures entre Abidjan et son travail ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage -26 min ; travail 07:34-17:04 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:04-05:34
- **Derniers événements** : 06/10 avancee_objectif (rendez-vous obtenu ou tenu pour son objectif : changer de métier); 07/10 sans_histoire; 17/10 sans_histoire; 27/10 petit_evenement (croisement, visite ou conversation de voisinage); 01/11 sans_histoire

### Damien Yao (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : rentrer en Côte d'Ivoire après des années à l'étranger ; **souci** : épargne et retraite à reconstituer avant un retour ; **foyer** : parent isolé
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +9 min ; travail 09:09-17:39 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:39-07:09
- **Derniers événements** : 04/10 petit_evenement (service rendu ou reçu); 12/10 sans_histoire; 17/10 sans_histoire; 21/10 sans_histoire; 03/11 sans_histoire

### Arsène Zadi (avocat(e) d'affaires à Abidjan (cabinet en liste restreinte))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : passer plus de temps avec ses enfants ; **souci** : clients qui paient avec des mois de retard ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : vote pour un parti qu'il n'avoue pas (gravité 1)
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage -9 min ; travail 07:51-17:21 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:21-05:51
- **Derniers événements** : 02/10 sans_histoire; 09/10 coup_dur (malade (forte fièvre)); 20/10 sans_histoire; 21/10 petit_evenement (rumeur entendue ou colportée); 28/10 petit_evenement (averse qui inonde la rue)

### Issouf Tano (avocat(e) d'affaires à Abidjan (cabinet en liste restreinte))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : trouver un partenaire européen pour financer un projet ; **souci** : tension avec la belle-famille ; **foyer** : en couple, enfants partis
- **Secret (moteur seulement)** : doit de l'argent à une tontine ou à un prêteur (gravité 1)
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage -9 min ; travail 07:51-17:21 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:21-05:51
- **Derniers événements** : 01/10 tournant (rencontre qui compte (amicale, amoureuse ou professionnelle)); 12/10 coup_dur (ennui avec son employeur ou un client); 18/10 avancee_objectif (rendez-vous obtenu ou tenu pour son objectif : trouver un partenaire européen pour financer un projet); 25/10 petit_evenement (service rendu ou reçu); 03/11 petit_evenement (croisement, visite ou conversation de voisinage)

### Ismaël Gnamien (avocat(e) d'affaires à Abidjan (cabinet en liste restreinte))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : voisin bruyant ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : a fait une demande de crédit refusée (gravité 1)
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage +22 min ; travail 08:22-17:52 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:52-06:22
- **Derniers événements** : 04/10 sans_histoire; 10/10 sans_histoire; 19/10 sans_histoire; 22/10 petit_evenement (dépense imprévue (réparation du téléphone)); 01/11 avancee_objectif (démarche pour son objectif : changer de métier)

### Kady Kouadio (étudiante en master à l'UFHB)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : préparer une compétition ou un examen ; **souci** : contrat de travail qui se termine bientôt ; **foyer** : vit chez ses parents
- **Secret (moteur seulement)** : —
- **Horaires** : règle « etudiant », fuseau abidjan, décalage -6 min ; travail 08:54-16:54 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:24-08:24
- **Derniers événements** : 30/09 sans_histoire; 07/10 sans_histoire; 14/10 sans_histoire; 23/10 sans_histoire; 03/11 sans_histoire

### Safiatou Camara (restaurateur de maquis)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : obtenir un poste de direction dans une grande entreprise ; **souci** : chef difficile ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : envoie de l'argent à une famille élargie qui en demande toujours plus (gravité 1)
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage -18 min ; travail 07:42-17:12 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:12-05:42
- **Derniers événements** : 03/10 sans_histoire; 08/10 petit_evenement (rumeur entendue ou colportée); 19/10 sans_histoire; 27/10 avancee_objectif (somme reçue, économisée ou investie pour son objectif : obtenir un poste de direction dans une grande entreprise); 28/10 avancee_objectif (démarche pour son objectif : obtenir un poste de direction dans une grande entreprise)

### Fatoumata Gnagne (étudiante en master d'économie UFHB)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : trouver quelqu'un et se poser ; **souci** : embouteillages et trajets de deux heures entre Abidjan et son travail ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : cherche un autre travail en cachette (gravité 1)
- **Horaires** : règle « etudiant », fuseau abidjan, décalage +28 min ; travail 09:28-17:28 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:58-08:58
- **Derniers événements** : 03/10 tournant (rencontre qui compte (amicale, amoureuse ou professionnelle)); 11/10 sans_histoire; 18/10 sans_histoire; 26/10 sans_histoire; 28/10 petit_evenement (dépense imprévue (cotisation imprévue))

### Kader Bamba (habitant des Deux-Plateaux)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : voyager loin une fois dans sa vie ; **souci** : fin de mois difficile, découvert bancaire ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : vote pour un parti qu'il n'avoue pas (gravité 1)
- **Horaires** : règle « commerce_abidjan », fuseau abidjan, décalage -9 min ; travail 08:21-18:51 (lun, mar, mer, jeu, sam, dim), trajet 30 min ; sommeil 22:51-05:51
- **Derniers événements** : 05/10 sans_histoire; 13/10 sans_histoire; 14/10 sans_histoire; 24/10 coup_dur (malade (dengue légère)); 29/10 petit_evenement (dépense imprévue (frais de scolarité))

### Brice Yao (agent de sécurité privée)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : préparer une compétition ou un examen ; **souci** : clients qui paient avec des mois de retard ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : a gonflé son expérience ou son diplôme sur son CV (gravité 2)
- **Horaires** : règle « bureau », fuseau abidjan, décalage +16 min ; travail 09:16-17:46 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:46-07:16
- **Derniers événements** : 06/10 sans_histoire; 11/10 coup_dur (dispute sérieuse ou mauvaise nouvelle dans la famille); 17/10 sans_histoire; 22/10 sans_histoire; 02/11 sans_histoire

### Christelle Kouamé (escort indépendante (annonce BabiEscort))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : se faire une place dans le milieu (club, lycée, quartier) ; **souci** : démarche administrative bloquée (titre de séjour, permis, impôts) ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : a raté un examen important qu'il dit avoir réussi (gravité 2)
- **Horaires** : règle « etudiant », fuseau abidjan, décalage -12 min ; travail 08:48-16:48 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:18-08:18
- **Derniers événements** : 04/10 sans_histoire; 10/10 sans_histoire; 16/10 petit_evenement (querelle courte); 21/10 sans_histoire; 28/10 sans_histoire

### Kady Coulibaly (escort indépendante)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : rembourser ses dettes ; **souci** : burn-out qui couve ; **foyer** : vit chez ses parents
- **Secret (moteur seulement)** : a menti sur son diplôme ou son expérience (gravité 2)
- **Horaires** : règle « bureau », fuseau abidjan, décalage +0 min ; travail 09:00-17:30 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:30-07:00
- **Derniers événements** : 04/10 petit_evenement (dépense imprévue (réparation de la moto)); 13/10 sans_histoire; 17/10 sans_histoire; 25/10 petit_evenement (nouvelle de la famille ou des amis); 29/10 petit_evenement (embouteillage monstre au pont Houphouët-Boigny)

### Nadège Kouassi (escort étudiante indépendante)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : trouver un partenaire européen pour financer un projet ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : cherche un autre travail en cachette (gravité 1)
- **Horaires** : règle « etudiant », fuseau abidjan, décalage +11 min ; travail 09:11-17:11 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:41-08:41
- **Derniers événements** : 05/10 sans_histoire; 07/10 tournant (rentrée ou perte d'argent importante); 20/10 sans_histoire; 21/10 petit_evenement (querelle courte); 28/10 petit_evenement (dépense imprévue (facture d'électricité plus lourde))

### Kady Konaté (escort indépendante étudiante)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : maigrir ou reprendre le sport ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : vit chez ses parents
- **Secret (moteur seulement)** : prend des antidépresseurs (gravité 1)
- **Horaires** : règle « etudiant », fuseau abidjan, décalage +25 min ; travail 09:25-17:25 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:55-08:55
- **Derniers événements** : 02/10 sans_histoire; 11/10 coup_dur (dispute sérieuse ou mauvaise nouvelle dans la famille); 15/10 tournant (déménagement, bail ou proche hébergé); 23/10 sans_histoire; 31/10 sans_histoire

### Mya Touré (escort indépendante (annonce BabiEscort))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : payer son année universitaire ; **souci** : — ; **foyer** : vit seule en studio
- **Secret (moteur seulement)** : —
- **Horaires** : règle « etudiant », fuseau abidjan, décalage +18 min ; travail 09:18-17:18 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:48-08:48
- **Derniers événements** : 05/10 sans_histoire; 08/10 avancee_objectif (rendez-vous obtenu ou tenu pour son objectif : payer son année universitaire); 15/10 petit_evenement (croisement, visite ou conversation de voisinage); 23/10 sans_histoire; 31/10 petit_evenement (croisement, visite ou conversation de voisinage)

### Marc-Antoine Kouadio (candidat Direction Commerciale)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un terrain et construire sa maison à Abidjan ; **souci** : contrat de travail qui se termine bientôt ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : fume en cachette alors qu'il dit avoir arrêté (gravité 1)
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage +21 min ; travail 08:21-17:51 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:51-06:21
- **Derniers événements** : 05/10 sans_histoire; 07/10 sans_histoire; 14/10 coup_dur (malade (gastro-entérite)); 26/10 sans_histoire; 29/10 petit_evenement (nouvelle de la famille ou des amis)

### Viviane Tanoh (candidate Direction Commerciale)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : un enfant qui décroche à l'école ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : consulte un psychologue (gravité 1)
- **Horaires** : règle « bureau », fuseau abidjan, décalage +26 min ; travail 09:26-17:56 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:56-07:26
- **Derniers événements** : 06/10 petit_evenement (querelle courte); 09/10 sans_histoire; 18/10 sans_histoire; 26/10 sans_histoire; 03/11 petit_evenement (querelle courte)

### Wilfried Yéo (gérant d'alimentation générale)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : faire croître son bureau d'études avec des clients internationaux ; **souci** : tension avec la belle-famille ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage -23 min ; travail 08:37-17:07 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:07-06:37
- **Derniers événements** : 04/10 sans_histoire; 08/10 sans_histoire; 20/10 sans_histoire; 21/10 petit_evenement (rumeur entendue ou colportée); 02/11 sans_histoire

### Éric Koffi Yao (directeur technique de Soleil B2B CI (ingénieur, recruté le 02/08/2041))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : passer plus de temps avec ses enfants ; **souci** : procédure de divorce ; **foyer** : parent isolé
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage +12 min ; travail 08:12-17:42 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:42-06:12
- **Derniers événements** : 06/10 petit_evenement (croisement, visite ou conversation de voisinage); 12/10 sans_histoire; 15/10 sans_histoire; 26/10 coup_dur (maladie ou accident de son enfant); 31/10 sans_histoire

### Luca Singh (dirigeant de Lagune Kilowatt (grosse PME d'installation solaire, prix agressifs), installateur solaire concurrent (société fictive))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : mettre de l'argent de côté pour ses vieux jours ; **souci** : coupures de courant et facture d'électricité lourde pour son activité ; **foyer** : en couple, enfants en bas âge
- **Secret (moteur seulement)** : a un enfant qu'il ne voit plus (gravité 3)
- **Horaires** : règle « commerce_abidjan », fuseau abidjan, décalage +5 min ; travail 08:35-19:05 (lun, mar, mer, jeu, ven, dim), trajet 30 min ; sommeil 23:05-06:05
- **Derniers événements** : 04/10 sans_histoire; 11/10 sans_histoire; 19/10 avancee_objectif (rendez-vous obtenu ou tenu pour son objectif : mettre de l'argent de côté pour ses vieux jours); 25/10 petit_evenement (croisement, visite ou conversation de voisinage); 28/10 sans_histoire

### Lukas Diallo (dirigeant de Comoé Solaire Services (PME relationnelle, recrute chez les concurrents), installateur solaire concurrent (société fictive))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : obtenir un poste de direction dans une grande entreprise ; **souci** : démarche administrative bloquée (titre de séjour, permis, impôts) ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : a fait une demande de crédit refusée (gravité 1)
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage -8 min ; travail 07:52-17:22 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:22-05:52
- **Derniers événements** : 05/10 petit_evenement (service rendu ou reçu); 13/10 petit_evenement (dépense imprévue (cotisation imprévue)); 20/10 sans_histoire; 26/10 coup_dur (malade (gastro-entérite)); 02/11 sans_histoire

### Brice N'Guessan (dirigeant de Ébène Watt (petite structure informelle, matériel d'entrée de gamme), installateur solaire concurrent (société fictive))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : loyer qui augmente ; **foyer** : en couple, enfants en bas âge
- **Secret (moteur seulement)** : doit de l'argent à un proche (gravité 1)
- **Horaires** : règle « sans_travail », fuseau abidjan, décalage +14 min ; pas d'horaires de travail ; sommeil 23:14-07:14
- **Derniers événements** : 01/10 petit_evenement (croisement, visite ou conversation de voisinage); 08/10 petit_evenement (dépense imprévue (cotisation imprévue)); 14/10 sans_histoire; 21/10 sans_histoire; 31/10 petit_evenement (dépense imprévue (réparation du téléphone))

### Wilfried Boni (chauffeur Yango (course commandée par la résidence))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : se faire une place dans le milieu (club, lycée, quartier) ; **souci** : fin de mois difficile, découvert bancaire ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : a fait une demande de crédit refusée (gravité 1)
- **Horaires** : règle « chauffeur », fuseau abidjan, décalage +10 min ; travail 06:10-18:10 (lun, mar, mer, jeu, ven, dim), trajet 20 min ; sommeil 22:10-05:10
- **Derniers événements** : 06/10 coup_dur (malade (dengue légère)); 11/10 avancee_objectif (démarche pour son objectif : se faire une place dans le milieu (club, lycée, quartier)); 15/10 sans_histoire; 25/10 sans_histoire; 30/10 sans_histoire

### Hervé Ouattara (chauffeur Yango (résidence → Sofitel Hôtel Ivoire))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : coupures de courant et facture d'électricité lourde pour son activité ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : a menti sur son diplôme ou son expérience (gravité 2)
- **Horaires** : règle « chauffeur », fuseau abidjan, décalage -5 min ; travail 05:55-17:55 (lun, mar, jeu, ven, sam, dim), trajet 20 min ; sommeil 21:55-04:55
- **Derniers événements** : 06/10 sans_histoire; 13/10 coup_dur (maladie ou accident de son père); 17/10 petit_evenement (dépense imprévue (facture d'électricité plus lourde)); 22/10 petit_evenement (coupure de courant dans le quartier); 28/10 sans_histoire

### Nathalie Cissé (hôtesse d'accueil du club de sport du Sofitel Hôtel Ivoire)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : avoir un enfant ; **souci** : loyer qui augmente ; **foyer** : en couple, enfants en bas âge
- **Secret (moteur seulement)** : se renseigne pour partir s'installer ailleurs (gravité 1)
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage +10 min ; travail 08:10-17:40 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:40-06:10
- **Derniers événements** : 02/10 avancee_objectif (démarche pour son objectif : avoir un enfant); 07/10 coup_dur (prêt à un proche jamais rendu); 19/10 avancee_objectif (démarche pour son objectif : avoir un enfant); 21/10 sans_histoire; 30/10 petit_evenement (coupure de courant dans le quartier)

### Yannick Kouamé (chauffeur Yango (Sofitel Hôtel Ivoire → résidence))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : embouteillages et trajets de deux heures entre Abidjan et son travail ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : a une liaison (gravité 3)
- **Horaires** : règle « chauffeur », fuseau abidjan, décalage +9 min ; travail 06:09-18:09 (lun, mar, mer, ven, sam, dim), trajet 20 min ; sommeil 22:09-05:09
- **Derniers événements** : 01/10 sans_histoire; 08/10 sans_histoire; 15/10 sans_histoire; 25/10 petit_evenement (service rendu ou reçu); 02/11 avancee_objectif (somme reçue, économisée ou investie pour son objectif : acheter un logement (ou un plus grand))

### Kader Konan (employé du room service de la résidence hôtelière (Deux-Plateaux))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : fin de mois difficile, découvert bancaire ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : a un problème d'alcool qu'il cache (gravité 2)
- **Horaires** : règle « bureau », fuseau abidjan, décalage +14 min ; travail 09:14-17:44 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:44-07:14
- **Derniers événements** : 04/10 petit_evenement (querelle courte); 12/10 petit_evenement (dépense imprévue (frais de scolarité)); 18/10 avancee_objectif (formation, lecture ou conseil utile : finir de rénover sa maison); 26/10 sans_histoire; 31/10 sans_histoire

### Fabrice Goulizan (chauffeur Yango (résidence → Playce Palmeraie))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : parent isolé
- **Secret (moteur seulement)** : fume en cachette alors qu'il dit avoir arrêté (gravité 1)
- **Horaires** : règle « chauffeur », fuseau abidjan, décalage -8 min ; travail 05:52-17:52 (lun, mar, mer, jeu, ven, sam), trajet 20 min ; sommeil 21:52-04:52
- **Derniers événements** : 30/09 sans_histoire; 12/10 petit_evenement (service rendu ou reçu); 14/10 petit_evenement (service rendu ou reçu); 24/10 coup_dur (dispute sérieuse ou mauvaise nouvelle dans la famille); 28/10 petit_evenement (croisement, visite ou conversation de voisinage)

### Landry Konan (vendeur de la boutique de sport du Playce Palmeraie)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : insomnies ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : a gonflé son expérience ou son diplôme sur son CV (gravité 2)
- **Horaires** : règle « commerce_abidjan », fuseau abidjan, décalage -7 min ; travail 08:23-18:53 (mar, mer, jeu, ven, sam, dim), trajet 30 min ; sommeil 22:53-05:53
- **Derniers événements** : 01/10 sans_histoire; 08/10 sans_histoire; 14/10 sans_histoire; 23/10 coup_dur (panne, coupure ou souci de logement); 01/11 sans_histoire

### Mariam Kra (chauffeur Yango (Playce Palmeraie → résidence))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : loyer qui augmente ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : a un enfant qu'il ne voit plus (gravité 3)
- **Horaires** : règle « chauffeur », fuseau abidjan, décalage +19 min ; travail 06:19-18:19 (lun, mar, mer, jeu, ven, sam), trajet 20 min ; sommeil 22:19-05:19
- **Derniers événements** : 03/10 petit_evenement (service rendu ou reçu); 09/10 coup_dur (dépense imprévue); 14/10 sans_histoire; 24/10 petit_evenement (querelle courte); 01/11 petit_evenement (nouvelle de la famille ou des amis)

### Yannick Bamba (propriétaire bailleur de la villa des Vallons)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : rembourser ses dettes ; **souci** : fin de mois difficile, découvert bancaire ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : doit de l'argent à un proche (gravité 1)
- **Horaires** : règle « bureau_abidjan », fuseau abidjan, décalage -25 min ; travail 07:35-17:05 (lun, mar, mer, jeu, ven), trajet 50 min ; sommeil 23:05-05:35
- **Derniers événements** : 05/10 avancee_objectif (démarche pour son objectif : rembourser ses dettes); 07/10 sans_histoire; 16/10 sans_histoire; 24/10 petit_evenement (nouvelle de la famille ou des amis); 28/10 sans_histoire

### Daniel Öztürk (chauffeur Yango (résidence → aéroport Félix-Houphouët-Boigny))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : préparer une compétition ou un examen ; **souci** : fin de mois difficile, découvert bancaire ; **foyer** : en colocation
- **Secret (moteur seulement)** : se renseigne pour partir s'installer ailleurs (gravité 1)
- **Horaires** : règle « chauffeur », fuseau abidjan, décalage +24 min ; travail 06:24-18:24 (lun, mar, mer, jeu, sam, dim), trajet 20 min ; sommeil 22:24-05:24
- **Derniers événements** : 01/10 petit_evenement (service rendu ou reçu); 07/10 sans_histoire; 16/10 avancee_objectif (démarche pour son objectif : préparer une compétition ou un examen); 23/10 sans_histoire; 31/10 sans_histoire
