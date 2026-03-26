notes = []

choix = ""

while choix != "5":
    print("1. Entrer des notes")
    print("2. Calculer la moyenne")
    print("3. Compter les réussites (>=50)")
    print("4. Compter les échecs (<50)")
    print("5. Quitter")

    choix = input("Choix: ")

    # 1. Entrer des notes
    if choix == "1":
        n = int(input("Combien de notes? "))
        
        for i in range(n):
            note = int(input("Entrer une note: "))
            notes.append(note)

    # 2. Moyenne
    elif choix == "2":
        if len(notes) == 0:
            print("Aucune note")
        else:
            total = 0
            for note in notes:
                total = total + note
            
            moyenne = total / len(notes)
            print("Moyenne:", moyenne)

    # 3. Réussites
    elif choix == "3":
        compteur = 0
        for note in notes:
            if note >= 50:
                compteur = compteur + 1
        print("Réussites:", compteur)

    # 4. Échecs
    elif choix == "4":
        compteur = 0
        for note in notes:
            if note < 50:
                compteur = compteur + 1
        print("Échecs:", compteur)

    # 5. Quitter
    elif choix == "5":
        print("Au revoir!")

    else:
        print("Choix invalide")