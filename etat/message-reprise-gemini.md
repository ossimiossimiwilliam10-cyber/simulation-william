# Message à coller dans Antigravity (Gemini) quand la limite d'utilisation de Claude est atteinte

> Rédigé par Claude le 27/10/2026 à la demande du joueur. Coller le bloc ci-dessous tel quel dans Antigravity, puis envoyer ensuite le message de jeu habituel.

```
Reprise de la simulation « William Ossimi » (univers 3). Claude a atteint sa limite d'utilisation : tu continues à sa place, au point exact où il s'est arrêté.

1. Dossier de travail : C:\Users\User\Desktop\simulation-william (branche master). Ne travaille dans aucun autre dossier ni aucune autre branche.
2. Première commande, avant toute autre chose : python outils/relais.py entree --agent "Gemini"
3. Lis ensuite, dans cet ordre : GEMINI.md (règles du monde : surtout §3, §5, §10 E), outils/LISEZMOI.md (§1 et §7 : reprise par un moteur moins puissant), etat/relais-notes.md (la dernière « PASSATION »), etat/dernier-tour.md (le texte exact du dernier tour et mon dernier message), etat/fils-ouverts.md.
4. Si l'entrée signale un worktree « claude/… » avec des fichiers non enregistrés, ou le verrou de Claude : c'est normal (sa session s'est coupée). Applique le §7.1 de outils/LISEZMOI.md (enregistrer là-bas, fusionner dans master, python outils/relais.py liberer). Ne supprime rien.
5. À chaque tour : python outils/tour.py debut ; joue le tour ; écris le texte dans un brouillon ; python outils/tour.py fin ... --enregistrer ; python outils/controle_coherence.py. Les réactions des personnages se TIRENT avec les outils (jet.py, reactions.py), elles ne s'inventent pas ; rien de caché n'est montré ; je décide seul de mes actions (règle 13).
6. Le téléphone de William : double-clique sur ouvrir-telephone.bat (ou lance python outils/telephone_serveur.py) ; je l'ouvre sur mon PC ou sur mon vrai téléphone (même Wi-Fi). Il se met à jour à chaque tour.
7. Avant de jouer, dis-moi en deux phrases où nous en sommes (date et heure dans le jeu, ce qui est en attente), puis attends mon message.
```
