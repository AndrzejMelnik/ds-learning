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