"""Dla datasetu Wine Quality zidentyfikuj outliery w kolumnie alcohol metodą z-score
(wartości > mean ± 3*std). Usuń outliery i porównaj statystyki przed/po.

Dataset:
Wine Quality

Wymagania:

Oblicz z-scores
Zidentyfikuj outliery (|z| > 3)
Boxplot przed i po usunięciu
Porównanie statystyk (mean, median, std)"""

import pandas as pd

url = ("https://archive.ics.uci.edu/ml/machine-learning-databases"
       "/wine-quality/winequality-red.csv")
wine = pd.read_csv(url, sep=';')
print("Dataset Jakości Win:")
print(wine.head())
print("\nInfo:")
print(wine.info())