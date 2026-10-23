"""CARTE D'ARRIVÉE ÉLECTRONIQUE DE CORÉE DU SUD (e-Arrival Card ; créée le 22/10/2026, arrivée de William à Séoul). Formalité en ligne
gratuite (F089) : elle n'est valable que si l'on entre dans le pays dans les 72 heures suivant son envoi ; un code QR est présenté au
contrôle d'immigration. Confirmation reçue par courriel, en PDF dans `courriels/` (règle 4 du fichier maître).

    python outils/e_arrival.py soumettre --reservation R001 --quand "2041-07-22 08:52" [--simule]

Le portail est en anglais (fidèle au vrai) ; le numéro de passeport, non fixé, est masqué comme sur les confirmations réelles. Le code QR
du PDF est un motif tiré par empreinte (voir etravel.py). Modèle de `etravel.py` (Philippines, univers 2).
"""
import argparse
import datetime as dt
import sys

from commun import ETAT, OUTILS, lire_csv, utf8

sys.path.insert(0, str(OUTILS))


def soumettre(reservation, quand, simule=False):
    from pdf_base import DocPDF, chemin
    import etravel
    import voyages
    res = next((r for r in lire_csv(ETAT / "reservations.csv") if r["id"] == reservation), None)
    if res is None or res["type"] != "vol":
        sys.exit(f"Réservation de vol inconnue : {reservation}")
    segs = voyages.segments(res["vol"], "aller")
    dernier = segs[-1]
    arrivee = dt.date.fromisoformat(res["aller"]) + dt.timedelta(days=int(dernier["jour_arrivee"]))
    debut_fenetre = dt.datetime.combine(arrivee, dt.time(*map(int, dernier["arrivee"].split(":")))) - dt.timedelta(hours=72)
    if quand < debut_fenetre - dt.timedelta(hours=7):  # heure de Séoul ; l'envoi n'est valable que 72 heures avant l'entrée
        sys.exit("REFUSÉ : la carte n'est valable que si l'on entre en Corée dans les 72 heures suivant son envoi (F089).")
    h = etravel.empreinte("e-arrival", reservation, quand.isoformat())
    ref = "EAC-" + f"{h % 10**10:010d}"
    if simule:
        print(f"(essai) {ref} · arrivée {arrivee:%d/%m/%Y} {dernier['numero']}")
        return ref
    retour = dt.date.fromisoformat(res["retour"])
    pdf = DocPDF("e-Arrival Card — Submission completed", "Korea e-Arrival Card · Ministry of Justice, Republic of Korea",
                 auteur="e-Arrival Card (Republic of Korea)", pied=f"e-Arrival Card — {ref}")
    pdf.meta("Submission no.", ref)
    pdf.meta("Traveller", "OSSIMI, William · Male · born 23 March 2005")
    pdf.meta("Nationality", "Luxembourgish · passport •••••••• (as registered)")
    pdf.meta("Country of residence", "France")
    pdf.meta("Date of arrival", f"{arrivee:%d %B %Y}")
    pdf.meta("Flight", f"{dernier['numero']} · {dernier['compagnie']} · from Paris (CDG) to Seoul Incheon (ICN), arrival {dernier['arrivee']}")
    pdf.meta("Address in Korea", "Furnished officetel, Yeonnam-dong, Mapo-gu, Seoul (booked through Stayeon)")
    pdf.meta("Intended stay", f"until {retour:%d %B %Y}")
    pdf.meta("Purpose of visit", "Tourism")
    pdf.meta("Health declaration", "No symptoms declared")
    pdf.meta("Customs declaration", "Nothing to declare")
    pdf.meta("Submitted", f"{quand:%d/%m/%Y %H:%M} (Seoul time)")
    m = etravel.motif_qr(ref)
    x0, y0, cote = 75, pdf.get_y() + 8, 2.4
    pdf.set_fill_color(0, 0, 0)
    for i, ligne in enumerate(m):
        for j, plein in enumerate(ligne):
            if plein:
                pdf.rect(x0 + j * cote, y0 + i * cote, cote, cote, style="F")
    pdf.set_y(y0 + len(m) * cote + 6)
    pdf.para("Present this QR code to the immigration officer. Valid only if you enter Korea within 72 hours of submission. "
             "The e-Arrival Card is free of charge: the government never asks for payment.", taille=9, italique=True)
    nom = f"{quand:%Y-%m-%d}_Confirmation_e-Arrival_Card_Coree.pdf"
    cible = chemin("courriels", nom)
    pdf.sauver(cible)
    print(f"e-Arrival Card {ref} : {cible.relative_to(chemin()).as_posix()}")
    return ref


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("soumettre")
    p.add_argument("--reservation", required=True, help="réservation du vol d'arrivée (etat/reservations.csv)")
    p.add_argument("--quand", required=True, help="AAAA-MM-JJ HH:MM, heure de Séoul")
    p.add_argument("--simule", action="store_true")
    args = ap.parse_args()
    soumettre(args.reservation, dt.datetime.fromisoformat(args.quand), args.simule)
    return 0


if __name__ == "__main__":
    sys.exit(main())
