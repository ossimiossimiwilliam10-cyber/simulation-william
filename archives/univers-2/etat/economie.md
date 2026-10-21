# Économie du monde — règles moins complaisantes (univers 2 ; repris de l'univers 1 le 17/07/2040)

> Règle (revue du lundi, validée le 23/07/2040, univers 1) : l'argent et le marché ne coopèrent pas. Valeurs à recontrôler par
> recherche web au moment de chaque achat, négociation ou contrat (prix, délais, taux) ; les repères ci-dessous ne sont pas des
> faits vérifiés. Les paramètres propres à OSIA (marges, clients, charges) sont archivés : `archives/univers-1/etat/economie.md`.

## Paramètres de jeu
- **Prix** : projetés en 2040 à partir des données actuelles (≈ +30 à 40 %) ; toujours vérifiés au moment où ils comptent.
- **Parité fixe** : 1 € = 655,957 FCFA (si l'histoire repart vers la zone franc).
- **Contrats, ventes, recrutements, achats importants** : jamais du premier coup ; contre-propositions, délais, pièces
  manquantes. Une signature attendue se tire semaine après semaine (`python outils/jet.py "Signature <partie>" <proba>`).
- **Négociations** : la réponse d'une personne qui a un intérêt direct (salaire, prix, contrat) se tire en **T12**.
- **Frontalier** : William vit en France (Moselle) et travaille au Luxembourg : impôt sur le traitement au Luxembourg,
  résidence et taxes locales en France ; toute question fiscale se vérifie par recherche web avant d'être jouée.

## Règle de friction administrative (validée le 23/07/2040, univers 1)
Toute démarche à enjeu (banque, administration, notaire, assurance, employeur, impôts, fournisseur, artisan) fait l'objet d'un
**jet « deuxième passage demandé » à 30 %** (`python outils/jet.py "<démarche>" 30`) : justificatif manquant, refus, délai,
mauvais service. Le résultat est joué sans commentaire et consigné. Ne pas rejouer un jet. Un taux différent est possible si le
réalisme l'exige (ex. dossier incomplet connu d'avance : 100 %).
