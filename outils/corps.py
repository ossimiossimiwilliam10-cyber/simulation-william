"""CORPS DE WILLIAM (créé le 11/10/2026) : sommeil, entraînements, repas, poids, maladies, blessures. Règle du §12 (« suivi léger
du sommeil, du sport et de l'alimentation ; ses effets colorent les scènes ») rendue mesurable : la dette de sommeil et la charge
d'entraînement se CALCULENT, au lieu d'une ligne de prose (« réveillé à 07h05, reposé »).

    python outils/corps.py nuit --coucher "2040-07-13 23:40" --lever "2040-07-14 08:10"   # une nuit (latence d'endormissement déduite)
    python outils/corps.py decalage --heures 7 [--quand "2041-07-22 08:12"]       # arrivée avec un décalage : trois nuits perturbées (R1)
    python outils/corps.py seance --duree 90 --note "MMA : sparring léger" [--quand "2040-07-14 18:00"] [--intensite haute]
    python outils/corps.py noter --type repas --note "pâtes au thon, 13h"         # repas, poids (--valeur 99.5), malade, blessure, note
    python outils/corps.py etat                                                   # bilan pour le moteur (jamais montré en chiffres)

Effets (ce que le moteur MONTRE, sans chiffres) : dette de sommeil > 3 h sur 7 jours = fatigue visible (bâillements, irritabilité,
réflexes) ; > 6 h = épuisement ; 0 séance depuis 4 jours = manque, nervosité ; 3 séances intenses en 3 jours = courbatures.
Ils colorent les scènes ; ils ne modifient AUCUNE réaction tirée (une table « défaillance de William » serait à valider par
l'utilisateur : voir memoire/propositions-2026-10-11.md).
Repères : besoin de sommeil d'un adulte 7 à 9 h (on retient 7 h 30) ; profil de William : 1,96 m, ≈ 100 kg, MMA et musculation
cinq jours par semaine depuis onze ans.
"""
import argparse
import datetime as dt
import sys

from commun import ETAT, ecrire_csv, lire_csv, maintenant_simule, utf8

FICHIER = ETAT / "corps.csv"
COLONNES = ["date", "heure", "type", "valeur", "unite", "note"]
BESOIN_SOMMEIL = 7.5
LATENCE_MIN = 15
HABITUDE_SEANCES = 5


def lire():
    return lire_csv(FICHIER)


def ajouter(ligne):
    lignes = lire()
    lignes.append(ligne)
    lignes.sort(key=lambda l: (l["date"], l["heure"] or "00:00"))
    ecrire_csv(FICHIER, lignes, COLONNES)


def instant(texte):
    d, h = texte.split()
    return dt.datetime.combine(dt.date.fromisoformat(d), dt.time.fromisoformat(h))


def maintenant():
    t = maintenant_simule()
    return t.replace(tzinfo=None) if t else dt.datetime(2040, 7, 14, 9, 0)


def decalage_actif(au):
    """(heures, numéro de la nuit à venir ou de la dernière nuit, 1 à 3) si un décalage horaire est en cours, sinon None."""
    des = [l for l in lire() if l["type"] == "decalage" and f"{l['date']} {l['heure'] or '00:00'}" <= f"{au:%Y-%m-%d %H:%M}"]
    if not des:
        return None
    d = des[-1]
    jours = (au.date() - dt.date.fromisoformat(d["date"])).days
    return (float(d["valeur"] or 0), jours) if 0 <= jours <= 3 else None


def perturbation_decalage(lever):
    """R1 (validé le 22/10/2026) : trois premières nuits après l'arrivée, endormissement tardif et réveil nocturne (tirés, consignés)."""
    import random
    des = [l for l in lire() if l["type"] == "decalage" and f"{l['date']} {l['heure'] or '00:00'}" <= f"{lever:%Y-%m-%d %H:%M}"]
    if not des:
        return 0.0, ""
    n = (lever.date() - dt.date.fromisoformat(des[-1]["date"])).days
    if not 1 <= n <= 3:
        return 0.0, ""
    bornes = {1: ((60, 120), (45, 90)), 2: ((30, 75), (20, 60)), 3: ((15, 40), (0, 30))}[n]
    rng = random.SystemRandom()
    latence, reveil = rng.randint(*bornes[0]), rng.randint(*bornes[1])
    import jet
    jet.consigner_json({"mode": "procedure", "libelle": f"Décalage horaire, nuit n° {n} : endormissement tardif de {latence} min, réveil nocturne de {reveil} min",
                        "pour": "", "valeur": f"{latence}+{reveil}", "regle": "corps.py (R1, 22/10/2026)"})
    return (latence + reveil) / 60, f"décalage horaire, nuit n° {n} : endormissement tardif ({latence} min), réveil nocturne ({reveil} min)"


def bilan(au=None):
    au = au or maintenant()
    lignes = [l for l in lire() if f"{l['date']} {l['heure'] or '00:00'}" <= f"{au:%Y-%m-%d %H:%M}"]
    nuits = [l for l in lignes if l["type"] == "sommeil"]
    seances = [l for l in lignes if l["type"] == "entrainement"]
    sept = au - dt.timedelta(days=7)
    nuits7 = [l for l in nuits if instant(f"{l['date']} {l['heure'] or '08:00'}") >= sept]
    dette = sum(max(0.0, BESOIN_SOMMEIL - float(l["valeur"] or 0)) for l in nuits7)
    derniere = float(nuits[-1]["valeur"]) if nuits else None
    s7 = [l for l in seances if instant(f"{l['date']} {l['heure'] or '18:00'}") >= sept]
    s3 = [l for l in seances if instant(f"{l['date']} {l['heure'] or '18:00'}") >= au - dt.timedelta(days=3)
          and "haute" in (l.get("note") or "")]
    depuis = (au - instant(f"{seances[-1]['date']} {seances[-1]['heure'] or '18:00'}")).days if seances else None
    poids = next((float(l["valeur"]) for l in reversed(lignes) if l["type"] == "poids" and l["valeur"]), 100.0)
    malade = [l for l in lignes if l["type"] in ("malade", "blessure") and l["date"] >= f"{au - dt.timedelta(days=10):%Y-%m-%d}"]
    deca = decalage_actif(au)
    if dette > 6:
        etat = "épuisé : yeux lourds, gestes lents, patience courte"
    elif deca and deca[1] <= 3:
        etat = (f"décalage horaire de {deca[0]:g} h (jour {deca[1] + 1}) : somnolence en début d'après-midi, faim à contretemps, "
                "éveillé la nuit" + (" ; fatigué : bâillements" if dette > 3 else ""))
    elif dette > 3:
        etat = "fatigué : bâillements, irritabilité en fin de journée"
    elif len(s3) >= 3:
        etat = "courbatures, raideur au réveil"
    elif depuis is not None and depuis >= 4:
        etat = "en manque d'entraînement : nerveux, besoin de se dépenser"
    else:
        etat = "reposé, en forme"
    return {"derniere_nuit": derniere, "nuits_connues_7j": len(nuits7), "dette_7j": round(dette, 1), "seances_7j": len(s7),
            "minutes_7j": int(sum(float(l["valeur"] or 0) for l in s7)), "jours_depuis_seance": depuis, "poids": poids,
            "recent_malade_blesse": [f"{l['date']} {l['type']} : {l['note']}" for l in malade], "etat": etat}


def donnees_telephone(t=None):
    """Application Santé du téléphone : sommeil des 14 dernières nuits, entraînements, poids (ce que montrerait une montre)."""
    au = (t.replace(tzinfo=None) if t is not None and t.tzinfo else t) or maintenant()
    lignes = [l for l in lire() if f"{l['date']} {l['heure'] or '00:00'}" <= f"{au:%Y-%m-%d %H:%M}"]
    b = bilan(au)
    nuits = [{"date": l["date"], "heures": float(l["valeur"] or 0)} for l in lignes if l["type"] == "sommeil"][-14:]
    seances = [{"date": l["date"], "minutes": int(float(l["valeur"] or 0)), "note": (l.get("note") or "")[:60]}
               for l in lignes if l["type"] == "entrainement"][-14:]
    return {"nuits": nuits, "seances": seances, "dette_7j": b["dette_7j"], "seances_7j": b["seances_7j"], "minutes_7j": b["minutes_7j"],
            "poids": b["poids"], "besoin": BESOIN_SOMMEIL}


def ligne_etat(b):
    morceaux = [f"nuit dernière {b['derniere_nuit']:.1f} h" if b["derniere_nuit"] is not None else "nuit dernière inconnue",
                f"dette de sommeil sur 7 j : {b['dette_7j']:g} h ({b['nuits_connues_7j']} nuit(s) notée(s))",
                f"{b['seances_7j']} séance(s) en 7 j (habitude {HABITUDE_SEANCES})",
                f"dernière séance : {'il y a ' + str(b['jours_depuis_seance']) + ' j' if b['jours_depuis_seance'] is not None else 'inconnue'}",
                f"poids {b['poids']:g} kg"]
    return "Corps : " + " ; ".join(morceaux) + f" -> à montrer : {b['etat']}" + (
        " ; récent : " + " / ".join(b["recent_malade_blesse"]) if b["recent_malade_blesse"] else "")


def main():
    utf8()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("nuit")
    p.add_argument("--coucher", required=True)
    p.add_argument("--lever", required=True)
    p.add_argument("--note", default="")
    p.add_argument("--sans-decalage", action="store_true", help="n'applique pas la perturbation du décalage horaire (vol, sieste)")
    p = sp.add_parser("decalage")
    p.add_argument("--heures", type=float, required=True, help="écart entre l'heure de départ et celle d'arrivée")
    p.add_argument("--quand", help="AAAA-MM-JJ HH:MM (arrivée), sinon l'horloge")
    p = sp.add_parser("seance")
    p.add_argument("--duree", type=int, required=True, help="minutes")
    p.add_argument("--note", default="")
    p.add_argument("--intensite", choices=("legere", "moyenne", "haute"), default="moyenne")
    p.add_argument("--quand")
    p = sp.add_parser("noter")
    p.add_argument("--type", required=True, choices=("repas", "poids", "malade", "blessure", "note", "alcool", "soin"))
    p.add_argument("--valeur", default="")
    p.add_argument("--note", default="")
    p.add_argument("--quand")
    sp.add_parser("etat")
    args = ap.parse_args()
    if args.cmd == "decalage":
        q = instant(args.quand) if args.quand else maintenant()
        ajouter({"date": f"{q:%Y-%m-%d}", "heure": f"{q:%H:%M}", "type": "decalage", "valeur": f"{args.heures:g}", "unite": "h",
                 "note": f"arrivée avec {args.heures:g} h de décalage horaire (R1)"})
        print(f"Décalage horaire de {args.heures:g} h noté : trois nuits perturbées.")
    elif args.cmd == "nuit":
        c, l = instant(args.coucher), instant(args.lever)
        heures = max(0.0, (l - c).total_seconds() / 3600 - LATENCE_MIN / 60)
        perte, note_dec = perturbation_decalage(l) if not args.sans_decalage else (0.0, "")
        heures = max(0.0, heures - perte)
        ajouter({"date": f"{l:%Y-%m-%d}", "heure": f"{l:%H:%M}", "type": "sommeil", "valeur": f"{heures:.2f}", "unite": "h",
                 "note": f"coucher {c:%d/%m %H:%M}, lever {l:%H:%M}" + (f" ; {note_dec}" if note_dec else "") + (f" ; {args.note}" if args.note else "")})
        print(f"Nuit notée : {heures:.1f} h de sommeil." + (f" ({note_dec})" if note_dec else ""))
    elif args.cmd == "seance":
        q = instant(args.quand) if args.quand else maintenant()
        ajouter({"date": f"{q:%Y-%m-%d}", "heure": f"{q:%H:%M}", "type": "entrainement", "valeur": str(args.duree), "unite": "min",
                 "note": f"{args.note} (intensité {args.intensite})".strip()})
        print("Séance notée.")
    elif args.cmd == "noter":
        q = instant(args.quand) if args.quand else maintenant()
        ajouter({"date": f"{q:%Y-%m-%d}", "heure": f"{q:%H:%M}", "type": args.type, "valeur": args.valeur,
                 "unite": "kg" if args.type == "poids" else "", "note": args.note})
        print(f"{args.type} noté.")
    print(ligne_etat(bilan()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
