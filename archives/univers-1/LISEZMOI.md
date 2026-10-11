# Archives de l'univers 1 (17/07/2040 → 11/08/2040)

> Archivé le 11/10/2026 (date réelle), quand l'utilisateur a demandé de redémarrer la simulation : « On reboot l'univers. On
> retourne à la toute première date mentionnée. » **Lecture seule** : le moteur n'en tire aucun fait pour l'univers 2. Ces
> fichiers servent à l'historique des règles et au profil de l'utilisateur.

## Ce que contient ce dossier
- L'état du monde de l'univers 1 tel qu'il était sur la branche principale le **jeudi 09/08/2040, 14h15 (heure de Lisbonne)** :
  `etat/`, `osia/`, `personnes/`, `journal/` (du 17/07 au 09/08/2040), `whatsapp/`, `serveur/`, `courriels/`,
  `documents_william/`, `memoire/` (synthèses W29 à W31, revues du lundi n° 1 à 3, tirages).
- `CLAUDE-univers-1.md` : le fichier maître complet à cette date (règles et point de reprise détaillé).
- `memoire/pieges-connus-univers-1.md` : les pièges connus à cette date (la version à jour, n° 1 à 82, est dans `memoire/` à la racine).
- `outils/` : les générateurs de PDF de l'univers 1 (OSIA) et `osia_pdf.py` ; ils écrivent dans ce dossier d'archive.

## Les trois chronologies de l'univers 1
L'univers 1 s'est divisé en trois suites jouées dans des sessions différentes, à partir du jeudi 09/08/2040, 14h15 :
1. **Branche principale** (ce dossier ; tag git `univers-1-master`) : arrêt au jeudi 09/08/2040, 14h15 (Lisbonne).
2. **Suite jouée dans une autre session** (tag git `univers-1-continuation`, jamais fusionnée) : jusqu'au samedi 11/08/2040,
   13h27 (Abidjan) : réunion de direction en visio, Aïcha annoncée CEO, retour à Abidjan, restructuration abandonnée.
   Pour la voir : `git log univers-1-continuation` ou `git show univers-1-continuation:journal/2040-08-11.md`.
3. **Session des outils du 09/10/2026** (jamais enregistrée) : installation des outils du moteur et des tables T12 à T14 (repris
   dans l'univers 2), audit n° 46 à 60, et un tour joué jusqu'au jeudi 09/08/2040, 15h20 (Lisbonne). Conservée ici :
   `session-outils/modifications-non-enregistrees.patch` (toutes les modifications) et les fichiers de données
   (`session-outils/etat/`, `memoire/`, `personnes/`, `whatsapp/`).
