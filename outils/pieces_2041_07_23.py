"""PIÈCES DU 23/07/2041 (univers 3, tour n° 46) :
1. Maquettes de Contrats de Travail — Niveaux 2 & 3 : Directeurs de Pôle & Chefs d'Équipe (CDI Cadres & Maîtrise) ;
2. Maquettes de Contrats de Travail — Niveau 4 : Techniciens & Employés d'Exécution (CDI Ouvriers & Employés) ;
3. Rapport quotidien du Directeur Général virtuel (23 juillet 2041, 20h00).

Génération des fichiers PDF physiques (règle 4 et directives de William du 22/07 et 23/07/2041)
déposés dans `documents_william/` et référencés dans l'application Gestion / Téléphone.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_maquette_directeurs_et_chefs():
    pdf = DocPDF(
        "Maquettes de Contrats de Travail — Niveaux 2 & 3",
        "Directeurs de Pôle (Cadres Dirigeants) & Chefs d'Équipe (Agents de Maîtrise) · Droit Ivoirien (CCI / Code du Travail)",
        auteur="Pôle Juridique virtuel & Direction Générale",
        pied="Projet Solaire B2B Abidjan — Maquettes Contrats Niveaux 2 & 3"
    )

    pdf.meta("Projet", "Projet Solaire B2B Abidjan (SAS de droit OHADA en constitution)")
    pdf.meta("Cadre légal", "Loi n° 2015-532 (Code du travail de Côte d'Ivoire) et Convention Collective Interprofessionnelle (CCI)")
    pdf.meta("Niveaux couverts", "Niveau 2 (Directeurs de pôle : Cadres) et Niveau 3 (Chefs d'équipe : Agents de maîtrise)")
    pdf.meta("Supervision", "Direction Générale & Associé Unique (William Ossimi)")
    pdf.meta("Date de validation", "Mardi 23 juillet 2041")
    pdf.ln(3)

    pdf.titre1("Préambule — Architecture pyramidale et principes directeurs")
    pdf.para(
        "Le présent document formalise le socle contractuel des cadres dirigeants de pôle (Niveau 2) et des agents de maîtrise "
        "d'encadrement opérationnel (Niveau 3) de la société. Alors que le Directeur Général relève d'un mandat social exclusif de "
        "salariat (Niveau 1, droit OHADA), les fonctions de Niveaux 2 et 3 sont expressément régies par le droit du travail ivoirien "
        "sous la forme de contrats de travail à durée indéterminée (CDI)."
    )
    pdf.para(
        "Les clauses économiques précises (salaires de base, barèmes de commissionnement spécifiques) comportent des variables "
        "qui seront arrêtées définitivement lors de la conclusion de chaque recrutement par la Direction Générale, dans le respect "
        "des seuils conventionnels ivoiriens."
    )

    pdf.titre1("Section 1 — Dispositions communes aux contrats de Niveaux 2 & 3")
    pdf.puces([
        "Forme juridique : Contrat de travail à durée indéterminée (CDI) soumis au Code du travail ivoirien et à la Convention Collective Interprofessionnelle.",
        "Période d'essai : 3 mois renouvelable une fois pour les cadres (Niveau 2), 2 mois renouvelable une fois pour les agents de maîtrise (Niveau 3).",
        "Lieu de travail : Grand Abidjan (siège social et chantiers), avec déplacements professionnels requis sur l'ensemble du territoire ivoirien.",
        "Protection sociale & santé : Affiliation obligatoire à la CNPS (retraite, accidents du travail, prestations familiales) et à la Couverture Maladie Universelle (CMU). Adhésion au Service Médical Inter-Entreprises (SMIE).",
        "Congés payés : 2,2 jours ouvrables par mois de travail effectif, conformément aux dispositions légales ivoiriennes.",
        "Obligation de loyauté et secret des affaires : Confidentialité absolue sur l'ensemble des études techniques, dimensionnements solaires, marges, prix d'achat fournisseurs et fichiers clients de la société."
    ])

    pdf.titre1("Section 2 — Contrat Cadre Niveau 2 : Directeur Technique Solaire")
    pdf.para(
        "Rattachement hiérarchique : Directeur Général. Statut : Cadre dirigeant technique (Catégorie Cadre supérieur CCI)."
    )
    pdf.para(
        "Missions principales : Pilotage intégral du bureau d'études, validation technique et dimensionnement des centrales photovoltaïques "
        "en toiture B2B (puissances 50 kWc à 1 MWc), validation des notes de calcul de structures et charges de toitures industrielles, "
        "direction des travaux, supervision des raccordements aux réseaux CIE et respect des normes CI-ÉNERGIES."
    )
    pdf.puces([
        "Habilitations obligatoires : Titulaire des habilitations électriques haute et basse tension (B2V, BR, BC, H2V). Maintien des certifications à la charge de la société.",
        "Sécurité et pouvoir d'arrêt d'urgence : Responsable de la sécurité des personnes sur les chantiers. Dispose d'une délégation expresse de pouvoir en matière d'hygiène et sécurité, incluant le droit et le devoir d'ordonner l'arrêt immédiat de tout chantier en toiture en cas de non-respect des équipements de protection individuelle (EPI) ou de risque météorologique grave.",
        "Régime horaire : Forfait-cadre autonome sans référence aux 40 heures hebdomadaires, impliquant une disponibilité totale en phase de mise en service.",
        "Rémunération : Rémunération fixe mensuelle brute [Fixée à l'embauche selon profil, plancher conventionnel cadre] + Prime annuelle de performance indexée sur le volume de MWc raccordés sans réserve technique et l'absence totale d'accident du travail avec arrêt.",
        "Clause de non-concurrence : Interdiction d'exercer dans toute entreprise concurrente de pose solaire en toiture sur le district d'Abidjan pendant 12 mois suivant la rupture du contrat, assortie d'une clause pénale équivalente à 6 mois de salaire brut."
    ])

    pdf.titre1("Section 3 — Contrat Cadre Niveau 2 : Directeur Commercial B2B")
    pdf.para(
        "Rattachement hiérarchique : Directeur Général. Statut : Cadre dirigeant commercial (Catégorie Cadre CCI)."
    )
    pdf.para(
        "Missions principales : Définition et exécution du plan de prospection B2B sur les zones industrielles et commerciales d'Abidjan "
        "(Vridi, Yopougon, Koumassi, Zone 4) et de l'intérieur (Bouaké, San Pedro). Négociation des contrats d'installation clé en main et "
        "contrats de vente d'électricité (PPA). Encadrement de la force de vente terrain."
    )
    pdf.puces([
        "Rémunération composite : Salaire fixe mensuel garanti [Fixé à l'embauche] + Commissions variables calculées exclusivement sur la marge brute encaissée par la société (taux indicatif de 3 à 5 % de la marge brute hors taxes après encaissement effectif du solde client).",
        "Condition suspensive de commissionnement : Aucune commission n'est exigible tant que le client n'a pas intégralement soldé les factures d'acompte et de réception de l'installation solaire.",
        "Propriété des fichiers et clientèle : L'ensemble des prospects, clients, contacts d'entreprises et devis constituent la propriété exclusive, inaliénable et confidentielle de la société. Interdiction formelle d'exporter ou copier la base CRM à des fins personnelles.",
        "Clause de non-sollicitation et non-concurrence : Interdiction de démarcher la clientèle de la société ou de travailler pour un installateur concurrent sur le territoire national ivoirien pendant une durée de 12 mois après cessation des fonctions."
    ])

    pdf.titre1("Section 4 — Contrat Cadre Niveau 2 : Responsable Administratif & Financier (DAF)")
    pdf.para(
        "Rattachement hiérarchique : Directeur Général et Associé Unique. Statut : Cadre dirigeant administratif et financier."
    )
    pdf.para(
        "Missions principales : Tenue de la comptabilité générale et analytique selon le Système Comptable OHADA (SYSCOHADA), gestion de la "
        "trésorerie locale, préparation des déclarations fiscales et sociales (TVA, CNPS, impôts sur les traitements et salaires), gestion des "
        "relations avec les banques ivoiriennes et recouvrement rigoureux des créances clients."
    )
    pdf.puces([
        "Gouvernance financière et limitations : Double signature obligatoire avec le Directeur Général sur l'ensemble des comptes bancaires de la société pour tout décaissement supérieur à 2 000 000 FCFA. Interdiction stricte d'octroyer des facilités de caisse ou découverts sans autorisation écrite de l'associé unique.",
        "Rémunération : Salaire fixe mensuel [Fixé à l'embauche] + Prime annuelle de bilan et d'optimisation du recouvrement.",
        "Secret professionnel renforcé : Confidentialité absolue sur la structure financière, les marges de l'entreprise, les flux de capitaux et les rémunérations du personnel. Tout manquement constitue une faute lourde entraînant rupture immédiate."
    ])

    pdf.titre1("Section 5 — Contrat Niveau 3 : Chef d'Équipe Pose et Installation Toiture")
    pdf.para(
        "Rattachement hiérarchique : Directeur Technique. Statut : Agent de maîtrise de chantier (Catégorie AM1 / AM2 CCI)."
    )
    pdf.para(
        "Missions principales : Encadrement opérationnel direct des techniciens monteurs sur les toitures industrielles. Organisation "
        "quotidienne du chantier, réception des approvisionnements sur site, contrôle des ancrages et fixations, raccordements DC et "
        "sécurisation des accès."
    )
    pdf.puces([
        "Responsabilité de sécurité toiture : Contrôle quotidien obligatoire avant toute montée en toiture des harnais, lignes de vie, filets de sécurité et casques avec jugulaire. Interdiction formelle de laisser un ouvrier monter sans sécurisation complète.",
        "Régime de travail : 40 heures hebdomadaires avec modulation possible selon les contraintes thermiques et météorologiques de chantier.",
        "Rémunération : Salaire de base garanti de maîtrise + Indemnité journalière de panier chantier + Prime de chantier au kWc posé sans anomalie ni incident de sécurité."
    ])

    pdf.titre1("Section 6 — Contrat Niveau 3 : Superviseur Commercial Terrain")
    pdf.para(
        "Rattachement hiérarchique : Directeur Commercial B2B. Statut : Agent de maîtrise commercial."
    )
    pdf.para(
        "Missions : Accompagnement terrain des commerciaux juniors, réalisation des pré-audits techniques de toitures (relevé de surface, "
        "inclinaison, ombrages, analyse des factures CIE) et qualification approfondie des décideurs industriels."
    )
    pdf.puces([
        "Rémunération : Salaire fixe de base + Prime d'encadrement d'équipe + Commission sur les dossiers audités convertis en contrats signés."
    ])

    fichier_sortie = chemin("documents_william", "2041-07-23_Maquette_Contrats_Directeurs_et_Chefs_d_Equipe.pdf")
    pdf.sauver(fichier_sortie)
    return fichier_sortie


def generer_maquette_techniciens_et_employes():
    pdf = DocPDF(
        "Maquettes de Contrats de Travail — Niveau 4",
        "Techniciens de Chantier & Employés d'Exécution · Droit du Travail Ivoirien (Loi n° 2015-532 & CCI)",
        auteur="Pôle Juridique virtuel, Pôle Technique & Pôle RH",
        pied="Projet Solaire B2B Abidjan — Maquettes Contrats Niveau 4"
    )

    pdf.meta("Projet", "Projet Solaire B2B Abidjan (SAS de droit OHADA en constitution)")
    pdf.meta("Cadre réglementaire", "Loi n° 2015-532 portant Code du travail de Côte d'Ivoire & CCI")
    pdf.meta("Niveau couvert", "Niveau 4 (Salariés d'exécution : Ouvriers qualifiés et Employés)")
    pdf.meta("Supervision", "Directeurs de pôle & Chefs d'équipe")
    pdf.meta("Date de validation", "Mardi 23 juillet 2041")
    pdf.ln(3)

    pdf.titre1("Section 1 — Cadre légal et conventionnel du personnel d'exécution")
    pdf.para(
        "Les contrats de travail de Niveau 4 concernent le personnel opérationnel de terrain et le support administratif. Ils sont régis "
        "par les dispositions impératives du Code du travail de Côte d'Ivoire et de la Convention Collective Interprofessionnelle (CCI). "
        "Chaque contrat est conclu sous la forme d'un CDI assorti d'une période d'essai d'un mois (renouvelable une fois pour les techniciens "
        "qualifiés selon les stipulations conventionnelles)."
    )
    pdf.para(
        "Le temps de travail effectif est fixé à la durée légale de 40 heures par semaine (article 21.1 du Code du travail). Toute heure "
        "effectuée au-delà donne lieu aux majorations légales pour heures supplémentaires. Les cotisations sociales obligatoires sont "
        "intégralement déclarées et versées à la Caisse Nationale de Prévoyance Sociale (CNPS) et à la Couverture Maladie Universelle (CMU)."
    )

    pdf.titre1("Section 2 — Contrat Technicien Monteur Électricien Photovoltaïque Toiture")
    pdf.para(
        "Qualification : Ouvrier qualifié / Monteur-électricien toiture (Catégorie Ouvrier qualifié OQ2 / OQ3 CCI). "
        "Rattachement : Chef d'équipe pose toiture et Directeur Technique."
    )
    pdf.para(
        "Missions opérationnelles : Manutention et déchargement des panneaux et profilés métalliques, installation des structures "
        "de fixation sur bacs acier et toitures industrielles, pose et fixation des modules solaires photovoltaïques, tirage des "
        "câbles solaires en courant continu (DC), raccordement des connecteurs MC4, mise à la terre des châssis métalliques, fixation "
        "et raccordement des onduleurs et coffrets de protection AC/DC."
    )
    pdf.titre1("Obligations impératives d'hygiène, sécurité et travail en hauteur")
    pdf.puces([
        "Aptitude médicale obligatoire : L'embauche définitive est subordonnée au certificat médical d'aptitude au travail en hauteur délivré par le Service Médical Inter-Entreprises (SMIE) agréé en Côte d'Ivoire.",
        "Port obligatoire permanent des EPI : Le port du casque de sécurité avec jugulaire, des chaussures de sécurité à semelle isolante, des gants de protection et du harnais de sécurité complet relié à une ligne de vie certifiée est strictement obligatoire dès la première marche d'accès à la toiture.",
        "Conditions climatiques d'arrêt : Interdiction absolue de monter sur toiture en cas de pluie, d'orage, de surface mouillée ou de vent soufflant en rafales supérieures à 40 km/h.",
        "Clause de sanction pour faute lourde : Tout refus, omission ou négligence avérée dans le port des EPI de sécurité constitue une violation délibérée des règles de sécurité engageant la vie du salarié et de ses collègues, qualifiée immédiatement de faute lourde justifiant un licenciement sans préavis ni indemnités de rupture.",
        "Rémunération et primes : Salaire de base indicatif [Fixé à l'embauche selon catégorie conventionnelle] + Indemnité journalière de panier chantier + Prime mensuelle de technicité et de travail en hauteur."
    ])

    pdf.titre1("Section 3 — Contrat Commercial B2B Junior / Chargé de Prospection")
    pdf.para(
        "Qualification : Employé commercial / Vendeur prospecteur B2B (Catégorie Employé E4 / E5 CCI). "
        "Rattachement : Superviseur commercial terrain et Directeur Commercial B2B."
    )
    pdf.para(
        "Missions principales : Prospection active de terrain dans les zones industrielles et parcs logistiques d'Abidjan (Vridi, Yopougon, "
        "Koumassi, Treichville, Zone 4), qualification des toitures de bâtiments commerciaux et entrepôts, identification des propriétaires "
        "et locataires industriels, collecte des factures d'électricité CIE des douze derniers mois et prise de rendez-vous qualifiés."
    )
    pdf.puces([
        "Structure de rémunération : Salaire fixe mensuel garanti supérieur au SMIG conventionnel [Fixé à l'embauche] + Commissions variables forfaitaires par dossier prospecté qualifié ayant fait l'objet d'un audit toiture et commission au résultat sur affaire signée et raccordée.",
        "Exclusivité et confidentialité de la prospection : Obligation de consacrer l'intégralité du temps de travail à la prospection exclusive des offres de la société. Interdiction formelle de représenter d'autres entreprises ou d'exercer une activité de courtage énergétique indépendant.",
        "Propriété des fichiers : Toutes les listes de contacts, adresses de sites, coordonnées de gérants et photographies de toitures recueillies constituent la propriété exclusive de l'entreprise. Restitution immédiate exigée en cas de rupture de contrat."
    ])

    pdf.titre1("Section 4 — Contrat Assistant Administratif & Logistique")
    pdf.para(
        "Qualification : Employé de gestion administrative et approvisionnements (Catégorie Employé E3 / E4 CCI). "
        "Rattachement : Responsable Administratif et Financier (DAF)."
    )
    pdf.para(
        "Missions principales : Gestion du secrétariat général, classement des documents comptables et juridiques, suivi des dossiers "
        "d'importation maritime des modules photovoltaïques et onduleurs transitant par le Port Autonome d'Abidjan (relation avec les transitaires, "
        "suivi des Bordereaux de Suivi de Cargaison - BSC, formalités douanières d'exonération Code des investissements), et tenue rigoureuse "
        "du registre d'entrées et sorties du magasin de pièces détachées et outillages."
    )
    pdf.puces([
        "Rémunération : Salaire mensuel conventionnel de base [Fixé à l'embauche] + Prime semestrielle de rigueur logistique et administrative.",
        "Responsabilité d'inventaire : Tenue à jour du stock physique et de l'inventaire informatisé. Aucune sortie de matériel (panneaux, onduleurs, câbles) ne peut s'effectuer sans bon de commande de chantier signé par le Directeur Technique ou un Chef d'équipe."
    ])

    pdf.titre1("Section 5 — Clauses de rupture et attribution de juridiction")
    pdf.para(
        "Les modalités de préavis, de démission et de licenciement sont strictement régies par les barèmes d'ancienneté du Code du travail "
        "ivoirien et de la CCI. En cas de litige individuel du travail non résolu à l'amiable par conciliation auprès de l'Inspection du Travail, "
        "compétence exclusive est attribuée au Tribunal du Travail d'Abidjan."
    )

    fichier_sortie = chemin("documents_william", "2041-07-23_Maquette_Contrats_Techniciens_et_Employes.pdf")
    pdf.sauver(fichier_sortie)
    return fichier_sortie


def generer_rapport_quotidien_23():
    pdf = DocPDF(
        "Rapport quotidien d'activité — Direction Générale virtuelle",
        "Mardi 23 juillet 2041 · 20h00 (heure de Luxembourg / 18h00 Abidjan)",
        auteur="Directeur Général virtuel",
        pied="Projet Solaire B2B Abidjan — Rapport d'activité du 23/07/2041"
    )

    pdf.meta("Émetteur", "Directeur Général virtuel (Pôle Central / Architecture IA)")
    pdf.meta("Destinataire", "William Ossimi, Associé unique et investisseur")
    pdf.meta("Date et heure", "Mardi 23 juillet 2041, 20h00")
    pdf.meta("Objet", "Rapport de clôture du chantier contractuel, suivi RH, échanges tiers et budget")
    pdf.ln(3)

    pdf.titre1("1. Synthèse de la journée du 23 juillet 2041")
    pdf.para(
        "La journée a été consacrée à deux chantiers majeurs menés par William : d'une part, la refonte ergonomique intégrale de "
        "l'application Gestion en Version 1.0 au cours de la matinée (4 heures de dev, 4 onglets étanches et intégration du visualiseur de PDF réels) ; "
        "d'autre part, une session de travail intense de huit heures cet après-midi avec l'ensemble des agents virtuels pour achever la "
        "rédaction des maquettes de contrats de travail pour l'ensemble des pôles de l'entreprise."
    )

    pdf.titre1("2. Finalisation de la pyramide contractuelle de l'entreprise")
    pdf.para(
        "Sous l'impulsion de William et avec l'appui conjoint du Pôle Juridique virtuel et du Pôle RH, l'ensemble de la structure contractuelle "
        "est désormais formalisée sous format PDF vérifié dans documents_william/ et consultable dans l'application Gestion :"
    )
    pdf.puces([
        "Niveau 1 (Direction Générale) : Convention de mandat social pur de droit OHADA (19 articles, caducité stricte, non-concurrence 12 mois sans contrepartie financière, tribunal de commerce). Validée le 22/07.",
        "Niveau 2 (Directeurs de pôle) : Maquette CDI Cadres Dirigeants régis par le Code du travail ivoirien. Couvre le Directeur Technique (habilitations BT/HT, pouvoir d'arrêt d'urgence chantier, garantie décennale), le Directeur Commercial B2B (commissions sur marge brute encaissée, secret de la clientèle) et le DAF (SYSCOHADA, double signature bancaire, secret financier).",
        "Niveau 3 (Chefs d'équipe) : Maquette CDI Agents de Maîtrise de terrain. Couvre le Chef d'équipe pose toiture (contrôle impératif des EPI, travail en hauteur, primes de chantier au kWc posé) et le Superviseur commercial terrain (audits toiture et pré-visites techniques).",
        "Niveau 4 (Salariés d'exécution) : Maquette CDI Salariés et Ouvriers selon le Code du travail ivoirien (40h/semaine, affiliation CNPS/CMU). Couvre le Technicien monteur toiture (obligation absolue des EPI, SMIE travail en hauteur, faute lourde en cas de non-port), le Commercial B2B junior (prospection terrain et exclusivité) et l'Assistant administratif et logistique (suivi douane Port d'Abidjan et tenue des stocks)."
    ])

    pdf.titre1("3. Pôle Ressources Humaines & Suivi des candidatures")
    pdf.puces([
        "Mohamed Coulibaly (note 91/100) : Retours des formulaires de vérification de références en cours de traitement par le pôle RH.",
        "Mariam Brou (note 88/100) : Deuxième profil d'élite en tête de vivier, en attente de calage de l'entretien approfondi.",
        "Kader Assi (note 84/100) : Troisième profil qualifié en attente.",
        "Jean-Baptiste Tuo (note 71/100) : Suite au message de refus courtois envoyé par William sur WhatsApp le 22/07 à 20h05, M. Tuo a répondu ce jour à 19h35 dans des termes dignes et courtois, actant la décision et souhaitant pleine réussite au projet."
    ])

    pdf.titre1("4. Pôle Juridique : Avocat conseil à Abidjan")
    pdf.para(
        "Suite à la validation formelle du devis de 2 100 000 FCFA HT hier soir et à la transmission des coordonnées de William en qualité "
        "d'associé unique (+352), le Cabinet de Me Ismaël Gnamien finalise la lettre de mission d'avocat et le questionnaire KYC d'ouverture de dossier. "
        "Réception attendue sous 24 à 48 heures."
    )

    pdf.titre1("5. Consommation d'API et budget du segment virtuel")
    pdf.para(
        "La session de travail intensif de cet après-midi (génération et validation des maquettes contractuelles Niveaux 2, 3 et 4, "
        "interconnexion des modules d'analyse) a généré une dépense d'API estimée à 4,80 €. Le total mensuel s'établit à 38,36 € sur "
        "le plafond de 1 000,00 €, laissant une réserve disponible de 961,64 € pour le mois de juillet 2041."
    )

    fichier_sortie = chemin("documents_william", "2041-07-23_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(fichier_sortie)
    return fichier_sortie


if __name__ == "__main__":
    f1 = generer_maquette_directeurs_et_chefs()
    f2 = generer_maquette_techniciens_et_employes()
    f3 = generer_rapport_quotidien_23()
    print("3 pièces générées avec succès.")
