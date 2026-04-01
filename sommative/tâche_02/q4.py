#David Toussaint
# Ce programme demande à l'utilisateur combien de valeurs il veut simuler.
# Il génère ensuite des nombres aléatoires entre 1 et 4 plusieurs fois.
# Il compte combien de fois chaque valeur apparaît.
# À la fin, il affiche le nombre d'occurrences et le pourcentage de chaque valeur.
# Durant ma revision mon frere ma apprit quelque chose pour le rendre plus simple.
# Au lieu de {print("Valeur 1 :", val1, "fois (", p1, "% )") }
# Il ma montrer de arroundir le decimal avec un decimal. Donc si par example diviser par 3, au lieu de 33.3333333% ca done seulement 33.3%

import random

n = int(input("Combien de valeurs veux-tu simuler: "))
while n <= 0:
    n = int(input("Entre un nombre plus grand que 0: "))

val1 = 0
val2 = 0
val3 = 0
val4 = 0

for i in range(n):
    nombre = random.randint(1, 4)

    if nombre == 1:
        val1 = val1 + 1
    elif nombre == 2:
        val2 = val2 + 1
    elif nombre == 3:
        val3 = val3 + 1
    else:
        val4 = val4 + 1

# calcul des pourcentages
p1 = (val1 / n) * 100
p2 = (val2 / n) * 100
p3 = (val3 / n) * 100
p4 = (val4 / n) * 100

print("Valeur 1 :", val1, "fois (", round(p1,1), "% )")
print("Valeur 2 :", val2, "fois (", round(p2,1), "% )")
print("Valeur 3 :", val3, "fois (", round(p3,1), "% )")
print("Valeur 4 :", val4, "fois (", round(p4,1), "% )")