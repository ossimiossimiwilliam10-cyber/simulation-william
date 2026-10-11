"""Note de Grace : étude des offres en location (vendredi 03/08/2040, déposée à 15h59) -> serveur/commercial/etude_offres_location_0308.pdf

Commandée par Aïcha avec l'accord de principe de William (31/07, « au moins un premier client d'ici fin août ») ; annoncée par Grace le
31/07 (« je la dépose sur le serveur vendredi »). Heure tirée : 13h00 + 74.6 × 2,4 min. Chiffres : annuité calculée sur 21 400 000 FCFA HT
(devis de la clinique), taux implicite de 14 % l'an, 84 mois ; maintenance forfaitaire. Trésorerie d'OSIA ≈ 138 M FCFA (31/07).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Étude : offres en location",
              "OSIA Énergies — direction commerciale — note de Grace Adjoua-Mensah — 3 août 2040")
pdf.meta("Destinataires", "Mme Aïcha Diomandé, gérante ; M. William Ossimi, associé unique")
pdf.meta("Origine", "Refus du conseil de la clinique de Marcory (31/07) : offre concurrente en location sur sept ans, sans investissement de départ")

pdf.titre1("1. Ce que veut le marché")
pdf.puces([
    "Cliniques, écoles privées, hôtels : la direction accepte le solaire, mais refuse de sortir 15 à 25 millions d'un coup.",
    "Ils comparent une mensualité à ce qu'ils paient déjà : gasoil du groupe, facture CIE, pannes liées aux délestages.",
    "Le concurrent retenu par la clinique propose une location sur sept ans, maintenance comprise, sans apport.",
])

pdf.titre1("2. Deux modèles possibles")
pdf.tableau(["Modèle", "Principe", "Avantage", "Risque"], [
    ["Location-vente", "Mensualité fixe sur 5 à 7 ans ; propriété transférée au client à la fin",
     "Simple à vendre ; trésorerie récupérée avec marge", "Impayés ; matériel installé chez le client"],
    ["Vente d'énergie", "Le client paie les kWh produits, à un prix inférieur au réseau ou au gasoil",
     "Argument très fort", "Comptage, litiges, rentabilité lente"],
], (28, 62, 40, 40))

pdf.titre1("3. Exemple chiffré (base : devis de la clinique)")
pdf.puces([
    "Installation : 21 400 000 FCFA HT.",
    "Location-vente sur 84 mois, taux implicite de 14 % l'an : environ 401 000 FCFA HT par mois, plus 25 000 FCFA de maintenance, soit environ 426 000 FCFA HT par mois.",
    "Total encaissé sur sept ans : environ 35 800 000 FCFA HT.",
    "Pour la clinique, la mensualité doit rester sous sa dépense actuelle de gasoil et d'électricité (à vérifier sur ses factures).",
])

pdf.titre1("4. Limites pour OSIA")
pdf.puces([
    "Avec la trésorerie actuelle (environ 138 millions), quatre ou cinq installations moyennes au plus, et rien pour le reste.",
    "Chaque installation immobilise la trésorerie plusieurs années : il faut des garanties (caution bancaire, domiciliation des paiements, dépôt de garantie).",
    "Au-delà de deux projets, un partenaire financier (banque ou société de crédit-bail) est nécessaire.",
])

pdf.titre1("5. Proposition")
pdf.puces([
    "Deux projets pilotes en location-vente, choisis parmi les prospects de juillet : l'école privée et l'hôtel.",
    "Relance du Dr Yapi si le contrat du concurrent tarde.",
    "Rendez-vous avec une banque ou une société de crédit-bail en septembre.",
    "Décision de la direction et autorisation de l'associé (engagements de plus de 5 millions) avant toute offre.",
])
pdf.para("G. Adjoua-Mensah", italique=True)

pdf.sauver(serveur("commercial", "etude_offres_location_0308.pdf"))
