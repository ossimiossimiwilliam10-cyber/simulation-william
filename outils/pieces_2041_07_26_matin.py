"""PIÈCE DU 26/07/2041 MATIN (univers 3, tour n° 54) :
Note stratégique du Directeur Général virtuel sur :
1. L'opportunité, le calendrier et le cadrage du déplacement de William à Abidjan ;
2. La typologie et la localisation du futur Siège / QG opérationnel (villa vs bureaux) ;
3. Le budget d'installation (bail, mobilier, informatique, groupe de secours) ;
4. Le respect strict de la gouvernance et de l'Article 14 (qui signe et qui décide).

Génération du fichier PDF physique déposé dans `documents_william/`
et référencé dans l'application Gestion / Téléphone.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_note_strategique_abidjan():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Direction Générale virtuelle",
        "Note stratégique : Implantation du QG à Abidjan & Calendrier de mission de l'Associé Unique",
        auteur="Directeur Général virtuel",
        pied="Projet Solaire B2B Abidjan — Note stratégique QG et déplacement Abidjan"
    )

    pdf.meta("Émetteur", "Directeur Général virtuel (Coordination juridique, financière et logistique)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique et Investisseur")
    pdf.meta("Date et heure", "Vendredi 26 juillet 2041, 10h00 (heure de Luxembourg)")
    pdf.meta("Objet", "Cadrage de la mission à Abidjan, stratégie immobilière du QG et budget d'équipement")
    pdf.ln(3)

    pdf.titre1("1. Analyse de l'opportunité et calendrier optimal pour votre séjour à Abidjan")
    pdf.para(
        "Votre démarche de vous rendre en personne à Abidjan est non seulement pertinente mais hautement stratégique. "
        "Elle permettra d'ancrer votre relation de travail avec Monsieur Mohamed Coulibaly, de valider physiquement "
        "l'emplacement du siège social, de rencontrer Maître Ismaël Gnamien pour la finalisation du dossier d'immatriculation "
        "et d'ouvrir formellement les relations avec les banques de la place (BICICI, Ecobank)."
    )
    pdf.para(
        "L'analyse croisée de vos contraintes professionnelles et de l'avancement juridique dégage la fenêtre temporelle suivante :"
    )
    pdf.tableau(
        ["Période étudiée", "Adéquation et contraintes", "Avis du Directeur Général virtuel"],
        [
            [
                "12 au 25 août 2041 (14 jours)",
                "Plein cœur de vos vacances scolaires. Coïncide exactement avec la fermeture estivale de votre club de combat "
                "(Minett Combat Club fermé du 12 au 25/08). Statuts enregistrés et immatriculation CEPICI effective.",
                "PÉRIODE IDÉALE (Recommandée) : zéro perturbation sportive, timing juridique optimal pour l'installation."
            ],
            [
                "18 au 25 août 2041 (7 jours)",
                "Format resserré sur une semaine. Permet de signer les actes finaux et de visiter les biens immobiliers présélectionnés.",
                "Option courte : efficace mais rythme très dense pour les démarches bancaires et notariales."
            ],
            [
                "Toussaint 2041 (fin octobre)",
                "Départ différé après deux mois d'exploitation pilotés à distance par Mohamed Coulibaly.",
                "Non recommandée pour le lancement initial : Mohamed aurait déjà dû engager les baux sans votre regard direct."
            ]
        ],
        largeurs=[50, 85, 55]
    )

    pdf.titre1("2. Typologie et localisation du futur QG d'entreprise")
    pdf.para(
        "Pour une société d'ingénierie et d'installation photovoltaïque B2B, le choix du siège opérationnel répond à des impératifs "
        "à la fois de standing commercial (accueil des dirigeants d'entreprises) et de logistique technique :"
    )
    pdf.tableau(
        ["Formule immobilière", "Quartier ciblé", "Loyer prévisionnel", "Avantages opérationnels"],
        [
            [
                "Villa individuelle à usage mixte (bureaux + cour/dépôt)",
                "Cocody Deux-Plateaux (Vallons ou 7e/8e tranche)",
                "1 200 000 à 1 800 000 FCFA/mois (≈ 1 800 à 2 700 €/mois)",
                "Configuration parfaite : 3 bureaux fermés, salle de réunion, open space, cour sécurisée pour véhicule et outillage technique."
            ],
            [
                "Villa ou plateau de bureaux",
                "Marcory Zone 4 / Zone 3",
                "1 500 000 à 2 200 000 FCFA/mois (≈ 2 300 à 3 350 €/mois)",
                "Proximité immédiate des toitures industrielles (Vridi, port), mais loyers plus élevés et accès encombré aux heures de pointe."
            ],
            [
                "Bureaux équipés / Coworking d'affaires (Transition 3 mois)",
                "Cocody Danga ou Plateau",
                "400 000 à 700 000 FCFA/mois (≈ 600 à 1 050 €/mois)",
                "Démarrage ultra-rapide sans engagement de bail 3-6-9, mais stockage matériel impossible."
            ]
        ],
        largeurs=[45, 45, 45, 55]
    )

    pdf.titre1("3. Estimation budgétaire de l'installation initiale du QG")
    pdf.para(
        "Les dépenses d'installation et d'équipement de démarrage s'imputeront sur la première tranche d'amorçage de votre budget "
        "d'investissement (enveloppe initiale de 60 000 € sur les 300 000 € prévus dans votre stratégie I6) :"
    )
    pdf.tableau(
        ["Poste de dépenses QG", "Montant estimatif (FCFA)", "Contrevaleur (EUR)", "Observations techniques"],
        [
            ["Dépôt de garantie & avance bail (3 mois)", "4 500 000 FCFA", "6 860 €", "Caution légale de 2 mois + 1 mois de loyer d'avance."],
            ["Mobilier de bureau ergonomique", "3 000 000 FCFA", "4 570 €", "5 postes complets, fauteuils, table de réunion 8 places, rangements."],
            ["Parc informatique et réseau local", "4 000 000 FCFA", "6 100 €", "4 PC portables cadres/ingénieurs, multifonction A3/A4, routeur fibre."],
            ["Secours énergétique (onduleur & batteries)", "3 500 000 FCFA", "5 335 €", "Indispensable pour continuité de service face aux coupures réseau CIE."],
            ["Frais d'agence et d'état des lieux", "1 500 000 FCFA", "2 290 €", "Commission standard d'agence immobilière agréée."],
            ["TOTAL INVESTISSEMENT DÉMARRAGE QG", "16 500 000 FCFA", "25 155 €", "Couvert à 42 % de l'enveloppe de 1ère tranche (solde restant : ≈ 34 800 €)."]
        ],
        largeurs=[65, 45, 35, 45]
    )

    pdf.titre1("4. Rappel impératif de gouvernance : respect de l'Article 14")
    pdf.para(
        "Le Pôle Juridique virtuel souligne un point cardinal : en application stricte de votre statut de fonctionnaire luxembourgeois "
        "(Article 14), vous êtes exclusivement l'Associé Unique et le bailleur de fonds de la société, et non son gérant opérationnel. "
        "En conséquence :"
    )
    pdf.puces([
        "Vous ne devez en aucun cas signer le bail commercial ou les contrats d'achat en qualité de représentant légal de l'entreprise ;",
        "C'est Monsieur Mohamed Coulibaly, en sa qualité de Directeur Général titulaire du mandat social, qui signera formellement le bail et engagera la société dès la délivrance de l'extrait RCCM ;",
        "Votre rôle lors du séjour à Abidjan sera de visiter les lieux, de valider l'opportunité économique et financière de l'implantation, et d'autoriser le décaissement des fonds sur le compte de la société."
    ])

    cible = chemin("documents_william", "2041-07-26_Note_strategique_Mission_Abidjan_et_Implantation_QG.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")


if __name__ == "__main__":
    generer_note_strategique_abidjan()
