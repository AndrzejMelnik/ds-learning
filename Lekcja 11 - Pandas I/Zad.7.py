"""Zadanie 7 – Sortowanie DataFrame

Posortuj pasażerów Titanica po wieku (od najmłodszego do najstarszego).

Wymagania:
Użyj .sort_values()
Wyświetl 10 najmłodszych
Wyświetl 10 najstarszych """

import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)
print(df)
print(df.columns)



