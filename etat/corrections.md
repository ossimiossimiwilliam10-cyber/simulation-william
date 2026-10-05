# Journal des corrections (audit de relais)

> À chaque changement de moteur (Claude ⇄ Gemini), le moteur entrant audite le travail du précédent,
> corrige, et **consigne ici** : date, fichier, avant → maintenant, raison. Ne jamais effacer une ligne.
> Objectif : que le moteur suivant ne réintroduise pas la même erreur (voir aussi `memoire/pieges-connus.md`).

## Audit du 21/07/2040 — Claude reprend après Gemini (Antigravity)

| # | Fichier | Avant | Maintenant | Raison |
|---|---|---|---|---|
| 1 | `serveur/rh/matrice_evaluation.pdf` | Aucun accent (« Evaluation », « Aicha », « Execution »…) | Accents rétablis | William avait recadré Mariette et Grace sur ce point le 18/07 ; les employés ne referaient pas la faute |
| 2 | `serveur/rh/matrice_evaluation.pdf` | Barème « 86 à 94 » puis « > 95 » : le score **95** n'était couvert par aucune règle | « 86 à 95 » puis « 96 et plus » | Trou logique ; William avait dit « au-dessus de 95 » |
| 3 | `serveur/rh/synthese_equipe_1807.pdf` | Aucun accent ; salaire de Grace tronqué (« 850 000 + 2% + b ») ; « Fin aout » mis dans la colonne Évaluation (celle d'Esther, censée être vide) ; « (+ 10k net) » | Accents ; salaires complets en brut ; colonnes Début/Fin CDD séparées ; colonne Évaluation vide ; note « prévisionnel » pour Esther ; format paysage | Même incident que 1 ; William avait demandé les dates exactes de début et de fin et une évaluation vide |
| 4 | `serveur/rh/contrats/*.pdf` | Salaires « Net » ; « Aicha », « Toure », « Gerante » sans accents ; pas de date de fin ; clauses de Grace absentes | Salaires **brut** ; noms/accents corrects ; date de fin (24 mois) ; articles 5-6 pour Grace (éthique commerciale, révision à 6 mois) | `osia/equipe.md` = bruts ; les virements du 21/07 sont calculés sur le brut ; William a hurlé le 20/07 sur des contrats faux |
| 5 | `serveur/**/generate_*.py` (5 scripts) | Scripts Python rangés **dans** `serveur/` | Déplacés dans `outils/` ; base commune `outils/osia_pdf.py` (police Unicode) ; `outils/verifier_pdf.py` | William a décrété le 20/07 « uniquement des PDF » sur le serveur ; le serveur est dans le monde, les scripts sont du moteur |
| 6 | `serveur/LISEZMOI.md` | « format `.md` ou `.csv` » ; arborescence `rapports/` | « PDF uniquement » ; arborescence réelle | Contredisait la règle de William (20/07) et le CLAUDE.md §3.4 |
| 7 | `etat/calendrier.md` | Daté du 18/07 ; événements des 19-21/07 encore « à venir » | À jour au 21/07, statuts « avant → maintenant », jours fériés 07/08 et 15/08 ajoutés | Fichier périmé |
| 8 | `etat/finances.md` | Commande d'onduleurs (2 750 €) jamais déduite des comptes de William | Compte projet 356 200 → ~353 450 € | Oubli de report ; l'ancien « PAYÉS le 21/07 » des salaires corrigé en « ordonnés, crédités lundi » |
| 9 | `etat/finances.md` | Avances informelles = 5 400 € seulement | Idem + avertissement : loyer/caution (≈ 26 800 €), Phase 1 et acompte Me Kouamé payés par William sans statut tracé | Risque comptable signalé par Aïcha le 18/07, sous-estimé |
| 10 | `osia/entreprise.md` | Daté du 18/07 ; compte « demande déposée » ; vidéosurveillance « prévue le 20/07 » | Compte ouvert le 21/07 ; install. reportée au 23/07 ; clinique et Dr Yapi ; risques juridiques consignés | Fichier périmé ; événement du 20/07 manquant au journal |
| 11 | `journal/2040-07-20.md` | Lignes de 17h20 et 17h25 après celle de 17h30 ; message WhatsApp de 16h40 (bonus/malus) absent | Ordre rétabli ; message ajouté ; note moteur sur SécuTech | Cohérence chronologique |
| 12 | `journal/2040-07-19.md` | Présentation d'Abdoul « au calendrier » mais jamais jouée ni reportée ; revue juridique de Mariette promise sans suite | Consignés comme non tenue / en suspens | Fils perdus |
| 13 | `personnes/` | Pas de fiche pour Mariette, Grace, Abdoul, Yves | 4 fiches créées (Grace : physique défini par le moteur) | CLAUDE.md §7 : « nouveau personnage récurrent = nouvelle fiche » |
| 14 | `CLAUDE.md` + `GEMINI.md` | Numérotation de §3 cassée (4, 5 en double) ; point de reprise au 18/07 | Renumérotés ; point de reprise au 21/07 ; §10 protocole de relais ; lecture de `whatsapp/` ajoutée | Les règles étaient devenues ambiguës |
| 15 | `etat/` | Aucun registre des fils en suspens | `etat/fils-ouverts.md` (relais) et `etat/corrections.md` | Pour que le moteur suivant sache où reprendre |

## Incohérences relevées mais NON modifiées (décision de l'utilisateur requise)
- ~~Naturalisation luxembourgeoise de William en 2022~~ : **RÉSOLU le 21/07** par William (naturalisation via son père, effet collectif sur mineur) ; voir `etat/william.md`.
- **Gérance** : William signe les contrats « Gérant » alors que la fiche d'entreprise dit « gérante : Aïcha (par procuration) ».
- **Contrats d'Aïcha (22/05) et de Mariette (01/06)** antérieurs au RCCM du 11/07 : à régulariser (consigné comme risque).
