# Carrière de William — Maquette Solo Intégrale & Entrepreneuriat (univers 3 ; validé le 21/10/2026, date réelle)

> **Source** : Maquette financière intégrale « Célibataire, sans enfant, Classe U » fournie par l'utilisateur le 21/10/2026.
> Supprime les trois aides familiales (-860 €/mois entre 28 et 49 ans), stabilise le revenu net à 10 370 €/mois de 48 à 65 ans.
> Intègre le cadre légal de l'entrepreneuriat à distance des fonctionnaires luxembourgeois (Statut général, art. 14 ; F083-F086).
> Voir `donnees/faits.csv`, `outils/carriere.py`, `.agents/rules/luxembourg_teacher_overtime_finances.md`.
> **Euros constants 2026** : tous les montants sont en euros constants 2026 (valeur du point indiciaire à 25,067 €).

---

## 1. Calcul exact d'une leçon supplémentaire (euros constants 2026)

Pour un bloc de **3 leçons supplémentaires par semaine** en mathématiques (portant l'emploi du temps de 18h20 à 20h50) :

| Étape | Calcul | Montant |
|---|---|---|
| Indemnité brute mensuelle lissée (3 leçons) | ~233,33 € × 3 | **700,00 € bruts / mois** |
| Cotisations sociales déductibles (11,55 %) | 8,50 % (pension) + 3,05 % (maladie CNS) | **−80,85 € / mois** |
| Assurance dépendance (1,40 % non déductible) | 700 × 1,40 % | **−9,80 € / mois** |
| Revenu imposable additionnel | 700,00 − 80,85 | **619,15 € / mois** |
| Impôt marginal Classe U (41,73 %) | 39 % × 1,07 = 41,73 % ; 619,15 × 41,73 % | **−258,37 € / mois** |
| **Gain NET réel** | 700,00 − 80,85 − 9,80 − 258,37 | **≈ 350 € nets / mois** |

Soit **~117 € nets / mois par leçon supplémentaire**.

---

## 2. Décharge d'âge convertie en heures supplémentaires (F078, source officielle)

| Âge | Tâche normale | Si William garde 25 leçons | Heures sup. payées | Gain net mensuel (h. sup.) |
|---|---|---|---|---|
| 28-44 ans | 22 | 25 | 3 | +350 € |
| 45-49 ans | 21 | 25 | 4 | +467 € |
| 50-54 ans | 20 | 25 | 5 | +584 € |
| 55-65 ans | **18** | 25 | **7** | **+817 €** |

---

## 3. Règle d'allocation du surplus mensuel (Formule Solo Validée)

Formule sur 100 % du Revenu Net Lissé :
- **Socle Vital fixe** : 2 000 € / mois (dépenses courantes, logement, transport).
- **Vacances** : 833 € / mois (plafonné à 10 000 € / an).
- **Sécurité Liquide (10 %)** : 10 % de l'excédent net total après socle vital (`(Net − 2 000 €) × 10 %`).
- **ETF Monde (Solde)** : Tout le reste (`Net − Socle − Vacances − Sécurité`), soit ~90 % de l'excédent hors vacances.

---

## 4. Tableau de bord intégral de carrière (26 à 65 ans — Solo, Sans Enfant, 3h sup.)

| Âge | Statut & Points Indiciaires | Salaire Brut Mensuel | **Revenu NET Lissé** (13e mois + 3h sup.) | Socle Vital Fixe | Vacances (Plafond 10k€/an) | **10 % Sécurité** (Cash & LIR 1,5 %) | **ETF Monde** (Épargne mensuelle) | **Patrimoine Net Cumulé** (Fin de période) |
|---|---|---|---|---|---|---|---|---|
| **26–27 ans** | Stage A1 (340 pts — 0 h sup.) | 8 523 € | **6 140 €** | 2 000 € | 833 € | 414 € / mois | **2 893 € / mois** | **82 940 €** *(à 28 ans)* |
| **28–29 ans** | Titulaire Gr. 12 (410 pts + 3h) | 10 977 € | **7 580 €** | 2 000 € | 833 € | 558 € / mois | **4 189 € / mois** | **209 990 €** *(à 30 ans)* |
| **30–31 ans** | Gr. 12/13 (445 pts + 3h) | 11 855 € | **8 060 €** | 2 000 € | 833 € | 606 € / mois | **4 621 € / mois** | **361 380 €** *(à 32 ans)* |
| **32–33 ans** | Gr. 13 (480 pts + 3h) | 12 732 € | **8 520 €** | 2 000 € | 833 € | 652 € / mois | **5 035 € / mois** | **539 050 €** *(à 34 ans)* |
| **34–35 ans** | Gr. 13 (515 pts + 3h) | 13 610 € | **8 980 €** | 2 000 € | 833 € | 698 € / mois | **5 449 € / mois** | **745 630 €** *(à 36 ans)* |
| **36–39 ans** | Gr. 14 (540 à 560 pts + 3h) | 14 236 € – 14 738 € | **9 320 € – 9 560 €** | 2 000 € | 833 € | ~744 € / mois | **~5 863 € / mois** | **1 245 980 €** *(à 40 ans)* |
| **40–44 ans** | Gr. 14 allongé (580 à 600 pts + 3h) | 15 239 € – 15 740 € | **9 830 € – 10 100 €** | 2 000 € | 833 € | ~799 € / mois | **~6 358 € / mois** | **2 057 190 €** *(à 45 ans)* |
| **45–49 ans** | Plafond A1 (625 pts + 3h) | 16 367 € | **10 370 € – 10 440 €** | 2 000 € | 833 € | ~840 € / mois | **~6 725 € / mois** | **3 113 690 €** *(à 50 ans)* |
| **50–54 ans** | Plafond A1 (625 pts + 3h) | 16 367 € | **10 370 €** | 2 000 € | 833 € | 837 € / mois | **6 700 € / mois** | **4 454 110 €** *(à 55 ans)* |
| **55–59 ans** | Plafond A1 (625 pts + 3h) | 16 367 € | **10 370 €** | 2 000 € | 833 € | 837 € / mois | **6 700 € / mois** | **6 159 770 €** *(à 60 ans)* |
| **60–64 ans** | Fin de carrière A1 (625 pts + 3h) | 16 367 € | **10 370 €** | 2 000 € | 833 € | 837 € / mois | **6 700 € / mois** | **8 333 040 €** *(à 65 ans)* |

**Décomposition finale à 65 ans (8 333 040 €) :**
- **Portefeuille ETF Monde (5 % net réel/an) : 7 861 818 €** (dont 2 804 892 € versés, 5 056 926 € d'intérêts composés purs).
- **Poche Sécurité & Prévoyance L.I.R. (1,5 % net réel/an) : 471 220 €** (dont 353 844 € versés, 117 376 € d'intérêts).

---

## 5. Stratégie d'Entrepreneuriat à Distance (Les 3 Fenêtres)

### Fenêtre 1 : 26 à 28 ans — La « Zone Rouge » (À proscrire)
- Priorité : validation des examens de stage (26-27 ans) et création complète des banques de cours, fiches LaTeX, exercices et examens.
- Risque : épuisement cognitif prématuré.

### Fenêtre 2 : 30 à 32 ans — Le « Sweet Spot » Opérationnel (Meilleur Moment pour Lancer)
- **Automatisation terminée** : Cours rodés, préparation à domicile proche de zéro, après-midis libres (dès 15h/16h), week-ends et 15 semaines de congés scolaires disponibles.
- **Autofinancement massif** : À 30 ans, 8 060 € nets/mois (dont 5 227 € d'épargne hors vacances) et 209 990 € de patrimoine liquide. Financement d'infrastructures sans crédit.
- **Cadre juridique (Art. 14 Statut général des fonctionnaires)** :
  - *Voie A (Activité accessoire autorisée)* : Demande officielle auprès du MENJE pour projets EdTech, édition scientifique/pédagogique, licences logicielles, propriété intellectuelle.
  - *Voie B (Détention patrimoniale)* : Associé / actionnaire majoritaire non-gérant d'une SAS (France) ou SARL (Luxembourg) avec mandat exécutif confié à un tiers.
  - *Option de jeu* : Type de projet et montage décidés en situation dans la simulation (« on verra »).

### Fenêtre 3 : 36 à 38 ans — Le Point d'Indépendance (« Lean FIRE »)
- Patrimoine à 36 ans : **745 630 €** (dont 670 380 € en ETF). Rendement passif à 5 % : 2 793 € nets/mois, franchissant 3 500 € nets/mois à 37 ans et demi (couvre 100 % du socle vital + vacances de 2 833 €/mois).
- **Leviers de bascule de la fonction publique** : Possibilité légale de demander un **temps partiel (50 % ou 75 %)** ou un **congé sans traitement** (jusqu'à 2 ans renouvelables, avec réintégration garantie).

---

## Historique
- **21/10/2026 (date réelle)** : intégration de la maquette intégrale Solo sans enfant (Classe U) et de la stratégie entrepreneuriale (art. 14).
