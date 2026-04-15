import random

eleves = { "Maksym", "Léo", "Hayden", "Angel", "Ibrahim", "Josh", "Grant", "Maxime", "David" }

while eleves:
    nom = random.choice(list(eleves))
    print(nom)
    eleves.remove(nom) 