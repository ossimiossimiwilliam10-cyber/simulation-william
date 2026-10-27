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
    if cmd == "poste":
        note_titre()
        fiche_poste()
    if cmd not in ("courriel-ministere", "abonnement", "annonce", "regles-v2", "regles-v3", "poste", "tout"):
        sys.exit(__doc__)
