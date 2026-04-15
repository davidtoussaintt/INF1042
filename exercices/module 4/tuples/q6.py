matchs = (
("Tigres", "Lynx", 25, 18),
("Aigles", "Panthères", 22, 25),
("Tigres", "Panthères", 25, 23),
("Lynx", "Aigles", 19, 25),
("Tigres", "Aigles", 21, 25),
("Lynx", "Panthères", 25, 20)
)

victoires = {}
defaites = {}
points = {}

for equipe1, equipe2, score1, score2 in matchs:
        


if score1 > score2:
        print(f"{equipe1} ont battu {equipe2} par {score1} à {score2}")
        victoires[equipe1] += 1
        defaites[equipe2] += 1
    else:
        print(f"{equipe2} ont battu {equipe1} par {score2} à {score1}")
        victoires[equipe2] += 1
        defaites[equipe1] += 1

#idk M