mots = ["chat", "chien", "chat", "oiseau", "chien", "chat"]

compte = {}

for mot in mots:
    compte[mot] = compte.get(mot, 0) + 1

print(compte)