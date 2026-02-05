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
from scipy import stats

url = ("https://archive.ics.uci.edu/ml/machine-learning-databases"
       "/wine-quality/winequality-red.csv")
wine = pd.read_csv(url, sep=';')
print("Dataset Jakości Win:")
print(wine.head())
print("\nInfo:")
print(wine.info())

df = pd.DataFrame(wine, columns=['alcohol'])
print(df)

zscore = stats.zscore(df['alcohol'])
df['zscore'] = zscore
print(df[['alcohol', 'zscore']])

outliers = df[df['zscore'].abs()  > 3]
print(outliers)

without_outliers = df[df['zscore'].abs() <= 3]
print(without_outliers)



#########################################                               
#####  Brak boxplotów i statystyk   #####
#########################################