"""
Génération des contrats et de la note de conformité juridique
Mercredi 7 août 2041 — Tour n° 71
1. Convention de mandat social de Président-Directeur Général (Mohamed Coulibaly)
2. Contrat de travail Cadre de Direction Administrative et Financière (Mariam Brou)
3. Contrat de travail Cadre de Direction Technique (Éric Koffi Yao)
4. Note de synthèse et contre-expertise juridique du pôle juridique virtuel
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_mandat_pdg_coulibaly():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Acte de Gouvernance",
        "Convention de Mandat Social de Président et Directeur Général",
        auteur="Pôle Juridique & Cabinet Me Ismaël Gnamien",
        pied="Convention de Mandat Social PDG — SOLEIL B2B CI — Signature 13/08/2041"
    )

    pdf.meta("Société mandante", "SOLEIL B2B CÔTE D'IVOIRE SASU (en formation), représentée par Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Mandataire désigné", "Monsieur Mohamed Coulibaly, de nationalité ivoirienne, domicilié à Bruxelles et Abidjan")
    pdf.meta("Qualité et mandat", "Président et Directeur Général (mandataire social exécutif au sens de l'art. 853-1 AUSCGIE)")
    pdf.meta("Date de signature prévue", "Mardi 13 août 2041, 10h00 — Étude notariale / Cabinet Me Gnamien, Abidjan")
    pdf.ln(3)

    pdf.titre1("Préambule et cadre de gouvernance")
    pdf.para(
        "Par décision de l'Associé Unique Fondateur Monsieur William Ossimi, la présidence exécutive et la direction "
        "générale opérationnelle de la société SOLEIL B2B CÔTE D'IVOIRE SASU sont expressément réunies et confiées à "
        "Monsieur Mohamed Coulibaly. Cette organisation assure une séparation absolue entre la détention patrimoniale du "
        "capital (détenu à 100 % par l'Associé Unique, sans fonction de gestion) et l'exercice du mandat social de direction "
        "exécutive, garantissant la parfaite conformité de l'Associé Unique avec les exigences statutaires de son administration d'origine."
    )

    pdf.titre1("Article 1 — Nature du mandat et absence de contrat de travail")
    pdf.para(
        "Monsieur Mohamed Coulibaly est investi d'un mandat social révocable dans les conditions prévues par les statuts "
        "et les dispositions impératives de l'Acte uniforme OHADA. Les parties excluent formellement toute relation de travail "
        "salarié et tout lien de subordination juridique entre la société et son mandataire social."
    )

    pdf.titre1("Article 2 — Pouvoirs et représentation vis-à-vis des tiers")
    pdf.para(
        "Le Président-Directeur Général est investi des pouvoirs les plus étendus pour agir en toute circonstance au nom de la "
        "société dans la limite de l'objet social. Il assure la direction opérationnelle, technique, commerciale et financière "
        "de l'entreprise, recrute et encadre le personnel, et représente la société auprès des autorités ivoiriennes (ANARE-CI, CIE, CEPICI)."
    )

    pdf.titre1("Article 3 — Limitations statutaires de pouvoirs")
    pdf.para(
        "À titre de mesure de sauvegarde patrimoniale, le Président-Directeur Général ne peut valablement accomplir les actes "
        "suivants sans avoir recueilli l'autorisation préalable écrite et expresse de l'Associé Unique Fondateur :"
    )
    pdf.puces([
        "Tout engagement, contrat de fourniture, bon de commande matériel ou devis d'un montant unitaire supérieur à 10 000 000 FCFA HT ;",
        "Toute souscription d'emprunt, crédit bancaire, facilité de caisse, découvert ou constitution de sûreté réelle ;",
        "La signature, la cession ou la résiliation de baux commerciaux portant sur les locaux de la société ;",
        "La nomination ou le licenciement des cadres dirigeants (DAF, Directeur Technique, Directeur Commercial) ;",
        "Toute prise de participation, constitution de filiale ou accord de partenariat stratégique engageant le capital."
    ])

    pdf.titre1("Article 4 — Rémunération et intéressement")
    pdf.para(
        "En contrepartie de l'accomplissement de ses fonctions de Président-Directeur Général, Monsieur Coulibaly perçoit :"
    )
    pdf.puces([
        "Traitement fixe mensuel : 2 000 000 FCFA net d'impôts sur les traitements et salaires ivoiriens, payable à terme échu ;",
        "Intéressement commercial : 2,5 % du montant hors taxes des encaissements effectifs sur les contrats d'autoproduction raccordés ;",
        "Prime de réalisation d'infrastructure : 5 000 000 FCFA forfaitaire versée à la livraison auditée de chaque tranche cumulée de 500 kWc solaires installés ;",
        "Objectifs minimaux : signature d'au moins deux contrats clients au cours du premier trimestre d'activité opérationnelle."
    ])

    pdf.titre1("Article 5 — Clause de non-concurrence post-mandat")
    pdf.para(
        "Pendant une durée de douze (12) mois consécutifs à compter de la cessation de ses fonctions, le mandataire s'interdit "
        "d'exercer, directement ou indirectement, toute activité concurrente dans le domaine du solaire photovoltaïque B2B "
        "sur l'ensemble du District Autonome d'Abidjan. En contrepartie, une indemnité mensuelle égale à 50 % de sa rémunération "
        "fixe lui sera versée en cas de révocation à l'initiative de la société hors cas de faute lourde."
    )

    pdf.titre1("Article 6 — Prise d'effet et droit applicable")
    pdf.para(
        "Le mandat prend effet au 1er octobre 2041 à plein temps, avec participation requise à Abidjan du 12 au 25 août 2041. "
        "La présente convention est régie par l'Acte uniforme OHADA et soumise à la juridiction du Tribunal de commerce d'Abidjan."
    )

    cible = chemin("documents_william", "2041-08-07_Convention_Mandat_Social_President_Directeur_General_Mohamed_Coulibaly.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_contrat_daf_mariam_brou():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Contrat de Travail",
        "Contrat de Travail à Durée Indéterminée — Directrice Administrative et Financière",
        auteur="Pôle Juridique & Cabinet Me Ismaël Gnamien",
        pied="Contrat Cadre CDI DAF — SOLEIL B2B CI — Signature 13/08/2041"
    )

    pdf.meta("Employeur", "SOLEIL B2B CÔTE D'IVOIRE SASU, représentée par son Président-Directeur Général, Monsieur Mohamed Coulibaly")
    pdf.meta("Salariée", "Madame Mariam Brou, cadre supérieure de gestion, de nationalité ivoirienne, domiciliée à Abidjan")
    pdf.meta("Fonction et statut", "Directrice Administrative et Financière (DAF) — Statut Cadre Supérieur, Catégorie F2")
    pdf.meta("Date de signature prévue", "Mardi 13 août 2041, 14h00 — Siège Cabinet Me Gnamien / Abidjan Plateau")
    pdf.ln(3)

    pdf.titre1("Article 1 — Engagement et fonction")
    pdf.para(
        "La société SOLEIL B2B CÔTE D'IVOIRE engage Madame Mariam Brou en qualité de Directrice Administrative et Financière (DAF), "
        "sous le régime du Code du travail de la République de Côte d'Ivoire et de la Convention Collective Interprofessionnelle."
    )

    pdf.titre1("Article 2 — Missions et responsabilités")
    pdf.para(
        "Sous l'autorité hiérarchique du Directeur Général, la DAF est chargée de :"
    )
    pdf.puces([
        "La tenue de la comptabilité générale et analytique selon le système comptable OHADA (SYSCOHADA révisé) ;",
        "La gestion rigoureuse de la trésorerie locale, des encaissements clients et des relations bancaires ;",
        "L'ordonnancement de la fiscalité d'entreprise, des déclarations DGI et des cotisations sociales CNPS ;",
        "La gestion administrative du personnel, l'établissement des bulletins de paie et la conformité contractuelle ;",
        "L'élaboration des budgets prévisionnels, bilans périodiques et tableaux de bord mensuels de gestion."
    ])

    pdf.titre1("Article 3 — Devoir d'information directe et transparence financière")
    pdf.para(
        "En application des statuts de la société et des directives de gouvernance arrêtées par l'Associé Unique Fondateur, "
        "Madame Mariam Brou est investie d'une obligation statutaire et contractuelle d'information directe et continue auprès de "
        "l'Associé Unique. Elle lui transmet sans délai, par canal sécurisé, l'ensemble des états de trésorerie hebdomadaires, "
        "relevés bancaires et états financiers prévisionnels, en toute indépendance fonctionnelle."
    )

    pdf.titre1("Article 4 — Rémunération et avantages")
    pdf.para(
        "En contrepartie de ses fonctions, Madame Mariam Brou perçoit une rémunération mensuelle nette forfaitaire de "
        "un million six cent mille (1 600 000) Francs CFA, payée à terme échu le 28 de chaque mois, majorée des cotisations "
        "patronales et salariales CNPS obligatoires et d'une assurance santé complémentaire groupe prise en charge par la société."
    )

    pdf.titre1("Article 5 — Période d'essai et prise d'effet")
    pdf.para(
        "Le présent contrat est conclu pour une durée indéterminée prenant effet le 1er septembre 2041, assorti d'une période "
        "d'essai de trois (3) mois renouvelable une fois conformément au Code du travail. Madame Brou participe aux séances de "
        "cadrage et de revue budgétaire prévues à Abidjan durant la mission du 13 au 25 août 2041."
    )

    pdf.titre1("Article 6 — Confidentialité et secret des affaires")
    pdf.para(
        "Madame Brou s'engage au secret professionnel absolu concernant l'ensemble des données financières, techniques, "
        "commerciales et stratégiques de la société. Cette obligation survit sans limitation de durée à la rupture des relations de travail."
    )

    cible = chemin("documents_william", "2041-08-07_Contrat_Travail_Direction_Administrative_Financiere_Mariam_Brou.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_contrat_dt_eric_yao():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Contrat de Travail",
        "Contrat de Travail à Durée Indéterminée — Directeur Technique",
        auteur="Pôle Juridique & Cabinet Me Ismaël Gnamien",
        pied="Contrat Cadre CDI DT — SOLEIL B2B CI — Signature 13/08/2041"
    )

    pdf.meta("Employeur", "SOLEIL B2B CÔTE D'IVOIRE SASU, représentée par son Président-Directeur Général, Monsieur Mohamed Coulibaly")
    pdf.meta("Salarié", "Monsieur Éric Koffi Yao, ingénieur électromécanicien et solaire, de nationalité ivoirienne, domicilié à Abidjan")
    pdf.meta("Fonction et statut", "Directeur Technique (DT) — Statut Cadre Supérieur, Catégorie F2")
    pdf.meta("Date de signature prévue", "Mardi 13 août 2041, 16h00 — Siège Cabinet Me Gnamien / Abidjan Plateau")
    pdf.ln(3)

    pdf.titre1("Article 1 — Engagement et qualification")
    pdf.para(
        "La société SOLEIL B2B CÔTE D'IVOIRE engage Monsieur Éric Koffi Yao en qualité de Directeur Technique, "
        "sous le régime du Code du travail ivoirien. Monsieur Yao a obtenu la note d'évaluation de 84/100, validée par la Direction."
    )

    pdf.titre1("Article 2 — Missions et responsabilités techniques")
    pdf.para(
        "Sous la responsabilité du Directeur Général, le Directeur Technique assure :"
    )
    pdf.puces([
        "La réalisation et la validation des études d'ingénierie préliminaires et d'exécution (dimensionnement PVsyst, plans de calepinage toitures) ;",
        "Le pilotage des chantiers d'installation en toiture industrielle, la sécurité des équipes et le respect des normes électriques UTE / NFC 15-100 ;",
        "La gestion des approvisionnements en équipements certifiés (panneaux de classe Tier-1, onduleurs industriels, câblage solaire) ;",
        "Le raccordement basse tension et moyenne tension, les essais de performance et les démarches de conformité auprès de la CIE et de l'ANARE-CI ;",
        "La mise en place des protocoles de télégestion, de monitoring à distance et de maintenance préventive des centrales installées."
    ])

    pdf.titre1("Article 3 — Rémunération et prime de mise en service")
    pdf.para(
        "En contrepartie de ses prestations, Monsieur Éric Koffi Yao perçoit :"
    )
    pdf.puces([
        "Rémunération fixe mensuelle : un million six cent mille (1 600 000) Francs CFA net d'impôts, payable le dernier jour ouvré du mois ;",
        "Prime de raccordement réussi : 500 000 FCFA par centrale industrielle mise en service sans réserves techniques majeures dans les délais contractuels ;",
        "Prise en charge intégrale des équipements de sécurité EPI, véhicule de service pour les déplacements sur site et couverture santé groupe."
    ])

    pdf.titre1("Article 4 — Prise d'effet et calendrier")
    pdf.para(
        "Le contrat prend effet au 1er septembre 2041 avec une période d'essai de trois (3) mois. Monsieur Yao confirme sa participation "
        "pleine et entière à la mission d'Abidjan du 13 au 25 août 2041 pour les visites de toitures pilotes identifiées."
    )

    pdf.titre1("Article 5 — Clause d'exclusivité et de propriété intellectuelle")
    pdf.para(
        "Monsieur Yao consacre l'exclusivité de son activité professionnelle à la société. L'ensemble des études, schémas, méthodes de montage "
        "et perfectionnements techniques élaborés durant le contrat sont la propriété exclusive de SOLEIL B2B CÔTE D'IVOIRE SASU."
    )

    cible = chemin("documents_william", "2041-08-07_Contrat_Travail_Direction_Technique_Eric_Koffi_Yao.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_note_synthese_juridique():
    pdf = DocPDF(
        "Pôle Juridique Virtuel — Direction Générale SOLEIL B2B",
        "Note de Synthèse et Contre-Expertise Juridique des Actes Contractuels",
        auteur="Pôle Juridique Virtuel",
        pied="Note Juridique Contrats Direction — SOLEIL B2B CI — 07/08/2041"
    )

    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Rédacteur", "Pôle Juridique Virtuel — Supervision des Actes OHADA et Droit Social Ivoirien")
    pdf.meta("Date", "Mercredi 7 août 2041, 08h30 (heure de Luxembourg)")
    pdf.meta("Objet", "Attestation de contre-expertise des contrats de direction en attente de signature à Abidjan")
    pdf.ln(3)

    pdf.titre1("1. Objet de la contre-expertise")
    pdf.para(
        "À la demande expresse de l'Associé Unique Fondateur, le pôle juridique virtuel a procédé à un audit approfondi "
        "et à une double vérification de l'ensemble des projets de contrats devant lier SOLEIL B2B CÔTE D'IVOIRE SASU "
        "à ses dirigeants et cadres supérieurs."
    )

    pdf.titre1("2. Résultats de l'audit contractuel")
    pdf.puces([
        "Convention de Mandat Social PDG (Mohamed Coulibaly) : Parfaite conformité avec l'Acte uniforme OHADA (AUSCGIE, art. 853-1). "
        "La présidence exécutive confiée à Monsieur Coulibaly immunise intégralement William Ossimi contre le risque d'incompatibilité "
        "posé par l'article 14 luxembourgeois. La clause de non-concurrence de 12 mois indemnisée à 50 % est juridiquement blindée et "
        "les seuils d'autorisation préalable (veto au-delà de 10 000 000 FCFA) garantissent la souveraineté de l'Associé Unique ;",
        "Contrat de Travail DAF (Mariam Brou) : Conforme au Code du travail ivoirien (Loi n° 2015-532). Rémunération de 1 600 000 FCFA net "
        "validée. La clause de transparence directe instaurant un devoir d'information permanente au profit de l'Associé Unique est "
        "valable et ne dénature pas le lien hiérarchique avec le Directeur Général ;",
        "Contrat de Travail DT (Éric Koffi Yao) : Conforme au Code du travail et aux normes techniques de sécurité des chantiers électriques. "
        "Rémunération de 1 600 000 FCFA net et prime de raccordement conformes à la grille de Niveau 2 approuvée."
    ])

    pdf.titre1("3. Statut de stockage et préparation de la mission")
    pdf.para(
        "L'ensemble des actes a été mis sous format officiel PDF, archivé dans le dossier 'documents_william/' et transmis au Cabinet "
        "de Maître Ismaël Gnamien pour impression des cinq exemplaires originaux sur papier timbré. Les documents sont rigoureusement prêts "
        "pour la séance solennelle de signature du mardi 13 août 2041 à Abidjan Plateau."
    )

    cible = chemin("documents_william", "2041-08-07_Note_Synthese_Juridique_Contrats_Direction_Prets_Signature.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_mandat_pdg_coulibaly()
    generer_contrat_daf_mariam_brou()
    generer_contrat_dt_eric_yao()
    generer_note_synthese_juridique()
