> Note de relais GÉNÉRÉE par `python outils/relais.py sortie` (ou `tour.py fin`) : ne pas éditer à la main. Les notes libres vont dans `etat/relais-notes.md`.

# Relais de la simulation — briefing généré le 11/10/2026 22:17 (heure machine) pour Claude Opus 5.5 (session du 11/10/2026)

## Alertes
- aucune

## Où en est la partie
- Horloge : samedi 14 juillet 2040, 08h37 (luxembourg) ; tour n° 0
- Lieu de William : Audun-le-Tiche (Moselle), chez William
- En attente de William : Sa journée du samedi 14/07/2040 (premier jour des vacances d'été ; Fête nationale française)

## Dernier tour montré au joueur (etat/dernier-tour.md)
- aucun tour enregistré dans etat/dernier-tour.md (premier tour, ou tour joué avant le 11/10/2026)

## Échéances : retards et prochaines 24 h (les lignes NON CONNU sont pour le moteur seul)
- rien

## Rituels du moteur dus (rituels.py)
- rien

## Décisions en attente de William (etat/fils-ouverts.md, A)
| 1 | **Sa journée du samedi 14/07/2040** | Début de l'univers 2 ; premier jour des vacances d'été ; Fête nationale française (commerces fermés à Audun) ; aucune obligation | — |

## Notes de passation (etat/relais-notes.md)
- (11/10/2026 22:30, Claude Opus 5.5) Redémarrage de l'univers 2 redaté au samedi 14/07/2040, 08h37 (premier vrai jour de vacances,
  demande de l'utilisateur). Le premier tour n'est PAS encore joué : il attend les réponses de l'utilisateur aux questions de
  biographie (etat/fils-ouverts.md, C) et sa décision sur les propositions (memoire/propositions-2026-10-11.md).
- (11/10/2026 22:30, Claude Opus 5.5) Infrastructure installée le 11/10/2026 : relais (relais.py, maitres.py, AGENTS.md,
  préférences dans memoire/preferences-utilisateur.md, dernier tour dans etat/dernier-tour.md), base de données (base.py),
  orchestrateur (tour.py), météo, lieux, faits, prix, échéancier, corps, fronts, générateur de personnages, rituels,
  téléphone de William (telephone.py). Index : outils/LISEZMOI.md.
- (11/10/2026 22:35, Claude Opus 5.5) Page « Téléphone de William » publiée (privée) : https://claude.ai/artifact/VJkYBmpJTrVarDVTs24MsS
  (adresse aussi dans etat/relais-config.json) ; la republier au même endroit après `python outils/telephone.py` (fin de journée ou à la demande).

## Préférences de l'utilisateur (memoire/preferences-utilisateur.md : à lire en entier)
- Format du tour : récit fluide, puis « Réponses attendues », « À faire », « Quêtes secondaires », « Que veux-tu faire ? ».
- Aucune explication, aucun conseil, aucun jet ni source montrés ; pas de morale ; William décide seul (règles 6, 13, 16).
- « 📌 Vraie vie : … » = hors fiction ; il dicte : interpréter les erreurs de dictée et le signaler en une ligne.
- Il joue parfois depuis son téléphone : lui envoyer les fichiers demandés dans la conversation.

## Routine
- Lire le fichier maître (CLAUDE.md, GEMINI.md ou AGENTS.md), puis memoire/preferences-utilisateur.md et outils/LISEZMOI.md.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, rituels, météo, corps, relais).
- Fin de tour : `python outils/tour.py fin --jusqua "AAAA-MM-JJ HH:MM" --lieu "…" --attente "…" --texte <brouillon>`.
- Avant de passer la main : `python outils/relais.py sortie --note "…" --commit "…" --fusionner`.

## État git détaillé
- branche courante : claude/simulation-realistic-agent-handoff-3deabc ; master : 3bafa2a ; avance 0, retard 0
- worktree simulation-william : branche master ; 0 commit(s) absents de master ; 0 fichier(s) modifié(s)
- worktree continuation-9f6d32 (ICI) : branche claude/simulation-realistic-agent-handoff-3deabc ; 0 commit(s) absents de master ; 4 fichier(s) modifié(s)
- worktree life-simulation-resume-892e7a : branche claude/life-simulation-resume-892e7a ; 0 commit(s) absents de master ; 0 fichier(s) modifié(s)
- worktree simulation-realistic-tools-d95e81 : branche claude/simulation-realistic-tools-d95e81 ; 0 commit(s) absents de master ; 48 fichier(s) modifié(s) ; ARCHIVÉ : univers 1 : session des outils du 09/10/2026, jamais enregistrée ; ses 48 modifications sont sauvées dans archives/univers-1/session-outils/modifications-non-enregistrees.patch ; worktree à nettoyer avec l'accord de l'utilisateur

