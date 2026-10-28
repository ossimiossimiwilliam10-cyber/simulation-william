"""
Génération de la Maquette des Missions Continues et Objectifs Récurrents par Pôle
Jeudi 8 août 2041 — Tour n° 73
Document préparatoire confidentiel destiné à la Direction Générale et à l'Associé Unique
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_maquette_missions_poles():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE SASU — Organisation & Gouvernance",
        "Maquette des Missions Continues et Objectifs Récurrents par Pôle",
        auteur="Direction Générale Virtuelle — Pôle Organisation",
        pied="Maquette Missions Continues par Pôle — Document Préparatoire Confidentiel — 08/08/2041"
    )

    pdf.meta("Émetteur", "Pôle Organisation & RH Virtuel — Pour le compte de l'Associé Unique Fondateur")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (usage interne préparatoire)")
    pdf.meta("Statut du document", "Document de travail confidentiel — Maquette avant concertation avec Mohamed Coulibaly")
    pdf.meta("Date d'établissement", "Jeudi 8 août 2041, 10h00 (heure de Luxembourg)")
    pdf.ln(3)

    pdf.titre1("1. Préambule et doctrine opérationnelle")
    pdf.para(
        "Ce document formalise la maquette des missions continues et des objectifs récurrents assignés à chaque "
        "direction opérationnelle de SOLEIL B2B CÔTE D'IVOIRE SASU. Une mission continue représente une routine "
        "hebdomadaire non négociable, tandis qu'un objectif récurrent fixe un seuil mesurable mensuel ou trimestriel. "
        "Cette maquette servira de base de travail pour l'échange de cadrage avec Monsieur Mohamed Coulibaly lors "
        "de la mission d'août à Abidjan."
    )

    pdf.titre1("2. Direction Générale (Président-Directeur Général — Mohamed Coulibaly)")
    pdf.para(
        "Le PDG pilote l'entreprise, veille à la rentabilité globale et incarne la société auprès des grands partenaires."
    )
    pdf.puces([
        "Missions continues hebdomadaires :",
        "  • Conduite du comité de direction hebdomadaire (lundi matin) : arbitrage des priorités entre commerce, technique et finance ;",
        "  • Accompagnement en binôme des négociations commerciales stratégiques sur les toitures industrielles majeures (> 500 kWc) ;",
        "  • Point d'avancement opérationnel avec le Directeur Technique (revue des plannings de chantiers et approvisionnements) ;",
        "  • Contrôle des équilibres de trésorerie avec la Directrice Administrative et Financière ;",
        "Objectifs récurrents mensuels et trimestriels :",
        "  • Maintien d'une marge brute opérationnelle minimale de 15 000 000 FCFA par trimestre à compter du T1 opérationnel ;",
        "  • Livraison auditée d'au moins 500 kWc cumulés par trimestre d'activité (conditionnant la prime d'infrastructure) ;",
        "  • Transmission d'un rapport de gestion mensuel complet à l'Associé Unique (états financiers, pipe commercial, RH) ;",
        "  • Respect strict des compétences réservées (aucun engagement financier > 10 000 000 FCFA sans validation écrite préalable)."
    ])

    pdf.titre1("3. Direction Commerciale (DC)")
    pdf.para(
        "La Direction Commerciale porte la croissance du chiffre d'affaires et la signature des contrats d'autoproduction B2B."
    )
    pdf.puces([
        "Missions continues hebdomadaires :",
        "  • Prospection directe ciblée : minimum 10 nouveaux contacts d'entreprises industrielles qualifiés par semaine ;",
        "  • Tenue rigoureuse du pipe commercial (CRM) : suivi hebdomadaire des étapes (prise de contact, audit, devis, closing) ;",
        "  • Organisation d'au moins 3 visites de sites industriels ou toitures par semaine avec l'équipe technique ;",
        "  • Réunion commerciale hebdomadaire de revue des offres en cours et relance des décideurs industriels ;",
        "Objectifs récurrents mensuels :",
        "  • Dépôt d'au moins 2 propositions commerciales fermes (études dimensionnées et chiffrées) par mois auprès de prospects chauds ;",
        "  • Objectif de closing en vitesse de croisière : signature de 1 à 2 contrats d'autoproduction PPA fermes par mois (puissance minimale 150 kWc) ;",
        "  • Objectif probatoire du 1er trimestre : signature ferme d'au moins 2 contrats d'autoproduction (condition de confirmation de poste)."
    ])

    pdf.titre1("4. Direction Technique (DT — Éric Koffi Yao)")
    pdf.para(
        "La Direction Technique garantit l'excellence de l'ingénierie, la sécurité des chantiers et le respect des normes."
    )
    pdf.puces([
        "Missions continues hebdomadaires :",
        "  • Visites techniques de préfaisabilité sur toitures sous 48h après sollicitation commerciale (structure, charpente, orientation) ;",
        "  • Élaboration des dimensionnements sur logiciel certifié (PVsyst), notes de calcul et calepinage des modules ;",
        "  • Supervision directe quotidienne des chantiers en cours : contrôle strict du port des EPI et des règles de sécurité en hauteur ;",
        "  • Suivi des approvisionnements de matériel Tier-1 et contrôle de conformité des réceptions d'onduleurs et panneaux ;",
        "Objectifs récurrents mensuels :",
        "  • Zéro accident de travail avec arrêt sur l'ensemble des chantiers sous gestion ;",
        "  • Achèvement des travaux et raccordement au réseau dans le respect rigoureux des délais contractuels convenus avec le client ;",
        "  • Taux de réception technique sans réserve majeure par les inspecteurs de la CIE et de l'ANARE-CI à 100 % ;",
        "  • Activation opérationnelle du télémonitoring de performance sur chaque centrale dès sa mise sous tension."
    ])

    pdf.titre1("5. Direction Administrative et Financière (DAF — Mariam Brou)")
    pdf.para(
        "La DAF assure la rigueur comptable SYSCOHADA, la gestion de la trésorerie et la transparence vis-à-vis de l'Associé Unique."
    )
    pdf.puces([
        "Missions continues hebdomadaires :",
        "  • Établissement du rapprochement bancaire hebdomadaire et suivi au jour le jour des soldes de trésorerie disponible ;",
        "  • Transmission hebdomadaire directe à l'Associé Unique du tableau de bord de trésorerie consolidé (obligation statutaire) ;",
        "  • Relance systématique à J+3 de toute créance client arrivée à échéance de facturation ;",
        "  • Suivi des pointages horaires du personnel de chantier et validation des frais professionnels justifiés ;",
        "Objectifs récurrents mensuels :",
        "  • Clôture comptable mensuelle à J+5 ouvrés selon le référentiel SYSCOHADA révisé ;",
        "  • Dépôt sans retard des déclarations fiscales (TVA, retenues) et sociales (CNPS) : zéro pénalité fiscale ou sociale tolérée ;",
        "  • Émission et paiement des salaires le 28 de chaque mois par virement bancaire sécurisé ;",
        "  • Comparaison mensuelle du budget engagé par rapport à l'enveloppe d'investissement initialement allouée par l'Associé Unique."
    ])

    pdf.titre1("6. Synthèse des flux de reporting vers l'Associé Unique")
    pdf.para(
        "Le dispositif repose sur deux canaux d'information complémentaires : un reporting hebdomadaire direct de trésorerie "
        "assuré par la DAF, et une revue de gestion mensuelle stratégique présentée par le PDG. Cette architecture préserve "
        "la pleine souveraineté de contrôle de l'Associé Unique tout en maintenant une autonomie d'action quotidienne pour la direction."
    )

    cible = chemin("documents_william", "2041-08-08_Maquette_Missions_Continues_et_Objectifs_Recurrents_Poles.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_maquette_missions_poles()
