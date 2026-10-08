"""CV et diplôme de master d'Aïcha Diomandé, envoyés par courriel à William le lundi 06/08/2040 à 08h20 (heure d'Abidjan) -> courriels/

Demandés par William le 05/08 (21h52). Dossiers RH hors serveur partagé (règles de classement de Mariette) : envoi par courriel.
Faits repris des fichiers : 27 ans, master en gestion-finance, ancienne employée de centre d'appels, deux ans de discriminations à
l'embauche, gérante d'OSIA depuis le 22/05/2040 (CDI, essai jusqu'au 21/11/2040). Faits créés par le moteur et consignés dans
`personnes/aicha.md` : née le 14/03/2013 à Touba ; UFHB (UFR SEG), master 2036 ; bac G2 en 2031 ; stage de 2036 ; missions de 2037-2038.
Coordonnées personnelles masquées volontairement.
"""
from osia_pdf import OsiaPDF, RACINE


class CvPDF(OsiaPDF):
    def header(self):
        self.set_font(self.fam, "B", 16)
        self.cell(0, 9, self.t("AÏCHA DIOMANDÉ"), new_x="LMARGIN", new_y="NEXT")
        self.set_font(self.fam, "", 10)
        self.cell(0, 6, self.t("Gestion et finance — Directrice générale (gérante)"), new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 6, self.t("Abidjan, Côte d'Ivoire · 27 ans · Téléphone : +225 07 XX XX XX XX"), new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t(f"CV — Aïcha Diomandé — août 2040 — page {self.page_no()}/{{nb}}"), align="C")


cv = CvPDF("Curriculum vitae")
cv.titre1("Profil")
cv.para("Titulaire d'un master en gestion, spécialité finance. Expérience de la relation client, de la saisie comptable et, depuis mai 2040, "
        "de la direction d'une jeune société d'énergie solaire, de sa création à son premier contrat.")
cv.titre1("Expérience professionnelle")
cv.para("Depuis mai 2040 — OSIA Énergies SARL (solaire), Abidjan-Cocody — Gérante, directrice générale")
cv.puces(["Création de la société avec le cabinet d'avocats : statuts, RCCM (11/07/2040), immatriculation CNPS, ouverture du compte à la SGBCI.",
          "Recrutement et coordination de l'équipe de direction (commercial, technique, RH, SAV) ; rapport quotidien à l'associé unique.",
          "Trésorerie, paiements et déclarations sociales ; suivi de l'augmentation de capital (115 000 000 FCFA, juillet-août 2040).",
          "Premier contrat client (installation solaire d'une villa, 15 900 000 FCFA HT)."])
cv.para("2038 – 2040 — Centre d'appels (sous-traitant d'un opérateur de téléphonie), Abidjan-Plateau — Téléconseillère, puis référente qualité")
cv.puces(["Traitement des réclamations, suivi des indicateurs de qualité, formation des nouveaux téléconseillers."])
cv.para("2037 – 2038 — Missions ponctuelles, Abidjan (Adjamé, Abobo) — Saisie comptable en indépendante")
cv.puces(["Tenue de caisse et saisie pour des commerçants ; déclarations simplifiées."])
cv.para("2036 (six mois) — Direction financière d'une société de distribution, Abidjan-Zone 4 — Stage de fin de master")
cv.puces(["Rapprochements bancaires, tableaux de trésorerie, préparation des déclarations fiscales mensuelles."])
cv.titre1("Formation")
cv.puces(["2036 — Master, domaine Sciences économiques et de gestion, mention Gestion, spécialité Finance — Université Félix Houphouët-Boigny "
          "(UFR SEG), Abidjan-Cocody — mention Assez bien. Mémoire : « Le financement bancaire des PME ivoiriennes : contraintes et garanties ».",
          "2034 — Licence, Sciences économiques et de gestion — Université Félix Houphouët-Boigny.",
          "2031 — Baccalauréat, série G2 (techniques quantitatives de gestion) — lycée de Touba."])
cv.titre1("Compétences")
cv.puces(["Analyse financière, trésorerie, rapprochements bancaires ; montage de dossiers de crédit.",
          "Fiscalité et social ivoiriens (ITS, CNPS) ; droit des sociétés OHADA : notions.",
          "Excel (tableaux croisés, fonctions financières) ; logiciel de comptabilité ; rédaction de rapports."])
cv.titre1("Langues")
cv.para("Français : courant. Malinké (dioula) : langue maternelle. Anglais : intermédiaire (B1).")
cv.titre1("Centres d'intérêt")
cv.para("Lecture ; tontine et association des femmes du quartier ; cuisine.")
cv.sauver(RACINE / "courriels" / "2040-08-06_cv_aicha_diomande.pdf")


class DiplomePDF(OsiaPDF):
    def header(self):
        self.set_font(self.fam, "", 9)
        self.cell(0, 5, self.t("RÉPUBLIQUE DE CÔTE D'IVOIRE — Union – Discipline – Travail"), align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, self.t("MINISTÈRE DE L'ENSEIGNEMENT SUPÉRIEUR ET DE LA RECHERCHE SCIENTIFIQUE"), align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font(self.fam, "B", 12)
        self.cell(0, 8, self.t("UNIVERSITÉ FÉLIX HOUPHOUËT-BOIGNY"), align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t("Copie numérisée (cybercafé, Cocody, 06/08/2040) — non certifiée conforme"), align="C")


dip = DiplomePDF("Diplôme de Master")
dip.set_font(dip.fam, "B", 20)
dip.cell(0, 14, dip.t("DIPLÔME DE MASTER"), align="C", new_x="LMARGIN", new_y="NEXT")
dip.ln(2)
dip.para("Vu les textes portant organisation des études supérieures selon le système Licence-Master-Doctorat ;")
dip.para("Vu le procès-verbal de délibération du jury de l'UFR des Sciences économiques et de gestion, session de juillet 2036 ;")
dip.ln(2)
dip.para("Le Président de l'Université Félix Houphouët-Boigny confère à")
dip.set_font(dip.fam, "B", 13)
dip.cell(0, 9, dip.t("Mademoiselle DIOMANDÉ Aïcha"), align="C", new_x="LMARGIN", new_y="NEXT")
dip.para("née le 14 mars 2013 à Touba (Côte d'Ivoire),")
dip.para("le diplôme de MASTER — Domaine : Sciences économiques et de gestion — Mention : Gestion — Spécialité : Finance,")
dip.para("avec la mention : Assez bien.")
dip.ln(3)
dip.para("Fait à Abidjan, le 15 décembre 2036.")
dip.tableau(["Le Doyen de l'UFR SEG", "Le Président de l'Université", "La titulaire"],
            [["[signature et cachet]", "[signature et sceau]", "[signature]"]], [60, 65, 55])
dip.para("N° d'enregistrement : UFHB/SEG/M/2036/04817", italique=True)
dip.sauver(RACINE / "courriels" / "2040-08-06_diplome_master_aicha_diomande.pdf")
