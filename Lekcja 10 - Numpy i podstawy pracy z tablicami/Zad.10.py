"""Dana tablica ocen (5 studentów x 4 egzaminy)

exams = np.array([
[78, 85, 92, 88],
[65, 72, 68, 70],
[90, 88, 95, 92],
[55, 60, 58, 62],
[82, 79, 85, 80]
])

Dodaj bonus do każdego egzaminu: [5, 10, 5, 10]

Następnie pomnóż wyniki każdego studenta
przez mnożnik: [1.0, 1.1, 0.95, 1.15, 1.0]"""

import numpy as np

exams = np.array([
[78, 85, 92, 88],
[65, 72, 68, 70],
[90, 88, 95, 92],
[55, 60, 58, 62],
[82, 79, 85, 80]
])
print("Shape dla 'exams': ", exams.shape)

bonus = np.array([5, 10, 5, 10])
print("Shape dla 'bonus': ", bonus.shape)

multiplier = np.array([1.0, 1.1, 0.95, 1.15, 1.0])
print("Shape dla mnożnika: ", multiplier.shape)

exams_with_bonus = exams + bonus
print("Egzaminy z bonusem: ", exams_with_bonus)


