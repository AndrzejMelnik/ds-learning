"""Napisz własną funkcję, która oblicza zakres międzykwartylowy
(IQR = Q3 - Q1) i zastosuj ją
do grupy.

Dataset: California Housing

Wymagania:
Napisz funkcję iqr_func(x) obliczającą IQR
Zastosuj ją do MedHouseVal według regionów
Porównaj IQR między regionami

Oczekiwany rezultat:
Tabela z IQR dla każdego regionu """


from scipy.stats import describe
from sklearn.datasets import fetch_california_housing
import pandas as pd
import geopip

housing = fetch_california_housing(as_frame=True)
df_housing = housing.frame

print(df_housing.head())

describe_data = df_housing.describe()



# iqr = describe_data.loc['75%'] - describe_data.loc['25%']
# print(iqr)

describe_data['Region'] = (
    pd.cut(describe_data["Latitude"], bins=3, labels=["Południe",
          "Centrum", "Północ"]).astype(str) + " " +
          pd.cut(describe_data["Longitude"],
          bins=3, labels=["Zachód", "Centrum", "Wschód"]).astype(str)
)
# print(describe_data[["Latitude", "Longitude", 'Region']])
print(describe_data.columns)