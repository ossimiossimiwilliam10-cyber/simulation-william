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

### Clément Grandjean (membre régulier du club (sparring))
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : couple en crise ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : se renseigne pour partir s'installer ailleurs (gravité 1)
- **Horaires** : règle « etudiant », fuseau luxembourg, décalage +25 min ; travail 09:25-17:25 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:55-08:55
- **Derniers événements** : 26/06 tournant (naissance, mariage, décès ou retour d'un proche); 01/07 petit_evenement (dépense imprévue (cotisation imprévue)); 09/07 sans_histoire; 21/07 sans_histoire; 20/07 coup_dur (dispute sérieuse ou mauvaise nouvelle dans la famille)

### Min-ji (match Meeff Séoul)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : voyager loin une fois dans sa vie ; **souci** : loyer qui augmente ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : se renseigne pour partir s'installer ailleurs (gravité 1)
- **Horaires** : règle « independant_seoul », fuseau seoul, décalage -8 min ; travail 10:52-19:52 (lun, mar, mer, jeu, ven), trajet 20 min ; sommeil 01:22-09:22
- **Derniers événements** : —

### Soo-jin (match Tinder Séoul)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : maigrir ou reprendre le sport ; **souci** : fin de mois difficile, découvert bancaire ; **foyer** : en colocation
- **Secret (moteur seulement)** : a une condamnation ancienne (conduite en état d'ivresse) (gravité 2)
- **Horaires** : règle « bureau_seoul », fuseau seoul, décalage -20 min ; travail 08:40-18:40 (lun, mar, mer, jeu, ven), trajet 55 min ; sommeil 00:10-06:40
- **Derniers événements** : —

### Hye-won (match Meeff Séoul)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : réussir le concours de la fonction publique ou un examen de certification ; **souci** : solitude depuis un déménagement ; **foyer** : vit chez ses parents
- **Secret (moteur seulement)** : doit de l'argent à un proche (gravité 1)
- **Horaires** : règle « etudiant_seoul », fuseau seoul, décalage +9 min ; travail 10:09-17:09 (lun, mar, mer, jeu, ven), trajet 35 min ; sommeil 01:09-08:39
- **Derniers événements** : —

### Thiago Rocha (contact LinkedIn)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : mal de dos chronique ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : vote pour un parti qu'il n'avoue pas (gravité 1)
- **Horaires** : règle « bureau », fuseau bresil, décalage +20 min ; travail 09:20-17:50 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:50-07:20
- **Derniers événements** : —

### Lucas Mendes (contact LinkedIn)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : obtenir une promotion ou un poste plus stable ; **souci** : lenteur des licences et des raccordements au réseau électrique ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : prend des antidépresseurs (gravité 1)
- **Horaires** : règle « bureau », fuseau bresil, décalage -3 min ; travail 08:57-17:27 (lun, mar, mer, jeu, ven), trajet 40 min ; sommeil 23:27-06:57
- **Derniers événements** : —
