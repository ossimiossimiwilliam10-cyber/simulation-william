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
| Compte épargne (Spuerkeess) | 357 000 € | Épargne libre de toute affectation · *avant : « Compte épargne « Projet » » → maintenant : « Compte épargne », renommé par William le 14/07/2040 à 10h12* |
| ETF | 288 000 € | Valeur de marché (calages seulement) |
| Part nette de la maison | 89 996,87 € | Audun-le-Tiche ; valeur estimée 200 000 € − capital restant dû 110 003,13 € (prêt PR1) |
| **Patrimoine net** | **744 796,87 €** | Comptes + ETF + part de maison |

*(Avant : part de maison 90 000 € (crédit « 110 000 €, ≈ 940 €/mois, fin 2059 ») et patrimoine 744 800 € → maintenant : 89 996,87 €
et 744 796,87 €, capital restant dû calculé par le tableau d'amortissement du prêt PR1, 12/10/2026.)*

*(Avant : soldes datés du mardi 17/07/2040, 07h00 → maintenant : 14/07/2040, 07h00, départ redaté le 11/10/2026 ; montants inchangés.)*

## Revenus et charges (échéancier, au 14/07/2040)
- **Traitement** : ≈ 9 300 € net par mois (395 points + 3 leçons supplémentaires), le dernier jour ouvré du mois (jour exact non
  vérifié) : E001 ; 410 points à partir de septembre 2040 (montant à recalculer). Allocation de fin d'année (13e mois) : E013,
  à chiffrer.
- **Charges actives** (montants 2026 sourcés × 1,35, ou estimations signalées) :
  - crédit 949,28 € (E002, le 5 : prêt PR1, mensualité 926,15 € + assurance 23,13 ; montant exact de chaque échéance tiré du
    tableau d'amortissement) ;
  - électricité 132 € (E003, le 10 : option heures creuses, 9 kVA, recharge de la voiture la nuit) ; gaz 253 € (E004, le 10) ;
  - internet et mobile 63 € (E005, le 15) ; eau 187,50 € deux fois par an (E006, mars et septembre) ;
  - assurance habitation 45 € (E007, le 5) ; assurance de la voiture électrique 107 € (E010, le 5) ;
  - Minett Combat Club 85 € (E008, le 1er) ; taxe foncière ≈ 1 190 € le 15/10 (E009, valeur locative estimée).
- **Virements automatiques** (ordres permanents, le 2 du mois) : 2 850 € vers le compte épargne (E012) et 2 850 € vers les
  ETF (E014).
- **Terminé** : soutien aux parents (E011 ; ponts coupés, précisé par l'utilisateur le 11/10/2026). **Encore à chiffrer** :
  allocation de fin d'année (E013).
- *(Avant : crédit ≈ 940 €, électricité ≈ 112 €, club « à confirmer », six lignes « à valider » → maintenant : réponses de
  l'utilisateur appliquées, prix vérifiés le 11/10/2026, 12/10/2026.)*
- Un prélèvement qui tombe un week-end ou un jour férié luxembourgeois passe au jour ouvré suivant (banque : Spuerkeess).
- **Compte courant, solde des lignes actives d'août 2040** : + 1 965,72 € (`python outils/echeancier.py budget 2040-08` :
  traitement − charges − virements), avant les dépenses de la vie courante (courses, sorties, vêtements : ≈ 1 200 € estimés) et
  le « plaisir ». *(Avant : « surplus ≈ 8 100 € », sans virements ni charges complètes → maintenant, 12/10/2026.)*

## Prêt immobilier (PR1 : `etat/prets.csv`, `python outils/prets.py tableau PR1`)
- 185 000 € à 3,5 % fixe sur 300 mois, première échéance le 05/09/2034 ; assurance emprunteur 23,13 €/mois (0,15 % par an du
  capital initial ; pas de questionnaire de santé : moins de 200 000 € et fin avant 60 ans, F042).
- Remboursement anticipé de 40 000 € le 05/06/2037, avec réduction de durée ; indemnité de 700 € (6 mois d'intérêts, plafond
  légal : F041).
- Au 14/07/2040 : 71 échéances payées, **capital restant dû 110 003,13 €** ; prochaine échéance le lundi 06/08/2040 (le 5 est
  un dimanche) : n° 72, capital 605,31 €, intérêts 320,84 €.
- Dernière échéance le 05/10/2052 ; intérêts restant à payer ≈ 25 242 €.

## Règle de répartition du surplus mensuel (habitude de William)
45 % ETF / 45 % compte épargne / 10 % plaisir, par **ordres permanents** (précisé par l'utilisateur le 11/10/2026) : 2 850 € +
2 850 € le 2 du mois (E012, E014 ; montants estimés par le moteur sur un surplus d'environ 6 335 €, modifiables par William).
*(Avant : « ordre permanent ou geste manuel : non fixé » → maintenant : automatique, 12/10/2026.)*

## Faits utiles (base des faits, `donnees/faits.csv`)
- Garantie des dépôts (FGDL) : 100 000 € par déposant et par banque (F022) ; au départ, ≈ 366 800 € à la Spuerkeess.
- Comptes luxembourgeois à déclarer chaque année en France (formulaire 3916, amende de 1 500 € par compte oublié : F015).
- Revenus de l'ETF : prélèvement forfaitaire unique de 31,4 % en 2026 (F016) ; régime 2040 inconnu.

## Engagements en cours
- Aucun.

## Historique
- **12/10/2026 (date réelle)** : réponses de biographie appliquées : prêt PR1 calculé (calages pret 110 003,13 € et part de
  maison 89 996,87 €) ; échéancier complété (gaz, électricité avec recharge, eau, assurances, virements permanents) ; prévus du
  grand livre recalculés (anciens prévus du crédit et de l'électricité annulés, suffixe « -v1 »).
- **14/07/2040, 07h00** : soldes de départ de l'univers 2 (grand livre : calages redatés du 17/07 au 14/07 le 11/10/2026).
- **11/10/2026 (date réelle)** : échéancier installé ; le prévu P001 (« traitement de juillet », 31/07) est annulé et remplacé
  par E001-20400731.
