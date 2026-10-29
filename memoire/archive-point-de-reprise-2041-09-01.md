# Archive du point de reprise (§9 des fichiers maîtres) au 01/09/2041 09:00

> Copie intégrale, mot pour mot, du §9 avant sa compression (outils/archiver_point_de_reprise.py). Ne rien supprimer ici.
> Les entrées sont classées de la plus récente à la plus ancienne ; les entrées « hors ordre » (corrections, pause du 25/07,
> levée des verrous…) sont à leur place d'origine.

**(Compression du §9, 25/08/2041)** Le journal détaillé des tours précédents est archivé tel quel dans `memoire/archive-point-de-reprise-2041-08-25.md` ; ce §9 ne garde que l'introduction et les 8 entrées les plus récentes. État courant : `python outils/resume_etat.py` (écrit `etat/resume.md`), `etat/horloge.txt`, `etat/fils-ouverts.md`, `etat/agenda.csv`. À chaque tour : ajouter l'entrée EN TÊTE de ce §9 ; au-delà de 12 entrées : `python outils/archiver_point_de_reprise.py --garder 8 --ecrire`.**
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
**Dimanche 1er septembre 2041, 09h00 — Audun-le-Tiche (Moselle), chez William : tour n° 139 joué (Semaine du 26 août en mode automatique (club, retour, société en ordre) ; séance du dimanche 1er septembre : trois décisions) ; en attente : **Séance du dimanche : trois décisions (gardiennage d'octobre, avenant des jalons, reçu du dépôt)**.**
**Lundi 26 août 2041, 05h52 (heure de Paris) — Paris, aéroport Charles-de-Gaulle, terminal 2E (arrivée du vol AF703) : tour n° 138 joué (Vol de retour, rhume, arrivée à Paris-CDG ; revue du lundi n° 6 (P42 à P44)) ; en attente : **Correspondance pour Luxembourg à 09h40 (terminal 2G) ; revue du lundi n° 6 : P42 à P44 à valider**.**
**Dimanche 25 août 2041, 17h12 (heure de Abidjan) — Abidjan, aéroport Félix-Houphouët-Boigny (hall des départs) : tour n° 137 joué (Plan rectifié lancé ; 5 000 €/mois redirigés vers la société, ETF plus alimenté ; caisse jusqu'à fin décembre sans contrat) ; en attente : **Rien ; enregistrement du vol AF703 en soirée**.**
**Dimanche 25 août 2041, 16h58 (heure de Abidjan) — Abidjan, aéroport Félix-Houphouët-Boigny (hall des départs) : tour n° 136 joué (Plan rectifié : redirection mensuelle de 6 487 € vers la société, informatique réduite sans crédit-bail ; deux décisions) ; en attente : **Plan rectifié (oui ou non) ; redirection des ordres permanents (date, montant)**.**
**Dimanche 25 août 2041, 16h25 (heure de Abidjan) — Abidjan, aéroport Félix-Houphouët-Boigny (hall des départs) : tour n° 135 joué (Chiffrage des leviers : la caisse tient jusqu'à la mi-décembre, ou la mi-février avec deux contrats ; deux décisions) ; en attente : **Lancer le plan des leviers 1-3 (oui ou non) ; garantie acceptée pour le crédit-bail**.**
**Dimanche 25 août 2041, 15h47 (heure de Abidjan) — Abidjan, aéroport Félix-Houphouët-Boigny (hall des départs) : tour n° 134 joué (Séance du dimanche : trois décisions ; l'analyse de trésorerie montre une caisse vide mi-novembre, cinq leviers proposés) ; en attente : **Choix des leviers de trésorerie ; enregistrement du vol AF703 en soirée**.**
**Dimanche 25 août 2041, 15h00 (heure de Abidjan) — Abidjan, aéroport Félix-Houphouët-Boigny (hall des départs) : tour n° 133 joué (Rapports archivés, séance de travail le dimanche ; résidence réglée, attente à l'aéroport, première séance à 15h00) ; en attente : **Séance du dimanche avec le conseiller : trois décisions (gardiennage, CIE-SODECI, Froid Lagune) ; vol AF703 22h15**.**
**Dimanche 25 août 2041, 07h18 (heure de Abidjan) — Abidjan (Cocody Deux-Plateaux), résidence hôtelière : tour n° 132 joué (Samedi calme, rapport sans décision ; dimanche matin, jour du départ) ; en attente : **Jour du départ : règlement de la résidence avant midi, vol AF703 à 22h15**.**
**Vendredi 23 août 2041, 23h40 (heure de Abidjan) — Abidjan (Cocody Deux-Plateaux), résidence hôtelière : tour n° 131 joué (William refait l'application Gestion : version 3.0, un écran simple relié aux autres applications) ; en attente : **Rien ; départ dimanche 25/08**.**
**Vendredi 23 août 2041, 20h00 (heure de Abidjan) — Abidjan (Cocody Deux-Plateaux), résidence hôtelière : tour n° 130 joué (Contrat de Viviane Tanoh signé, dépôt de garantie payé, recrutements de niveaux 3 et 4 pas avant septembre) ; en attente : **Rien ce soir ; départ dimanche 25/08**.**
**Jeudi 22 août 2041, 20h14 (heure de Abidjan) — Abidjan (Cocody Deux-Plateaux), résidence hôtelière : tour n° 129 joué (Versement de 20 000 € avancé (voie B) ; point demandé à Coulibaly sur les recrutements de niveaux 3 et 4) ; en attente : **Réponse de Coulibaly sur les niveaux 3 et 4**.**
**Jeudi 22 août 2041, 20h00 (heure de Abidjan) — Abidjan (Cocody Deux-Plateaux), résidence hôtelière : tour n° 128 joué (Veille faute lourde confiée au conseiller ; contrats déjà en main ; accord du bailleur pour les travaux ; décision sur l'acompte de Froid Lagune Services) ; en attente : **Décision sur l'acompte de Froid Lagune Services (prolongation du prix ou versement 1 avancé)**.**
**Mercredi 21 août 2041, 21h12 (heure de Abidjan) — Abidjan (Cocody Deux-Plateaux), résidence hôtelière : tour n° 127 joué (Calendrier de la première tranche validé ; le conseiller explique le champ de manœuvre pour une éventuelle révocation de Coulibaly) ; en attente : **Consultation de Me Gnamien sur la révocation de Coulibaly : oui ou non**.**
