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
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X, y = data.data, data.target
