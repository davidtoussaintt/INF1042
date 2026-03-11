a = int(input("Longueur 1: "))
b = int(input("Longueur 2: "))
c = int(input("Longueur 3: "))

if a + b > c and a + c > b and b + c > a:
    print("C'est possible")
else:
    print("Ce n'est pas possible")