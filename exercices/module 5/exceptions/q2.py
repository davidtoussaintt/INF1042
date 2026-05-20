try:
    note1 = input("Note 1 : ")
    note2 = input("Note 2 : ")

    note1 = float(note1)
    note2 = float(note2)

    if note1 < 0 or note1 > 100 or note2 < 0 or note2 > 100:
        raise ValueError("les notes doivent être entre 0 et 100.")

except ValueError:
    print("Erreur : les notes doivent être numériques.")

else:
    moyenne = (note1 + note2) / 2
    print("Moyenne :", moyenne)

finally:
    print("Fin du programme.")