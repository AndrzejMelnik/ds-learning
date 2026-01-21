

""" Część I

Masz 2 punkty w przestrzeni 5-wymiarowej:

point_a = np.array([1, 2, 3, 4, 5])
point_b = np.array([5, 4, 3, 2, 1])

Oblicz odległość Euklidesową: sqrt(sum((a - b)^2)) """

import numpy as np

point_a = np.array([1, 2, 3, 4, 5])
point_b = np.array([5, 4, 3, 2, 1])

def distance_a_b(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))

print(distance_a_b(point_a, point_b))