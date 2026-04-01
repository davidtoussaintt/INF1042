#David Toussaint
# Ce programme demande le prix d'achat à l'utilisateur.
# Il calcule un rabais selon le montant:
# - 0% si le prix est inférieur à 50$
# - 10% si le prix est entre 50$ et 100$
# - 15% si le prix est supérieur à 100$
# Ensuite, il calcule le prix après rabais, ajoute une taxe de 13%,
# et affiche tous les résultats (prix initial, rabais, taxe, prix total).

prix = int(input("Entrez le prix d'achat: "))
def rabais(prix):
    if prix<50:
        rab = 0 
    elif prix>=50 and prix<=100:
        rab = prix * 0.1
    else:
        rab = prix * 0.15
    return rab


rab = rabais(prix)
prix_ap_rab = prix - rab
taxe = prix_ap_rab * 0.13
prix_totale = prix_ap_rab + taxe

print("Prix: ", prix, "dollars")
print("Rabais: ", rab, "dollars")
print("Prix avec rabais: ", prix_ap_rab, "dollars")
print("Taxe: ", taxe, "dollars.")
print("Le prix totale est donc", prix_totale, "dollars.")
