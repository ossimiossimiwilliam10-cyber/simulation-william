"""
Génération de la Maquette Organisationnelle : Équipes Opérationnelles, Profils Niveaux 3 & 4 et Typologie des Missions
Vendredi 9 août 2041 — Tour n° 76
Document préparatoire confidentiel destiné à l'Associé Unique Fondateur
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_maquette_equipes_operationnelles():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Organisation & Ressources Humaines",
        "Maquette Organisationnelle : Structuration des Équipes, Niveaux 3 & 4 et Typologie des Missions",
        auteur="Pôle Organisation & RH Virtuel",
        pied="Maquette Équipes Opérationnelles — SOLEIL B2B CI — 09/08/2041"
    )

    pdf.meta("Émetteur", "Pôle Organisation, RH & Stratégie Virtuel")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (usage interne préparatoire)")
    pdf.meta("Statut du document", "Document de travail confidentiel — Maquette n° 3 avant concertation avec Mohamed Coulibaly")
    pdf.meta("Date d'établissement", "Vendredi 9 août 2041, 15h30 (heure de Luxembourg)")
    pdf.meta("Objet", "Dimensionnement des effectifs, typologie des missions (continues, direction, spéciales) et critères de sélection")
    pdf.ln(3)

    pdf.titre1("1. Préambule : Philosophie de dimensionnement agile")
    pdf.para(
        "En complément des maquettes sur les missions des directeurs (Maquette 1) et le contrôle interne (Maquette 2), "
        "ce document formalise l'architecture complète des équipes opérationnelles de terrain (Niveaux 3 et 4). "
        "Pour un démarrage d'activité dans le solaire industriel B2B à Abidjan, la structure doit être agile, "
        "maîtrisée en coûts fixes et hautement qualifiée. Le schéma cible prévoit un effectif initial de 7 à 9 collaborateurs "
        "répartis en pôles spécialisés, avec une montée en charge conditionnée aux signatures effectives de centrales."
    )

    pdf.titre1("2. Typologie trifonctionnelle des missions")
    pdf.para(
        "Pour assurer une gouvernance fluide et un contrôle sans faille, les tâches de l'ensemble du personnel "
        "s'articulent selon une typologie stricte à trois niveaux :"
    )
    pdf.puces([
        "A. Missions Continues : Responsabilités permanentes et récurrentes inscrites dans les fiches de poste (routines hebdomadaires, tenue de tableaux de bord, prospection minimale, maintenance préventive) ;",
        "B. Missions de Direction : Ordres d'exécution et directives d'exploitation émis par le Président-Directeur Général et les directeurs de pôles dans le cadre de la gestion opérationnelle courante ;",
        "C. Missions Spéciales : Missions d'investigation, d'audit inopiné ou de vérification ciblée ordonnées exclusivement par l'Associé Unique Fondateur (William Ossimi) via son canal souverain confidentiel, exécutées par le pôle virtuel ou des tiers accrédités."
    ])

    pdf.titre1("3. Structuration détaillée des équipes par direction")
    pdf.para(
        "L'organisation cible s'articule autour des quatre directions principales de la société :"
    )
    pdf.puces([
        "Direction Générale (PDG Mohamed Coulibaly — Niveau 1) :",
        "  • Assistance de direction : En Phase 1 (amorçage), afin de minimiser la masse salariale fixe, le PDG s'appuie sur le secrétariat partagé et la DAF. En Phase 2 (dès 3 chantiers simultanés), création d'un poste d'Assistant(e) de Direction Générale & Juridique (Niveau 4, note 75-85) ; la question sera posée à Mohamed Coulibaly pour recueillir son appréciation de charge ;",
        "Direction Commerciale (Sous l'autorité du Directeur Commercial — Niveau 2) :",
        "  • Absence de chef d'équipe intermédiaire : structure directe sans échelon superflu au démarrage ;",
        "  • Force de vente : 2 Ingénieurs Commerciaux B2B / Chargés d'Affaires Grands Comptes (Niveau 4) dédiés à la prospection des toitures industrielles (zones de Vridi, Yopougon, PK24) et à la négociation des baux solaires PPA ;",
        "Direction Technique (Sous l'autorité du Directeur Technique Éric Koffi Yao — Niveau 2) :",
        "  • 1 Chef d'Équipe Travaux & Chantiers Solaires (Niveau 3) : pilotage sur site, coordination de la sécurité, respect des plannings et interface avec les industriels hôtes ;",
        "  • 1ère Équipe Travaux (Niveau 4) : 2 à 3 Techniciens Installateurs Photovoltaïques & Câbleurs Électriciens qualifiés (montage mécanique toiture, câblage DC/AC, raccordement onduleurs, mise sous tension) ;",
        "  • Évolutivité : création d'une 2e Équipe Travaux dès que deux chantiers d'envergure se déroulent en parallèle ;",
        "Direction Administrative et Financière (Sous l'autorité de la DAF Mariam Brou — Niveau 2) :",
        "  • 1 Analyste Quantitatif / Risk Analyst (Niveau 3 ou 4 spécialisé) : modélisation financière, scoring de contrepartie sur 10-15 ans, suivi de rentabilité (LCOE/TRI) et calcul du burn rate (1 analyste suffit pour l'ensemble du portefeuille initial) ;",
        "  • 1 Comptable Général & Paie (Niveau 4) : tenue de la comptabilité générale, déclarations fiscales et sociales ivoiriennes, facturation des redevances et gestion de la facturation fournisseurs."
    ])

    pdf.titre1("4. Doctrine de sélection et critères de recrutement (Niveaux 3 & 4)")
    pdf.para(
        "Conformément aux instructions de l'Associé Unique, les exigences de qualification sont calibrées selon le niveau hiérarchique :"
    )
    pdf.puces([
        "Niveau 3 (Chefs d'équipe & Spécialistes seniors) : Seuil éliminatoire strict >= 80/100, avec une note minimale de 85 sur le critère cœur de métier et une expérience préalable réussie d'au moins 5 ans sur chantiers industriels ;",
        "Niveau 4 (Opérationnels, techniciens et commerciaux juniors) : Priorité aux profils jeunes (< 30 ans) dotés d'un fort potentiel de progression. Note de sélection globale comprise entre 75 et 85/100, intégrant un segment d'évaluation spécifique 'Potentiel & Agilité' (capacité d'apprentissage rapide, rigueur d'exécution, adaptabilité aux normes internationales) pour favoriser l'émergence de talents d'avenir."
    ])

    pdf.titre1("5. Stratégie de transmission à Mohamed Coulibaly")
    pdf.para(
        "L'Associé Unique dispose désormais de 3 maquettes complètes de gouvernance : (1) Missions continues par direction, "
        "(2) Contrôle interne et anti-détournement, (3) Équipes opérationnelles et profils Niveaux 3/4. "
        "Deux options stratégiques s'offrent pour leur transmission :",
    )
    pdf.puces([
        "Option 1 (Anticipation numérique) : Transmission officielle des 3 maquettes à Mohamed Coulibaly par courriel institutionnel dès ce vendredi après-midi, pour lui donner le week-end d'étude préalable avant l'arrivée de William à Abidjan ;",
        "Option 2 (Restitution physique) : Conservation des maquettes dans les dossiers de William et remise solennelle en main propre lors de la première séance de cadrage en personne à Abidjan le mardi 13 août."
    ])

    cible = chemin("documents_william", "2041-08-09_Maquette_Organisationnelle_Equipes_Operationnelles_et_Profils.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_maquette_equipes_operationnelles()