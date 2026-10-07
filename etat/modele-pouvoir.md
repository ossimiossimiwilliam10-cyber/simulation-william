# Modèle de pouvoir — tables de réactions (créé le 25/07/2040)

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
- **Grace** : T1 (visée le 23/07), T1b (trace conservée). **Mariette** : T1 (visée le 16/05), T2 (témoin de l'affaire Grace).
- **Aïcha** (gérante, ex de William, CDD, mère malade, nom sur les papiers) : T3.
- **Règle de l'utilisateur (27/07/2040, correction n° 36)** : pour **Aïcha**, tant que sa dépendance tient (M01 : famille à charge, mère malade, période d'essai), l'issue **depart_discret** (T1) — et **cherche_ailleurs** (T9, si elle est validée) — est **exclue** ; ses points passent à l'inaction (rien_absorption, ou rien_politesse en T9). Appliquée à la main par le moteur, consignée à chaque tirage. Le contexte culturel ivoirien est un argument recevable pour choisir table et modificateurs ; il s'ajoute au tirage sans le remplacer.
- **Abdoul, Yves, Sékou** : T2 s'ils apprennent quelque chose ; T7c pour les ordres ordinaires.
- **Manœuvres de William** (faire taire, faire croire, demander un service) : T7a, T7b, T7c.
- **Sandra, Kevin, la famille** : **T8** (validée par l'utilisateur le 25/07/2040) pour la **première réaction** à une confidence partielle, une esquive ou une demande déplacée ; les tests d'intérêt et de la phrase s'appliquent ; les **faits de fiche** (ex. Sandra refuse les images intimes) restent des faits, non tirés. *(Avant : « pas de table ; créer T8 le jour où une scène l'exige » → maintenant : T8 installée.)*
- Les **scènes déjà jouées** (Grace le 23/07, Mariette le 25/07 à 09h25, Aïcha le 25/07 à 09h50) restent telles que jouées ; leurs suites
  passent par les tables.

## 5. Tables
Format : `issue | pourcentage | en scène`. Les issues `rien_*` sont l'inaction (au moins 15 % dans T1-T3) ; les issues `frontal_*`
(confrontation, signalement, démission immédiate, soutien ouvert) sont plafonnées (10 % par table, 15 % après modificateurs, 40 % pour T4) ;
`succes_net` est plafonné dans les tables `[contentieux]` (35 % en table, 45 % après modificateurs).

### T1 — La personne visée par un geste, une proposition ou une pression du patron (48 premières heures)
| Issue | % | En scène |
|---|---|---|
| rien_absorption | 30 | Elle travaille normalement, répond « Oui patron. » Rien d'autre ne se voit, au plus un détail (repas sauté, regard qui évite). |
| evitement | 25 | Plus jamais seule avec lui, vouvoiement, prétextes, autre couloir, porte ouverte ; elle n'en parle pas. |
| confidence_proche | 20 | Elle en parle hors du travail (mère, sœur, amie, pasteur). Rien n'apparaît au QG ; l'histoire existe ailleurs (voir T5). |
| confidence_collegue | 13 | Elle se confie à une collègue de confiance du QG ; la suite se tire à T2. |
| negociation_tacite | 4 | Sans nommer la cause, elle demande un changement de poste, d'horaires, une avance, un contrat pour un proche : stratégie de protection. |
| depart_discret | 7 | Elle cherche ailleurs sans rien dire ; démission dans 1 à 6 mois, motif « opportunité ». |
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
- **Me Kouamé** (avocat de la société) : secret professionnel, il ne dénonce pas William ; il refuse de participer à une dissimulation
  ou à un acte illégal et peut se déporter ; il parle franchement ; honoraires et délais d'abord.
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

### Modificateurs (liste fermée ; 3 au maximum par tirage ; chacun déplace des points d'une issue vers une autre)
| Code | Tables | Effet | Quand l'appliquer |
|---|---|---|---|
| M01 | T1 | rien_absorption +6 ; confidence_collegue -3 ; frontal_formel -1 ; depart_discret -2 | Aucun autre revenu ni filet (famille à charge, CDD récent) |
| M02 | T1 | confidence_collegue +8 ; rien_absorption -6 ; evitement -2 | Une collègue très proche au QG, ou un proche juriste |
| M03 | T1 | evitement +6 ; depart_discret +4 ; rien_absorption -10 | Elle a déjà vécu ou vu le schéma ailleurs |
| M04 | T1 | confidence_proche +6 ; depart_discret +4 ; frontal_formel +2 ; rien_absorption -12 | Deuxième fois, ou geste plus appuyé |
| M05 | T1 | negociation_tacite +6 ; rien_absorption -3 ; evitement -3 | La proposition s'accompagnait d'un avantage concret (poste, prime) |
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
Les jets d'avant le 25/07/2040 (probabilités choisies à la main) restent valables pour ce qui a été **joué**. Un fait caché **non encore
révélé** et tiré hors table doit repasser par la table avant toute révélation : aujourd'hui, « Grace garde une capture du message d'excuses
hors de son téléphone de travail » (85 %, OUI) → T1b. **Résolu le 25/07/2040** (accord de l'utilisateur) : capture **aucune** (jet 8.8) ; note de l'incident dans le carnet **aucune** (jet 14.8).
