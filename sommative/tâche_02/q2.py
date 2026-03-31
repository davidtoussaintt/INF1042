#David Toussaint
#Ce programme est capable de convertir des valeur celsius en valeur Fahrenheit et Kelvin en utilisant la formule de chaque unite
#Temp = température

Temp_Celsius = int(input("C'est quoi la température en Celsius: "))

Temp_Fahrenheit = (Temp_Celsius * 9)/5 + 32
Temp_Kelvin = Temp_Celsius + 273.15

print("La température en celsius: ", Temp_Celsius, "°C")
print("La température en Fahrenheit: ", Temp_Fahrenheit, "°F")
print("La température en Kelvin: ", Temp_Kelvin, "K")