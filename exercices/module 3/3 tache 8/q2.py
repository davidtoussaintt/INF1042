nombre = int(input("Entrez un nombre: "))

if nombre % 3 ==0:
    print("C'est divisible par 3")

if nombre % 5 ==0:
    print("C'est divisible par 5")

if nombre % 5== 0 and nombre % 3==0:
    print("Donc divisible par les deux")

else:
    print("Ce n'est pas divisible par 5 ou 3")