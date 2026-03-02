"""Wczytaj California Housing. Użyj LassoCV. Wypisz optymalne alpha
oraz ile cech zostało
wyzerowanych.
    Dataset: sklearn.datasets.fetch_california_housing()
    Wymagania:
LassoCV z cv=5
Policz cechy gdzie |coef| < 1e-6
Wypisz nazwy aktywnych cech
    Oczekiwany rezultat:
Alpha, liczba niezerowych cech, lista aktywnych cech"""

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

california = fetch_california_housing()
X = california.data
y = california.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)