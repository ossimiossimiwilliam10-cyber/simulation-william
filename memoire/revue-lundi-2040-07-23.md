# Revue du lundi — 23/07/2040 (semaine ISO 29)

## 1. Bilan de la semaine écoulée
- **Réussi** : suivi rigoureux des fichiers d'état ; livrables PDF désormais accentués et contrôlés ; fils ouverts tracés ; décisions de William toujours rejouées sans réécriture.
- **Erreurs trouvées et corrigées** : PDF sans accents, contrats en « net », barème à trou, scripts dans `serveur/`, calendrier et finances périmés, onduleurs non déduits, « faute grave » au lieu de « faute lourde » (corrigé le 23/07), plafond de virement générique (précisé Spuerkeess).
- **Interprétations du moteur à surveiller** : destinataire de la confirmation d'ordre (Aïcha) ; niveau de la néobanque ; textes reconstitués de plusieurs messages de William.
- **Stagnation / répétitions relevées** : presque tous les personnages répondent en une phrase polie (« Bien noté ») ; les démarches administratives aboutissent trop souvent ; presque aucun imprévu extérieur ne frappe le monde ; l'argent circule sans friction humaine.

## 2. Idées de réalisme proposées (à valider par William)
1. **Activer un pack d'aléas** tirés au sort chaque lundi (`etat/aleas.md`, `outils/tirage_aleas.py`) : A01 maladie d'un membre de l'équipe, A04 délestage, A06 retard fournisseur/douane, A09 erreur administrative, A13 opportunité commerciale inattendue. Probabilités indicatives à calibrer.
2. **Vie propre des personnages** : chacun a un fil privé qui avance sans William (mère d'Aïcha, fatigue de Mariette, ambition de Grace, fierté d'Abdoul, insécurité d'Yves, argent de Sandra, école de Kevin).
3. **Friction administrative systématique** : chaque démarche (banque, attestation, RCCM, CNPS, ministère) a une chance de demander un deuxième passage, des justificatifs ou un délai (déjà pratiqué le 22-23/07 : Capitol, Spuerkeess, SécuTech).
4. **Économie moins complaisante** : délais de paiement clients, concurrence (devis rivaux), variation des prix du matériel, remises exigées.
5. **Mémoire des traces** : le moteur tient un dossier des traces de William (écrits, signatures, messages, comportements) qui peuvent ressortir (rumeur, plainte, contrôle) ; applicable au statut de fonctionnaire et aux comportements envers l'équipe.

## 3. Décision de l'utilisateur
**William a validé les cinq idées (23/07)** : « Toutes tes idées, je les valide. C'est du super boulot. » Il demande que la revue ait lieu **chaque lundi**.

## 4. Application
- Pack d'aléas **A01 A04 A06 A09 A13 actif** dans `etat/aleas.md`.
- **Tirage réel** de la semaine (lundi après-midi) : consigné dans `memoire/tirages-aleas.md` ; un aléa est déclenché cette semaine (détail dans le journal des tirages ; non révélé au joueur, se jouera au jour tiré).
- Nouveaux fichiers : `etat/vies-privees.md` (vie propre des personnages), `etat/traces.md` (dossier des traces de William), `etat/economie.md` (économie et règle de friction), outil `outils/jet.py`.
- Première friction jouée : jet « Me Kouamé : deuxième passage » à 30 % → NON (rendez-vous du mercredi 25/07 15h confirmé).
