"""Génération des pièces du samedi 27 juillet 2041 au soir (tour n° 62).
- Rapport d'activité quotidien n° 8 du Directeur Général virtuel (20h00).
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_rapport_dg_27_juillet():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Direction Générale virtuelle",
        "Rapport d'activité quotidien n° 8 — Samedi 27 juillet 2041 (20h00)",
        auteur="Directeur Général virtuel",
        pied="Projet Solaire B2B Abidjan — Rapport quotidien n° 8 du 27/07/2041"
    )

    pdf.meta("Émetteur", "Directeur Général virtuel (Coordination des pôles Juridique, RH, Technique, Commercial)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique et Investisseur")
    pdf.meta("Date et heure", "Samedi 27 juillet 2041, 20h00 (heure de Luxembourg)")
    pdf.meta("Objet", "Bilan d'activité quotidien, validation des préparatifs de mission Abidjan et situation des recrutements")
    pdf.ln(3)

    pdf.titre1("1. Situation de la Direction Générale et gouvernance")
    pdf.para(
        "La journée a été marquée par la consolidation définitive des accords de gouvernance :"
    )
    pdf.puces([
        "Accusé de réception formel de Mohamed Coulibaly : reçu ce matin à 08h45 par voie officielle, confirmant son accord plein et sans réserve sur le protocole écrit exclusif (adresse institutionnelle de direction) et l'organigramme cible à six pôles ;",
        "Feuille de route opérationnelle : activation de ses réseaux professionnels dès le début de semaine prochaine pour le sourcing des Directeurs Technique et Commercial ;",
        "Disponibilité confirmée : congés calés et vol réservé pour une arrivée à Abidjan le lundi 12 août en fin d'après-midi, en vue des signatures notariées et visites terrain dès le mardi 13 août."
    ])

    pdf.titre1("2. Situation du recrutement de la Direction Administrative et Financière (DAF)")
    pdf.para(
        "Conformément aux instructions stratégiques de l'associé unique, le positionnement de Madame Mariam Brou a été sécurisé :"
    )
    pdf.puces([
        "Notification officielle transmise : message du pôle RH envoyé à 09h45 confirmant sa sélection prioritaire pour le poste de DAF et l'invitant à préparer sereinement ses prétentions ;",
        "Transmission de la maquette contractuelle : communication du contrat cadre Niveau 2 (CDI Cadre dirigeant SYSCOHADA) pour étude préalable ;",
        "Délégation de l'entretien final : la prise de contact et la conduite de l'entretien d'embauche seront assurées par Mohamed Coulibaly après la signature formelle de son propre mandat social à Abidjan."
    ])

    pdf.titre1("3. Verrouillage logistique de la mission à Abidjan (12 au 25 août 2041)")
    pdf.para(
        "L'ensemble des formalités d'organisation du déplacement a été exécuté ce jour avec succès :"
    )
    pdf.puces([
        "Transport aérien : Billet électronique Air France émis (réf. AF-782J9X, 1 285,00 € TTC réglé par carte Visa Premier, débit au 07/08/2041) pour le trajet Luxembourg-Findel via Paris CDG vers Abidjan A/R ;",
        "Formalité d'entrée : Pré-enrôlement e-Visa biométrique validé auprès de la SNEDAI (réf. CI-2041-88419B, 73,00 € TTC), attestation officielle archivée ;",
        "Hébergement : Option confirmée sur la résidence hôtelière sécurisée de Cocody Deux-Plateaux (appartement F2 avec groupe électrogène industriel, 13 nuits pour 1 690 € à régler sur place)."
    ])

    pdf.titre1("4. Affirmations vérifiées du jour (Pôle Juridique)")
    pdf.tableau(
        ["Élément analysé", "Statut de conformité", "Constat du Pôle Juridique"],
        [
            ["Contrat cadre Niveau 2 (DAF)", "VÉRIFIÉE", "Les stipulations du contrat cadre transmis à Mariam Brou sont strictement conformes au Code du travail ivoirien et à la convention collective."],
            ["Procédure e-Visa SNEDAI", "VÉRIFIÉE", "L'attestation de pré-enrôlement est le document légalement requis pour l'embarquement et la prise d'empreintes à l'arrivée à Abidjan Port-Bouët."],
            ["Assurances Visa Premier", "VÉRIFIÉE", "Le règlement des billets d'avion par la carte Visa Premier active les garanties assistance rapatriement et annulation voyage."],
        ],
        largeurs=[55, 45, 90]
    )

    pdf.titre1("5. Consommation du budget informatique virtuel")
    pdf.para(
        "La consommation de ressources informatiques pour la journée du 27 juillet 2041 s'établit à 0,80 € HT (instruction du dossier DAF et notification). "
        "Le cumul mensuel s'élève à 44,06 € sur le plafond alloué de 1 000,00 € (solde disponible : 955,94 €)."
    )

    pdf.titre1("6. Prochain jalon")
    pdf.para(
        "Lundi 29 juillet 2041 : Réception des projets d'actes constitutifs de la SAS et de la convention de mandat social rédigés par le cabinet de Maître Ismaël Gnamien."
    )

    cible = chemin("documents_william", "2041-07-27_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


if __name__ == "__main__":
    generer_rapport_dg_27_juillet()
