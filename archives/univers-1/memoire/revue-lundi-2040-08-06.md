# Revue du lundi — 06/08/2040 (semaine ISO 31 écoulée)

## 1. Bilan de la semaine écoulée
- **Réussi** : retour au Luxembourg joué au jour près (vol, Findel, retrouvailles) ; réactions de Sandra tirées en T8 et T7b, sans moralisation ;
  constats comptables d'Estelle chiffrés à partir des fichiers (pénalités, ITS non retenu, frais de la dotation) ; paiement instantané de l'UEMOA
  intégré ; bulletin d'impôt luxembourgeois au courrier ; synthèse W31 écrite le dimanche soir.
- **Erreurs trouvées et corrigées** : fiche complète du 03/08 oubliée, faite le 04/08 (n° 40) ; la mère de Sandra placée à Esch au lieu de
  Differdange (n° 41) ; un quartier inventé pour la mère d'Aïcha, corrigé avant publication.
- **Tics d'écriture relevés** : « le message est lu… pas de réponse » répété ; « l'odeur de lessive » trois tours de suite ; ouvertures en
  « Dehors, … » ; la valise « qui attend » au pied de l'escalier ; à varier.
- **Fils à surveiller** : fibre Orange au QG (14/08, à confirmer) ; statut de sous-traitant de Bertin ; M. Tanoh (propriétaire du QG) ;
  date d'arrivée d'Esther N'Guessan ; avis de Me Kouamé sur les évaluations mensuelles (demandé le 03/08) ; **déclaration de l'investissement
  étranger** (dans le mois qui suit la réception des fonds du 31/07, donc vers le 31/08) ; pilotes de Grace (école, hôtel) ; offre écrite promise
  à Estelle ; régularisation au Luxembourg (secrétariat le 13/08).
- **Audit des jets** (`python outils/audit_jets.py`) : 137 tirages de table, 0 non-conformité ; issues frontales : 5 observées pour 2,3 attendues
  (dont T7c frontal_refus 4/2,0) ; T8 : creuse_doucement 13/7,7 et releve_esquive 3/6,7 (hasard, à surveiller) ; **135 dérogations**, presque toutes
  pour des délais de réponse ou des heures de messages.

## 2. Idées de réalisme et d'immersion proposées (à valider)
1. **A18 actif** : incident de transport (taxi, panne, retard ; 15 % par semaine) : semaine de voyages (Lisbonne, Mindelo, Sal).
2. **A03 actif** : maladie ou accident d'un des enfants de Sandra (8 % par semaine) : les petits sont chez leur grand-mère pendant le voyage.
3. **A07 actif** : panne de réseau ou de banque en ligne (15 % par semaine) : William pilote OSIA à distance depuis le Cap-Vert.
4. **A12 actif** : fuite d'information (salaires, avances, statut de William ; 5 % par semaine) : l'histoire du 23/07 circule déjà au QG.
5. **Table des délais (proposition, à valider par l'utilisateur)** : une petite table T10 pour l'heure et le délai des réponses et des messages
   spontanés (proches, équipe, prestataires), afin de remplacer les dérogations au cas par cas ; elle ne tire jamais le contenu d'une réaction.

## 3. Décision de l'utilisateur
**William a validé les cinq idées (06/08, vers 05h00, au comptoir de Findel)** : « Je valide toutes tes cinq idées. »

## 4. Application
- **Tirage des aléas actifs de la semaine** (`python outils/tirage_aleas.py 2040-08-06`, consigné) : un aléa déclenché, joué au jour tiré, non
  révélé au joueur.
- **Vie hors d'Abidjan** : expéditeur et jour tirés (jets 59.8 et 65.1), non révélés.
- T4 et T5 du 05/08 : affaire Grace : aucune escalade, fuite interne (9 informés) ; relation William–Aïcha : rien (3).
- **Après validation (06/08, 05h02)** : A03, A07, A12, A18 passés « actifs » et tirés pour la semaine (A03 NON 61.7 ; A07 NON 24.6 ; A12 NON 25.8 ; A18 NON 66.6) ; **table T10 (délais) installée** (M70-M74 ; `outils/jet.py --table T10`), premières utilisations : Oasis (dans_l_heure) et Sandra (rapide).
