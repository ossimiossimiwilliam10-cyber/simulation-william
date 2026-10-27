"""ÉTUDES DE L'AGENT IA DE WILLIAM (16/07/2041, univers 3) : opportunités d'investissement et de projets au Brésil, puis en Côte d'Ivoire.
Livrables demandés par William au tour n° 2 (règle 4 du fichier maître : vrais PDF dans `documents_william/`), à partir des faits F096 à F108
(`python outils/faits.py cherche "Brésil"`), recherchés le 27/10/2026. Les chiffres sont des repères 2025-2026 (le monde est en 2041) : le rapport
le dit et ne les extrapole pas.

    python outils/etude_ia_2041.py bresil
    python outils/etude_ia_2041.py cote-ivoire
"""
import sys

from pdf_base import DocPDF, chemin

AUTEUR = "Agent IA de William Ossimi"

PROFIL = ("Profil retenu : William Ossimi, 36 ans, fonctionnaire de l'État luxembourgeois (enseignant), résident en France ; non-résident dans "
          "le pays étudié ; français et anglais ; capital liquide immédiatement mobilisable : épargne de sécurité de 75 250 € (le portefeuille ETF "
          "de 670 380 € n'est pas supposé mobilisable) ; pas de temps plein disponible hors vacances scolaires.")

ART14 = [
    "Article 14 du statut général des fonctionnaires de l'État : l'exercice d'une profession commerciale ou d'un mandat de gestionnaire ou "
    "d'administrateur exige une autorisation ministérielle préalable.",
    "Détention de parts : être associé ou actionnaire non-gérant d'une SARL ou d'une SAS est admis sans demande préalable tant qu'aucun mandat "
    "exécutif ni acte de gestion n'est exercé. Dans ce cadre, William ne peut être ni gérant ni administrateur de la société étrangère : la "
    "gestion est confiée à un partenaire local.",
    "Si William voulait un jour gérer lui-même : service à temps partiel (50 % ou 75 %, sous réserve des nécessités du service) ou congé "
    "sans traitement (jusqu'à 2 ans renouvelables, avec droit à réintégration).",
]


def _fin(pdf, sources, limites):
    pdf.titre1("Limites de ce rapport")
    pdf.puces(limites, taille=9)
    pdf.titre1("Sources consultées (chiffres de référence 2025-2026)")
    pdf.puces(sources, taille=8)
    pdf.ln(2)
    pdf.para("Rapport établi par l'agent IA de William pour son usage personnel. Les chiffres cités sont des repères publics, à actualiser auprès des "
             "sources officielles avant tout engagement ; ils ne constituent ni un conseil juridique, ni un conseil fiscal, ni un conseil en investissement.",
             taille=8, italique=True)


def bresil():
    pdf = DocPDF("Opportunités d'investissement et de projets — Brésil",
                 "Rapport n° 1 de l'agent IA de William Ossimi · mardi 16 juillet 2041, 09h41", auteur=AUTEUR,
                 pied="Agent IA de William Ossimi — Brésil")
    pdf.meta("Question posée", "Secteurs à forte demande où un projet peut être lancé ou financé, en commençant par le Brésil (puis la Côte d'Ivoire).")
    pdf.meta("Base", "Séries publiques 2025-2026 recoupées (7 recherches, sources en fin de document).")
    pdf.para(PROFIL, taille=9, italique=True)

    pdf.titre1("1. Synthèse")
    pdf.puces([
        "La demande la mieux documentée est dans l'énergie (solaire distribué, stockage), les infrastructures numériques (centres de données) et "
        "l'eau et l'assainissement. Les tickets d'entrée sont très inégaux : de quelques centaines de milliers d'euros à plusieurs milliards.",
        "Le segment le plus compatible avec le profil de William est le solaire distribué : projets de quelques centaines de kW à quelques MW, "
        "portés par un partenaire local qui construit et exploite, William restant associé non-gérant (compatible avec l'article 14).",
        "Points durs : un administrateur ou représentant résident au Brésil, l'enregistrement du capital étranger à la Banque centrale, une retenue de 10 % "
        "sur les dividendes versés à un non-résident depuis 2026, le risque de change, un crédit local à environ 14 %.",
        "Trous du rapport : l'agro-industrie et l'assainissement n'ont pas de source récente exploitable ; ils sont signalés, pas évalués.",
    ], taille=9.5)

    pdf.titre1("2. Contexte macroéconomique (repères 2026)")
    pdf.tableau(["Indicateur", "Repère", "Lecture"], [
        ["Taux directeur (Selic)", "environ 14 % par an", "Crédit local très cher : les projets financés en fonds propres venus de l'étranger sont favorisés face aux concurrents endettés."],
        ["Inflation attendue", "environ 5 %", "Au-dessus de la cible : pression sur les coûts d'exploitation en reais."],
        ["Croissance du PIB", "environ 1,9 à 2 %", "Marché intérieur vaste mais croissance modérée ; la demande sectorielle tient à des moteurs structurels."],
        ["Dollar en fin d'année", "environ 5,20 reais", "Risque de change réel pour un investisseur en euros (revenus en reais, capital en euros)."],
    ], [38, 34, 102], taille=8.5)
    pdf.para("Sources : bulletin Focus de la Banque centrale (juin à août 2026) relayé par la presse brésilienne ; les relevés de semaines différentes "
             "divergent légèrement.", taille=8, italique=True)

    pdf.titre1("3. Secteurs à forte demande")
    pdf.tableau(["Secteur", "Moteur de la demande", "Repères chiffrés", "Ticket et barrières", "Compat. /5"], [
        ["Solaire distribué", "Facture d'électricité élevée, compensation d'énergie (loi 14.300), toitures et parcs à distance.",
         "De moins de 1 GW (2018) à 40 GW (juin 2025) : 43 % des ajouts de capacité (EIA, d'après l'ANEEL). 99 % de la production distribuée est solaire.",
         "Quelques centaines de k€ à quelques M€. Barrières : raccordement, redevance réseau croissante jusqu'en 2029, concurrence.", "4"],
        ["Stockage par batteries", "Écrêtement (curtailment) en hausse, première enchère de capacité.",
         "Environ 2 GW mis aux enchères, systèmes d'au moins 30 MW, fourniture dès août 2028, calendrier repoussé ; environ 18 GW de projets prêts.",
         "Dizaines de M€ par projet : hors de portée en direct ; accessible seulement en amont ou en aval (intégration, services).", "2"],
        ["Centres de données", "IA, nuage, souveraineté des données.",
         "Environ 114 Md US$ d'investissements annoncés pour 2026 (Brasscom, via la presse) ; pénurie de main-d'œuvre qualifiée.",
         "Ticket de plusieurs centaines de M€ ; barrière technique et énergétique.", "1"],
        ["Eau et assainissement", "Objectif légal de 99 % d'eau potable et 90 % d'égouts en 2033 (prorogeable jusqu'en 2040).",
         "Environ 64,6 Md R$ de concessions et PPP signés ; environ 130 Md R$ avec la privatisation de la Sabesp. Besoins estimés de 120 à plus de 700 Md R$ selon les sources.",
         "Concessions publiques : fonds spécialisés ; sous-traitance locale possible. Sources peu récentes.", "1"],
        ["Logistique et infrastructures (PPP)", "Goulots ferroviaires et routiers ; programmes de partenariats public-privé.",
         "Fort besoin, peu de chiffres récents trouvés.", "Concessions de grande taille ; fonds ou coentreprises.", "2"],
        ["Agro-industrie", "Premier exportateur agricole : demande de transformation, de stockage, de froid.",
         "Aucune source récente exploitable dans cette passe.", "Non évalué : à approfondir en portugais.", "—"],
    ], [26, 38, 50, 44, 16], taille=8)
    pdf.para("« Compat. » = compatibilité avec le profil ci-dessus (ticket accessible, gestion à distance, absence de mandat exécutif). Le Brésil "
             "aurait reçu le plus de capitaux étrangers d'Amérique latine en 2025 (agrégateur, à vérifier).", taille=8, italique=True)

    pdf.titre1("4. Focus : le solaire distribué")
    pdf.puces([
        "Parc de génération à distance : un parc de quelques centaines de kW à quelques MW injecte sur le réseau, des consommateurs (commerces, PME, "
        "particuliers) reçoivent des crédits d'énergie ; revenus par abonnement ou location de la capacité.",
        "Toitures commerciales et industrielles : vente ou location d'installations chez le client (PPA ou crédit).",
        "Exploitation et maintenance : services récurrents sur des parcs existants, avec un faible besoin de capital.",
        "Cadre : loi 14.300 de 2022, compensation jusqu'à 5 MW, redevance de réseau qui monte de 2023 à 2029 (plein tarif ensuite), droits acquis "
        "jusqu'en 2045 pour les installations de moins de 5 MW selon la presse spécialisée. La rentabilité reste jugée élevée mais se resserre.",
    ], taille=9.5)

    pdf.titre1("5. Cadre pour un non-résident")
    pdf.tableau(["Point", "Repère (sources secondaires)"], [
        ["Forme sociale", "Société à responsabilité limitée (LTDA) ou société de projet ; 100 % de détention étrangère en général possible, sauf secteurs restreints."],
        ["Numéro fiscal", "CPF obligatoire pour chaque associé personne physique, CNPJ pour la société après l'immatriculation."],
        ["Représentation", "Administrateur ou représentant résidant au Brésil (ou procurateur provisoire) : William ne peut pas l'être."],
        ["Capital étranger", "À enregistrer auprès de la Banque centrale (RDE-IED) ; sans cela, pas de rapatriement des bénéfices."],
        ["Capital minimum", "Sources divergentes (aucun minimum fixe ou un montant non confirmé) : à vérifier."],
        ["Dividendes", "Retenue à la source de 10 % depuis le 01/01/2026 sur tout dividende versé à un non-résident (loi 15.270/2025) ; remboursement lié aux conventions fiscales non encore réglementé selon les sources."],
        ["Fiscalité de William", "Résident fiscal en France : revenus étrangers déclarés en France ; effet de la convention France-Brésil à faire valider par un fiscaliste."],
        ["Décalage horaire", "Brésil (heure de São Paulo) : 5 heures de moins qu'au Luxembourg l'été."],
        ["Langue", "Portugais pour les contrats, l'administration et l'exploitation : un partenaire ou un conseil local bilingue est nécessaire."],
    ], [34, 140], taille=8.5)

    pdf.titre1("6. Cadre luxembourgeois (statut de fonctionnaire)")
    pdf.puces(ART14, taille=9.5)

    pdf.titre1("7. Risques principaux")
    pdf.puces([
        "Change : recettes en reais, capital en euros ; la retenue de 10 % et la fiscalité française se cumulent avec la perte éventuelle au change.",
        "Contrepartie : tout dépend du partenaire local qui construit, exploite et administre ; contrôle à distance limité.",
        "Réglementaire : redevance de réseau croissante, évolutions possibles du cadre de la génération distribuée.",
        "Juridique : lenteur judiciaire, litiges fonciers pour les parcs ; documents en portugais.",
        "Liquidité : sortie difficile d'une société de projet non cotée.",
    ], taille=9.5)

    pdf.titre1("8. Points à valider avant tout engagement")
    pdf.puces([
        "Un avocat brésilien : forme sociale, représentation, enregistrement RDE-IED, capital minimum.",
        "Un fiscaliste couvrant France, Luxembourg et Brésil : convention fiscale, déclaration des revenus, retenue de 10 %.",
        "Le partenaire local : références, projets livrés, litiges, antécédents, structure de capital, garanties de bonne exécution.",
        "Un audit technique indépendant des projets (ensoleillement, raccordement, contrats de compensation, titres fonciers).",
    ], taille=9.5)

    _fin(pdf, [
        "EIA, Today in Energy, solaire distribué au Brésil : https://www.eia.gov/todayinenergy/detail.php?id=66184",
        "CleanTechnica (26/09/2025) : https://cleantechnica.com/2025/09/26/distributed-solar-generating-capacity-is-the-fastest-growing-power-source-in-brazil/",
        "pv magazine, nouvelles règles de la génération distribuée : https://www.pv-magazine.com/?p=29302",
        "Trench Rossi, loi 14.300 : https://www.trenchrossi.com/en/legal-alerts/law-establishing-the-legal-framework-for-distributed-generation-in-the-brazilian-electricity-sector-is-enacted/",
        "pv magazine (29/10/2025) et ess-news (12/06/2026), enchère de stockage : https://www.pv-magazine.com/2025/10/29/brazil-eyes-april-2026-for-first-battery-storage-auction/",
        "Paraíba Business, centres de données (Brasscom) : https://paraibabusiness.com.br/investimentos-em-data-centers-devem-alcancar-us-114-bilhoes-no-brasil-em-2026/",
        "Diário do Comércio, marco legal do saneamento : https://diariodocomercio.com.br/especial-sme/engenharia-hoje-marco-legal-gera-otimismo-e-duvidas/",
        "Guides de création de société au Brésil (non officiels) : https://www.commenda.io/blog/incorporate-in-brazil · https://establishbrazil.com/faq/company-formation",
        "Loi 15.270/2025, dividendes : https://jornalcontabil.com.br/noticia/lei-15-270-define-regras-para-taxacao-de-lucros-e-dividendos-a-partir-de-2026/",
        "Banque centrale du Brésil, bulletin Focus (relais de presse) : https://www.infomoney.com.br/?p=3335666",
    ], [
        "Les chiffres sont des repères de 2025-2026 ; les séries plus récentes ne sont pas reprises et rien n'est extrapolé jusqu'en 2041.",
        "Plusieurs sources sont des guides ou des blogs : le capital minimum, la retenue sur les dividendes et le traitement conventionnel sont à confirmer par un professionnel.",
        "Aucun partenaire, aucun projet, aucun prix de parc n'a été examiné : ce rapport cartographie des secteurs, pas des opportunités précises.",
    ])
    pdf.sauver(chemin("documents_william", "2041-07-16_Étude_IA_Brésil_Opportunités.pdf"))


def cote_ivoire():
    pdf = DocPDF("Opportunités d'investissement et de projets — Côte d'Ivoire",
                 "Rapport n° 2 de l'agent IA de William Ossimi · mardi 16 juillet 2041, 10h34", auteur=AUTEUR,
                 pied="Agent IA de William Ossimi — Côte d'Ivoire")
    pdf.meta("Question posée", "Secteurs à forte demande où un projet peut être lancé ou financé, après le Brésil : la Côte d'Ivoire.")
    pdf.meta("Base", "Séries publiques 2025-2026 recoupées (7 recherches, sources en fin de document).")
    pdf.para(PROFIL, taille=9, italique=True)

    pdf.titre1("1. Synthèse")
    pdf.puces([
        "Économie en forte croissance (environ 6 à 6,7 % par an), inflation très basse, programme du FMI achevé, risque de surendettement jugé faible : "
        "le contexte est plus stable que celui du Brésil, et le franc CFA est à parité fixe avec l'euro (655,957 FCFA pour 1 €), donc sans risque de change pour un investisseur en euros.",
        "Secteurs les mieux documentés : transformation agro-industrielle (anacarde, cacao), énergie solaire, logement abordable. Les paiements "
        "mobiles sont dominés par de grands opérateurs : peu de place pour un petit investisseur.",
        "Une création de société est annoncée en 24 à 72 heures au guichet unique du CEPICI, mais les frais et les exigences pour un associé étranger "
        "ne sont documentés que par des sources non officielles.",
        "Trous du rapport : santé, éducation, distribution et services aux entreprises ne sont pas couverts ; le taux de broyage du cacao en 2025 n'est pas confirmé.",
    ], taille=9.5)

    pdf.titre1("2. Contexte macroéconomique (repères 2025-2026)")
    pdf.tableau(["Indicateur", "Repère", "Lecture"], [
        ["Croissance du PIB", "environ 6,5 % en 2025 ; 6 à 6,7 % en 2026 (FMI, gouvernement)", "Demande intérieure et investissement publics soutenus."],
        ["Inflation", "environ 0,1 % en 2025 ; 1,5 à 3,3 % en 2026 selon les sources", "Coûts maîtrisés ; la hausse attendue vient de l'alimentation et de l'énergie."],
        ["Finances publiques", "déficit d'environ 3 % du PIB en 2025 ; risque de surendettement faible", "Programme du FMI achevé en 2026 ; marge pour les concessions et partenariats."],
        ["Investissements privés agréés (CEPICI)", "812,67 Md FCFA en 2025 (+9,6 %) ; 4 242 Md sur 2021-2025, soit 66 % de l'objectif de 6 400 Md", "Les services, l'industrie et l'agriculture en bénéficient ; l'agro-industrie a reçu 169 Md FCFA en 2024."],
        ["Monnaie", "1 € = 655,957 FCFA (parité fixe)", "Aucun risque de change entre l'euro et le FCFA ; risque de convertibilité faible."],
    ], [38, 62, 74], taille=8.5)

    pdf.titre1("3. Secteurs à forte demande")
    pdf.tableau(["Secteur", "Moteur de la demande", "Repères chiffrés", "Ticket et barrières", "Compat. /5"], [
        ["Transformation de l'anacarde", "Politique de valorisation locale ; objectif de plus de 50 % transformé en 2030.",
         "Taux de transformation d'environ 43 % en 2025 (2 % en 2011) ; 659 579 t livrées aux usiniers nationaux contre 344 026 t en 2024 ; environ 37 usines, près de 20 000 emplois.",
         "Usine ou coentreprise : de quelques M€ à plusieurs dizaines de M€ ; besoin de gestion industrielle et d'accès à la matière première.", "3"],
        ["Transformation du cacao", "Valeur ajoutée locale, usines de broyage.",
         "Usine Transcao PK24 inaugurée le 26/06/2025 : 100 000 t par an, jusqu'à 210 000 t. Taux de broyage 2025 non confirmé.",
         "Très capitalistique ; acteurs établis ; entrée possible par participation minoritaire ou services.", "2"],
        ["Énergie solaire", "Plan d'urgence énergétique 2026-2030 (925 MW solaires visés) ; 45 % de renouvelables en 2030.",
         "Ferké Solar 52 MWc (juillet 2026, environ 41 Md FCFA) ; Kong 50 MW (1er trim. 2027) ; Dabakala et Niakaramandougou 2 × 100 MW avec stockage en appel d'offres ; électrification d'environ 94 % (2024).",
         "Grandes centrales en concession de 25 ans : tickets de dizaines de M€. Petite autoproduction industrielle : non documentée.", "3"],
        ["Logement abordable", "Déficit cumulé estimé à 800 000 à 830 000 logements ; Abidjan à 5,6 M d'habitants (2021).",
         "Programme d'urgence de 25 000 logements sociaux (juillet 2024), objectif de 150 000 d'ici 2030 ; prêt de la SFI de 27 M$ à Addoha CIV pour 5 600 logements.",
         "Promotion immobilière : foncier, permis, ventes sur plans ; tensions sur le foncier urbain relayées par la presse (2025).", "3"],
        ["Paiements mobiles et fintech", "Inclusion financière, transferts, paiements marchands.",
         "Plus de 25 M d'abonnés (2023) ; Orange Money 13,83 M, MTN MoMo 8,46 M, Moov Money 2,87 M ; Wave Bank Africa lancée en octobre 2025.",
         "Licences, capitaux et acteurs dominants : marché fermé aux petits acteurs.", "1"],
    ], [26, 38, 52, 42, 16], taille=8)
    pdf.para("« Compat. » = compatibilité avec le profil ci-dessus (ticket accessible, gestion à distance, absence de mandat exécutif).", taille=8, italique=True)

    pdf.titre1("4. Cadre pour un non-résident")
    pdf.tableau(["Point", "Repère (sources non officielles)"], [
        ["Forme sociale", "SARL ou SAS de droit OHADA (acte uniforme sur les sociétés commerciales, révisé en 2014)."],
        ["Procédure", "Guichet unique du CEPICI, en ligne depuis 2012 ; délai annoncé de 24 à 72 heures pour une SARL."],
        ["Frais", "De 30 000 à 150 000 FCFA selon les sources (soit environ 46 à 229 €) ; succursale étrangère plus chère et plus longue."],
        ["Capital", "Libre ; les sources citent de 1 FCFA symbolique à 100 000 FCFA : à confirmer."],
        ["Associé étranger", "Exigences spécifiques (autorisations, résidence) non documentées par les sources consultées : à demander au CEPICI."],
        ["Gérant", "Une SARL a un gérant : il sera local, William ne peut pas l'être (article 14)."],
        ["Décalage horaire", "Abidjan : 2 heures de moins qu'au Luxembourg l'été."],
        ["Langue", "Français : aucune barrière linguistique pour William."],
    ], [34, 140], taille=8.5)

    pdf.titre1("5. Cadre luxembourgeois (statut de fonctionnaire)")
    pdf.puces(ART14, taille=9.5)

    pdf.titre1("6. Comparaison avec le Brésil")
    pdf.tableau(["Critère", "Brésil (rapport n° 1)", "Côte d'Ivoire"], [
        ["Change", "Reais ; risque de change réel", "FCFA à parité fixe avec l'euro"],
        ["Coût du crédit local", "Selic d'environ 14 %", "Faible inflation ; coût du crédit non documenté dans cette passe"],
        ["Taille et croissance", "Grand marché, croissance d'environ 2 %", "Marché plus petit, croissance d'environ 6 %"],
        ["Fiscalité des dividendes", "Retenue de 10 % pour les non-résidents (2026)", "Non documentée dans cette passe"],
        ["Création de société", "Procédure plus lourde : CPF, représentant résident, enregistrement du capital", "Guichet unique en ligne annoncé en 24 à 72 h"],
        ["Langue", "Portugais", "Français"],
        ["Décalage horaire", "5 heures de moins", "2 heures de moins"],
        ["Documentation du dossier", "Solaire distribué très documenté", "Agro-industrie, énergie et logement documentés"],
    ], [38, 68, 68], taille=8.5)

    pdf.titre1("7. Risques principaux")
    pdf.puces([
        "Foncier : titres contestés, tensions sur le foncier urbain (presse, 2025) ; indispensable pour le logement et les usines.",
        "Concentration : économie très exposée au cacao, à l'anacarde et aux cours mondiaux.",
        "Climat et sécurité régionale : signalés par le FMI comme vulnérabilités.",
        "Contrepartie : gestion locale à distance, sans mandat exécutif de William ; qualité du partenaire déterminante.",
        "Juridique : sources de procédure non officielles ; délais réels souvent supérieurs aux délais annoncés.",
    ], taille=9.5)

    pdf.titre1("8. Points à valider avant tout engagement")
    pdf.puces([
        "Le CEPICI : frais officiels, exigences pour un associé étranger, régimes d'agrément.",
        "Un avocat ou notaire à Abidjan : statuts OHADA, pacte d'associés, clauses de sortie.",
        "Un fiscaliste France-Luxembourg-Côte d'Ivoire : traitement des revenus et de la convention fiscale.",
        "Le partenaire local : références, projets livrés, litiges, antécédents, structure de capital.",
        "L'état du foncier et des permis pour tout projet immobilier ou industriel.",
    ], taille=9.5)

    _fin(pdf, [
        "CEPICI, bilan 2025 : https://fr.allafrica.com/stories/202602200622.html · https://economie-ivoirienne.ci/actualites/attractivite-economique-81267-milliards-fcfa-dinvestissements-prives-agrees-par-le",
        "Ecofin Agency, investissements agréés en 2025 : https://www.ecofinagency.com/news/2002-53132-cote-divoire-approved-private-investment-rises-9-6-to-1-45-billion-in-2025",
        "FMI et Trésor ivoirien, perspectives 2026 : https://economie-ivoirienne.ci/actualites/cote-divoire-cap-sur-une-croissance-de-67-en-2026-dans-un-cadre-macroeconomique",
        "Filière anacarde : https://fr.allafrica.com/stories/202601200594.html · https://connectionivoirienne.net/2026/06/22/filiere-anacarde-le-gouvernement-poursuit-la-valorisation-locale-pour-renforcer-les-revenus-des-acteurs/",
        "Usine Transcao PK24 : https://www.afrique-sur7.fr/nouvelle-usine-de-cacao-a-abidjan-la-cote-divoire-poursuit-sa-mue-industrielle",
        "Centrales solaires : https://www.ecofinagency.com/news/0607-57093-cote-divoire-commissions-71-million-solar-plant-to-expand-clean-energy · https://www.ecofinagency.com/news-industry/0406-47136-cote-d-ivoire-opens-bidding-for-200-mw-solar-projects-with-storage",
        "Logement : https://afrique.le360.ma/economie/cote-divoire-prix-prohibitifs-offre-insuffisante-lacces-au-logement-un-veritable-calvaire_MY4EMSFVYBAPBO4RK7ZDYPOFWI/ · https://connectionivoirienne.net/2025/03/12/en-plein-scandale-du-foncier-urbain-la-sfi-annonce-le-financement-dun-nouveau-projet-immobilier-en-cote-divoire/",
        "Paiements mobiles : https://www.ecofinagency.com/news-finances/2610-49842-wave-launches-commercial-bank-in-cote-d-ivoire · https://www.afrique-sur7.fr/fintech-afrique-orange-money-2026",
        "Création de société (guides non officiels) : https://africarrieres.com/cote-divoire/fr/guide/employeur-entreprise/creer-entreprise · kolonell.com (blog, guide CEPICI 2026)",
    ], [
        "Les chiffres sont des repères de 2025-2026 ; les séries plus récentes ne sont pas reprises et rien n'est extrapolé jusqu'en 2041.",
        "La fiscalité des dividendes, le coût du crédit et les exigences pour un associé étranger ne sont pas documentés par des sources officielles.",
        "Aucun partenaire, aucun projet, aucun prix d'usine ou de programme n'a été examiné : ce rapport cartographie des secteurs, pas des opportunités précises.",
    ])
    pdf.sauver(chemin("documents_william", "2041-07-16_Étude_IA_Côte_d_Ivoire_Opportunités.pdf"))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "bresil":
        bresil()
    elif cmd == "cote-ivoire":
        cote_ivoire()
    else:
        sys.exit(__doc__)
