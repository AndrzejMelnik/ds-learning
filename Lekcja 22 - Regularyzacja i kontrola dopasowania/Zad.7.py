"""Wczytaj California Housing. Użyj RidgeCV z automatycznym doborem alpha.
Wypisz wybrane alpha i R² na zbiorze testowym.
    Dataset:
sklearn.datasets.fetch_california_housing()
    Wymagania:
RidgeCV z cv=5
alphas = np.logspace(-4, 4, 100)
Ewaluacja na oddzielnym zbiorze testowym"""
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

california = fetch_california_housing()
X = california.data
y = california.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

alphas = np.logspace(-4, 4, 100)