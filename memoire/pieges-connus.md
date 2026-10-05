# Pièges connus (leçons d'audit — lire à chaque tour)

> Erreurs réellement commises dans cette simulation et à ne pas reproduire. Mis à jour à chaque relais
> (voir `etat/corrections.md` pour le détail daté).

1. **Accents dans les PDF.** William l'exige (recadrage de Mariette et de Grace, 18/07). Générer avec
   `outils/osia_pdf.py` (police Unicode) puis lancer `python outils/verifier_pdf.py`. Un PDF sans accent,
   vide ou illisible = livrable raté. Les noms propres : Aïcha Diomandé, Abdoul Touré.
2. **Brut / net.** Tous les salaires de la simulation sont des **bruts mensuels** ; les virements réels sont
   à ≈ 87 % du brut. Ne jamais écrire « net » sur un montant de `osia/equipe.md`.
3. **Le serveur ne contient que des PDF** (règle de William, 20/07). Les scripts de génération vivent dans
   `outils/`, jamais dans `serveur/`. Ne pas déguiser un .md en livrable.
4. **Événements prévus = événements à clore.** Tout ce qui est « prévu » au calendrier doit, le jour dit,
   avoir lieu, être reporté (avec raison) ou annulé, et être consigné au journal. Le 20/07, l'installation
   SécuTech a disparu sans trace ; la présentation d'Abdoul du 19/07 aussi.
5. **Calendrier et finances périmés.** Un état daté de plusieurs jours est une erreur. Mettre à jour les dates
   d'en-tête et les statuts (« avant → maintenant ») à chaque tour notable. Reporter chaque dépense dans le
   bon compte (l'achat d'onduleurs de 2 750 € n'avait jamais été déduit).
6. **Journal chronologique.** Les lignes horodatées vont dans l'ordre. Ne pas oublier les messages
   WhatsApp du jour (le 16h40 du 20/07 manquait).
7. **Fiche par personnage récurrent** dans `personnes/` (physique, caractère, lien, historique).
8. **Fils en suspens** dans `etat/fils-ouverts.md` : une promesse de personnage (« je vous envoie ça ce
   soir ») qui n'est pas tenue est un événement du monde à jouer, pas à oublier.
9. **Droit ivoirien réaliste** (vérifié le 21/07, à re-vérifier si besoin) : CDD de 24 mois maximum ; rupture
   anticipée seulement pour faute lourde, force majeure ou accord commun (art. 15.9) ; un CDD ne doit pas pourvoir durablement
   un emploi permanent (requalification en CDI) ; règlement intérieur obligatoire au-delà de 10 salariés
   (procédure : délégués du personnel → inspecteur du travail → greffe → affichage) ; congés 2,2 jours
   ouvrables par mois. Les personnages compétents (Mariette, Esther, Me Kouamé) doivent le dire, à leur façon.
10. **Droit luxembourgeois de William** : art. 14 du statut général des fonctionnaires — autorisation
    préalable du ministre pour toute activité commerciale ; risque latent, non demandé.
11. **Fuseaux** : Abidjan UTC+0, Luxembourg UTC+2 en été (Sandra travaille de nuit, dort en milieu de journée).
12. **Banque** : un ordre de virement donné le samedi est traité le jour ouvré suivant ; SGBCI Plateau ouvre
    le samedi de 8h à 13h ; fériés ivoiriens du 07/08 (fête nationale) et du 15/08 (Assomption).
13. **Ne jamais décider ni voix à la place de William** pour un choix important ; en « Go », seulement du
    routinier cohérent avec ses intentions déclarées ; s'arrêter dès qu'un vrai choix se présente.
14. **Personnages imparfaits** : Aïcha oublie (SécuTech), Mariette panique, Abdoul est rigide, Grace brûle
    les étapes. Pas de personnage parfait ni dévoué sans raison.
15. **Cotisations sociales ivoiriennes** (vérifié le 21/07) : immatriculation CNPS dans les 30 jours après le premier salarié ; déclaration d'embauche avant la prise de service ; déclaration mensuelle (DIS) et cotisations dues le 15 du mois suivant, **ITS avant le 10** du mois suivant ; majoration CNPS ≈ 10 % par mois de retard, amende de 50 000 à 500 000 FCFA pour défaut de déclaration. Cotisations ≈ 6,3 % salarié, ≈ 14-17 % employeur.
16. **Groupe « Direction »** = Aïcha, Mariette, Grace, Abdoul, Yves : tout message y est lu par les cinq. Mariette ne parle jamais de salaires dans le groupe (règle de William).
17. **William réside en France** (Audun-le-Tiche) et travaille au Luxembourg (fonctionnaire) : sa participation dans une société ivoirienne, d'éventuels dividendes et des comptes hors de France ont des obligations déclaratives en France (formulaires 2047/2042 pour les revenus étrangers, 3916 pour les comptes hors de France). Jamais abordé dans la simulation à ce jour : à faire apparaître par Esther ou un comptable, pas par le moteur en tant que conseil.
18. **Rythme de Sandra** : travail de nuit au CHEM (service vers 21h à Esch = 19h à Abidjan), repos en milieu de journée ; ses messages tombent pendant ses pauses ou en début d'après-midi.
19. **Investissement étranger en Côte d'Ivoire** (vérifié le 22/07) : toute constitution ou apport d'un non-résident est déclaré (Trésor, Finances extérieures, et BCEAO) au plus tard un mois après la première réception de fonds, avec statuts, PV, déclaration de souscription et versement ; un non-résident associé désigne un représentant résident. Compte SGBCI pour non-résident : passeport (entrée < 3 mois hors CEDEAO), photos, attestation de domicile, visite en agence.
20. **Merge Claude → Antigravity** : le dossier principal est sur la branche `master` (pas `main`) ; fusion en avance rapide (`git merge --ff-only`) depuis le dossier principal.
21. **Statut de fonctionnaire de William** (vérifié le 22/07) : art. 14 — autorisation préalable du ministre (avis conforme Fonction publique) pour toute activité commerciale ou participation à la direction d'une entreprise commerciale ; sanctions : avertissement, réprimande, amende, changement d'affectation, puis Conseil de discipline. William est déjà « en défaut » en lecture stricte (aucune demande). Ne jamais le résoudre à sa place : c'est son choix.
22. **Augmentation de capital OHADA (SARL, Côte d'Ivoire)** : décision de l'associé unique, modification des statuts, inscription modificative au RCCM, publication légale ; en plus déclaration de l'investissement étranger. Formalités à faire cadrer par Me Kouamé (pas de chiffres inventés sur les coûts).
23. **Fuseaux et créneaux** : quand William note « 16h », préciser le fuseau (Esch = Abidjan + 2 h).
24. **Revue du lundi** (règle de l'utilisateur, 22/07/2040) : chaque lundi, bilan de la semaine et nouvelles idées de réalisme (aléas, maladies…) ; ne pas oublier de la faire dès le premier tour du lundi.
25. **Hasard** : ne jamais « tirer au sort de tête » ; utiliser `python outils/tirage_aleas.py` et consigner le résultat.
26. **Virement SWIFT de gros montant** (vérifié le 22/07) : pas de plafond légal mais plafonds en ligne des banques (de l'ordre de 3 000 à 6 000 € par jour chez beaucoup de banques françaises), vigilance anti-blanchiment dès 8 000 € (justificatif d'origine des fonds possible), délai de 2 à 4 jours ouvrés. Le document qui atteste du départ (avis de virement, justificatif avec référence SWIFT/UETR) n'existe qu'après exécution ; avant, on n'a qu'une confirmation d'ordre.
27. **Néobanque ivoirienne (Djamo)** (vérifié le 22/07) : passeport accepté pour un non-CEDEAO ; niveau 1 solde max 200 000 FCFA ; niveau 2 solde 2 M FCFA et 10 M FCFA/mois ; niveau 3 (justificatif de domicile) illimité ; plafonds de virement par transaction/jour.
28. **Déclaration à l'administration luxembourgeoise** : l'autorisation de l'art. 14 est *préalable* ; une demande tardive n'est pas rétroactive. William a décidé (22/07) de se déclarer d'ici décembre en minimisant : jouer les réactions réalistes (ministre, direction du lycée, Fonction publique), sans sermon.
29. **Spuerkeess** (banque de William, vérifié le 22/07) : limite S-Net standard 15 000 € (modifiable via S-Net), commission hors SEPA 0,175 % (min 10 €, max 100 €), options de frais OUR/SHA, SWIFT 2 à 5 jours ouvrés vers l'Afrique. Ses comptes luxembourgeois sont « à l'étranger » pour le fisc français (3916).
30. **Dates** : le 30/12/2040 est un **dimanche** (échéance de la déclaration de William) ; dernier jour ouvré : vendredi 28/12. Toujours vérifier le jour de la semaine d'une échéance.
31. **CDD en droit ivoirien (Code du travail 2015, vérifié le 23/07)** : art. 15.2 écrit obligatoire ; 15.4 durée maximale 2 ans, renouvellements sans dépasser 2 ans ; 15.6 cas de recours énumérés (remplacement, surcroît occasionnel, saisonnier, secteurs spécifiques, durée d'un chantier ou projet) ; 15.8 indemnité de fin de contrat 3 % de la rémunération brute totale ; **15.9 rupture anticipée seulement pour force majeure, accord commun ou FAUTE LOURDE** (et non « faute grave », corrigé le 23/07) ; 15.10 CDD non conforme = réputé CDI.
32. **Harcèlement** : art. 5 du Code du travail ivoirien interdit le harcèlement moral et sexuel (ordre public social) ; définition : tout comportement abusif, menace, parole, intimidation, écrit, attitude ou acte répété à connotation sexuelle visant à obtenir des faveurs sexuelles. Grace est une subordonnée directe de William ; Mariette (DRH) recevrait les signalements.
33. **Diffamation par communication publique** : amende de 1 à 3 M FCFA d'après les textes consultés (Code pénal / régime de la presse), plus dommages-intérêts civils.
