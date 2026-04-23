import random

liste = []
for i in range(100):
    liste.append(random.randint(1, 20))

print("Liste originale :")
print(liste)

sans_doublons = set(liste)
liste_triee = sorted(list(sans_doublons))

print("Liste triée sans doublons :")
print(liste_triee)