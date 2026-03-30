import random


prenom = input("Prénom : ")
nom = input("Nom : ")
annee = int(input("Année de naissance : "))
ville = input("Ville : ")


username = prenom + nom
print("Nom d'utilisateur :", username)


email = prenom + "." + nom + "@" + ville + ".ca"
print("Email :", email)


age = 2026 - annee

if age >= 18:
    print("Tu as 18 ans ou plus")
else:
    print("Tu as moins de 18 ans")


part1 = prenom[0:2]   
part2 = nom[-2:]      


lettres = "abcde12345"
random_part = ""

for i in range(4):
    random_part = random_part + random.choice(lettres)

password = part1 + part2 + str(annee) + random_part

print("Mot de passe :", password)