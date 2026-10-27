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


def regles_v2():
    """Règles de l'agent IA, version du 18/07/2041 (consigne permanente de William, 22h15 : entretien des profils A et B, seuil de contact, réseaux sociaux)."""
    pdf = DocPDF("Règles de l'agent IA : version du 18 juillet 2041", "Projet solaire en Côte d'Ivoire · remplace le brouillon du 16 juillet", auteur="Claude (agent IA)",
                 pied="Règles de l'agent IA — version 2")
    pdf.titre1("1. Tri et entretien")
    pdf.puces([
        "Le tri A, B, C ne change pas (dix ans d'expérience, références vérifiables, métier pertinent, absence de signal d'alerte).",
        "Pour chaque profil A ou B : étude de son parcours public, puis entretien sur ce qu'il peut apporter au projet, puis note sur 100.",
        "Cinq critères : réseau utile en clients potentiels (30 points), pertinence pour le solaire (25), accès réel aux décideurs et introductions déjà faites (20), "
        "fiabilité (15), disponibilité et motivation (10).",
        "Seuil de contact : 70 sur 100. De 60 à 69, second entretien. Sous 60, dossier gardé. Au-dessus du seuil, l'agent obtient le numéro de la personne et le transmet à William.",
        "Une question qui touche au projet (montant, calendrier, rôle) ou à l'identité de William est posée à William avant toute réponse.",
    ], taille=9.5)
    pdf.titre1("2. Plateformes")
    pdf.tableau(["Plateforme", "État au 18/07/2041, 23h08", "Détail"], [
        ["LinkedIn", "En ligne", "Publication depuis le profil de William."],
        ["Educarriere.ci", "En ligne", ""],
        ["NovoJob", "En ligne", ""],
        ["CoinAfrique", "En ligne", "Annonce validée à 22h58 (compte annonceur du projet)."],
        ["Kosafi Annonce CI", "En ligne", "Annonce validée à 22h51 (compte annonceur du projet)."],
        ["Facebook", "En attente", "Compte du projet créé ; publication envoyée dans des groupes d'entrepreneurs, d'ingénieurs et d'immobilier d'Abidjan, en attente de l'approbation des administrateurs."],
        ["Instagram", "Bloqué", "Compte bloqué à la création : pièce d'identité et vidéo-selfie demandées. Décision de William."],
        ["Reddit", "En attente", "Compte du projet créé, trop récent pour publier dans les communautés ivoiriennes ; nouvel essai dans quelques jours."],
        ["Indeed", "En attente", "Justificatif d'entreprise demandé."],
        ["Emploi.ci", "Refusé", "Société immatriculée en Côte d'Ivoire exigée."],
    ], [32, 34, 108], taille=9)
    pdf.titre1("3. Limites de l'agent")
    pdf.puces([
        "Autorisation permanente de William (18/07/2041) : publier sur les réseaux sociaux et les sites locaux, sous un compte du projet, sans le nom de William.",
        "Aucune promesse, aucun engagement, aucun paiement, aucun document signé ; jamais de frais d'avance.",
        "Le nom et le numéro de William ne sont donnés qu'avec sa décision.",
    ], taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-18_Règles_de_l_agent_IA_version_2.pdf"))



def regles_v3():
    """Règles de l'agent IA, version du 19/07/2041 (11h45 : au-dessus du seuil, l'agent fournit le numéro de William au candidat)."""
    pdf = DocPDF("Règles de l'agent IA : version du 19 juillet 2041", "Projet solaire en Côte d'Ivoire · remplace la version du 18 juillet", auteur="Claude (agent IA)",
                 pied="Règles de l'agent IA — version 3")
    pdf.titre1("1. Tri et entretien")
    pdf.puces([
        "Le tri A, B, C ne change pas (dix ans d'expérience, références vérifiables, métier pertinent, absence de signal d'alerte).",
        "Pour chaque profil A ou B : étude de son parcours public, puis entretien sur ce qu'il peut apporter au projet, puis note sur 100.",
        "Cinq critères : réseau utile en clients potentiels (30 points), pertinence pour le solaire (25), accès réel aux décideurs et introductions déjà faites (20), "
        "fiabilité (15), disponibilité et motivation (10).",
        "Seuil de contact : 70 sur 100. De 60 à 69, second entretien. Sous 60, dossier gardé. Au-dessus du seuil, l'agent fournit le numéro de William à la personne et l'invite à le contacter directement pour la suite des échanges ; il ne demande plus son numéro à elle (décision de William, 19/07/2041, 11h45).",
        "Une question qui touche au projet (montant, calendrier, rôle) ou à l'identité de William est posée à William avant toute réponse.",
    ], taille=9.5)
    pdf.titre1("2. Plateformes")
    pdf.tableau(["Plateforme", "État au 19/07/2041, 11h58", "Détail"], [
        ["LinkedIn", "En ligne", "Publication depuis le profil de William."],
        ["Educarriere.ci", "En ligne", ""],
        ["NovoJob", "En ligne", ""],
        ["CoinAfrique", "En ligne", "Annonce validée à 22h58 (compte annonceur du projet)."],
        ["Kosafi Annonce CI", "En ligne", "Annonce validée à 22h51 (compte annonceur du projet)."],
        ["Facebook", "En attente", "Compte du projet créé ; publication envoyée dans des groupes d'entrepreneurs, d'ingénieurs et d'immobilier d'Abidjan, en attente de l'approbation des administrateurs."],
        ["Instagram", "Bloqué", "Compte bloqué à la création : pièce d'identité et vidéo-selfie demandées. Décision de William."],
        ["Reddit", "En attente", "Compte du projet créé, trop récent pour publier dans les communautés ivoiriennes ; nouvel essai dans quelques jours."],
        ["Indeed", "En attente", "Justificatif d'entreprise demandé."],
        ["Emploi.ci", "Refusé", "Société immatriculée en Côte d'Ivoire exigée."],
    ], [32, 34, 108], taille=9)
    pdf.titre1("3. Limites de l'agent")
    pdf.puces([
        "Autorisation permanente de William (18/07/2041) : publier sur les réseaux sociaux et les sites locaux, sous un compte du projet, sans le nom de William.",
        "Aucune promesse, aucun engagement, aucun paiement, aucun document signé ; jamais de frais d'avance.",
        "Le numéro de William n'est donné qu'au-dessus du seuil ; son nom ne l'est qu'avec sa décision.",
    ], taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-19_Règles_de_l_agent_IA_version_3.pdf"))


def regles_v4():
    """Registre des règles du segment virtuel, version du 19/07/2041 (18h27) : le directeur général virtuel surveille le segment virtuel."""
    pdf = DocPDF("Règles du segment virtuel : version du 19 juillet 2041", "Directeur général virtuel (agent central) · remplace « Règles de l'agent IA, version 3 »", auteur="Claude (agent central)",
                 pied="Règles du segment virtuel — version 4")
    pdf.titre1("1. Rôles")
    pdf.puces([
        "Le directeur général virtuel (agent central de l'application Gestion) examine les réponses de tous les pôles avant qu'elles parviennent à William ; William se tourne vers lui avant toute décision, et la décision reste celle de William.",
        "Le pôle RH virtuel (Claude) recrute : annonces, tri A, B, C, entretiens, notes sur 100. Les pôles juridique, finance, technique et commercial viennent après la signature du directeur général réel.",
        "Le segment virtuel apporte l'analyse, les chiffres et la vérification contre les textes ; l'aspect humain, le terrain et l'autorité sur des salariés appartiennent à l'équipe réelle.",
    ], taille=9.5)
    pdf.titre1("2. Confidentialité (consigne de William, 19/07/2041, 18h12)")
    pdf.puces([
        "Aucune personne réelle n'est informée du système d'IA de William ni de ce qu'il a mis en place avec les IA.",
        "Aucun élément de la vie privée de William n'est mis en avant, jamais.",
        "Si une personne s'étonne de son niveau d'expertise : « un homme cultivé qui prend son projet au sérieux » ; rien de plus.",
        "Le nom de William n'est communiqué qu'avec sa décision.",
    ], taille=9.5)
    pdf.titre1("3. Contact avec les candidats")
    pdf.puces([
        "Seuil de contact : 70 sur 100 (de 60 à 69, second entretien ; sous 60, dossier gardé).",
        "Au-dessus du seuil : le numéro de téléphone ET le courriel de William sont fournis au candidat, qui est invité à le contacter directement. Le courriel de William est connecté à l'agent central.",
        "Un candidat peut remonter jusqu'à William grâce à ces deux éléments : c'est connu et accepté par William.",
    ], taille=9.5)
    pdf.titre1("4. Surveillance du segment virtuel")
    pdf.puces([
        "Chaque message sortant d'un agent vers une personne réelle est relu par le directeur général virtuel avant l'envoi (les accusés de réception automatiques exceptés).",
        "Contrôle : pas de nom de William, pas de mention d'un système d'IA, pas de vie privée, pas de promesse, pas de chiffre hors annonce, pas de somme demandée, numéro et courriel seulement au-dessus du seuil.",
        "Un écart est bloqué et signalé à William. Un rapport de surveillance est écrit à chaque série de messages.",
    ], taille=9.5)
    pdf.titre1("5. Limites")
    pdf.puces([
        "Aucun agent ne signe, ne paie, ne promet ; jamais de frais d'avance demandés à un candidat.",
        "Budget d'API de l'application Gestion : 1 000 € par mois au plus.",
        "Aucun contact avec un avocat, un comptable ou une administration n'est lancé sans l'accord de William (des honoraires peuvent en découler).",
    ], taille=9.5)
    pdf.titre1("6. Avocat d'Abidjan : critères de sélection")
    pdf.puces([
        "Inscrit au barreau d'Abidjan ; droit OHADA des sociétés ; droit de l'électricité et de l'autoproduction (autorité de régulation) ; droit des investissements ; droit du travail.",
        "Expérience de sociétés montées avec un investisseur étranger associé non-gérant ; capacité à rédiger statuts, pacte d'associés, clauses de sortie et contrat du dirigeant en cohérence avec la fiche de poste du pôle RH.",
        "Honoraires au forfait ou plafonnés ; absence de conflit d'intérêts ; notation sur 100 comme pour les candidats ; trois cabinets en liste restreinte.",
    ], taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-19_Règles_du_segment_virtuel_version_4.pdf"))


def regles_v5():
    """Registre des règles du segment virtuel, version du 19/07/2041 (18h46) : le directeur général virtuel gère tous les pôles ; un seul rapport final par jour, à 20h00."""
    pdf = DocPDF("Règles du segment virtuel : version du 19 juillet 2041 (18h46)", "Directeur général virtuel · remplace la version 4 de 18h27", auteur="Claude (directeur général virtuel)",
                 pied="Règles du segment virtuel — version 5")
    pdf.titre1("1. Rôles")
    pdf.puces([
        "Le directeur général virtuel gère TOUS les pôles (RH, juridique, finance, technique, commercial) au fur et à mesure de leur ouverture ; William se tourne vers lui avant toute décision, et la décision reste celle de William.",
        "Le pôle RH virtuel recrute : annonces, tri A, B, C, entretiens, notes sur 100. Les autres pôles s'ouvrent après la signature du directeur général réel.",
        "Le segment virtuel apporte l'analyse, les chiffres et la vérification contre les textes ; le terrain, l'aspect humain et l'autorité sur des salariés appartiennent à l'équipe réelle.",
    ], taille=9.5)
    pdf.titre1("2. Rapport à William")
    pdf.puces([
        "William ne reçoit qu'UN rapport final par jour, à 20h00 (le premier : le 19/07/2041). Il remplace le rapport de 18h00 du pôle RH et les alertes immédiates de niveau A.",
        "Contenu : les décisions que William seul peut prendre, chacune ramenée à une question fermée avec l'analyse en deux lignes ; puis l'état des pôles en dix lignes au plus. Sans décision à prendre, le rapport le dit.",
        "Exceptions à l'attente de 20h00 : un candidat qui fixe un délai de réponse court, un document à signer, un paiement demandé.",
        "Circuit : chaque agent adresse son rapport au directeur général virtuel ; les agents actifs relisent le rapport final avant l'envoi et leurs réserves sont jointes. Même circuit pour l'équipe réelle : ses rapports passent par le directeur général virtuel.",
        "Limite du circuit : ce qui arrive directement sur le numéro de téléphone de William ne passe pas par le directeur général virtuel ; son courriel lui est connecté.",
    ], taille=9.5)
    pdf.titre1("3. Confidentialité (consigne de William, 19/07/2041, 18h12)")
    pdf.puces([
        "Aucune personne réelle n'est informée du système d'IA de William. Aucun élément de sa vie privée n'est mis en avant, jamais.",
        "Si une personne s'étonne de son niveau d'expertise : « un homme cultivé qui prend son projet au sérieux » ; rien de plus.",
        "Le nom de William n'est communiqué qu'avec sa décision.",
    ], taille=9.5)
    pdf.titre1("4. Contact avec les candidats et surveillance")
    pdf.puces([
        "Seuil de contact : 70 sur 100. Au-dessus du seuil : le numéro de téléphone ET le courriel de William sont fournis au candidat, invité à le contacter directement.",
        "Chaque message sortant d'un agent vers une personne réelle est relu par le directeur général virtuel avant l'envoi ; un écart est bloqué et signalé dans le rapport.",
        "Contrôle : pas de nom de William, pas de mention d'un système d'IA, pas de vie privée, pas de promesse, pas de chiffre hors annonce, pas de somme demandée.",
    ], taille=9.5)
    pdf.titre1("5. Limites")
    pdf.puces([
        "Aucun agent ne signe, ne paie, ne promet ; jamais de frais d'avance demandés à un candidat.",
        "Budget d'API de l'application Gestion : 1 000 € par mois au plus.",
        "Aucun contact avec un avocat, un comptable ou une administration sans l'accord de William (des honoraires peuvent en découler).",
    ], taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-19_Règles_du_segment_virtuel_version_5.pdf"))


def regles_v6():
    """Registre des règles du segment virtuel, version du 19/07/2041 (18h55) : le numéro de téléphone de William n'est plus fourni à personne ; seul le courriel professionnel du projet sert."""
    pdf = DocPDF("Règles du segment virtuel : version du 19 juillet 2041 (18h55)", "Directeur général virtuel · remplace la version 5 de 18h46", auteur="Claude (directeur général virtuel)",
                 pied="Règles du segment virtuel — version 6")
    pdf.titre1("1. Rôles")
    pdf.puces([
        "Le directeur général virtuel gère TOUS les pôles (RH, juridique, finance, technique, commercial) au fur et à mesure de leur ouverture ; William se tourne vers lui avant toute décision, et la décision reste celle de William.",
        "Le pôle RH virtuel recrute : annonces, tri A, B, C, entretiens, notes sur 100. Les autres pôles s'ouvrent après la signature du directeur général réel.",
        "Le segment virtuel apporte l'analyse, les chiffres et la vérification contre les textes ; le terrain, l'aspect humain et l'autorité sur des salariés appartiennent à l'équipe réelle.",
    ], taille=9.5)
    pdf.titre1("2. Rapport à William")
    pdf.puces([
        "William ne reçoit qu'UN rapport final par jour, à 20h00 (le premier : le 19/07/2041). Il remplace le rapport de 18h00 du pôle RH et les alertes immédiates de niveau A.",
        "Contenu : les décisions que William seul peut prendre, chacune ramenée à une question fermée avec l'analyse en deux lignes ; puis l'état des pôles en dix lignes au plus. Sans décision à prendre, le rapport le dit.",
        "Exceptions à l'attente de 20h00 : un candidat qui fixe un délai de réponse court, un document à signer, un paiement demandé.",
        "Circuit : chaque agent adresse son rapport au directeur général virtuel ; les agents actifs relisent le rapport final avant l'envoi et leurs réserves sont jointes. Même circuit pour l'équipe réelle : ses rapports passent par le directeur général virtuel.",
        "Le numéro de téléphone de William n'est plus fourni à personne (décision du 19/07/2041, 18h50). Le seul canal est le courriel professionnel du projet, connecté au directeur général virtuel, qui converse avec les candidats par ce courriel, analyse et prépare la décision que William prend (elle arrive dans le rapport de 20h00).",
    ], taille=9.5)
    pdf.titre1("3. Confidentialité (consigne de William, 19/07/2041, 18h12)")
    pdf.puces([
        "Aucune personne réelle n'est informée du système d'IA de William. Aucun élément de sa vie privée n'est mis en avant, jamais.",
        "Si une personne s'étonne de son niveau d'expertise : « un homme cultivé qui prend son projet au sérieux » ; rien de plus.",
        "Le nom de William n'est communiqué qu'avec sa décision.",
    ], taille=9.5)
    pdf.titre1("4. Contact avec les candidats et surveillance")
    pdf.puces([
        "Seuil de contact : 70 sur 100. Au-dessus du seuil : seul le courriel professionnel du projet est fourni au candidat ; le numéro de téléphone de William n'est jamais fourni. Un numéro déjà transmis (Jean-Baptiste Tuo, 19/07/2041, 11h53) ne se reprend pas.",
        "Chaque message sortant d'un agent vers une personne réelle est relu par le directeur général virtuel avant l'envoi ; un écart est bloqué et signalé dans le rapport.",
        "Contrôle : pas de nom de William, pas de mention d'un système d'IA, pas de vie privée, pas de promesse, pas de chiffre hors annonce, pas de somme demandée.",
    ], taille=9.5)
    pdf.titre1("5. Limites")
    pdf.puces([
        "Aucun agent ne signe, ne paie, ne promet ; jamais de frais d'avance demandés à un candidat.",
        "Budget d'API de l'application Gestion : 1 000 € par mois au plus.",
        "Aucun contact avec un avocat, un comptable ou une administration sans l'accord de William (des honoraires peuvent en découler).",
    ], taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-19_Règles_du_segment_virtuel_version_6.pdf"))


def regles_v7():
    """Registre des règles du segment virtuel, version du 19/07/2041 (19h56) : doubles virtuels (décision, puis évaluation et contre-expertise) et messages humains aux personnes réelles."""
    pdf = DocPDF("Règles du segment virtuel : version du 19 juillet 2041 (19h56)", "Directeur général virtuel · remplace la version 6 de 18h55", auteur="Claude (directeur général virtuel)",
                 pied="Règles du segment virtuel — version 7")
    pdf.titre1("1. Rôles")
    pdf.puces([
        "Le directeur général virtuel gère TOUS les pôles (RH, juridique, finance, technique, commercial) au fur et à mesure de leur ouverture ; William se tourne vers lui avant toute décision, et la décision reste celle de William.",
        "Le pôle RH virtuel recrute : annonces, tri A, B, C, entretiens, notes sur 100. Les autres pôles s'ouvrent après la signature du directeur général réel.",
        "Le segment virtuel apporte l'analyse, les chiffres et la vérification contre les textes ; le terrain, l'aspect humain et l'autorité sur des salariés appartiennent à l'équipe réelle.",
    ], taille=9.5)
    pdf.titre1("2. Rapport à William")
    pdf.puces([
        "William ne reçoit qu'UN rapport final par jour, à 20h00 (le premier : le 19/07/2041). Il remplace le rapport de 18h00 du pôle RH et les alertes immédiates de niveau A.",
        "Contenu : les décisions que William seul peut prendre, chacune ramenée à une question fermée avec l'analyse en deux lignes ; puis l'état des pôles en dix lignes au plus. Sans décision à prendre, le rapport le dit.",
        "Exceptions à l'attente de 20h00 : un candidat qui fixe un délai de réponse court, un document à signer, un paiement demandé.",
        "Circuit : chaque agent adresse son rapport au directeur général virtuel ; les agents actifs relisent le rapport final avant l'envoi et leurs réserves sont jointes. Même circuit pour l'équipe réelle : ses rapports passent par le directeur général virtuel.",
        "Le numéro de téléphone de William n'est plus fourni à personne (décision du 19/07/2041, 18h50). Le seul canal est le courriel professionnel du projet, connecté au directeur général virtuel, qui converse avec les candidats par ce courriel, analyse et prépare la décision que William prend (elle arrive dans le rapport de 20h00).",
    ], taille=9.5)
    pdf.titre1("3. Confidentialité (consigne de William, 19/07/2041, 18h12)")
    pdf.puces([
        "Aucune personne réelle n'est informée du système d'IA de William. Aucun élément de sa vie privée n'est mis en avant, jamais.",
        "Si une personne s'étonne de son niveau d'expertise : « un homme cultivé qui prend son projet au sérieux » ; rien de plus.",
        "Le nom de William n'est communiqué qu'avec sa décision.",
    ], taille=9.5)
    pdf.titre1("4. Contact avec les candidats et surveillance")
    pdf.puces([
        "Seuil de contact : 70 sur 100. Au-dessus du seuil : seul le courriel professionnel du projet est fourni au candidat ; le numéro de téléphone de William n'est jamais fourni. Un numéro déjà transmis (Jean-Baptiste Tuo, 19/07/2041, 11h53) ne se reprend pas.",
        "Chaque message sortant d'un agent vers une personne réelle est relu par le directeur général virtuel avant l'envoi ; un écart est bloqué et signalé dans le rapport.",
        "Contrôle : pas de nom de William, pas de mention d'un système d'IA, pas de vie privée, pas de promesse, pas de chiffre hors annonce, pas de somme demandée.",
    ], taille=9.5)
    pdf.titre1("5. Limites")
    pdf.puces([
        "Aucun agent ne signe, ne paie, ne promet ; jamais de frais d'avance demandés à un candidat.",
        "Budget d'API de l'application Gestion : 1 000 € par mois au plus.",
        "Aucun contact avec un avocat, un comptable ou une administration sans l'accord de William (des honoraires peuvent en découler).",
    ], taille=9.5)
    pdf.titre1("6. Doubles virtuels et pouvoirs (règle de William, 19/07/2041, 19h47)")
    pdf.puces([
        "Chaque pôle virtuel est le double du directeur du même pôle dans la vraie vie ; le directeur général virtuel est le double du directeur général réel.",
        "Tant que le poste réel est vacant, le pôle virtuel DÉCIDE dans son périmètre (exemple : le pôle RH virtuel crée les offres d'emploi et les gère).",
        "Dès qu'un responsable réel occupe le poste, le pôle virtuel ne décide plus : il ÉVALUE et CONTRE-EXPERTISE.",
        "Les rapports des responsables réels atterrissent dans le pôle virtuel correspondant, qui les évalue ; le directeur général virtuel consolide dans le rapport final de 20h00.",
        "Rapport du directeur général réel (proposition) : résultats contre jalons, trésorerie et engagements, risques et décisions demandées, appréciation courte de chaque membre de l'équipe, recoupée par le pôle RH virtuel. Il arrive en parallèle des rapports des pôles, pas à travers eux.",
    ], taille=9.5)
    pdf.titre1("7. Messages aux personnes réelles (règle de William, 19/07/2041, 19h47)")
    pdf.puces([
        "Aucune personne ne doit soupçonner qu'elle parle à une IA : messages humains, phrases courtes et variées, ton du pays du destinataire, ni liste à puces ni formule d'assistant.",
        "Aucun envoi la nuit chez le destinataire (entre 23h et 7h), pas de réponse instantanée à toute heure, pas de texte répété d'un candidat à l'autre.",
        "Le directeur général virtuel relit chaque message sur ce critère avant l'envoi. Signature : décision de William (prénom d'assistant de projet ou « l'équipe du projet »).",
        "Le numéro de téléphone privé de William n'est plus jamais fourni ; Jean-Baptiste Tuo est un cas exceptionnel que William traite lui-même.",
    ], taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-19_Règles_du_segment_virtuel_version_7.pdf"))


def regles_v8():
    """Registre des règles du segment virtuel, version du 19/07/2041 (19h59) : signature « L'équipe du projet » et deux rapports hebdomadaires de chaque responsable réel."""
    pdf = DocPDF("Règles du segment virtuel : version du 19 juillet 2041 (19h59)", "Directeur général virtuel · remplace la version 7 de 19h56", auteur="Claude (directeur général virtuel)",
                 pied="Règles du segment virtuel — version 8")
    pdf.titre1("1. Rôles")
    pdf.puces([
        "Le directeur général virtuel gère TOUS les pôles (RH, juridique, finance, technique, commercial) au fur et à mesure de leur ouverture ; William se tourne vers lui avant toute décision, et la décision reste celle de William.",
        "Le pôle RH virtuel recrute : annonces, tri A, B, C, entretiens, notes sur 100. Les autres pôles s'ouvrent après la signature du directeur général réel.",
        "Le segment virtuel apporte l'analyse, les chiffres et la vérification contre les textes ; le terrain, l'aspect humain et l'autorité sur des salariés appartiennent à l'équipe réelle.",
    ], taille=9.5)
    pdf.titre1("2. Rapport à William")
    pdf.puces([
        "William ne reçoit qu'UN rapport final par jour, à 20h00 (le premier : le 19/07/2041). Il remplace le rapport de 18h00 du pôle RH et les alertes immédiates de niveau A.",
        "Contenu : les décisions que William seul peut prendre, chacune ramenée à une question fermée avec l'analyse en deux lignes ; puis l'état des pôles en dix lignes au plus. Sans décision à prendre, le rapport le dit.",
        "Exceptions à l'attente de 20h00 : un candidat qui fixe un délai de réponse court, un document à signer, un paiement demandé.",
        "Circuit : chaque agent adresse son rapport au directeur général virtuel ; les agents actifs relisent le rapport final avant l'envoi et leurs réserves sont jointes. Même circuit pour l'équipe réelle : ses rapports passent par le directeur général virtuel.",
        "Le numéro de téléphone de William n'est plus fourni à personne (décision du 19/07/2041, 18h50). Le seul canal est le courriel professionnel du projet, connecté au directeur général virtuel, qui converse avec les candidats par ce courriel, analyse et prépare la décision que William prend (elle arrive dans le rapport de 20h00).",
    ], taille=9.5)
    pdf.titre1("3. Confidentialité (consigne de William, 19/07/2041, 18h12)")
    pdf.puces([
        "Aucune personne réelle n'est informée du système d'IA de William. Aucun élément de sa vie privée n'est mis en avant, jamais.",
        "Si une personne s'étonne de son niveau d'expertise : « un homme cultivé qui prend son projet au sérieux » ; rien de plus.",
        "Le nom de William n'est communiqué qu'avec sa décision.",
    ], taille=9.5)
    pdf.titre1("4. Contact avec les candidats et surveillance")
    pdf.puces([
        "Seuil de contact : 70 sur 100. Au-dessus du seuil : seul le courriel professionnel du projet est fourni au candidat ; le numéro de téléphone de William n'est jamais fourni. Un numéro déjà transmis (Jean-Baptiste Tuo, 19/07/2041, 11h53) ne se reprend pas.",
        "Chaque message sortant d'un agent vers une personne réelle est relu par le directeur général virtuel avant l'envoi ; un écart est bloqué et signalé dans le rapport.",
        "Contrôle : pas de nom de William, pas de mention d'un système d'IA, pas de vie privée, pas de promesse, pas de chiffre hors annonce, pas de somme demandée.",
    ], taille=9.5)
    pdf.titre1("5. Limites")
    pdf.puces([
        "Aucun agent ne signe, ne paie, ne promet ; jamais de frais d'avance demandés à un candidat.",
        "Budget d'API de l'application Gestion : 1 000 € par mois au plus.",
        "Aucun contact avec un avocat, un comptable ou une administration sans l'accord de William (des honoraires peuvent en découler).",
    ], taille=9.5)
    pdf.titre1("6. Doubles virtuels et pouvoirs (règle de William, 19/07/2041, 19h47)")
    pdf.puces([
        "Chaque pôle virtuel est le double du directeur du même pôle dans la vraie vie ; le directeur général virtuel est le double du directeur général réel.",
        "Tant que le poste réel est vacant, le pôle virtuel DÉCIDE dans son périmètre (exemple : le pôle RH virtuel crée les offres d'emploi et les gère).",
        "Dès qu'un responsable réel occupe le poste, le pôle virtuel ne décide plus : il ÉVALUE et CONTRE-EXPERTISE.",
        "Les rapports des responsables réels atterrissent dans le pôle virtuel correspondant, qui les évalue ; le directeur général virtuel consolide dans le rapport final de 20h00.",
        "Rapport du directeur général réel (proposition) : résultats contre jalons, trésorerie et engagements, risques et décisions demandées, appréciation courte de chaque membre de l'équipe, recoupée par le pôle RH virtuel. Il arrive en parallèle des rapports des pôles, pas à travers eux.",
        "Fréquence (décision de William, 19/07/2041, 19h58) : DEUX rapports hebdomadaires de chaque responsable réel, à la place d'un rapport mensuel, en plus du rapport final quotidien de 20h00. Jours proposés par le directeur général virtuel : mardi 17h00 (point d'étape) et vendredi 12h00 (rapport complet) ; un rapport de plus les jours importants.",
    ], taille=9.5)
    pdf.titre1("7. Messages aux personnes réelles (règle de William, 19/07/2041, 19h47)")
    pdf.puces([
        "Aucune personne ne doit soupçonner qu'elle parle à une IA : messages humains, phrases courtes et variées, ton du pays du destinataire, ni liste à puces ni formule d'assistant.",
        "Aucun envoi la nuit chez le destinataire (entre 23h et 7h), pas de réponse instantanée à toute heure, pas de texte répété d'un candidat à l'autre.",
        "Le directeur général virtuel relit chaque message sur ce critère avant l'envoi. Signature : « L'équipe du projet » (décision de William, 19/07/2041, 19h58) ; aucun prénom ni nom inventé, car se faire passer pour une personne qui n'existe pas exposerait le projet à un risque juridique en cas de découverte.",
        "Le numéro de téléphone privé de William n'est plus jamais fourni ; Jean-Baptiste Tuo est un cas exceptionnel que William traite lui-même.",
    ], taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-19_Règles_du_segment_virtuel_version_8.pdf"))


def note_titre():
    """Note de William sur le titre du dirigeant (SARL : gérant, SAS : directeur général), rédigée avec un autre agent IA ; remise à Claude le 18/07/2041 au soir."""
    pdf = DocPDF("Note : titre du dirigeant local (SARL ou SAS)", "Rapport de William Ossimi, établi avec un agent IA · jeudi 18 juillet 2041", auteur="William Ossimi",
                 pied="Note de William Ossimi — titre du dirigeant")
    pdf.para("Le titre officiel de la personne placée au sommet de la structure dépend de la forme juridique de droit OHADA retenue en Côte d'Ivoire : une SARL ou une SAS "
             "(acte uniforme sur les sociétés commerciales, révisé en 2014). Dans le cadre du statut de fonctionnaire luxembourgeois (article 14), William reste associé ou actionnaire "
             "non-gérant, sans mandat exécutif, sans fonction de gérant, de gestionnaire ou d'administrateur : toute la direction opérationnelle est confiée à un dirigeant local.")
    pdf.titre1("1. Quel titre selon la structure ?")
    pdf.puces([
        "SARL : « Gérant » (ou gérant statutaire). Une SARL est dirigée par un gérant, obligatoirement local puisque l'article 14 interdit ce poste à William, qui détient les parts comme associé non-gérant.",
        "SAS : « Directeur Général (DG) » ou « Président », mandataire exécutif. William y est actionnaire non-gérant, sans mandat exécutif ni acte de gestion. "
        "L'intitulé exact est à fixer dans les statuts par un avocat ou un notaire d'Abidjan.",
        "Pas de « PDG » : ce titre suppose un conseil d'administration, propre aux sociétés anonymes, et créerait des mandats d'administrateur interdits à William sans autorisation ministérielle.",
    ], taille=9.5)
    pdf.tableau(["Forme sociale", "Titre du numéro 1 local", "Statut de William (article 14)"], [
        ["SARL de droit OHADA", "Gérant (ou gérant local)", "Associé non-gérant, sans acte de gestion"],
        ["SAS de droit OHADA", "Mandataire exécutif (Président ou DG, fixé dans les statuts)", "Actionnaire non-gérant, sans mandat exécutif"],
    ], [44, 70, 60], taille=9)
    pdf.titre1("2. Formuler la recherche")
    pdf.puces([
        "Intitulé conseillé dans l'annonce ou l'approche directe : « Gérant local / Directeur Général (partenaire opérationnel) », qui couvre la SARL (gérant) et le langage courant d'une SAS (DG).",
        "Répartition des rôles : le candidat est seul détenteur du mandat exécutif et de la signature de gestion sur place ; son pouvoir est encadré par les statuts OHADA, un pacte d'associés et des clauses de sortie rédigés par l'avocat ou le notaire d'Abidjan.",
        "Avant toute nomination : références, projets livrés, absence de litiges, antécédents et structure de capital envisagée s'il prend des parts.",
    ], taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-18_Note_titre_du_dirigeant_SARL_SAS.pdf"))


def fiche_poste():
    """Fiche de poste et annonce version 2 de l'agent IA, pôle ressources humaines de William (19/07/2041, 00h04)."""
    pdf = DocPDF("Fiche de poste et annonce : Directeur Général / Gérant", "Pôle ressources humaines (Claude) · version du vendredi 19 juillet 2041, 00h04", auteur="Claude (agent IA)",
                 pied="Fiche de poste — Directeur Général / Gérant")
    pdf.titre1("1. Intitulé et structure")
    pdf.puces([
        "Intitulé : « Directeur Général / Gérant, partenaire opérationnel ». Titre légal : Gérant si la société est une SARL, Directeur Général si c'est une SAS.",
        "Le choix SARL ou SAS reste à trancher avec l'avocat ou le notaire d'Abidjan.",
        "Rôle : seul détenteur du mandat exécutif sur place, sous les statuts OHADA, un pacte d'associés, un audit annuel indépendant et des clauses de sortie. William est associé non-gérant.",
        "Rémunération : à discuter avec le candidat, selon ce qu'il apporte.",
    ], taille=9.5)
    pdf.titre1("2. Compétences requises")
    pdf.tableau(["Domaine", "Ce qu'il faut maîtriser"], [
        ["Solaire en toiture", "Dimensionner une centrale (outil de simulation de type PVSyst, plans), suivre le chantier, raccorder en basse et moyenne tension, normes de sécurité électrique, "
                               "maintenance et supervision à distance, pilotage des sous-traitants."],
        ["Régime ivoirien", "Code de l'électricité (loi 2014-132), régulateur ANARE-CI, distributeur, vente de l'excédent d'un autoproducteur (décret 2016-783), autorisations et raccordement."],
        ["Commercial en entreprises", "Prospecter des PME, hôtels, cliniques et entrepôts ; chiffrer l'économie sur la facture d'électricité ; accompagner le financement du client."],
        ["Gestion", "Diriger une petite équipe (techniciens, commercial, administratif) ; budget d'investissement et d'exploitation ; comptabilité OHADA ; achats et importation de matériel."],
        ["Gouvernance", "Rendre compte à l'associé non-gérant ; audit annuel indépendant ; respecter les tranches conditionnelles et le pacte d'associés."],
        ["Intégrité", "Références vérifiables, projets livrés, absence de litiges, antécédents nets."],
    ], [38, 136], taille=9)
    pdf.titre1("3. Diplôme et expérience")
    pdf.puces([
        "Diplôme : ingénieur en électricité ou en énergétique (bac + 5) de préférence ; à défaut, dix ans de pratique du solaire en entreprise. Une formation en gestion est un plus. "
        "Un doctorat n'est pas exigé : utile seulement s'il touche à l'énergie.",
        "Expérience : dix ans ou plus, dont cinq en direction de projets ou d'équipe.",
    ], taille=9.5)
    pdf.titre1("4. Barème de recrutement (100 points)")
    pdf.tableau(["Critère", "Points"], [
        ["Compétences techniques solaire", "25"], ["Régime ivoirien et autorisations", "15"], ["Expérience commerciale en entreprises", "15"],
        ["Gestion d'équipe et de budget", "15"], ["Fiabilité et antécédents", "20"], ["Disponibilité et motivation", "10"],
    ], [130, 44], taille=9)
    pdf.para("Seuil de contact direct avec William : 70. De 60 à 69, second entretien. Sous 60, dossier gardé (postes commerciaux ou futurs).", taille=9, italique=True)
    pdf.titre1("5. Points à vérifier")
    pdf.puces([
        "En Côte d'Ivoire, l'autoproducteur doit être propriétaire de son installation, selon une analyse de cabinet d'avocats : cela exclut la location de panneaux aux entreprises. "
        "Le projet devrait vendre, installer et entretenir plutôt que louer. À faire confirmer par l'avocat d'Abidjan et par l'ANARE-CI (seuils et procédure non trouvés).",
        "Forme sociale (SARL ou SAS), statuts, pacte d'associés : avocat ou notaire d'Abidjan.",
    ], taille=9.5)
    pdf.titre1("6. Annonce, version 2")
    pdf.para("Directeur Général / Gérant, partenaire opérationnel : solaire pour entreprises à Abidjan", taille=11)
    pdf.para("Un investisseur européen crée à Abidjan une société de droit OHADA dédiée à l'installation et à la maintenance de centrales solaires d'autoproduction sur toitures d'entreprises "
             "(PME, cliniques, entrepôts, hôtels). Il recherche la personne qui la dirigera sur place : Directeur Général (Gérant si la société est une SARL), partenaire opérationnel.")
    pdf.puces([
        "Investissement : 300 000 € (environ 196,8 millions FCFA) sur trois ans, en trois tranches conditionnelles : 60 000 € la première année (société et pilote), 135 000 € la deuxième, 105 000 € la troisième, "
        "chacune débloquée sur résultats vérifiés et bilan audité.",
        "Structure : société de droit OHADA. L'investisseur est associé non-gérant. Le dirigeant local détient seul la direction opérationnelle, encadrée par les statuts, un pacte d'associés, un audit annuel indépendant et des clauses de sortie.",
        "Marché : croissance du PIB de 6 à 6,7 % par an, objectif de 45 % d'énergies renouvelables en 2030, électrification d'environ 94 % en 2024, franc CFA à parité fixe avec l'euro.",
        "Rémunération : à définir ensemble selon le profil et l'apport du candidat.",
        "Profil : ingénieur en électricité ou en énergétique de préférence (ou dix ans de solaire en entreprise), dix ans d'expérience ou plus, connaissance du régime ivoirien de l'autoproduction, "
        "expérience de vente en entreprises et de direction d'équipe, références vérifiables.",
    ], taille=9.5)
    pdf.para("Pour répondre : parcours détaillé, trois références, lecture du marché. Aucune somme n'est demandée à qui répond.", taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-19_Fiche_de_poste_Directeur_général_Gérant.pdf"))


def annonce_v3():
    """Annonce version 3 de l'agent IA (19/07/2041, 12h32) : ouverte à la diaspora ivoirienne et au monde entier, bilingue."""
    pdf = DocPDF("Annonce version 3 : diaspora et international", "Pôle ressources humaines (Claude) · vendredi 19 juillet 2041, 12h32", auteur="Claude (agent IA)",
                 pied="Annonce version 3 — diaspora et international")
    pdf.titre1("Version française")
    pdf.para("Directeur Général / Gérant, partenaire opérationnel : solaire pour entreprises à Abidjan. Ouvert aux candidats de la diaspora ivoirienne et d'ailleurs dans le monde qui souhaitent rentrer en Côte d'Ivoire.", taille=11)
    pdf.para("Un investisseur européen crée à Abidjan une société de droit OHADA dédiée à l'installation et à la maintenance de centrales solaires d'autoproduction sur toitures d'entreprises "
             "(PME, cliniques, entrepôts, hôtels). Il recherche la personne qui la dirigera sur place, y compris depuis l'étranger pour une période de transition : relocalisation à Abidjan à discuter.")
    pdf.puces([
        "Investissement : 300 000 € (environ 196,8 millions FCFA) sur trois ans, en trois tranches conditionnelles : 60 000 €, 135 000 € et 105 000 €, chacune débloquée sur résultats vérifiés et bilan audité.",
        "Structure : société de droit OHADA ; l'investisseur est associé non-gérant ; le dirigeant local détient seul la direction opérationnelle, encadrée par les statuts, un pacte d'associés, un audit annuel indépendant et des clauses de sortie.",
        "Marché : croissance du PIB de 6 à 6,7 % par an, objectif de 45 % d'énergies renouvelables en 2030, franc CFA à parité fixe avec l'euro.",
        "Rémunération : à définir ensemble selon le profil et l'apport du candidat. Aucune promesse de relocalisation ou de salaire à ce stade.",
        "Profil : ingénieur en électricité ou en énergétique de préférence (ou dix ans de solaire en entreprise), dix ans d'expérience ou plus, vente en entreprises, direction d'équipe, références vérifiables.",
    ], taille=9.5)
    pdf.para("Pour répondre : parcours détaillé, trois références, lecture du marché. Aucune somme n'est demandée à qui répond.", taille=9.5)
    pdf.titre1("English version")
    pdf.para("General Manager / Managing Director, operating partner: solar power for businesses in Abidjan. Open to candidates from the Ivorian diaspora and from anywhere in the world who wish to return to Côte d'Ivoire.", taille=11)
    pdf.para("A European investor is setting up an OHADA-law company in Abidjan to install and maintain self-generation solar plants on business rooftops (SMEs, clinics, warehouses, hotels). "
             "The investor is looking for the person who will run it on the ground, possibly from abroad during a transition period; relocation to Abidjan to be discussed.")
    pdf.puces([
        "Investment: EUR 300,000 (about CFA 196.8 million) over three years in three conditional tranches of EUR 60,000, 135,000 and 105,000, each released on verified results and audited accounts.",
        "Structure: OHADA-law company; the investor is a non-managing partner; the local manager holds sole operational management, framed by the articles, a shareholders' agreement, an annual independent audit and exit clauses.",
        "Market: GDP growth of 6 to 6.7% a year, a 45% renewable-energy target for 2030, CFA franc pegged to the euro.",
        "Pay: to be agreed according to the candidate's profile and contribution. No promise of relocation or salary at this stage.",
        "Profile: electrical or energy engineer preferred (or ten years of solar experience in business), ten years or more of experience, B2B sales, team management, verifiable references.",
    ], taille=9.5)
    pdf.para("To apply: detailed background, three references, your view of the market. No payment is ever requested from applicants.", taille=9.5)
    pdf.sauver(chemin("documents_william", "2041-07-19_Annonce_version_3_diaspora_et_international.pdf"))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd in ("courriel-ministere", "tout"):
        courriel_ministere()
    if cmd in ("abonnement", "tout"):
        abonnement()
    if cmd in ("annonce", "tout"):
        annonce()
    if cmd == "regles-v2":
        regles_v2()
    if cmd == "regles-v3":
        regles_v3()
    if cmd == "regles-v4":
        regles_v4()
    if cmd == "regles-v5":
        regles_v5()
    if cmd == "regles-v6":
        regles_v6()
    if cmd == "regles-v7":
        regles_v7()
    if cmd == "regles-v8":
        regles_v8()
    if cmd == "annonce-v3":
        annonce_v3()
    if cmd == "poste":
        note_titre()
        fiche_poste()
    if cmd not in ("courriel-ministere", "abonnement", "annonce", "regles-v2", "regles-v3", "regles-v4", "regles-v5", "regles-v6", "regles-v7", "regles-v8", "annonce-v3", "poste", "tout"):
        sys.exit(__doc__)
