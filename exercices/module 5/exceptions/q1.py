try:
    texte = input("Entrez votre âge : ")
    age = int(texte)

except ValueError:
    raise ValueError("l'âge doit être un nombre entier.")

else:
    print(f"Vous avez {age} ans.")