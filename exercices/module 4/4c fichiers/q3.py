with open("valeurs.txt", "r", encoding="utf-8") as f, \
     open("bas.txt", "w", encoding="utf-8") as bas, \
     open("haut.txt", "w", encoding="utf-8") as haut:

    for line in f:
        number = int(line.strip())

        if number <= 49999:
            bas.write(str(number) + "\n")
        else:
            haut.write(str(number) + "\n")