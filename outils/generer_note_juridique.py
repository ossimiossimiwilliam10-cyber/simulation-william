"""Note juridique de Mariette (23/07/2040) -> serveur/rh/note_juridique_2307.pdf

Demandée par William le 19/07 (WhatsApp) et relancée le 21/07 ; promise « lundi avant midi ».
Références vérifiées le 23/07/2040 : Code du travail ivoirien (loi 2015-532) art. 5 et 15.2 à 15.10 ;
décret 96-197 (règlement intérieur) ; échéances CNPS/ITS ; diffamation par communication publique.
Ton : prudent, très précis, la note ne se substitue pas à un avis d'avocat.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Note juridique : chartes, contrats et conformité sociale",
              "OSIA Énergies — confidentiel — à valider par Maître Kouamé")
pdf.meta("Date", "23/07/2040")
pdf.meta("Auteur", "Mariette Kouadio (DRH)")
pdf.meta("Destinataires", "William Ossimi, Aïcha Diomandé")
pdf.meta("Références", "Code du travail (loi n° 2015-532 du 20 juillet 2015), art. 5 et 15.2 à 15.10 ; décret n° 96-197 (règlement intérieur)")

pdf.titre1("Résumé")
pdf.para("Quatre points demandent une décision rapide. (1) Nos CDD de direction risquent d'être requalifiés en CDI et "
         "ne permettent pas de licencier sur un score d'évaluation. (2) Le « naming and shaming » nous expose à des "
         "poursuites pour diffamation. (3) La charte du 19/07 n'a pas encore valeur de règlement intérieur. "
         "(4) La régularisation sociale (CNPS, impôt sur salaires) est en retard, y compris pour mon propre contrat.")

pdf.titre1("1. Les contrats à durée déterminée")
pdf.puces([
    "Art. 15.4 : durée maximale de deux ans. Nos CDD de 24 mois sont à la limite ; aucun renouvellement n'est possible "
    "au-delà (échéances : 21/05/2042, 31/05/2042, 15/07/2042).",
    "Art. 15.6 : le recours au CDD est limité à des cas énumérés (remplacement temporaire, surcroît occasionnel d'activité, "
    "emplois saisonniers, secteurs spécifiques, durée d'un chantier ou d'un projet). Des postes de direction permanents n'y "
    "figurent pas clairement. Art. 15.10 : un CDD qui ne respecte pas ces exigences est réputé à durée indéterminée. "
    "Risque : requalification en CDI.",
    "Art. 15.9 : rupture avant terme uniquement pour force majeure, accord commun ou faute lourde. Un licenciement fondé sur "
    "une mauvaise évaluation ou une « insuffisance de résultats » n'entre pas dans ces cas : il exposerait l'entreprise à des "
    "dommages-intérêts. En CDI, l'insuffisance professionnelle peut être un motif personnel, mais avec lettre motivée et procédure.",
    "Art. 15.8 : indemnité de fin de contrat de 3 % de la rémunération brute totale perçue. Elle n'est pas provisionnée "
    "(ordre de grandeur pour les six cadres sur 24 mois : environ 3,4 M FCFA, hors primes et commissions).",
    "Art. 15.2 : écrit obligatoire. Condition respectée.",
])
pdf.para("Recommandation : examiner avec Maître Kouamé la conversion des CDD de direction en CDI (période d'essai et clauses de "
         "performance rédigées avec soin) avant la première évaluation trimestrielle.", italique=True)

pdf.titre1("2. La matrice d'évaluation et le « naming and shaming »")
pdf.puces([
    "Un système de primes est tout à fait possible. Les critères chiffrés (chiffre d'affaires, délais, plaintes) sont défendables. "
    "L'ajustement discrétionnaire (bonus ou malus du Gérant, sans critère) est le point le plus fragile : il peut être présenté "
    "comme arbitraire en cas de litige. Je recommande de l'encadrer (plafond, motif écrit).",
    "La sanction maximale « licenciement pour incompétence notoire » est soumise aux limites du point 1 (impossible en CDD sauf faute lourde).",
    "Le « naming and shaming » (signalement d'un ancien salarié sur des forums ou réseaux professionnels) : la diffamation par "
    "communication publique est punie d'une amende de 1 à 3 millions de FCFA d'après les textes consultés, sans compter les "
    "dommages-intérêts civils. L'écrire dans un document interne signé aggrave la preuve de l'intention. Je recommande de le retirer de la matrice.",
])

pdf.titre1("3. Règlement intérieur")
pdf.puces([
    "Obligatoire au-delà de 10 salariés (décret n° 96-197). OSIA compte aujourd'hui 6 cadres : il n'est pas encore obligatoire, "
    "mais la charte du 19/07 ne peut pas servir de base à des sanctions tant qu'elle n'a pas suivi la procédure : présentation aux "
    "délégués du personnel, transmission à l'inspecteur du travail (observations sous un mois), dépôt au greffe, affichage.",
    "Il devra rappeler l'interdiction du harcèlement moral et sexuel (art. 5 du Code du travail), la procédure de signalement et les voies de recours.",
])

pdf.titre1("4. Qualité du signataire (gérance)")
pdf.para("Les cinq contrats numérisés sont signés « William Ossimi, Gérant ». Les statuts et le registre désignent Mme Diomandé comme "
         "gérante par procuration. À clarifier avec Maître Kouamé : validité des signatures et représentation de la société.")

pdf.titre1("5. Régularisation sociale et fiscale")
pdf.puces([
    "Les contrats de Mme Diomandé (22/05) et de moi-même (01/06) sont antérieurs au RCCM du 11/07 : actes passés pour la société "
    "en formation, à faire reprendre par la société.",
    "Les salaires de juin (payés en net par M. Ossimi, sans fiche de paie) n'ont fait l'objet ni de déclaration à la CNPS ni de "
    "retenue d'ITS. Échéances dépassées : ITS le 10/07, CNPS le 15/07. Majoration de 10 % par mois de retard à la CNPS et amende "
    "de 50 000 à 500 000 FCFA pour défaut de déclaration, selon les sources consultées (à confirmer auprès de la CNPS). Mon propre "
    "contrat est concerné.",
    "L'affiliation CNPS et la déclaration fiscale d'existence sont toujours « en cours » : à finaliser avant la paie de juillet "
    "(échéances du 10/08 pour l'ITS et du 15/08 pour la CNPS).",
    "Les salaires du 1er au 15/07 de Grace, Abdoul et Yves (période précédant leur prise de poste du 16/07) sont à qualifier "
    "(salaire ou indemnité) avant d'être déclarés.",
])

pdf.titre1("6. Plan d'action proposé")
pdf.tableau(["Action", "Responsable", "Échéance"], [
    ["Faire valider cette note par Maître Kouamé", "A. Diomandé", "25/07"],
    ["Décider du sort des CDD de direction (conversion en CDI ou maintien assumé)", "W. Ossimi", "avant le 31/07"],
    ["Retirer le « naming and shaming » ; encadrer le bonus/malus", "W. Ossimi, A. Diomandé", "avant la légalisation de la matrice"],
    ["Clarifier la gérance et la qualité des signataires", "Maître Kouamé", "31/07"],
    ["Régulariser CNPS et ITS de juin ; préparer la déclaration de la paie de juillet", "M. Kouadio, A. Diomandé", "avant le 10/08 et le 15/08"],
    ["Lancer la procédure de règlement intérieur (anticiper le seuil de 11 salariés)", "M. Kouadio", "à planifier"],
], [95, 45, 34])

pdf.para("Cette note est une analyse RH, pas un avis d'avocat : elle doit être validée par Maître Kouamé avant toute décision. "
         "Je reste disponible à tout moment pour la détailler.", italique=True)
pdf.para("Mariette Kouadio, DRH", italique=True)

pdf.sauver(serveur("rh", "note_juridique_2307.pdf"))
