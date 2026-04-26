produit1 = ("Clavier", 49.99, 12)

print("Nom du produit :", produit1[0])
print("Prix :", produit1[1])
print("Quantité :", produit1[2])

nom, prix, quantite = produit1

print("Le produit", nom, "coûte", prix, "$ et il y en a", quantite, "en stock.")

produit2 = ("Souris", 29.99, 20)

nom2, prix2, quantite2 = produit2

if prix > prix2:
    print("Le produit le plus cher est :", nom)
else:
    print("Le produit le plus cher est :", nom2)