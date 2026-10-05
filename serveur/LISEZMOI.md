# Serveur de l'entreprise (OSIA Énergies)

Ce dossier est le **serveur interne d'OSIA dans le monde de la simulation**. Règles de William (WhatsApp du
20/07/2040) : tout document produit par l'équipe y est classé (« absolument tout », oubli sanctionné) et
**uniquement au format PDF** (règle absolue : ni .md, ni .csv, ni script).

## Arborescence
- `rh/` : synthèses d'équipe, matrice d'évaluation. `rh/contrats/` : copies numérisées des contrats.
- `commercial/` : rapports de prospection, devis, contrats clients (Grace).
- `direction/` : chartes, règlement intérieur, synthèses générales (Aïcha).
- `technique/` (à créer au premier livrable) : chantiers, devis fournisseurs (Abdoul, Yves).
- `conformite/` (à créer à l'arrivée d'Esther) : risques, juridique.

## Règle d'usage pour le moteur
1. Quand William demande un livrable à un personnage, **générer le vrai PDF ici** (CLAUDE.md §3.4). Nom :
   `sujet_JJMM.pdf` (ex. `rapport_prospects_1807.pdf`).
2. Les scripts de génération ne vivent **pas** ici mais dans `outils/` (base commune `outils/osia_pdf.py`,
   police Unicode : accents obligatoires). Après chaque génération : `python outils/verifier_pdf.py`.
3. Lire ce dossier si le contexte exige l'avancement d'un pôle. Les livrables sont aussi résumés dans le
   journal du jour (une ligne : qui, quoi, chemin).
4. Un livrable corrigé écrase l'ancien (même nom) ; la correction est consignée dans `etat/corrections.md`.
