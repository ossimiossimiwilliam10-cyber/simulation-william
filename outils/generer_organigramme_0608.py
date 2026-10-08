"""Organigramme cible d'OSIA rédigé par William (fichier personnel, mis en page en PDF) -> documents_william/

Source : le fichier de William `organigramme_osia.md` (05-06/08/2040), repris tel quel (texte, tutoiement « ton groupe » et note finale
comprise) ; le schéma Mermaid est rendu en arborescence ; les émojis des titres sont retirés (police du PDF).
Envoyé par William à Estelle sur WhatsApp le lundi 06/08/2040 vers 07h10 (heure de Luxembourg).
"""
from osia_pdf import OsiaPDF, RACINE


class OrgaPDF(OsiaPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t(f"Document personnel de William Ossimi — organigramme cible — page {self.page_no()}/{{nb}}"), align="C")


pdf = OrgaPDF("Organigramme cible d'OSIA Énergies",
              "Voici la structure complète et détaillée de ton groupe, intégrant le CEO, les deux Directeurs Généraux, les 4 pôles, "
              "et les futures équipes opérationnelles.")

pdf.titre1("Représentation visuelle")
pdf.puces([
    "William Ossimi (Président / Actionnaire) — reçoit le rapport hebdo du CEO",
    "    CEO / Administrateur Général (À recruter - Le Poids Lourd)",
    "        Directeur Général Opérations (COO) (À définir)",
    "            Pôle Business & Client (Grace & Yves) → Équipe Commerciale (2 à 3 démarcheurs terrains)",
    "            Pôle Technique & Déploiement (Abdoul) → Équipe Technique (2 à 3 techniciens/installateurs)",
    "        Directeur Général Support & Finances (CFO) (Estelle ?)",
    "            Pôle Support & Légal (Mariette & Esther) → Équipe Administrative (Assistante RH + Assistante Conformité)",
    "            Pôle Financier (Directeur Financier) → Équipe Analyse (2 Analystes Quantitatifs / Risque)",
])

pdf.titre1("Détail des effectifs et des rôles")
pdf.titre1("Niveau 1 : Le Conseil (Toi)")
pdf.para("William Ossimi : Président. N'intervient plus dans l'opérationnel. Valide la stratégie globale et lit le rapport hebdomadaire du CEO.")
pdf.titre1("Niveau 2 : Le Super DG (CEO)")
pdf.puces(["Profil à recruter : Un vétéran du monde de l'entreprise (40-50 ans).",
           "Rôle : Synthétise les informations des deux DG, gère les crises majeures, et te fait un rapport unique chaque vendredi."])
pdf.titre1("Niveau 3 : Les Directeurs Généraux (COO & CFO)")
pdf.puces(["DG Opérations (COO) : Doit faire cohabiter Grace et Abdoul pour que les ventes soient livrées en temps et en heure.",
           "DG Support & Finances (CFO - Potentiellement Estelle) : S'assure que l'entreprise est rentable, légale et que les employés sont payés."])
pdf.titre1("Niveau 4 : Les 4 Pôles et leurs équipes de terrain (2 à 3 personnes par pôle)")
pdf.para("1. Pôle Business & Client (Front-Office)")
pdf.puces(["Management : Grace (Ventes) et Yves (SAV).",
           "La nouvelle équipe : 2 à 3 démarcheurs commerciaux. Leur rôle est d'être sur le terrain (B2B, entreprises, cliniques) pour fluidifier "
           "le pipeline de Grace, qui se concentrera sur le \"closing\" (la signature) des gros contrats."])
pdf.para("2. Pôle Technique & Déploiement (Moteur)")
pdf.puces(["Management : Abdoul.",
           "La nouvelle équipe : 2 à 3 techniciens salariés (en plus des sous-traitants comme Bertin). Ils gèrent la maintenance rapide, le SAV "
           "technique, et les petites installations pour soulager Abdoul."])
pdf.para("3. Pôle Support & Légal (Back-Office)")
pdf.puces(["Management : Mariette (RH) et Esther (Conformité - arrive en sept.).",
           "La nouvelle équipe : Des assistantes RH et conformité. Elles gèrent la paperasse quotidienne (contrats de travail, déclarations CNPS, "
           "vérification des pièces d'identité des clients) pour libérer Mariette et Esther."])
pdf.para("4. Pôle Financier (Stratégie)")
pdf.puces(["Management : (Estelle ou autre profil senior).",
           "La nouvelle équipe : 2 profils \"Quant\" (Analystes quantitatifs / Analystes risques). Des jeunes diplômés en mathématiques "
           "financières ou statistiques. Leur rôle est de calculer froidement : probabilité de défaut de paiement d'un client, rentabilité "
           "d'un emprunt, modélisation de crise."])
pdf.para("(Note : Si tu adoptes cette structure, Aïcha perd de fait son rôle de Gérante globale. Elle devra soit être reclassée dans le Pôle "
         "Support, soit être poussée vers la sortie).", italique=True)

pdf.sauver(RACINE / "documents_william" / "2040-08-06_organigramme_osia.pdf")
