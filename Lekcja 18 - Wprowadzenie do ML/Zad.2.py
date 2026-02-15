"""Zadanie 2 – Porównanie trzech algorytmów

Porównaj accuracy trzech algorytmów na datasecie Wine: LogisticRegression,
DecisionTree, KNN.
Dataset: sklearn.datasets.load_wine()

Wymagania:
Ten sam podział train/test dla wszystkich
Wydrukuj wyniki w formie tabeli"""

import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

wine = sklearn.datasets.load_wine()
X, y = wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=42,stratify=y)

print(f"Rozmiar zbioru treningowego: {X_train.shape[0]}")
print(f"Rozmiar zbioru testowego: {X_test.shape[0]}")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) # fit + transform na train
X_test_scaled = scaler.transform(X_test)

models = {
'Logistic Regression': LogisticRegression(max_iter=1000),
'Decision Tree': DecisionTreeClassifier(random_state=42),
'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5)}

print("\nPorównanie algorytmów:")
print("-" * 50)
for name, model in models.items():
    model.fit(X_train_scaled, y_train) # Trening
    train_score = model.score(X_train, y_train) # Accuracy na train
    test_score = model.score(X_test_scaled, y_test) # Accuracy na test
    print(f"{name:25s} | Train: {train_score:.3f} | Test: {test_score:.3f}")