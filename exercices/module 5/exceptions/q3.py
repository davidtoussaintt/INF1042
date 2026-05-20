solde = 250.00

try:
    montant = input("Montant à retirer : ")
    montant = float(montant)

    if montant <= 0:
        raise ValueError("Erreur : le montant doit être plus grand que 0.")

    if montant > solde:
        raise ValueError("Erreur : fonds insuffisants.")

except ValueError as erreur:
    print(erreur)

else:
    solde = solde - montant
    print("Retrait accepté.")
    print("Nouveau solde :", solde, "$")

finally:
    print("Fin de la transaction.")