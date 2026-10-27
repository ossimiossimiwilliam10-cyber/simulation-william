"""Génération des pièces du lundi 29 juillet 2041 (tour n° 64) :
- D028 : Projet de Statuts constitutifs de la SASU « SOLEIL B2B CÔTE D'IVOIRE » rédigé par le Cabinet Gnamien
- D029 : Projet de Convention de Mandat Social du Directeur Général (Mohamed Coulibaly) rédigé par le Cabinet Gnamien
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_statuts_sasu():
    pdf = DocPDF(
        "Cabinet Me Ismaël Gnamien & Associés — Avocats à la Cour (Abidjan)",
        "Projet de Statuts Constitutifs — SASU « SOLEIL B2B CÔTE D'IVOIRE »",
        auteur="Cabinet Me Ismaël Gnamien & Associés",
        pied="Projet Statuts SASU SOLEIL B2B CÔTE D'IVOIRE — Cabinet Gnamien — 29/07/2041"
    )

    pdf.meta("Émetteur", "Cabinet Me Ismaël Gnamien & Associés, Avocat à la Cour, Barreau d'Abidjan")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Date et heure", "Lundi 29 juillet 2041, 09h00 (heure d'Abidjan / 11h00 Luxembourg)")
    pdf.meta("Objet", "Projet d'actes constitutifs : Statuts d'une Société par Actions Simplifiée Unipersonnelle")
    pdf.ln(3)

    pdf.titre1("Préambule et identité du fondateur")
    pdf.para(
        "Le soussigné, Monsieur William Ossimi, né à Audun-le-Tiche, de nationalité luxembourgeoise, "
        "demeurant professionnellement à Luxembourg et domicilié à Audun-le-Tiche (France), a établi ainsi qu'il suit "
        "les statuts constitutifs d'une Société par Actions Simplifiée Unipersonnelle régie par l'Acte uniforme de l'OHADA "
        "relatif au droit des sociétés commerciales et du groupement d'intérêt économique (AUSCGIE)."
    )

    pdf.titre1("Article 1 — Forme juridique")
    pdf.para(
        "Il est formé par l'associé unique soussigné une Société par Actions Simplifiée Unipersonnelle (SASU) régie par les "
        "dispositions légales et réglementaires de l'Acte uniforme OHADA, ainsi que par les présents statuts. La société "
        "peut valablement fonctionner avec un seul associé ou accueillir ultérieurement de nouveaux actionnaires sans modification de sa forme juridique."
    )

    pdf.titre1("Article 2 — Dénomination sociale")
    pdf.para(
        "La société a pour dénomination sociale : « SOLEIL B2B CÔTE D'IVOIRE » (en abrégé « SOLEIL B2B CI »). "
        "Dans tous les actes, factures, annonces et documents émanant de la société, la dénomination doit être précédée "
        "ou suivie immédiatement des mots « Société par Actions Simplifiée Unipersonnelle » ou du sigle « SASU », et de l'énonciation du montant du capital social."
    )

    pdf.titre1("Article 3 — Objet social")
    pdf.para(
        "La société a pour objet, directement ou indirectement, en République de Côte d'Ivoire et dans tout État partie à l'OHADA :"
    )
    pdf.puces([
        "L'étude technique, l'ingénierie, la conception, le dimensionnement de centrales photovoltaïques d'autoproduction en toiture ;",
        "L'importation, l'acquisition, la distribution et la fourniture de panneaux solaires, onduleurs, structures de montage et équipements électriques associés ;",
        "L'installation, le montage, le raccordement basse et moyenne tension, la mise en service et la maintenance d'infrastructures solaires B2B destinées aux entreprises industrielles, commerciales et tertiaires ;",
        "L'audit d'efficacité énergétique et la commercialisation de solutions décentralisées d'autoconsommation d'électricité ;",
        "Et généralement, toutes opérations commerciales, financières, industrielles, mobilières ou immobilières se rattachant directement ou indirectement à l'objet précité."
    ])

    pdf.titre1("Article 4 — Siège social")
    pdf.para(
        "Le siège social est fixé à : District Autonome d'Abidjan, Commune de Cocody, Quartier Deux-Plateaux. "
        "Il peut être transféré en tout autre lieu du même district par simple décision du Président ou du Directeur Général, "
        "sous réserve de ratification par l'associé unique."
    )

    pdf.titre1("Article 5 — Durée de la société")
    pdf.para(
        "La durée de la société est fixée à quatre-vingt-dix-neuf (99) années à compter de la date de son immatriculation "
        "au Registre du Commerce et du Crédit Mobilier (RCCM), sauf cas de dissolution anticipée ou de prorogation."
    )

    pdf.titre1("Article 6 — Capital social et actions")
    pdf.para(
        "Le capital social est fixé à la somme de dix millions (10 000 000) de Francs CFA (environ 15 245 €). "
        "Il est divisé en mille (1 000) actions ordinaires de dix mille (10 000) Francs CFA chacune, toutes de même catégorie, "
        "intégralement souscrites et libérées en numéraire par l'associé unique Monsieur William Ossimi."
    )

    pdf.titre1("Article 7 — Présidence de la société")
    pdf.para(
        "La société est représentée par son Président, Monsieur William Ossimi, associé unique fondateur. "
        "Le Président exerce ses prérogatives d'actionnaire souverain et ne perçoit aucune rémunération salariale ni mandat de gestion exécutive courante. "
        "Il dispose de la compétence exclusive pour approuver les comptes annuels, affecter les résultats, modifier le capital, nommer ou révoquer le Directeur Général."
    )

    pdf.titre1("Article 8 — Direction Générale et délégation opérationnelle")
    pdf.para(
        "La direction générale opérationnelle et technique de la société est confiée à un Directeur Général, mandataire social désigné par l'associé unique. "
        "Monsieur Mohamed Coulibaly est désigné en qualité de premier Directeur Général de la société pour une durée indéterminée, prenant effet au 1er octobre 2041. "
        "Le Directeur Général assure la représentation courante de la société vis-à-vis des tiers, des clients et des administrations ivoiriennes."
    )
    pdf.para(
        "À titre de mesure d'ordre intérieur et de protection patrimoniale de l'associé unique, tout engagement financier unitaire supérieur "
        "à dix millions (10 000 000) de Francs CFA HT, toute souscription d'emprunt ou de ligne de crédit, toute constitution de sûreté réelle "
        "ou personnelle, tout achat ou cession d'immeuble ou de fonds de commerce requiert l'autorisation écrite préalable et expresse du Président."
    )

    pdf.titre1("Article 9 — Direction Administrative et Financière")
    pdf.para(
        "La Direction Administrative et Financière (DAF) est rattachée hiérarchiquement et fonctionnellement au Directeur Général pour l'ordonnancement "
        "des tâches quotidiennes. Toutefois, en application des règles de transparence statutaire, la DAF est investie d'un devoir d'information direct, "
        "immédiat et permanent envers le Président / Associé Unique, auquel elle transmet sans délai l'ensemble des états de trésorerie, relevés bancaires "
        "et tableaux de bord financiers."
    )

    pdf.titre1("Article 10 — Exercice social et affectation des résultats")
    pdf.para(
        "L'exercice social commence le 1er janvier et se termine le 31 décembre de chaque année. Par exception, le premier exercice social commencera "
        "le jour de l'immatriculation de la société au RCCM et se clôturera le 31 décembre 2042. Le bénéfice net distribuable est attribué sous forme "
        "de dividendes à l'associé unique après dotation de la réserve légale obligatoire (10 % jusqu'à concurrence d'un cinquième du capital)."
    )

    pdf.titre1("Article 11 — Juridiction compétente")
    pdf.para(
        "Toutes les contestations relatives aux affaires sociales survenant pendant la durée de la société ou au cours de sa liquidation sont soumises "
        "à la compétence exclusive du Tribunal de commerce d'Abidjan."
    )

    cible = chemin("documents_william", "2041-07-29_Cabinet_Gnamien_Projet_Statuts_SASU_Projet_Solaire_B2B_Abidjan.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


def generer_mandat_dg():
    pdf = DocPDF(
        "Cabinet Me Ismaël Gnamien & Associés — Avocats à la Cour (Abidjan)",
        "Projet de Convention de Mandat Social de Directeur Général",
        auteur="Cabinet Me Ismaël Gnamien & Associés",
        pied="Projet Convention Mandat Social DG — Cabinet Gnamien — 29/07/2041"
    )

    pdf.meta("Émetteur", "Cabinet Me Ismaël Gnamien & Associés, Avocat à la Cour, Barreau d'Abidjan")
    pdf.meta("Parties", "SASU SOLEIL B2B CÔTE D'IVOIRE (Société) ET Monsieur Mohamed Coulibaly (Directeur Général)")
    pdf.meta("Date et heure", "Lundi 29 juillet 2041, 09h00 (heure d'Abidjan / 11h00 Luxembourg)")
    pdf.meta("Objet", "Convention régissant le mandat social de direction générale, la rémunération et la non-concurrence")
    pdf.ln(3)

    pdf.titre1("Préambule et qualification juridique")
    pdf.para(
        "Entre les soussignés : La société SOLEIL B2B CÔTE D'IVOIRE SASU, représentée par son Associé Unique Monsieur William Ossimi, "
        "d'une part, et Monsieur Mohamed Coulibaly, né à Abidjan, de nationalité ivoirienne, cadre supérieur en banque d'affaires, d'autre part. "
        "Il a été expressément convenu que Monsieur Mohamed Coulibaly exerce ses fonctions en qualité exclusive de mandataire social au sens "
        "des articles 414 et suivants de l'Acte uniforme OHADA (AUSCGIE). Les parties excluent formellement tout contrat de travail salarié "
        "et tout lien de subordination juridique."
    )

    pdf.titre1("Article 1 — Missions et pouvoirs opérationnels")
    pdf.para(
        "Le Directeur Général est investi des pouvoirs opérationnels les plus étendus pour agir au nom de la société dans la limite de l'objet social :"
    )
    pdf.puces([
        "Conduite de la stratégie commerciale B2B, négociation et signature des contrats d'installation photovoltaïque auprès des industriels ;",
        "Supervision technique des chantiers d'installation en toiture, approvisionnements et relations avec les distributeurs de matériel ;",
        "Direction hiérarchique du personnel, des directeurs de pôle et des équipes de techniciens de chantier ;",
        "Relations avec les administrations ivoiriennes, la CIE, l'ANARE-CI et les partenaires bancaires locaux."
    ])

    pdf.titre1("Article 2 — Limitations conventionnelles de pouvoirs")
    pdf.para(
        "Conformément aux directives de l'associé unique, le Directeur Général ne peut valablement accomplir les actes suivants sans avoir "
        "obtenu au préalable l'autorisation écrite et expresse du Président :"
    )
    pdf.puces([
        "Tout engagement financier, bon de commande matériel ou contrat d'un montant supérieur à 10 000 000 FCFA HT ;",
        "Toute souscription d'emprunt, crédit bancaire, découvert ou aval au nom de la société ;",
        "La signature ou la résiliation de baux commerciaux portant sur le siège ou les ateliers de la société ;",
        "La nomination ou le licenciement des directeurs de pôle (cadres C-level) ;",
        "La prise de participation dans toute entité tierce."
    ])

    pdf.titre1("Article 3 — Rémunération et intéressement (Formule 1)")
    pdf.para(
        "En contrepartie de l'accomplissement de ses fonctions de direction, le Directeur Général perçoit :"
    )
    pdf.puces([
        "Traitement fixe mensuel : 2 000 000 FCFA net (soit environ 3 050 €), payable à terme échu le dernier jour ouvré du mois ;",
        "Intéressement variable au chiffre d'affaires : 2,5 % du montant hors taxes des encaissements effectifs réalisés sur les contrats commerciaux conclus et raccordés ;",
        "Prime d'infrastructure industrielle : 5 000 000 FCFA forfaitaire (environ 7 622 €) versée à l'achèvement et à la mise en service auditée de chaque tranche cumulée de 500 kWc solaires installés ;",
        "Évaluation trimestrielle : maintien du mandat subordonné à la signature d'au moins 2 contrats au 1er trimestre d'activité et à une marge brute minimale de 15 000 000 FCFA par trimestre ultérieur."
    ])

    pdf.titre1("Article 4 — Prise de fonction et calendrier de transition")
    pdf.para(
        "Le Directeur Général prend officiellement ses fonctions à plein temps à compter du 1er octobre 2041, à l'issue de son préavis bancaire à Bruxelles. "
        "Toutefois, Monsieur Coulibaly s'engage à être présent physiquement à Abidjan du 12 au 25 août 2041 pour participer à la signature des actes, "
        "aux visites du futur siège social et aux entretiens préalables de constitution de l'équipe locale."
    )

    pdf.titre1("Article 5 — Clause de non-concurrence post-mandat")
    pdf.para(
        "En cas de cessation du mandat social pour quelque cause que ce soit, le Directeur Général s'interdit d'exercer, directement ou indirectement, "
        "toute activité concurrente dans le domaine de l'ingénierie et de l'installation solaire photovoltaïque B2B en toiture, que ce soit en qualité "
        "de dirigeant, d'associé, de consultant ou de salarié. Cette interdiction s'applique sur l'ensemble du District Autonome d'Abidjan pendant "
        "une durée de douze (12) mois consécutifs à compter du départ effectif."
    )

    pdf.titre1("Article 6 — Indemnité compensatrice de non-concurrence")
    pdf.para(
        "En contrepartie de l'obligation de non-concurrence ci-dessus stipulée, la société versera au mandataire une indemnité compensatrice mensuelle "
        "égale à 50 % de sa dernière rémunération fixe nette perçue (soit 1 000 000 FCFA par mois pendant 12 mois). "
        "Cette indemnité sera due exclusivement dans l'hypothèse où la révocation du mandat social est prononcée à l'initiative discrétionnaire de la société, "
        "à l'exclusion formelle de toute démission du mandataire, de toute révocation consécutive à une faute lourde, une faute intentionnelle de gestion ou une violation des statuts."
    )

    pdf.titre1("Article 7 — Clause pénale")
    pdf.para(
        "Toute violation de l'obligation de non-concurrence entraînera de plein droit le versement d'une pénalité forfaitaire égale à douze (12) mois "
        "de rémunération fixe (soit 24 000 000 FCFA), sans préjudice des actions judiciaires en référé tendant à l'interdiction de l'activité litigieuse."
    )

    pdf.titre1("Article 8 — Loi applicable et litiges")
    pdf.para(
        "La présente convention est soumise au droit OHADA et aux lois de la République de Côte d'Ivoire. "
        "Tout litige relatif à sa validité, son interprétation ou son exécution relève de la compétence exclusive du Tribunal de commerce d'Abidjan."
    )

    cible = chemin("documents_william", "2041-07-29_Cabinet_Gnamien_Projet_Convention_Mandat_Social_DG.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


if __name__ == "__main__":
    generer_statuts_sasu()
    generer_mandat_dg()

