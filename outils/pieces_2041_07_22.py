"""PIÈCES DU 22/07/2041 (univers 3, tour n° 42) :
1. Rapport quotidien du Directeur Général virtuel (22 juillet 2041, 20h00) ;
2. Maquette de la Convention de Mandat Social du Directeur Général (22 juillet 2041, 21h15),
   intégrant les 4 arbitrages de William et la transposition des 17 clauses contractuelles.

Génération de vrais fichiers PDF (règle 4 du fichier maître et consigne de William du 22/07/2041)
déposés dans `documents_william/` et consultables dans l'application Gestion / Fichiers du téléphone.
"""
import sys
from pathlib import Path

# Assure l'import de pdf_base
RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_rapport_quotidien():
    pdf = DocPDF(
        "Rapport quotidien d'activité — Direction Générale virtuelle",
        "Lundi 22 juillet 2041 · 20h00 (heure de Luxembourg / 18h00 Abidjan)",
        auteur="Directeur Général virtuel",
        pied="Projet Solaire B2B Abidjan — Rapport d'activité du 22/07/2041"
    )
    
    pdf.meta("Émetteur", "Directeur Général virtuel (Pôle Central / Architecture IA)")
    pdf.meta("Destinataire", "William Ossimi, Associé unique et investisseur")
    pdf.meta("Date et heure", "Lundi 22 juillet 2041, 20h00")
    pdf.meta("Objet", "Rapport de situation quotidien : candidatures, cadrage juridique, budget et arbitrages")
    pdf.ln(3)

    pdf.titre1("1. Synthèse de la journée du 22 juillet 2041")
    pdf.para(
        "La journée a été marquée par la consolidation des candidatures de direction générale, la réception du devis "
        "définitif du cabinet d'avocats à Abidjan et le lancement des arbitrages sur la convention de mandat social."
    )

    pdf.titre1("2. Pôle Ressources Humaines : Recrutement de la Direction Générale")
    pdf.para(
        "Le vivier de candidatures issues des plateformes Educarriere.ci, NovoJob, LinkedIn et réseaux professionnels "
        "a été resserré autour des profils élite ayant obtenu une note égale ou supérieure à 70/100 :"
    )
    pdf.puces([
        "Mohamed Coulibaly (note 91/100) : profil ingénieur d'élite, directeur de projets énergétiques solaires. "
        "Courriels officiels adressés à ses deux référents professionnels (DG filiale multinationale et Directeur "
        "des Opérations) pour recueil de la grille d'évaluation.",
        "Mariam Brou (note 88/100) : directrice commerciale B2B dans le secteur des équipements industriels et de l'énergie. "
        "Prises de contact en cours avec ses référents professionnels par le pôle RH.",
        "Kader Assi (note 84/100) : ingénieur d'affaires senior. A transmis ce matin les coordonnées de ses deux références ; "
        "projet présenté sous l'intitulé « Projet Solaire B2B Abidjan ».",
        "Jean-Baptiste Tuo (note 71/100) : suite à la survenue de profils d'un niveau supérieur, l'entretien téléphonique prévu "
        "le 26/07 a été annulé avec courtoisie sur WhatsApp. Son dossier est classé en réserve active."
    ])

    pdf.titre1("3. Pôle Juridique : Conseil et constitution de société à Abidjan")
    pdf.para(
        "Le Cabinet de Me Ismaël Gnamien a transmis sa proposition de services formalisée à hauteur de 2 100 000 FCFA HT "
        "(environ 3 200 €), incluant la rédaction intégrale des statuts de SAS, le pacte d'associés, l'immatriculation au RCCM, "
        "la déclaration fiscale d'existence, la publication au Journal Officiel et la rédaction de la convention de mandat social du DG."
    )
    pdf.para(
        "Ce devis a été formellement validé par William ce soir à 20h02. William a été introduit comme associé majoritaire et "
        "investisseur unique (contact +352), dans le respect strict de l'article 14 du statut de la fonction publique luxembourgeoise."
    )

    pdf.titre1("4. Sécurité opérationnelle et gouvernance")
    pdf.para(
        "Une tentative de smishing (faux SMS de livraison de colis) reçue à 19h42 sur le terminal privé de William a été "
        "immédiatement bloquée et supprimée, confirmant l'étanchéité des canaux de communication du projet."
    )

    pdf.titre1("5. Consommation d'API et budget du segment virtuel")
    pdf.para(
        "La consommation d'API pour le pilotage des agents virtuels (Pôle RH, Juridique et Agent Central) s'établit à 32,61 € "
        "sur le plafond mensuel de 1 000,00 €, laissant un solde disponible de 967,39 € pour le mois de juillet 2041."
    )

    fichier_sortie = chemin("documents_william", "2041-07-22_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(fichier_sortie)
    return fichier_sortie


def generer_maquette_mandat_dg():
    pdf = DocPDF(
        "Convention de Mandat Social de Directeur Général — Maquette type",
        "Société par Actions Simplifiée (SAS) de droit OHADA en cours de constitution · Abidjan (RCI)",
        auteur="Pôle Juridique virtuel & Direction Générale",
        pied="Projet Solaire B2B Abidjan — Maquette Convention Mandat Social DG"
    )

    pdf.meta("Nature de l'acte", "Convention de Mandat Social de Directeur Général (organe exécutif)")
    pdf.meta("Cadre juridique", "Acte Uniforme OHADA sur les Sociétés Commerciales et le GIE")
    pdf.meta("Associé unique", "William Ossimi (Investisseur / Associé non-gérant)")
    pdf.meta("Bénéficiaire", "Candidat sélectionné à la Direction Générale (Mohamed Coulibaly / Mariam Brou)")
    pdf.meta("Date de validation", "Lundi 22 juillet 2041, 21h15")
    pdf.ln(3)

    pdf.titre1("Préambule et architecture générale des contrats d'entreprise")
    pdf.para(
        "La présente convention fixe les règles d'exercice, de rémunération, d'objectifs et de protection relatives au "
        "Directeur Général de la SAS en formation. Elle constitue le Contrat de Niveau 1 (Direction Générale), mis en place "
        "directement par l'associé unique."
    )
    pdf.para(
        "L'organisation contractuelle de la société s'établit selon une gouvernance en trois paliers hiérarchiques distincts :"
    )
    pdf.puces([
        "Contrat de Niveau 1 (Directeur Général) : Mandat social pur de droit des sociétés commerciales (OHADA), exclusif de "
        "tout lien de subordination salarié, conclu entre l'associé unique et le Directeur Général.",
        "Contrats de Niveau 2 (Directeurs de pôle) : Contrats de travail de cadres dirigeants salariés régis par le Code du travail "
        "ivoirien (Technique, Commercial, Administratif et Financier), rédigés selon une maquette générale soumise par le Directeur "
        "Général à l'associé unique.",
        "Contrats de Niveau 3 (Collaborateurs et techniciens) : Contrats de travail salariés d'exécution (techniciens solaires toiture, "
        "commerciaux terrain, monteurs), rédigés selon des maquettes propres élaborées par chaque directeur de pôle selon les impératifs de son métier."
    ])

    pdf.titre1("Article 1 — Désignation, prise de fonction et limitations des pouvoirs")
    pdf.para(
        "Le Directeur Général est nommé par décision de l'associé unique. Il assure la direction opérationnelle et commerciale "
        "de la société et dispose des pouvoirs de représentation générale vis-à-vis des tiers, sous réserve expresse des limitations "
        "statutaires suivantes requérant l'accord écrit préalable de l'associé unique :"
    )
    pdf.puces([
        "Tout investissement unitaire, achat d'actif ou engagement financier supérieur à 10 000 000 FCFA HT ;",
        "Toute souscription d'emprunt bancaire, facilité de caisse, aval, caution ou garantie accordée par la société ;",
        "La conclusion, résiliation ou cession de tout bail commercial portant sur les locaux de la société ;",
        "Le recrutement, la fixation de rémunération ou le licenciement des directeurs de pôle (cadres C-level) ;",
        "La conclusion d'accords stratégiques, partenariats capitalistiques ou licences technologiques exclusives."
    ])

    pdf.titre1("Article 2 — Nature juridique du mandat et exclusion du salariat")
    pdf.para(
        "Le Directeur Général exerce ses fonctions en qualité de mandataire social pur conformément aux dispositions des articles "
        "414 et suivants de l'Acte Uniforme de l'OHADA relatif au droit des sociétés commerciales et du GIE. Les parties reconnaissent "
        "expressément l'absence totale de contrat de travail et de lien de subordination juridique."
    )
    pdf.para(
        "Par dérogation volontaire et explicite aux règles du droit du travail ivoirien, le Directeur Général ne bénéficie d'aucun statut "
        "de salarié. Son mandat est révocable ad nutum par décision unilatérale de l'associé unique, sous réserve des seules stipulations "
        "de la présente convention."
    )

    pdf.titre1("Article 3 — Rémunération globale et primes de performance")
    pdf.para(
        "En contrepartie de l'exercice effectif de son mandat, le Directeur Général perçoit une rémunération structurée selon la Formule 1 incitative :"
    )
    pdf.puces([
        "Rémunération fixe mensuelle : 2 000 000 FCFA net d'impôts sur les traitements et salaires (soit environ 3 050 €), "
        "versée à terme échu le dernier jour ouvré de chaque mois civil.",
        "Rémunération variable trimestrielle : commission de 2,5 % du chiffre d'affaires hors taxes effectivement encaissé par la "
        "société sur les affaires solaires en toiture raccordées et mises en service.",
        "Prime annuelle de surperformance : prime forfaitaire de 5 000 000 FCFA versée en cas d'atteinte ou de dépassement du seuil "
        "de 500 kWc cumulés raccordés et audités sur l'exercice civil."
    ])

    pdf.titre1("Article 4 — Régime légal et inapplication des conventions collectives")
    pdf.para(
        "Compte tenu de sa qualité exclusive d'organe social de direction, le mandataire ne relève d'aucune convention collective "
        "interprofessionnelle, ni d'aucun barème de salaire salarié de branche. Ses droits et obligations sont exclusivement régis "
        "par les statuts de la SAS et les termes de la présente convention."
    )

    pdf.titre1("Article 5 — Régime social et fiscal")
    pdf.para(
        "Le mandataire social est affilié au Régime Social des Travailleurs Indépendants et dirigeants de société (CNPS RSTI) et "
        "à la Couverture Maladie Universelle (CMU) en Côte d'Ivoire. La fiscalité applicable à ses indemnités de fonction relève "
        "du régime fiscal des rémunérations de dirigeants selon le Code Général des Impôts ivoirien (ITS, CN, IGR), géré par la société."
    )

    pdf.titre1("Article 6 — Temps d'activité et engagement d'exclusivité totale")
    pdf.para(
        "Le mandataire n'est soumis à aucune réglementation sur les horaires hebdomadaires de travail (durée légale de 40 heures exclue). "
        "En contrepartie, il s'engage à consacrer l'intégralité de son temps utile, de son énergie et de ses compétences au développement "
        "de la société. Il lui est formellement interdit d'exercer toute autre activité professionnelle, salariée, libérale ou de conseil, "
        "ou de détenir un quelconque autre mandat social sans accord exprès, préalable et écrit de l'associé unique."
    )

    pdf.titre1("Article 7 — Gouvernance d'entreprise, éthique et conformité")
    pdf.para(
        "Le Directeur Général est chargé d'édicter le règlement intérieur de l'entreprise, sous validation de l'associé unique, et d'en "
        "assurer la rigoureuse application auprès du personnel. Il garantit la conformité stricte de l'ensemble des opérations aux "
        "lois ivoiriennes, aux normes techniques de sécurité des chantiers photovoltaïques et aux règles internationales anti-corruption."
    )

    pdf.titre1("Article 8 — Périodes de repos rémunérées du dirigeant")
    pdf.para(
        "Le Directeur Général bénéficie d'un crédit annuel forfaitaire de 30 jours calendaires de repos rémunéré. Les dates de prise "
        "de ces périodes doivent être notifiées au moins 15 jours à l'avance à l'associé unique afin de ne pas compromettre la marche "
        "des affaires, les livraisons de chantiers solaires et les clôtures commerciales."
    )

    pdf.titre1("Article 9 — Frais de représentation, mobilité et dotation matérielle")
    pdf.para(
        "La société prend en charge l'ensemble des dépenses nécessitées par l'exercice du mandat : remboursement des frais professionnels "
        "sur états justificatifs réguliers, mise à disposition d'un véhicule de fonction pour les déplacements professionnels sur Abidjan, "
        "d'un ordinateur portable professionnel chiffré et d'un smartphone d'entreprise avec forfait voix et données illimité."
    )

    pdf.titre1("Article 10 — Systèmes d'information, cybersécurité et confidentialité des flux")
    pdf.para(
        "Le mandataire doit faire usage exclusif de la messagerie institutionnelle et des environnements applicatifs sécurisés de la société. "
        "Il lui est strictement interdit d'extraire, copier ou stocker sur des supports personnels des fichiers clients, des devis techniques "
        "ou des bases tarifaires. Les échanges stratégiques avec l'associé unique empruntent les canaux directs validés."
    )

    pdf.titre1("Article 11 — Propriété intellectuelle et cession exclusive")
    pdf.para(
        "L'ensemble des réalisations, méthodes, études d'ingénierie solaire, dimensionnements photovoltaïques, outils de chiffrage, "
        "marques, fichiers prospects et bases de données élaborés par le Directeur Général au cours de son mandat sont la propriété "
        "exclusive, perpétuelle et universelle de la société. Le mandataire cède irrévocablement tous droits patrimoniaux afférents."
    )

    pdf.titre1("Article 12 — Formation professionnelle et maintien des habilitations")
    pdf.para(
        "La société assure la prise en charge financière des actions de formation continue nécessaires au maintien au plus haut niveau "
        "des habilitations électriques (BT/HT), des certifications techniques solaires et de la participation aux salons professionnels "
        "majeurs de la sous-région ouest-africaine."
    )

    pdf.titre1("Article 13 — Couverture santé et prévoyance complémentaire")
    pdf.para(
        "La société souscrit et finance une police d'assurance maladie-hospitalisation et prévoyance complémentaire haut de gamme "
        "(comprenant une garantie d'évacuation sanitaire d'urgence) au bénéfice du Directeur Général et de ses ayants droit légaux."
    )

    pdf.titre1("Article 14 — Droit applicable")
    pdf.para(
        "La présente convention est soumise aux règles de l'Acte Uniforme OHADA relatif au droit des sociétés commerciales et du GIE, "
        "et subsidiairement aux règles du droit civil et commercial applicable en République de Côte d'Ivoire."
    )

    pdf.titre1("Article 15 — Attribution exclusive de compétence juridictionnelle")
    pdf.para(
        "Tout litige relatif à la formation, l'exécution, l'interprétation ou la cessation de la présente convention de mandat social "
        "relève de la compétence exclusive du Tribunal de commerce d'Abidjan, à l'exclusion formelle de toute juridiction prud'homale "
        "ou du travail."
    )

    pdf.titre1("Article 16 — Protection des données à caractère personnel")
    pdf.para(
        "Le Directeur Général veille au respect strict des dispositions de la Loi ivoirienne n° 2013-450 relative à la protection des "
        "données à caractère personnel dans l'ensemble des traitements informatiques conduits par la société auprès de ses clients, "
        "partenaires et salariés."
    )

    pdf.titre1("Article 17 — Devoir de loyauté renforcé, secret des affaires et conflits d'intérêts")
    pdf.para(
        "Le mandataire est tenu à une obligation de loyauté absolue et à un secret professionnel perpétuel. Il lui est interdit de "
        "détenir des intérêts directs ou indirects chez des clients, sous-traitants, fournisseurs d'onduleurs ou panneaux solaires, ou "
        "concurrents de la société. Toute situation de conflit d'intérêts potentiel doit faire l'objet d'une divulgation écrite immédiate."
    )

    pdf.titre1("Article 18 — Objectifs de performance et clause de caducité automatique")
    pdf.para(
        "Conformément à l'Option C retenue par l'associé unique, le mandat social est subordonné à l'atteinte de paliers économiques stricts :"
    )
    pdf.puces([
        "Trimestre 1 (démarrage) : signature effective d'au moins 2 contrats d'installations solaires B2B en toiture ;",
        "Trimestre 2 et suivants : génération d'un seuil minimum de 15 000 000 FCFA de marge brute encaissée par trimestre civil.",
        "Sanction de caducité : en cas de non-atteinte de ces seuils sur deux trimestres consécutifs, le mandat social prend fin "
        "de plein droit et par le seul fait de cette défaillance constatée arithmétiquement, sans indemnité de rupture ni préavis."
    ])

    pdf.titre1("Article 19 — Clause de non-concurrence post-mandat et clause pénale")
    pdf.para(
        "Conformément à l'Option A retenue par l'associé unique, le Directeur Général s'interdit d'exercer toute activité concurrente :"
    )
    pdf.puces([
        "Périmètre matériel : interdiction d'exercer dans le secteur du solaire photovoltaïque B2B en toiture et de l'efficacité "
        "énergétique, que ce soit comme dirigeant, associé, salarié, consultant ou partenaire indépendant.",
        "Périmètre géographique et temporel : district autonome d'Abidjan pendant une durée ferme de 12 mois suivant la fin du mandat.",
        "Contrepartie financière : aucune indemnité financière post-mandat n'est due par la société (licite en droit OHADA).",
        "Clause pénale : toute infraction entraînera le paiement immédiat d'une indemnité forfaitaire égale à 12 mois de rémunération "
        "fixe (soit 24 000 000 FCFA), sans préjudice des actions judiciaires en cessation sous astreinte et des dommages et intérêts."
    ])

    fichier_sortie = chemin("documents_william", "2041-07-22_Maquette_Convention_Mandat_Social_Directeur_General.pdf")
    pdf.sauver(fichier_sortie)
    return fichier_sortie


if __name__ == "__main__":
    f1 = generer_rapport_quotidien()
    f2 = generer_maquette_mandat_dg()
    print("Génération terminée avec succès.")
