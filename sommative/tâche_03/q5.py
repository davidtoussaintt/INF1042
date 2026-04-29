eleves = [
    {
        "nom": "Ava",
        "niveau": 12,
        "activites": ["programmation", "robotique", "mathématiques"]
    },
    {
        "nom": "Liam",
        "niveau": 11,
        "activites": ["robotique", "sport"]
    },
    {
        "nom": "Emma",
        "niveau": 12,
        "activites": ["arts", "mathématiques"]
    },
    {
        "nom": "Noah",
        "niveau": 10,
        "activites": ["robotique", "échecs"]
    }
]
print("Noms des élèves :")
for eleve in eleves:
    print(eleve["nom"])

print("Élèves de 12e année :")
for eleve in eleves:
    if eleve["niveau"] == 12:
        print(eleve["nom"])

activites_uniques = set()
#En set car il y a pas de dupes
for eleve in eleves:
    for activite in eleve["activites"]:
        activites_uniques.add(activite)

print("Activités uniques :", activites_uniques)

eleve_max = eleves[0]

for eleve in eleves:
    if len(eleve["activites"]) > len(eleve_max["activites"]):
        eleve_max = eleve
#comparaison des length de chaque activite des eveles pour trouver qui a le plus
print("Élève avec le plus d'activités :", eleve_max["nom"])

compteur_robotique = 0

for eleve in eleves:
    if "robotique" in eleve["activites"]:
        compteur_robotique += 1

print("Nombre d'élèves en robotique :", compteur_robotique)