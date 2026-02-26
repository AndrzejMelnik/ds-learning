"""Zadanie 16 – Cross-validation dla klasyfikacji
    Przeprowadź walidację krzyżową modelu klasyfikacyjnego.
Dataset:
    Breast Cancer dataset
Wymagania:
    Użyj StratifiedKFold (5 foldów)
    Oblicz średnią i odchylenie standardowe dla: accuracy, precision, recall, f1
    Użyj cross_val_score i cross_validate
Oczekiwany rezultat:
    Tabela z metrykami (mean ± std)
    Boxplot metryk z CV"""


from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X, y = data.data, data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)