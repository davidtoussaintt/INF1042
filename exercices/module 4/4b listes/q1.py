notes = [12, 15, 9, 18, 15, 12]

moy = sum(notes) / len(notes)
print(moy)

max_count = 0
plus_freq = None

for n in notes:
    count = notes.count(n)
    if count > max_count:
        max_count = count
        plus_freq = n

print(plus_freq)