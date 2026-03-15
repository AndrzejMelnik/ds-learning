"""Zadanie 8 -- Early stopping eksperyment
Porownaj trening z i bez early_stopping.
    Wymagania:
Dataset: Breast Cancer
Architektura: (64, 32), solver='adam', max_iter=1000
Wariant 1: early_stopping=False
Wariant 2: early_stopping=True, validation_fraction=0.15
Porownaj: epoki, czas, accuracy

    Oczekiwany wynik:
Tabela porownawcza i wykresy loss"""

from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer()
X, y = cancer_data.data, cancer_data.target