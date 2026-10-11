# Comment utiliser ce dossier

> **Univers 2 depuis le 11/10/2026** : la simulation a été redémarrée (univers neuf à 35 ans, argent initial, paramètres repris ;
> départ le **samedi 14/07/2040, 08h37**, premier jour des vacances d'été, à Audun-le-Tiche ; avant : mardi 17/07, faux départ
> archivé dans `archives/univers-2-faux-depart/`). L'univers 1 (Abidjan, OSIA) est archivé dans `archives/univers-1/` (voir son
> `LISEZMOI.md`) et dans les tags git `univers-1-master` et `univers-1-continuation`.

1. Copie le dossier `simulation-william/` sur ton PC (déjà fait).
2. **Claude Code** : ouvre un terminal dans ce dossier et lance `claude` ; le fichier `CLAUDE.md` est lu automatiquement et un
   crochet de démarrage affiche le briefing de relais. **Gemini CLI / Antigravity** : il lit `GEMINI.md`. **Codex et la plupart
   des autres agents** : ils lisent `AGENTS.md`. Les trois fichiers ont le même contenu à la ligne 3 près : on en modifie un, puis
   `python outils/maitres.py synchroniser --depuis <ce fichier>`.
3. Premier message conseillé (quel que soit l'agent) :
   « Lance `python outils/relais.py entree --agent "<ton nom>"`, lis le fichier maître et `memoire/preferences-utilisateur.md`,
   puis reprends la simulation au point de reprise. »
4. **Changement d'agent** (limite d'utilisation, autre outil) : rien à faire de spécial si le précédent a terminé par
   `python outils/relais.py sortie …` ; sinon le nouvel agent voit, dès `relais.py entree`, les sessions non fusionnées et le
   texte exact du dernier tour (`etat/dernier-tour.md`). Le protocole complet est au §10 du fichier maître.
5. **Git** : un commit à chaque fin de journée simulée (au minimum). Quand un agent travaille dans un *worktree* (copie isolée),
   ses commits sont sur une branche fusionnée en avance rapide dans `master` (`relais.py sortie --fusionner`), sinon l'agent
   suivant ne verrait pas la partie. La branche principale s'appelle `master`.
6. Dossiers : `etat/` (état du monde), `donnees/` (faits, prix, lieux, climat, calendrier, population : tout est sourcé),
   `personnes/`, `journal/` (et `journal/tours/` : textes exacts des tours), `memoire/` (préférences, synthèses, pièges, tirages,
   propositions), `whatsapp/`, `courriels/` et `documents_william/` (pièces en PDF), `outils/` (scripts du moteur),
   `sorties/` (généré : base de données, page « téléphone de William » ; ignoré par git), `archives/`.
7. **Outils du moteur** : index complet dans `outils/LISEZMOI.md`. Un tour = `python outils/tour.py debut` puis
   `python outils/tour.py fin …`. Base de données : `python outils/base.py requete "SELECT …"` ou `python outils/base.py cherche
   "mots"`. Essais automatiques de tous les outils : `python outils/tests_moteur.py`.
8. **Archives** : `archives/univers-1/` et `archives/univers-2-faux-depart/` (lecture seule : le moteur n'en tire aucun fait pour la
   partie en cours ; les générateurs de PDF de l'univers 1 restent utilisables depuis ce dossier).
