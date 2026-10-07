"""Premier contrôle du serveur par Mariette (vendredi 27/07/2040, 16h) -> serveur/direction/controle_serveur_2707.pdf

Prévu par ses règles de classement du 23/07 (validées par William le 26/07 à 13h21) : « Je passe en revue le serveur chaque vendredi à 16h
et je vous remets la liste des écarts. » État réel du serveur à 16h00 relevé par le moteur ; Mariette nomme les responsables sans juger
(précautions, vouvoiement) ; elle déplace elle-même sa note juridique de rh/ vers juridique/ (16h35). Remis à William et à Aïcha à 16h42.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Contrôle du serveur — vendredi 27 juillet 2040",
              "OSIA Énergies — Mariette Kouadio (DRH) — destinataires : M. William Ossimi, Mme Aïcha Diomandé")
pdf.meta("Référence", "Règles de classement du 23/07/2040 (direction/regles_classement_2307.pdf), validées le 26/07")
pdf.meta("Périmètre", "commercial/, direction/, juridique/, rh/, technique/ — état à 16h00")

pdf.titre1("1. Documents conformes")
pdf.puces([
    "commercial/ : rapport des prospects, récap de Grace, note sur la clause, devis de la villa Riviera, devis de la clinique.",
    "direction/ : charte du 19/07, règles de classement, rapport de direction du 26/07.",
    "juridique/ : renonciation de M. Ossimi au remboursement de ses avances (déposée le 27/07 à 13h05).",
    "rh/ : synthèse des équipes, contrats ; évaluation de Mme Diomandé en accès restreint dans rh/evaluations/ (déposée d'abord dans direction/ à 14h28, déplacée à 14h59).",
    "technique/ : plan technique d'Abdoul.",
])

pdf.titre1("2. Écarts")
pdf.tableau(["Document", "Écart", "Responsable"], [
    ["Décision de l'associé unique du 26/07 (augmentation de capital)", "Absente de juridique/ ; un original est chez M. Ossimi, l'autre au cabinet", "Direction générale"],
    ["Convention d'honoraires de l'augmentation (signée le 27/07)", "À déposer dans juridique/", "Mme Diomandé"],
    ["Comptes rendus de Maître Kouamé (23/07) et chiffrage (24/07)", "Transmis par WhatsApp, absents du serveur", "Mme Diomandé"],
    ["Devis SécuTech (17/07) et procès-verbal de réception (26/07)", "Absents de direction/", "Mme Diomandé"],
    ["Facture pro forma du fournisseur de Vridi (18/07)", "Absente de technique/", "Abdoul"],
    ["Statuts, matrice d'évaluation, contrats", "Noms sans date (déposés avant les règles) : à renommer à la prochaine version", "Mariette"],
], (62, 78, 30))

pdf.titre1("3. Correction faite pendant le contrôle")
pdf.para("Ma note juridique du 23/07, déposée dans rh/ avant la création de juridique/, a été déplacée dans juridique/ à 16h35.")

pdf.para("Excusez-moi pour la longueur. Je reste disponible pour toute précision.", italique=True)
pdf.para("Mariette Kouadio, DRH", italique=True)

pdf.sauver(serveur("direction", "controle_serveur_2707.pdf"))
