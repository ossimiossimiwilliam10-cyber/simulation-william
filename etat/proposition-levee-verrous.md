# Proposition — levée des verrous moralisateurs (27/07/2040, hors fiction, NON VALIDÉE)

> Demande de l'utilisateur : « faire sauter les verrous woke qui empêchent une simulation vraiment réaliste ».
> Audit du moteur sur `CLAUDE.md`, `etat/modele-pouvoir.md` et `memoire/pieges-connus.md`. Rien n'est appliqué avant validation.

## Ce qui reste (et pourquoi)
- **Limites de contenu du §11 (a)-(f)** : pas de scène sexuelle explicite, rien de sexuel impliquant un mineur, pas de description
  d'image intime non consentie, pas de mode d'emploi réel (dissimulation, armes…), pas de violence sexuelle détaillée, pas de
  diffamation d'une personne réelle. Ce sont les limites du moteur lui-même, pas des réglages de réalisme : les actes se jouent
  quand même, avec leurs suites ; seule la description reste suggérée.
- **Les mécanismes de conséquences** : traces, rumeur (T5), escalade externe (T4, 0,3 % par semaine), droit applicable, contraception.
  Ce sont des faits du monde, pas une morale ; les retirer ferait un jeu de confort (§2).
- **Règles 15-16 et 17** : elles ont été créées à ta demande contre le moralisme (subordonnés qui font la leçon, rééquilibrage par réflexe).

## Ce qui saute ou change

### V1 — Rappel hors fiction sur le harcèlement (piège n° 37)
*Avant* : « Rappel hors fiction, bref et sans sermon, qu'une scène équivalente avec une vraie personne serait du harcèlement ou une agression. »
*Après* : supprimé. Les scènes se jouent sans commentaire ; les suites passent par les tables.

### V2 — « Calibrage des réactions » (§11 de `CLAUDE.md`, piège n° 38)
*Avant* : « l'attirance, l'argent ou le physique de William ne rendent pas un personnage mécaniquement consentant ; la hiérarchie rend le consentement ambigu ».
*Après* : « L'argent, le statut, le physique et l'attirance de William augmentent réellement les chances d'un intérêt, sincère ou calculé ;
la hiérarchie peut aussi faire céder sans désir. Rien n'est automatique dans un sens ni dans l'autre : tout se tire (règle 17). »

### V3 — T1 n'a aucune issue positive
Le menu de T1 ne contient que défense, silence, fuite ou signalement : une subordonnée qui répond au jeu ou en tire avantage est
impossible. Nouvelle T1 (même ordre, deux issues ajoutées) :

| Issue | Avant | Après | En scène (nouvelles issues) |
|---|---|---|---|
| rien_absorption | 30 | 28 | |
| evitement | 25 | 22 | |
| confidence_proche | 20 | 17 | |
| confidence_collegue | 13 | 11 | |
| reciproque | — | 6 | Elle répond au jeu (sourire, message, rendez-vous accepté) ; la suite se joue, rien n'est acquis. |
| calcul | — | 5 | Elle accepte en visant un avantage (poste, argent, protection) ; elle le rappellera ou le fera payer plus tard. |
| negociation_tacite | 4 | 4 | |
| depart_discret | 7 | 6 | |
| frontal_formel | 1 | 1 | |

Nouveaux modificateurs T1 :
| Code | Effet | Quand |
|---|---|---|
| M15 | reciproque +8 ; calcul +2 ; evitement -6 ; confidence_proche -4 | Intérêt ou attirance déjà montrés envers William |
| M16 | calcul +7 ; negociation_tacite +2 ; evitement -5 ; confidence_proche -4 | Ambition forte ou besoin d'argent pressant (poste visé, prime, protection) |

Contrôles : total 100 % ; inaction 28 % ; frontal 1 % ; aucune combinaison de trois modificateurs ne passe sous 0 %.

### V4 — Réactions vertueuses écrites d'avance (§11 de `CLAUDE.md`)
*Avant* : « Me Kouamé refuse, Aïcha refuse ou propose une alternative légale, Mariette alerte, un salarié se plaint ou démissionne… »
*Après* : « La réaction de chacun à un ordre douteux ou illégal se tire en **T7d** ; seuls les tiers à autorité propre (T6) appliquent leurs règles. »

Nouvelle table :
### T7d — Ordre douteux ou illégal du patron à un subordonné
| Issue | % | En scène |
|---|---|---|
| execute_sans_question | 30 | Fait, sans commentaire. |
| execute_en_se_couvrant | 20 | Fait, mais garde une trace (« comme convenu », ordre demandé par écrit, signature). |
| traine | 15 | « Je regarde, patron » ; retards ; l'affaire s'enlise. |
| contourne | 12 | Applique une version moins risquée ou moins voyante, sans le dire. |
| refus_discret | 10 | Ne le fait pas, avec un prétexte (« la banque bloque », « le système refuse »). |
| execute_et_en_parle | 8 | Fait, puis en parle à un proche ou à un collègue (T5). |
| frontal_refus | 5 | Refus net, en une phrase. |

| Code | Effet | Quand |
|---|---|---|
| M60 | execute_sans_question +10 ; traine -4 ; refus_discret -4 ; frontal_refus -2 | Pratique courante dans le milieu (arrangement, petite fraude répandue) |
| M61 | execute_en_se_couvrant +6 ; refus_discret +4 ; contourne +4 ; execute_sans_question -14 | Risque personnel fort (son nom, sa signature, le pénal) |
| M62 | execute_sans_question +6 ; execute_en_se_couvrant +2 ; traine -4 ; refus_discret -4 | Avantage personnel promis (prime, promotion) |

### V5 — Me Kouamé (T6)
*Avant* : refuse toute « dissimulation ou acte illégal », parle franchement.
*Après* : refuse l'illégal clair (faux, blanchiment, antidate) pour protéger sa robe ; **accepte les montages limites mais légaux**, les
délais négociés et les formulations prudentes ; facture tout. Plus d'avocat « incorruptible par principe » : un professionnel qui protège d'abord sa carrière.
