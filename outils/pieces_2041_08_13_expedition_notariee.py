"""
Génération de l'Expédition Notariée et Recueil des Actes Signés et Scellés
Cabinet Notarial Maître Ismaël Gnamien — Abidjan Plateau
Mardi 13 août 2041 — Séance solennelle d'immatriculation
"""
import sys
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_expedition_notariee():
    pdf = DocPDF(
        "ÉTUDE NOTARIALE DE MAÎTRE ISMAËL GNAMIEN — ABIDJAN PLATEAU",
        "Expédition Notariée : Dépôt, Enregistrement et Scellement des Actes Constitutifs de SOLEIL B2B CI SASU",
        auteur="Cabinet Notarial Maître Ismaël Gnamien",
        pied="Expédition Notariée Certifiée Conforme — Réf. GNAM-2041/08-8842 — 13/08/2041"
    )

    pdf.meta("Office notarial", "Maître Ismaël Gnamien, Notaire à la Résidence d'Abidjan-Plateau (Côte d'Ivoire)")
    pdf.meta("Soussigné", "Monsieur William Ossimi, Associé Unique Fondateur")
    pdf.meta("Dirigeant nommé", "Monsieur Mohamed Coulibaly, Président-Directeur Général")
    pdf.meta("Cadre de direction", "Madame Mariam Brou, Directrice Administrative et Financière")
    pdf.meta("Date des actes", "Mardi 13 août 2041, 10h00")
    pdf.meta("Dépôt CEPICI", "Récépissé officiel d'enregistrement n° CI-ABJ-2041-D-08842")
    pdf.ln(3)

    pdf.titre1("1. Attestation de signature solennelle et conservation des minutes")
    pdf.para(
        "Par-devant Maître Ismaël Gnamien, Notaire soussigné, titulaire d'un office notarial à Abidjan-Plateau, ont comparu "
        "ce mardi 13 août 2041 à 10h00 : Monsieur William Ossimi, de nationalité luxembourgeoise, demeurant à Audun-le-Tiche (France) ; "
        "Monsieur Mohamed Coulibaly, de nationalité ivoirienne, cadre bancaire et dirigeant d'entreprise ; et Madame Mariam Brou, "
        "de nationalité ivoirienne, cadre de gestion financière."
    )
    pdf.para(
        "Le Notaire soussigné certifie que l'ensemble des actes constitutifs a été signé en personne par les comparants en cinq originaux "
        "sous chemise officielle notariée, après lecture intégrale et vérification des identités. Un original a été déposé au rang "
        "des minutes de l'Étude sous le numéro 2041/ACT-0813, et trois originaux ont été transmis sous bordereau officiel au Centre "
        "de Promotion des Investissements en Côte d'Ivoire (CEPICI) pour formalités de publicité légale et attribution du RCCM."
    )

    pdf.titre1("2. Inventaire certifié conforme des actes signés et scellés")
    entetes_actes = ["Intitulé de l'acte", "Parties signataires", "Nature juridique", "Statut d'enregistrement"]
    lignes_actes = [
        ["Statuts SASU SOLEIL B2B CI", "William Ossimi (Associé Unique)", "Acte sous seing privé notarié", "Déposé CEPICI (Réf. 08842)"],
        ["Décisions constitutif Associé Unique", "William Ossimi (Associé Unique)", "Procès-Verbal souverain", "Enregistré aux minutes"],
        ["Convention de Mandat Social DG", "W. Ossimi & M. Coulibaly", "Mandat social exécutif OHADA", "Scellé & exécutoire"],
        ["Contrat de travail DAF", "M. Coulibaly & Mariam Brou", "Contrat CDI Cadre Dirigeant", "Validé par l'Associé Unique"],
        ["Convention Prêt d'Associé (CCA)", "W. Ossimi & M. Coulibaly", "Convention de trésorerie bloquée", "Soumis à la DAF"]
    ]
    pdf.tableau(entetes_actes, lignes_actes, [50, 45, 55, 45])

    pdf.titre1("3. Mentions légales et formule exécutoire notariée")
    pdf.para(
        "Le Notaire soussigné atteste que les signatures apposées sur lesdits actes sont authentiques et engagent pleinement "
        "les parties conformément aux dispositions de l'Acte Uniforme OHADA relatif au droit des sociétés commerciales et du GIE. "
        "La présente expédition certifiée conforme fait pleine foi des conventions intervenues."
    )
    pdf.puces([
        "Capital social souscrit et libéré : 1 000 000 FCFA intégralement constaté sur attestation bancaire CARPA ;",
        "Régime fiscal d'enregistrement : Droit fixe d'enregistrement acquitté auprès du receveur des impôts du Plateau ;",
        "Délivrance de l'extrait RCCM : Attestation définitive prévue sous 24 à 48 heures ouvrées par le guichet unique du CEPICI."
    ])

    pdf.para(
        "Fait et délivré à Abidjan-Plateau, en l'Étude de Maître Ismaël Gnamien, le treize août deux mille quarante-et-un. "
        "Scellé du sceau de l'Office Notarial."
    )

    fichier_pdf = RACINE / "documents_william" / "2041-08-13_Cabinet_Gnamien_Expedition_Notariee_et_Actes_Signes_Scelles.pdf"
    pdf.sauver(str(fichier_pdf))
    print(f"Expédition notariée générée : {fichier_pdf}")


if __name__ == "__main__":
    generer_expedition_notariee()

