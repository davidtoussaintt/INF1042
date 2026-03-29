heure = int(input("Entrez une heure (0 à 23): "))

if heure == 0:
    print("12 am")
elif heure < 12:
    print(heure, "am")
elif heure == 12:
    print("12 pm")
else:
    print(heure - 12, "pm")