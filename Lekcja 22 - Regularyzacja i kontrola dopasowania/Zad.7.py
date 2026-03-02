"""Wczytaj California Housing. Użyj RidgeCV z automatycznym doborem alpha.
Wypisz wybrane alpha i R² na zbiorze testowym.
    Dataset:
sklearn.datasets.fetch_california_housing()
    Wymagania:
RidgeCV z cv=5
alphas = np.logspace(-4, 4, 100)
Ewaluacja na oddzielnym zbiorze testowym"""

from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()
X = california.data
y = california.target