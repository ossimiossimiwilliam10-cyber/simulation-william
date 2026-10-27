"""PIÈCES DU 16/07/2041 (univers 3, tour n° 4) : courriel de William au ministère (article 14), confirmation d'abonnement à l'agent IA, annonce et
règles de l'agent IA. Vrais PDF (règle 4 du fichier maître) : `documents_william/` pour ce que William rédige ou garde, `courriels/` pour ce qu'il reçoit.

    python outils/pieces_2041_07_16.py courriel-ministere | abonnement | annonce | tout

Le texte du courriel est celui que William a décidé d'envoyer (intentions de son message du tour n° 4) ; il est rédigé par le moteur d'après ces intentions,
sans y ajouter de fait de biographie (le lycée n'est pas nommé, la rémunération est celle de `etat/william.md`).
"""
import sys

from pdf_base import DocPDF, chemin

ANNONCE = [
    "Un porteur de projet européen prépare une société de droit OHADA consacrée à l'autoproduction solaire sur toitures d'entreprises à Abidjan (PME, cliniques, "
    "entrepôts, hôtels). Avant tout engagement, il cherche sur place un contact de confiance pour répondre à une question simple : le marché est-il intéressant ?",
]
ELEMENTS = [
    "Croissance du PIB de 6 à 6,7 % par an attendue en 2025-2026 ; franc CFA à parité fixe avec l'euro (1 € = 655,957 FCFA).",
    "Objectif de 45 % d'énergies renouvelables dans la production d'électricité en 2030 ; taux d'électrification d'environ 94 % en 2024.",
    "Investissement envisagé de l'ordre de 300 000 € sur trois ans, par tranches conditionnées à des résultats vérifiés.",
    "Structure prévue : société de droit OHADA, gérant local, investisseur européen associé non-gérant.",
]
PROFIL = [
    "Expérience confirmée (dix ans ou plus) dans l'énergie solaire, le bâtiment, l'industrie ou le financement de projets à Abidjan.",
    "Réseau auprès d'entreprises susceptibles d'installer du solaire sur leurs toitures.",
    "Très haut niveau de qualification (ingénieur ou équivalent) ; un doctorat est un atout s'il est pertinent pour l'énergie, l'ingénierie ou la gestion.",
    "Personne de confiance, références vérifiables, disponible pour des échanges réguliers en français.",
]


def courriel_ministere():
    pdf = DocPDF("Courriel envoyé au ministère (article 14)", "Copie gardée par William · mardi 16 juillet 2041, 12h14", auteur="William Ossimi",
                 pied="Courriel de William Ossimi — 16/07/2041")
    pdf.meta("De", "William Ossimi")
    pdf.meta("À", "info@men.lu (Ministère de l'Éducation nationale, de l'Enfance et de la Jeunesse, 33 rives de Clausen, L-2165 Luxembourg)")
    pdf.meta("Date", "mardi 16 juillet 2041, 12h14")
    pdf.meta("Objet", "Demande d'avis et d'autorisation (article 14 du statut général) : participation non exécutive à une société en Côte d'Ivoire")
    pdf.ln(3)
    pdf.para("Madame, Monsieur,")
    pdf.para("Je suis William Ossimi, professeur de mathématiques et de physique, fonctionnaire de l'État (carrière A1, grade 14), affecté à un lycée de "
             "Luxembourg-Ville. Je vous écris au sujet de l'article 14 du statut général des fonctionnaires de l'État et je souhaite savoir quelle démarche je dois suivre.")
    pdf.para("Le projet. Je prépare, avec un partenaire local à trouver, une société de droit OHADA en Côte d'Ivoire consacrée à l'installation de panneaux solaires sur "
             "les toitures d'entreprises à Abidjan. Mon rôle serait celui d'un associé non-gérant : je fournirais une partie du capital (de l'ordre de 300 000 € sur deux à "
             "trois ans, par tranches) et la gestion quotidienne serait confiée à un gérant local. Je n'exercerais ni gérance, ni mandat d'administrateur, ni fonction "
             "exécutive, et je ne percevrais aucune rémunération de la société en dehors d'éventuels dividendes.")
    pdf.para("Mes questions.")
    pdf.puces([
        "Cette participation exige-t-elle une autorisation préalable ? Si oui, à qui dois-je adresser ma demande et par quelle voie ?",
        "Où se situent exactement mes limites ? Quels actes me sont interdits (décisions de gestion, autorisation préalable sur certaines dépenses, présence dans les "
        "organes de la société) et quels droits puis-je garder (information, audit annuel, vote en assemblée) ?",
        "Ce projet est-il possible dans ces conditions ?",
    ])
    pdf.para("Ma situation professionnelle. Mon service est assuré normalement (22 leçons et 3 leçons supplémentaires par semaine). Je gère sans difficulté mes obligations "
             "d'enseignant ; le projet se mènerait pendant les vacances scolaires et en dehors des heures de cours, sans effet sur mes élèves ni sur mon établissement.")
    pdf.para("Je reste à votre disposition pour fournir tout document utile et je vous remercie de l'attention que vous porterez à ma demande.")
    pdf.para("Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.")
    pdf.para("William Ossimi\nProfesseur de mathématiques et de physique")
    pdf.sauver(chemin("documents_william", "2041-07-16_Courriel_au_MENJE_demande_d_autorisation_article_14.pdf"))


def abonnement():
    pdf = DocPDF("Confirmation d'abonnement", "Claude · agent IA · mardi 16 juillet 2041", auteur="Claude (agent IA)", pied="Claude — confirmation d'abonnement")
    pdf.meta("Client", "William Ossimi")
    pdf.meta("Formule", "Pro (agents, connecteurs d'applications et recherches approfondies ; usage plafonné par périodes)")
    pdf.meta("Engagement", "12 mois, du 16/07/2041 au 15/07/2042, prélevé chaque mois")
    pdf.meta("Référence", "AIA-001")
    pdf.titre1("Détail du premier prélèvement")
    pdf.tableau(["Poste", "Montant"], [
        ["Formule Pro, engagement de 12 mois (hors taxe)", "20,25 €"],
        ["TVA (20 %)", "4,05 €"],
        ["Total payé le 16/07/2041 à 12h33", "24,30 €"],
    ], [120, 54], taille=10)
    pdf.para("Moyen de paiement : carte Visa Debit. Prochain prélèvement : le 16 août 2041, puis le 16 de chaque mois jusqu'au 16 juin 2042 (12 prélèvements).")
    pdf.para("Après la période d'engagement, l'abonnement se poursuit au mois le mois et peut être résilié à tout moment depuis les paramètres du compte. "
             "Formule sans engagement : 29,16 € par mois. Formule Max : à partir de 145,80 € par mois.", taille=9, italique=True)
    pdf.sauver(chemin("courriels", "2041-07-16_Confirmation_d_abonnement_Claude_Pro.pdf"))


def annonce():
    pdf = DocPDF("Annonce et règles de l'agent IA", "Projet solaire en Côte d'Ivoire · brouillon du mardi 16 juillet 2041, 13h04 (non publié)", auteur="Claude (agent IA)",
                 pied="Annonce et règles de l'agent IA — brouillon")
    pdf.titre1("1. Annonce")
    pdf.para("Recherche d'un contact de confiance en Côte d'Ivoire : solaire pour entreprises (Abidjan)", taille=11)
    for p in ANNONCE:
        pdf.para(p)
    pdf.para("Éléments de contexte")
    pdf.puces(ELEMENTS, taille=9.5)
    pdf.para("Profil recherché")
    pdf.puces(PROFIL, taille=9.5)
    pdf.para("Pour répondre : un message avec votre parcours, trois références et votre lecture du marché (demande, prix, concurrence), à l'agent du porteur de projet. "
             "Aucune somme n'est demandée à qui répond ; les candidatures sont vérifiées.")

    pdf.titre1("2. Plateformes")
    pdf.tableau(["Plateforme", "État", "Détail"], [
        ["LinkedIn", "Connecté", "Profil de William trouvé ; publication d'un message public possible."],
        ["Educarriere.ci", "Connecté", "Compte recruteur ouvert sans justificatif."],
        ["NovoJob", "Connecté", "Compte recruteur ouvert sans justificatif."],
        ["Indeed", "En attente", "Compte créé ; la plateforme demande un justificatif d'entreprise avant de publier."],
        ["Emploi.ci", "Refusé", "Inscription recruteur refusée : une société immatriculée en Côte d'Ivoire est exigée."],
    ], [34, 28, 112], taille=9)

    pdf.titre1("3. Tri des réponses")
    pdf.tableau(["Niveau", "Règle", "Suite"], [
        ["A", "Dix ans d'expérience ou plus, références vérifiables, qualification élevée (doctorat apprécié), réseau d'entreprises.", "Alerte immédiate à William."],
        ["B", "Profil sérieux mais incomplet (références manquantes, expérience plus courte).", "Questions complémentaires, rapport du soir."],
        ["C", "Hors profil, ou signaux d'alerte : demande d'argent, paiement anticipé, promesse de rendement, profil créé récemment.", "Écarté, signalé dans le rapport."],
    ], [18, 110, 46], taille=9)

    pdf.titre1("4. Réponse automatique (modèle)")
    pdf.para("« Merci de votre message. Pour avancer, pouvez-vous m'indiquer : 1) votre expérience dans le solaire, le bâtiment ou le financement de projets ; "
             "2) trois références que l'on peut contacter ; 3) votre lecture du marché des entreprises à Abidjan. Je transmets votre réponse au porteur du projet. "
             "Aucune somme n'est demandée à ce stade. »", taille=9.5)
    pdf.para("Limites de l'agent : aucune promesse, aucun engagement, aucun chiffre financier au nom de William ; jamais de virement ni de document signé.", taille=9, italique=True)

    pdf.titre1("5. Compte-rendu")
    pdf.puces(["Rapport chaque jour à 18h00 : réponses reçues, niveau A, B et C, signaux d'alerte.",
               "Alerte immédiate pour tout profil de niveau A."], taille=9.5)
    pdf.para("État : en attente du feu vert de William (annonce, règles de tri, réponse automatique, rapport quotidien).", taille=9, italique=True)
    pdf.sauver(chemin("documents_william", "2041-07-16_Annonce_et_règles_de_l_agent_IA_Côte_d_Ivoire.pdf"))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd in ("courriel-ministere", "tout"):
        courriel_ministere()
    if cmd in ("abonnement", "tout"):
        abonnement()
    if cmd in ("annonce", "tout"):
        annonce()
    if cmd not in ("courriel-ministere", "abonnement", "annonce", "tout"):
        sys.exit(__doc__)
