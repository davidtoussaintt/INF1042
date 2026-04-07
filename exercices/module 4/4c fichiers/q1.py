import random

with open("valeurs.txt", "w", encoding="utf-8") as f:
    for i in range(1000):
        number = random.randint(0, 100000)
        f.write(str(number) + "\n")