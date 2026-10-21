# Sécurité Temporelle et Géographique des Outils de Simulation

1. **Année Dynamique dans les Contrôles de Cohérence** :
   - Tout outil ou script validant la concordance des jours de la semaine (lundi, mardi...) avec le calendrier grégorien DOIT impérativement lire l'année courante depuis `etat/horloge.txt` ou l'en-tête du document concerné. Ne jamais coder d'année en dur (ex: `2040`) comme valeur par défaut sans détection dynamique préalable.
2. **Robustesse du Slicing Géographique (Europe vs International)** :
   - Tout générateur d'événements, d'actualités ou de météo basé sur la localisation de William (`ici = pays_de_william()`) DOIT s'adapter dynamiquement au nombre de pays gérés dans le contexte actif (2 pays en Europe transfrontalière : France et Luxembourg ; 3 pays ou plus lors de séjours à l'étranger). Ne jamais indexer directement `ordre[2]` sans vérifier la longueur de la collection.
