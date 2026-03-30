import random
import time

nb = int(input("Combien de questions ? "))

bonnes = 0

for i in range(nb):
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    start = time.time()

    reponse = int(input(str(a) + " x " + str(b) + " = "))

    end = time.time()

    if reponse == a * b:
        print("Correct !")
        bonnes = bonnes + 1
    else:
        print("Faux")

    print("Temps :", round(end - start, 2), "sec")

print("Tu as", bonnes, "bonnes réponses sur", nb)