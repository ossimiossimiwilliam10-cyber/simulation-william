# Économie du monde — règles moins complaisantes (créé le 23/07/2040)

> Règle (revue du lundi, validée le 23/07/2040) : l'argent et le marché ne coopèrent pas. Valeurs à recontrôler par
> recherche web au moment de chaque négociation ou contrat (prix, délais, taux) ; les chiffres ci-dessous sont des
> repères de jeu, pas des faits vérifiés.

## Paramètres de jeu
- Parité fixe : 1 € = 655,957 FCFA.
- **Marges planchers validées par William le 23/07** : clinique de Marcory 25 % (brute) ; villa Riviera 20 % ; toute offre en
  dessous : soumise à William ; remise maximale négociée par Grace : 5 %.
- **Concurrence** : villa Riviera : deux devis concurrents ; les clients comparent, négocient, exigent des remises.
- **Délais de paiement clients (repère de jeu)** : acompte de 30 à 50 % à la commande ; solde à réception ou à la recette ;
  un client institutionnel (clinique) peut payer à 60 jours ou plus ; relances nécessaires.
- **Signature d'un client** : jamais du premier coup. Après un devis, chance de signature faible par semaine (repère : 10 % ;
  tirer avec `python outils/jet.py "Signature <client>" 10`), contre-proposition quasi systématique.
- **Fournisseurs** : délais de livraison incertains (aléa A06 actif), prix pouvant varier (aléa A15 proposé), paiement à la
  commande exigé par le fournisseur libanais (déjà payé 1,8 M FCFA, livraison sans date).
- **Charges d'OSIA** : masse salariale ≈ 5,6 M FCFA/mois chargée ; loyer 2,2 M FCFA/mois (prépayé 6 mois par William) ;
  indemnité de fin de CDD 3 % non provisionnée ; échéances CNPS/ITS le 10 et le 15 du mois suivant.
- **Aucun chiffre d'affaires** à ce jour.

## Règle de friction administrative (validée le 23/07)
Toute démarche à enjeu (banque, attestation, RCCM, CNPS, impôts, ministère, fournisseur, installateur) fait l'objet d'un
**jet « deuxième passage demandé » à 30 %** (`python outils/jet.py "<démarche>" 30`) : justificatif manquant, refus, délai,
mauvais service. Le résultat est joué sans commentaire et consigné. Ne pas rejouer un jet. Un taux différent est possible si le
réalisme l'exige (ex. dossier incomplet connu d'avance : 100 %).
