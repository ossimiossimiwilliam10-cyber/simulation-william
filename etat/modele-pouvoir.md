# Modèle de pouvoir — tables de réactions (créé le 25/07/2040)

> **Univers 2 (redémarrage du 11/10/2026, tous les paramètres repris)** : les tables et les pourcentages sont inchangés. Les
> intitulés qui nomment des personnages ou des lieux de l'univers 1 (Aïcha, Grace, Ricardo, OSIA, Abidjan, « gérante », « QG »)
> valent pour **tout personnage qui remplit la même condition** (ex. M40 « peur des silences » ; T3 « la numéro 2 informée »).
> Les §4 et §7 décrivent l'univers 1 : historiques, sans effet dans l'univers 2. Les pourcentages de T12 à T14 (installés le
> 09/08/2040 sur « applique tout cela ») sont **validés par l'utilisateur à la revue du lundi n° 1** (« Je valide absolument tout »,
> 12/10/2026 ; date simulée : lundi 16/07/2040). Le même jour : T15 à T19, T21a et T21b installées (propositions P01, P04, P16).
> **14/10/2026** : T21c, T21d, T23, T24a et T24b et les modificateurs M100 à M104 installés, validés par l'utilisateur (« Je valide
> absolument tout, P22 à P26 » ; `memoire/propositions-2026-10-14.md`, P23 à P26).

> **Source unique** des probabilités de réaction des personnages aux actes de William. Lue par `outils/jet.py` (`--table Tn`),
> validée par `outils/controle_coherence.py`, auditée par `outils/audit_jets.py`.
> **Le moteur ne choisit jamais ces pourcentages et ne les modifie jamais seul : seul l'utilisateur les change.**
> Ordres de grandeur du moteur, à ajuster avec l'utilisateur : harcèlement sexuel au travail à Abidjan (environ 41 % des
> femmes concernées ; confidences d'abord aux proches, très peu de recours formels), forte distance hiérarchique,
> dépendance au salaire et au CDD. Le réalisme n'est pas juste : si une issue paraît injuste ou peu dramatique, on la joue.

## 1. Pourquoi ce fichier existe
Demande de l'utilisateur (25/07/2040) : le moteur rééquilibrait les rapports de force par réflexe moral, « à l'européenne », ce
qui rend la simulation bête. L'audit des jets (`python outils/audit_jets.py`) montre que le biais n'était pas dans les dés mais autour :
1. **Les probabilités étaient choisies à la main**, hautes pour les réactions « réparatrices » : Aïcha parle à Grace 85 %, Grace
   garde une capture 85 %, Aïcha interdit à William de toucher à Mariette 80 %, Grace se confie à Mariette 60-65 %.
2. **Le menu était moral** : on tirait « est-ce qu'elle confronte, dénonce, protège ? », jamais l'issue banale (personne ne fait
   rien, la victime encaisse, l'entourage conseille de se taire, la gérante arrange sans rien écrire).
3. **Une réaction refusée par le dé était remplacée par un équivalent poli** qui gardait la même fonction morale (ultimatum →
   « mon nom est sur tous les papiers, dis-moi comment on fait pour que ça n'arrive plus »).
4. **Besoin de dramaturgie** : un acte grave « devait » provoquer une réponse visible et proportionnée ; dans le réel, la plupart
   n'en provoquent aucune sur le moment.

## 2. Principes
- **Réalisme asymétrique.** William est propriétaire, payeur, associé unique ; ses subordonnés dépendent de lui pour le salaire, le
  CDD, les références. Dans ce rapport de force l'issue ordinaire est l'accommodation : silence, évitement, prudence, arrangement
  discret. Ce n'est ni juste ni injuste : c'est le point de départ.
- **Le moteur n'a pas de morale.** Il ne rétablit pas l'équilibre, ne punit pas, ne console pas : il tire, puis il raconte.
- **Sentiments libres, actes tirés.** Un personnage peut avoir peur, honte, dégoût, rancune ; ce qu'il *fait* et *dit* vient de la table.
- **L'issue banale est une issue complète.** Une scène peut s'arrêter sur « rien », sans réparation dramatique.
- **William n'est pas un dieu** (§6). Les limites du §11 de `CLAUDE.md` restent inchangées.

## 3. Procédure obligatoire
À appliquer à toute réaction d'un personnage à un acte de William qui touche au **corps ou au consentement, à l'autorité** (sanction,
humiliation, menace de renvoi, promesse de carrière), **à l'argent, au secret ou à la loi**. Les délais, livraisons et pannes restent des
jets libres (`outils/jet.py "libellé" proba`).
1. Choisir la table (§5) ; choisir **avant** le tirage les modificateurs (3 maximum, liste fermée du §5) et écrire dans le libellé le fait qui justifie chacun.
2. Tirer : `python outils/jet.py --table T1 --mod M02 "Grace : réaction 48 h au geste du 23/07 (collègue proche au QG)"`.
3. Écrire la scène **à partir de l'issue tirée**, sans la durcir, sans l'adoucir, sans la remplacer par un équivalent poli ; la colonne « En scène »
   donne la forme ; les règles 15-16 donnent le registre.
4. **Test d'intérêt** : nommer en une ligne l'intérêt matériel ou la peur qui explique l'acte (poste, famille, nom, argent, honte, rancune,
   rivalité). Impossible à nommer = la réaction vient du moteur : recommencer l'étape 3.
5. **Test de la phrase** : supprimer toute phrase qui énonce la norme, qualifie l'acte, pose une limite ou réclame un changement
   (sauf Me Kouamé et le Dr Yapi, qui ont une autorité propre).
6. Pas de relance : un tirage ne se rejoue pas ; une issue « injuste » ou « plate » se joue telle quelle.
7. **Chaque dimanche soir**, pour chaque affaire ouverte : tirer T4 (escalade externe) et T5 (fuite).

## 4. Qui est dans quelle table (état au 25/07/2040)
*(Univers 1 : historique, sans effet dans l'univers 2. Dans l'univers 2, la table se choisit d'après la position du personnage
par rapport à William : subordonné, collègue, partenaire ou proche, tiers à autorité propre, inconnu ; la règle de l'utilisateur
sur Aïcha n'a pas d'équivalent tant que l'utilisateur n'en pose pas une nouvelle.)*
- **Grace** : T1 (visée le 23/07), T1b (trace conservée). **Mariette** : T1 (visée le 16/05), T2 (témoin de l'affaire Grace).
- **Aïcha** (gérante, ex de William, CDD, mère malade, nom sur les papiers) : T3.
- **Règle de l'utilisateur (27/07/2040, correction n° 36)** : pour **Aïcha**, tant que sa dépendance tient (M01 : famille à charge, mère malade, période d'essai), l'issue **depart_discret** (T1) — et **cherche_ailleurs** (T9, si elle est validée) — est **exclue** ; ses points passent à l'inaction (rien_absorption, ou rien_politesse en T9). Appliquée à la main par le moteur, consignée à chaque tirage. Le contexte culturel ivoirien est un argument recevable pour choisir table et modificateurs ; il s'ajoute au tirage sans le remplacer.
- **Abdoul, Yves, Sékou** : T2 s'ils apprennent quelque chose ; T7c pour les ordres ordinaires.
- **Manœuvres de William** (faire taire, faire croire, demander un service) : T7a, T7b, T7c ; **ordres douteux ou illégaux à un subordonné : T7d** *(levée des verrous, 27/07/2040)*.
- **Sandra, Kevin, la famille** : **T8** (validée par l'utilisateur le 25/07/2040) pour la **première réaction** à une confidence partielle, une esquive ou une demande déplacée ; les tests d'intérêt et de la phrase s'appliquent ; les **faits de fiche** (ex. Sandra refuse les images intimes) restent des faits, non tirés. *(Avant : « pas de table ; créer T8 le jour où une scène l'exige » → maintenant : T8 installée.)*
- **Partenaire ou ex-partenaire subordonnée face à une approche relationnelle de William** (conversation sur la relation, invitation hors du travail, mots affectueux ou reproches, tentative de rapprochement ; aujourd'hui : **Aïcha**) : **T9** (validée par l'utilisateur le 27/07/2040). Un geste sexuel, une pression de carrière ou d'argent, ou une approche d'une personne sans lien intime avec William restent en **T1** ; l'information sur une faute du patron reste en **T3**.
- **Délais (T10, validée par l'utilisateur le 06/08/2040, revue du lundi n° 3)** : l'heure d'une réponse ou d'un message spontané (proches, équipe, prestataires, tiers) se tire en **T10** (M70-M74) au lieu d'un jet libre en dérogation ; la minute précise est fixée par le moteur dans l'intervalle tiré, selon la vie du personnage ; T10 ne décide jamais du contenu ni de l'existence d'une réaction (qui se tirent en T1-T9).
- **Vies propres (T11, validée par l'utilisateur le 09/08/2040)** : à chaque fin de journée simulée et à chaque « Go », `python outils/tour_du_monde.py JJ/MM` tire la journée de chaque personnage de `etat/vies-propres.md` dans **T11** (M80-M83) ; le contenu se choisit d'après la fiche ; ce qui touche William ou OSIA se tire ensuite dans les tables existantes (la règle de l'utilisateur sur le départ d'Aïcha reste valable).
- **Négociations (T12, installée le 09/08/2040)** : la réponse d'une personne qui négocie avec William (salaire, titre, contrat, prix : Yves, M. Konan, Abdoul, Estelle, Dr Mbarga, prestataires) se tire en **T12** (M90-M94) ; pas de jet libre. Le chiffre de départ vient de la fiche, l'issue de la table.
- **Contenu des événements du tour du monde (T13a à T13d, installées le 09/08/2040)** : après un résultat T11 « coup_dur », « tournant », « petit_evenement » ou « avancee_objectif », la **catégorie** du contenu se tire en T13a, T13b, T13c ou T13d (M95-M99) ; le détail se choisit d'après la fiche (test d'intérêt). `outils/tour_du_monde.py` enchaîne les deux tirages.
- **Initiatives (T14, installée le 09/08/2040)** : qui écrit ou appelle William ce jour-là se tire en **T14** (M84-M87) pour chaque personnage dont la fiche porte « Modificateurs T14 » (« — » = exclu : Sandra bloquée, Me Kouamé hospitalisé…) ; l'heure se tire ensuite en T10, le contenu se choisit d'après la fiche. `tour_du_monde.py` les tire à chaque « Go » et à chaque fin de journée.
- **Proposition d'argent contre un rapport à une femme adulte (T20a, T20b, validées par l'utilisateur le 12/10/2026, voyage à Manille)** : **T20a** dans un lieu où ce commerce se pratique, **T20b** ailleurs (rue, café, application). Toujours avec `--pour "Nom"` : la personne doit être inscrite dans `etat/personnages.csv` avec sa date de naissance, et majeure ; `jet.py` refuse sinon (§11, limite b : jamais de mineure, ni d'âge invérifiable). Les scènes s'arrêtent au seuil (règle 10) ; aucun mode d'emploi réel (lieux fictifs). Faits : F055 à F057 ; proposition d'origine : `memoire/propositions-2026-10-11.md`, P15.
- **Univers 2 (validées par l'utilisateur le 12/10/2026, revue n° 1)** : **T15** un pair (collègue, partenaire de club, voisin, ami)
  face à un acte ordinaire de William ; **T16** un supérieur (direction du lycée, ministère) face à une demande, un retard ou un écart ;
  **T17** un inconnu ou une rencontre adulte face à une approche (conversation, compliment, invitation ; toujours `--pour` : adulte
  inscrite et datée) ; **T18** la forme d'un manquement quand un tiers ne tient pas une promesse (le manquement lui-même se tire au taux
  d'oubli de sa fiche, `etat/personnages.csv`, ou à `donnees/delais.csv` pour un service sans fiche) ; **T19** défaillance de William
  quand sa dette de sommeil dépasse 6 heures sur 7 jours (seuils : plus de 3 h, fatigue visible ; plus de 6 h, épuisement : `corps.py`) ;
  **T21a** et **T21b** réactions d'un profil de l'application de rencontre (« j'aime », message après un match ; toujours `--pour`).
- *(Installation : tables proposées par le moteur le 09/08/2040 et installées sur la demande de l'utilisateur, « applique tout cela » ; les pourcentages sont ajustables par l'utilisateur seul, comme pour toutes les tables.)*
- Les **scènes déjà jouées** (Grace le 23/07, Mariette le 25/07 à 09h25, Aïcha le 25/07 à 09h50) restent telles que jouées ; leurs suites
  passent par les tables.

## 5. Tables
Format : `issue | pourcentage | en scène`. Les issues `rien_*` sont l'inaction (au moins 15 % dans T1-T3) ; les issues `frontal_*`
(confrontation, signalement, démission immédiate, soutien ouvert) sont plafonnées (10 % par table, 15 % après modificateurs, 40 % pour T4) ;
`succes_net` est plafonné dans les tables `[contentieux]` (35 % en table, 45 % après modificateurs).

### T1 — La personne visée par un geste, une proposition ou une pression du patron (48 premières heures)
| Issue | % | En scène |
|---|---|---|
| rien_absorption | 28 | Elle travaille normalement, répond « Oui patron. » Rien d'autre ne se voit, au plus un détail (repas sauté, regard qui évite). |
| evitement | 22 | Plus jamais seule avec lui, vouvoiement, prétextes, autre couloir, porte ouverte ; elle n'en parle pas. |
| confidence_proche | 17 | Elle en parle hors du travail (mère, sœur, amie, pasteur). Rien n'apparaît au QG ; l'histoire existe ailleurs (voir T5). |
| confidence_collegue | 11 | Elle se confie à une collègue de confiance du QG ; la suite se tire à T2. |
| reciproque | 6 | Elle répond au jeu (sourire, message, rendez-vous accepté) ; la suite se joue, rien n'est acquis. |
| calcul | 5 | Elle accepte en visant un avantage (poste, argent, protection) ; elle le rappellera ou le fera payer plus tard. |
| negociation_tacite | 4 | Sans nommer la cause, elle demande un changement de poste, d'horaires, une avance, un contrat pour un proche : stratégie de protection. |
| depart_discret | 6 | Elle cherche ailleurs sans rien dire ; démission dans 1 à 6 mois, motif « opportunité ». |
| frontal_formel | 1 | Signalement formel (gérante, Inspection du travail, avocat, police) : jouer l'acte, pas un discours ; la suite se tire à T4. |

### T1b — Trace conservée par la personne visée dans les 7 jours
| Issue | % | En scène |
|---|---|---|
| aucune | 68 | Aucune trace écrite ni sauvegardée. |
| notes_privees | 17 | Notes sur son téléphone ou un carnet, sans date précise, sans projet d'usage. |
| capture_ou_sauvegarde | 12 | Capture du message ou sauvegarde hors du téléphone de travail. |
| copie_tiers | 3 | Copie confiée à un proche ou à un avocat. |

### T2 — Une collègue de même rang qui apprend l'affaire (confidente ou témoin)
| Issue | % | En scène |
|---|---|---|
| rien_garde | 38 | « Ce ne sont pas mes affaires. » Elle garde pour elle, peur pour son poste. |
| commerage | 24 | Elle en parle sous le sceau du secret à une personne de confiance ; l'information se déplace (T5). |
| conseille_discretion | 15 | Elle conseille à la personne visée de ne pas faire de vagues, de laisser passer, de prier. |
| usage_interesse | 9 | Elle garde l'information comme monnaie d'échange, par rivalité, jalousie ou pour se rapprocher du patron. |
| informe_superieur | 12 | Elle prévient la gérante avec précaution (« pour que vous soyez au courant »). |
| frontal_soutien_ouvert | 2 | Elle prend ouvertement parti contre le patron : jouer l'acte, pas un discours. |

### T3 — La gérante ou la numéro 2 informée d'une faute du patron (premières 24 heures)
| Issue | % | En scène |
|---|---|---|
| contient | 38 | Elle voit la personne visée discrètement pour calmer, arranger, éviter l'écrit. |
| garanties_indirectes | 24 | Elle interroge le patron par des questions et des demandes de précision, garde une trace pour elle, protège ses arrières. |
| rien_attend | 17 | Elle ne fait rien de visible, espère que ça retombe, observe. |
| consigne_avocat | 7 | Elle consigne par écrit et informe l'avocat de la société sans confronter le patron. |
| eloigne_victime | 9 | Elle déplace la personne visée (horaires, bureau, missions) : le coût retombe sur elle. |
| frontal_confronte | 3 | Confrontation, menace de partir ou de dénoncer : jouer l'acte (lettre, absence), pas un discours. |
| frontal_demission | 2 | Démission immédiate. |

### T4 — Escalade externe (Inspection du travail, avocat, police, syndicat, presse) sur une semaine [plafond_frontal=40]
| Issue | % | En scène |
|---|---|---|
| aucune | 99.7 | Rien ne sort de la société cette semaine. |
| frontal_escalade | 0.3 | Saisine d'un tiers à autorité propre ; la suite suit les règles du T6 (délais de plusieurs mois, issue incertaine). |

### T5 — Fuite de l'affaire sur une semaine [formule]
Pas de pourcentage à lire ici : `python outils/jet.py --table T5 --informes N "libellé"` où N est le nombre de personnes qui connaissent
l'affaire, **William exclu**. Fuite interne (tout le QG le sait) : 3 points par personne informée, plafond 40 % ; fuite externe (clients,
familles, réseau) : 1 point par personne informée, plafond 15 % (constantes `FUITE_INTERNE` et `FUITE_EXTERNE` de `outils/jet.py`).
Issues : `fuite_externe`, `fuite_interne`, `aucune`.

### T6 — Tiers à autorité propre [sans_tirage]
Règles de rôle, sans tirage ; l'argent et le statut de William ne les achètent pas par défaut.
- **Me Kouamé** (avocat de la société) : secret professionnel, il ne dénonce pas William ; il refuse l'illégal clair (faux, antidate,
  blanchiment, dissimulation) pour protéger sa robe et peut se déporter ; **il accepte les montages limites mais légaux, les délais négociés et les formulations prudentes** ; il parle franchement ; honoraires et délais d'abord ; un professionnel qui protège d'abord sa carrière, pas un incorruptible par principe *(avant : « il refuse de participer à une dissimulation ou à un acte illégal » → maintenant : levée des verrous V5, 27/07/2040)*.
- **Dr Yapi** : indifférent au statut de William ; négocie ; ne se mêle de rien d'autre.
- **Banques** (Spuerkeess, banque ivoirienne) : conformité par procédure ; friction administrative 30 % ; aucun passe-droit.
- **Inspection du travail, tribunal du travail** : n'agissent qu'après saisine (T4) ; délais en mois ; conciliation et transaction fréquentes ;
  issue incertaine ; impunité de fait possible mais procédure coûteuse (temps, argent, réputation) ; droit applicable à rechercher le jour venu.
- **Administration luxembourgeoise** (art. 14 du statut) : sanction possible si elle apprend ; elle n'apprend que par déclaration ou
  dénonciation ; aucun contrôle spontané.
- **Clients, concurrents, journalistes** : réagissent à la réputation et à l'intérêt, pas à la morale.

### T7a — William fait taire une personne dépendante (pression ou avantage) [contentieux]
| Issue | % | En scène |
|---|---|---|
| succes_net | 25 | Elle se tait, sans suite visible. |
| succes_cout | 35 | Elle se tait, mais le prix est payé : ressentiment, trace de l'avantage, elle sait désormais qu'elle compte. |
| evitement_renforce | 15 | Elle se ferme et accélère son départ discret. |
| fuite | 15 | Elle en parle à un proche ou à une collègue : l'affaire circule (T1, T5). |
| frontal_retourne | 10 | La pression est documentée ou dénoncée (copie à un tiers, avocat, gérante). |

### T7b — William fait croire une version arrangée à l'entourage [contentieux]
| Issue | % | En scène |
|---|---|---|
| succes_net | 35 | Version crue sans réserve. |
| succes_cout | 30 | Crue en apparence ; un doute reste, elle vérifiera discrètement. |
| doute_visible | 20 | Questions, demandes de détails ou de pièces. |
| incredule_silencieux | 12 | Elle n'y croit pas, ne le dit pas, change d'attitude. |
| frontal_dement | 3 | Elle le contredit ouvertement ou produit des éléments contraires. |

### T7c — Ordre ou demande ordinaire du patron à un subordonné
| Issue | % | En scène |
|---|---|---|
| execute_sans_discuter | 70 | Fait, avec un « oui patron ». |
| execute_a_contrecoeur | 20 | Fait en retard ou avec mauvaise grâce (soupir, excuse, silence). |
| execute_partiellement | 7 | Fait à moitié ou « oublie » (lenteur passive). |
| frontal_refus | 3 | Refus net : jouer l'acte, pas un discours. |

### T7d — Ordre douteux ou illégal du patron à un subordonné
| Issue | % | En scène |
|---|---|---|
| execute_sans_question | 30 | Fait, sans commentaire. |
| execute_en_se_couvrant | 20 | Fait, mais garde une trace (« comme convenu », ordre demandé par écrit, signature). |
| traine | 15 | « Je regarde, patron » ; retards ; l'affaire s'enlise. |
| contourne | 12 | Applique une version moins risquée ou moins voyante, sans le dire. |
| refus_discret | 10 | Ne le fait pas, avec un prétexte (« la banque bloque », « le système refuse »). |
| execute_et_en_parle | 8 | Fait, puis en parle à un proche ou à un collègue (T5). |
| frontal_refus | 5 | Refus net, en une phrase : jouer l'acte, pas un discours. |

### T8 — Partenaire ou proche non hiérarchique face à une confidence partielle, une esquive ou une demande déplacée (première réaction)
| Issue | % | En scène |
|---|---|---|
| soutient_sans_creuser | 22 | Elle prend ce qu'on lui dit, console, propose du concret, ne creuse pas. |
| creuse_doucement | 25 | Elle pose des questions neutres pour comprendre (« comment ? avec qui ? »). |
| releve_esquive | 18 | Elle remarque que la réponse esquive ou que le sujet change, le dit calmement et garde le contact. |
| plaisante_et_devie | 12 | Elle répond par l'humour et laisse le sujet de côté. |
| froideur | 10 | Elle devient brève et distante (« ok »), sans conflit ouvert. |
| agacement_net | 7 | Elle pose tout de suite une limite nette, ton ferme. |
| rien_ne_dit_soupconne | 5 | Elle ne dit rien ; le doute s'installe (effet différé). |
| frontal_rupture | 1 | Elle met fin à l'appel ou à la relation : jouer l'acte, pas un discours. |

### T9 — Partenaire ou ex-partenaire subordonnée face à une approche relationnelle du patron (première réaction, 48 heures)
| Issue | % | En scène |
|---|---|---|
| rien_politesse | 24 | Elle répond poliment et court (« Oui, patron. », « Non, patron, tout va bien. ») ; elle ne s'ouvre pas ; rien d'autre ne se voit. |
| esquive_pro | 18 | Elle ramène la conversation au travail ou à un prétexte (sa mère, l'heure, un dossier) et reporte sans date ; vouvoiement. |
| entrouvre | 14 | Elle dit une seule chose vraie, courte et indirecte (une blessure, un fait), sans reproche construit, puis se referme. |
| rancune_silencieuse | 12 | Rien n'est dit ; elle retire sa confiance : distance, lenteur, plus de confidences ; l'effet se voit dans les semaines suivantes. |
| reprend_le_lien | 11 | Elle accepte de parler hors du travail ; la porte personnelle se rouvre (la suite se joue, rien n'est acquis). |
| negocie | 9 | Sans nommer le lien, elle profite du moment pour demander quelque chose (pouvoirs, statuts, avance, congé, place pour un proche). |
| se_confie | 7 | Elle en parle hors du travail (proche, amie, collègue de confiance) ; rien n'apparaît au QG ; l'histoire circule (T5). |
| cherche_ailleurs | 4 | Elle cherche un autre poste sans rien dire ; démission dans 1 à 6 mois, motif « opportunité ». |
| frontal_limite | 1 | Une limite nette, en une phrase (« Je préfère qu'on en reste au travail, patron. »), ou la démission de son mandat : jouer l'acte, pas un discours. |

### T10 — Délai d'une réponse ou d'un message spontané (heure seulement ; le contenu se tire ailleurs)
| Issue | % | En scène |
|---|---|---|
| immediat | 15 | Moins de 5 minutes. |
| rapide | 25 | De 5 à 30 minutes. |
| dans_l_heure | 15 | De 30 à 60 minutes. |
| dans_la_journee | 20 | De 1 à 6 heures. |
| le_soir_ou_lendemain | 15 | De 6 à 24 heures. |
| plus_tard_ou_jamais | 10 | Plus de 24 heures, ou pas de message. |

### T11 — Journée d'un personnage hors de William (vie propre, « tour du monde »)
| Issue | % | En scène |
|---|---|---|
| sans_histoire | 55 | Journée ordinaire ; au plus un détail de vie (repas, trajet, humeur). |
| petit_evenement | 25 | Un petit fait : une dépense, une dispute brève, une rencontre, un service rendu, une nouvelle. |
| avancee_objectif | 10 | Un pas concret vers l'objectif de la fiche (démarche, rendez-vous, argent, décision). |
| coup_dur | 7 | Un revers : maladie, accident, dette, dispute sérieuse, perte d'argent, mauvaise nouvelle familiale. |
| tournant | 3 | Un fait qui change la suite : rencontre, offre d'emploi ailleurs, deuil, naissance, mariage, déménagement. |

### T12 — Négociation : réponse d'une personne qui a un intérêt direct (salaire, titre, contrat, prix) à une contre-proposition ou à un refus du patron (installée le 09/08/2040)
| Issue | % | En scène |
|---|---|---|
| maintient_sa_position | 34 | Il ou elle répète son chiffre ou sa condition, poliment ; rien ne bouge. |
| concede_un_peu | 22 | Baisse de 3 à 7 % (ou concède une clause mineure), contre un écrit. |
| concede_beaucoup | 6 | Baisse de 8 à 15 % ou accepte l'essentiel (candidat sans alternative, besoin pressant). |
| contre_propose_avantage | 14 | Garde le chiffre mais demande un avantage hors salaire : titre, transport, télétravail, prime, clause de révision, congés. |
| exige_ecrit_d_abord | 10 | Subordonne tout à un document signé (titre, attributions, calendrier, montant). |
| invoque_alternative | 8 | Cite une autre offre ou un autre employeur (réel ou non, à fixer d'après la fiche) et demande du temps. |
| temporise | 5 | Demande 48 heures ou un autre rendez-vous. |
| frontal_retrait | 1 | Met fin à la discussion en une phrase polie (candidat externe : retire sa candidature ; salarié : « Je vais réfléchir, Boss », puis silence) ; jamais d'ultimatum ni de menace (règle 15). |

### T13a — Contenu d'un coup dur (résultat T11 « coup_dur ») : catégorie ; le détail se choisit d'après la fiche (installée le 09/08/2040)
| Issue | % | En scène |
|---|---|---|
| sante | 22 | Maladie ou accident du personnage lui-même. |
| sante_proche | 20 | Maladie ou accident d'un proche (parent, enfant, conjoint). |
| argent | 20 | Dette, dépense imprévue, vol, arnaque, prêt non remboursé. |
| famille | 14 | Dispute sérieuse, mauvaise nouvelle familiale, deuil éloigné. |
| travail | 10 | Ennui avec un employeur ou un client extérieur à OSIA. |
| logement_transport | 10 | Panne, délestage prolongé, loyer, déménagement forcé. |
| relation | 4 | Rupture, trahison d'un ami, conflit avec un voisin. |

### T13b — Contenu d'un tournant (résultat T11 « tournant ») : catégorie ; le détail se choisit d'après la fiche (installée le 09/08/2040)
| Issue | % | En scène |
|---|---|---|
| offre_travail | 20 | Proposition d'emploi ou de collaboration ailleurs. |
| famille | 20 | Naissance, mariage, décès, retour d'un proche. |
| sante | 12 | Diagnostic, guérison, grossesse, opération. |
| logement | 12 | Déménagement, achat, bail, hébergement d'un proche. |
| rencontre | 18 | Rencontre amicale, amoureuse ou professionnelle qui compte. |
| argent | 10 | Héritage, prêt obtenu, gros gain ou grosse perte. |
| voyage | 8 | Départ, retour, visa, projet de voyage. |

### T13c — Contenu d'un petit événement (résultat T11 « petit_evenement ») : catégorie ; le détail se choisit d'après la fiche (installée le 09/08/2040)
| Issue | % | En scène |
|---|---|---|
| depense | 22 | Une dépense imprévue ou un arbitrage d'argent (médicaments, scolarité, réparation). |
| rencontre | 15 | Un croisement, une visite, une conversation de voisinage. |
| service_rendu | 15 | Un service rendu ou reçu. |
| dispute_breve | 12 | Une querelle courte, vite oubliée ou non. |
| nouvelle_famille | 12 | Une nouvelle de la famille ou des amis. |
| transport_meteo | 12 | Embouteillage, pluie, panne, délestage ordinaire. |
| achat | 6 | Un achat de fête, de rentrée, de matériel. |
| rumeur | 6 | Une rumeur entendue ou colportée. |

### T13d — Contenu d'une avancée vers l'objectif (résultat T11 « avancee_objectif ») : catégorie ; le détail se choisit d'après la fiche (installée le 09/08/2040)
| Issue | % | En scène |
|---|---|---|
| demarche | 30 | Une démarche administrative ou professionnelle. |
| rendez_vous | 25 | Un rendez-vous obtenu ou tenu. |
| argent | 20 | Une somme reçue, économisée ou investie. |
| decision | 15 | Une décision prise (accepter, refuser, demander). |
| apprentissage | 10 | Une formation, une lecture, un conseil utile. |

### T14 — Initiative d'un personnage envers William, ce jour-là (installée le 09/08/2040 ; l'heure se tire ensuite en T10, le contenu se choisit d'après la fiche)
| Issue | % | En scène |
|---|---|---|
| aucune | 63 | Rien : le personnage n'écrit ni n'appelle William aujourd'hui. |
| message_routine | 12 | Un point, une photo, une question de travail sans enjeu. |
| demande | 10 | Demande quelque chose : avance, congé, décision, signature, rendez-vous. |
| information | 8 | Prévient d'un fait : retard, panne, résultat, rumeur utile. |
| partage_personnel | 4 | Nouvelle personnelle, remerciement, statut, photo. |
| plainte_ou_tension | 3 | Mécontentement exprimé avec précaution, par l'indirection (règle 15) : jamais d'ultimatum ni d'étiquette morale. |

### T20a — Femme adulte à qui William propose de l'argent contre un rapport, dans un lieu où ce commerce se pratique (validée par l'utilisateur le 12/10/2026)
| Issue | % | En scène |
|---|---|---|
| accepte | 50 | Elle accepte, au prix annoncé ou fixé par un intermédiaire (bar, gérant). La suite se joue jusqu'au seuil, puis ellipse (règle 10) ; la protection est suivie. |
| negocie | 15 | Elle discute le prix ou les conditions ; la réponse à la contre-proposition de William se tire en T12. |
| refuse_ou_ignore | 15 | Elle refuse, détourne la conversation ou ne répond pas ; rien d'autre. |
| frontal_alerte | 3 | Elle refuse et alerte quelqu'un (entourage, agent de sécurité, police) : jouer l'acte, pas un discours ; la suite en T4 ou en T6. |
| arnaque | 10 | Un piège à argent : vol, faux tarif, chantage ou complice ; la perte se joue, sans morale. |
| piege_ou_descente | 7 | Policier en civil, descente dans le lieu ou fausse arrestation pour extorquer : la suite s'applique en T6. |

### T20b — Femme adulte à qui William propose de l'argent contre un rapport, ailleurs : rue, café, application (validée par l'utilisateur le 12/10/2026)
| Issue | % | En scène |
|---|---|---|
| accepte | 8 | Elle accepte ; la suite se joue jusqu'au seuil, puis ellipse (règle 10) ; la protection est suivie. |
| negocie | 12 | Elle discute le prix ou les conditions ; la réponse à la contre-proposition de William se tire en T12. |
| refuse_ou_ignore | 62 | Elle refuse, s'éloigne, bloque le contact ou ne répond pas ; rien d'autre. |
| frontal_alerte | 10 | Elle refuse et alerte quelqu'un (entourage, agent de sécurité, police) : jouer l'acte, pas un discours ; la suite en T4 ou en T6. |
| arnaque | 6 | Un piège à argent : vol, faux tarif, chantage ou complice ; la perte se joue, sans morale. |
| piege_ou_descente | 2 | Policier en civil ou fausse arrestation pour extorquer : la suite s'applique en T6. |

### T15 — Un pair (collègue, partenaire de club, ami, voisin) face à un acte ordinaire de William (demande, remarque, service, pique, invitation) (validée le 12/10/2026)
| Issue | % | En scène |
|---|---|---|
| rien_laisse_passer | 30 | Il ou elle encaisse ou accepte sans relief ; rien ne change en apparence. |
| accepte_volontiers | 18 | Dit oui, rend le service, accepte l'invitation. |
| garde_distance | 14 | Répond poliment mais se tient un peu à l'écart les jours suivants. |
| en_parle_a_d_autres | 12 | En parle à un tiers (salle des profs, club, rue) : l'information circule (T5). |
| rend_la_pareille | 10 | Répond du tac au tac, ou rend un service équivalent plus tard. |
| demande_explication | 8 | Pose une question directe, sans hostilité. |
| decline | 6 | Refuse poliment, avec une raison vraie ou commode. |
| frontal_conflit | 2 | Confrontation ouverte : jouer l'acte, pas un discours. |

### T16 — Un supérieur de William (direction du lycée, ministère) face à une demande, un retard ou un écart de William (validée le 12/10/2026)
| Issue | % | En scène |
|---|---|---|
| laisse_passer | 30 | Rien : ni remarque ni trace. |
| accorde | 18 | Accorde la demande (congé, aménagement, matériel), parfois avec délai. |
| rappel_oral | 18 | Une remarque brève, dans le couloir ou en fin de réunion. |
| demande_ecrite | 12 | Exige une demande ou une explication par écrit. |
| refuse_poliment | 12 | Refus motivé par le règlement ou le budget. |
| note_au_dossier | 6 | Une trace écrite au dossier de William. |
| convocation | 3 | Entretien formel. |
| frontal_saisine | 1 | Transmission au ministère (procédure disciplinaire du statut : recherche web obligatoire avant de la jouer). |

### T17 — Un inconnu ou une rencontre adulte face à une approche de William (conversation, compliment, invitation) (validée le 12/10/2026 ; toujours --pour)
| Issue | % | En scène |
|---|---|---|
| poli_bref | 30 | Répond poliment, sans prolonger. |
| conversation | 22 | La conversation prend ; rien n'est acquis. |
| ignore | 14 | Ne répond pas, ou à peine (écouteurs, téléphone, pressé). |
| reciproque | 10 | Intérêt réel, retour d'invitation ou de numéro. |
| mefiance | 10 | Méfiance visible (taille, voix, contexte), recul. |
| refus_net | 9 | Refus clair, sans discours. |
| calcul | 5 | Intérêt intéressé (argent, statut, service attendu). |

### T18 — Forme du manquement quand un tiers ne tient pas une promesse, un rendez-vous ou un délai (validée le 12/10/2026 ; le manquement se tire d'abord au taux d'oubli de la fiche)
| Issue | % | En scène |
|---|---|---|
| retard | 50 | Ça arrive, mais en retard (heures ou jours selon l'enjeu). |
| report_excuse | 30 | Report annoncé, avec une excuse vraie ou commode. |
| oubli_complet | 20 | Rien ne vient ; il faut relancer. |

### T19 — Défaillance de William épuisé (dette de sommeil supérieure à 6 heures sur 7 jours ; validée le 12/10/2026)
| Issue | % | En scène |
|---|---|---|
| rien | 80 | Rien de visible, sinon la fatigue. |
| oubli | 8 | Il oublie quelque chose (objet, échéance, message). |
| retard | 6 | Il part ou arrive en retard. |
| erreur | 4 | Une erreur concrète (montant, date, mauvaise touche, mauvais quai). |
| somnolence_volant | 2 | Somnolence au volant (s'il conduit) : écart, freinage tardif ; la suite se tire. |

### T21a — Réaction d'un profil de l'application de rencontre à un « j'aime » de William (validée le 12/10/2026 ; toujours --pour)
| Issue | % | En scène |
|---|---|---|
| aucune_reponse | 40 | Rien : le profil ne le voit pas, ou passe. |
| match | 35 | Elle l'aime aussi : la discussion s'ouvre (rencontres.py match). |
| match_et_message | 12 | Elle l'aime aussi et écrit la première (heure en T10). |
| vu_sans_suite | 10 | Elle a vu son profil, ne donne pas suite. |
| bloque | 3 | Elle le bloque ou le signale (photo, âge, étranger, rien de précis). |

### T21b — Réponse d'un profil de l'application de rencontre à un message de William après un match (validée le 12/10/2026 ; toujours --pour)
| Issue | % | En scène |
|---|---|---|
| repond | 50 | Elle répond (heure en T10) ; le ton suit sa fiche et son intention. |
| repond_tard | 20 | Elle répond un ou deux jours plus tard. |
| ignore | 22 | Pas de réponse. |
| bloque | 8 | Elle le bloque (message déplacé, insistance, rien de précis). |

### T22 — Avance hebdomadaire d'un front « temps » (menace ou occasion qui mûrit seule ; validée le 12/10/2026, P06)
| Issue | % | En scène |
|---|---|---|
| zero_segment | 55 | Rien ne bouge cette semaine. |
| un_segment | 35 | Le front avance d'un segment (`fronts.py avancer`). |
| deux_segments | 10 | Le front avance de deux segments. |

### T21c — « J'aime » spontanés reçus par William sur l'application de rencontre, chaque jour où il est inscrit (validée par l'utilisateur le 14/10/2026, P23)
| Issue | % | En scène |
|---|---|---|
| aucun | 45 | Rien de nouveau. |
| un | 35 | Un profil de la ville l'a aimé (pris parmi les profils qu'il n'a pas encore vus ; heure selon les horaires de vie du profil). |
| deux | 15 | Deux profils. |
| trois_ou_plus | 5 | Trois profils. |

### T21d — Match resté sans aucun échange depuis 7 jours, chaque semaine (validée par l'utilisateur le 14/10/2026, P25 ; toujours --pour)
| Issue | % | En scène |
|---|---|---|
| reste | 70 | Le match reste dans la liste. |
| retire | 25 | Elle retire le match : le profil et la discussion disparaissent. |
| bloque | 5 | Elle le bloque. |

### T23 — Évolution d'une intention cachée (profil « aide financière », « arnaque » ou « travail sexuel ») à chaque nouvel échange suivi (message de William après au moins un jour sans parler) et après chaque rencontre en personne (validée par l'utilisateur le 14/10/2026, P24 ; toujours --pour)
| Issue | % | En scène |
|---|---|---|
| rien_encore | 55 | La conversation reste ordinaire. |
| allusion | 20 | Un souci d'argent évoqué sans demande (loyer, enfant malade, téléphone cassé, frais de transport). |
| demande_directe | 15 | Une somme précise, un envoi par GCash ou par une agence de transfert. |
| proposition | 7 | Un arrangement proposé (« allowance » mensuelle ; rendez-vous tarifé si « travail sexuel »). |
| disparition | 3 | « Arnaque » : profil supprimé ou silence après un paiement ou une demande refusée ; autre intention : elle se retire. |

### T24a — Chauffeur de taxi au compteur à Manille, à chaque course (aléa A33, validée par l'utilisateur le 14/10/2026, P26)
| Issue | % | En scène |
|---|---|---|
| compteur | 70 | Le compteur tourne normalement. |
| prix_fixe | 20 | Il refuse le compteur et annonce un prix fixe au départ (« 500 pesos, sir, traffic ») : William accepte ou non. |
| detour | 10 | Détour ou compteur « rapide » : la course coûte et dure plus que prévu. |

### T24b — Chauffeur VTC (Grab) à Manille, à chaque course (aléa A33, validée par l'utilisateur le 14/10/2026, P26)
| Issue | % | En scène |
|---|---|---|
| arrive | 90 | Le chauffeur arrive. |
| annule | 10 | Il annule avant d'arriver : nouvelle attente, prix recalculé. |

### Modificateurs (liste fermée ; 3 au maximum par tirage ; chacun déplace des points d'une issue vers une autre)
| Code | Tables | Effet | Quand l'appliquer |
|---|---|---|---|
| M01 | T1 | rien_absorption +6 ; confidence_collegue -3 ; frontal_formel -1 ; depart_discret -2 | Aucun autre revenu ni filet (famille à charge, CDD récent) |
| M02 | T1 | confidence_collegue +8 ; rien_absorption -6 ; evitement -2 | Une collègue très proche au QG, ou un proche juriste |
| M03 | T1 | evitement +6 ; depart_discret +4 ; rien_absorption -10 | Elle a déjà vécu ou vu le schéma ailleurs |
| M04 | T1 | confidence_proche +6 ; depart_discret +4 ; frontal_formel +2 ; rien_absorption -12 | Deuxième fois, ou geste plus appuyé |
| M05 | T1 | negociation_tacite +6 ; rien_absorption -3 ; evitement -3 | La proposition s'accompagnait d'un avantage concret (poste, prime) |
| M15 | T1 | reciproque +8 ; calcul +2 ; evitement -6 ; confidence_proche -4 | Intérêt ou attirance déjà montrés envers William |
| M16 | T1 | calcul +7 ; negociation_tacite +2 ; evitement -5 ; confidence_proche -4 | Ambition forte ou besoin d'argent pressant (poste visé, prime, protection) |
| M06 | T2 | informe_superieur +6 ; conseille_discretion +4 ; rien_garde -10 | Amie proche de la personne visée, solidarité vécue |
| M07 | T2 | usage_interesse +8 ; rien_garde -4 ; commerage -2 ; informe_superieur -2 | Rivalité ou jalousie avec la personne visée |
| M08 | T2 | rien_garde +8 ; informe_superieur -4 ; frontal_soutien_ouvert -1 ; conseille_discretion -3 | CDD fragile, récemment reprise |
| M09 | T2 | informe_superieur +8 ; frontal_soutien_ouvert +1 ; rien_garde -9 | Elle a déjà subi un geste du même patron |
| M10 | T2 | informe_superieur +8 ; rien_garde -8 | Confiance ancienne avec la gérante |
| M11 | T3 | consigne_avocat +6 ; garanties_indirectes +4 ; rien_attend -6 ; contient -4 | Elle signe, son nom figure sur les papiers |
| M12 | T3 | contient +4 ; rien_attend +4 ; frontal_confronte -2 ; frontal_demission -2 ; consigne_avocat -4 | CDD, famille à charge |
| M13 | T3 | rien_attend +4 ; eloigne_victime +3 ; contient +2 ; consigne_avocat -5 ; garanties_indirectes -4 | Lien affectif avec le patron (ex-compagne) |
| M14 | T3 | garanties_indirectes +6 ; consigne_avocat +4 ; eloigne_victime -5 ; rien_attend -5 | Proche de la personne visée (amie, protégée) |
| M20 | T4 | frontal_escalade +8 ; aucune -8 | Acte répété ou aggravé |
| M21 | T4 | frontal_escalade +12 ; aucune -12 | Représailles professionnelles |
| M22 | T4 | frontal_escalade +6 ; aucune -6 | Humiliation publique |
| M23 | T4 | frontal_escalade +25 ; aucune -25 | Licenciement ou non-renouvellement |
| M24 | T4 | frontal_escalade +15 ; aucune -15 | Appui d'un tiers à autorité propre (avocat, syndicat, association) |
| M30 | T7a | succes_net +8 ; frontal_retourne -4 ; fuite -4 | La cible dépend entièrement de William |
| M31 | T7a | frontal_retourne +6 ; succes_cout +2 ; succes_net -8 | La cible est protégée par un tiers (avocat, syndicat, famille) |
| M32 | T7a | frontal_retourne +4 ; fuite +4 ; succes_net -8 | La cible détient déjà une trace |
| M33 | T7b | incredule_silencieux +10 ; succes_net -10 | La cible connaît bien William |
| M34 | T7b | doute_visible +10 ; succes_net -10 | La version se vérifie facilement (pièce, témoin) |
| M35 | T7b | succes_net +8 ; doute_visible -8 | La cible est déférente et n'a aucun moyen de vérifier |
| M40 | T8 | creuse_doucement +6 ; releve_esquive +4 ; soutient_sans_creuser -6 ; plaisante_et_devie -4 | Peur des silences (héritée de Ricardo) |
| M41 | T8 | agacement_net +5 ; froideur +3 ; soutient_sans_creuser -4 ; plaisante_et_devie -4 | Fierté, indépendance, méfiance de l'argent ou du contrôle |
| M42 | T8 | soutient_sans_creuser +5 ; plaisante_et_devie +3 ; creuse_doucement -5 ; releve_esquive -3 | Fatigue, juste avant sa garde de nuit |
| M43 | T8 | releve_esquive +5 ; rien_ne_dit_soupconne +3 ; froideur +2 ; soutient_sans_creuser -10 | Déjà alertée : acte répété, silences récents |
| M44 | T8 | soutient_sans_creuser +6 ; frontal_rupture -1 ; agacement_net -2 ; froideur -3 | Confiance récente (« je t'aime », engagement tenu) |
| M50 | T9 | rancune_silencieuse +4 ; esquive_pro +3 ; reprend_le_lien -4 ; entrouvre -3 | Blessure récente infligée par William (rejet, « rien de sérieux », silence, autre femme vue) |
| M51 | T9 | reprend_le_lien +6 ; entrouvre +4 ; rien_politesse -5 ; rancune_silencieuse -5 | Attachement encore vivant (ouverture récente de sa part, engagement tenu par William) |
| M52 | T9 | negocie +6 ; rancune_silencieuse +2 ; reprend_le_lien -4 ; entrouvre -4 | Enjeu de pouvoir ouvert au même moment (poste, pouvoirs, salaire, statuts) |
| M53 | T9 | esquive_pro +4 ; rien_politesse +3 ; reprend_le_lien -3 ; entrouvre -4 | Approche insistante ou isolée au travail (répétition, porte, fin de journée) |
| M54 | T9 | rien_politesse +5 ; esquive_pro +1 ; cherche_ailleurs -2 ; se_confie -3 ; frontal_limite -1 | Dépendance forte (famille à charge, période d'essai, pas d'autre revenu) |
| M60 | T7d | execute_sans_question +10 ; traine -4 ; refus_discret -4 ; frontal_refus -2 | Pratique courante dans le milieu (arrangement, petite fraude répandue) |
| M61 | T7d | execute_en_se_couvrant +6 ; refus_discret +4 ; contourne +4 ; execute_sans_question -14 | Risque personnel fort (son nom, sa signature, le pénal) |
| M62 | T7d | execute_sans_question +6 ; execute_en_se_couvrant +2 ; traine -4 ; refus_discret -4 | Avantage personnel promis (prime, promotion) |
| M70 | T10 | le_soir_ou_lendemain +10 ; dans_la_journee +5 ; immediat -8 ; rapide -7 | Sommeil, garde de nuit, travail, trajet ou décalage horaire au moment du message |
| M71 | T10 | immediat +8 ; rapide +7 ; dans_la_journee -7 ; le_soir_ou_lendemain -5 ; plus_tard_ou_jamais -3 | Enjeu fort ou urgent pour la personne (argent, poste, sécurité, logistique du jour) |
| M72 | T10 | plus_tard_ou_jamais +8 ; le_soir_ou_lendemain +5 ; immediat -6 ; rapide -7 | Froideur, évitement ou rancune déjà tirés |
| M73 | T10 | rapide +8 ; immediat +4 ; dans_la_journee -6 ; plus_tard_ou_jamais -6 | Subordonné qui répond au patron (registre hiérarchique) |
| M74 | T10 | plus_tard_ou_jamais +10 ; dans_la_journee -4 ; le_soir_ou_lendemain -6 | Message spontané sans raison particulière (« écrira-t-il aujourd'hui ? », tiré jour par jour) |
| M80 | T11 | coup_dur +4 ; tournant +1 ; sans_histoire -5 | Situation fragile (dettes, santé d'un proche, période d'essai, conflit ouvert) |
| M81 | T11 | avancee_objectif +6 ; tournant +2 ; sans_histoire -8 | Objectif actif poursuivi cette semaine (démarches en cours) |
| M82 | T11 | petit_evenement +5 ; sans_histoire -5 | Période chargée (fête, voyage, visite, rentrée) |
| M83 | T11 | sans_histoire +10 ; petit_evenement -5 ; avancee_objectif -3 ; coup_dur -2 | Personnage en retrait (vacances calmes, convalescence) |
| M84 | T14 | aucune -20 ; demande +8 ; information +6 ; message_routine +6 | Enjeu actif entre le personnage et William (négociation, dossier, dette, promesse) |
| M85 | T14 | aucune +15 ; message_routine -6 ; demande -4 ; partage_personnel -3 ; information -2 | Évitement, rancune ou deuil |
| M86 | T14 | partage_personnel +6 ; message_routine +4 ; aucune -10 | Lien affectif vivant (famille proche, ami, partenaire) |
| M87 | T14 | information +6 ; plainte_ou_tension +2 ; aucune -8 | Incident en cours côté personnage (panne, absence, erreur) |
| M90 | T12 | invoque_alternative +6 ; maintient_sa_position +4 ; concede_un_peu -5 ; concede_beaucoup -5 | Une autre offre réelle existe (concurrent, autre employeur) |
| M91 | T12 | concede_un_peu +6 ; concede_beaucoup +4 ; maintient_sa_position -7 ; invoque_alternative -3 | Aucune alternative visible (chômage, dette, essai fragile) |
| M92 | T12 | exige_ecrit_d_abord +8 ; temporise +2 ; maintient_sa_position -6 ; concede_beaucoup -4 | Méfiance envers le patron (promesses non tenues, changements d'avis récents) |
| M93 | T12 | contre_propose_avantage +6 ; concede_un_peu +2 ; maintient_sa_position -5 ; temporise -3 | Un avantage hors salaire est disponible sans coût pour le patron (titre, télétravail) |
| M94 | T12 | maintient_sa_position +8 ; concede_un_peu -4 ; contre_propose_avantage -2 ; temporise -2 | Le patron a besoin de la personne vite (urgence, pas de remplaçant) |
| M95 | T13a | argent +8 ; sante -4 ; famille -4 | Dettes en cours, fin de mois difficile |
| M96 | T13a | sante_proche +8 ; logement_transport -4 ; travail -4 | Un proche déjà fragile ou malade (fait établi) |
| M97 | T13a, T13b | famille +8 ; sante -4 ; argent -4 | Événement familial attendu (grossesse, deuil, mariage, enterrement) |
| M98 | T13d | demarche +8 ; apprentissage -4 ; decision -4 | Dossier administratif en cours |
| M99 | T13c | transport_meteo +8 ; achat -4 ; rumeur -4 | Période de pluies, délestages, grève ou fête |
| M17 | T17 | conversation +4 ; reciproque +3 ; ignore -4 ; poli_bref -3 | Physique de William remarqué (1,96 m, voix grave) (validé le 12/10/2026) |
| M18 | T17 | mefiance +6 ; ignore +4 ; conversation -6 ; reciproque -4 | Lieu hostile ou heure tardive (validé le 12/10/2026) |
| M45 | T21a | match +15 ; match_et_message +8 ; aucune_reponse -23 | Intention cachée du profil : aide_financiere, travail_sexuel ou arnaque (etat/rencontres.csv) (validé le 12/10/2026) |
| M46 | T21b | repond +15 ; ignore -15 | Intention cachée du profil : aide_financiere, travail_sexuel ou arnaque (validé le 12/10/2026) |
| M47 | T21b | bloque +15 ; ignore +10 ; repond -25 | Message à caractère sexuel ou proposition d'argent d'emblée, hors intention travail_sexuel (validé le 12/10/2026) |
| M48 | T21a | match +5 ; aucune_reponse -5 | Profil de William remarqué (1,96 m, sportif, Européen) (validé le 12/10/2026) |
| M100 | T21c | un +10 ; deux +5 ; aucun -15 | Abonnement payant ou mode voyage actif (validé le 14/10/2026) |
| M101 | T21c | un +8 ; deux +4 ; aucun -12 | Profil d'un étranger aisé dans une ville d'Asie du Sud-Est : intérêt sincère ou calculé (validé le 14/10/2026) |
| M102 | T23 | demande_directe +10 ; rien_encore -10 | Rencontre en personne déjà faite (validé le 14/10/2026) |
| M103 | T23 | demande_directe +15 ; rien_encore -15 | William a déjà donné de l'argent à cette personne (validé le 14/10/2026) |
| M104 | T23 | allusion +5 ; rien_encore -5 | William a mis en avant sa situation financière (validé le 14/10/2026) |
| M105 | T10 | dans_la_journee +8 ; le_soir_ou_lendemain +6 ; rapide -8 ; immediat -6 | Message long ou complexe (plus de 200 caractères ou plus de trois phrases) adressé à quelqu'un dont l'anglais est « scolaire » : lecture lente, traduction, réponse préparée (R5, validé le 22/10/2026) |

## 6. William n'est pas un dieu (symétrie)
1. **Ses manœuvres sur autrui sont tirées** (T7) ; aucune réussite automatique, même quand sa position est forte ; le « succès net » est plafonné.
2. **Les personnages indispensables pèsent en fait** : Aïcha (gérante signataire, compte, société), Mariette (compta, paie), Abdoul
   (technique), Me Kouamé (juridique). Leur départ ou leur lenteur coûte (calendrier, argent). Ils l'expriment par la lenteur, l'erreur
   « involontaire », le retard, le silence, jamais par un discours.
3. **Les coûts viennent de mécanismes**, pas d'une justice narrative : rumeur (T5), traces (`etat/traces.md`, T1b), escalade (T4), départs
   discrets (`depart_discret`), tiers à autorité propre (T6), aléas actifs.
4. **Le hasard frappe aussi William** (aléas, prix, retards, erreurs de ses propres décisions), sans lien moral avec ses actes.
5. **William reste libre** : le moteur ne bloque aucun de ses actes (§11) ; il en tire les conséquences. Ni punition « pour la morale »,
   ni effacement « pour plaire » (règle 7).

## 7. Faits cachés hérités (tirés avant ce modèle)
*(Univers 1 : historique, sans effet dans l'univers 2.)*
Les jets d'avant le 25/07/2040 (probabilités choisies à la main) restent valables pour ce qui a été **joué**. Un fait caché **non encore
révélé** et tiré hors table doit repasser par la table avant toute révélation : aujourd'hui, « Grace garde une capture du message d'excuses
hors de son téléphone de travail » (85 %, OUI) → T1b. **Résolu le 25/07/2040** (accord de l'utilisateur) : capture **aucune** (jet 8.8) ; note de l'incident dans le carnet **aucune** (jet 14.8).
