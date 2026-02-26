"""Zadanie 18 – Learning Curves dla klasyfikacji
Narysuj krzywe uczenia dla regresji logistycznej.

Dataset:
    Breast Cancer dataset
Wymagania:
    Użyj sklearn.model_selection.learning_curve
    Narysuj train score i validation score vs rozmiar danych
    Zinterpretuj: czy model ma bias/variance problem?
Oczekiwany rezultat:
    Wykres learning curves
    Analiza overfitting/underfitting"""
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X, y = data.data, data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression(max_iter=1000, random_state=42)

train_sizes, train_scores, val_scores = learning_curve(
    model, X_scaled, y,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

#Wizualizacja danych
plt.plot(train_sizes, train_scores.mean(axis=1), 'o-',
         label='Train Score', color='red')
plt.plot(train_sizes, val_scores.mean(axis=1), 'o-',
         label='Validation Score', color='green')

plt.fill_between(train_sizes,
                 train_scores.mean(axis=1) - train_scores.std(axis=1),
                 train_scores.mean(axis=1) + train_scores.std(axis=1),
                 alpha=0.1, color='red')

plt.fill_between(train_sizes,
                 val_scores.mean(axis=1) - val_scores.std(axis=1),
                 val_scores.mean(axis=1) + val_scores.std(axis=1),
                 alpha=0.1, color='green')
plt.xlabel('Rozmiar zbioru treningowego')
plt.ylabel('Accuracy')
plt.title('Learning Curves')
plt.legend(loc='best')
plt.grid(True, alpha=0.3)
plt.show()