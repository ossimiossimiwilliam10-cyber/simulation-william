"""PIÈCES DU SAMEDI 27 JUILLET 2041 MATIN (univers 3, tour n° 62) :
1. courriels/2041-07-27_Confirmation_billet_Air_France_Luxembourg_Abidjan.pdf
   Billet électronique Air France (Luxembourg - Paris CDG - Abidjan A/R, 12 au 25 août 2041).
2. courriels/2041-07-27_Confirmation_e-visa_SNEDAI_Cote_d_Ivoire.pdf
   Attestation officielle de pré-enrôlement biométrique e-visa Côte d'Ivoire (SNEDAI).
3. documents_william/2041-07-27_Notification_selection_DAF_Mariam_Brou.pdf (D025)
   Courriel officiel d'information à Mariam Brou avec transmission de la maquette de contrat Niveau 2.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_billet_air_france():
    pdf = DocPDF(
        "Air France — Billet Électronique & Reçu de Voyage",
        "Référence de réservation : AF-782J9X · Billet n° 057-2489102845",
        auteur="Air France KLM",
        pied="Air France — Reçu Passager e-Ticket AF-782J9X"
    )

    pdf.meta("Passager", "Monsieur William OSSIMI")
    pdf.meta("Émetteur", "Air France Direct / S-Net Spuerkeess Zebra")
    pdf.meta("Date d'émission", "Samedi 27 juillet 2041, 09h15 (heure de Luxembourg)")
    pdf.meta("Paiement", "Carte Visa Premier •••• 4128 — 1 285,00 € TTC (autorisé)")
    pdf.ln(3)

    pdf.titre1("1. Détail de l'itinéraire de vol")
    pdf.tableau(
        ["Trajet", "Date", "Vol & Appareil", "Départ", "Arrivée", "Classe & Bagages"],
        [
            ["Luxembourg (LUX) -> Paris (CDG)", "12/08/2041", "AF 1251 (A220-300)", "07h15 Findel", "08h20 CDG 2F", "Economy Flex · 2x23kg"],
            ["Paris (CDG) -> Abidjan (ABJ)", "12/08/2041", "AF 702 (B777-300ER)", "10h30 CDG 2E", "15h40 Port-Bouët", "Economy Flex · 2x23kg"],
            ["Abidjan (ABJ) -> Paris (CDG)", "25/08/2041", "AF 703 (B777-300ER)", "22h30 Port-Bouët", "06h00 (+1) CDG 2E", "Economy Flex · 2x23kg"],
            ["Paris (CDG) -> Luxembourg (LUX)", "26/08/2041", "AF 1250 (A220-300)", "08h05 CDG 2F", "09h10 Findel", "Economy Flex · 2x23kg"],
        ],
        largeurs=[45, 25, 38, 28, 28, 26]
    )

    pdf.titre1("2. Décomposition tarifaire")
    pdf.tableau(
        ["Poste de coût", "Montant en EUR"],
        [
            ["Tarif de base hors taxes (aller-retour Luxembourg - Abidjan)", "840,00 €"],
            ["Surcharges transporteur / carburant international (YQ/YR)", "265,00 €"],
            ["Taxes aéroportuaires et sûreté (Luxembourg LUX + Paris CDG)", "88,40 €"],
            ["Redevance de développement aéronautique et sûreté Abidjan (ABJ)", "91,60 €"],
            ["Total payé par carte Visa Premier (débit différé au 07/08/2041)", "1 285,00 €"],
        ],
        largeurs=[140, 50]
    )

    pdf.titre1("3. Formalités d'enregistrement et conditions du tarif")
    pdf.puces([
        "Enregistrement en ligne disponible 30 heures avant le départ sur airfrance.lu ou l'application mobile ;",
        "Franchise bagages : 2 bagages en soute de 23 kg chacun + 1 bagage cabine (12 kg) et 1 accessoire personnel ;",
        "Conditions tarifaires Economy Flex : billet modifiable sans frais avant départ, remboursable en cas d'annulation ;",
        "Documents requis : passeport en cours de validité (au moins 6 mois), e-visa biométrique ivoirien, carnet de vaccination international (fièvre jaune obligatoire)."
    ])

    cible = chemin("courriels", "2041-07-27_Confirmation_billet_Air_France_Luxembourg_Abidjan.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


def generer_evisa_snedai():
    pdf = DocPDF(
        "République de Côte d'Ivoire — e-Visa Biométrique",
        "Attestation officielle de pré-enrôlement e-Visa · Réf. CI-2041-88419B",
        auteur="SNEDAI Technologies & Ministère de la Sécurité",
        pied="e-Visa Côte d'Ivoire — SNEDAI Réf. CI-2041-88419B"
    )

    pdf.meta("Demandeur", "Monsieur William OSSIMI")
    pdf.meta("Nationalité", "Luxembourgeoise (Passeport LUX ••••••••)")
    pdf.meta("Type de visa", "Court séjour Affaires / Investissement (90 jours, entrées multiples)")
    pdf.meta("Paiement", "73,00 € TTC (47 885 FCFA) — Visa Premier autorisée le 27/07/2041 09h30")
    pdf.ln(3)

    pdf.titre1("1. Statut de la demande de visa")
    pdf.para(
        "Le Ministère de la Sécurité et de l'Intérieur de la République de Côte d'Ivoire certifie que la demande de pré-enrôlement "
        "en ligne pour l'obtention d'un visa biométrique à l'arrivée a été enregistrée avec succès sous la référence officielle :"
    )
    pdf.para(
        "CODE DOSSIER : CI-2041-88419B — PAIEMENT SÉCURISÉ CONFIRMÉ"
    )

    pdf.titre1("2. Informations du séjour déclaré")
    pdf.tableau(
        ["Paramètre", "Donnée déclarée"],
        [
            ["Nom et Prénom", "OSSIMI William"],
            ["Date de naissance", "19/07/2005 (36 ans)"],
            ["Nationalité & Pièce", "Luxembourg · Passeport ordinaire n° L8492015"],
            ["Motif du déplacement", "Prospection économique et investissement d'affaires (Projet Solaire SAS)"],
            ["Période de séjour", "Du 12/08/2041 au 25/08/2041 (14 jours)"],
            ["Adresse de résidence à Abidjan", "Résidence Hôtelière Sécurisée, Cocody Deux-Plateaux Vallon, Abidjan"],
            ["Contact local", "Cabinet d'Avocats Ismaël Gnamien & Associés (Plateau, Abidjan)"],
        ],
        largeurs=[60, 130]
    )

    pdf.titre1("3. Procédure de délivrance à l'arrivée (Aéroport d'Abidjan Port-Bouët)")
    pdf.puces([
        "Présenter la présente attestation imprimée ou sur smartphone à l'espace e-Visa de l'Aéroport Félix-Houphouët-Boigny ;",
        "Prise des empreintes digitales et photographie biométrique au guichet dédié e-Visa (délai moyen de délivrance : 10 minutes) ;",
        "Vignette visa apposée directement sur le passeport luxembourgeois pour une durée de validité de 90 jours ;",
        "Contrôle sanitaire obligatoire : présentation du carnet de vaccination international attestant du vaccin contre la fièvre jaune."
    ])

    cible = chemin("courriels", "2041-07-27_Confirmation_e-visa_SNEDAI_Cote_d_Ivoire.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


def generer_notification_mariam_brou():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Pôle Ressources Humaines",
        "Notification de sélection de candidature · À l'attention de Madame Mariam Brou",
        auteur="L'équipe du projet",
        pied="Projet Solaire B2B Abidjan — Candidature DAF (Mme Brou)"
    )

    pdf.meta("Émetteur", "L'équipe du projet (Direction des Ressources Humaines)")
    pdf.meta("Destinataire", "Madame Mariam Brou (Comptable / Gestionnaire, Abidjan)")
    pdf.meta("Date et heure", "Samedi 27 juillet 2041, 09h45 (heure de Luxembourg / 07h45 Abidjan)")
    pdf.meta("Objet", "Sélection de votre candidature à la Direction Administrative et Financière & Maquette contractuelle")
    pdf.ln(3)

    pdf.titre1("1. Statut de votre candidature à la Direction Administrative et Financière")
    pdf.para(
        "Chère Madame Brou,"
    )
    pdf.para(
        "Nous faisons suite à la transmission de votre dossier de candidature, de vos attestations d'expérience ainsi qu'aux retours "
        "très positifs recueillis auprès de vos références professionnelles à Abidjan."
    )
    pdf.para(
        "Nous avons le plaisir de vous informer que votre profil a été formellement retenu comme choix prioritaire pour assurer "
        "la Direction Administrative et Financière (DAF) de notre future société par actions simplifiée (SAS) dédiée aux solutions solaires B2B en Côte d'Ivoire. "
        "Vous pouvez d'ores et déjà vous considérer comme faisant partie intégrante de notre projet d'entreprise."
    )

    pdf.titre1("2. Calendrier d'intégration et prise de contact par la Direction Générale")
    pdf.para(
        "La finalisation de notre structuration juridique a requis quelques jours supplémentaires afin de sceller en priorité "
        "la nomination de notre Directeur Général, un cadre supérieur de banque d'affaires à Bruxelles disposant d'une expertise éprouvée des projets industriels."
    )
    pdf.para(
        "Dans la mesure où le Directeur Général assure la conduite opérationnelle plénipotentiaire sur le terrain et que la Direction Administrative "
        "et Financière lui sera directement rattachée au quotidien pour la gestion comptable, la trésorerie et le reporting actionnarial, "
        "c'est lui qui prendra directement attache avec vous très prochainement en visioconférence pour conduire votre entretien opérationnel "
        "d'intégration et caler les derniers détails de votre entrée en fonction."
    )

    pdf.titre1("3. Transmission de la maquette contractuelle de Direction (Niveau 2)")
    pdf.para(
        "Afin de vous permettre d'examiner en amont le cadre d'exercice et de préparer sereinement vos attentes ainsi que vos prétentions, "
        "nous vous transmettons en pièce jointe la maquette contractuelle cadre régissant les postes de directeurs opérationnels au sein de notre structure "
        "(Contrat de travail à durée indéterminée, statut Cadre dirigeant, conformité au Code du travail ivoirien et aux normes SYSCOHADA)."
    )
    pdf.puces([
        "Statut : Cadre dirigeant sous contrat de travail de droit ivoirien avec convention d'objectifs ;",
        "Périmètre : Responsabilité complète de la comptabilité générale et analytique, gestion de trésorerie, déclarations fiscales et sociales, conformité OHADA ;",
        "Rattachement : Subordination hiérarchique au Directeur Général avec obligation de transparence et reporting direct à l'associé unique."
    ])

    pdf.para(
        "Nous vous remercions très chaleureusement pour votre confiance et votre disponibilité, et nous réjouissons à l'idée "
        "de bâtir cette aventure industrielle ensemble."
    )
    pdf.ln(2)
    pdf.para("Veuillez agréer, Madame Brou, l'expression de nos salutations les plus cordiales.")
    pdf.ln(4)
    pdf.para("L'équipe du projet")

    cible = chemin("documents_william", "2041-07-27_Notification_selection_DAF_Mariam_Brou.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


if __name__ == "__main__":
    generer_billet_air_france()
    generer_evisa_snedai()
    generer_notification_mariam_brou()
