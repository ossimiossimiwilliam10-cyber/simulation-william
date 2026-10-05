# Mémoire longue durée

Ce dossier contient des synthèses condensées couvrant des périodes passées.
Elles sont lues par le moteur à chaque tour pour maintenir la cohérence
sans avoir à relire tous les journaux quotidiens.

## Format
- `semaine-AAAA-WNN.md` : synthèse de la semaine ISO NN de l'année AAAA.
- Chaque synthèse contient : décisions clés, changements d'état majeurs,
  évolution des relations, événements marquants.
- Les synthèses sont créées à la fin de chaque semaine simulée (dimanche soir).

## Quand lire ce dossier
Le moteur lit **tous** les fichiers de `memoire/` avant chaque tour.
Cela remplace la relecture des anciens journaux quotidiens.
