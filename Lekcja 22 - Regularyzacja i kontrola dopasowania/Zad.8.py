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
from sklearn.linear_model import LassoCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

california = fetch_california_housing()
X = california.data
y = california.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lasso_cv = LassoCV(cv=5, max_iter=10000, random_state=42)
lasso_cv.fit(X_train_scaled, y_train)