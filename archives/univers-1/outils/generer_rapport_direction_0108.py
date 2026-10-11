"""Rapport quotidien d'Aïcha (mercredi 01/08/2040, déposé à 17h42) -> serveur/direction/rapport_direction_0108.pdf

Rapport en retard (jet 85 % « à l'heure » : NON ; 17h05 + 37.3 min). Aïcha est en évitement (T1, 31/07) et a exécuté à contrecœur l'ordre
« Koné, quoi qu'il en coûte » (T7c) : elle consigne l'embauche comme décision du patron, transmise par Yves et Abdoul, et rappelle par écrit
le seuil des statuts modifiés pour le contrat de la villa et l'achat du matériel. Faits du jour tirés : entretiens (un candidat se détache),
procuration et courrier signés (T7c), pas d'autre fournisseur, accord du client de la villa (option A, acompte de 20 % accepté par William).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de direction — mercredi 1er août 2040",
              "OSIA Énergies — établi par Aïcha Diomandé, gérante — à l'attention de M. William Ossimi — 17h42")

pdf.titre1("1. Ce qui s'est passé")
pdf.puces([
    "Entretiens SAV (10h-11h30, avec M. Touré et M. Kanga) : trois candidats présents. Sur votre instruction, transmise par M. Kanga et "
    "M. Touré, offre faite à M. Ibrahim Koné à 16h40 : 380 000 FCFA brut par mois. Il répond vendredi : il doit d'abord parler à son employeur.",
    "Banque : procuration au nom de M. Kanga (double signature au-delà de 5 000 000 FCFA) et courrier pour l'envoi des relevés en copie, signés. "
    "Dépôt demain matin à la SGBCI avec M. Kanga (spécimen de signature), en même temps que le retrait de l'attestation de versement.",
    "Villa Riviera : le client accepte l'option A (15 900 000 FCFA HT), avec un acompte de 20 % que vous avez accepté. Grace prépare le contrat ; "
    "signature prévue la semaine prochaine.",
    "Matériel : Vridi annonce les batteries et onduleurs vers le 19 août ; M. Touré n'a pas trouvé d'autre fournisseur avec du stock à Abidjan. "
    "Installation de la villa possible fin août ou début septembre.",
    "Étude des offres en location : en cours (Grace), note sur le serveur vendredi.",
    "Mme Estelle : premier suivi de trésorerie ce week-end.",
])

pdf.titre1("2. Décisions prises")
pdf.puces([
    "Point d'équipe vendredi 3 août à 8h30, avec M. Kanga.",
    "Contrat de la villa : rédaction par Grace, relecture par moi, signature la semaine prochaine.",
])

pdf.titre1("3. Décisions qui vous concernent")
pdf.puces([
    "Embauche de M. Koné à 380 000 FCFA brut, au-dessus du plan (350 000) : je l'enregistre comme votre décision, transmise par M. Kanga et M. Touré.",
    "Contrat de la villa (15 900 000 FCFA HT) : au-delà de 10 000 000 FCFA. Après votre signature des statuts demain, votre autorisation écrite "
    "sera nécessaire. Je me permets de vous la demander avant votre départ.",
    "Achat du matériel de la villa (au-delà de 5 000 000 FCFA, avec un acompte du client limité à 20 %) : votre autorisation écrite et la double "
    "signature seront aussi nécessaires.",
])

pdf.titre1("4. Prochains jours")
pdf.puces([
    "Jeudi 2/08 : SGBCI à l'ouverture (attestation, procuration, spécimen de M. Kanga) ; 15h, votre signature au cabinet.",
    "Vendredi 3/08 : point d'équipe à 8h30 ; réponse de M. Koné ; note de Grace ; votre départ.",
])
pdf.para("Aïcha Diomandé", italique=True)

pdf.sauver(serveur("direction", "rapport_direction_0108.pdf"))
