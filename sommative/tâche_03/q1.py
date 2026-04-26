notes = [78, 85, 92, 67, 85, 74]

print("Liste complète :", notes)

print("Première note :", notes[0])
print("Dernière note :", notes[-1])

notes.append(88)
print("Après avoir ajouté 88 :", notes)

notes.remove(85)
print("Après avoir supprimé le premier 85 :", notes)

total = sum(notes)
moyenne = total / len(notes)
note_max = max(notes)
note_min = min(notes)

print("Total des notes :", total)
print("Moyenne :", moyenne)
print("Note la plus élevée :", note_max)
print("Note la plus basse :", note_min)
