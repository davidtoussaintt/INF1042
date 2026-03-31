#David Toussaint

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
