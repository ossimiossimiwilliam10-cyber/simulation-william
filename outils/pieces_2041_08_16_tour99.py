"""
Génération des pièces officielles du vendredi 16 août 2041, 22h30 (Tour n° 99) :
1. Courriel officiel de Mohamed Coulibaly : Confirmation visite villa Vallons samedi matin, refus net d'exposition directe de William et cadrage de la sous-traitance technique
2. Note d'audit stratégique et de gouvernance de l'équipe virtuelle : Revue des projections 5 ans, contrôle des risques de long terme et validation de l'étanchéité patrimoniale
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_coulibaly_partenariats():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Cadrage Opérationnel : Visite du QG & Partenariats Techniques",
        auteur="Mohamed Coulibaly",
        pied="Visite QG & Sous-traitance technique — SOLEIL B2B CI — 16/08/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly, Directeur Général (m.coulibaly@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Vendredi 16 août 2041, 18h45 (heure d'Abidjan)")
    pdf.meta("Objet", "Organisation de la visite de la Villa des Vallons et doctrine sur la sous-traitance technique")
    pdf.ln(3)

    pdf.titre1("1. Visite de la Villa des Vallons — Samedi 17 août à 10h00")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "C'est avec un très grand plaisir que je prends note de votre disponibilité pour demain, samedi 17 août en matinée. "
        "Je vous donne rendez-vous à 10h00 précises devant la villa aux Deux-Plateaux Vallons. J'aurai en ma possession les clés "
        "officielles remises cet après-midi par le mandataire du bailleur, ainsi que les plans d'aménagement intérieur. "
        "Nous pourrons parcourir sereinement les sept pièces, tester le raccordement électrique, inspecter l'emplacement du groupe électrogène de 45 kVA "
        "et valider ensemble la répartition spatiale prévisionnelle des différentes directions."
    )

    pdf.titre1("2. Refus formel d'exposition directe de l'Associé Unique")
    pdf.para(
        "Concernant votre proposition de prendre directement contact avec des équipes techniques ou des sous-traitants pour soulager ma charge : "
        "je vous remercie infiniment pour votre prévenance et votre bienveillance à mon égard. Cependant, je me dois d'opposer un refus net et catégorique "
        "à ce que vous vous exposiez ainsi en première ligne sur le terrain à Abidjan."
    )
    pdf.para(
        "En tant que Directeur Général et mandataire social de SOLEIL B2B CÔTE D'IVOIRE SASU, il relève de ma mission stricte et exclusive d'engager "
        "les pourparlers opérationnels. Si vous intervenez en personne auprès d'installateurs locaux sans disposer d'un mandat social déposé au Greffe, "
        "nous créons un précédent préjudiciable : cela brouille la chaîne de commandement vis-à-vis des acteurs du BTP ivoirien, expose inutilement "
        "votre personne à des intermédiaires peu scrupuleux, et risque d'affaiblir l'étanchéité juridique de votre statut d'associé non-gérant. "
        "Je ne vous transmettrai donc aucun contact pour des démarches directes : c'est à moi de porter cette charge, et je l'assume pleinement."
    )

    pdf.titre1("3. Doctrine sur la sous-traitance et situation du Directeur Technique")
    pdf.para(
        "Votre vision stratégique sur le recours à des partenaires installateurs locaux est parfaitement juste : dans notre modèle de déploiement "
        "solaire B2B, l'externalisation de la pose de toiture et du tirage de câbles à des prestataires qualifiés permet d'absorber les pics d'activité "
        "sans alourdir inutilement notre masse salariale fixe. C'est le modèle que j'ai toujours préconisé."
    )
    pdf.para(
        "Concernant notre futur Directeur Technique, Monsieur Éric Koffi Yao : il est actuellement lié par son contrat de travail et ses obligations "
        "de préavis jusqu'au 31 août. Il ne peut donc en aucun cas signer d'acte, ni représenter officiellement SOLEIL B2B CI avant sa prise de fonction "
        "le 1er septembre, sous peine de poursuites pour débauchage ou concurrence déloyale de la part de son employeur actuel. "
        "En revanche, je prends l'initiative de le sonder de manière informelle dès ce week-end afin qu'il nous dresse une cartographie confidentielle "
        "des 3 à 4 meilleures entreprises d'installation photovoltaïque d'Abidjan disposant des habilitations haute/basse tension et des assurances décennales. "
        "Dès le 1er septembre, Éric Yao mènera les audits techniques sous mon autorité, et je vous présenterai les accords-cadres pour validation."
    )

    sortie = chemin("courriels", "2041-08-16_Courriel_Mohamed_Coulibaly_Refus_Negociation_Directe_et_Partenariats_Techniques.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


def generer_note_audit_strategique():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Audit Stratégique de Gouvernance, Modélisation des Risques & Stress-Test à 5 Ans",
        auteur="Équipe Virtuelle de Gestion — Pôles Juridique, Financier & Direction",
        pied="Audit Stratégique & Risques Long Terme — 16/08/2041"
    )

    pdf.meta("Émetteur", "Équipe Virtuelle de Supervision (Direction Générale, Juridique, Quantitatif/DAF, RH)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Date et heure", "Vendredi 16 août 2041, 21h30 (heure de Luxembourg / Abidjan)")
    pdf.meta("Objet", "Revue critique d'alignement, contrôle d'absence d'erreurs structurelles et plan de sécurisation à long terme")
    pdf.ln(3)

    pdf.titre1("1. Bilan d'exécution de la semaine d'amorçage : Une trajectoire sans faute")
    pdf.para(
        "À l'issue de cette première semaine d'implantation opérationnelle à Abidjan, l'équipe virtuelle a mené une revue intégrale "
        "de tous les actes, contrats, mouvements financiers et engagements souscrits par William Ossimi et pour le compte de la société en constitution. "
        "Le constat est sans équivoque : la trajectoire d'exécution est optimale, aucune faille juridique n'est décelée, et aucun dérapage budgétaire n'est à déplorer."
    )

    entetes_bilan = ["Domaine audité", "Statut d'exécution", "Niveau de conformité"]
    lignes_bilan = [
        ["Forme sociale (SASU)", "Statuts notariés signés Me Gnamien (13/08)", "100 % Conforme OHADA"],
        ["Immatriculation RCCM", "Dépôt CEPICI effectué, formalités validées", "100 % Sécurisé"],
        ["Compte bancaire d'exploitation", "Compte SGCI Plateau ouvert et activé", "100 % Opérationnel"],
        ["Financement initial CCA", "8 000 EUR (5,25 M FCFA) virés le 16/08", "Convention CCA active"],
        ["Implantation Siège Social", "Bail commercial Villa Vallons signé 16/08", "Franchise 15j obtenue"],
        ["Comité de Direction (Niveau 2)", "DG, DAF, DT, DC sélectionnés (> 80/100)", "Élite complète"]
    ]
    pdf.tableau(entetes_bilan, lignes_bilan, [60, 80, 50])

    pdf.ln(3)
    pdf.titre1("2. Audit juridique & Gouvernance : L'erreur d'immixtion évitée")
    pdf.para(
        "Le Pôle Juridique virtuel valide sans réserve la réaction de refus opposée par Mohamed Coulibaly ce vendredi soir. "
        "Dans la doctrine de gouvernance sous l'égide de l'Article 14 du statut général des fonctionnaires luxembourgeois, "
        "William Ossimi doit impérativement préserver sa stricte qualité d'associé unique investisseur, passif vis-à-vis des tiers. "
        "Toute négociation commerciale directe de William sur le terrain ivoirien avec des sous-traitants aurait constitué une gestion de fait, "
        "ouvrant un risque juridique majeur. En refusant d'exposer son associé et en sanctuarisant la ligne hiérarchique, Mohamed Coulibaly "
        "prouve sa maturité managériale et son parfait alignement avec les intérêts de protection patrimoniale du fondateur."
    )

    pdf.titre1("3. Modélisation quantitative & Stress-Test des flux de trésorerie")
    pdf.para(
        "Le Pôle Financier et Modélisation Quantitative a réévalué le plan de trésorerie à 5 ans au regard de la situation réelle :"
    )
    pdf.para(
        "- Trésorerie personnelle de William : Reconstituée à 8 243,99 EUR sur le compte courant Spuerkeess, avec 67 982,00 EUR de liquidités "
        "en épargne projet et 676 135,00 EUR sur l'ETF Monde (générant en moyenne 7 % annualisés). La trésorerie personnelle est totalement étanche "
        "et capable d'absorber toute dépense imprévue sans débouclage de positions boursières."
    )
    pdf.para(
        "- Trésorerie de démarrage SOLEIL B2B CI : Les 5 247 656 FCFA apportés en CCA couvrent largement les frais d'installation préliminaires, "
        "les acomptes de raccordement et les fournitures de base. Le besoin de décaissement du solde du prêt d'associé (jusqu'à 43 M FCFA) "
        "sera échelonné en fonction des devis réels d'aménagement retenus par Mohamed Coulibaly."
    )
    pdf.para(
        "- Point de vigilance capital (Risque de crédit client) : Dans le modèle PPA (Power Purchase Agreement), le risque principal réside dans "
        "le délai de recouvrement auprès des PME/PMI industrielles locales. L'Analyste Quantitatif recommande d'intégrer dans le manuel des procédures "
        "de Viviane Tanoh (DC) et Mariam Brou (DAF) trois verrous absolus : 1. Dépôt de garantie ou caution bancaire de 3 mois de facturation ; "
        "2. Clause de réserve de propriété stricte sur les onduleurs et panneaux solaires ; 3. Dispositif de coupure et bridage à distance par télégestion GSM."
    )

    pdf.titre1("4. Recommandations prioritaires pour les prochaines étapes")
    pdf.para(
        "1. Samedi 17 août (10h00) : Visite de la villa des Vallons avec Mohamed Coulibaly. Se concentrer sur l'inspection physique des lieux, "
        "la sécurité du périmètre et l'évaluation visuelle des travaux de rafraîchissement sans donner d'ordres directs aux artisans."
    )
    pdf.para(
        "2. Dimanche 18 août : Repos et récupération physique. Aucune sollicitation des équipes opérationnelles."
    )
    pdf.para(
        "3. Semaine du 19 au 23 août : Suivi par l'application Gestion de la mise en concurrence des devis d'aménagement par Coulibaly, "
        "et cadrage par Mariam Brou de la fiche de poste de l'Analyste Quantitatif (Niveau 3) pour lancement du sourcing début septembre."
    )

    sortie = chemin("documents_william", "2041-08-16_Note_Audit_Strategique_Gouvernance_et_Projections_5_Ans.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_courriel_coulibaly_partenariats()
    generer_note_audit_strategique()
