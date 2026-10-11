"""Classement des 12 candidatures à l'offre LinkedIn (directeur planification, achats et projets), produit le 07/08/2040 vers 06h55
(heure de Lisbonne) par l'assistant d'IA de William (Claude, 2040), relié à son compte LinkedIn -> documents_william/

Critères de l'offre : ingénieur génie électrique ou énergétique (bac + 5) ; 6 ans minimum dans le solaire ; tableur et logiciel de
dimensionnement ; procédures de la CIE ; doctorat valorisé ; 700 000 à 1 000 000 FCFA brut. Cible de William : 94-95/100 (« profil Messi »).
Tirages (memoire/tirages-aleas.md, 07/08) : meilleure note 78 (55 + 64,6 × 0,35) ; 3 candidatures à 70 ou plus ; 2 sans CV joint.
Candidats fictifs créés par le moteur.
"""
from osia_pdf import OsiaPDF, RACINE


class ClassementPDF(OsiaPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t(f"Évaluation automatique — document personnel de William Ossimi — page {self.page_no()}/{{nb}}"), align="C")


pdf = ClassementPDF("Classement des candidatures — Directeur·rice Planification, Achats et Projets",
                    "Offre LinkedIn d'OSIA Énergies — 12 candidatures au 07/08/2040, 06h50 — évaluation automatique sur 100")
pdf.titre1("Barème appliqué")
pdf.para("Diplôme bac + 5 en génie électrique ou énergétique : 20 points. Expérience dans le solaire (6 ans minimum) : 30 points. "
         "Planification, achats, fournisseurs et dédouanement : 20 points. Dimensionnement et outils (tableur, logiciel photovoltaïque), "
         "procédures de la CIE : 15 points. Doctorat : 10 points. Adéquation des prétentions salariales à la fourchette : 5 points.")
pdf.titre1("Résultat")
pdf.tableau(["Rang", "Candidat", "Lieu", "Profil", "Note"], [
    ["1", "Ange-Michel Konan, 36 ans", "Abidjan", "Ingénieur électricien (bac + 5) ; 8 ans dont 5 dans le solaire (chef de projet chez un intégrateur) ; dimensionnement ; achats peu pratiqués ; prétentions : 950 000", "78"],
    ["2", "Fatou Ndiaye, 33 ans", "Dakar", "Ingénieure énergies renouvelables (bac + 5) ; 6 ans dans les mini-réseaux solaires ; achats internationaux ; mobilité à confirmer ; prétentions : 1 100 000", "74"],
    ["3", "Dr Serge-Alain Mbarga, 41 ans", "Lyon", "Doctorat en génie électrique (stockage par batteries) ; 3 ans en bureau d'études solaire, 7 ans de recherche ; peu de terrain africain ; prétentions : « à discuter »", "71"],
    ["4", "Éric Yao Kouassi, 30 ans", "Abidjan", "Ingénieur électromécanicien (bac + 5) ; 4 ans dans le solaire", "66"],
    ["5", "Aminata Coulibaly, 29 ans", "Bamako", "Master en énergétique ; 3 ans dans le solaire", "61"],
    ["6", "Jean-Baptiste Gnagne, 45 ans", "Abidjan", "BTS électrotechnique ; 15 ans en électricité du bâtiment, 2 ans dans le solaire", "58"],
    ["7", "Ibrahim Ouédraogo, 32 ans", "Ouagadougou", "Licence ; 5 ans d'installation solaire", "52"],
    ["8", "Désiré Aka, 27 ans", "Abidjan", "Master en génie électrique ; 1 an dans le solaire", "47"],
    ["9", "Patricia Essoh, 38 ans", "Abidjan", "Ingénieure en génie civil ; aucune expérience dans le solaire", "41"],
    ["10", "Hervé Zadi, 25 ans", "Abidjan", "BTS ; stage de six mois", "35"],
    ["—", "Moussa Diabaté", "Abidjan", "Profil LinkedIn seul, sans CV : évaluation incomplète (estimation 30 à 45)", "n. c."],
    ["—", "Christelle Ahoua", "Grand-Bassam", "Profil LinkedIn seul, sans CV : évaluation incomplète (estimation 25 à 40)", "n. c."],
], [12, 40, 22, 90, 14], taille=8)
pdf.titre1("Synthèse de l'assistant")
pdf.puces(["Aucune candidature n'atteint la cible de 94/100. La meilleure obtient 78/100.",
           "Trois profils dépassent 70 : M. Konan (le plus proche du poste, dans la fourchette), Mme Ndiaye (au-dessus de la fourchette, "
           "mobilité à confirmer), Dr Mbarga (le seul docteur, mais peu d'expérience de terrain et des prétentions non chiffrées).",
           "Les profils réunissant bac + 5, six ans de solaire et un doctorat sont rares ; dans la fourchette de 700 000 à 1 000 000 FCFA, "
           "ils le sont encore plus. Pour viser plus haut, il faudrait soit élargir la fourchette, soit assouplir l'un des critères.",
           "Les notes reposent sur les CV et les profils déclarés : rien n'est vérifié (diplômes, références, salaires antérieurs)."])
pdf.sauver(RACINE / "documents_william" / "2040-08-07_classement_candidatures.pdf")
