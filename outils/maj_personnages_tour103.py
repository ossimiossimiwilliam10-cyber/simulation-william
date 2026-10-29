"""
Mise à jour des fiches personnages pour le Tour 103 (Règle 18 et historique) :
- Wilfried Yéo
- Safiatou Camara
- Kader Bamba
"""
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# 1. Wilfried Yéo
path_yeo = RACINE / "personnes" / "wilfried-yeo.md"
content_yeo = path_yeo.read_text(encoding="utf-8")
old_physique_yeo = """## Physique (graines tirées, à préciser dans la première scène)
- 159 cm, corpulence moyenne, tatouage visible."""
new_physique_yeo = """## Physique (description exhaustive — Règle 18, 18/08/2041)
- Stature : 159 cm ; corpulence moyenne, carrure trapue et charpentée.
- Silhouette et allure : buste compact, épaules larges pour sa petite taille, bras fermes et musclés façonnés par le déchargement quotidien des casiers et cartons d'eau, ventre légèrement arrondi ; posture vigilante et sur la défensive derrière son comptoir, tatouage tribal foncé visible sur l'avant-bras droit.
- Visage et carnation : teint ébène chaud, peau luisante aux tempes sous la chaleur tropicale ; visage carré aux traits marqués par le travail et l'âge, mâchoire serrée, sourcils drus surplombant un regard plissé, inquisiteur et méfiant, bouche pincée aux lèvres sèches.
- Cheveux : crâne rasé de près, laissant poindre quelques fils argentés discrets sur les tempes.
- Style vestimentaire : polo vert délavé à col boutonné élimé, pantalon en toile sombre retroussé aux chevilles, claquettes en plastique bleu aux pieds ; chiffon synthétique posé sur l'épaule droite."""

content_yeo = content_yeo.replace(old_physique_yeo.replace("\r\n", "\n"), new_physique_yeo)
content_yeo = content_yeo.replace(old_physique_yeo, new_physique_yeo)

old_hist_yeo = "- 17/08/2041 : fiche créée (tirage du générateur)."
new_hist_yeo = """- 17/08/2041 : fiche créée (tirage du générateur).
- 18/08/2041 : première apparition (alimentation générale, Deux-Plateaux) ; réaction méfiante (T17 : mefiance) face aux questions de William sur les compteurs CIE et le solaire ; description exhaustive Règle 18 consignée."""
content_yeo = content_yeo.replace(old_hist_yeo, new_hist_yeo)
path_yeo.write_text(content_yeo, encoding="utf-8")
print("wilfried-yeo.md mis à jour")

# 2. Safiatou Camara
path_camara = RACINE / "personnes" / "safiatou-camara.md"
content_camara = path_camara.read_text(encoding="utf-8")
old_physique_camara = """## Physique (graines tirées, à préciser dans la première scène)
- 153 cm, corpulence mince."""
new_physique_camara = """## Physique (description exhaustive — Règle 18, 18/08/2041)
- Stature : 153 cm ; silhouette menue mais galbée et vive.
- Silhouette et galbe : maintien souple et plein d'assurance, taille fine (environ 64 cm), hanches bien dessinées (environ 94 cm), poitrine menue et ferme (bonnet B) sous un tissu léger ; démarche rapide et décidée entre les tables du maquis ; tatouage floral discret sur le poignet droit.
- Visage et carnation : peau caramel doré éclatante et satinée ; visage expressif aux pommettes hautes et rondes, mâchoire douce, nez fin, bouche large et volubile s'ouvrant sur des dents blanches très régulières ; grands yeux noirs vifs et rieurs soulignés par une fine cicatrice discrète au-dessus du sourcil gauche.
- Cheveux : nattes fines tressées avec soin, plaquées vers l'arrière et retenues par une pince discrète sur la nuque.
- Style vestimentaire : pagne wax traditionnel en coton imprimé aux motifs géométriques jaune soleil et indigo noué à la taille, débardeur noir moulant sans manches, fines savates en cuir verni, anneaux dorés aux oreilles ; tablier en toile autour de la taille contenant un carnet et des billets de banque."""

content_camara = content_camara.replace(old_physique_camara.replace("\r\n", "\n"), new_physique_camara)
content_camara = content_camara.replace(old_physique_camara, new_physique_camara)

old_hist_camara = "- 17/08/2041 : fiche créée (tirage du générateur)."
new_hist_camara = """- 17/08/2041 : fiche créée (tirage du générateur).
- 18/08/2041 : première apparition (maquis d'Anono) ; échange chaleureux et très direct (T17 : conversation) sur la facture CIE, les pannes de courant et la rentabilité illusoire du solaire bas coût pour petits frigos ; description exhaustive Règle 18 consignée."""
content_camara = content_camara.replace(old_hist_camara, new_hist_camara)
path_camara.write_text(content_camara, encoding="utf-8")
print("safiatou-camara.md mis à jour")

# 3. Kader Bamba
path_bamba = RACINE / "personnes" / "kader-bamba.md"
content_bamba = path_bamba.read_text(encoding="utf-8")
old_physique_bamba = """## Physique (graines tirées, à préciser dans la première scène)
- 174 cm, corpulence moyenne."""
new_physique_bamba = """## Physique (description exhaustive — Règle 18, 18/08/2041)
- Stature : 174 cm ; corpulence moyenne (environ 73 kg), silhouette équilibrée.
- Silhouette et allure : démarche tranquille du dimanche matin, épaules droites, carrure svelte sans graisse superflue ; gestuelle sobre, tenant d'une main un smartphone à coque transparente.
- Visage et carnation : teint chocolat profond, peau uniforme ; visage ovale régulier, front haut, sourcils bien arqués, regard calme, direct mais sans insistance, bouche bien proportionnée, barbe courte très soignée et taillée au millimètre le long de la mâchoire.
- Cheveux : cheveux crépus coupés courts et parfaitement dégradés sur les tempes.
- Style vestimentaire : allure décontractée soignée typique de la classe moyenne abidjanaise le week-end : t-shirt blanc uni en coton peigné, bermuda en toile de coton beige avec poches italiennes, baskets basses légères en toile grise, montre sportive au poignet gauche."""

content_bamba = content_bamba.replace(old_physique_bamba.replace("\r\n", "\n"), new_physique_bamba)
content_bamba = content_bamba.replace(old_physique_bamba, new_physique_bamba)

old_hist_bamba = "- 17/08/2041 : fiche créée (tirage du générateur)."
new_hist_bamba = """- 17/08/2041 : fiche créée (tirage du générateur).
- 18/08/2041 : première apparition (rue résidentielle des Deux-Plateaux) ; contact poli mais bref (T17 : poli_bref) soulignant les contraintes locatives et le monopole CIE ; description exhaustive Règle 18 consignée."""
content_bamba = content_bamba.replace(old_hist_bamba, new_hist_bamba)
path_bamba.write_text(content_bamba, encoding="utf-8")
print("kader-bamba.md mis à jour")
