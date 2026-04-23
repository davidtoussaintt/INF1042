import math

def distance_origine(point):
    x = point[0]
    y = point[1]
    distance = math.sqrt(x**2 + y**2)
    return distance

print(distance_origine((3, 4)))