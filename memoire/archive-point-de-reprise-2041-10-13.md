# Archive du point de reprise (§9 des fichiers maîtres) au 13/10/2041 09:00

> Copie intégrale, mot pour mot, du §9 avant sa compression (outils/archiver_point_de_reprise.py). Ne rien supprimer ici.
> Les entrées sont classées de la plus récente à la plus ancienne ; les entrées « hors ordre » (corrections, pause du 25/07,
> levée des verrous…) sont à leur place d'origine.

**(Compression du §9, 22/09/2041)** Le journal détaillé des tours précédents est archivé tel quel dans `memoire/archive-point-de-reprise-2041-09-22.md` ; ce §9 ne garde que l'introduction et les 8 entrées les plus récentes. État courant : `python outils/resume_etat.py` (écrit `etat/resume.md`), `etat/horloge.txt`, `etat/fils-ouverts.md`, `etat/agenda.csv`. À chaque tour : ajouter l'entrée EN TÊTE de ce §9 ; au-delà de 12 entrées : `python outils/archiver_point_de_reprise.py --garder 8 --ecrire`.**
**(Compression du §9, 17/07/2040)** Le journal détaillé des tours précédents est archivé tel quel dans `memoire/archive-point-de-reprise-2040-07-17.md` ; ce §9 ne garde que l'introduction et les 8 entrées les plus récentes. État courant : `python outils/resume_etat.py` (écrit `etat/resume.md`), `etat/horloge.txt`, `etat/fils-ouverts.md`, `etat/agenda.csv`. À chaque tour : ajouter l'entrée EN TÊTE de ce §9 ; au-delà de 12 entrées : `python outils/archiver_point_de_reprise.py --garder 8 --ecrire`.**
> **Règle du §9 (09/08/2040)** : une entrée par tour, EN TÊTE, juste sous cette introduction (une entrée = un paragraphe qui
> commence par « ** ») ; jamais l'état complet (il est dans `etat/resume.md` : `python outils/resume_etat.py`, `etat/horloge.txt`,
> `etat/fils-ouverts.md`, `etat/agenda.csv`) ; au-delà de 12 entrées : `python outils/archiver_point_de_reprise.py --garder 8 --ecrire`.
> **UNIVERS 2 — REDÉMARRAGE COMPLET demandé par l'utilisateur le 11/10/2026 (date réelle)** : « On reboot l'univers. On retourne à
> la toute première date mentionnée. » Choix de l'utilisateur : **univers neuf à 35 ans** (il ne reste que William, son métier et
> son argent : ni OSIA, ni équipe, ni Sandra, ni Kevin, ni Aïcha) ; **argent : le niveau initial** (celui du 17/07/2040 de
> l'univers 1 : compte courant ≈ 9 800 €, épargne « Projet » ≈ 357 000 €, ETF ≈ 288 000 €, maison avec 110 000 € de crédit) ;
> **paramètres : tous repris** (règles 1-17, tables T1-T14, monde vivant, aléas, revue du lundi, outils du §13 récupérés de la
> session du 09/10/2026, jamais enregistrée). **Départ : samedi 14 juillet 2040, 08h37**, premier vrai jour de vacances de William
> (demande de l'utilisateur du 11/10/2026 au soir ; avant : mardi 17/07/2040, 07h05, « la toute première date » : faux départ
> archivé dans `archives/univers-2-faux-depart/`), chez William à Audun-le-Tiche. Univers 1 archivé : `archives/univers-1/` (état du 09/08/2040, 14h15,
> heure de Lisbonne), tags git `univers-1-master` et `univers-1-continuation` (suite jouée dans une autre session jusqu'au
> samedi 11/08/2040, 13h27, jamais fusionnée), `archives/univers-1/session-outils/` (session des outils du 09/10/2026).
> Objectif inchangé : établir un profil précis sur environ une année simulée ; « mode entraînement » disponible sur demande.
> **UNIVERS 3 — depuis le 21/10/2026 (date réelle)** : reboot demandé par l'utilisateur après l'univers 2 (Manille), joué d'abord par Gemini
> (Antigravity), repris par Claude le 22/10/2026. William a 36 ans, enseigne les mathématiques (titularisé à 28 ans, classe U),
> départ le mardi 16/07/2041 à 08h37 (9 320 € nets par mois, patrimoine net 853 008 €, ETF 670 380 €, épargne 75 250 €, courant 10 000 €).
> (Avant le reboot du 27/10/2026 : voyage en Corée du Sud du 22/07 au 02/09/2041, décidé par le joueur dans la première partie ; au reboot, rien n'est décidé ni réservé.) L'univers 2 reste sur sa branche (tour n° 28) et dans `archives/univers-2/`.
> **UNIVERS 3 — REBOOT du 27/10/2026 (date réelle)** : « recommençons tout simplement la simulation dès le premier jour de l'univers trois »
> (choix de l'utilisateur : « reboot propre »). Retour à l'état du lancement du 16/07/2041, 08h37 (commit `848ac17`, tour n° 1 déjà montré) :
> argent, maison, entourage de départ, agenda, grand livre, météo, monde vivant. **Conservés** : règles 1-18, tables T1-T24, outils, données
> (Séoul, Brésil, téléphone, KRW), propositions R1 à R5 de la revue du 22/07 (validées par l'utilisateur le 22/10/2026, déjà installées : à ne pas
> reproposer), aléas A34 à A36, journaux d'audit (`etat/corrections.md`), pièges. **Archivés** (rien n'est supprimé) : la partie jouée des tours n° 2 à 13
> (Min-ji, Hye-won, Soo-jin, Thiago Rocha, Lucas Mendes, voyage à Séoul) dans `archives/univers-3-partie-1/` et sous le tag git
> `univers-3-partie-1` ; leurs lignes du §9 : `memoire/archive-point-de-reprise-univers-3-partie-1.md`. Tirages neufs : aucun résultat de la
> première partie n'est rejoué. Les essais du moteur utilisent l'archive comme état d'essai (`outils/tests_moteur.py`).
**Dimanche 13 octobre 2041, 09h00 — Audun-le-Tiche (Moselle), chez William : tour n° 151 joué (Notation branchée sur Gestion ; semaine du 7 octobre : retards de Coulibaly, Viviane Tanoh sous 60 ; séance du 13 : trois décisions) ; en attente : **Séance du dimanche : offre écrite à Vridi, objectifs de Viviane Tanoh, retards de Coulibaly ; programme de la semaine du 14 octobre**.**
**Dimanche 6 octobre 2041, 09h31 — Audun-le-Tiche (Moselle), chez William : tour n° 150 joué (Enveloppe validée, point écrit sur Vridi demandé ; proposition de notation continue des dirigeants) ; en attente : **Notation continue : grille, information des dirigeants, premières notes**.**
**Dimanche 6 octobre 2041, 09h00 — Audun-le-Tiche (Moselle), chez William : tour n° 149 joué (Semaine du 1er octobre : climatiseurs partiels, Viviane Tanoh manque Vridi ; séance du 6 : enveloppe et suite de Vridi) ; en attente : **Séance du dimanche : enveloppe d'approvisionnement (3,5 M FCFA), suite de Vridi ; programme de la semaine du 7 octobre**.**
**Mardi 1er octobre 2041, 17h58 — Luxembourg-Ville, parking du lycée, dans la voiture de William (visioconférence) : tour n° 148 joué (Réunion d'équipe du 1er octobre : William expose, l'équipe accepte avec réserves ; deux questions de Coulibaly) ; en attente : **Coulibaly demande : délégation du geste sur les prix ; enveloppe d'approvisionnement d'Éric Koffi Yao**.**
**Mardi 1er octobre 2041, 17h30 — Luxembourg-Ville, parking du lycée, dans la voiture de William (visioconférence) : tour n° 147 joué (Avance jusqu'à la réunion d'équipe du 1er octobre : Coulibaly donne la parole à William) ; en attente : **Réunion d'équipe : Coulibaly donne la parole à William pour ouvrir**.**
**Dimanche 29 septembre 2041, 09h00 — Audun-le-Tiche (Moselle), chez William : tour n° 146 joué (Semaine du 23 septembre : versement de 40 000 €, prospection faite, Lagune Kilowatt casse ses prix ; séance du 29 : consigne commerciale) ; en attente : **Consigne commerciale face à Lagune Kilowatt ; programme de la semaine ; réunion d'équipe mardi 01/10 17h30**.**
**Dimanche 22 septembre 2041, 09h00 — Audun-le-Tiche (Moselle), chez William : tour n° 145 joué (Semaine de rentrée en mode automatique ; rituels oubliés rattrapés ; séance du 22 : assurance et comptable) ; en attente : **Séance du dimanche : assurance et cabinet comptable ; programme de la semaine du 23/09**.**
**Dimanche 15 septembre 2041, 09h00 — Audun-le-Tiche (Moselle), chez William : tour n° 144 joué (Semaine du 9 septembre : Coulibaly accepte l'indemnité, six tâches en cours ; séance du 15 avant la rentrée) ; en attente : **Séance du dimanche : signature des actes, report des niveaux 3-4, prospection ; entraînement du dimanche ; programme de la rentrée**.**
**Dimanche 8 septembre 2041, 10h21 — Audun-le-Tiche (Moselle), chez William : tour n° 143 joué (Le conseiller expose le risque du mois non rémunéré de Coulibaly et trois options) ; en attente : **Option pour le mois non rémunéré de Coulibaly ; validation des six tâches ; programme de la semaine**.**
**Dimanche 8 septembre 2041, 09h52 — Audun-le-Tiche (Moselle), chez William : tour n° 142 joué (Devis acceptés ; rapport sur les tâches de Coulibaly : six tâches à confier, question de sa rémunération de septembre) ; en attente : **Tâches à confier à Coulibaly ; indemnité de septembre ; programme de la semaine**.**
**Dimanche 8 septembre 2041, 09h00 — Audun-le-Tiche (Moselle), chez William : tour n° 141 joué (Semaine du 2 septembre en mode automatique ; séance du 8 : devis de Me Gnamien et devis informatique) ; en attente : **Séance du dimanche : devis de Me Gnamien (295 000 FCFA TTC) ; devis informatique (3,9 M FCFA ou attendre)**.**
**Dimanche 1er septembre 2041, 09h18 — Audun-le-Tiche (Moselle), chez William : tour n° 140 joué (Séance du 1er septembre : trois décisions ; règle des réponses automatiques pendant l'avance hebdomadaire) ; en attente : **Programme de la semaine du 2 au 8 septembre ; réponse à Lenny**.**
**Dimanche 1er septembre 2041, 09h00 — Audun-le-Tiche (Moselle), chez William : tour n° 139 joué (Semaine du 26 août en mode automatique (club, retour, société en ordre) ; séance du dimanche 1er septembre : trois décisions) ; en attente : **Séance du dimanche : trois décisions (gardiennage d'octobre, avenant des jalons, reçu du dépôt)**.**
