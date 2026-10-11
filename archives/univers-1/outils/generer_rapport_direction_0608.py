"""Rapport quotidien d'Aïcha (lundi 06/08/2040, 17h04) -> serveur/direction/rapport_direction_0608.pdf

Omis dans le récit du 06/08 (correction n° 43) ; déposé à 17h04 (heure d'Abidjan), notification à William à 18h04 (heure de Lisbonne), non ouvert.
Faits : dépôt au CEPICI (Me Kouamé, 09h20) ; salaire de la gérante refait en paiement instantané (08h05) ; tableau de trésorerie d'Estelle reçu
par courriel (ITS de juin non retenu en bas de page) ; contrat de la villa relu avec Grace ; question des clauses posée à Me Kouamé (14h30) ;
ITS et CNPS de juillet préparés. Ton : vouvoiement, factuel ; rien sur l'organigramme ni sur l'appel de 13h33 (évitement).
"""
from osia_pdf import OsiaPDF, serveur

pdf = OsiaPDF("Rapport de direction — lundi 6 août 2040",
              "OSIA Énergies — établi par Aïcha Diomandé, gérante — à l'attention de M. William Ossimi — 17h04")
pdf.titre1("1. Ce qui s'est passé")
pdf.puces([
    "Formalités de l'augmentation de capital et des statuts modifiés déposées ce matin au guichet unique du CEPICI par Maître Kouamé. Extrait RCCM attendu sous une à deux semaines.",
    "Salaire de juillet de la gérante refait ce matin par paiement instantané, sur votre accord écrit du 5 août. Le virement rejeté doit revenir sur le compte d'OSIA d'ici le 14 août.",
    "Tableau de trésorerie de Mme Estelle reçu par courriel ; il est classé dans finances/.",
    "Contrat de la villa Riviera relu avec Grace, article par article. Signature mercredi 8 août.",
    "Question posée à Maître Kouamé sur les clauses de rétrogradation, de promotion et de licenciement ; réponse attendue.",
    "ITS et CNPS de juillet préparés : paiement de l'ITS avant le 10 août, de la CNPS avant le 15 août.",
])
pdf.titre1("2. Décisions prises")
pdf.puces(["Aucune décision nouvelle aujourd'hui."])
pdf.titre1("3. Décisions qui vous concernent")
pdf.puces(["Aucune aujourd'hui."])
pdf.titre1("4. Prochains jours")
pdf.puces(["Mardi 7/08 : fête nationale, QG fermé.",
           "Mercredi 8/08 : signature du contrat de la villa.",
           "Vendredi 10/08 : paiement de l'ITS de juillet."])
pdf.para("Aïcha Diomandé", italique=True)
pdf.sauver(serveur("direction", "rapport_direction_0608.pdf"))
