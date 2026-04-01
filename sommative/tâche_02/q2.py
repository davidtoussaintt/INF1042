#David Toussaint
# Ce programme demande à l'utilisateur une température en Celsius.
# Il convertit cette température en Fahrenheit et en Kelvin
# en utilisant les formules mathématiques appropriées.
# finalement, il affiche les trois températures.
#Temp = température

Temp_Celsius = int(input("C'est quoi la température en Celsius: "))

Temp_Fahrenheit = (Temp_Celsius * 9)/5 + 32
Temp_Kelvin = Temp_Celsius + 273.15

print("La température en celsius: ", Temp_Celsius, "°C")
print("La température en Fahrenheit: ", Temp_Fahrenheit, "°F")
print("La température en Kelvin: ", Temp_Kelvin, "K")