"""Génération des pièces officielles des 29, 30 et 31 juillet 2041 (tour n° 66) :
- D033 : Courriel officiel de la Direction Générale à Mohamed Coulibaly (feu vert DAF, sourcing DT/DC, filtre note > 80/100) (29/07 20h30)
- Courriel incoming : Mohamed Coulibaly accuse réception et confirme l'application du filtre (29/07 20h55)
- Courriel incoming : Mohamed Coulibaly transmet le compte-rendu d'entretien opérationnel avec Mariam Brou (DAF) (30/07 19h30)
- D034 : Rapport d'activité quotidien n° 11 du Directeur Général virtuel (30/07 20h00)
- Aléa A09 : Attestation rectifiée de pré-enrôlement e-visa SNEDAI Côte d'Ivoire (31/07 11h20)
- D035 : Rapport d'activité quotidien n° 12 du Directeur Général virtuel (31/07 20h00)
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))

from pdf_base import DocPDF, chemin


def generer_courriel_mohamed_coulibaly_cadrage():
    pdf = DocPDF(
        "SOLEIL B2B COTE D'IVOIRE (SASU)",
        "Direction Générale — Cadrage Opérationnel et Gouvernance Recrutement",
        auteur="William Ossimi / Direction Générale",
        pied="Soleil B2B CI — Instructions de gouvernance — 29/07/2041"
    )

    pdf.meta("Émetteur", "Direction Générale / William Ossimi (direction@soleil-b2b.ci)")
    pdf.meta("Destinataire", "Monsieur Mohamed Coulibaly (m.coulibaly@...)")
    pdf.meta("Date et heure", "Lundi 29 juillet 2041, 20h30 (heure Luxembourg / 18h30 Abidjan)")
    pdf.meta("Objet", "Finalisation des actes constitutifs, lancement entretien DAF et protocole impératif de recrutement")
    pdf.ln(3)

    pdf.titre1("1. Finalisation des statuts et convention de mandat")
    pdf.para(
        "Monsieur Coulibaly,"
    )
    pdf.para(
        "Faisant suite à nos accords de principe et aux conclusions de notre réunion du 26 juillet, j'ai l'honneur de vous confirmer "
        "que les statuts constitutifs de la SASU SOLEIL B2B COTE D'IVOIRE ainsi que la Convention de Mandat Social de Directeur Général "
        "ont été formellement validés ce jour avec le Cabinet d'Avocats Ismaël Gnamien & Associés."
    )
    pdf.para(
        "Tous les points négociés y figurent rigoureusement : rémunération fixe de 2 000 000 FCFA net, intéressement de 2,5 % du chiffre "
        "d'affaires encaissé, prime annuelle sur rentabilité, clause de non-concurrence de 12 mois à 50 %, et prise d'effet de votre mandat "
        "au 1er octobre 2041. La séance solennelle de signature se tiendra à Abidjan le mardi 13 août 2041 à 10h00 en l'étude de Maître Gnamien, "
        "à laquelle votre présence physique est attendue."
    )

    pdf.titre1("2. Entretien d'évaluation opérationnelle avec Madame Mariam Brou (DAF)")
    pdf.para(
        "Le pôle Ressources Humaines ayant formellement sécurisé la candidature de Madame Mariam Brou et lui ayant transmis la maquette de contrat "
        "cadre Niveau 2 (rémunération cible 1 200 000 FCFA net, reporting SYSCOHADA et audit permanent), vous avez désormais le feu vert intégral "
        "pour mener sans délai son entretien d'évaluation opérationnelle."
    )
    pdf.para(
        "Vous vous assurerez de son adhésion complète aux objectifs de rigueur comptable, de gestion rigoureuse de la trésorerie et de "
        "transparence totale avec la Direction Générale et le Président."
    )

    pdf.titre1("3. Cadrage du recrutement des directeurs de pôle et filtre d'excellence (> 80/100)")
    pdf.para(
        "Vous disposez de l'autorisation d'amorcer le sourcing actif pour les postes de Directeur Technique (projets photovoltaïques toiture "
        "et raccordement industriel) et Directeur Commercial (prospection grands comptes B2B et C&I)."
    )
    pdf.para(
        "Toutefois, une règle de gouvernance absolue et non négociable régit ce processus :"
    )
    pdf.puces([
        "Canal unique : Tout profil retenu à l'issue de votre premier tri doit être obligatoirement transmis par écrit via cette adresse officielle (direction@soleil-b2b.ci), accompagné du CV exhaustif, des états de service vérifiés, des prétentions et de votre avis motivé ;",
        "Matrice d'évaluation : Chaque dossier est soumis à un processus strict d'analyse et de scoring multicritères ;",
        "Seuil éliminatoire impératif : Seuls les candidats obtenant une note strictement supérieure à 80 sur 100 (> 80/100) recevront l'approbation formelle de la Direction Générale pour engager les négociations contractuelles ;",
        "Absence d'engagement prématuré : Aucun accord, promesse d'embauche ou projet de contrat ne peut être délivré sans cette validation préalable écrite."
    ])
    pdf.para(
        "Cette méthodologie garantit la sélection exclusive de talents de premier ordre pour porter l'expansion de notre structure."
    )

    cible = chemin("documents_william", "2041-07-29_Courriel_Mohamed_Coulibaly_Feu_vert_DAF_et_protocole_recrutement_direction.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_courriel_reponse_mohamed_coulibaly():
    pdf = DocPDF(
        "CABINET DE REPRÉSENTATION MOHAMED COULIBALY",
        "Accusé de réception et engagement sur le protocole de recrutement",
        auteur="Mohamed Coulibaly",
        pied="Mohamed Coulibaly — Accusé et engagement recrutement — 29/07/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly (m.coulibaly@...)")
    pdf.meta("Destinataire", "Direction Générale / William Ossimi (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Lundi 29 juillet 2041, 20h55 (heure Luxembourg / 18h55 Abidjan)")
    pdf.meta("Objet", "RE : Finalisation des actes constitutifs, lancement entretien DAF et protocole impératif de recrutement")
    pdf.ln(3)

    pdf.titre1("1. Accusé de réception et confirmation de signature")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "J'accuse bonne réception de votre courriel de ce soir et de la confirmation formelle de la finalisation des statuts et du mandat DG "
        "avec le Cabinet Gnamien. Je vous réitère mon plein engagement pour cette aventure entrepreneuriale."
    )
    pdf.para(
        "Je confirme d'ores et déjà ma présence physique à l'étude de Maître Gnamien à Abidjan le mardi 13 août 2041 à 10h00 précises, "
        "muni de l'ensemble de mes pièces d'identité originales et justificatifs requis pour l'immatriculation."
    )

    pdf.titre1("2. Déploiement de l'entretien DAF avec Madame Mariam Brou")
    pdf.para(
        "Je prends immédiatement attache avec Madame Mariam Brou ce soir même pour convenir d'un créneau d'entretien opérationnel approfondi "
        "dès demain après-midi, mardi 30 juillet. Je passerai au crible ses réflexes SYSCOHADA, sa capacité de négociation bancaire locale et "
        "son adhésion totale aux protocoles de double validation et de reporting permanent."
    )
    pdf.para(
        "Un compte-rendu exhaustif vous sera transmis par écrit dès la clôture de notre échange."
    )

    pdf.titre1("3. Respect absolu du protocole de sélection et du seuil > 80/100")
    pdf.para(
        "Je prends acte de la règle impérative de filtrage fixée à 80/100 pour l'équipe de direction. Je partage entièrement votre souci "
        "d'excellence : le marché ivoirien du solaire exige des directeurs rigoureux, autonomes et d'une probité absolue."
    )
    pdf.para(
        "J'active dès à présent mes canaux professionnels (alumni INP-HB et cadres du secteur de l'énergie en poste) pour identifier les meilleurs "
        "Directeurs Techniques et Directeurs Commerciaux disponibles. Chaque dossier sera transmis à cette adresse avec mon avis détaillé et les "
        "justificatifs complets pour votre notation avant toute promesse."
    )

    cible = chemin("courriels", "2041-07-29_Courriel_Mohamed_Coulibaly_Accuse_et_lancement_recrutement.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_compte_rendu_entretien_mariam_brou():
    pdf = DocPDF(
        "SOLEIL B2B COTE D'IVOIRE (EN CONSTITUTION)",
        "Direction Générale — Compte-rendu d'Entretien Opérationnel DAF",
        auteur="Mohamed Coulibaly",
        pied="Entretien DAF Mariam Brou — Mohamed Coulibaly — 30/07/2041"
    )

    pdf.meta("Émetteur", "Mohamed Coulibaly (m.coulibaly@...)")
    pdf.meta("Destinataire", "Direction Générale / William Ossimi (direction@soleil-b2b.ci)")
    pdf.meta("Date et heure", "Mardi 30 juillet 2041, 19h30 (heure Luxembourg / 17h30 Abidjan)")
    pdf.meta("Objet", "Compte-rendu d'entretien opérationnel : Madame Mariam Brou (Direction Administrative et Financière)")
    pdf.ln(3)

    pdf.titre1("1. Synthèse de l'entretien opérationnel")
    pdf.para(
        "Monsieur le Président,"
    )
    pdf.para(
        "J'ai conduit ce mardi 30 juillet 2041, de 15h00 à 16h20 GMT, l'entretien approfondi avec Madame Mariam Brou en visioconférence "
        "sécurisée. Cet échange confirme en tous points l'excellence de son profil et sa parfaite adéquation avec nos exigences."
    )

    pdf.titre1("2. Évaluation des compétences et des réflexes métier")
    pdf.puces([
        "Comptabilité & Fiscalité OHADA : Maîtrise exemplaire du plan SYSCOHADA révisé, expérience solide des déclarations fiscales ivoiriennes (DGI, TVA, ITS, CNPS) et habitude des audits de commissaires aux comptes ;",
        "Gestion de trésorerie & Banque locale : Connaissance intime des pratiques bancaires d'Abidjan (lignes d'escompte, garanties de restitution d'acompte, ouvertures de crédit documentaire pour matériel importé) ;",
        "Rapprochement et reporting : Adhésion totale au principe de clôture mensuelle au plus tard le 5 du mois suivant, avec balance générale consolidée et réconciliation bancaire au centime près ;",
        "Transparence institutionnelle : Pleine acceptation du statut de reporting direct envers le Président et l'associé unique, sans restriction d'accès aux relevés bancaires."
    ])

    pdf.titre1("3. Conditions contractuelles et disponibilité")
    pdf.para(
        "Madame Brou confirme son accord sur la maquette contractuelle Niveau 2 qui lui a été transmise : rémunération mensuelle fixe de "
        "1 200 000 FCFA net, prime annuelle liée au recouvrement client et à la maîtrise du BFR. Elle est disponible immédiatement pour assister "
        "à nos côtés à la formalisation définitive dès notre mission d'août à Abidjan."
    )

    pdf.titre1("4. Recommandation formelle")
    pdf.para(
        "Au vu de sa rigueur, de sa pondération et de sa parfaite maîtrise technique, je recommande formellement la signature de son contrat de travail "
        "en qualité de Directrice Administrative et Financière dès le dépôt des statuts au CEPICI le 13 août prochain."
    )

    cible = chemin("courriels", "2041-07-30_Courriel_Mohamed_Coulibaly_Compte_rendu_entretien_DAF_Mariam_Brou.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_rapport_quotidien_11():
    pdf = DocPDF(
        "Rapport Quotidien du Directeur Général Virtuel (n° 11)",
        "État d'avancement des opérations et pilotage stratégique",
        auteur="Directeur Général virtuel",
        pied="Rapport n° 11 — Opérations Côte d'Ivoire & Luxembourg — 30/07/2041"
    )

    pdf.meta("Période", "Mardi 30 juillet 2041, 00h00 - 20h00")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Président Fondateur")
    pdf.meta("Statut global", "Nominal — Processus de recrutement DAF verrouillé — Actes en préparation")
    pdf.ln(3)

    pdf.titre1("1. Pôle Ressources Humaines & Recrutement")
    pdf.puces([
        "DAF (Mariam Brou) : Entretien opérationnel conduit avec succès par Mohamed Coulibaly ce jour (15h00-16h20 GMT). Recommandation formelle d'embauche transmise par le DG. Accord confirmé sur la grille Niveau 2 (1,2 M FCFA net/mois) ;",
        "Équipe de Direction (DT / DC) : Protocole de notation verrouillé (note > 80/100 éliminatoire). Mohamed Coulibaly a activé son vivier INP-HB et énergie. Deux candidatures préliminaires en cours de qualification locale ;",
        "Note de synthèse RH : Mariam Brou consolidée à 88/100, engagement prévu le 13 août après enregistrement CEPICI."
    ])

    pdf.titre1("2. Pôle Juridique & Formalités administratives")
    pdf.puces([
        "Cabinet Ismaël Gnamien : Impression des statuts et mandats sur chemises notariales en cours. Dossier CEPICI finalisé pour le 13 août ;",
        "MENJE Luxembourg : Dossier Article 14 (D031) conservé pour la rentrée de septembre, aucun élément bloquant."
    ])

    pdf.titre1("3. Pôle Logistique & Déplacements")
    pdf.puces([
        "Mission Abidjan : Vols Air France A/R confirmés (12 au 25 août) ; e-visas SNEDAI en cours de traitement usuel ;",
        "Hébergement : Option résidence sécurisée Cocody Ambassades pré-réservée."
    ])

    pdf.titre1("4. Trésorerie et consommation API")
    pdf.para(
        "Consommation API de la journée : 0,80 EUR (traitement compte-rendu Coulibaly, analyse matrices RH, veille juridique). "
        "Budget mensuel engagé : 46,86 EUR sur le plafond autorisé de 50,00 EUR."
    )

    cible = chemin("documents_william", "2041-07-30_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_attestation_snedai_rectifiee():
    pdf = DocPDF(
        "REPUBLIQUE DE COTE D'IVOIRE — MINISTERE DE L'INTERIEUR",
        "SNEDAI TECHNOLOGIES — E-VISA BIOMÉTRIQUE AEROPORT ABIDJAN",
        auteur="SNEDAI Technologies",
        pied="SNEDAI Côte d'Ivoire — Attestation de pré-enrôlement e-visa — 31/07/2041"
    )

    pdf.meta("Numéro de dossier", "CI-EV-2041-0727-89102-REV")
    pdf.meta("Date de rectification", "Mercredi 31 juillet 2041, 11h20")
    pdf.meta("Bénéficiaire", "OSSIMI Stéphane William")
    pdf.meta("Nationalité / Passeport", "Française — Passeport 31AB99402 (validité 2048)")
    pdf.meta("Statut administratif", "VALIDE — Enrôlement biométrique confirmé à l'arrivée FHB")
    pdf.ln(3)

    pdf.titre1("1. Confirmation de régularisation administrative")
    pdf.para(
        "La Direction de la Surveillance du Territoire et le service e-visa de SNEDAI Technologies confirment la prise en compte "
        "de la rectification opérée ce jour sur le dossier CI-EV-2041-0727-89102."
    )
    pdf.para(
        "L'ordre des prénoms (« Stéphane William » en concordance avec la bande ZMR du passeport) a été mis à jour et validé. "
        "L'anomalie de lecture optique initiale est levée."
    )

    pdf.titre1("2. Instructions pour l'arrivée à l'Aéroport Félix Houphouët-Boigny")
    pdf.puces([
        "Se présenter au guichet « E-VISA / Biométrie » dès la descente de l'appareil Air France AF702 le 12 août 2041 ;",
        "Munir l'agent de police de cette attestation imprimée portant le code-barres 2D sécurisé, du passeport original et du carnet international de vaccination (fièvre jaune obligatoire) ;",
        "Prise d'empreintes digitales et délivrance immédiate de la vignette visa biométrique court séjour (90 jours)."
    ])

    cible = chemin("courriels", "2041-07-31_SNEDAI_Attestation_pre_enrolement_e-visa_rectifiee.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def generer_rapport_quotidien_12():
    pdf = DocPDF(
        "Rapport Quotidien du Directeur Général Virtuel (n° 12)",
        "État d'avancement des opérations et clôture mensuelle",
        auteur="Directeur Général virtuel",
        pied="Rapport n° 12 — Opérations Côte d'Ivoire & Luxembourg — 31/07/2041"
    )

    pdf.meta("Période", "Mercredi 31 juillet 2041, 00h00 - 20h00")
    pdf.meta("Destinataire", "Monsieur William Ossimi, Président Fondateur")
    pdf.meta("Statut global", "Excellent — Trésorerie renforcée — Recrutement DAF validé — Mission Abidjan parée")
    pdf.ln(3)

    pdf.titre1("1. Pôle Finances & Comptabilité personnelle")
    pdf.puces([
        "Traitement mensuel Luxembourg : Virement de l'État luxembourgeois perçu ce jour (+9 320,00 EUR net) sur le compte courant Spuerkeess Zebra Premium. Solde bancaire disponible clôturé à 17 784,70 EUR ;",
        "Clôture mensuelle de juillet : Toutes les dépenses opérationnelles de lancement (Claude Pro 24,30 EUR, acompte Me Gnamien 1 511,00 EUR, billets Air France 1 285,00 EUR, visa 73,00 EUR) sont intégralement absorbées ;",
        "Programmations du 1er au 5 août : Les prélèvements récurrents (Minett Combat Club 85 EUR, Zebra 12,83 EUR, épargne 732 EUR, ETF 5 755 EUR, prêt immobilier 949,28 EUR, assurances 152 EUR) sont parfaitement couverts."
    ])

    pdf.titre1("2. Pôle Ressources Humaines & Opérations terrain")
    pdf.puces([
        "DAF (Mariam Brou) : Compte-rendu d'entretien validé. Offre ferme prête pour signature le 13 août à Abidjan ;",
        "Directoire (DT / DC) : Mohamed Coulibaly finalise les présélections. La grille de notation stricte (> 80/100) est active sur nos systèmes ;",
        "Organisation cible : Gouvernance prête pour le déploiement opérationnel à compter du 1er octobre 2041."
    ])

    pdf.titre1("3. Pôle Juridique & Logistique")
    pdf.puces([
        "E-visa SNEDAI : Anomalie administrative ZMR résolue avec succès ce matin, attestation officielle régularisée reçue (guichet biométrique FHB prêt) ;",
        "Cabinet Gnamien : Originaux sous reliure prêts pour la séance du 13 août à 10h00 ;",
        "MENJE Luxembourg : Dossier Article 14 prêt pour dépôt à la rentrée scolaire."
    ])

    pdf.titre1("4. Trésorerie et consommation API")
    pdf.para(
        "Consommation API du jour : 0,40 EUR (clôture mensuelle, archivage justificatif SNEDAI). "
        "Consommation totale cumulée au 31 juillet 2041 : 47,26 EUR (respect strict de l'enveloppe de 50,00 EUR)."
    )

    cible = chemin("documents_william", "2041-07-31_Rapport_quotidien_Directeur_General_virtuel.pdf")
    pdf.sauver(cible)
    print(f"Généré : {cible}")


def main():
    generer_courriel_mohamed_coulibaly_cadrage()
    generer_courriel_reponse_mohamed_coulibaly()
    generer_compte_rendu_entretien_mariam_brou()
    generer_rapport_quotidien_11()
    generer_attestation_snedai_rectifiee()
    generer_rapport_quotidien_12()


if __name__ == "__main__":
    main()
