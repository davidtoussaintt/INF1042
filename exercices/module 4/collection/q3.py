import random

A = set()
B = set()

for i in range(10):
    A.add(random.randint(1, 20))
    B.add(random.randint(1, 20))

print("A =", A)
print("B =", B)

print("Union :", A.union(B))
print("Intersection :", A.intersection(B))
print("Différence A - B :", A.difference(B))
print("Différence B - A :", B.difference(A))