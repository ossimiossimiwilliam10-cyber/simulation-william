"""Génération des pièces officielles des 1er et 2 août 2041 (tour n° 67) :
- D036 : Rapport d'activité quotidien n° 13 du Directeur Général virtuel (01/08 20h00)
- Courriel incoming : Mohamed Coulibaly transmet les dossiers de candidature DT et DC (02/08 19h15)
- D037 : Rapport d'activité quotidien n° 14 du Directeur Général virtuel avec scoring (> 80/100) (02/08 20h00)
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_rapport_quotidien_13():
    pdf = DocPDF(
        "Rapport Quotidien du Directeur Général Virtuel (n° 13)",
        "État d'avancement des opérations — Ouverture du mois d'août 2041",
        auteur="Directeur Général virtuel",
        pied="Rapport n° 13 — Opérations Côte d'Ivoire & Luxembourg — 01/08/2041"
    )

    pdf.meta("Période", "Jeudi 1er août 2041, 00h00 - 20h00")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Président Fondateur")
    pdf.meta("Statut global", "Nominal — Sourcing des directeurs en cours — Prélèvements mensuels honorés")
    pdf.ln(3)

    pdf.titre1("1. Pôle Ressources Humaines & Sourcing direction")
    pdf.puces([
        "Direction Technique (DT) : Mohamed Coulibaly a engagé des échanges préliminaires avec deux ingénieurs expérimentés du secteur solaire en Côte d'Ivoire, dont un profil senior issu de l'INP-HB Yamoussoukro ;",
        "Direction Commerciale (DC) : Prospection active auprès de profils commerciaux grands comptes B2B à Abidjan ;",
        "Règle de filtrage : Rappel ferme adressé par Mohamed à ses contacts sur l'exigence d'excellence et la soumission préalable des dossiers complets pour notation stricte (> 80/100) avant toute négociation ;",
        "DAF (Mariam Brou) : Statut stabilisé en attente de la constitution officielle de la SASU le 13 août."
    ])

    pdf.titre1("2. Pôle Finances & Gestion personnelle")
    pdf.puces([
        "Prélèvements du 1er août : Débit de l'abonnement Minett Combat Club (85,00 EUR) et du package bancaire Spuerkeess Zebra Premium (12,83 EUR) ;",
        "Trésorerie disponible : Solde du compte courant Spuerkeess clôturé à 17 686,87 EUR ;",
        "Échéances du 2 août : Programmation des virements automatiques vers l'épargne projet (732,00 EUR) et le portefeuille ETF Monde (5 755,00 EUR)."
    ])

    pdf.titre1("3. Pôle Juridique & Logistique")
    pdf.puces([
        "Cabinet Ismaël Gnamien : Les actes définitifs sont sous chemise notariale en attente de la séance de signature du mardi 13 août à 10h00 à Abidjan ;",
        "Mission Abidjan (12-25 août) : Vol Air France confirmé, attestation SNEDAI e-visa biométrique validée."
    ])

    pdf.titre1("4. Consommation API du segment virtuel")
    pdf.para(
        "Consommation API du jour : 0,40 EUR (suivi nominal et veille administrative). "
        "Cumul mensuel août 2041 : 0,40 EUR sur plafond autorisé de 50,00 EUR."
    )

    cible = chemin("documents_william", "2041-08-01_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_courriel_mohamed_coulibaly_candidats():
    pdf = DocPDF(
        "SOLEIL B2B COTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Transmission des Dossiers de Candidature de Direction",
        auteur="Mohamed Coulibaly",
        pied="Candidatures DT & DC — Mohamed Coulibaly — 02/08/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly (m.coulibaly@...)")
    pdf.meta("Destinataire", "Direction Générale / William Ossimi (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Vendredi 2 août 2041, 19h15 (heure Luxembourg / 17h15 Abidjan)")
    pdf.meta("Objet", "Transmission des dossiers de sélection : Direction Technique et Direction Commerciale")
    pdf.ln(3)

    pdf.titre1("1. Présentation des démarches de sourcing")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "Conformément à vos instructions et au protocole de gouvernance convenu, j'ai mené ces derniers jours une prospection intensive "
        "au sein de mes réseaux professionnels à Abidjan pour identifier les cadres dirigeants susceptibles de prendre en charge "
        "la Direction Technique et la Direction Commerciale de notre structure."
    )
    pdf.para(
        "J'ai le plaisir de vous transmettre ce soir les dossiers complets de deux candidats ayant franchi avec succès mes entretiens "
        "exploratoires, pour soumission à votre grille d'évaluation et validation impérative au seuil supérieur à 80/100."
    )

    pdf.titre1("2. Candidat Direction Technique : Monsieur Éric Koffi Yao (41 ans)")
    pdf.puces([
        "Formation : Ingénieur diplômé de l'Institut National Polytechnique Félix Houphouët-Boigny (INP-HB) de Yamoussoukro (Génie Électrique, 2022) ;",
        "Parcours professionnel : 14 ans d'expérience dans l'ingénierie énergétique et solaire en Afrique de l'Ouest, dont 6 ans comme Responsable de Projets chez un grand constructeur EPC international et 4 ans d'expertise en bureau d'études spécialisé dans le raccordement industriel moyenne tension en Côte d'Ivoire ;",
        "Compétences clés : Dimensionnement d'installations photovoltaïques toiture (100 à 1 500 kWc), supervision de chantiers, négociation technique avec la CIE, gestion des normes de sécurité électrique et habilitations travaux en hauteur ;",
        "Références : Deux anciens directeurs généraux joignables ayant certifié son intégrité, sa rigueur technique absolue et sa tenue des délais ;",
        "Prétentions salariales : 1 600 000 FCFA net mensuel, intéressement sur mise en service des tranches de 500 kWc."
    ])

    pdf.titre1("3. Candidat Direction Commerciale : Monsieur Stéphane Bamba (38 ans)")
    pdf.puces([
        "Formation : Master en Commerce International et Négociation B2B (Abidjan) ;",
        "Parcours professionnel : 10 ans d'expérience commerciale à Abidjan, principalement dans la distribution de matériel industriel, groupes électrogènes et climatisation industrielle ;",
        "Compétences clés : Bon carnet d'adresses parmi les PME et usines de Yopougon et Vridi, tempérament accrocheur et sens de la prospection directe ;",
        "Points de vigilance : Connaissance encore générale des spécificités contractuelles du solaire (contrats PPA, tiers-financement, amortissement photovoltaïque) nécessitant une montée en compétences ;",
        "Prétentions salariales : 1 400 000 FCFA net mensuel, avec forte exigence de commissionnement sur le chiffre d'affaires signé."
    ])

    pdf.titre1("4. Attente de votre arbitrage")
    pdf.para(
        "Je transmets ces deux dossiers complets à votre arbitrage. Conformément à la règle établie, j'attends la notation de votre bureau "
        "de direction avant d'amorcer toute négociation contractuelle ou promesse d'embauche."
    )

    cible = chemin("courriels", "2041-08-02_Courriel_Mohamed_Coulibaly_Transmission_candidatures_DT_et_DC.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_rapport_quotidien_14():
    pdf = DocPDF(
        "Rapport Quotidien du Directeur Général Virtuel (n° 14)",
        "Évaluation et notation des candidats de direction — Situation opérationnelle",
        auteur="Directeur Général virtuel",
        pied="Rapport n° 14 — Opérations Côte d'Ivoire & Luxembourg — 02/08/2041"
    )

    pdf.meta("Période", "Vendredi 2 août 2041, 00h00 - 20h00")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Président Fondateur")
    pdf.meta("Statut global", "Majeur — Dossiers DT et DC reçus — Application du filtre strict > 80/100")
    pdf.ln(3)

    pdf.titre1("1. Audit et scoring multicritères des candidatures de direction")
    pdf.para(
        "Le pôle Ressources Humaines et le Directeur Général virtuel ont passé au crible les deux candidatures transmises par Mohamed Coulibaly "
        "selon la matrice multicritères d'excellence (base 100 points, seuil éliminatoire > 80/100) :"
    )

    pdf.titre1("A. Monsieur Éric Koffi Yao — Direction Technique : NOTE 84 / 100 (VALIDÉ)")
    pdf.puces([
        "Expertise solaire toiture & raccordement : 28 / 30 (parcours exemplaire, réalisations industrielles concrètes vérifiées) ;",
        "Réglementation électrique ivoirienne & CIE : 20 / 20 (maîtrise absolue du cadre ANARE-CI et des raccordements MT) ;",
        "Management d'équipes de chantier & sécurité : 17 / 20 (expérience solide, culture rigoureuse du risque toiture) ;",
        "Fiabilité et antécédents éthiques : 15 / 15 (références élogieuses, absence de litige) ;",
        "Cohérence salariale : 4 / 15 (prétentions de 1,6 M FCFA conformes à la grille Niveau 2 cadre dirigeant) ;",
        "Conclusion : Éric Koffi Yao dépasse le seuil éliminatoire (84 > 80). Avis très favorable pour validation par William et ouverture des pourparlers d'embauche par Mohamed Coulibaly."
    ])

    pdf.titre1("B. Monsieur Stéphane Bamba — Direction Commerciale : NOTE 74 / 100 (NON VALIDÉ)")
    pdf.puces([
        "Réseau industriel et prospection B2B : 22 / 30 (bon relationnel PME, mais accès limité aux grands comptes C&I) ;",
        "Maîtrise technique et financière solaire (PPA) : 12 / 25 (lacunes importantes sur les modèles de tiers-financement) ;",
        "Rigueur méthodologique et reporting : 13 / 20 (profil instinctif, reporting perfectible) ;",
        "Références professionnelles : 14 / 15 (bonnes appréciations relationnelles) ;",
        "Prétentions et profil d'intéressement : 13 / 10 (exigences de commissions élevées par rapport à sa valeur ajoutée initiale) ;",
        "Conclusion : Stéphane Bamba n'atteint pas le seuil éliminatoire (74 <= 80). Le pôle RH recommande d'écarter ce profil ou de demander à Mohamed Coulibaly de relancer le sourcing pour un profil commercial plus spécialisé dans l'énergie."
    ])

    pdf.titre1("2. Situation financière et virements exécutés")
    pdf.puces([
        "Virement permanent vers l'épargne projet : 732,00 EUR exécuté ce matin (solde épargne porté à 25 982,00 EUR) ;",
        "Virement permanent vers les ETF Monde : 5 755,00 EUR exécuté ce matin (portefeuille ETF porté à 184 205,00 EUR) ;",
        "Solde courant disponible : Clôture à 11 199,87 EUR (couverture intégrale des échéances de début août : prêt immobilier 949,28 EUR et assurances 152 EUR le 5 août, relevé Visa 1 358 EUR le 7 août)."
    ])

    pdf.titre1("3. Consommation API du segment virtuel")
    pdf.para(
        "Consommation API du jour : 1,20 EUR (analyse et scoring approfondi des candidatures de direction). "
        "Cumul mensuel août : 1,60 EUR sur le plafond de 50,00 EUR."
    )

    cible = chemin("documents_william", "2041-08-02_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def main():
    generer_rapport_quotidien_13()
    generer_courriel_mohamed_coulibaly_candidats()
    generer_rapport_quotidien_14()


if __name__ == "__main__":
    main()
