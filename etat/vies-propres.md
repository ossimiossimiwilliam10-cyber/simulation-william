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

### Thiago Alves (coach de musculation du club)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : voyager loin une fois dans sa vie ; **souci** : mal de dos chronique ; **foyer** : parent isolé
- **Secret (moteur seulement)** : consulte un psychologue (gravité 1)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +3 min ; travail 09:03-17:33 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:33-07:03
- **Derniers événements** : 08/07 sans_histoire; 20/07 petit_evenement (nouvelle de la famille ou des amis); 18/07 sans_histoire; 22/07 petit_evenement (bouchons sur l'A4 et la frontière); 30/07 petit_evenement (achat (cadeau d'anniversaire))

### Mariana Oliveira (membre régulière du club (sparring))
- **Lien avec William** : contact_recent (whatsapp)
- **Objectif** : obtenir la nationalité luxembourgeoise ; **souci** : contrat de travail qui se termine bientôt ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : fume en cachette alors qu'il dit avoir arrêté (gravité 1)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage -17 min ; travail 08:43-17:13 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:13-06:43
- **Derniers événements** : 09/07 sans_histoire; 18/07 petit_evenement (querelle courte); 21/07 petit_evenement (achat (vêtements)); 27/07 petit_evenement (querelle courte); 03/08 sans_histoire

### Clément Grandjean (membre régulier du club (sparring))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : couple en crise ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : se renseigne pour partir s'installer ailleurs (gravité 1)
- **Horaires** : règle « etudiant », fuseau luxembourg, décalage +25 min ; travail 09:25-17:25 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:55-08:55
- **Derniers événements** : 09/07 sans_histoire; 21/07 sans_histoire; 17/07 coup_dur (malade (mal de dos)); 28/07 avancee_objectif (démarche pour son objectif : finir de rénover sa maison); 31/07 sans_histoire

### Arthur Kieffer (membre régulier du club (sparring))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : trouver quelqu'un et se poser ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : prend des antidépresseurs (gravité 1)
- **Horaires** : règle « etudiant », fuseau luxembourg, décalage +4 min ; travail 09:04-17:04 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:34-08:34
- **Derniers événements** : 12/07 coup_dur (malade (mal de dos)); 20/07 petit_evenement (chantier d'été qui bloque la rue); 15/07 sans_histoire; 28/07 coup_dur (prêt à un proche jamais rendu); 04/08 petit_evenement (nouvelle de la famille ou des amis)

### Eugène Doumbia (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : faire croître son bureau d'études avec des clients internationaux ; **souci** : voisin bruyant ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : cherche un autre travail en cachette (gravité 1)
- **Horaires** : règle « bureau », fuseau abidjan, décalage +11 min ; travail 09:11-17:41 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:41-07:11
- **Derniers événements** : 19/07 petit_evenement (querelle courte); 24/07 sans_histoire; 02/08 sans_histoire

### Nadège Kouamé (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : burn-out qui couve ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage +1 min ; travail 09:01-17:31 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:31-07:01
- **Derniers événements** : 19/07 petit_evenement (dépense imprévue (réparation du téléphone)); 23/07 petit_evenement (querelle courte); 29/07 sans_histoire

### Jean-Baptiste Tuo (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : obtenir un poste de direction dans une grande entreprise ; **souci** : dettes de jeu ; **foyer** : en couple, enfants partis
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage -7 min ; travail 08:53-17:23 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:23-06:53
- **Derniers événements** : 20/07 sans_histoire; 26/07 petit_evenement (dépense imprévue (frais de scolarité)); 01/08 sans_histoire

### Sandrine Cissé (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : faire croître son bureau d'études avec des clients internationaux ; **souci** : un parent âgé dont la santé décline ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : fume en cachette alors qu'il dit avoir arrêté (gravité 1)
- **Horaires** : règle « bureau », fuseau abidjan, décalage -28 min ; travail 08:32-17:02 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:02-06:32
- **Derniers événements** : 16/07 coup_dur (panne, coupure ou souci de logement); 22/07 petit_evenement (achat (vêtements)); 02/08 petit_evenement (querelle courte)

### Hervé Touré (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : se faire une place dans le milieu (club, lycée, quartier) ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage +18 min ; travail 09:18-17:48 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:48-07:18
- **Derniers événements** : 15/07 sans_histoire; 25/07 coup_dur (maladie ou accident de son enfant); 01/08 sans_histoire

### Franck Konan (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un terrain et construire sa maison à Abidjan ; **souci** : voiture qui lâche, pas d'argent pour la remplacer ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage +14 min ; travail 09:14-17:44 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:44-07:14
- **Derniers événements** : 16/07 sans_histoire; 24/07 sans_histoire; 31/07 avancee_objectif (démarche pour son objectif : acheter un terrain et construire sa maison à Abidjan)

### Yannick N'Guessan (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : fin de mois difficile, découvert bancaire ; **foyer** : parent isolé
- **Secret (moteur seulement)** : —
- **Horaires** : règle « sans_travail », fuseau abidjan, décalage -13 min ; pas d'horaires de travail ; sommeil 22:47-06:47
- **Derniers événements** : 25/07 sans_histoire; 31/07 sans_histoire

### Solange Gnagne (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : trouver quelqu'un et se poser ; **souci** : embouteillages et trajets de deux heures entre Abidjan et son travail ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage +24 min ; travail 09:24-17:54 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:54-07:24
- **Derniers événements** : 24/07 petit_evenement (croisement, visite ou conversation de voisinage); 31/07 petit_evenement (dépense imprévue (réparation de la moto))

### Jonathan Ouattara (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : un parent âgé dont la santé décline ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +1 min ; travail 09:01-17:31 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:31-07:01
- **Derniers événements** : 24/07 coup_dur (malade (grippe)); 03/08 petit_evenement (service rendu ou reçu)

### Mohamed Coulibaly (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : contrat de travail qui se termine bientôt ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage -21 min ; travail 08:39-17:09 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:09-06:39
- **Derniers événements** : 23/07 sans_histoire; 04/08 sans_histoire

### Maïmouna Koné (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : obtenir une promotion ou un poste plus stable ; **souci** : voisin bruyant ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « enseignant », fuseau luxembourg, décalage -15 min ; travail 07:45-15:45 (lun, mar, mer, jeu, ven), trajet 45 min ; sommeil 22:45-06:15
- **Derniers événements** : 22/07 sans_histoire; 31/07 avancee_objectif (décision prise pour son objectif : obtenir une promotion ou un poste plus stable)

### Brice Tapé (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : passer plus de temps avec ses enfants ; **souci** : problème de santé qu'il refuse de faire examiner ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage -21 min ; travail 08:39-17:09 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:09-06:39
- **Derniers événements** : 23/07 sans_histoire; 01/08 petit_evenement (querelle courte)

### Kader Assi (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : préparer une compétition ou un examen ; **souci** : loyer qui augmente ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +30 min ; travail 09:30-18:00 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 00:00-07:30
- **Derniers événements** : 22/07 avancee_objectif (rendez-vous obtenu ou tenu pour son objectif : préparer une compétition ou un examen); 02/08 coup_dur (prêt à un proche jamais rendu)

### Boubacar Sylla (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : monter ou diriger une entreprise au pays ; **souci** : loyer qui augmente ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : a menti sur son diplôme ou son expérience (gravité 2)
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +9 min ; travail 09:09-17:39 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:39-07:09
- **Derniers événements** : 24/07 sans_histoire; 30/07 coup_dur (dispute sérieuse ou mauvaise nouvelle dans la famille)

### Cédric Soro (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : contrat de travail qui se termine bientôt ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage -5 min ; travail 08:55-17:25 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:25-06:55
- **Derniers événements** : 24/07 sans_histoire; 02/08 sans_histoire

### Landry Aka (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : préparer une compétition ou un examen ; **souci** : famille installée à l'étranger qui hésite à rentrer ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +28 min ; travail 09:28-17:58 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:58-07:28
- **Derniers événements** : 25/07 sans_histoire; 31/07 sans_histoire

### Fabrice Koffi (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : mettre de l'argent de côté pour ses vieux jours ; **souci** : mal de dos chronique ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage +12 min ; travail 09:12-17:42 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:42-07:12
- **Derniers événements** : 26/07 petit_evenement (croisement, visite ou conversation de voisinage); 04/08 sans_histoire

### Aboubacar Kouassi (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : dettes de jeu ; **foyer** : parent isolé
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage -19 min ; travail 08:41-17:11 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:11-06:41
- **Derniers événements** : 25/07 sans_histoire; 01/08 sans_histoire

### Ousmane Yéo (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : faire croître son bureau d'études avec des clients internationaux ; **souci** : coupures de courant et facture d'électricité lourde pour son activité ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage +20 min ; travail 09:20-17:50 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:50-07:20
- **Derniers événements** : 27/07 sans_histoire; 03/08 sans_histoire

### Mariam Brou (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : embouteillages et trajets de deux heures entre Abidjan et son travail ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau abidjan, décalage -26 min ; travail 08:34-17:04 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:04-06:34
- **Derniers événements** : 27/07 sans_histoire; 03/08 sans_histoire

### Damien Yao (répondant à l'annonce)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : rentrer en Côte d'Ivoire après des années à l'étranger ; **souci** : épargne et retraite à reconstituer avant un retour ; **foyer** : parent isolé
- **Secret (moteur seulement)** : —
- **Horaires** : règle « bureau », fuseau luxembourg, décalage +9 min ; travail 09:09-17:39 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:39-07:09
- **Derniers événements** : 22/07 avancee_objectif (formation, lecture ou conseil utile : rentrer en Côte d'Ivoire après des années à l'étranger); 04/08 petit_evenement (nouvelle de la famille ou des amis)

### Arsène Zadi (avocat(e) d'affaires à Abidjan (cabinet en liste restreinte))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : passer plus de temps avec ses enfants ; **souci** : clients qui paient avec des mois de retard ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : vote pour un parti qu'il n'avoue pas (gravité 1)
- **Horaires** : règle « bureau », fuseau abidjan, décalage -9 min ; travail 08:51-17:21 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:21-06:51
- **Derniers événements** : 25/07 avancee_objectif (somme reçue, économisée ou investie pour son objectif : passer plus de temps avec ses enfants); 01/08 avancee_objectif (décision prise pour son objectif : passer plus de temps avec ses enfants)

### Issouf Tano (avocat(e) d'affaires à Abidjan (cabinet en liste restreinte))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : trouver un partenaire européen pour financer un projet ; **souci** : tension avec la belle-famille ; **foyer** : en couple, enfants partis
- **Secret (moteur seulement)** : doit de l'argent à une tontine ou à un prêteur (gravité 1)
- **Horaires** : règle « bureau », fuseau abidjan, décalage -9 min ; travail 08:51-17:21 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:21-06:51
- **Derniers événements** : 26/07 coup_dur (maladie ou accident de son enfant); 04/08 sans_histoire

### Ismaël Gnamien (avocat(e) d'affaires à Abidjan (cabinet en liste restreinte))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : changer de métier ; **souci** : voisin bruyant ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : a fait une demande de crédit refusée (gravité 1)
- **Horaires** : règle « bureau », fuseau abidjan, décalage +22 min ; travail 09:22-17:52 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:52-07:22
- **Derniers événements** : 22/07 avancee_objectif (démarche pour son objectif : changer de métier); 01/08 sans_histoire
