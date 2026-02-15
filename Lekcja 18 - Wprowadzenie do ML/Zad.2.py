"""Zadanie 2 – Porównanie trzech algorytmów

Porównaj accuracy trzech algorytmów na datasecie Wine: LogisticRegression,
DecisionTree, KNN.
Dataset: sklearn.datasets.load_wine()

Wymagania:
Ten sam podział train/test dla wszystkich
Wydrukuj wyniki w formie tabeli"""

import sklearn


wine = sklearn.datasets.load_wine()
X, y = wine.data, wine.target