code = input("Donne moi un code postal: ")

if len(code) == 7 and code [3] == " ":
    if code[0].isalpha() and code[1].isdigit() and code[2].isalpha() and code[4].isdigit() and code[5].isalpha() and code[6].isdigit():
        print("True")
    #Ici je demande pour chaque lettre/nombre du code si ca va suivre les conditions. Donc lettre--> nombre et continue

else:
    print("Pas vrai")