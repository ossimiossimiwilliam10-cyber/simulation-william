# Propositions du 14/10/2026 (à valider par l'utilisateur)

> Contexte : demande de l'utilisateur du 14/10/2026 (date réelle), avant le tour n° 29 : rendre l'univers « le plus vivant et
> réaliste que possible », « indépendant », « pas moral, réaliste », et une simulation « surtout informatique, avec un contrôle de
> l'IA », pour limiter la dépense d'utilisation. Les outils sont installés (voir `outils/LISEZMOI.md`, section du 14/10/2026).
> Ce qui suit touche les tables ou les mécanismes validés : **rien n'entre en vigueur sans l'accord de l'utilisateur**, sauf P22,
> appliquée à titre provisoire (elle ne change aucune table, seulement le rythme des tirages) et réversible.

## P22. Rythme du monde vivant (appliqué à titre provisoire)
- **Chaque jour** : T11 (vie propre), puis T13 si besoin, pour les personnages en lien avec William (`etat/liens.csv` : actif,
  proche, enjeu, rejeté par William, rejet de sa part) ; T14 (initiative envers William, heure en T10) pour actif, proche, enjeu,
  rejeté par William ; jamais quand une réponse de ce personnage est déjà programmée dans les 72 heures.
- **Une fois par semaine** (jour tiré) : T11 pour tous les autres (entourage pré-généré, profils de l'application, figurants).
- Pourquoi : à un T11 par jour, chacune des quelque 70 personnes aurait un « tournant » (3 %) environ une fois par mois et un « coup
  dur » (7 %) deux fois par mois ; à un par semaine, un tournant tous les huit mois environ, ce qui est proche de la vie réelle.
- Choix : **(a)** valider ; **(b)** tout le monde chaque jour (ancien rythme) ; **(c)** autre rythme.

## P23. Table T21c — « j'aime » spontanés reçus par William (chaque jour où il est inscrit)
| Issue | % | En scène |
|---|---|---|
| aucun | 45 | Rien de nouveau. |
| un | 35 | Un profil de la ville l'a aimé (tiré par `rencontres.py`, intention cachée selon la loi déjà validée). |
| deux | 15 | Deux profils. |
| trois_ou_plus | 5 | Trois profils (ou plus : un par tranche de 5 au-dessus de 95 au jet). |
- Modificateurs proposés : **M100** abonnement payant ou mode voyage actif (+10 « un », +5 « deux », −15 « aucun ») ; **M101** profil
  d'un étranger aisé dans une ville d'Asie du Sud-Est (intérêt sincère ou calculé : +8 « un », +4 « deux », −12 « aucun »).

## P24. Table T23 — Évolution d'une intention cachée (profil « aide financière », « arnaque » ou « travail sexuel »)
Tirée à chaque nouvel échange suivi (message de William après au moins un jour sans parler) et après chaque rencontre en personne.
| Issue | % | En scène |
|---|---|---|
| rien_encore | 55 | La conversation reste ordinaire. |
| allusion | 20 | Un souci d'argent évoqué sans demande (loyer, enfant malade, téléphone cassé, frais de transport). |
| demande_directe | 15 | Une somme précise, un envoi par GCash ou par une agence de transfert. |
| proposition | 7 | Arrangement proposé (« allowance » mensuelle ; rendez-vous tarifé si « travail sexuel »). |
| disparition | 3 | « Arnaque » : profil supprimé ou silence après un paiement ou une demande refusée. |
- Modificateurs proposés : **M102** rencontre en personne déjà faite (+10 « demande_directe », −10 « rien_encore ») ; **M103** William a
  déjà donné de l'argent (+15 « demande_directe », −15 « rien_encore ») ; **M104** William a mis en avant sa situation financière (+5
  « allusion », −5 « rien_encore »).

## P25. Table T21d — Match resté sans échange depuis 7 jours (chaque semaine)
| Issue | % | En scène |
|---|---|---|
| reste | 70 | Le match reste dans la liste. |
| retire | 25 | Elle retire le match (la discussion disparaît). |
| bloque | 5 | Elle le bloque. |

## P26. Aléa A33 — Courses en taxi à Manille (chaque course en taxi au compteur ; les VTC ont leur ligne)
- Taxi au compteur : compteur mis 70 % ; prix fixe demandé au départ 20 % (« 500 pesos, sir, traffic ») ; détour ou compteur
  « rapide » 10 %. VTC : le chauffeur annule avant d'arriver 10 % (nouvelle attente, prix recalculé).

## Information (aucune validation requise, CLAUDE.md §14)
- Deux applications ajoutées au téléphone : **Portefeuille** (espèces, taux du jour, convertisseur, distributeurs, retrait préparé)
  et **Courses** (Grab et taxis à Manille : prix, attente, durée ; installation de Grab, carte enregistrée, commande).
- Réponses et initiatives des personnages : l'heure suit désormais leur routine (sommeil, travail, trajets : `outils/routines.py`) ;
  les jours et minutes sont des sous-tirages de procédure, plus des jets libres en dérogation.
- Météo de Manille : typhons et mousson renforcée tirés sur la climatologie (`outils/tropiques.py`), alertes dans l'application Météo.
- Nouvelles du monde : la section hebdomadaire de `etat/monde.md` s'écrit seule chaque lundi (`outils/actualites.py`).
