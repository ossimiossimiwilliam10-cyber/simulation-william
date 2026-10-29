"""PIÈCE PDF À PARTIR D'UN TEXTE (créé le 29/10/2026, audit du travail de Gemini : un script Python par tour pour chaque PDF).

Règle 4 : tout document demandé ou reçu existe en vrai PDF. Au lieu d'écrire un nouveau script à chaque tour, le moteur écrit un texte
simple (dans `sorties/brouillons/`) et lance :

    python outils/piece.py sorties/brouillons/courriel.txt          # écrit le PDF, puis lancer python outils/verifier_pdf.py
    python outils/piece.py sorties/brouillons/courriel.txt --simule # montre ce qui serait écrit

Format du texte (UTF-8) :
    titre: Courriel de Mohamed Coulibaly : lancement de l'appel d'offres
    sous-titre: Abidjan, lundi 19 août 2041, 08h15
    auteur: Mohamed Coulibaly
    pied: Soleil B2B CI — courriel du 19/08/2041
    dossier: courriels                    (courriels = pièce reçue par William ; documents_william = pièce rédigée ou gardée par William)
    fichier: 2041-08-19_Courriel_Mohamed_Coulibaly_appel_d_offres.pdf   (commence TOUJOURS par la date de réception AAAA-MM-JJ)
    meta: De | Mohamed Coulibaly
    meta: À | William
    (ligne vide : fin de l'en-tête)
    # Titre de section
    Un paragraphe, sur une ou plusieurs lignes ; une ligne vide le termine.
    - une puce
    - une autre puce
    | Colonne 1 | Colonne 2 |
    | valeur | valeur |
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pdf_base import DocPDF, chemin  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CLES = {"titre", "sous-titre", "auteur", "pied", "dossier", "fichier"}


def lire(texte):
    entete, metas, corps = {}, [], []
    lignes = texte.replace("\r\n", "\n").split("\n")
    i = 0
    while i < len(lignes) and lignes[i].strip():
        m = re.match(r"\s*([a-zé-]+)\s*:\s*(.*)$", lignes[i])
        if not m:
            break
        cle, val = m.group(1).lower(), m.group(2).strip()
        if cle == "meta":
            a, _, b = val.partition("|")
            metas.append((a.strip(), b.strip()))
        elif cle in CLES:
            entete[cle] = val
        else:
            break
        i += 1
    corps = lignes[i:]
    for cle in ("titre", "dossier", "fichier"):
        if not entete.get(cle):
            sys.exit(f"En-tête incomplet : « {cle}: … » manquant.")
    if entete["dossier"] not in ("courriels", "documents_william"):
        sys.exit("dossier: courriels ou documents_william (règle 4).")
    if not re.match(r"\d{4}-\d{2}-\d{2}_.+\.pdf$", entete["fichier"]):
        sys.exit("fichier: le nom commence par la date AAAA-MM-JJ_ et finit par .pdf")
    return entete, metas, corps


def blocs(corps):
    """-> [(type, contenu)] avec type parmi titre, para, puces, tableau."""
    res, para, puces, table = [], [], [], []

    def vider():
        nonlocal para, puces, table
        if para:
            res.append(("para", " ".join(para)))
        if puces:
            res.append(("puces", puces))
        if table:
            res.append(("tableau", table))
        para, puces, table = [], [], []

    for l in corps:
        s = l.strip()
        if not s:
            vider()
        elif s.startswith("# "):
            vider()
            res.append(("titre", s[2:].strip()))
        elif s.startswith(("- ", "• ")):
            if para or table:
                vider()
            puces.append(s[2:].strip())
        elif s.startswith("|") and s.endswith("|"):
            if para or puces:
                vider()
            cellules = [c.strip() for c in s.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cellules):
                table.append(cellules)
        else:
            if puces or table:
                vider()
            para.append(s)
    vider()
    return res


def construire(entete, metas, liste):
    pdf = DocPDF(entete["titre"], entete.get("sous-titre"), auteur=entete.get("auteur"), pied=entete.get("pied"))
    for a, b in metas:
        pdf.meta(a, b)
    for typ, contenu in liste:
        if typ == "titre":
            pdf.titre1(contenu)
        elif typ == "para":
            pdf.para(contenu, taille=10)
        elif typ == "puces":
            pdf.puces(contenu, taille=9.5)
        elif typ == "tableau":
            entetes, lignes = contenu[0], contenu[1:]
            n = len(entetes)
            largeur = 174 / max(1, n)
            pdf.tableau(entetes, [l + [""] * (n - len(l)) for l in lignes], [largeur] * n, taille=9)
    return pdf


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("texte")
    ap.add_argument("--simule", action="store_true")
    a = ap.parse_args()
    entete, metas, corps = lire(Path(a.texte).read_text(encoding="utf-8"))
    liste = blocs(corps)
    sortie = chemin(entete["dossier"], entete["fichier"])
    if a.simule:
        print(f"(essai) {sortie} : {len(metas)} méta, " + ", ".join(f"{t}" for t, _ in liste))
        return 0
    construire(entete, metas, liste).sauver(sortie)
    print("Vérifier : python outils/verifier_pdf.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
