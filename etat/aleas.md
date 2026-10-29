# Catalogue des aléas (hasard, maladies, imprévus) — créé le 22/07/2040

> **Univers 2 (redémarrage du 11/10/2026 ; départ le samedi 14/07/2040)** : le pack actif est conservé tel que validé (A01 A02 A03 A04 A05 A06 A07 A09 A12 A13
> A17 A18) et tiré chaque lundi. Plusieurs aléas visent le contexte de l'univers 1 (équipe d'OSIA, enfants de Sandra, délestages
> d'Abidjan, fournisseurs de Vridi) : tant que l'univers 2 n'a pas de contexte équivalent, un aléa déclenché sans objet est
> consigné « sans objet » et n'est pas joué. Adaptation du pack à proposer à la revue du lundi n° 1 (lundi 16/07/2040 ; avant : 23/07 ; proposition A19-A30 dans
> `memoire/propositions-2026-10-11.md`) ; seul
> l'utilisateur la valide.

> **16/07/2040 (revue du lundi n° 1 de l'univers 2 ; « Je valide absolument tout », 12/10/2026) — pack de l'univers 2 : A01, A03,
> A04, A05 et A06 (Abidjan) passent au statut « univers 1 » (plus tirés) ; A19 à A30 (proposition P02) et A31, A32 (idée I4,
> santé en voyage, chiffrée sur des études de cohortes de voyageurs) deviennent actifs ; A02, A07, A09, A12, A13, A17, A18 restent
> actifs.** Un aléa tiré un jour où il n'a pas d'objet (A20 pendant les vacances, A25 sans entraînement, A31 et A32 hors voyage,
> A29 sans conduite) est consigné « sans objet » et n'est pas joué.
> **06/08/2040 — William a validé A03, A07, A12 et A18 (revue du lundi n° 3) : pack actif A01 A02 A03 A04 A05 A06 A07 A09 A12 A13 A17 A18.**
> **30/07/2040 — William a validé A02, A05 et A17 (revue du lundi n° 2) : pack actif A01 A02 A04 A05 A06 A09 A13 A17.**
> **23/07/2040 — William a validé le pack : A01, A04, A06, A09, A13 sont ACTIFS.** Les autres restent « proposé »
> (à réexaminer chaque lundi).

> Règle du lundi (CLAUDE.md §12) : chaque lundi simulé, on analyse la semaine écoulée et on décide ensemble de
> nouveaux éléments de réalisme. Ce fichier est la **réserve d'idées** et le **catalogue des aléas**.
> - Statut **proposé** = idée non validée : **jamais tirée**. Statut **actif** = validée par l'utilisateur.
> - Les probabilités sont **indicatives** (à calibrer en revue du lundi). Tirage : `python outils/tirage_aleas.py AAAA-MM-JJ`
>   (vrai hasard ; résultat consigné dans `memoire/tirages-aleas.md` ; ne jamais rejouer un tirage).
> - Un aléa ne tombe jamais « pour punir » ni n'est effacé « pour plaire » : il s'ajoute au monde, les personnages réagissent
>   selon leur caractère. Il n'écrase pas William sauf si le tirage et la situation s'y prêtent.

| ID | Événement | Probabilité par semaine | Statut | Effets / conditions |
|---|---|---|---|---|
| A01 | Maladie d'un membre de l'équipe (paludisme, gastro, typhoïde) | 10 % | actif | (avant : « univers 1 » → maintenant : actif à Abidjan, P39 validée le 29/10/2026)  Absence de 2 à 5 jours ; qui est touché : tirer parmi les salariés ; saison des pluies = plus fréquent |
| A02 | Problème de santé d'un proche d'un personnage (ex. mère d'Aïcha, tension) | 8 % | actif | Personnage moins disponible, humeur, demande d'absence ou d'avance |
| A03 | Maladie ou accident d'un des enfants de Sandra | 8 % | univers 1 | Sandra indisponible, échange d'argent ou d'aide possible, test pour William |
| A04 | Délestage / coupure d'électricité prolongée | 25 % | actif | (avant : « univers 1 » → maintenant : actif à Abidjan, P39 validée le 29/10/2026)  QG sans groupe électrogène (hors service) ; chantiers et visites perturbés |
| A05 | Fortes pluies / inondation | 15 % | actif | (avant : « univers 1 » → maintenant : actif à Abidjan, P39 validée le 29/10/2026)  Transports et chantiers retardés (Abidjan, saison des pluies) |
| A06 | Retard fournisseur ou douane (NVR, onduleurs, batteries) | 30 % | actif | (avant : « univers 1 » → maintenant : actif à Abidjan, P39 validée le 29/10/2026)  Délai supplémentaire ; l'excuse du fournisseur est plausible mais pas toujours vraie |
| A07 | Panne réseau (fibre, 4G) ou banque en ligne | 15 % | actif | Retard d'un virement, d'un envoi, d'un rapport |
| A08 | Contrôle ou courrier administratif (Inspection du travail, CNPS, impôts) | 5 % | proposé | Dossiers incomplets (CNPS, salaires de juin) ressortent |
| A09 | Erreur administrative (virement mal affecté, pièce perdue, nom mal orthographié) | 10 % | actif | Correction longue, agacement |
| A10 | Offre concurrente ou démission d'un cadre | 3 % | proposé | Négociation, révision salariale, ou départ |
| A11 | Cérémonie familiale ou décès dans l'entourage d'un salarié (funérailles ivoiriennes) | 4 % | proposé | Absence de plusieurs jours, contribution financière attendue |
| A12 | Fuite d'information (salaires, avances, statut de William) | 5 % | actif | Rumeur, tension d'équipe, risque pour William |
| A13 | Opportunité commerciale inattendue (recommandation, appel d'un prospect) | 10 % | actif | Nouvelle piste (rarement un contrat tout de suite) |
| A14 | Incident de sécurité au QG (intrusion, vol, alarme) | 3 % | proposé | Moussa et le gardien de jour, SécuTech si installé |
| A15 | Variation de prix du matériel ou du change | 8 % | proposé | Devis à revoir, marge rognée |
| A16 | Grève de transport ou embouteillage exceptionnel | 5 % | proposé | Retards de personnes, rendez-vous manqués |
| A17 | William lui-même malade ou épuisé (fatigue, gastro) | 5 % | actif | Jour de repos forcé, décisions moins bonnes |
| A18 | Incident de transport (taxi, panne, retard) | 15 % | actif | Retard à un rendez-vous |
| A19 | Rhume, angine ou gastro de William | 5 % | actif | Un adulte attrape 2 à 4 rhumes par an ; 1 à 4 jours diminué (corps.py noter --type malade) |
| A20 | Perturbation des trajets frontaliers (bus en retard, A4 ou N4 bouchée, travaux) | 20 % | actif | Semaines de travail (F029) ; sans objet pendant les vacances ou à l'étranger |
| A21 | Panne domestique (chauffe-eau, électroménager, fuite) | 4 % | actif | Maison ancienne ; si William est absent, découverte au retour |
| A22 | Courrier administratif (impôts français ou luxembourgeois, CNS, mairie, banque) | 10 % | actif | Frontalier : deux administrations ; boîte aux lettres (lue au retour si absent) ou courriel |
| A23 | Tentative d'arnaque (SMS de faux colis, faux conseiller bancaire, faux site) | 15 % | actif | Très courant ; William voit le message et décide |
| A24 | Souci de voisinage (bruit, travaux, haie, stationnement) | 5 % | actif | Maison mitoyenne ; à l'étranger, seulement par un message d'un voisin |
| A25 | Blessure légère à l'entraînement (entorse, côte, doigt) | 1 % | actif | ≈ 1,4 blessure pour 1 000 h de MMA (étude de 2025) ; sans objet sans entraînement |
| A26 | Imprévu d'argent (amende, réparation, cadeau, cotisation) | 6 % | actif | Montant tiré dans une fourchette réaliste (prix.py) |
| A27 | Signe d'un ancien (collègue, élève devenu adulte, connaissance) | 8 % | actif | Réseau d'un homme de 35 ans ; jamais les parents (ponts coupés) |
| A28 | Courriel ou appel du lycée pendant les vacances (réunion de rentrée, ajournements, emploi du temps) | 10 % (juillet), 30 % (fin août) | actif | Le moteur règle le taux selon la période (le tirage lit le premier) |
| A29 | Contrôle routier ou radar | 3 % | actif | Seulement un jour où William conduit |
| A30 | Occasion inattendue (proposition de cours particuliers, invitation, bon plan) | 8 % | actif | Nouvelle piste ; rien n'est acquis |
| A31 | Diarrhée du voyageur ou intoxication alimentaire (à l'étranger) | 12 % | actif | Seulement les jours à l'étranger ; 14 % la première semaine, 10 % ensuite (cohorte de voyageurs en Thaïlande : 14 % à 7 jours, 23,5 % à 14 jours, 33 % à 28 jours) ; 1 à 3 jours diminué |
| A33 | Course en taxi ou en VTC à l'étranger (Manille, Séoul) : compteur refusé et prix fixe, détour ; chauffeur VTC qui annule | à chaque course, pas par semaine | par course | Validé par l'utilisateur le 14/10/2026 (P26) : taxi au compteur 70 % compteur, 20 % prix fixe demandé, 10 % détour (table T24a) ; VTC 90 % arrive, 10 % annule (table T24b) ; tiré par `courses.py commander`, jamais par `tirage_aleas.py` |
| A32 | Dengue (à l'étranger, zone d'endémie) | 0,2 % | sans objet à Séoul | Seulement les jours à Manille ; ≈ 0,2 % par semaine en saison de transmission (modèle pour la Thaïlande : 0,2 % pour 7 jours, 0,81 % pour 30 jours) ; fièvre 4 à 10 jours après la piqûre |
| A34 | Coup de chaleur ou déshydratation de William (un jour d'effort quand le maximum dépasse 35 °C) | 6 % par jour concerné | par jour de chaleur | Validé par l'utilisateur le 22/10/2026 (R3, revue n° 1 de l'univers 3) ; tiré chaque jour où le maximum de Séoul dépasse 35 °C (aussi le jour de l'arrivée) par `tour.py fin`, jamais par `tirage_aleas.py` ; malaise léger, une demi-journée perdue |
| A35 | Surfacturation ou arnaque visant un touriste (taxi, boutique, bar) | 5 % par semaine à l'étranger | actif | Validé le 22/10/2026 (R3) ; montant tiré dans une fourchette réaliste (prix.py) ; le contrôle des taxis de Séoul existe (F093) |
| A36 | Malentendu de langue (adresse mal comprise, commande erronée, document en coréen) | 10 % par semaine à l'étranger | actif | Validé le 22/10/2026 (R3) ; jamais de refus, un détour ou un retard |
| A37 | Embouteillage, pont saturé ou route coupée à Abidjan (un trajet de William ou de l'équipe prend une à deux heures de plus) | 30 % | actif | Seulement quand William ou l'équipe circule à Abidjan ; ajouté le 29/10/2026 (P39, validée par l'utilisateur) |
| A38 | Contrôle routier ou guichet : un agent sollicite un « geste » (2 000 à 10 000 FCFA) | 10 % | actif | Seulement à Abidjan ; William peut refuser (délai, paperasse, ton qui se durcit) ; jamais de mode d'emploi réel |
| A39 | Paludisme de William (séjour en zone d'endémie) | 0,5 % | actif | Par semaine passée à Abidjan sans traitement préventif (divisé par dix avec) ; incubation de 7 à 30 jours : les premiers symptômes peuvent survenir APRÈS le retour (fièvre, frissons) ; consultation, test, traitement |
| A40 | Départ d'un directeur pendant sa période d'essai (préavis court, recrutement à refaire) | 5 % par mois et par directeur | actif | À partir du 1er octobre 2041, pour chaque directeur en période d'essai ; validé le 29/10/2026 (P43, revue n° 6) |
| A41 | Retard de paiement d'un client (15 à 90 jours) | 30 % par facture | actif | Dès la première facture de SOLEIL B2B CI ; validé le 29/10/2026 (P44, revue n° 6) |
