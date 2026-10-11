"""Note de Grace sur la clause d'éthique commerciale (25/07/2040) -> serveur/commercial/clause_marches_2507.pdf

Promise à William le 23/07 (« une demi-page écrite d'ici mercredi : ce que je peux faire sans toucher au contrat, et ce que
je ne ferai pas »). Depuis le 23/07 midi, Grace vouvoie William et privilégie l'écrit : ton strictement professionnel.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Note sur la clause d'éthique commerciale", "Article 5 du contrat de travail de Grace Adjoua-Mensah (16/07/2040)")
pdf.meta("Date", "25/07/2040")
pdf.meta("Auteur", "Grace Adjoua-Mensah (directrice commerciale)")
pdf.meta("Destinataire", "William Ossimi")

pdf.titre1("1. Rappel")
pdf.para("L'article 5 de mon contrat exclut de ma mission les marchés publics ainsi que toute commission, rétro-commission ou "
         "avantage occulte. Je l'ai demandé moi-même à la signature et je m'y tiens.")

pdf.titre1("2. Ce que je peux faire sans toucher au contrat")
pdf.puces([
    "Assurer une veille des appels d'offres publics et la transmettre à la direction générale, à titre d'information.",
    "À la demande de la direction générale, préparer la partie technique et commerciale d'un dossier de candidature conforme à la "
    "procédure officielle, sans aucun contact avec les décideurs ; la signature, le dépôt et le suivi relèvent de la gérante, Mme Diomandé.",
    "Développer les clients privés et parapublics à contrat de gré à gré : cliniques, hôtels, écoles, entreprises, villas.",
])

pdf.titre1("3. Ce que je ne ferai pas")
pdf.puces([
    "Aucune commission, aucun « remerciement », aucun avantage, sous quelque forme que ce soit.",
    "Aucune participation personnelle à un marché public ni aucune démarche auprès d'un agent public en lien avec un marché.",
])

pdf.titre1("4. Modification de ma mission")
pdf.para("Toute modification de ma mission suppose un avenant écrit, signé par les deux parties. Je ne donne aucun accord oral sur ce sujet.")

pdf.para("Je reste à votre disposition par écrit.", italique=True)

pdf.sauver(serveur("commercial", "clause_marches_2507.pdf"))
