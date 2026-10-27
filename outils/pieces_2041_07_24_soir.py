"""PIÈCES DU 24/07/2041 SOIR (univers 3, tour n° 49) :
Courriel officiel d'acceptation de mission, transmission du dossier KYC et demande de RIB
adressé au Cabinet d'Avocats Ismaël Gnamien & Associés à Abidjan (24 juillet 2041, 20h08).

Génération du fichier PDF physique (règle 4 et directives de William)
déposé dans `documents_william/` et référencé dans l'application Gestion / Téléphone.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_gnamien_acceptation():
    pdf = DocPDF(
        "Projet Solaire B2B Abidjan — Acceptation de Mission & KYC",
        "Transmission au Cabinet d'Avocats Ismaël Gnamien & Associés · Abidjan (RCI)",
        auteur="William Ossimi, Associé Unique & Investisseur",
        pied="Projet Solaire B2B Abidjan — Acceptation mission Cabinet Gnamien"
    )

    pdf.meta("Émetteur", "Monsieur William Ossimi, Associé Unique et Investisseur (Audun-le-Tiche / Luxembourg)")
    pdf.meta("Destinataire", "Maître Ismaël Gnamien, Avocat à la Cour, Barreau d'Abidjan")
    pdf.meta("Date et heure", "Mercredi 24 juillet 2041, 20h08 (heure de Luxembourg / 18h08 Abidjan)")
    pdf.meta("Objet", "Acceptation formelle de la convention d'honoraires, transmission KYC et demande de RIB bancaire")
    pdf.ln(3)

    pdf.titre1("1. Acceptation formelle de la convention d'assistance juridique")
    pdf.para(
        "Maître,"
    )
    pdf.para(
        "J'accuse formellement réception de la convention d'assistance juridique et du dossier d'identification client (KYC) "
        "transmis ce jour par votre cabinet pour la constitution et l'immatriculation de la société Projet Solaire B2B Abidjan SAS."
    )
    pdf.para(
        "Par la présente, je vous confirme mon accord plein et entier sur l'ensemble des termes de votre convention, notamment :"
    )
    pdf.puces([
        "Le forfait global ferme et définitif de 2 100 000 FCFA Hors Taxes (soit environ 3 200 € HT / 2 478 000 FCFA TTC) ;",
        "L'échelonnement convenu : premier acompte de 40 % à la signature (991 200 FCFA TTC, ≈ 1 511 €), deuxième acompte de 40 % "
        "au dépôt CEPICI, et solde de 20 % à la délivrance de l'immatriculation RCCM et des statuts enregistrés ;",
        "Le périmètre complet : rédaction personnalisée des Statuts de SAS régie par l'Acte Uniforme OHADA, rédaction du Pacte d'Associés, "
        "enregistrement de la Convention de Mandat Social du Directeur Général, formalités au CEPICI, déclaration fiscale et Journal Officiel."
    ])

    pdf.titre1("2. Transmission des éléments du dossier d'identification client (KYC)")
    pdf.para(
        "Afin de satisfaire aux obligations légales de conformité et de lutte contre le blanchiment de capitaux (dispositions CENTIF / UEMOA), "
        "vous trouverez ci-joint les pièces justificatives requises :"
    )
    pdf.puces([
        "Copie numérique certifiée conforme de mon passeport en cours de validité (ressortissant communautaire) ;",
        "Justificatif de domicile récent attestant de ma résidence principale à Audun-le-Tiche (Moselle) ;",
        "Attestation sur l'honneur confirmant l'origine licite des capitaux investis, issus de mon épargne salariale personnelle "
        "constituée dans le cadre de mes fonctions d'enseignant titulaire de la fonction publique d'État au Grand-Duché de Luxembourg."
    ])
    pdf.para(
        "Je réitère formellement que mon intervention s'exerce à titre d'associé unique non-gérant et investisseur en fonds propres, "
        "exclusif de toute fonction d'administration ou de gérance exécutive locale, conformément aux exigences de l'article 14 du statut "
        "général des fonctionnaires luxembourgeois."
    )

    pdf.titre1("3. Demande de coordonnées bancaires (RIB / IBAN)")
    pdf.para(
        "Je vous remercie de bien vouloir me transmettre en retour les coordonnées bancaires officielles de votre cabinet (RIB / IBAN "
        "du compte séquestre CARPA du Barreau d'Abidjan ou compte professionnel de votre cabinet auprès d'un établissement bancaire agréé) "
        "afin que je puisse ordonner sans délai le virement bancaire international correspondant au premier acompte de 991 200 FCFA TTC (≈ 1 511 €)."
    )
    pdf.para(
        "Dès confirmation de la mise en place de ce règlement, vous disposerez de mon plein accord pour engager les travaux de rédaction "
        "des statuts et du pacte d'associés."
    )
    pdf.para(
        "Restant à votre entière disposition pour tout élément complémentaire, je vous prie d'agréer, Maître, l'expression de mes salutations distinguées."
    )
    pdf.para(
        "William Ossimi — Associé Unique et Investisseur",
        italique=True
    )

    fichier_sortie = chemin("documents_william", "2041-07-24_Courriel_Cabinet_Gnamien_Acceptation_mission_et_demande_RIB.pdf")
    pdf.sauver(fichier_sortie)
    return fichier_sortie


if __name__ == "__main__":
    f = generer_courriel_gnamien_acceptation()
    print("Courriel généré avec succès.")

