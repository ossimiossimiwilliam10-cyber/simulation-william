# Finances de William (univers 2 ; estimations au samedi 14/07/2040, 08h37)

> Parité fixe : 1 € = 655,957 FCFA (utile si l'histoire repart vers la zone franc).
> **Source des soldes : le grand livre** (`python outils/grand_livre.py solde`), jamais un solde écrit à la main ; ce fichier les
> cite et donne les règles. Les salaires sont exprimés en NET pour William (traitement de fonctionnaire), en BRUT pour les contrats
> qu'il signerait comme employeur.
> **Niveaux initiaux** : choisis par l'utilisateur le 11/10/2026 (« le niveau d'argent initial ») : ceux du 17/07/2040 de
> l'univers 1 (`archives/univers-1/etat/finances.md`, première version). Dans l'univers 2, cet argent n'a jamais servi à OSIA.
> **Mouvements récurrents** (depuis le 11/10/2026) : `etat/echeancier.csv` (`python outils/echeancier.py liste`) ; les lignes
> « actif » écrivent leurs prévus au grand livre et deviennent des mouvements réels quand l'horloge passe leur date
> (`tour.py fin`). Les lignes « a_valider » attendent une réponse de l'utilisateur (biographie) ou une vérification.

## Soldes de départ (samedi 14/07/2040, 07h00, calages du grand livre)
| Poste | Montant | Remarques |
|---|---|---|
| Compte courant (Spuerkeess) | 9 800 € | Dépenses courantes |
| Compte épargne « Projet » (Spuerkeess) | 357 000 € | Épargne libre de toute affectation dans l'univers 2 |
| ETF | 288 000 € | Valeur de marché (calages seulement) |
| Part nette de la maison | 90 000 € | Audun-le-Tiche ; crédit restant 110 000 €, mensualité ≈ 940 €, fin 2059 (incohérence signalée : voir etat/william.md) |
| **Patrimoine net** | **744 800 €** | Comptes + ETF + part de maison |

*(Avant : soldes datés du mardi 17/07/2040, 07h00 → maintenant : 14/07/2040, 07h00, départ redaté le 11/10/2026 ; montants inchangés.)*

## Revenus et charges (échéancier, au 14/07/2040)
- **Traitement** : ≈ 9 300 € net par mois (395 points + 3 leçons supplémentaires), le dernier jour ouvré du mois (jour exact non
  vérifié) : E001 ; 410 points à partir de septembre 2040 (montant à recalculer). Allocation de fin d'année (13e mois) : E013,
  à chiffrer.
- **Charges actives** (montants 2026 sourcés × 1,35, ou estimations signalées) : crédit ≈ 940 € (E002, le 5, jour estimé) ;
  électricité ≈ 112 € (E003, consommation estimée) ; internet et mobile ≈ 63 € (E005) ; club de combat ≈ 85 € (E008, club à
  confirmer) ; taxe foncière ≈ 1 190 € le 15/10 (E009, valeur locative estimée).
- **À valider par l'utilisateur** : chauffage (E004), eau (E006, prix à vérifier), assurance habitation (E007), voiture (E010),
  soutien aux parents (E011), répartition automatique ou manuelle du surplus (E012).
- Un prélèvement qui tombe un week-end ou un jour férié luxembourgeois passe au jour ouvré suivant (banque : Spuerkeess).
- **Surplus mensuel des lignes actives** : ≈ 8 100 € (`python outils/echeancier.py budget 2040-08`), avant dépenses courantes
  (courses, carburant, sorties) et avant les lignes à valider.

## Règle de répartition du surplus mensuel (habitude de William)
45 % ETF / 45 % épargne « Projet » / 10 % plaisir (ordre permanent ou geste manuel : non fixé, E012).

## Faits utiles (base des faits, `donnees/faits.csv`)
- Garantie des dépôts (FGDL) : 100 000 € par déposant et par banque (F022) ; au départ, ≈ 366 800 € à la Spuerkeess.
- Comptes luxembourgeois à déclarer chaque année en France (formulaire 3916, amende de 1 500 € par compte oublié : F015).
- Revenus de l'ETF : prélèvement forfaitaire unique de 31,4 % en 2026 (F016) ; régime 2040 inconnu.

## Engagements en cours
- Aucun.

## Historique
- **14/07/2040, 07h00** : soldes de départ de l'univers 2 (grand livre : calages redatés du 17/07 au 14/07 le 11/10/2026).
- **11/10/2026 (date réelle)** : échéancier installé ; le prévu P001 (« traitement de juillet », 31/07) est annulé et remplacé
  par E001-20400731.
