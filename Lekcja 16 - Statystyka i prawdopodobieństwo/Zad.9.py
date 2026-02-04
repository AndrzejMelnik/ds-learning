"""Symuluj 1000 eksperymentów rzutu 20 monetami (p=0.5).
Porównaj histogram wyników z
teoretycznym rozkładem dwumianowym B(20, 0.5).

Dataset:
Wygeneruj używając np.random.binomial()

Wymagania:
Symulacja 1000 eksperymentów
Histogram wyników symulacji
Teoretyczny PMF rozkładu B(20, 0.5) nałożony na histogram
Porównanie średniej empirycznej z teoretyczną"""

import numpy as np

n= 20
p = 0.5
size = 1000
np.random.seed(42)
coin_flips = np.random.binomial(n , p, size)
print(coin_flips)