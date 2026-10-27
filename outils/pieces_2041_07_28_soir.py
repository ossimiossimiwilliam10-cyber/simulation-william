"""Génération des pièces du dimanche 28 juillet 2041 au soir.
- Rapport d'activité quotidien n° 9 du Directeur Général virtuel (20h00).
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_rapport_dg_28_juillet():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Direction Générale virtuelle",
        "Rapport d'activité quotidien n° 9 — Dimanche 28 juillet 2041 (20h00)",
        auteur="Directeur Général virtuel",
        pied="Projet Solaire B2B Abidjan — Rapport quotidien n° 9 du 28/07/2041"
    )

    pdf.meta("Émetteur", "Directeur Général virtuel (Coordination des pôles Juridique, RH, Technique, Commercial)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique et Investisseur")
    pdf.meta("Date et heure", "Dimanche 28 juillet 2041, 20h00 (heure de Luxembourg)")
    pdf.meta("Objet", "Bilan d'activité quotidien, veille des pôles et préparatifs de réception des statuts")
    pdf.ln(3)

    pdf.titre1("1. Situation de la gouvernance et des ressources humaines")
    pdf.para(
        "Le suivi du week-end confirme la parfaite stabilité de l'organisation et des contacts stratégiques :"
    )
    pdf.puces([
        "Direction Générale (Mohamed Coulibaly) : Accord formel et protocole écrit consolidés ; le futur dirigeant prépare ses démarches de sourcing pour les pôles technique et commercial en amont de son arrivée à Abidjan le 12 août ;",
        "Direction Administrative et Financière (Mariam Brou) : Notification formelle de sélection et maquette contractuelle de Niveau 2 prises en compte ; dossier en attente de la prise de contact opérationnelle par le Directeur Général ;",
        "Filtrage et contre-expertise (I43) : Les modules d'évaluation algorithmique du Pôle RH virtuel sont armés pour auditer les candidatures de directeurs dès leur transmission par Mohamed."
    ])

    pdf.titre1("2. Préparatifs juridiques et échéance statutaire")
    pdf.para(
        "L'attention du Pôle Juridique virtuel est focalisée sur la livraison attendue lundi 29 juillet :"
    )
    pdf.puces([
        "Cabinet Me Ismaël Gnamien : Livraison des projets complets des statuts constitutifs de la SAS et de la convention de mandat social du Directeur Général ;",
        "Procédure de validation : Dès réception des documents numériques, le Pôle Juridique virtuel procédera à un examen de conformité avec les stipulations arrêtées (mandat social pur, non-concurrence de 12 mois à 50 % d'indemnité, pouvoirs du DG, protection de l'associé unique) ;",
        "Formalités CEPICI : Préparation des formalités d'enregistrement et d'immatriculation au RCCM dès validation définitive des actes par l'associé unique."
    ])

    pdf.titre1("3. Logistique de mission Abidjan (12 au 25 août 2041)")
    pdf.para(
        "Le dispositif logistique demeure parfaitement verrouillé :"
    )
    pdf.puces([
        "Transport : Billets Air France confirmés (réf. AF-782J9X, départ le lundi 12 août à 07h15 de Luxembourg-Findel via Paris CDG) ;",
        "Immigration : Attestation de pré-enrôlement biométrique e-Visa SNEDAI enregistrée (dossier n° CI-2041-88419B), prête pour les formalités à l'aéroport d'Abidjan Port-Bouët ;",
        "Hébergement : Option active sur l'appartement F2 en résidence hôtelière sécurisée à Cocody Deux-Plateaux (1 690 € pour 13 nuits avec groupe électrogène permanent)."
    ])

    pdf.titre1("4. Affirmations vérifiées du jour (Pôle Juridique)")
    pdf.tableau(
        ["Élément analysé", "Statut de conformité", "Constat du Pôle Juridique"],
        [
            ["Sécurisation du mandat DG", "VÉRIFIÉE", "Les paramètres convenus avec Mohamed Coulibaly respectent scrupuleusement les dispositions de l'Acte uniforme OHADA relatif au droit des sociétés commerciales."],
            ["Veille des candidatures DAF", "VÉRIFIÉE", "L'absence de relance prématurée de Mariam Brou confirme sa posture d'attente disciplinée conforme à la notification transmise."],
            ["Couverture voyage Air France", "VÉRIFIÉE", "Les polices d'assurance associées à la carte Visa Premier couvrent l'intégralité du séjour du 12 au 25 août 2041."],
        ],
        largeurs=[55, 45, 90]
    )

    pdf.titre1("5. Consommation du budget informatique virtuel")
    pdf.para(
        "La consommation de ressources informatiques pour la journée du 28 juillet 2041 s'établit à 0,80 € HT (veille quotidienne, maintenance et audit des flux). "
        "Le cumul mensuel s'élève à 44,86 € sur le plafond alloué de 1 000,00 € (solde disponible : 955,14 €)."
    )

    pdf.titre1("6. Prochain jalon")
    pdf.para(
        "Lundi 29 juillet 2041 (matinée) : Réception et audit approfondi des projets de statuts et de mandat DG transmis par le cabinet de Maître Ismaël Gnamien."
    )

    cible = chemin("documents_william", "2041-07-28_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Créé : {cible}")
    return cible


if __name__ == "__main__":
    generer_rapport_dg_28_juillet()

