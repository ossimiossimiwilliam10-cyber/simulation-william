"""Génération des pièces du vendredi 26 juillet 2041 au soir (tour n° 59).
- Rapport d'activité quotidien n° 7 du Directeur Général virtuel (20h00).
"""
from pdf_base import DocPDF, chemin


def generer_rapport_dg_26_juillet():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Direction Générale virtuelle",
        "Rapport d'activité quotidien n° 7 — Vendredi 26 juillet 2041 (20h00)",
        auteur="Directeur Général virtuel",
        pied="Projet Solaire B2B Abidjan — Rapport quotidien n° 7 du 26/07/2041"
    )

    pdf.meta("Émetteur", "Directeur Général virtuel (Coordination des pôles Juridique, RH, Technique, Commercial)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique et Investisseur")
    pdf.meta("Date et heure", "Vendredi 26 juillet 2041, 20h00 (heure de Luxembourg)")
    pdf.meta("Objet", "Bilan d'activité quotidien, accord de recrutement du Directeur Général, mission Abidjan et budget")
    pdf.ln(3)

    pdf.titre1("1. Recrutement de la Direction Générale réelle (Monsieur Mohamed Coulibaly)")
    pdf.para(
        "L'entretien officiel de sélection mené ce jour de 18h30 à 19h35 en visioconférence a permis de sceller "
        "un accord de principe complet entre l'associé unique et Monsieur Mohamed Coulibaly. Les termes de la gouvernance "
        "et de l'engagement contractuel ont été définitivement harmonisés :"
    )
    pdf.puces([
        "Nature du mandat : Mandat social pur de Directeur Général de SASU sous l'Acte uniforme OHADA, sans contrat de travail salarié, révocable ad nutum par décision de l'associé unique ;",
        "Rémunération arrêtée : Fixe mensuel net de 2 000 000 FCFA (~3 050 €), intéressement de 2,5 % du chiffre d'affaires HT encaissé, prime de 5 000 000 FCFA par tranche de 500 kWc raccordée ;",
        "Clause de non-concurrence : Durée de 12 mois post-mandat sur le Grand Abidjan, assortie d'une indemnité compensatrice mensuelle de 50 % du fixe (1 000 000 FCFA/mois) en cas de révocation à l'initiative de l'actionnaire ;",
        "Gouvernance opérationnelle : Mohamed Coulibaly assurera la direction plénipotentiaire sur le terrain. La DAF lui sera hiérarchiquement rattachée au quotidien avec obligation de reporting régulier à l'actionnaire ;",
        "Calendrier d'installation : Présence conjointe à Abidjan pour la mission du 12 au 25 août 2041, déploiement des directeurs technique et commercial dès la mi-septembre, prise de poste physique permanente au 1er octobre 2041."
    ])

    pdf.titre1("2. Cadrage du déplacement à Abidjan et implantation du QG")
    pdf.para(
        "Conformément aux directives de l'associé unique, le déploiement opérationnel a été formalisé comme suit :"
    )
    pdf.puces([
        "Dates du séjour : Mission confirmée du lundi 12 août au dimanche 25 août 2041 (14 jours), calée sur la fermeture annuelle du Minett Combat Club ;",
        "Sécurisation des baux et investissements : Gel temporaire de l'enveloppe de démarrage (25 155 €) dans l'attente des visites sur place et de la contre-expertise du DG désigné ;",
        "Objectifs de la mission : Finalisation des actes constitutifs au Cabinet Gnamien, signature de la convention de mandat social, visite et bail de la villa QG à Cocody Deux-Plateaux, formalités bancaires CEPICI."
    ])

    pdf.titre1("3. Affirmations vérifiées du jour (Pôle Juridique)")
    pdf.tableau(
        ["Élément analysé", "Statut de conformité", "Constat du Pôle Juridique"],
        [
            ["Non-concurrence mandataire", "VÉRIFIÉE", "La stipulation d'une indemnité compensatrice de 50 % renforce la validité de la clause face à la jurisprudence OHADA sur la liberté d'entreprendre."],
            ["Prise d'effet différée au RCCM", "VÉRIFIÉE", "La nomination d'un Directeur Général avec prise d'effet au 1er octobre est pleinement recevable pour l'immatriculation au CEPICI."],
            ["Reporting DAF / Actionnaire", "VÉRIFIÉE", "La double subordination (hiérarchique au DG et fonctionnelle à l'actionnaire) est conforme aux statuts types de SAS de droit des affaires."],
        ],
        largeurs=[55, 45, 90]
    )

    pdf.titre1("4. Consommation du budget informatique virtuel")
    pdf.para(
        "La consommation de ressources informatiques pour la journée du 26 juillet 2041 s'établit à 1,70 € HT (0,90 € pour l'étude comparative "
        "d'implantation et 0,80 € pour la synthèse de coordination). Le cumul mensuel s'élève à 43,26 € sur le plafond alloué de 1 000,00 € (solde disponible : 956,74 €)."
    )

    pdf.titre1("5. Décisions fermées soumises à l'associé unique")
    pdf.para(
        "Pour clore la semaine de cadrage et préparer les livrables juridiques du lundi 29 juillet, l'équipe virtuelle vous soumet deux décisions fermées :"
    )
    pdf.puces([
        "Question 1 : Validez-vous la transmission des termes de la convention de mandat de Mohamed Coulibaly à Me Ismaël Gnamien pour insertion dans le dossier constitutif de la SAS ? (Oui / Non)",
        "Question 2 : Autorisez-vous l'évaluation des options de réservation pour la mission à Abidjan (vol Luxair/Air France et résidence sécurisée Cocody du 12 au 25 août) ? (Oui / Non)"
    ])

    cible = chemin("documents_william", "2041-07-26_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


if __name__ == "__main__":
    generer_rapport_dg_26_juillet()

