#David Toussaint
# Ce programme calcule le coût du stationnement.
# Il demande le nombre d'heures stationnées et si la voiture est électrique.
# Le coût est de 4$ pour la première heure et 3$ pour chaque heure supplémentaire.
# Si le stationnement dépasse 5 heures, un frais de 10$ est ajouté.
# Si la voiture est électrique, un rabais de 20% est appliqué.
# Le programme affiche ensuite le prix final.
# Apres plusieur fautes et essaye j'ai fais mon programme plus simple. Ex:
# Avant pour tout les frais += x, j'avais mis frais = frais + x. Mais apres d'avoir eu l'appuit de mon frere, il ma montrer une facon plus simple

hr_stationnées = int(input("Entrez le nombre d'heures stationnées: "))
voiture_électrique = int(input("Est ce que la voiture est électrique 1 (oui) ou  2 (non): "))

while voiture_électrique not in [1, 2]:
    voiture_électrique = int(input("Est ce que la voiture est électrique 1 (oui) ou  2 (non): "))

frais = 4

if hr_stationnées > 1:
    hr_sup = hr_stationnées - 1 
    frais += (hr_sup * 3)

if hr_stationnées > 5:
    frais += 10
    
prix_finale = frais

if voiture_électrique == 1:
     prix_finale = prix_finale * 0.8
    

print("Le coût total du stationnement est:", round(prix_finale, 2), "$")