# Mémoire longue durée (univers 2)

Ce dossier contient des synthèses condensées couvrant des périodes passées.
Elles sont lues par le moteur à chaque tour pour maintenir la cohérence
sans avoir à relire tous les journaux quotidiens.

## Univers 2 (depuis le 11/10/2026, date réelle)
La simulation a été redémarrée à la demande de l'utilisateur : univers neuf à 35 ans, argent initial, tous les paramètres repris.
Les synthèses, revues et tirages de l'univers 1 sont archivés dans `archives/univers-1/memoire/` : ils servent au profil de
l'utilisateur et à l'historique des règles, **jamais** de faits pour l'univers 2.

## Format
- `semaine-AAAA-WNN.md` : synthèse de la semaine ISO NN de l'année AAAA.
- Chaque synthèse contient : décisions clés, changements d'état majeurs,
  évolution des relations, événements marquants.
- Les synthèses sont créées à la fin de chaque semaine simulée (dimanche soir).

## Quand lire ce dossier
Le moteur lit **tous** les fichiers de `memoire/` avant chaque tour.
Cela remplace la relecture des anciens journaux quotidiens.

## Autres fichiers de ce dossier
- `pieges-connus.md` : leçons d'erreurs passées (univers 1 compris : les leçons restent valables), relu à chaque tour.
- `revue-lundi-AAAA-MM-JJ.md` : compte rendu de la revue du lundi (règle du 22/07/2040, `CLAUDE.md` §12).
- `tirages-aleas.md` : journal des tirages de hasard (créé par `outils/tirage_aleas.py` et `outils/jet.py`), à ne jamais effacer ni rejouer.
