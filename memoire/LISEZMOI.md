# Mémoire longue durée (univers 2)

Ce dossier contient la mémoire partagée par TOUS les agents (Claude, Gemini, Codex…) : préférences de l'utilisateur, synthèses
condensées des périodes passées, leçons d'erreurs, tirages, sessions. Il est lu par le moteur à chaque tour pour maintenir la
cohérence sans relire tous les journaux quotidiens.

## Univers 2 (depuis le 11/10/2026, date réelle)
La simulation a été redémarrée à la demande de l'utilisateur : univers neuf à 35 ans, argent initial, tous les paramètres repris ;
départ le samedi 14/07/2040, 08h37. Les synthèses, revues et tirages de l'univers 1 sont archivés dans `archives/univers-1/memoire/` :
ils servent au profil de l'utilisateur et à l'historique des règles, **jamais** de faits pour l'univers 2.

## Format des synthèses
- `semaine-AAAA-WNN.md` : synthèse de la semaine ISO NN de l'année AAAA (décisions clés, changements d'état majeurs, évolution
  des relations, événements marquants), créée le dimanche soir.

## Fichiers de ce dossier
- `preferences-utilisateur.md` : **à lire au début de chaque session, par tout agent** (format des tours, ton, pratiques, profil
  hors fiction de l'utilisateur). Créé le 11/10/2026 pour le relais entre agents.
- `pieges-connus.md` : leçons d'erreurs passées (univers 1 compris : les leçons restent valables), relu à chaque tour. Les FAITS
  vérifiés (droit, prix, calendriers…) vont désormais dans `donnees/faits.csv` (`outils/faits.py`).
- `revue-lundi-AAAA-MM-JJ.md` : compte rendu de la revue du lundi (`CLAUDE.md` §12).
- `tirages-aleas.md` : journal des tirages de hasard (texte, lu par `outils/audit_jets.py`), à ne jamais effacer ni rejouer ;
  `tirages.jsonl` : les mêmes tirages en JSON (une ligne par tirage, lue par la base de données) ; `simulations.jsonl` : les essais
  `--simule` (aucun dé ne se relance en cachette).
- `sessions.csv` : journal des sessions d'agents (début, fin, agent, branche, horloge, tours) tenu par `outils/relais.py`.
- `propositions-2026-10-11.md` : idées et propositions qui touchent les tables, les règles ou la biographie (à valider par
  l'utilisateur).
- `conception-2026-10-11/` : explorations de l'agent du 11/10/2026 (audit de l'univers 1, société et personnages, mécanismes).
- `archive-point-de-reprise-*.md` : anciennes entrées du §9 du fichier maître (s'il y en a).
