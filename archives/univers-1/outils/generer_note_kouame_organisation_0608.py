"""Note de Me Kouamé à William sur son organigramme cible (lundi 06/08/2040, 18h40 à Abidjan) -> courriels/

Réponse T6 (autorité propre, franchise) aux deux questions de William (10h52 à Lisbonne) : son avis, et la faisabilité avec les statuts
actuels (SARL, gérante unique, statuts modifiés du 02/08). Me Kouamé ignore que le document a circulé (Estelle, Aïcha) et ignore l'offre
LinkedIn. Il a reçu à 14h30 le courriel d'Aïcha sur les clauses de rétrogradation, de promotion et de licenciement ; il lui répond
séparément sur ce seul point.
Droit : AUSCGIE (SARL : gérance, art. 323 s. ; révocation du gérant, art. 326) ; organes de SA et de SAS ; Code du travail ivoirien
(sanctions disciplinaires prévues au règlement intérieur ; rupture de l'essai ; licenciement : motif légitime et procédure).
"""
from osia_pdf import OsiaPDF, RACINE


class NotePDF(OsiaPDF):
    def footer(self):
        self.set_y(-14)
        self.set_font(self.fam, "I", 8)
        self.cell(0, 8, self.t(f"Cabinet de Me Kouamé, avocat à la Cour — confidentiel — page {self.page_no()}/{{nb}}"), align="C")


pdf = NotePDF("Note à M. William Ossimi, associé unique d'OSIA Énergies SARL",
              "Objet : votre projet d'organisation de la direction — Abidjan, le 6 août 2040")
pdf.para("Monsieur,")
pdf.para("Vous me demandez mon avis sur le document que vous m'avez transmis ce matin, et s'il peut être mis en place avec les statuts "
         "actuels. Voici ma réponse, point par point.")

pdf.titre1("1. Ce que la loi permet dans une SARL")
pdf.para("OSIA Énergies est une SARL. L'Acte uniforme ne connaît, pour la diriger, que le ou les gérants (article 323 et suivants). Les "
         "titres de « CEO », d'« administrateur général » et de « directeurs généraux » n'existent pas dans une SARL : ce peuvent être des "
         "intitulés de postes salariés, rien de plus. Leurs pouvoirs ne viendront que de délégations écrites de la gérance, dans les limites "
         "de vos statuts du 2 août (seuils de 5 et 10 millions, actes réservés, double signature au-delà de 5 millions).")
pdf.para("L'administrateur général est un organe de la société anonyme. Si vous voulez de vrais dirigeants, avec des pouvoirs propres "
         "opposables aux tiers, il faudra soit nommer plusieurs cogérants (modification des statuts), soit transformer la société en SA ou en "
         "SAS. Une transformation est possible, mais elle a un coût et des délais ; je ne la conseille pas avant que la société ait des "
         "revenus réguliers.")

pdf.titre1("2. Le « CEO » au-dessus de la gérante")
pdf.para("Un salarié placé « au-dessus » de la gérante n'aurait aucun pouvoir propre : c'est la gérante qui signe, qui représente la société "
         "et qui répond de la gestion. Si vous voulez qu'une autre personne dirige réellement, il faut la nommer gérante, à la place de "
         "Mme Diomandé ou à côté d'elle. Tant que ce n'est pas fait, l'organigramme ne change rien vis-à-vis des banques, de la CNPS, des "
         "impôts et des clients.")

pdf.titre1("3. Mme Diomandé")
pdf.para("Mme Diomandé a deux qualités distinctes. Comme gérante, vous pouvez la révoquer par une décision d'associé unique (article 326) ; "
         "une révocation sans juste motif peut ouvrir droit à des dommages-intérêts. Comme salariée, elle est en période d'essai jusqu'au "
         "21 novembre : l'essai peut être rompu sans préavis, mais une rupture décidée pour un motif sans lien avec ses aptitudes "
         "professionnelles peut être jugée abusive.")
pdf.para("La dernière ligne de votre document (« reclassée dans le Pôle Support » ou « poussée vers la sortie ») est une intention écrite. "
         "Je vous déconseille de faire circuler ce document. S'il devait servir un jour dans un contentieux, c'est la première pièce que "
         "l'on produirait.")

pdf.titre1("4. Les clauses de rétrogradation, de promotion et de licenciement")
pdf.para("Mme Diomandé m'a écrit cet après-midi à ce sujet ; je lui réponds séparément, sur ce seul point, dans les mêmes termes.")
pdf.puces(["Promotion : une clause d'évolution liée aux évaluations est possible et utile.",
           "Rétrogradation : c'est une sanction disciplinaire. Elle doit être prévue par le règlement intérieur, suivre la procédure "
           "disciplinaire, et, parce qu'elle touche à la qualification et au salaire, je recommande de recueillir l'accord écrit du salarié au "
           "moment où elle intervient. Une rétrogradation automatique déclenchée par une note serait fragile.",
           "Licenciement : il faut toujours un motif légitime et la procédure du Code du travail. Une mauvaise évaluation peut appuyer un "
           "licenciement pour insuffisance professionnelle ; elle ne le déclenche pas toute seule. Ce que je vous ai écrit le 27 juillet sur la "
           "clause de sanction de la matrice reste valable."])

pdf.titre1("5. Votre propre position")
pdf.para("Je vous rappelle ce que je vous ai dit le 25 juillet : si vous menez vous-même les entretiens, les négociations de salaires et les "
         "recrutements, vous redevenez gérant de fait. Les recrutements de cadres sont un acte réservé : vous les autorisez par écrit, la "
         "gérante les conduit et signe. Ne signez rien vous-même.")

pdf.titre1("6. Ce que je vous propose")
pdf.puces(["Garder la SARL et une gérante ; créer des directions salariées avec des fiches de poste et des délégations écrites de la gérance.",
           "Rédiger un modèle de contrat de cadre (clause d'évolution, objectifs, renvoi au règlement intérieur pour les sanctions) et mettre "
           "à jour le règlement intérieur : 450 000 FCFA HT, à la charge de la société.",
           "Étudier une transformation en SAS l'an prochain, si la croissance le justifie."])
pdf.para("Je reste à votre disposition. Bien cordialement.")
pdf.para("Me Kouamé, avocat à la Cour", italique=True)

pdf.sauver(RACINE / "courriels" / "2040-08-06_note_kouame_organisation.pdf")
