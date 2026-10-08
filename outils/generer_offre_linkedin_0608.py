"""Offre d'emploi publiée par William sur LinkedIn le lundi 06/08/2040 vers 15h15 (heure de Lisbonne) -> documents_william/ (copie)

Contenu décidé par William : poste de directeur « planification, achats et projets » du pôle Technique & Déploiement (pôle à deux
directeurs) ; missions et profil repris de la première recommandation de son assistant d'IA ; 6 ans d'expérience minimum dans le solaire ;
doctorat apprécié et valorisé ; 700 000 à 1 000 000 FCFA brut par mois ; cible : Côte d'Ivoire, Afrique, diaspora en Europe.
Publication gratuite depuis le profil personnel de William (une seule offre gratuite active ; mise en pause automatique au plafond).
"""
from osia_pdf import OsiaPDF, RACINE


class OffrePDF(OsiaPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t("Copie de l'offre publiée sur LinkedIn le 06/08/2040 par William Ossimi — page {}/{{nb}}".format(self.page_no())),
                  align="C")


pdf = OffrePDF("OSIA Énergies recrute",
               "Directeur·rice Planification, Achats et Projets — Pôle Technique & Déploiement")
pdf.meta("Entreprise", "OSIA Énergies SARL, énergie solaire (Abidjan, Côte d'Ivoire)")
pdf.meta("Lieu", "Abidjan, sur site ; candidatures ouvertes en Côte d'Ivoire, en Afrique et à la diaspora en Europe")
pdf.meta("Contrat", "CDI, temps plein")
pdf.meta("Publié par", "William Ossimi")

pdf.titre1("Le poste")
pdf.para("OSIA Énergies installe des systèmes solaires pour les villas, les cliniques, les écoles et les hôtels. Notre pôle Technique & "
         "Déploiement est dirigé par deux directeurs complémentaires : l'un pilote le terrain et la qualité des installations, l'autre "
         "pilote la planification, les achats et les projets. C'est ce second poste que nous ouvrons.")
pdf.titre1("Missions")
pdf.puces(["Planning des chantiers.",
           "Passation des commandes ; suivi des fournisseurs et du dédouanement (au moins deux fournisseurs par composant).",
           "Dimensionnement et dossiers techniques : schémas, notes de calcul, réception.",
           "Classement et traçabilité des documents sur le serveur de l'entreprise.",
           "Reporting hebdomadaire."])
pdf.titre1("Profil recherché")
pdf.puces(["Ingénieur(e) en génie électrique ou énergétique (bac + 5).",
           "Au minimum 6 ans d'expérience dans le solaire.",
           "À l'aise avec un tableur et un logiciel de dimensionnement photovoltaïque.",
           "La connaissance des procédures de raccordement de la CIE est appréciée.",
           "Un doctorat est un plus et apportera un réel avantage sur la rémunération."])
pdf.titre1("Rémunération")
pdf.para("De 700 000 à 1 000 000 FCFA brut par mois, selon l'expérience et le doctorat.")
pdf.titre1("Candidater")
pdf.para("Postulez directement sur LinkedIn avec votre CV.")

pdf.sauver(RACINE / "documents_william" / "2040-08-06_offre_linkedin_directeur_planification.pdf")
