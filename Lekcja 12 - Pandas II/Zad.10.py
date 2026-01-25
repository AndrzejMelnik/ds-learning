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

from sklearn.datasets import fetch_california_housing
import pandas as pd

housing = fetch_california_housing(as_frame=True)
df_housing = housing.frame

print(df_housing.head())


