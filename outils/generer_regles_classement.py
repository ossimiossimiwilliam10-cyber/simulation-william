"""Règles de classement du serveur (Mariette, 23/07/2040 au soir) -> serveur/direction/regles_classement_2307.pdf

Demandées par William le 23/07 à 11h50 (« j'ai horreur du désordre électronique »), annoncées par Mariette dans le groupe
Direction à 13h20 (« mes règles de ce soir »), déposées à 23h52. Ton : clair, structuré, sans fioriture.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Règles de classement du serveur", "OSIA Énergies — applicables à toute l'équipe dès le 24/07/2040")
pdf.meta("Date", "23/07/2040")
pdf.meta("Auteur", "Mariette Kouadio (DRH)")
pdf.meta("Destinataires", "William Ossimi, toute l'équipe")

pdf.titre1("1. Principe")
pdf.para("Tout document de l'entreprise est un PDF, déposé sur le serveur le jour même, au bon endroit, avec un nom conforme. "
         "Rien n'est gardé en local. Cette règle prolonge celles du 20/07 (« tout sur le serveur », « uniquement des PDF ») "
         "et correspond au critère « Usage du serveur et traçabilité » de la matrice d'évaluation (10 points).")

pdf.titre1("2. Arborescence officielle")
pdf.tableau(["Dossier", "Contenu", "Responsable"], [
    ["rh/", "Synthèses d'équipe, matrice d'évaluation, notes RH ; rh/contrats/ : contrats numérisés", "M. Kouadio"],
    ["commercial/", "Rapports de prospection, devis, récapitulatifs, contrats clients", "G. Adjoua-Mensah"],
    ["technique/", "Plans techniques, relevés, devis fournisseurs, chantiers", "A. Touré, Y. Kanga"],
    ["direction/", "Statuts, chartes, règles internes, synthèses générales", "A. Diomandé"],
    ["juridique/ (nouveau)", "Notes juridiques, décisions de l'associé unique, correspondance avec les avocats", "A. Diomandé, M. Kouadio"],
    ["conformite/", "Risques et conformité (à l'arrivée d'Esther N'Guessan)", "E. N'Guessan"],
], [38, 100, 36])
pdf.para("Les documents déjà déposés restent où ils sont jusqu'à nouvel ordre ; seuls les nouveaux documents juridiques vont dans juridique/.",
         italique=True)

pdf.titre1("3. Nom des fichiers")
pdf.puces([
    "Forme obligatoire : sujet_JJMM.pdf (exemple : rapport_prospects_1807.pdf).",
    "Pas d'espaces dans le nom ; les accents restent obligatoires dans le contenu du document.",
    "Nouvelle version d'un même document : sujet_JJMM_v2.pdf ; l'ancienne version est conservée.",
    "Interdits dans un nom : « final », « copie », « nouveau », « test ».",
])

pdf.titre1("4. Interdits")
pdf.puces([
    "Aucun fichier à la racine du serveur.",
    "Aucun doublon : un document, un emplacement.",
    "Aucun format autre que PDF (ni .doc, ni .md, ni tableur, ni script).",
    "Aucun document gardé uniquement en local ou dans une messagerie.",
])

pdf.titre1("5. Contrôle")
pdf.para("Chaque directeur contrôle son pôle. Je passe en revue le serveur chaque vendredi à 16h et je remets à M. Ossimi la liste des "
         "écarts constatés. Un écart répété est reporté dans la ligne « Usage du serveur et traçabilité » de l'évaluation trimestrielle.")

pdf.sauver(serveur("direction", "regles_classement_2307.pdf"))
