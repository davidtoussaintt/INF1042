#David Toussaint
#Ce programme est un jeux de roche, papier, ciseaux contre l'ordi qui choisi un des symbol au hasard en utilisant random.randint
#J'ai aussi mis presque tout dans un while loop pour ca va continuer a ce repeter lorsque rematch est egale a 1 (ce qui veut dire que le joueur
# veut jouer encore) pour chaque gagne/defaite/egale etc j'ai ajoute +1 pour que chaque partie il ajoute 1 dependant au resultat du match
#J'aimerai aussi dire que j'avais deja fais cela avec Chase Curwin dans le club mais la partie de afficher les stats ou rejouer etait nouveau
# et un peu un challenge car je voulais s'avoir comment je pourrais le faire plus simple et claire

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
