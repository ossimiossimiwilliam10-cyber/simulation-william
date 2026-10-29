"""
Génération des pièces officielles du vendredi 16 août 2041, 18h30 (Tour n° 98) :
1. Avis d'opéré Spuerkeess S-Net : Virement compte à compte interne de 8 000 EUR (Épargne Projet -> Courant)
2. Courriel officiel de Mohamed Coulibaly : Retour d'expérience sur le démarrage, sentiment général et gestion autonome des devis du QG
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_avis_virement_interne():
    pdf = DocPDF(
        "BANQUE ET CAISSE D'ÉPARGNE DE L'ÉTAT, LUXEMBOURG (SPUERKEESS)",
        "Avis d'Opéré — Virement Interne de Compte à Compte (S-Net Mobile)",
        auteur="Spuerkeess — Banque Digitale & Tenue de Comptes",
        pied="Avis d'Opéré Virement Interne — Spuerkeess S-Net — 16/08/2041"
    )

    pdf.meta("Émetteur", "Banque et Caisse d'Épargne de l'État, Luxembourg (BCEE / Spuerkeess)")
    pdf.meta("Titulaire des comptes", "Monsieur William Ossimi")
    pdf.meta("Compte émetteur (débit)", "Compte Épargne Projet — LU34 0019 4006 4472 0100")
    pdf.meta("Compte bénéficiaire (crédit)", "Compte Courant Zebra Premium — LU28 0019 4006 4472 0000")
    pdf.meta("Date et heure d'exécution", "Vendredi 16 août 2041, 15h50 (heure Luxembourg / 13h50 UTC)")
    pdf.meta("Référence transaction", "TRANS-BCEE-20410816-INT-08000")
    pdf.meta("Canal d'authentification", "S-Net Mobile — Session sécurisée LuxTrust")
    pdf.ln(3)

    pdf.titre1("1. Caractéristiques de l'opération interne")
    pdf.para(
        "Nous vous confirmons l'enregistrement et l'exécution immédiate du virement interne ordonné "
        "entre vos comptes Spuerkeess via votre application mobile S-Net :"
    )

    entetes_op = ["Paramètre de l'ordre", "Valeur enregistrée"]
    lignes_op = [
        ["Montant transféré", "8 000,00 EUR"],
        ["Frais d'opération", "0,00 EUR (Gratuit entre comptes propres Spuerkeess)"],
        ["Date d'effet comptable", "16 août 2041 (Immédiat)"],
        ["Date de valeur débit", "16 août 2041"],
        ["Date de valeur crédit", "16 août 2041"],
        ["Nouveau solde Compte Épargne Projet", "67 982,00 EUR"],
        ["Nouveau solde Compte Courant Zebra Premium", "8 243,99 EUR"],
        ["Motif renseigné par le titulaire", "Reconstitution liquidités de précaution compte courant"],
        ["Référence interne", "VIR-INT-20410816-01"]
    ]
    pdf.tableau(entetes_op, lignes_op, [80, 110])

    pdf.ln(3)
    pdf.titre1("2. Situation de trésorerie disponible")
    pdf.para(
        "Le montant viré est immédiatement disponible pour vos opérations courantes, prélèvements et cartes bancaires. "
        "Votre portefeuille de titres (ETF Monde) demeure inchangé et poursuit sa valorisation sans arbitrage."
    )

    sortie = chemin("documents_william", "2041-08-16_Avis_Virement_Interne_Spuerkeess_Epargne_Courant.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


def generer_courriel_sentiment_coulibaly():
    pdf = DocPDF(
        "SOLEIL B2B CÔTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Note d'Étape & Ressenti Personnel du Démarrage",
        auteur="Mohamed Coulibaly",
        pied="Ressenti Démarrage & Aménagement Vallons — SOLEIL B2B CI — 16/08/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly, Directeur Général (m.coulibaly@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Associé Unique Fondateur (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Vendredi 16 août 2041, 18h15 (heure d'Abidjan)")
    pdf.meta("Objet", "Retour d'expérience sur notre première semaine, sentiment général et pilotage autonome des devis")
    pdf.ln(3)

    pdf.titre1("1. Mon sentiment sur le démarrage de SOLEIL B2B CÔTE D'IVOIRE")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "Je vous remercie sincèrement pour votre message et pour l'attention que vous portez à mon ressenti personnel. "
        "Dans la culture d'entreprise ivoirienne, il est rare qu'un dirigeant et actionnaire prenne ainsi le pouls de son directeur général "
        "avec autant de bienveillance et de franchise directe. Je vous en sais infiniment gré."
    )
    pdf.para(
        "Si je devais résumer mon sentiment en un mot : impressionnant. En à peine une semaine, nous avons accompli ce que beaucoup de "
        "structures mettent six mois à poser. La constitution notariée avec Maître Gnamien, l'immatriculation au CEPICI, l'ouverture et "
        "la capitalisation du compte à la Société Générale, le bail commercial de la villa des Vallons signé avec quinze jours de franchise, "
        "et surtout la constitution complète de l'équipe de Direction Niveau 2 (Mariam Brou, Éric Yao, Viviane Tanoh). "
        "C'est une dynamique galvanisante."
    )

    pdf.titre1("2. Concernant le rythme et la charge de travail")
    pdf.para(
        "Pour être totalement honnête avec vous, le rythme est particulièrement soutenu — c'est du sport de haut niveau ! "
        "Mais ce n'est en rien une charge excessive ou écrasante, pour une raison essentielle : vos arbitrages tombent avec une clarté, "
        "une précision et une rapidité remarquables. Dans mon parcours professionnel antérieur, ce qui épuise un dirigeant, c'est l'indécision, "
        "les allers-retours politiques et le flou stratégique. Avec vous, chaque réponse est nette, chiffrée et immédiatement actionnable. "
        "Cela supprime 90 % du stress parasite."
    )
    pdf.para(
        "De plus, la collaboration avec Mariam Brou est extrêmement fluide. Elle abat un travail préparatoire rigoureux qui me soulage "
        "considérablement sur les aspects administratifs et financiers. Je me sens pleinement soutenu et valorisé dans mes prérogatives."
    )

    pdf.titre1("3. Pilotage des devis d'aménagement et visite du week-end")
    pdf.para(
        "Conformément à vos directives d'autonomie, je prends en main dès demain matin la consultation des prestataires "
        "(peinture/rafraîchissement, climatisation réversible, câblage réseau fibre sécurisé, onduleurs et mobilier de bureau). "
        "Je veillerai à mettre en concurrence au minimum deux à trois artisans locaux réputés pour obtenir les meilleurs rapports qualité/prix "
        "dans le respect strict du cadrage budgétaire de 20 millions FCFA."
    )
    pdf.para(
        "Concernant votre venue à la villa des Vallons ce week-end, c'est une excellente nouvelle. Les clés sont entre mes mains. "
        "Je suis à votre entière disposition samedi ou dimanche, selon l'horaire qui vous conviendra le mieux, pour vous faire découvrir les locaux "
        "et vous présenter la configuration spatiale des différents pôles."
    )

    sortie = chemin("courriels", "2041-08-16_Courriel_Mohamed_Coulibaly_Retour_Sentiment_Demarrage_et_Organisation_Devis.pdf")
    pdf.sauver(sortie)
    print(f"Document généré : {sortie}")


if __name__ == "__main__":
    generer_avis_virement_interne()
    generer_courriel_sentiment_coulibaly()
