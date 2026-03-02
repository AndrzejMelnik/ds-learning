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
from sklearn.linear_model import RidgeCV
from sklearn.metrics import r2_score
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

ridge_cv = RidgeCV(alphas=alphas, cv=5, scoring='neg_mean_squared_error')
ridge_cv.fit(X_train_scaled, y_train)
print(f"Optymalne alpha: {ridge_cv.alpha_:.4f}")

y_pred_test = ridge_cv.predict(X_test_scaled)
y_pred_train = ridge_cv.predict(X_train_scaled)
