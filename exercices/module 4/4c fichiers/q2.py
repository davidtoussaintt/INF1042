with open("valeurs.txt", "r", encoding="utf-8") as f:
    numbers = []

    for line in f:
        numbers.append(int(line.strip()))

maximum = max(numbers)
minimum = min(numbers)
moy = sum(numbers) / len(numbers)

print("Max:", maximum)
print("Min:", minimum)
print("Moyenne:", moy)