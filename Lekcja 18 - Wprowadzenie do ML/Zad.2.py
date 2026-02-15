"""Zadanie 2 – Porównanie trzech algorytmów

Porównaj accuracy trzech algorytmów na datasecie Wine: LogisticRegression,
DecisionTree, KNN.
Dataset: sklearn.datasets.load_wine()

Wymagania:
Ten sam podział train/test dla wszystkich
Wydrukuj wyniki w formie tabeli"""

import sklearn
from sklearn.model_selection import train_test_split

wine = sklearn.datasets.load_wine()
X, y = wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=42,stratify=y)

print(f"Rozmiar zbioru treningowego: {X_train.shape[0]}")
print(f"Rozmiar zbioru testowego: {X_test.shape[0]}")