"""Zadanie 10 – Wykres czasowy

Utwórz wykres ceny akcji w czasie z:
    Główną linią ceny
    Średnią kroczącą 7-dniową (MA7)
    Średnią kroczącą 21-dniową (MA21)
    Zacienionym obszarem między MA7 a MA21 """

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

np.random.seed(42)
dates = pd.date_range('2025-01-01', periods=100)
price = 100 + np.cumsum(np.random.randn(100))
df = pd.DataFrame({'date': dates, 'price': price})
print(df)

fig, ax = plt.subplots(3, 1, figsize=(18, 14))
ax = ax.flatten()

#Pierwszy wykres - Główna linia ceny
ax[0].plot(df['date'], df['price'], color='#2E86AB', # kolor hex
           linewidth=2.5,
           marker='o', # okrągłe markery
           markersize=8,
           markerfacecolor='white',
           markeredgewidth=2)
ax[0].set_title("Wykres cen akcji w czasie")
ax[0].set_ylabel('Cena akcji', fontsize=12)
df['7-dniowa średnia krocząca'] = df['price'].rolling(window=7,
                                    min_periods=1).mean()
print(df)

ax[1].plot(df['date'], df['7-dniowa średnia krocząca'])
ax[1].set_title("7-dniowa średnia krocząca")
ax[1].set_ylabel('Cena akcji', fontsize=12)

#21 dniowa średnia krocząca
df['21-dniowa średnia krocząca'] = df['price'].rolling(window=21,
                                    min_periods=1).mean()
ax[2].plot(df['date'], df['21-dniowa średnia krocząca'])
ax[2].set_title("21-dniowa średnia krocząca")
ax[2].set_xlabel('Data', fontsize=12)
ax[2].set_ylabel('Cena akcji', fontsize=12)

