# Comment utiliser ce dossier

> **Univers 2 depuis le 11/10/2026** : la simulation a été redémarrée (univers neuf à 35 ans, argent initial, paramètres repris ;
> départ le mardi 17/07/2040 à Audun-le-Tiche). L'univers 1 (Abidjan, OSIA) est archivé dans `archives/univers-1/` (voir son
> `LISEZMOI.md`) et dans les tags git `univers-1-master` et `univers-1-continuation`.

1. Copie le dossier `simulation-william/` sur ton PC (déjà fait).
2. **Claude Code** : ouvre un terminal dans ce dossier et lance `claude`.
   Le fichier `CLAUDE.md` est lu automatiquement.
   **Gemini CLI / Antigravity** : il lit `GEMINI.md`.
   (Les deux fichiers ont le même contenu à une ligne près : garde-les synchronisés si tu
   modifies les règles. Vérification : `diff CLAUDE.md GEMINI.md` ne doit montrer que la ligne 3.)
3. Premier message conseillé (quel que soit le moteur) :
   « Lis CLAUDE.md (ou GEMINI.md), tous les fichiers d'état et le dernier journal, puis
   reprends la simulation au point de reprise. »
4. **Changement de moteur (Claude ⇄ Gemini)** : le moteur qui arrive applique le protocole de relais
   (§10 du fichier maître) : il audite le travail du précédent, corrige, consigne dans
   `etat/corrections.md`, puis reprend. Avant de changer, le moteur qui part met à jour le point de
   reprise (§9) et `etat/fils-ouverts.md`.
5. **Git** : un dépôt existe ; un commit à chaque fin de journée simulée. Si Claude travaille dans un
   *worktree* (copie isolée), ses commits sont sur une branche à fusionner dans `main` avant de
   rebasculer sur Antigravity, sinon celui-ci ne verra pas les corrections.
   La branche principale s'appelle `master`.
6. Dossiers : `etat/` (état du monde + fils ouverts + corrections), `personnes/`, `journal/`,
   `memoire/` (synthèses + pièges connus), `whatsapp/` (conversations), `courriels/` et `documents_william/` (pièces reçues ou gardées par William),
   `outils/` (scripts du moteur, hors monde).
7. **Outils du moteur (depuis le 09/08/2040)** : voir `CLAUDE.md` §13. En début de tour : `python outils/resume_etat.py` puis
   `python outils/agenda.py dus --jusqua "AAAA-MM-JJ HH:MM"` ; en fin de tour : `horloge.py --regler`, `grand_livre.py ajouter`,
   `savoir.py ajouter`, `agenda.py clore/ajouter`, `controle_coherence.py`. Données : `etat/horloge.txt`, `etat/agenda.csv`,
   `etat/grand-livre.csv`, `etat/savoir.csv` ; résumé généré : `etat/resume.md` ; archive du §9 : `memoire/archive-point-de-reprise-*.md`.
8. **Archives** : `archives/univers-1/` (lecture seule : le moteur n'en tire aucun fait pour l'univers 2 ; ses générateurs de PDF
   restent utilisables depuis ce dossier).
