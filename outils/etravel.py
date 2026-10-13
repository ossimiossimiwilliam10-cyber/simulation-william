"""eTRAVEL (créé le 13/10/2026, arrivée de William aux Philippines : proposition P19 validée à la revue n° 1). Inscription de
William sur le portail officiel philippin (F064 : gratuite, seulement dans les 72 heures avant l'arrivée, un code QR à présenter à
l'immigration et à la douane) : confirmation reçue par courriel, en PDF dans `courriels/`.

    python outils/etravel.py inscrire --reservation R004 --quand "2040-07-16 10:42" [--simule]

Le code QR du PDF est un motif tiré par empreinte de la référence (un vrai code QR exigerait une bibliothèque absente) : c'est
l'image que William garde sur son téléphone. Le portail est en anglais (fidèle au vrai) ; aucune donnée inventée sur William :
le numéro de passeport, non fixé, est masqué comme sur les confirmations réelles.
"""
import argparse
import datetime as dt
import hashlib
import sys

from commun import ETAT, OUTILS, lire_csv, utf8

sys.path.insert(0, str(OUTILS))


def empreinte(*m):
    return int(hashlib.sha1("|".join(map(str, m)).encode("utf-8")).hexdigest(), 16)


def motif_qr(graine, n=25):
    """Matrice n × n : trois repères carrés aux coins (comme un code QR) et des modules tirés par empreinte."""
    h = hashlib.sha256(str(graine).encode()).digest() * 8
    bits = "".join(f"{b:08b}" for b in h)
    m = [[bits[(i * n + j) % len(bits)] == "1" for j in range(n)] for i in range(n)]
    for (r, c) in ((0, 0), (0, n - 7), (n - 7, 0)):
        for i in range(7):
            for j in range(7):
                bord = i in (0, 6) or j in (0, 6)
                centre = 2 <= i <= 4 and 2 <= j <= 4
                m[r + i][c + j] = bord or centre
        for i in range(-1, 8):  # marge blanche autour des repères
            for j in range(-1, 8):
                if 0 <= r + i < n and 0 <= c + j < n and (i in (-1, 7) or j in (-1, 7)):
                    m[r + i][c + j] = False
    return m


def inscrire(reservation, quand, simule=False):
    from pdf_base import DocPDF, chemin
    res = next((r for r in lire_csv(ETAT / "reservations.csv") if r["id"] == reservation), None)
    if res is None or res["type"] != "vol":
        sys.exit(f"Réservation de vol inconnue : {reservation}")
    import voyages
    segs = voyages.segments(res["vol"], "aller")
    dernier = segs[-1]
    arrivee = dt.date.fromisoformat(res["aller"]) + dt.timedelta(days=int(dernier["jour_arrivee"]))
    if not (0 < (dt.datetime.combine(arrivee, dt.time(*map(int, dernier["arrivee"].split(":")))) - quand - dt.timedelta(hours=6)).total_seconds() <= 72 * 3600):
        sys.exit("REFUSÉ : l'inscription n'est possible que dans les 72 heures avant l'arrivée (F064).")
    h = empreinte("etravel", reservation, quand.isoformat())
    ref = "ETR-" + f"{h % 10**10:010d}"
    hotel = next((r for r in lire_csv(ETAT / "reservations.csv") if r["type"] == "forfait" and r["aller"] == res["aller"]
                  and r["statut"] == "confirme"), None)
    adresse = (hotel["note"].split(" + ")[-1].split(" · ")[0] + ", Makati City, Metro Manila") if hotel else "à préciser"
    if simule:
        print(f"(essai) {ref} · arrivée {arrivee:%d/%m/%Y} {dernier['numero']} · {adresse}")
        return ref
    pdf = DocPDF("eTravel — Registration successful", "Philippine Travel Information System · etravel.gov.ph",
                 auteur="eTravel (Republic of the Philippines)", pied=f"eTravel — {ref}")
    pdf.meta("Registration no.", ref)
    pdf.meta("Traveller", "OSSIMI, William · Male · born 23 March 2005")
    pdf.meta("Nationality", "Luxembourgish · passport •••••••• (as registered)")
    pdf.meta("Residence", "France")
    pdf.meta("Travel type", "Arrival")
    pdf.meta("Date of arrival", f"{arrivee:%d %B %Y}")
    pdf.meta("Flight", f"{dernier['numero']} · {dernier['compagnie']} · from Doha (DOH) to Manila (MNL), arrival {dernier['arrivee']}")
    pdf.meta("Stay address", adresse)
    pdf.meta("Purpose of travel", "Holiday / leisure")
    pdf.meta("Health declaration", "No symptoms declared · countries visited in the last 30 days: Luxembourg, France")
    pdf.meta("Customs", "Nothing to declare")
    pdf.meta("Submitted", f"{quand:%d/%m/%Y %H:%M} (Luxembourg time)")
    m = motif_qr(ref)
    x0, y0, cote = 75, pdf.get_y() + 8, 2.4
    pdf.set_fill_color(0, 0, 0)
    for i, ligne in enumerate(m):
        for j, plein in enumerate(ligne):
            if plein:
                pdf.rect(x0 + j * cote, y0 + i * cote, cote, cote, style="F")
    pdf.set_y(y0 + len(m) * cote + 6)
    pdf.para("Present this QR code to the Immigration and Customs officers upon arrival. One registration per trip. "
             "eTravel registration is free of charge: the government never asks for payment.", taille=9, italique=True)
    nom = f"{quand:%Y-%m-%d}_Confirmation_eTravel_Philippines.pdf"
    cible = chemin("courriels", nom)
    pdf.sauver(cible)
    print(f"eTravel {ref} : {cible.relative_to(chemin()).as_posix()}")
    return ref


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("inscrire")
    p.add_argument("--reservation", required=True, help="réservation du vol d'arrivée (etat/reservations.csv)")
    p.add_argument("--quand", required=True, help="AAAA-MM-JJ HH:MM, heure du Luxembourg")
    p.add_argument("--simule", action="store_true")
    args = ap.parse_args()
    inscrire(args.reservation, dt.datetime.fromisoformat(args.quand), args.simule)
    return 0


if __name__ == "__main__":
    sys.exit(main())
