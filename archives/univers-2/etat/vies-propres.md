# Vies propres des personnages — fiches vivantes (univers 2 ; état au 14/07/2040, 08h37)

> **Mécanisme validé par l'utilisateur le 09/08/2040 (univers 1), repris dans l'univers 2** : chaque personnage récurrent vit
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
> - **Univers 2** : les fiches de l'univers 1 sont archivées (`archives/univers-1/etat/vies-propres.md`) ; aucun de ces
>   personnages n'existe ici. Une fiche se crée quand un personnage devient récurrent (deuxième apparition, ou lien durable).
> - **Depuis le 11/10/2026** : un personnage nouveau se crée avec `python outils/personnage.py nouveau --contexte … --role …`
>   (tirage selon la démographie réelle ; il écrit lui-même la fiche ci-dessous, `personnes/` et `etat/personnages.csv`).

## Fiches

> Section RÉGÉNÉRÉE par `python outils/monde_vivant.py fiches` (appelé par `tour.py fin`) : ne pas éditer à la main ; les événements complets sont dans `etat/vies.csv`.

### Clément Grandjean (membre régulier du club (sparring))
- **Lien avec William** : contact_recent (whatsapp)
- **Objectif** : finir de rénover sa maison ; **souci** : couple en crise ; **foyer** : en couple, sans enfant
- **Secret (moteur seulement)** : se renseigne pour partir s'installer ailleurs (gravité 1)
- **Horaires** : règle « etudiant », fuseau luxembourg, décalage +25 min ; travail 09:25-17:25 (lun, mar, mer, jeu, ven), trajet 30 min ; sommeil 00:55-08:55
- **Derniers événements** : 21/07 petit_evenement (dépense imprévue (facture d'électricité plus lourde))

### Julia Dimaculangan (profil d'application de rencontre (Manille))
- **Lien avec William** : rejete_par_william (rencontres) · William lui écrit le 19/07 à 23h27 qu'il n'est « plus du tout intéressé »
- **Objectif** : acheter un logement (ou un plus grand) ; **souci** : contrat de six mois non renouvelé (« endo ») ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : envoie presque tout son salaire à ses parents en province (gravité 1)
- **Horaires** : règle « centre_appels_nuit », fuseau manille, décalage -6 min ; travail 21:54-06:54 (lun, mar, mer, jeu, ven), trajet 60 min ; sommeil 08:24-15:24
- **Derniers événements** : 19/07 tournant (diagnostic, guérison, grossesse ou opération)

### Shane Lopez (profil d'application de rencontre (Manille))
- **Lien avec William** : actif (rencontres)
- **Objectif** : rembourser ses dettes ; **souci** : trois heures de trajet par jour dans les embouteillages ; **foyer** : parent isolé
- **Secret (moteur seulement)** : a un enfant qu'il ne voit plus (gravité 3)
- **Horaires** : règle « serveur_soir », fuseau manille, décalage +3 min ; travail 15:03-23:03 (lun, mer, jeu, ven, sam, dim), trajet 90 min ; sommeil 01:03-09:03
- **Derniers événements** : 19/07 sans_histoire

### Hannah De Leon (profil d'application de rencontre (Manille))
- **Lien avec William** : bloque (rencontres)
- **Objectif** : se faire une place dans le milieu (club, lycée, quartier) ; **souci** : chef difficile ; **foyer** : vit seul(e)
- **Secret (moteur seulement)** : vote pour un parti qu'il n'avoue pas (gravité 1)
- **Horaires** : règle « infirmier_soir », fuseau manille, décalage +26 min ; travail 15:26-23:26 (lun, mar, jeu, ven, sam), trajet 45 min ; sommeil 01:26-08:56
- **Derniers événements** : 18/07 sans_histoire

### Kiara Reyes (profil d'application de rencontre (Manille))
- **Lien avec William** : enjeu (rencontres) · rendez-vous proposé par William pour le samedi 21/07 à son hôtel (réponse de Kiara attendue, A027)
- **Objectif** : décrocher un poste stable dans un centre d'appels ; **souci** : dette auprès d'un prêteur au jour le jour (« 5-6 ») ; **foyer** : parent isolé
- **Secret (moteur seulement)** : a une condamnation ancienne (conduite en état d'ivresse) (gravité 2)
- **Horaires** : règle « centre_appels_nuit », fuseau manille, décalage +26 min ; travail 22:26-07:26 (lun, mar, mer, jeu, ven), trajet 60 min ; sommeil 08:56-15:56
- **Derniers événements** : 19/07 sans_histoire

### Simão Pinto (agent d'enregistrement de Lufthansa (prestataire d'assistance au sol) à l'aéroport de Findel)
- **Lien avec William** : aucun (whatsapp)
- **Objectif** : mettre de l'argent de côté pour ses vieux jours ; **souci** : insomnies ; **foyer** : en couple, avec enfants
- **Secret (moteur seulement)** : a raté un examen important qu'il dit avoir réussi (gravité 2)
- **Horaires** : règle « aeroport », fuseau luxembourg, décalage +1 min ; travail 05:01-13:31 (lun, mer, jeu, ven, dim), trajet 30 min ; sommeil 21:31-04:01
- **Derniers événements** : 22/07 sans_histoire
