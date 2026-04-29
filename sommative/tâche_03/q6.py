achats = [
    ("Liam", "Galaxy Battle", "PC", 59.99),
    ("Emma", "Speed Zone", "PlayStation", 49.99),
    ("Liam", "Pixel Quest", "Switch", 39.99),
    ("Noah", "Galaxy Battle", "PC", 59.99),
    ("Emma", "Sky Builder", "PC", 29.99),
    ("Olivia", "Speed Zone", "Xbox", 54.99),
    ("Liam", "Sky Builder", "PC", 29.99),
    ("Noah", "Pixel Quest", "Switch", 39.99)
]

print("Tous les achats :")
for achat in achats:
    print(achat)

jeux_uniques = set()

for achat in achats:
    client, jeu, plateforme, prix = achat
    jeux_uniques.add(jeu)

print("Jeux uniques :", jeux_uniques)

# Crée un ensemble contenant toutes les plateformes uniques
plateformes_uniques = set()

for achat in achats:
    client, jeu, plateforme, prix = achat
    plateformes_uniques.add(plateforme)

print("Plateformes uniques :", plateformes_uniques)

# 4. Calcule le montant total dépensé par tous les clients
total_depense = 0

for achat in achats:
    client, jeu, plateforme, prix = achat
    total_depense += prix

print("Montant total dépensé :", total_depense, "$")


# 5. Crée un dictionnaire qui indique combien chaque client a dépensé au total
depenses_clients = {}

for achat in achats:
    client, jeu, plateforme, prix = achat

    if client in depenses_clients:
        depenses_clients[client] += prix
    else:
        depenses_clients[client] = prix

print("Dépenses par client :", depenses_clients)


# 6. Détermine quel client a dépensé le plus d'argent
client_max = ""
montant_max = 0

for client in depenses_clients:
    if depenses_clients[client] > montant_max:
        montant_max = depenses_clients[client]
        client_max = client

print("Client qui a dépensé le plus :", client_max)
print("Montant dépensé :", montant_max, "$")


# 7. Crée un dictionnaire qui indique combien de fois chaque jeu a été acheté
compteur_jeux = {}

for achat in achats:
    client, jeu, plateforme, prix = achat

    if jeu in compteur_jeux:
        compteur_jeux[jeu] += 1
    else:
        compteur_jeux[jeu] = 1

print("Nombre de fois que chaque jeu a été acheté :", compteur_jeux)


# 8. Affiche seulement les achats faits sur PC
print("Achats faits sur PC :")

for achat in achats:
    client, jeu, plateforme, prix = achat

    if plateforme == "PC":
        print(client, "a acheté", jeu, "pour", prix, "$")


# Trouver le jeu le plus acheté pour le résumé final
jeu_plus_achete = ""
nombre_max = 0

for jeu in compteur_jeux:
    if compteur_jeux[jeu] > nombre_max:
        nombre_max = compteur_jeux[jeu]
        jeu_plus_achete = jeu


# 9. Affiche un résumé final
print("Résumé final :")
print("Nombre total d'achats :", len(achats))
print("Jeux uniques :", jeux_uniques)
print("Plateformes uniques :", plateformes_uniques)
print("Client qui a dépensé le plus :", client_max)
print("Jeu le plus acheté :", jeu_plus_achete)