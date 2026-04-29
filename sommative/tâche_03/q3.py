liste_a = ["Batterie", "Basse", "Piano", "Basse", "Guitare", "Batterie"]
liste_b = ["Piano", "Voix", "Guitare", "Synthé", "Piano"]

ensemble_a = set(liste_a)
ensemble_b = set(liste_b)

print("Chanson uniques du liste A sont", ensemble_a)
print("Chanson uniques du liste B sont", ensemble_b)

print("Chansons dans les deux listes :", ensemble_a & ensemble_b)

print("Chansons seulement dans une des deux listes :", ensemble_a ^ ensemble_b)

print("Toutes les chansons uniques combinées :", ensemble_a | ensemble_b)

