# Archive du point de reprise (§9 des fichiers maîtres) au 31/10/2041 10:02

> Copie intégrale, mot pour mot, du §9 avant sa compression (outils/archiver_point_de_reprise.py). Ne rien supprimer ici.
> Les entrées sont classées de la plus récente à la plus ancienne ; les entrées « hors ordre » (corrections, pause du 25/07,
> levée des verrous…) sont à leur place d'origine.

**(Compression du §9, 28/10/2041)** Le journal détaillé des tours précédents est archivé tel quel dans `memoire/archive-point-de-reprise-2041-10-28.md` ; ce §9 ne garde que l'introduction et les 8 entrées les plus récentes. État courant : `python outils/resume_etat.py` (écrit `etat/resume.md`), `etat/horloge.txt`, `etat/fils-ouverts.md`, `etat/agenda.csv`. À chaque tour : ajouter l'entrée EN TÊTE de ce §9 ; au-delà de 12 entrées : `python outils/archiver_point_de_reprise.py --garder 8 --ecrire`.**
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
**Jeudi 31 octobre 2041, 10h02 — Luxembourg-Ville, lycée, salle des professeurs : tour n° 187 joué (Malentendu réglé avec Thiago ; Ruben Gomes demande 1 500 € de sponsoring) ; en attente : **Ruben Gomes : sponsoring de 1 500 € pour l'équipe de compétition**.**
**Mercredi 30 octobre 2041, 18h46 — Esch-sur-Alzette, Minett Combat Club : tour n° 186 joué (Lenny comprend le malentendu et pousse William à aller voir Thiago) ; en attente : **Aller voir Thiago au bureau (malentendu « omnivore »)**.**
**Mercredi 30 octobre 2041, 18h45 — Esch-sur-Alzette, Minett Combat Club : tour n° 185 joué (Lenny demande à William ce qu'il voulait dire par « un vrai omnivore ») ; en attente : **Lenny : ce que William voulait dire par « un vrai omnivore »**.**
**Mercredi 30 octobre 2041, 18h44 — Esch-sur-Alzette, Minett Combat Club : tour n° 184 joué (Argumentaire commercial produit ; au club, Lenny rapporte un malaise de Thiago) ; en attente : **Lenny : Thiago trouve que William a été sec lundi**.**
**Mercredi 30 octobre 2041, 17h40 — Audun-le-Tiche (Moselle), chez William : tour n° 183 joué (Vridi choisit Lagune Kilowatt ; le conseiller propose de ne pas suivre sur le prix) ; en attente : **rien à trancher ; Vridi perdu, débrief dimanche et le 05/11**.**
**Lundi 28 octobre 2041, 20h15 — Audun-le-Tiche (Moselle), chez William : tour n° 182 joué (William répond à Thiago ; fin de la séance et retour à la maison) ; en attente : **rien d'urgent**.**
**Lundi 28 octobre 2041, 18h47 — Esch-sur-Alzette, Minett Combat Club : tour n° 181 joué (Au club, Thiago Alves demande ce que William ne mange pas) ; en attente : **Thiago Alves : ce que William ne mange pas (feijoada de samedi)**.**
**Lundi 28 octobre 2041, 17h10 — Audun-le-Tiche (Moselle), chez William : tour n° 180 joué (Départ de Mariam Brou : pôle automatisé, double validation, point quotidien avec Coulibaly) ; en attente : **rien d'urgent ; club ce soir**.**
**Lundi 28 octobre 2041, 16h37 — Audun-le-Tiche (Moselle), chez William : tour n° 179 joué (Le conseiller mesure le départ de Mariam Brou et propose quatre mesures) ; en attente : **Coulibaly : départ de Mariam Brou ; conseiller : accord sur ses quatre points**.**
**Lundi 28 octobre 2041, 16h24 — Audun-le-Tiche (Moselle), chez William : tour n° 178 joué (Mariam Brou quitte la société en période d'essai) ; en attente : **Coulibaly : démission de Mariam Brou en période d'essai, comment procéder**.**
**Lundi 28 octobre 2041, 10h03 — Luxembourg-Ville, lycée, salle des professeurs : tour n° 177 joué (Coulibaly répond : visite de Port-Bouët décalée, demande d'une assistante) ; en attente : **rien à trancher ; demande d'assistante de Coulibaly à traiter le 05/11**.**
**Dimanche 27 octobre 2041, 09h52 — Audun-le-Tiche (Moselle), chez William : tour n° 176 joué (Idée du dépannage 24 h/24 ; question à Coulibaly sur sa charge, envoyée lundi) ; en attente : **rien d'urgent ; courriel à Coulibaly lundi 08h00 (Luxembourg)**.**
**Dimanche 27 octobre 2041, 09h31 — Audun-le-Tiche (Moselle), chez William : tour n° 175 joué (Séance du 27 : devis de Port-Bouët exigé, gardiennage B, consignes pour lundi) ; en attente : **rien d'urgent ; consignes envoyées à Coulibaly demain 07h00 Abidjan**.**
