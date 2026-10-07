# Catalogue des aléas (hasard, maladies, imprévus) — créé le 22/07/2040

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
| A01 | Maladie d'un membre de l'équipe (paludisme, gastro, typhoïde) | 10 % | actif | Absence de 2 à 5 jours ; qui est touché : tirer parmi les salariés ; saison des pluies = plus fréquent |
| A02 | Problème de santé d'un proche d'un personnage (ex. mère d'Aïcha, tension) | 8 % | actif | Personnage moins disponible, humeur, demande d'absence ou d'avance |
| A03 | Maladie ou accident d'un des enfants de Sandra | 8 % | proposé | Sandra indisponible, échange d'argent ou d'aide possible, test pour William |
| A04 | Délestage / coupure d'électricité prolongée | 25 % | actif | QG sans groupe électrogène (hors service) ; chantiers et visites perturbés |
| A05 | Fortes pluies / inondation | 15 % | actif | Transports et chantiers retardés (Abidjan, saison des pluies) |
| A06 | Retard fournisseur ou douane (NVR, onduleurs, batteries) | 30 % | actif | Délai supplémentaire ; l'excuse du fournisseur est plausible mais pas toujours vraie |
| A07 | Panne réseau (fibre, 4G) ou banque en ligne | 15 % | proposé | Retard d'un virement, d'un envoi, d'un rapport |
| A08 | Contrôle ou courrier administratif (Inspection du travail, CNPS, impôts) | 5 % | proposé | Dossiers incomplets (CNPS, salaires de juin) ressortent |
| A09 | Erreur administrative (virement mal affecté, pièce perdue, nom mal orthographié) | 10 % | actif | Correction longue, agacement |
| A10 | Offre concurrente ou démission d'un cadre | 3 % | proposé | Négociation, révision salariale, ou départ |
| A11 | Cérémonie familiale ou décès dans l'entourage d'un salarié (funérailles ivoiriennes) | 4 % | proposé | Absence de plusieurs jours, contribution financière attendue |
| A12 | Fuite d'information (salaires, avances, statut de William) | 5 % | proposé | Rumeur, tension d'équipe, risque pour William |
| A13 | Opportunité commerciale inattendue (recommandation, appel d'un prospect) | 10 % | actif | Nouvelle piste (rarement un contrat tout de suite) |
| A14 | Incident de sécurité au QG (intrusion, vol, alarme) | 3 % | proposé | Moussa et le gardien de jour, SécuTech si installé |
| A15 | Variation de prix du matériel ou du change | 8 % | proposé | Devis à revoir, marge rognée |
| A16 | Grève de transport ou embouteillage exceptionnel | 5 % | proposé | Retards de personnes, rendez-vous manqués |
| A17 | William lui-même malade ou épuisé (fatigue, gastro) | 5 % | actif | Jour de repos forcé, décisions moins bonnes |
| A18 | Incident de transport (taxi, panne, retard) | 15 % | proposé | Retard à un rendez-vous |
