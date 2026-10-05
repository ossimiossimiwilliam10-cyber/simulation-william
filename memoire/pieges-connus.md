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
   anticipée seulement pour faute grave, force majeure ou accord ; un CDD ne doit pas pourvoir durablement
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
