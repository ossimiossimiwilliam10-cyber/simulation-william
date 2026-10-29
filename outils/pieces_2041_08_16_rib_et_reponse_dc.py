"""
Génération des pièces officielles du vendredi 16 août 2041, 13h35 (Tour n° 96) :
1. Attestation bancaire d'ouverture de compte et RIB officiel SGCI pour SOLEIL B2B CI SASU
2. Courriel de Mohamed Coulibaly : accusé de sélection DC, bilan équipe de direction et transmission RIB
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_attestation_rib_sgci():
    pdf = DocPDF(
        "SOCIÉTÉ GÉNÉRALE CÔTE D'IVOIRE (SGCI) — Pôle Grandes Entreprises",
        "Attestation d'Ouverture de Compte Professionnel & Relevé d'Identité Bancaire (RIB)",
        auteur="Direction de la Clientèle Entreprises — Agence Principale Plateau",
        pied="Attestation SGCI & RIB Officiel — SOLEIL B2B CÔTE D'IVOIRE SASU — 16/08/2041"
    )

    pdf.meta("Établissement émetteur", "Société Générale Côte d'Ivoire (SGCI) — Agence Centrale du Plateau, Abidjan")
    pdf.meta("Destinataire / Titulaire", "SOLEIL B2B CÔTE D'IVOIRE SASU")
    pdf.meta("Représentant légal", "Monsieur Mohamed Coulibaly, Directeur Général")
    pdf.meta("Associé Unique Fondateur", "Monsieur William Ossimi")
    pdf.meta("Date d'établissement", "Vendredi 16 août 2041, 13h15 (heure d'Abidjan)")
    pdf.meta("Référence dossier", "SGCI-ENT-2041-0816-0042 / SOLEIL-B2B-CI")
    pdf.ln(3)

    pdf.titre1("1. Attestation officielle d'ouverture de compte")
    pdf.para(
        "La Société Générale Côte d'Ivoire (SGCI), société anonyme au capital de 15 555 555 000 FCFA, régie par la réglementation "
        "bancaire de l'UMOA, certifie par la présente avoir ouvert ce jour dans ses livres un compte courant professionnel au nom de :"
    )
    pdf.para(
        "• Dénomination sociale : SOLEIL B2B CÔTE D'IVOIRE SASU\n"
        "• Forme juridique : Société par Actions Simplifiée Unipersonnelle\n"
        "• Capital social : 1 000 000 FCFA entièrement libéré\n"
        "• Immatriculation RCCM : CI-ABJ-03-2041-B16-04821 (Tribunal de Commerce d'Abidjan)\n"
        "• Identifiant Unique (IDU) : CI-2041-0089421-E\n"
        "• Siège social : Villa Duplex QG, Deux-Plateaux Vallons, Commune de Cocody, Abidjan"
    )
    pdf.para(
        "Le dossier juridique et les vérifications de conformité (KYC / LCB-FT) ont été formellement validés par notre direction juridique. "
        "Le compte est pleinement actif pour recevoir des virements nationaux et internationaux en devises et en francs CFA (XOF)."
    )

    pdf.titre1("2. Relevé d'Identité Bancaire officiel (Norme UEMOA / SWIFT)")
    entetes_rib = ["Élément d'identification bancaire", "Coordonnées certifiées conformes"]
    lignes_rib = [
        ["Nom de la banque", "Société Générale Côte d'Ivoire (SGCI)"],
        ["Code Banque", "CI008"],
        ["Code Guichet / Agence", "01005 (Agence Principale du Plateau, Avenue Delafosse)"],
        ["Numéro de compte", "0120 4589 7102"],
        ["Clé RIB", "83"],
        ["Numéro IBAN (format UEMOA)", "CI93 CI00 8010 0501 2045 8971 0283"],
        ["Code BIC / SWIFT", "SGCB CI AB"],
        ["Devise du compte", "Franc CFA BEAC/BCEAO (XOF)"],
        ["Titulaire officiel", "SOLEIL B2B CÔTE D'IVOIRE SASU"],
        ["Domiciliation de facturation", "Agence Entreprises Plateau, Abidjan (Côte d'Ivoire)"]
    ]
    pdf.tableau(entetes_rib, lignes_rib, [70, 120])

    pdf.ln(3)
    pdf.titre1("3. Modalités de fonctionnement et délégations de signature")
    pdf.para(
        "Le fonctionnement du compte est soumis aux stipulations statutaires de la société et aux procurations bancaires enregistrées :\n"
        "• Signature principale : Monsieur Mohamed Coulibaly, Directeur Général (ordonnancement des opérations courantes et contrats) ;\n"
        "• Co-signature financière : Madame Mariam Brou, Directrice Administrative et Financière (contrôle de gestion et décaissements) ;\n"
        "• Accès consultation & audit souverain : Monsieur William Ossimi, Associé Unique (accès distant permanent en lecture seule et reporting direct)."
    )

    sortie = chemin("courriels", "2041-08-16_SGCI_Attestation_Ouverture_Compte_et_RIB_Officiel_Soleil_B2B_CI.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


def generer_courriel_reponse_coulibaly():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Accusé Sélection DC, Bilan de Direction & Transmission RIB",
        auteur="Mohamed Coulibaly",
        pied="Bilan Direction & RIB Officiel — SOLEIL B2B CI — 16/08/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly, Directeur Général (m.coulibaly@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Vendredi 16 août 2041, 13h35 (heure d'Abidjan)")
    pdf.meta("Objet", "Accusé de sélection Direction Commerciale, bilan de l'équipe de direction Niveau 2 et transmission du RIB officiel")
    pdf.ln(3)

    pdf.titre1("1. Prise d'acte de la sélection commerciale et gestion de la shortlist")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "J'accuse bonne réception de votre décision souveraine portant sélection de Madame Viviane Tanoh au poste de Directrice Commerciale "
        "de SOLEIL B2B CÔTE D'IVOIRE. C'est un arbitrage d'une grande pertinence stratégique : sa vélocité de closing à 45 jours et son partenariat "
        "de crédit-bail bancaire vont nous permettre de sécuriser très rapidement nos premières lignes de facturation auprès du tissu des PME locales."
    )
    pdf.para(
        "J'ai également pris note de votre directive concernant Monsieur Marc-Antoine Kouadio. Je le contacte ce jour avec déférence "
        "pour lui notifier la réserve de sa candidature au sein d'une shortlist d'experts stratégiques prioritaires. Sa remarquable maîtrise "
        "technico-économique des offres anti-délestage et sa rigueur de conformité constituent un atout précieux que nous pourrons mobiliser "
        "sous forme de missions d'ingénierie d'affaires ponctuelles dès que nous aborderons des dossiers industriels lourds à Vridi."
    )

    pdf.titre1("2. Bilan de constitution de l'équipe de Direction (Niveau 2)")
    pdf.para(
        "En réponse à votre demande de bilan, j'ai l'immense satisfaction de vous informer que le Comité de Direction (Niveau 2) "
        "de notre société est désormais INTÉGRALEMENT POURVU et stabilisé :"
    )
    entetes_dir = ["Pôle de Direction", "Titulaire sélectionné", "Statut contractuel", "Date de prise de fonction"]
    lignes_dir = [
        ["Direction Générale (DG)", "Mohamed Coulibaly (41 ans)", "Mandat social signé (13/08)", "Immédiate (en exercice)"],
        ["Direction Administrative & Financière (DAF)", "Mariam Brou (43 ans)", "Contrat Niveau 2 signé (07/08)", "1er octobre 2041"],
        ["Direction Technique (DT)", "Éric Koffi Yao (41 ans)", "Contrat Niveau 2 signé (07/08)", "1er octobre 2041"],
        ["Direction Commerciale (DC)", "Viviane Tanoh (36 ans)", "Contrat Niveau 2 à signer (19/08)", "1er octobre 2041"]
    ]
    pdf.tableau(entetes_dir, lignes_dir, [50, 45, 55, 40])

    pdf.ln(3)
    pdf.para(
        "Il ne manque plus aucun poste de direction générale ou sectorielle. L'armature managériale de Niveau 2 est complète."
    )

    pdf.titre1("3. Déploiement du recrutement en cascade (Niveaux 3 et 4)")
    pdf.para(
        "Conformément au principe de subsidiarité que vous avez posé (le Niveau 1 recrute le Niveau 2, le Niveau 2 recrute les Niveaux 3 et 4), "
        "j'ai instruit Madame Brou, Monsieur Yao et Madame Tanoh de lancer sans tarder la pré-sélection de leurs futurs collaborateurs :"
    )
    pdf.puces([
        "Pôle Technique (DT / Éric Koffi Yao) : Sourcing de 2 chefs d'équipe électriciens photovoltaïques (Niveau 3) et de 4 techniciens monteurs-câbleurs (Niveau 4) habilités aux travaux en hauteur ;",
        "Pôle Commercial (DC / Viviane Tanoh) : Identification de 2 technico-commerciaux expérimentés (Niveau 3) et de 3 prospecteurs juniors de terrain (Niveau 4) pour sillonner Yopougon, Marcory et Vridi ;",
        "Pôle Finance & Support (DAF / Mariam Brou) : Sélection d'un comptable d'exploitation junior (Niveau 3) et finalisation du cahier des charges des prestataires de sécurité gardiennage et intendance QG (Niveau 4)."
    ])
    pdf.para(
        "Les entretiens finals et la signature des contrats de Niveaux 3 et 4 se dérouleront au cours du mois de septembre, afin que l'ensemble "
        "des équipes opérationnelles soit prêt pour l'ouverture effective du QG le 1er octobre."
    )

    pdf.titre1("4. Transmission du RIB officiel et signature du bail de 14h00")
    pdf.para(
        "Je vous transmets en pièce jointe l'attestation officielle de la SGCI certifiant l'ouverture et l'activation immédiate du compte "
        "bancaire professionnel de SOLEIL B2B CÔTE D'IVOIRE SASU (IBAN : CI93 CI00 8010 0501 2045 8971 0283, Code SWIFT : SGCB CI AB). "
        "Votre apport en compte courant d'associé de 8 000 euros (5 250 000 FCFA) peut désormais être exécuté en toute sécurité."
    )
    pdf.para(
        "Je me trouve actuellement en route vers les Deux-Plateaux Vallons. Je vous confirmerai la signature définitive du bail "
        "commercial et la remise des clés dès l'achèvement de la séance de 14h00."
    )

    sortie = chemin("courriels", "2041-08-16_Courriel_Mohamed_Coulibaly_Accuse_Selection_DC_Bilan_Direction_et_Transmission_RIB.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_attestation_rib_sgci()
    generer_courriel_reponse_coulibaly()
