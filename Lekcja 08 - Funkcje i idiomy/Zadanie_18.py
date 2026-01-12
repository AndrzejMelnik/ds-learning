"""Zadanie 18 – Funkcja kroswalidacji (podstawowa wersja)
Napisz funkcję k_fold_split(dane, k) , która dzieli dane na k części (foldów) do
walidacji krzyżowej.

dane = list(range(1, 101)) # 100 obserwacji

Wymagania:

k = 5 (5-fold cross-validation)
Podziel dane na 5 równych części
Funkcja zwraca listę foldów (każdy fold to lista)
Użyj slicing i comprehensions

Oczekiwany rezultat:

5 foldów po 20 elementów każdy
Fold 1: [1-20], Fold 2: [21-40],

"""

dane = list(range(1, 101))

def k_fold_split(dane, k=5):
    lista = [[]]
    k_fold = len(dane) // k
    lista = [dane[i * k_fold : (i + 1) * k_fold] for i in range(k)]
    return lista

