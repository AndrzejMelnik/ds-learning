"""Zadanie 13 -- Wiele modeli w jednym API
Zbuduj API obsługujące wiele modeli: /predict/v1 (LogReg), /predict/v2
(RandomForest),/predict/v3 (GradientBoosting).
Klient wybiera wersję modelu.
Oczekiwany wynik: API z 3 modelami, porównanie predykcji
"""
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X, y = data.data, data.target