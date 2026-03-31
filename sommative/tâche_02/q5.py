import random

defaite = 0
victoire = 0
egale = 0
parties = 0
rematch = 1

while rematch == 1:
    answer = int(input("Rock (1), papier (2), ciseaux (3): "))
    while answer not in [1, 2, 3]:
        answer = int(input("Choix invalide. Choisis 1, 2 ou 3: "))
    ai_answer = random.randint(1,3)

    win_con = {
        1: 3,
        2: 1,
        3: 2,
    }

    if ai_answer == 1:
        print("Ordi a choisi Pierre")
    elif ai_answer == 2:
        print("Ordi a choisi Papier")
    else:
        print("Ordi a choisi ciseaux")

    if answer == ai_answer:
        print("C'est egale")
        egale = egale + 1
        parties = parties + 1

    elif win_con[answer] == ai_answer:
        print("Tu gagnes!")
        victoire = victoire + 1
        parties = parties + 1

    else:
        print("Tu perds")
        defaite = defaite + 1
        parties = parties + 1

    rematch = int(input("Est ce que tu veux continuer à jouer, 1 (oui) ou 2 (non): "))
if rematch == 2:
    print("Nombre de defaite: ", defaite)
    print("Nombre de vicoire: ", victoire)
    print("Nombre d'egalite: ", egale)
    print("Nombre de parties joue: ", parties)

while rematch not in [1, 2]:
    rematch = int(input("Choix invalide. 1 ou 2: "))
