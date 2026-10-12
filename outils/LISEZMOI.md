# Outils du moteur — index, architecture et démarrage à froid

> Mis à jour le 11/10/2026 (date réelle). Pour TOUT agent (Claude Code, Gemini CLI / Antigravity, Codex, autre) : ce fichier
> suffit pour savoir quoi lancer et où sont les données. Chaque outil a une aide : `python outils/<outil>.py --help`.
> Conventions : Python 3 ; fichiers en UTF-8 avec fins de ligne CRLF ; CSV séparés par « ; » (jamais de « ; » dans un champ :
> utiliser « · ») ; dates AAAA-MM-JJ ; heures HH:MM dans le fuseau de l'horloge. Sous Windows, si les accents s'affichent mal
> dans la console, lancer avec `PYTHONIOENCODING=utf-8` (le fichier, lui, est juste).

## 1. Démarrage à froid (un agent qui ne connaît rien)
1. `python outils/relais.py entree --agent "<nom de l'agent>"` : briefing complet (alertes de sessions parallèles, horloge,
   dernier tour montré au joueur, échéances, rituels dus, notes de passation, préférences, routine) ; pose le verrou.
2. Lire le fichier maître (CLAUDE.md = GEMINI.md = AGENTS.md, sauf la ligne 3), puis `memoire/preferences-utilisateur.md`,
   puis les fichiers listés au §7 du fichier maître.
3. `python outils/tour.py debut` : la fiche moteur du tour (météo, soleil, fériés, échéances, argent, corps, lieu, rituels).
4. Jouer le tour (règles du fichier maître ; réactions tirées avec `jet.py --table`).
5. Écrire le texte du tour dans un fichier brouillon, puis
   `python outils/tour.py fin --jusqua "AAAA-MM-JJ HH:MM" --lieu "…" --attente "…" --texte <brouillon> --message "<message du joueur>"`.
6. Avant de passer la main : `python outils/relais.py sortie --note "…" --commit "…" --fusionner`.

## 2. Où est quoi
| Dossier | Contenu | Nature |
|---|---|---|
| `etat/` | État du monde : horloge, agenda, grand livre, échéancier, savoir, personnages, relations, météo tirée, corps, fronts, fichiers d'état en Markdown, note de relais, dernier tour | change à chaque tour |
| `donnees/` | Référentiels sourcés : faits vérifiés, prix, lieux et ambiances, climat de Findel, calendrier scolaire, événements publics, délais, population (générateur de personnages) | change rarement, après recherche web |
| `journal/` | Un journal par jour simulé ; `journal/tours/` : texte EXACT de chaque tour et message du joueur | ajout seulement |
| `memoire/` | Préférences de l'utilisateur, pièges connus, synthèses, revues, tirages (texte et JSONL), journal des sessions, propositions | ajout seulement |
| `personnes/`, `whatsapp/`, `courriels/`, `documents_william/` | Fiches, conversations, pièces reçues, pièces de William (PDF) | |
| `sorties/` | Généré, ignoré par git : base SQLite `monde.sqlite`, page `telephone/index.html` | reconstruit à volonté |
| `archives/` | Univers 1 et faux départ de l'univers 2 : lecture seule, aucun fait pour l'univers en cours | figé |

## 3. Les outils
| Outil | Rôle | Commandes principales |
|---|---|---|
| `relais.py` | Relais entre agents : briefing, sessions parallèles, verrou, note de relais, journal des sessions, commit et fusion | `entree`, `sortie`, `verifier`, `git`, `verrou`, `liberer` |
| `maitres.py` | CLAUDE.md, GEMINI.md, AGENTS.md identiques sauf la ligne 3 | `verifier`, `synchroniser --depuis CLAUDE.md` |
| `tour.py` | Orchestrateur : début et fin de tour, aperçu d'une avance rapide | `debut`, `fin`, `apercu` |
| `base.py` | Base de données SQLite reconstruite depuis les fichiers ; SQL en lecture ; recherche plein texte | `construire`, `requete`, `cherche`, `schema`, `vues`, `verifier` |
| `horloge.py` | Heure du monde, lieu de William, attentes, numéro du tour | `--regler`, `--tour +1` |
| `agenda.py` | Rendez-vous, échéances, promesses (règle 14) | `dus`, `retards`, `ajouter`, `clore`, `reporter` |
| `grand_livre.py` | Argent : soldes calculés, prévus, mouvements | `solde`, `ajouter`, `realiser`, `journal` |
| `echeancier.py` | Mouvements récurrents (traitement, factures, virements permanents avec contrepartie, échéances de prêt) écrits au grand livre | `liste`, `prevoir`, `realiser`, `budget`, `verifier` |
| `prets.py` | Prêts de William : tableau d'amortissement calculé (prêt PR1 de la maison), capital restant dû, contrôle des calages | `liste`, `tableau`, `crd`, `verifier` |
| `savoir.py` | Qui sait quoi ; décomptes de fuite (T5) | `qui`, `peut`, `ajouter`, `t5` |
| `jet.py` | Tirages (libres ou dans les tables T1-T14) ; garde de la règle 17 ; garde « mineurs » (`--pour`) | `--table Tn`, `--liste` |
| `tour_du_monde.py` | Vie propre des personnages (T11, T13, T14) chaque jour | `JJ/MM` |
| `tirage_aleas.py` | Aléas de la semaine (le lundi) | `AAAA-MM-JJ` |
| `personnage.py` | Générateur de personnages tirés selon la démographie réelle ; registre ; entourage pré-généré (jamais montré avant son apparition) ; noms sans homonymes ; audit des biais | `nouveau`, `reseau`, `apparait`, `promouvoir`, `liste --statut`, `audit` |
| `meteo.py` | Météo tirée sur les normales de la station du lieu où se trouve William (Findel, Manille : `donnees/stations-meteo.csv`) ; prévisions vues par William | `jour`, `heure`, `prevision`, `mois` |
| `calendrier_2040.py` | Fériés (LU, FR avec droit local, CI, CV), Pâques, Ramadan, lune, soleil, calendrier scolaire, événements, jours ouvrés | `--soleil`, `--scolaire`, `--evenements`, `--ouvres` |
| `lieux.py` | Lieux : ouvert ou fermé (fériés selon le pays, congés annuels), accès, prix ; ambiances tournantes contre les tics | `voir`, `ouverts`, `liste` |
| `faits.py` | Faits vérifiés (source, date, fiabilité, projection 2040) : à consulter AVANT une recherche web | `cherche`, `ajouter`, `perimes` |
| `prix.py` | Prix 2026 sourcés et projetés en 2040 (× 1,35 fixe) ; tirage dans une fourchette | `cherche`, `tirer`, `ajouter` |
| `corps.py` | Sommeil, entraînements, repas, poids, maladies de William ; état à montrer | `nuit`, `seance`, `noter`, `etat` |
| `fronts.py` | Menaces, occasions, projets en segments avec paliers écrits d'avance | `creer`, `avancer`, `liste`, `clore` |
| `rituels.py` | Ce que le moteur doit faire (fiches, tour du monde, synthèses, revue, aléas) | `dus`, `liste` |
| `telephone.py` | Page « téléphone de William » : écran d'accueil et applications (`telephone_web/` : coque, noyau, une feuille JS par application ; CLAUDE.md §14) | (sans argument) ; `--json` |
| `voyages.py` | Application Voyages : vols (calendrier des prix), hôtels, forfaits vol + hôtel, formalités ; calcul déterministe partagé avec la page | `vols`, `mois`, `hotels`, `forfait`, `formalites`, `verifier` |
| `appli_calendrier.py` | Données de l'application Calendrier (fériés FR, LU, PH ; vacances, événements, rendez-vous connus, argent) | (sans argument : résumé) |
| `banque.py` | Banque : virements ponctuels (entre comptes ou vers un tiers), ordres permanents (créer, modifier, suspendre, reprendre), liste ; prévus recalculés | `virement`, `ordre-modifier`, `ordre-creer`, `ordre-suspendre`, `ordre-reprendre`, `liste` |
| `rencontres.py` | Application de rencontre : profils tirés (Manille, 18 ans au moins : majorité, garde absolue), inscription de William, j'aime, matchs, messages ; intention réelle cachée ; vivier complété si une tranche d'âge s'ouvre après coup | `generer`, `completer`, `inscription`, `aimer`, `passer`, `match`, `message`, `liste`, `voir` |
| `etiquettes.py` | Applique les actions copiées depuis le téléphone (étiquettes [voyages|banque|rencontres: …]) : la commande exacte, à l'heure du jeu | `--texte "…"`, `--simule` |
| `resume_etat.py` | `etat/resume.md` : l'essentiel en trois minutes | `--silencieux` |
| `controle_coherence.py` | Contrôle de fin de tour (dates, maîtres, CSV, base, rituels, tables, PDF, tics) | (sans argument) |
| `audit_jets.py`, `chasse_tics.py`, `fuseaux.py`, `archiver_point_de_reprise.py`, `pdf_base.py`, `verifier_pdf.py` | Audit des probabilités, tics d'écriture, fuseaux horaires, archivage du §9, PDF | voir `--help` |
| `tests_moteur.py` | Essais automatiques de tous les outils sur une COPIE du dépôt | (sans argument) |

## 4. Base de données
- **Source de vérité** : les fichiers texte (CSV, Markdown, JSONL) versionnés par git. **Base** : `sorties/monde.sqlite`,
  reconstruite à la demande (`python outils/base.py construire`, environ une seconde), ignorée par git. Pourquoi : git fusionne
  des lignes de texte, jamais un fichier binaire ; tout agent lit les fichiers même sans Python ; la base n'est qu'un index.
- Tables : horloge, attentes, agenda, grand_livre, comptes, soldes, echeancier, prets, savoir, personnages, relations, lieux,
  ambiances, faits, prix, climat, meteo, corps, fronts, evenements_publics, calendrier_scolaire, delais, journal (lignes
  horodatées), tours (textes des tours), messages (WhatsApp), fiches (personnes/), documents (PDF, texte extrait), tirages
  (JSONL), tirages_md (ancien journal), recherche (plein texte, accents ignorés), meta.
- Vues : `python outils/base.py vues` (agenda à venir, agenda connu de William, retards, prévus, personnages avec âge et
  minorité, qui sait quoi, messages, journal, météo, tirages, documents).
- Exemples : `python outils/base.py requete "SELECT date, type, tmax FROM v_meteo"` ;
  `python outils/base.py cherche "boulangerie"`.

## 5. Ce que les outils ne font pas (et qui reste au moteur)
Écrire le récit, le journal, les WhatsApp, les fiches et les fils ouverts ; tirer les réactions des personnages dans les tables ;
vérifier sur le web un fait nouveau (puis l'ajouter avec `faits.py ajouter`) ; décider quoi que ce soit à la place de William.
