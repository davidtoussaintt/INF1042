print("Pizza party!")

eleves = int(input("Entrez le nombre d'eleves: "))
pointes = int(input("Entrez le nombre de pointes (pizza): "))
n = pointes//eleves
reste = pointes % eleves

if pointes % eleves ==0:
    print("Chaque eleves peuvent avoir", n, "pizza")
else:
    print("Chaque eleves peuvent avoir", n, "Cepedant", reste, "pointes ne peuvent pas être distribuées également")