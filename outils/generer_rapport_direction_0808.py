"""Rapport quotidien d'Aïcha (mercredi 08/08/2040, 17h00) -> serveur/direction/rapport_direction_0808.pdf

William est hors ligne (message du 07/08). Faits tirés : aléa A04 (délestage au QG le matin, groupe électrogène hors service) ; signature de la
villa malgré le délestage (jet 80 % : OUI, 52.1), chez le client ; acompte pas encore reçu (jet : NON, 72.7) ; ITS de juillet payé (jet : OUI,
16.0) ; convention de Me Kouamé signée (jet : OUI, 29.5) ; régularisation de l'ITS de juin sur les salaires d'août de la gérante et de la DRH
(T7c : execute_sans_discuter, 69.8), à la demande de M. Ossimi transmise par Mme Estelle. Ton : vouvoiement, factuel.
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de direction — mercredi 8 août 2040",
              "OSIA Énergies — établi par Aïcha Diomandé, gérante — à l'attention de M. William Ossimi — 17h00")
pdf.titre1("1. Ce qui s'est passé")
pdf.puces([
    "Coupure de courant au QG de 7h40 à 11h20 ; le groupe électrogène est toujours hors service. L'équipe a travaillé sur batteries et sur la 4G.",
    "Contrat de la villa Riviera signé à 11h30 chez le client, à la Riviera, par la gérante, en présence de Grace. Facture d'acompte envoyée : 3 180 000 FCFA HT, soit 3 752 400 FCFA TTC. Le client annonce le virement sous huit jours.",
    "ITS de juillet payé aujourd'hui. CNPS de juillet : paiement avant le 15 août.",
    "Convention d'honoraires de Maître Kouamé signée : modèle de contrat de cadre, règlement intérieur et matrice d'évaluation, 600 000 FCFA HT.",
    "Mme Estelle m'a transmis votre demande sur l'ITS de juin, non retenu sur les salaires de la gérante et de la DRH. Mariette applique la retenue sur les salaires d'août : 133 500 et 112 500 FCFA.",
])
pdf.titre1("2. Décisions prises")
pdf.puces(["Commande du matériel de la villa dès réception de l'acompte, selon votre autorisation du 1er août ; au-delà de 5 millions, double signature avec M. Kanga."])
pdf.titre1("3. Décisions qui vous concernent")
pdf.puces(["Projets pilotes en location (note de Grace du 3 août) : toujours en attente de votre décision.",
           "Groupe électrogène du QG : devis de réparation demandé ; je vous le transmets dès réception."])
pdf.titre1("4. Prochains jours")
pdf.puces(["Vendredi 10/08 : point avec Grace sur les pilotes.",
           "Mardi 14/08 : raccordement de la fibre (à confirmer) ; retour attendu du virement rejeté.",
           "Mercredi 15/08 : CNPS de juillet."])
pdf.para("Aïcha Diomandé", italique=True)
pdf.sauver(serveur("direction", "rapport_direction_0808.pdf"))
