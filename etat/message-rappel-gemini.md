# Message de rappel pour Gemini en cours de partie (à coller dans Antigravity)

> Rédigé par Claude le 28/10/2026, après l'audit des tours n° 32 à 68. À coller tel quel quand Gemini a déjà repris la simulation ; le message de reprise complet (début de session) reste `etat/message-reprise-gemini.md`.

```
MISE À JOUR DE CONSIGNES (audit de Claude sur tes tours 32 à 68). Continue la simulation exactement au même point, avec le même format, mais applique ceci dès maintenant.

1. Nouveautés à relire : GEMINI.md §5 (nouveau point 8, « texte du joueur propre ») et outils/LISEZMOI.md §7 (points 6 et 7). Un contrôle automatique existe : python outils/verifier_texte_joueur.py --texte <ton brouillon> AVANT tour.py fin. tour.py fin t'affiche aussi « RELIRE (texte joueur) » : tant que le tour n'est pas montré, corrige ce qui est signalé, réécris le brouillon et relance.

2. Ce qui n'allait pas, à ne plus faire :
a) Identifiants du moteur dans le texte du joueur : D038, « A106 clos », « (I1) », « (A003) », « (E007) »… Cite les pièces par leur titre (« le rapport quotidien du 3 août »), jamais par un code.
b) Mécanismes cachés : « tirage hebdomadaire », « fuite interne », « escalade externe », dérogations, tables… Jamais dans le texte du joueur.
c) Aléas tirés annoncés d'avance (ex. « aléa A09 programmé jeudi 8 août ») : jamais ; un aléa se joue le jour dit, par surprise. La Revue du lundi ne les annonce pas non plus.
d) Plusieurs jours avancés d'un coup, racontés en liste (« Le samedi 3 août… Le dimanche 4 août… ») : raconte d'un trait, en prose fluide ; n'avance pas de plus de 36 h dans un tour, et arrête-toi dès qu'un événement important arrive.
e) Personnages trop lisses : pas de « Premièrement… Deuxièmement… », pas de flatterie (« Monsieur le Président »). Phrases courtes, hésitations, intérêts propres ; les défauts, soucis et secrets tirés de chaque fiche (personnes/<nom>.md) se voient dans les actes : retards, oublis, ton, argent.
f) Revue du lundi : elle doit contenir 3 à 5 idées nouvelles de réalisme et d'immersion (à piocher d'abord dans etat/aleas.md, statut « proposé »), à faire valider par moi, pas seulement un bilan et un programme.

3. Point que tu NE tranches PAS toi-même : tu m'appelles « Président » et tu parles de « décision présidentielle ». Si cela veut dire que j'exerce la présidence de la SASU (mandat exécutif), cela contredit l'article 14 (associé non-gérant). Signale-le-moi en une ligne « 📌 Vraie vie » au prochain tour et demande au pôle juridique virtuel de vérifier ce point dans son prochain rapport.

4. Le reste ne change pas : même format de réponse (le texte du tour seul ; en-tête en gras ; récit à la deuxième personne ; « Il est HHhMM. » ; --- ; Réponses attendues ; À faire / à fournir ; Quêtes secondaires ; Que veux-tu faire ?), réactions tirées par les outils, tour.py fin --enregistrer, controle_coherence, je décide seul de mes actions. Ne réécris PAS les tours déjà envoyés : applique ces règles à partir du prochain. Confirme en une phrase, puis attends mon message de jeu.
```
