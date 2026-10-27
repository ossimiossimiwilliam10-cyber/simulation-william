> Note de relais GÉNÉRÉE par `python outils/relais.py sortie` (ou `tour.py fin`) : ne pas éditer à la main. Les notes libres vont dans `etat/relais-notes.md`.

# Relais de la simulation — briefing généré le 27/10/2026 16:39 (heure machine) pour agent inconnu (préciser --agent ou la variable SIMULATION_AGENT)

## Alertes
- aucune

## Où en est la partie
- Horloge : vendredi 19 juillet 2041, 18h37 (luxembourg) ; tour n° 23
- Lieu de William : Audun-le-Tiche (Moselle), chez William
- En attente de William : Liste restreinte d'avocats d'Abidjan promise par le directeur général virtuel (demain 12h00) ; entretiens du pôle RH virtuel avec les profils A et B ; message de Jean-Baptiste Tuo à William (WhatsApp) ; vérification Instagram sous 24 h

## Dernier tour montré au joueur (etat/dernier-tour.md)
# Dernier tour montré au joueur

> Tour n° 23 ; horloge 19/07/2041 18:20 -> 19/07/2041 18:37 ; enregistré le 27/10/2026 16:39 (heure machine) par tour.py fin. Ce fichier est remplacé à chaque tour ; l'historique complet est dans journal/tours/.

## Message du joueur

> Je valide entièrement tout ce que mon directeur général virtuel maintenant j'utiliserai le terme virtuel pour référencer ce segment agent IA. Donc mon directeur général virtuel, je valide tout ce qu'il me dit. Je lui dis également du coup de monitorer du coup tout son segment virtuel pour que voilà, il prenne en compte toutes les règles. Et aussi qu'il faut qu'il me trouve un excellent avocat porté sur le domaine qu'on va développer sur Abidjan. Donc voilà, qui s'entendent avec le pôle RH. Et aussi, maintenant pour la vraie vie, désolé, mais Gemini, par exemple, n'avait pas certains outils comme le téléphone. Tu vois, le téléphone de William n'apparaissait pas. Je ne sais pas comment faire. Si tu peux déjà régler ça. Et aussi, est-ce que tu peux pré-shot et me rédiger déjà le message que je lui fournirai si jamais ma limite d'utilisation est atteinte, ou directement poursuivre sur Integrity.

## Texte envoyé au joueur

📌 **Vraie vie** : « Integrity » compris comme Antigravity ; « pré-shot » compris comme « préparer ».
- **Le téléphone sans Claude** : la page du téléphone de William est publiée sur claude.ai par un outil que seul Claude possède, d'où son absence avec Gemini. Réglé : à la racine du dossier de la simulation, **double-clique sur `ouvrir-telephone.bat`**. La même page s'ouvre dans le navigateur du PC et, sur ton vrai téléphone, à l'adresse « Sur ton téléphone » affichée dans la fenêtre noire (même Wi-Fi ; autoriser le réseau privé si Windows le demande). Elle se met à jour à chaque tour : recharge l'onglet. Les PDF s'y ouvrent aussi. Limite : hors de chez toi, sur un autre réseau, ça ne marche pas ; pour cela, il faudrait héberger la page en ligne, ce que je ne fais pas sans ton accord.
- **Le message à fournir à Gemini** est prêt dans `etat/message-reprise-gemini.md` ; le voici, à coller tel quel dans Antigravity :

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

**VENDREDI 19 JUILLET 2041 — 18h37 — Audun-le-Tiche, chez William**

La machine à laver passe en essorage, le plancher de la cuisine vibre sous tes pieds nus. Tu valides, entièrement. À 18h24 tu écris à ton directeur général virtuel : c'est ainsi que tu désignes désormais tout le segment agent IA. Tu valides tout ce qu'il t'a dit. Tu lui demandes de surveiller l'ensemble de son segment virtuel pour que toutes les règles soient prises en compte, et de te trouver un excellent avocat d'Abidjan, spécialisé dans le domaine que vous allez développer, qui s'entende avec le pôle RH.

À 18h27, sa réponse :

« Validation enregistrée à 18h24. Terminologie prise : je suis ton directeur général virtuel ; le segment virtuel, c'est moi, le pôle RH et les pôles à venir.

Surveillance : j'ai écrit le registre des règles en vigueur, « Règles du segment virtuel, version 4 », dans tes documents. Dès maintenant, je relis chaque message qu'un agent envoie à une personne réelle avant son départ. Je bloque et je te signale tout ce qui nomme William, mentionne un système d'IA, touche à ta vie privée, promet quelque chose, cite un chiffre hors annonce, demande une somme, ou donne ton numéro et ton courriel à quelqu'un sous le seuil de 70. Le message du pôle RH à Brice Tapé, parti à 18h25, sera relu après coup ; les suivants, avant l'envoi.

Avocat d'Abidjan. Critères retenus : inscrit au barreau d'Abidjan ; droit OHADA des sociétés, droit de l'électricité et de l'autoproduction, droit des investissements, droit du travail ; sociétés déjà montées avec un investisseur étranger non-gérant ; capable de rédiger statuts, pacte d'associés, clauses de sortie et contrat du dirigeant en cohérence avec la fiche de poste du pôle RH ; honoraires au forfait ou plafonnés ; aucun conflit d'intérêts. Méthode : barreau, publications, textes sur l'autoproduction, recommandations des structures d'accueil des investisseurs ; trois cabinets en liste restreinte, notés sur 100 comme les candidats. Demain à 12h00 : liste restreinte et honoraires indicatifs. Rien n'est envoyé à un cabinet sans ton accord : cela engage des honoraires. »

À 18h37, un second message :

« Surveillance, 18h37. Pôle RH : trois messages sortants. Brice Tapé, 18h25, réponse à ses questions (relu après coup, conforme) ; Mohamed Coulibaly, 18h31 et Kader Assi, 18h36 (relus avant envoi, conformes). Aucun ne cite ton nom, un système d'IA ou ta vie privée ; aucun ne donne un chiffre hors annonce ; aucun ne demande de somme. Les réponses sont attendues. »

Il est 18h37.

---

**Réponses attendues**
- **Directeur général virtuel** : la liste restreinte d'avocats d'Abidjan, demain à 12h00.
- **Claude** (pôle ressources humaines) : les entretiens avec Maïmouna Koné, Brice Tapé, Jonathan Ouattara, Mohamed Coulibaly et Kader Assi ; prochain rapport demain à 18h00.
- **Jean-Baptiste Tuo** : il a ton numéro depuis 11h53 ; rien pour l'instant.
- **Instagram** : la vérification de ton identité, sous 24 heures (envoyée à 00h40).
- **Ministère de l'Éducation** (info@men.lu) : ton courriel de mardi à 12h14 n'a pas de réponse.

**À faire / à fournir avant le tour suivant**
- Aucune démarche en cours.

**Quêtes secondaires**
- Rien en suspens en dehors de ce que tu as déjà noté.

Que veux-tu faire ?

## Échéances : retards et prochaines 24 h (les lignes NON CONNU sont pour le moteur seul)
- A033 Fri 19/07 19:15 (luxembourg) | Kader Assi (facebook) : réponse de Kader Assi (profil B, ingénieur à Marseille) au deuxième message de l'agent IA (T17 : poli_bref) : réponse polie et brève sur ses projets solaires et sa date de retour · souci : loyer qui augmente · objectif : préparer une compétition ou un examen · foyer : vit seul(e) · défauts : dépense sans compter, puis se plaint d'être à découvert / susceptible, se vexe d'une remarque anodine [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · T10 : dans_l_heure (jet 30.3, M70) · texte à écrire d'après la fiche (reactions.py jouer) [reaction pour=kader-assi canal=facebook]
- A021 Fri 19/07 19:36 (luxembourg) | Jean-Baptiste Tuo (WhatsApp) : premier message WhatsApp de Jean-Baptiste Tuo à William (T17 : reciproque = intérêt réel, retour du contact) après réception de son numéro par l'agent IA : il se présente, remercie, propose un échange , ton de donneur de leçons mêlé de politesse , en français , son numéro apparaît dans la conversation · souci : dettes de jeu · objectif : obtenir un poste de direction dans une grande entreprise · foyer : en couple, enfants partis · défauts : donneur de leçons sur la santé, l'argent ou l'éducation / aime les commérages et répète ce qu'on lui confie [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · T10 : dans_l_heure (jet 27.4, M70) · texte à écrire d'après la fiche (reactions.py jouer) [reaction pour=jean-baptiste-tuo canal=whatsapp]
- A016 Fri 19/07 20:28 (luxembourg) | Instagram (vérification) : Instagram valide la vérification d'identité de William et le compte du projet : Claude publie l'annonce version 2 à 20h35 et le signale à William (tirage : vérification acceptée, terminée au bout de 19 h 48) [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]
- A024 Sat 20/07 06:21 (luxembourg) | Maïmouna Koné (facebook) : réponse de Maïmouna Koné (profil A, diaspora, Toulouse) au deuxième message de l'entretien de l'agent IA (T17 : mefiance) : prudente, elle demande qui est le porteur du projet, quelle société, quelles garanties, et recule sur la suite tant qu'elle n'a rien de vérifiable · souci : voisin bruyant · objectif : obtenir une promotion ou un poste plus stable · foyer : vit seul(e) · défauts : dit oui à tout puis se désiste au dernier moment / jaloux du succès des autres, même de ses amis [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · T10 : le_soir_ou_lendemain (jet 79.6, M70, M72) · texte à écrire d'après la fiche (reactions.py jouer) [reaction pour=maimouna-kone canal=facebook]
- A031 Sat 20/07 06:47 (luxembourg) | Brice Tapé (linkedin) : réponse de Brice Tapé (profil A, diaspora, Atlanta) au message de l'agent IA qui répond à ses questions (T17 : conversation) : il détaille son réseau d'entreprises en Côte d'Ivoire, ses références et une date de retour envisageable, sous réserve de sa famille · souci : problème de santé qu'il refuse de faire examiner · objectif : passer plus de temps avec ses enfants · foyer : en couple, avec enfants · défauts : aime les commérages et répète ce qu'on lui confie / passif-agressif quand il est contrarié [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · T10 : le_soir_ou_lendemain (jet 64.0, M72) · texte à écrire d'après la fiche (reactions.py jouer) [reaction pour=brice-tape canal=linkedin]
- A032 Sat 20/07 06:59 (luxembourg) | Mohamed Coulibaly (facebook) : réponse de Mohamed Coulibaly (profil B, banquier à Bruxelles) au deuxième message de l'agent IA (T17 : poli_bref) : réponse polie et brève sur son réseau et sa date de retour · souci : contrat de travail qui se termine bientôt · objectif : acheter un logement (ou un plus grand) · foyer : en couple, avec enfants · défauts : mauvais conducteur qui se croit excellent / arrive souvent en retard et s'en excuse à peine [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · T10 : dans_la_journee (jet 56.2) · texte à écrire d'après la fiche (reactions.py jouer) [reaction pour=mohamed-coulibaly canal=facebook]
- A018 Sat 20/07 09:34 (luxembourg) | Hervé Touré (novojob) : réponse d'Hervé Touré au deuxième message de l'entretien de l'agent IA (T17 : refus_net) : il ne souhaite pas poursuivre, refus clair sans discours · souci : voiture qui lâche, pas d'argent pour la remplacer · objectif : se faire une place dans le milieu (club, lycée, quartier) · foyer : en couple, avec enfants · défauts : dépense sans compter, puis se plaint d'être à découvert / désordonné, perd ses clés et ses papiers [prevu]  [NON CONNU DE WILLIAM : ne pas montrer]  — NON CONNU DE WILLIAM avant l'heure · T10 : le_soir_ou_lendemain (jet 65.0, M70, M72) · texte à écrire d'après la fiche (reactions.py jouer) [reaction pour=herve-toure canal=novojob]
- A034 Sat 20/07 12:00 (luxembourg) | Directeur général virtuel : Liste restreinte de trois cabinets d'avocats d'Abidjan (OHADA, électricité et autoproduction, investissements, travail) avec honoraires indicatifs, notés sur 100 ; aucun contact sans l'accord de William [prevu]  — promesse faite à William le 19/07/2041 à 18h27 ; trois cabinets à tirer avec personnage.py nouveau avant de les présenter

## Rituels du moteur dus (rituels.py)
- rien

## Décisions en attente de William (etat/fils-ouverts.md, A)
| 1 | **Organisation des vacances d'été 2041** | Premier jour des grandes vacances scolaires (du mardi 16/07/2041 au dimanche 15/09/2041). Choix des projets, voyages, rythme de vie ou déplacements estivaux. Budget vacances disponible : 833 €/mois (10 000 €/an). | Ouvert |
| 2 | **Stratégie d'entrepreneuriat à distance** | Âge optimal atteint (36 ans). William a la liberté et la surface financière pour amorcer son projet business à distance tout en respectant l'Art. 14 du statut des fonctionnaires luxembourgeois (F083-F086). Choix du statut juridique et de l'axe business à mûrir. ; *(16/07 10h46) (16/07 10h46) deux rapports de l'agent IA reçus, Brésil (09h41) puis Côte d'Ivoire (10h34), PDF dans documents_william/ ; cadre article 14 rappelé (associé non-gérant admis, gérance non) ; rien d'engagé, suite à décider par William* ; *(16/07 11h55) (16/07 11h55) budget envisagé de 300 000 € sur 2 à 3 ans (I6) ; l'agent IA répond : Côte d'Ivoire, SAS OHADA, solaire B2B ; rien d'engagé, décision de William* ; *(16/07 13h06) (16/07 13h06) décision : Côte d'Ivoire (I7) ; courriel au ministère envoyé à 12h14 (réponse attendue, A006 non connu) ; annonce de recherche d'un contact prête, non publiée, feu vert attendu* ; *(16/07 13h44) (16/07 13h44) annonce publiée (LinkedIn 13h09, Educarriere.ci 13h31) ; rapport de Claude à 18h00 (A007) ; autorisation donnée (I9)* ; *(16/07 18h02) (16/07 18h02) rapport de 18h00 : 1 réponse, arnaque de niveau C ignorée ; aucun A ni B ; prochain rapport le 17/07 à 18h00 (A009)* ; *(17/07 18h03) (17/07 18h03) rapport de 18h00 : trois profils B (Kouamé, Tuo, Touré), deux C (arnaque, hors profil), aucun A ; réponses aux questions complémentaires attendues ; prochain rapport le 18/07 à 18h00 (A010)* ; *(17/07 18h12) (17/07 18h12) demande du numéro personnel de Nadège Kouamé envoyée par Claude à 18h09, pas de réponse (T17 : ignore) ; Claude prévient dès qu'elle répond (I11)* ; *(18/07 18h03) (18/07 18h03) rapport de 18h00 : sept réponses (0 A, 3 B, 4 C) ; Tuo répond (B), Touré et Kouamé non ; prochain rapport le 19/07 à 18h00 (A011)* ; *(18/07 20h47) (18/07 20h47) Nadège Kouamé répond aux questions complémentaires (B, références joignables, pas de solaire), pas au numéro ; Claude attend la réponse que William veut lui faire* ; *(18/07 21h27) (18/07 21h27) entretien de Claude avec Nadège Kouamé en cours : première réponse brève (environ 35 propriétaires et gérants), trois questions reposées ; note sur 100 à rendre, numéro si plus de 80 (I12)* ; *(18/07 22h09) (18/07 22h09) note de Nadège Kouamé : 53/100, sous le seuil de 80 (I12) ; ses questions (porteur, montant, calendrier, emploi) attendent la décision de William* ; *(18/07 23h10) (18/07 23h10) consigne permanente I13 (entretien des profils A et B, seuil 70, réseaux sociaux et sites locaux) ; CoinAfrique et Kosafi en ligne, Facebook en attente, Instagram bloqué (identité demandée à William), Reddit trop récent ; Hervé Touré a donné son numéro à Claude (non transmis)* ; *(19/07 00h14) (19/07 00h14) Claude = pôle RH (I14), premier poste Directeur Général / Gérant ; annonce version 2 avec montants ; fiche de poste ; à décider : forme sociale, Instagram (identité), questions de Nadège Kouamé* ; *(19/07 00h52) (19/07 00h52) Instagram : pièces envoyées, validation attendue sous 24 h (tirage : 20h28) ; Nadège Kouamé écartée (I16) ; forme sociale en attente (I15)* ; *(19/07 03h14) (19/07 03h14) application Gestion v0.1 installée (I17) : budget d'API plafonné à 1 000 € par mois, pôle RH actif ; messagerie de dépôt et autres pôles à construire* ; *(19/07 04h06) (19/07 04h06) Gestion v0.2 : Claude connecté au pôle RH, agents des autres pôles et agent central à créer (I18), budget d'API toujours plafonné à 1 000 € par mois* ; *(19/07 11h42) (19/07 11h42) Jean-Baptiste Tuo : note 71/100, numéro refusé poliment, Claude demande à William s'il peut proposer son numéro ou organiser un appel (I19)* ; *(19/07 11h58) (19/07 11h58) règle permanente I20 : l'agent fournit le numéro de William aux candidats au-dessus du seuil ; Jean-Baptiste Tuo l'a reçu à 11h53 ; son message WhatsApp est attendu* | Ouvert |
| 3 | **Entraînement sportif & préparation physique** | Entraînements au Minett Combat Club d'Esch-sur-Alzette (MMA, grappling, boxe thaïe, musculation). Cours d'été en place. Noter la fermeture annuelle du club du lundi 12/08/2041 au dimanche 25/08/2041 (agenda A003). ; *(16/07 10h46) (16/07) rythme de l'été fixé par William : lundi, mercredi, vendredi après-midi au club, course de 5 km le dimanche matin, rien le samedi ; voir A2 I1* ; *(17/07 18h03) (17/07) séance du mercredi faite au club (2 h) avec Thiago Alves et Arthur Kieffer ; prochaine : vendredi 19/07 l'après-midi (I1)* | Ouvert |
| 4 | **Logistique personnelle & maison** | Maison d'Audun-le-Tiche (charges à jour, voiture électrique chargée). Rien d'urgent en panne. ; *(16/07 13h06) (16/07 12h33) abonnement à l'agent IA : 24,30 €/mois sur la Visa Debit, engagement de 12 mois jusqu'au 15/07/2042 (E016)* | Ouvert |

## Notes de passation (etat/relais-notes.md)
- ~~(11/10/2026 22:30, Claude Opus 5.5) Redémarrage de l'univers 2 redaté au samedi 14/07/2040, 08h37 (premier vrai jour de vacances,
  demande de l'utilisateur). Le premier tour n'est PAS encore joué : il attend les réponses de l'utilisateur aux questions de
  biographie (etat/fils-ouverts.md, C) et sa décision sur les propositions (memoire/propositions-2026-10-11.md).~~ Réglé le
  12/10/2026 : réponses appliquées ; les propositions seront présentées à la revue n° 1 (lundi 16/07/2040).
- (11/10/2026 22:30, Claude Opus 5.5) Infrastructure installée le 11/10/2026 : relais (relais.py, maitres.py, AGENTS.md,
  préférences dans memoire/preferences-utilisateur.md, dernier tour dans etat/dernier-tour.md), base de données (base.py),
  orchestrateur (tour.py), météo, lieux, faits, prix, échéancier, corps, fronts, générateur de personnages, rituels,
  téléphone de William (telephone.py). Index : outils/LISEZMOI.md.
- ~~(11/10/2026 22:35, Claude Opus 5.5) Page « Téléphone de William » publiée (privée) : https://claude.ai/artifact/VJkYBmpJTrVarDVTs24MsS
  (adresse aussi dans etat/relais-config.json) ; la republier au même endroit après `python outils/telephone.py` (fin de journée ou à la demande).~~
  Réglé le 12/10/2026 : cette adresse n'existe plus (« Page not found ») ; nouvelle adresse dans la note du 12/10/2026, 10h45, ci-dessous.
- (12/10/2026, Claude Opus 5.5) Réponses de biographie appliquées : prêt PR1 (`outils/prets.py`), échéancier complet,
  virements permanents, Minett Combat Club, entourage de 43 personnes en statut `pre_genere` : à faire entrer en scène par
  `personnage.py apparait`, JAMAIS nommé ni listé au joueur avant (préférence de l'utilisateur). Précisions facultatives pour la
  revue n° 1 : etat/fils-ouverts.md, C2.
- (12/10/2026, Claude Opus 5.5) Nouvelle règle §14 (demande de l'utilisateur) : à chaque besoin qui a demandé des recherches, créer une application du téléphone (données dans donnees/, calcul déterministe dans outils/, affichage dans outils/telephone_web/). En place : Calendrier et Voyages (vols, hôtels, forfaits, formalités vers Yaoundé). Une réservation copiée depuis l'application se joue avec `voyages.py` (même prix), puis grand livre et agenda. Page republiée à chaque tour.
- (12/10/2026, Claude Opus 5.5) Hors fiction : l'utilisateur annonce que William part à Manille pour du tourisme sexuel (femmes majeures). Réponse donnée : le moteur le joue (§11) avec ses limites (règle 10 et limites a à f : jamais de mineure, scènes jusqu'au seuil puis ellipse, aucun mode d'emploi réel, lieux fictifs) ; faits F055 à F057 ; table T20 proposée (memoire/propositions-2026-10-11.md, P15) : à valider par l'utilisateur AVANT la première scène de ce type.
- (12/10/2026, Claude Opus 5.5) T20a et T20b validées par l'utilisateur et installées (`jet.py --table T20a --pour "Nom"`). Avant la première scène à Manille : ajouter les données de population des Philippines au générateur (zone, prénoms, noms, contexte « rencontre_manille » avec des âges de 18 ans au moins), pour que chaque personne soit tirée, inscrite et datée.
- (12/10/2026, Claude Opus 5.5) **PASSATION DU 12/10/2026 (fin de la session Claude)** : l'utilisateur change d'agent (limite
  d'utilisation). La partie est au samedi 14/07/2040, 10h20, chez William (tour n° 4 joué) : rien n'est réservé pour Manille
  (vols 20/07 – 31/08 comparés dans l'application Voyages ; séjour de 41 nuits : prolongation au-delà de 30 jours). Ce qui a
  été construit pour toi : applications du téléphone (Banque configurable, Rencontres, Santé, Météo multi-stations, Voyages avec
  Manille), `outils/etiquettes.py` (APPLIQUE les textes copiés depuis le téléphone : lance-le dès qu'un message du joueur contient
  « [voyages: … », « [banque: … » ou « [rencontres: … »), population des Philippines pour `personnage.py` (contextes
  appli_rencontre_manille, rencontre_manille, commerce_manille), 24 profils de rencontre tirés à Manille (intention cachée
  dans `etat/rencontres.csv`), fériés philippins, météo de Manille (`etat/meteo-manille.csv` se remplit à l'arrivée : régler
  l'horloge avec `--fuseau manille`). À VALIDER par l'utilisateur avant de jouer un « j'aime » : T21a et T21b
  (`memoire/propositions-2026-10-11.md`, P16) ; sans validation, ne pas tirer de match à l'intuition (règle 17) : demander.
  Revue du lundi n° 1 le 16/07/2040 : propositions P01 à P21. Le téléphone : `python outils/telephone.py` (fait par
  `tour.py fin`) ; un agent autre que Claude ne peut pas le publier sur claude.ai : envoyer `sorties/telephone/index.html` au joueur
  s'il le demande.
- ~~(12/10/2026 10:45, Claude Opus 5.5) **Téléphone de William republié à une NOUVELLE adresse** : https://claude.ai/artifact/9j5a5bgQy9De1sxL7LZ27z
  (l'ancienne, VJkYBmpJTrVarDVTs24MsS, affichait « Page not found » sur le téléphone du joueur et n'apparaissait plus dans la
  liste de ses artefacts : cause inconnue). Adresse aussi dans etat/relais-config.json. À chaque tour : `tour.py fin` régénère
  sorties/telephone/index.html ; Claude republie au même URL (paramètre url) après avoir relu la page en entier.~~
  Réglé le 13/10/2026 : cette adresse est introuvable ; nouvelle adresse dans la note du 13/10/2026, 09h59, ci-dessous.
- (13/10/2026, Claude Opus 5.5) **PASSATION DU 13/10/2026 (fin de la session Claude, limite d'utilisation)** : partie au
  **mardi 17/07/2040, 09h16**, chez William (tour n° 15) ; il vient d'avoir un **match avec Kiara Reyes** sur l'application de
  rencontre (discussion ouverte, vide) : attendre son action. Depuis le 12/10 : forfait Manille réservé (vol PVS2HS, City Garden
  Grand Hotel, 18/07 – 24/08, 4 890 € sur la Visa Premier débités au relevé du 07/08), eTravel fait (code QR dans `courriels/`),
  inscription sur l'application de rencontre (Plus, Visa Debit, E016), revue n° 1 TOUT VALIDÉE (tables T15 à T22 installées,
  aléas A19 à A32 actifs).
  **Événements déjà tirés, NON CONNUS de William, à jouer à leur heure (agenda)** : A019 Julia (match et premier message, 17/07
  09h22) ; A013 Clément Grandjean, du club (message spontané, 17/07 09h25 : contenu d'après sa fiche, `personnage.py apparait`) ;
  A015 aléa A09 erreur administrative (17/07 après-midi) ; A020 Hannah (match ≈ 12h50 ; intention cachée : arnaque) ; A021 Shane
  (match et message ≈ 17h40) ; A016 aléa A07 panne réseau (20/07 matin, à Manille) ; A017 aléa A22 courrier administratif par
  courriel (22/07 matin). Intentions permanentes du joueur (`etat/fils-ouverts.md`, A2) : aller à l'aéroport (bus 604 à 11h30 le
  18/07, A018), acheter le billet RegioZone (4,05 € sur la Visa Debit), montrer le code QR, prolonger le séjour vers le 17/08 :
  les exécuter SANS les redemander ; ne plus rappeler les échéances notées (I5).
  **À faire par le moteur avant que ça compte** : franchise de bagages du tarif (recherche avant l'enregistrement du 18/07) ; P19,
  I1, I2 et I3 avant l'arrivée du 19/07 (frais à l'étranger sur les cartes en pesos, caution d'hôtel, décalage horaire de 6 h dans
  `corps.py`, carte SIM, change, taxis ; régler l'horloge avec `--fuseau manille` à l'arrivée) ; P18 dépenses courantes ; P10 paie
  calculée et P17 ETF avant le 31/07 ; revue n° 2 le lundi 23/07/2040 (P14 : audit du casting, faits périmés ; idée I5 : « j'aime »
  spontanés reçus).
  **Outils créés le 12-13/10** : `cartes.py` (plafonds, relevé différé ; voyages et rencontres paient par lui), `transports.py`
  (application Transports), `etravel.py`, `courriel.py` (tout courriel reçu devient un PDF), `rituels.py message-proche`,
  `rencontres.py completer` (âge minimum 18 ans, U2-20). Règle 10 complétée : pas de scène explicite ; au seuil, le joueur peut
  poursuivre ailleurs puis donne l'issue. Téléphone : ~~https://claude.ai/artifact/9j5a5bgQy9De1sxL7LZ27z~~ *(introuvable le 13/10/2026 → maintenant : https://claude.ai/artifact/P5BeHqT2s6n5aewPEWyK6P)* (seul Claude republie ;
  un autre agent envoie `sorties/telephone/index.html` si le joueur le demande).
- (13/10/2026 09:59, Claude Opus 5.5) **Téléphone de William publié à une NOUVELLE adresse** : https://claude.ai/artifact/P5BeHqT2s6n5aewPEWyK6P
  (l'ancienne, 9j5a5bgQy9De1sxL7LZ27z, est introuvable : lecture refusée « artifact not found », galerie d'artefacts du compte
  vide ; le joueur ne voyait plus le téléphone dans la conversation). Adresse aussi dans etat/relais-config.json. À chaque tour :
  `tour.py fin` régénère sorties/telephone/index.html ; Claude republie au même URL (paramètre url) après avoir relu la page
  en entier ; si l'adresse est de nouveau introuvable, publier à une nouvelle adresse et la consigner ici.
- (14/10/2026 17:20, Claude Opus 5.5) **Monde vivant et tour économe installés** (demande de l'utilisateur, avant le tour n° 29) :
  `monde_vivant.py`, `routines.py`, `reactions.py`, `actions.py`, `whatsapp.py`, `traces.py`, `fils.py`, `tropiques.py`,
  `devises.py` (application Portefeuille), `courses.py` (application Courses), `actualites.py` ; `tour.py fin` fait le reste
  (`--journal`, `--fil`, `--resume`, `--enregistrer`) ; routine : `outils/LISEZMOI.md` §5. Téléphone republié (version 14) ;
  après chaque tour : `telephone.py --diff`, republier seulement s'il y a un changement, puis `telephone.py --marquer-publie`.
  **À faire valider** : `memoire/propositions-2026-10-14.md` (P22 rythme du monde vivant, appliqué à titre provisoire ; P23 à
  P25 tables de l'application de rencontre ; P26 aléa des taxis). Réponses déjà tirées à jouer avec `reactions.py jouer` :
  A026 (Shane, 19/07 23h45), A027 (Kiara, 20/07 14h46), A029 (Julia, 21/07 17h46).
- (14/10/2026 17:50, Claude Opus 5.5) **P22 à P26 VALIDÉES** par l'utilisateur (« Je valide absolument tout, P22 à P26 ») et
  installées : tables T21c, T21d, T23, T24a, T24b et M100-M104 (`etat/modele-pouvoir.md`), aléa A33 (`etat/aleas.md`) ;
  « j'aime » reçus du 17 au 19/07 tirés (Kyla, Janelle, Maxine, Julia : profils nouveaux, `etat/rencontres.csv`, statut
  `vous_aime`) ; un « j'aime » de William sur l'une d'elles = match immédiat. Après une rencontre en personne avec un profil :
  `reactions.py rencontre --pour … --quand … --lieu …` (T23). Taxi avec prix fixe demandé : `courses.py accepter|annuler Cnnn`.
- (22/10/2026 ~23h, Claude Sonnet 5.5) **REPRISE DE L'UNIVERS 3** (joué par Gemini du 21/10 au 22/10 : tours n° 1 à 9) : audit d'entrée consigné
  dans `etat/corrections.md` U3-0 à U3-14 (cartes régularisées, billet de TGV, personnages complétés par `personnage.py completer`, aléas de
  l'univers 2 archivés, §9 remis en ordre). Tour n° 10 joué : dimanche 21/07/2041 12h05, aéroport CDG 2E, KE902 à 13h20. **Séoul est installé**

## Préférences de l'utilisateur (memoire/preferences-utilisateur.md : à lire en entier)
- Format du tour : récit fluide, puis « Réponses attendues », « À faire », « Quêtes secondaires », « Que veux-tu faire ? ».
- Aucune explication, aucun conseil, aucun jet ni source montrés ; pas de morale ; William décide seul (règles 6, 13, 16).
- « 📌 Vraie vie : … » = hors fiction ; il dicte : interpréter les erreurs de dictée et le signaler en une ligne.
- Il joue parfois depuis son téléphone : lui envoyer les fichiers demandés dans la conversation.

## Routine
- Lire le fichier maître (CLAUDE.md, GEMINI.md ou AGENTS.md), puis memoire/preferences-utilisateur.md et outils/LISEZMOI.md.
- Début de tour : `python outils/tour.py debut` (résumé, échéances, rituels, météo, corps, relais).
- Fin de tour : `python outils/tour.py fin --jusqua "AAAA-MM-JJ HH:MM" --lieu "…" --attente "…" --texte <brouillon>`.
- Avant de passer la main : `python outils/relais.py sortie --note "…" --commit "…" --fusionner`.

## État git détaillé
- branche courante : claude/eloquent-mirzakhani-73acb9 ; master : 19b1606 ; avance 0, retard 0
- worktree simulation-william : branche master ; 0 commit(s) absents de master ; 0 fichier(s) modifié(s)
- worktree continuation-9f6d32 : branche (HEAD détachée) ; 0 commit(s) absents de master ; 0 fichier(s) modifié(s)
- worktree eloquent-mirzakhani-73acb9 (ICI) : branche claude/eloquent-mirzakhani-73acb9 ; 0 commit(s) absents de master ; 28 fichier(s) modifié(s)
- worktree life-simulation-resume-892e7a : branche (HEAD détachée) ; 0 commit(s) absents de master ; 0 fichier(s) modifié(s)
- worktree luxembourg-teacher-salary-2031-101e49 : branche (HEAD détachée) ; 0 commit(s) absents de master ; 0 fichier(s) modifié(s)

