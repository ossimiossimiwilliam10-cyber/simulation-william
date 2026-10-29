"""
Génération du courriel officiel de transmission des dossiers de Direction Commerciale
Vendredi 16 août 2041, 12h00 — Tour n° 94
Mohamed Coulibaly transmet les dossiers complets de Marc-Antoine Kouadio et Viviane Tanoh
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_dossiers_dc():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Transmission des Dossiers Stratégiques Direction Commerciale",
        auteur="Mohamed Coulibaly",
        pied="Dossiers DC Kouadio & Tanoh — SOLEIL B2B CI — 16/08/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly, Directeur Général (m.coulibaly@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Vendredi 16 août 2041, 12h00 (heure d'Abidjan)")
    pdf.meta("Objet", "Remise officielle des dossiers de sélection DC : Marc-Antoine Kouadio et Viviane Tanoh (réponses à la grille en 5 questions)")
    pdf.ln(3)

    pdf.titre1("1. Point d'avancement des formalités administratives et bancaires")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "J'ai le plaisir de vous confirmer que les formalités d'immatriculation au CEPICI se sont déroulées sans difficulté "
        "ce matin dès huit heures. Les exemplaires originaux physiques du Registre du Commerce et du Crédit Mobilier (RCCM) "
        "et de l'Identifiant Unique (IDU) de SOLEIL B2B CÔTE D'IVOIRE SASU sont désormais en ma possession."
    )
    pdf.para(
        "Je me suis immédiatement rendu à l'agence centrale de la Société Générale Côte d'Ivoire (SGCI) au Plateau avec Me Gnamien "
        "pour formaliser l'ouverture définitive et l'activation opérationnelle du compte professionnel de la société. Le chargé d'affaires "
        "grandes entreprises a enregistré les pouvoirs, les statuts et le mandat social. Le traitement des signatures et la validation "
        "informatique de conformité KYC sont en cours ; le relevé d'identité bancaire (RIB) officiel me sera remis dès le début d'après-midi, "
        "vers 13h30, ce qui permettra l'exécution de votre apport en compte courant dès réception."
    )
    pdf.para(
        "Conformément à votre calendrier, j'ai reçu ce jour à midi les dossiers complets et les plans d'actions stratégiques des deux "
        "candidats finalistes retenus pour la Direction Commerciale. Vous trouverez ci-après leur synthèse structurée selon les cinq "
        "axes de la grille d'évaluation que vous avez formalisée."
    )

    pdf.titre1("2. Candidat n° 1 : Monsieur Marc-Antoine Kouadio (38 ans)")
    pdf.para(
        "• Profil & Expérience : 12 ans d'expérience commerciale grands comptes B2B dans le secteur de l'énergie et de l'équipement électrique "
        "industriel en Côte d'Ivoire, dont 6 ans comme Responsable Grands Comptes chez un leader multinational de la distribution électrique moyenne tension.\n"
        "• Formation : Master en Commerce International (ESCA Abidjan) et certificat spécialisé en management de la transition énergétique (2032).\n"
        "• Prétentions financières : 1 500 000 FCFA net mensuel fixe + variable cible de 1,5 % sur la marge brute encaissée des contrats signés."
    )
    pdf.para("Réponses aux 5 questions clés de la grille :")
    pdf.puces([
        "Axe 1 — Portefeuille Clients (25 %) : Transmet une cartographie ciblée de 14 comptes industriels majeurs à Vridi et San Pedro (cimenteries, agro-industrie du cacao, meuneries) avec identité des directeurs d'usine et puissances actuelles de 250 kWc à 1 MWc. Relations directes et établies avec 9 décideurs.",
        "Axe 2 — Offre Anti-Délestage (25 %) : Approche technique de haute précision. Il modélise le coût complet du kWh thermique (groupes électrogènes avec gasoil à 850 FCFA/l + maintenance lourde) comparé à une solution hybride solaire + stockage LFP amortie sur 4,2 ans. Argumentaire financier très solide à destination des DAF.",
        "Axe 3 — Vélocité du Cycle de Vente (20 %) : Plan de vente structuré en 4 étapes, mais annonce un délai moyen de contractualisation de 75 à 90 jours (au lieu des 60 jours visés), justifié selon lui par la lourdeur des circuits de décision des comités d'investissement des grands groupes industriels.",
        "Axe 4 — Management Équipe Terrain (15 %) : Style de gestion directif et analytique. Grille de reporting hebdomadaire rigoureuse sur CRM, objectifs individuels stricts, suivi serré des taux de conversion. Exige une forte autonomie des commerciaux juniors de Niveau 4.",
        "Axe 5 — Conformité & Zéro Bakchich (15 %) : Engagement éthique sans réserve. Refus formel de tout intermédiaire officieux. Préconise la signature d'accords d'audit de conformité bilatéraux avec les clients et des clauses anticorruption strictes conformes aux standards internationaux."
    ])

    pdf.titre1("3. Candidate n° 2 : Madame Viviane Tanoh (36 ans)")
    pdf.para(
        "• Profil & Expérience : 10 ans d'expérience commerciale terrain dans la distribution industrielle, groupes électrogènes et matériel B2B "
        "à Abidjan, dont 5 ans comme Directrice des Ventes chez un distributeur majeur d'équipements industriels couvrant Yopougon, Marcory et Treichville.\n"
        "• Formation : Diplôme Supérieur de Commerce et Vente (INP-HB Yamoussoukro, 2027).\n"
        "• Prétentions financières : 1 400 000 FCFA net mensuel fixe + variable cible de 2 % sur la marge brute encaissée des contrats signés."
    )
    pdf.para("Réponses aux 5 questions clés de la grille :")
    pdf.puces([
        "Axe 1 — Portefeuille Clients (25 %) : Transmet une liste détaillée de 18 PME/PMI dynamiques à Yopougon et Treichville (chambres froides, conserveries, imprimeries, logistique) ayant un besoin urgent d'autonomie énergétique (puissances de 100 à 400 kWc). Accès direct aux patrons fondateurs.",
        "Axe 2 — Offre Anti-Délestage (25 %) : Discours orienté vers la continuité d'exploitation et la prévention des pertes de stock dues aux délestages CIE. Chiffrage clair des pertes d'exploitation, mais s'appuie largement sur le bureau d'études technique pour les calculs d'optimisation batterie.",
        "Axe 3 — Vélocité du Cycle de Vente (20 %) : Plan d'attaque très agressif visant un closing en 45 jours. Elle intègre un partenariat de pré-financement leasing avec deux banques de la place (financement à 100 % sur 5 ans), levant le principal frein à l'investissement initial.",
        "Axe 4 — Management Équipe Terrain (15 %) : Style de management énergique et coachant. Rituels du lundi matin avec mise en situation, débriefings quotidiens de 15 minutes, accompagnement terrain des prospecteurs juniors et prime de palier pour valoriser la prise de rendez-vous qualifié.",
        "Axe 5 — Conformité & Zéro Bakchich (15 %) : Adhésion totale à la politique d'intégrité. Propose un cadre formalisé d'apport d'affaires déclaré et facturé par des sociétés de conseil juridique ou d'ingénierie enregistrées, excluant toute remise en espèces ou rétro-commission individuelle."
    ])

    pdf.titre1("4. Tableau Récapitulatif et Modalités d'Arbitrage")
    entetes_recap = ["Critère / Axe", "Marc-Antoine Kouadio", "Viviane Tanoh", "Pondération"]
    lignes_recap = [
        ["1. Portefeuille Clients", "14 Grands Comptes (Vridi, San Pedro)", "18 PME/PMI (Yopougon, Treichville)", "25 %"],
        ["2. Offre Anti-Délestage", "Excellence financière / ROI 4,2 ans", "Approche pertes d'exploitation terrain", "25 %"],
        ["3. Vélocité Cycle Vente", "Cycle de 75 à 90 jours (prudent)", "Cycle de 45 jours (partenariat leasing)", "20 %"],
        ["4. Management Terrain", "Directif, reporting CRM très poussé", "Coaching actif, accompagnement terrain", "15 %"],
        ["5. Éthique & Conformité", "Conformité stricte, audit bilatéral", "Apports d'affaires formels et déclarés", "15 %"],
        ["Prétentions Salariales", "1 500 000 FCFA net + 1,5 % marge", "1 400 000 FCFA net + 2,0 % marge", "Indicateur"]
    ]
    pdf.tableau(entetes_recap, lignes_recap, [45, 60, 60, 25])

    pdf.ln(3)
    pdf.para(
        "Avis consultatif du Directeur Général : Monsieur Kouadio apporte une crédibilité institutionnelle et une expertise technique "
        "indispensable pour les installations de grande puissance (> 500 kWc). Madame Tanoh offre une vélocité d'acquisition exceptionnelle "
        "et une énergie commerciale terrain idéales pour sécuriser rapidement nos premiers flux de trésorerie auprès des PME. "
        "Les deux profils satisfont à nos exigences préliminaires. Je reste à votre disposition pour recueillir vos notations souveraines "
        "critère par critère afin de trancher conformément à notre seuil éliminatoire de 80/100."
    )

    sortie = chemin("courriels", "2041-08-16_Courriel_Mohamed_Coulibaly_Transmission_Dossiers_DC_Kouadio_et_Tanoh.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_courriel_dossiers_dc()
