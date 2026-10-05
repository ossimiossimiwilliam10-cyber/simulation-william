# Comment utiliser ce dossier

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
6. Dossiers : `etat/` (état du monde + fils ouverts + corrections), `osia/`, `personnes/`, `journal/`,
   `memoire/` (synthèses + pièges connus), `whatsapp/` (conversations), `serveur/` (PDF du monde),
   `outils/` (scripts du moteur, hors monde).
