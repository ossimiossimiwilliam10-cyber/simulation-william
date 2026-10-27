# Revue du lundi n° 1 de l'univers 3 (lundi 22/07/2041 ; préparée le 22/10/2026 en date réelle)

## 1. Bilan de la semaine écoulée (15-21/07/2041)
- Réaliste : le déroulé du voyage (TGV direct, enregistrement à CDG 2E, vol de 11 h 30, atterrissage à 07h50 heure de Séoul avec
  7 h de décalage) ; les formalités (e-Arrival Card valable 72 heures) ; le prix du vol.
- Non réaliste, corrigé : achats sans plafond de carte, billet de TGV jamais payé, trajet de 30 minutes entre Audun et Louvigny (réel :
  1 h 15), personnages coréens écrits sans défaut ni secret, aléas de l'univers 2 mêlés à ceux de l'univers 3, téléphone resté sur Manille
  (`etat/corrections.md`, U3-1 à U3-14).
- Fils perdus : aucun ; promesse de Thiago Rocha (data room par courriel lundi matin) programmée (A012).
- Livrables : 2 PDF de William (étude IA, grille d'audit) et 3 courriels reçus, tous contrôlés par `verifier_pdf.py`.
- Tics d'écriture : répétitions de « voir le texte exact du tour » dans les journaux (non bloquant).
- Audit des jets (`audit_jets.py`) : aucune dérogation, aucun jet libre sur une réaction, aucune dérive notable.

## 2. Nouvelles idées de réalisme et d'immersion
Voir `memoire/propositions-2026-10-22.md` (R1 à R5).

## 3. Casting et faits périmés (P14)
- Personnages complétés par `personnage.py completer` (Min-ji, Soo-jin, Hye-won, Thiago Rocha, Lucas Mendes) ; douze profils de l'application
  de rencontre tirés, tous de 20 ans au moins (garde de Séoul, F087).
- Faits à surveiller : statut du K-ETA et de l'e-Arrival Card en 2041 (hypothèse : dispense reconduite, F089) ; cours du won (référence 1 700,
  F091) ; frais des distributeurs de Corée (estimation, F092).

## 4. Le monde cette semaine
Voir `etat/monde.md`, « Semaine du 22 au 28/07/2041 » (écrite par `actualites.py` quand l'horloge a passé le lundi).

## 5. Décisions de l'utilisateur
« Je valide R1 à R5, et j'écris à Hye-won. » (22/10/2026) : propositions R1 à R5 validées et installées (corrections U3-15).

## 6. Tirage des aléas de la semaine
Tiré le 22/10/2026 (`python outils/tirage_aleas.py 2041-07-22`) : A24 (souci de voisinage) dimanche 28/07 après-midi, par un message d'un voisin ; A28 (courriel du lycée) vendredi 26/07 soir ; les autres aléas : non. A34 (coup de chaleur) se tire chaque jour de maximum ≥ 35 °C par `tour.py fin`.
