long1 = int(input("Donne la longueure du rectangle: "))
larg1 = int(input("Donne la largeur du rectangle: "))
aire1 = long1 * larg1
print("L'aire du rectangle 1 est", aire1)

long2 = int(input("Donne la longueure du rectangle: "))
larg2 = int(input("Donne la largeur du rectangle: "))
aire2 = long2 * larg2
print("L'aire du rectangle 2 est", aire2)

if aire1 == aire2:
    print("Les aires des rectangles sont la meme!")
else:
    print("Les aire ne sont pas la meme!")