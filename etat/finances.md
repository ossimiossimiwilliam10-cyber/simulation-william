# Finances de William (univers 3 ; état au mardi 16/07/2041, 08h37)

> **Source des soldes : le grand livre** (`python outils/grand_livre.py solde`), jamais un solde écrit à la main.
> Ce fichier cite les montants officiels et formalise les règles de gestion budgétaire et patrimoniale.
> Les revenus sont en NET pour William (traitement de fonctionnaire d'État luxembourgeois).
> **Mouvements récurrents** : gérés dans `etat/echeancier.csv` (`python outils/echeancier.py liste`).

## Soldes de départ (mardi 16/07/2041, 07h00, calages du grand livre)
| Poste | Montant | Remarques |
|---|---|---|
| Compte courant (Spuerkeess) | 10 000,00 € | Dépenses courantes et vie quotidienne |
| Compte épargne sécurité (Spuerkeess) | 75 250,00 € | Poche de sécurité liquide (matelas de précaution) |
| ETF Monde | 670 380,00 € | Portefeuille d'actifs financiers capitalisant |
| Part nette de la maison | 97 378,22 € | Audun-le-Tiche ; valeur estimée 200 000 € − capital restant dû 102 621,78 € (prêt PR1) |
| **Patrimoine net total** | **853 008,22 €** | Comptes + ETF + Part nette immobilière |

*Patrimoine financier hors immobilier : 755 630,00 €.*

## Cartes et moyens de paiement (Zebra Premium, Spuerkeess)
- **Package Zebra Premium** : 12,83 €/mois (E015).
- **Visa Debit** : limite mensuelle de 2 500 € (retraits et paiements).
- **Visa Premier** (crédit / débit différé) : limite mensuelle de 5 000 € (relevé débité le 5 du mois suivant). Assurances voyage incluses.
- **S-Net** : virements standards jusqu'à 15 000 €/semaine (modifiable en ligne jusqu'à 50 000 €).

## Revenus et charges mensuelles (Échéancier 2041)
- **Traitement de fonctionnaire** : **9 320,00 € net par mois** (Groupe A1, Grade 14, 540 points indiciaires + 3 leçons supplémentaires hebdomadaires lissées, F076-F082 ; E001). Versé le dernier jour ouvré du mois.
- **Allocation de fin d'année (13e mois)** : versée fin décembre (E013).
- **Charges mensuelles récurrentes** :
  - Crédit immobilier : **949,28 €** (prêt PR1 : mensualité 926,15 € + assurance 23,13 €, E002, le 5).
  - Électricité (recharge VE comprise) : 132,00 € (E003, le 10).
  - Gaz naturel (chauffage et eau chaude) : 253,00 € (E004, le 10).
  - Téléphonie & Fibre internet : 63,00 € (E005, le 15).
  - Assurance habitation : 45,00 € (E007, le 5).
  - Assurance auto tous risques : 107,00 € (E010, le 5).
  - Minett Combat Club (cotisation) : 85,00 € (E008, le 1er).
  - Package bancaire Zebra Premium : 12,83 € (E015, le 1er).
- **Charges semestrielles / annuelles** :
  - Eau : 187,50 € semestriel (mars et septembre, E006).
  - Taxe foncière : ≈ 1 190,00 € (octobre, E009).

## Règle de répartition du surplus (Maquette Solo sans enfant, Classe U)
Validation du 21/10/2026 :
- **Socle vital incompressible** : 2 000 € / mois (couvre toutes les charges de base, nourriture, énergie, logement).
- **Budget vacances / voyages** : 833 € / mois (plafonné à 10 000 € / an).
- **Excédent net disponible** : `9 320 € − 2 000 € = 7 320 € / mois`.
- **Épargne de sécurité liquide (10 %)** : **732,00 € / mois** (virement permanent vers compte épargne, E012).
- **Investissement ETF Monde (Solde, 90 %)** : **5 755,00 € / mois** (virement permanent DCA ETF Monde, E014).
- **Total épargne et investissement** : **6 487,00 € / mois** (taux d'épargne effectif de ~70 % des revenus nets).

## Prêt immobilier (PR1 : `etat/prets.csv`, `python outils/prets.py tableau PR1`)
- Emprunt initial : 185 000 € à 3,5 % fixe sur 300 mois (début septembre 2034).
- Remboursement anticipé de 40 000 € en juin 2037 avec réduction de durée.
- Au 16/07/2041 : 83 échéances payées, **capital restant dû : 102 621,78 €**. Prochaine échéance le 05/08/2041 (n° 84 : amortissement 627,10 €, intérêts 299,05 €, assurance 23,13 €).
- Échéance finale : 05/10/2052.
