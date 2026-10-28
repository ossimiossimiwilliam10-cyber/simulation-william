"""Génération des pièces officielles des 2 au 5 août 2041 (tour n° 68) :
- D038 : Courriel officiel Direction Générale à Mohamed Coulibaly (validation DT Yao, rejet DC Bamba) (02/08 20h15)
- Courriel incoming : Mohamed Coulibaly accuse réception des instructions DT/DC (03/08 09h30)
- D039 : Rapport d'activité quotidien n° 15 du Directeur Général virtuel (03/08 20h00)
- D040 : Rapport d'activité quotidien n° 16 du Directeur Général virtuel (04/08 20h00)
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_dg_validation_dt_rejet_dc():
    pdf = DocPDF(
        "SOLEIL B2B COTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Décision sur les Candidatures de Direction",
        auteur="William Ossimi, Président Fondateur",
        pied="Instruction DG — Candidatures Direction — 02/08/2041"
    )

    pdf.meta("Émetteur", "Direction Générale / William Ossimi (direction@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur Mohamed Coulibaly, Directeur Général désigné")
    pdf.meta("Date et heure", "Vendredi 2 août 2041, 20h15 (heure Luxembourg / 18h15 Abidjan)")
    pdf.meta("Objet", "Décision de gouvernance : Validation Direction Technique et Relance Direction Commerciale")
    pdf.ln(3)

    pdf.titre1("1. Arbitrage relatif à la Direction Technique")
    pdf.para(
        "Monsieur le Directeur Général,"
    )
    pdf.para(
        "J'accuse bonne réception de la transmission des dossiers de candidature pour la Direction Technique et la Direction Commerciale, "
        "reçus ce jour à 19h15. Après examen approfondi et application stricte de notre grille d'évaluation multicritères :"
    )
    pdf.puces([
        "Candidature de Monsieur Éric Koffi Yao (41 ans) : VALIDÉE. Le dossier obtient une notation globale de 84/100, supérieure au seuil d'exigence de 80/100 fixé par notre gouvernance ;",
        "Points forts retenus : Solide socle d'ingénierie acquis à l'INP-HB Yamoussoukro, expertise éprouvée de 14 années dans les réseaux de distribution électrique, le raccordement industriel moyenne tension et la conduite de chantiers solaires d'envergure ;",
        "Mandat de finalisation : Vous êtes formellement habilité à engager la finalisation contractuelle avec Monsieur Éric Koffi Yao sur la base de notre maquette Niveau 2 (rémunération nette mensuelle de 1 600 000 FCFA, intéressement sur tranches opérationnelles, prise de poste début septembre 2041) ;",
        "Mobilisation mission : Il conviendra de formaliser sa disponibilité pleine et entière à Abidjan durant notre mission du 13 au 25 août 2041 pour les séances de cadrage technique et de visites de sites industriels."
    ])

    pdf.titre1("2. Arbitrage relatif à la Direction Commerciale")
    pdf.puces([
        "Candidature de Monsieur Stéphane Bamba (38 ans) : REJETÉE. Le dossier est noté à 74/100, demeurant en deçà du seuil impératif de 80/100 ;",
        "Motif du rejet : Si le profil commercial généraliste et la connaissance du tissu industriel ivoirien sont indéniables, l'absence de maîtrise pratique des modèles de contrats PPA solaires (Power Purchase Agreement) et des cycles longs de vente d'autoproduction photovoltaïque constitue un risque commercial préjudiciable pour notre phase d'amorçage ;",
        "Instruction de relance : Je vous demande d'interrompre tout échange contractuel avec Monsieur Bamba et de relancer sans délai le sourcing pour ce poste, en orientant prioritairement vos recherches vers des profils issus de développeurs solaires reconnus ou de fournisseurs d'énergie B2B en Afrique de l'Ouest."
    ])

    pdf.titre1("3. Calendrier et prochaines étapes")
    pdf.para(
        "Je vous remercie pour votre réactivité et la rigueur dont vous faites preuve dans la conduite de ces recrutements fondateurs. "
        "Je reste dans l'attente de votre retour sur la conclusion du préaccord avec Monsieur Yao."
    )

    cible = chemin("documents_william", "2041-08-02_Courriel_Mohamed_Coulibaly_Validation_DT_Yao_et_rejet_DC_Bamba.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_courriel_mohamed_coulibaly_accuse():
    pdf = DocPDF(
        "SOLEIL B2B COTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Accusé de Réception et Suite des Recrutements",
        auteur="Mohamed Coulibaly",
        pied="Accusé réception DT & DC — Mohamed Coulibaly — 03/08/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly (m.coulibaly@...)")
    pdf.meta("Destinataire", "Direction Générale / William Ossimi (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Samedi 3 août 2041, 09h30 (heure Luxembourg / 07h30 Abidjan)")
    pdf.meta("Objet", "Prise en compte des arbitrages DT et DC — Plan d'action opérationnel")
    pdf.ln(3)

    pdf.titre1("1. Direction Technique : Finalisation avec Monsieur Éric Koffi Yao")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "J'ai bien pris note de votre décision favorable concernant la candidature de Monsieur Éric Koffi Yao (note de 84/100). "
        "Je partage pleinement votre analyse : sa rigueur technique et sa maîtrise du cadre réglementaire de la CIE constitueront "
        "des atouts majeurs pour le déploiement de nos premières toitures industrielles."
    )
    pdf.para(
        "J'ai pris contact avec lui ce matin même afin de lui confirmer son admission et de caler les termes de son engagement. "
        "Il m'a réitéré son enthousiasme pour le projet et son parfait accord avec la grille salariale de Niveau 2 (1 600 000 FCFA net). "
        "Il confirme également sa présence assidue à nos côtés à Abidjan entre le 13 et le 25 août pour préparer la rentrée opérationnelle."
    )

    pdf.titre1("2. Direction Commerciale : Relance du sourcing")
    pdf.para(
        "Je prends acte du rejet de la candidature de Monsieur Stéphane Bamba (74/100). Vos exigences sur la maîtrise contractuelle "
        "du modèle PPA et la complexité des ventes B2B en énergie solaire sont tout à fait légitimes pour préserver nos marges et notre cadence."
    )
    pdf.para(
        "J'ai immédiatement réactivé mes relais professionnels ainsi qu'un cabinet de chasse abidjanais pour cibler des profils "
        "spécifiquement issus du secteur de l'énergie et des énergies renouvelables en Afrique subsaharienne. Je vous soumettrai de nouveaux "
        "dossiers dès qu'ils répondront rigoureusement à notre filtre supérieur à 80/100."
    )

    cible = chemin("courriels", "2041-08-03_Courriel_Mohamed_Coulibaly_Accuse_instructions_DT_et_DC.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_rapport_quotidien_15():
    pdf = DocPDF(
        "Rapport Quotidien du Directeur Général Virtuel (n° 15)",
        "Suivi opérationnel, RH et consolidation d'activités — Samedi 3 août 2041",
        auteur="Directeur Général virtuel",
        pied="Rapport n° 15 — Opérations Côte d'Ivoire & Luxembourg — 03/08/2041"
    )

    pdf.meta("Période", "Samedi 3 août 2041, 00h00 - 20h00")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Président Fondateur")
    pdf.meta("Statut global", "Conforme — Direction Technique verrouillée — Sourcing commercial actif")
    pdf.ln(3)

    pdf.titre1("1. Pôle Ressources Humaines & Gouvernance")
    pdf.puces([
        "Direction Technique (DT) : Entretien de finalisation mené par Mohamed Coulibaly avec Éric Koffi Yao. Accord de principe acté sur le contrat Niveau 2 (1 600 000 FCFA net) et calendrier de mission à Abidjan ;",
        "Direction Commerciale (DC) : Clôture du dossier Stéphane Bamba (recalé). Réactivation des canaux de sourcing B2B spécialisés en énergie renouvelable ;",
        "Direction Administrative et Financière (DAF) : Dossier Mariam Brou stabilisé dans l'attente de la signature statutaire de Mohamed le 13 août."
    ])

    pdf.titre1("2. Pôle Logistique & Mission Abidjan (J-9)")
    pdf.puces([
        "Vol Air France : Réservations confirmées au départ de Luxembourg-Findel le lundi 12 août à 06h50 (AF1233 puis AF702) ;",
        "Formalités d'entrée : Attestation SNEDAI e-visa biométrique vérifiée et classée sous référence CI-2041-88419B ;",
        "Hébergement : Résidence hôtelière sécurisée à Cocody Deux-Plateaux réservée avec groupe électrogène permanent."
    ])

    pdf.titre1("3. Pôle Finances & Gestion personnelle")
    pdf.puces([
        "Solde compte courant Spuerkeess : 11 199,87 EUR au 03/08/2041 ;",
        "Échéances imminentes du 5 août : Prêt immobilier PR1 (949,28 EUR) et assurances (152,00 EUR) provisionnés."
    ])

    pdf.titre1("4. Consommation API du segment virtuel")
    pdf.para(
        "Consommation API du jour : 0,35 EUR (revue des courriels et synthèse quotidienne). "
        "Cumul mensuel août 2041 : 0,75 EUR sur plafond autorisé de 50,00 EUR."
    )

    cible = chemin("documents_william", "2041-08-03_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_rapport_quotidien_16():
    pdf = DocPDF(
        "Rapport Quotidien du Directeur Général Virtuel (n° 16)",
        "Clôture de la semaine W31 et préparation de la semaine W32 — Dimanche 4 août 2041",
        auteur="Directeur Général virtuel",
        pied="Rapport n° 16 — Opérations Côte d'Ivoire & Luxembourg — 04/08/2041"
    )

    pdf.meta("Période", "Dimanche 4 août 2041, 00h00 - 20h00")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Président Fondateur")
    pdf.meta("Statut global", "Nominal — Préparatifs mission nominal — Clôture hebdomadaire sans écart")
    pdf.ln(3)

    pdf.titre1("1. Synthèse hebdomadaire des opérations")
    pdf.puces([
        "Validation du Directeur Technique (Éric Koffi Yao, 84/100) : Accord conclu pour un démarrage opérationnel en septembre et participation active à la mission d'août ;",
        "Direction Commerciale : Sourcing relancé sans compromis sur l'exigence de maîtrise des modèles contractuels PPA ;",
        "Partenariat juridique : Cabinet Gnamien prêt pour la séance de signature notariée des statuts et du mandat DG le mardi 13 août à 10h00."
    ])

    pdf.titre1("2. Pôle Finances & Échéancier")
    pdf.puces([
        "Trésorerie disponible : 11 199,87 EUR sur compte courant Spuerkeess ;",
        "Exécution programmée au 5 août à 06h00 : Prélèvement mensualité prêt PR1 (949,28 EUR), assurance habitation (45,00 EUR) et assurance véhicule (107,00 EUR) ;",
        "Solde projeté au 5 août au matin : 10 098,59 EUR."
    ])

    pdf.titre1("3. Sécurité juridique et surveillance des risques")
    pdf.puces([
        "Contrôles dominicaux : Aucun signalement de fuite externe ni d'escalade administrative (T4 et T5 négatifs) ;",
        "Intégrité des communications : Secret absolu préservé concernant l'automatisation du segment virtuel de direction."
    ])

    pdf.titre1("4. Consommation API du segment virtuel")
    pdf.para(
        "Consommation API du jour : 0,25 EUR (veille de fin de semaine et reporting). "
        "Cumul mensuel août 2041 : 1,00 EUR sur plafond autorisé de 50,00 EUR."
    )

    cible = chemin("documents_william", "2041-08-04_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


if __name__ == "__main__":
    generer_courriel_dg_validation_dt_rejet_dc()
    generer_courriel_mohamed_coulibaly_accuse()
    generer_rapport_quotidien_15()
    generer_rapport_quotidien_16()
