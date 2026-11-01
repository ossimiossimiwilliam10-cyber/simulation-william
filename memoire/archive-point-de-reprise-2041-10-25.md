# Archive du point de reprise (§9 des fichiers maîtres) au 25/10/2041 21:36

> Copie intégrale, mot pour mot, du §9 avant sa compression (outils/archiver_point_de_reprise.py). Ne rien supprimer ici.
> Les entrées sont classées de la plus récente à la plus ancienne ; les entrées « hors ordre » (corrections, pause du 25/07,
> levée des verrous…) sont à leur place d'origine.

**(Compression du §9, 24/10/2041)** Le journal détaillé des tours précédents est archivé tel quel dans `memoire/archive-point-de-reprise-2041-10-24.md` ; ce §9 ne garde que l'introduction et les 8 entrées les plus récentes. État courant : `python outils/resume_etat.py` (écrit `etat/resume.md`), `etat/horloge.txt`, `etat/fils-ouverts.md`, `etat/agenda.csv`. À chaque tour : ajouter l'entrée EN TÊTE de ce §9 ; au-delà de 12 entrées : `python outils/archiver_point_de_reprise.py --garder 8 --ecrire`.**
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
**Vendredi 25 octobre 2041, 21h36 — Audun-le-Tiche (Moselle), chez William : tour n° 169 joué (William soumet l'idée d'injecter l'ETF ; le conseiller distingue survie et exécution d'un contrat) ; en attente : **Conseiller : prix de revient de l'ETF ; tableau pour dimanche**.**
**Vendredi 25 octobre 2041, 21h20 — Audun-le-Tiche (Moselle), chez William : tour n° 168 joué (Huit rounds avec Lenny ; Thiago Alves invite William à dîner le 2 novembre) ; en attente : **Thiago Alves : dîner du samedi 2 novembre**.**
**Vendredi 25 octobre 2041, 18h41 — Esch-sur-Alzette, Minett Combat Club : tour n° 167 joué (Au club, Lenny réclame sa revanche : huit rounds) ; en attente : **Lenny Nguyen réclame sa revanche : huit rounds**.**
**Vendredi 25 octobre 2041, 17h14 — Audun-le-Tiche (Moselle), chez William : tour n° 166 joué (Courrier de la CPAM posté ; William se regarde dans le miroir) ; en attente : **rien d'urgent ; club ce soir**.**
**Vendredi 25 octobre 2041, 16h41 — Audun-le-Tiche (Moselle), devant chez William : tour n° 165 joué (Courrier de la CPAM : contrôle de résidence à renvoyer avant le 30 novembre) ; en attente : **rien d'urgent ; courrier CPAM à renvoyer avant le 30/11**.**
**Jeudi 24 octobre 2041, 10h04 — Luxembourg-Ville, lycée, salle des professeurs : tour n° 164 joué (William salue Kim ; elle répond poliment et garde ses distances) ; en attente : **rien d'urgent**.**
**Jeudi 24 octobre 2041, 07h51 — Luxembourg-Ville, parking du lycée : tour n° 163 joué (Coulibaly confirme l'entretien du 10 décembre) ; en attente : **rien d'urgent (accusé de Coulibaly reçu)**.**
**Mercredi 23 octobre 2041, 20h56 — Audun-le-Tiche (Moselle), chez William : tour n° 162 joué (Entretien de Mme Tanoh fixé au 10 décembre ; point clients et potentiel chiffrés par le conseiller) ; en attente : **rien d'urgent**.**
**Mercredi 23 octobre 2041, 20h49 — Audun-le-Tiche (Moselle), chez William : tour n° 161 joué (Message envoyé à Coulibaly ; il propose le 10 décembre pour l'entretien de Mme Tanoh) ; en attente : **Coulibaly : entretien de Mme Tanoh le mardi 10/12 17h30 ? la prévenir dès demain ?**.**
**Mercredi 23 octobre 2041, 20h43 — Audun-le-Tiche (Moselle), chez William : tour n° 160 joué (Séjour de décembre annulé ; le conseiller soumet un motif pour Coulibaly) ; en attente : **Conseiller : accord sur le brouillon pour Coulibaly (annulation de décembre) et sur la visio du 9/12**.**
**Mercredi 23 octobre 2041, 18h42 — Esch-sur-Alzette, Minett Combat Club : tour n° 159 joué (Avance courte jusqu'au club : Lenny propose six rounds de sparring) ; en attente : **Lenny Nguyen propose six rounds de sparring**.**
**Mardi 22 octobre 2041, 10h06 — Luxembourg-Ville, lycée, salle des professeurs : tour n° 158 joué (Kim Schmitz esquive poliment l'invitation à investir ; revue mensuelle et P60-P62 validées) ; en attente : **rien d'urgent ; compte rendu de Coulibaly à 17h00**.**
**Mardi 22 octobre 2041, 10h01 — Luxembourg-Ville, lycée, salle des professeurs : tour n° 157 joué (Reprise après annulation du tour 156 : Kim Schmitz interroge William sur son affaire en Afrique) ; en attente : **Kim Schmitz attend la réponse de William (affaire en Afrique)**.**
