"""Zadanie 7 – Sortowanie DataFrame

Posortuj pasażerów Titanica po wieku (od najmłodszego do najstarszego).

Wymagania:
Użyj .sort_values()
Wyświetl 10 najmłodszych
Wyświetl 10 najstarszych """

import pandas as pd



# Błędne wyniki -- 10 najmłodszych pasażerów

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print(df)
print(df.columns)
df_clean = df.dropna(subset=['Age'])
the_youngest_10 = df_clean.sort_values('Age').head(10)
print(the_youngest_10[['PassengerId', 'Age']])








