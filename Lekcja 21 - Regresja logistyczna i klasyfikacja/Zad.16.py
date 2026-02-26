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
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X, y = data.data, data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression(max_iter=1000, random_state=42)

#Walidacja krzyżowa
strat_fold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
score_list = ['accuracy', 'precision', 'recall', 'f1']

cross_val = cross_validate(model, X_scaled, y, cv=strat_fold,
                           scoring=score_list)

#Tabela z naszymi wynikami
table = pd.DataFrame({
    'Metryki': ['Accuracy', 'Precision', 'Recall', 'F1-score'],
    'Średnia': [
        cross_val['test_accuracy'].mean(),
        cross_val['test_precision'].mean(),
        cross_val['test_recall'].mean(),
        cross_val['test_f1'].mean()
    ],
    'Odchylenie standardowe': [
        cross_val['test_accuracy'].std(),
        cross_val['test_precision'].std(),
        cross_val['test_recall'].std(),
        cross_val['test_f1'].std()
    ]
})
print(table)