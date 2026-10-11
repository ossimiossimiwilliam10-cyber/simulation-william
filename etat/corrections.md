# Corrections du moteur (univers 2 ; créé le 17/07/2040)

> Chaque correction est consignée ici (« avant → maintenant ») ; rien n'est effacé. Les corrections n° 1 à 60 de l'univers 1 sont
> archivées : `archives/univers-1/etat/corrections.md` (n° 1 à 45) et `archives/univers-1/session-outils/` (n° 46 à 60, audit du
> 09/08/2040 resté dans une session non enregistrée). Les leçons générales sont dans `memoire/pieges-connus.md`.
> Numérotation de l'univers 2 : U2-1, U2-2…

| N° | Objet | Avant | Maintenant | Cause |
|---|---|---|---|---|
| U2-0 | Redémarrage de la simulation (11/10/2026, date réelle) | Univers 1 : Abidjan, OSIA, du 17/07 au 11/08/2040 (trois chronologies : master au 09/08 14h15, suite au 11/08 13h27, session des outils au 09/08 15h20) | Univers 2 : univers neuf à 35 ans, argent initial, tous les paramètres repris, départ le mardi 17/07/2040 | Demande de l'utilisateur |
| U2-1 | Date de départ de l'univers 2 (11/10/2026, date réelle) | Mardi 17/07/2040, 07h05 (« la toute première date mentionnée ») | Samedi 14/07/2040, 08h37 : premier jour des vacances d'été luxembourgeoises (coucher à 23h20 et réveil à 08h37 tirés au dé) | Demande de l'utilisateur : « le premier vrai jour de libre, le premier jour du début des vacances » (avant cela, il avait demandé le 1er juin, puis s'est ravisé) |
| U2-2 | Journal du faux départ | `journal/2040-07-17.md` (un tour, sans action de William) | Archivé, mot pour mot : `archives/univers-2-faux-depart/` ; le 17/07 se rejouera normalement | Redatation (U2-1) ; rien n'est supprimé |
| U2-3 | Agenda | A001 (revue n° 1) le 23/07 ; A002 (traitement de juillet) latent | A001 reporté au lundi 16/07, 08h00 ; A002 annulé et remplacé par l'échéancier (E001) | Redatation ; échéancier installé |
| U2-4 | Grand livre | Calages datés du 17/07 ; prévu P001 (traitement du 31/07) | Calages au 14/07, 07h00 (montants inchangés) ; P001 annulé (« prevu_annule ») et remplacé par E001-20400731 ; prévus de l'échéancier écrits jusqu'au 12/09 | Redatation ; échéancier (`outils/echeancier.py`) |
| U2-5 | Fin d'année et rentrée scolaires | « Projection d'après les règlements récents : fin d'année au 15 juillet, rentrée au 15 septembre » | Règlement grand-ducal du 3 juin 2026 : en 2028-2029 (même configuration de jours), année jusqu'au vendredi 13/07, vacances du samedi 14/07 au dimanche 16/09 ; projection 2040 identique (F001) | Recherche de l'agent du 11/10/2026 (document FEDIL), reprise par le moteur |
| U2-6 | Météo | Écrite à l'intuition (« 17 °C, 26 °C annoncés ») | Tirée jour par jour par `outils/meteo.py` sur les normales officielles de Findel 1991-2020 + 1,5 °C (projection) | Réalisme (demande de l'utilisateur du 11/10/2026) |
| U2-7 | Garde de la règle 17 dans `jet.py` | Inopérante sans fiche de personnage (motif vide « (?!) ») ; `--simule` relançait un dé sans trace | Reconnaît aussi les rôles (voisin, directrice, collègue…) ; les essais sont tracés (`memoire/simulations.jsonl`) ; `--pour` refuse T1, T1b et T9 pour un mineur | Audit de l'agent du 11/10/2026 (famille « intégrité des tirages ») |
| U2-8 | Contrôle de cohérence | Dates en toutes lettres non contrôlées ; deux fichiers maîtres ; CSV non vérifiés | Dates en toutes lettres contrôlées ; trois fichiers maîtres (AGENTS.md ajouté) ; colonnes de tous les CSV ; base, rituels et relais contrôlés | Relais entre agents et base de données (11/10/2026) |
| U2-9 | Sessions parallèles | Worktree `simulation-realistic-tools-d95e81` (48 fichiers non enregistrés, univers 1) et branche `claude/continuation-9f6d32` (univers 1) non fusionnés | Marqués « archivés » dans `etat/relais-config.json` (patch dans `archives/univers-1/session-outils/`, tag `univers-1-continuation`) ; à nettoyer seulement avec l'accord de l'utilisateur | Contrôle `relais.py entree` |
| U2-10 | Travail de l'agent précédent (11/10/2026) | Workflow de conception interrompu par la limite d'utilisation (3 explorations sur 6 ; synthèse et critique non faites) ; rien dans le dépôt | Résultats sauvegardés dans `memoire/conception-2026-10-11/` (audit de l'univers 1, société et personnages, mécanismes) et repris dans le plan | Relais demandé par l'utilisateur |

## Incohérences relevées mais non modifiées (biographie de William : à trancher par l'utilisateur)
- **Crédit** : 110 000 € restants, 940 €/mois, fin en 2059 = taux d'environ 8 % ; à 3-3,5 %, fin vers 2052 ou mensualité de 630 à 660 €.
- **Jour de versement du traitement** : non trouvé par recherche (fin de mois retenue, E001).
- Voiture, chauffage, soutien aux parents, club, répartition du surplus : non fixés (etat/fils-ouverts.md, C).
