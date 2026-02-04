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
from matplotlib import pyplot as plt
from scipy.stats import binom

n= 20
p = 0.5
size = 1000
np.random.seed(42)
coin_flips = np.random.binomial(n , p, size)
print(coin_flips)

#Wykres
plt.hist(coin_flips, bins=np.arange(-0.5, n + 1.5, 1),
         density=True, edgecolor='black')

x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

plt.scatter(x, pmf, color='red', label='Teoretyczny PMF')
plt.vlines(x, 0, pmf, colors='red', linestyles='dashed')

plt.title("Histogram z rozkładem dwumianowym (n=20, p=0.5)")
plt.xlabel("Liczba wyrzuconych orłów")
plt.ylabel("Stopień prawdopodobieństwa")
plt.legend()
plt.grid(True)
plt.show()


#Średnia teoretyczna i empiryczna

th_mean = n * p # 20 * 0.5
print("Srednia arytmetyczna(teoretyczna): ", th_mean)

emp_mean = np.mean(coin_flips)
print("Średnia empiryczna: ", emp_mean)

