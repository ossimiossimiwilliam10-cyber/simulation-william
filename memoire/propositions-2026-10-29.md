# Propositions P37 à P41 : un univers plus vivant et plus réaliste (29/10/2026)

> Rédigées par Claude à la demande de l'utilisateur (« est-ce qu'il n'y a pas un moyen pour rendre l'univers encore plus vivant, encore plus
> réaliste ? […] si on force une interaction, ça ne va pas être réaliste »). Rien n'est installé avant sa validation. Principe commun : rien n'est
> forcé ; tout est TIRÉ, et l'issue la plus fréquente reste « rien ne se passe ».

## Constat
- Ce qui marche : personnages tirés selon la démographie, vies propres quotidiennes, initiatives envers William, réponses à l'heure de leur routine,
  argent, agenda, météo, état caché, contrôles automatiques.
- Ce qui manque le plus : (1) les personnages vivent surtout autour de William et ne se parlent presque pas entre eux, donc pas de rumeurs ni
  d'alliances qui naissent d'elles-mêmes ; (2) les affaires avancent trop vite et trop facilement (en un mois : société, quatre directeurs, un QG ;
  dans la vraie vie, chaque étape prend des semaines et une bonne part dérape) ; (3) Abidjan n'a ni aléas propres, ni courses, ni portefeuille en FCFA.

## Propositions
- **P37 — Vie sociale entre personnages (`monde_social.py`)** : chaque jour, pour chaque paire de personnages liés (`etat/liens.csv` : collègues,
  famille, club, voisins, équipe), une probabilité de contact selon leurs routines et la force du lien ; issue tirée dans une table : rien (le plus
  souvent), échange banal, information transmise, tension, service rendu. Ce qu'un personnage sait (`etat/savoir.csv`) circule selon son caractère
  (bavard : il répète ; discret : il garde). William ne le voit que par des traces : un message, une allusion, un changement de ton.
- **P38 — Lenteur réelle des affaires** : chaque démarche (immatriculation, compte bancaire, CNPS, impôts, abonnements CIE et SODECI, autorisations,
  livraisons, travaux) devient un front à paliers (`fronts.py`) avec des délais et des incidents tirés (pièce manquante, second passage, agent absent,
  frais imprévus) ; les engagements des personnes (prise de poste, promesse de références) se tiennent ou se défont selon leur fiabilité tirée.
- **P39 — Aléas d'Abidjan** : réactiver et compléter ceux retirés à l'univers 2 (A01, A03 à A06) : délestages, embouteillages et ponts, pluies et
  inondations, contrôles routiers, sollicitation d'un « geste » par un agent (que William peut refuser), paludisme (incubation de 7 à 30 jours : il peut
  se déclarer après le retour).
- **P40 — Courses et portefeuille à Abidjan** (une application par besoin, §14) : Yango, taxis compteur et woro-woro, prix par trajet et par heure,
  paiement en espèces ou en mobile money, chauffeur tiré (A33) ; retraits en FCFA et frais de la carte hors zone euro ; chaque course au grand livre.
- **P41 — Concurrence et trésorerie de la société** : deux ou trois installateurs solaires concurrents (fictifs, tirés) qui réagissent à l'arrivée de
  Soleil B2B CI (prix cassés, débauchage, rumeurs, appels d'offres perdus) ; trésorerie de la société suivie mois par mois (salaires, loyer, CNPS)
  face à la première tranche de 60 000 €.

## Décision de l'utilisateur
- 29/10/2026 : « Je valide P37 à P41 » (avant : en attente → maintenant : validées et installées le même jour ; voir `outils/LISEZMOI.md` §7, consigne 8).

## Revue n° 6 (26/08/2041) : P42 à P44
- 29/10/2026 : « Je valide P42 à P44 » : rubrique « Rapports archivés » dans Gestion (P42), aléas A40 et A41 actifs (P43, P44).

## Revue n° 7 (16/09/2041) : P45 à P47
- 29/10/2026 : « Je valide les propositions de P45 à P47 » : calendrier du lycée joué en mode automatique (P45) ; fatigue de rentrée tirée (P46) ; tirage hebdomadaire T15 sur un collègue ou un élève qui évoque l'activité en Côte d'Ivoire (P47).

## Revue n° 8 (23/09/2041) : P48 à P50
- 29/10/2026 : « je valide les propositions P48 à P50 » : devis_solaire.py (P48), calendrier fiscal et social à l'agenda (P49), etat/moral-equipe.csv (P50).
