inventaire = {
    "stylos": 24,
    "cahiers": 15,
    "gommes": 10
}

print("Quantité de cahiers :", inventaire["cahiers"])

inventaire["marqueurs"] = 18
inventaire["stylos"] = 30
del inventaire["gommes"]

print("Inventaire mis à jour :", inventaire)

for produit, quantite in inventaire.items():
    print(produit, ":", quantite)

total_articles = sum(inventaire.values())
#ajoute tout les valeurs
print("Nombre total d'articles en stock :", total_articles)