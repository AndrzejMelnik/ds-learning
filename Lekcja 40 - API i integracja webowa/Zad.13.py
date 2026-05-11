"""Zadanie 13 -- Wiele modeli w jednym API
Zbuduj API obsługujące wiele modeli: /predict/v1 (LogReg), /predict/v2
(RandomForest),/predict/v3 (GradientBoosting).
Klient wybiera wersję modelu.
Oczekiwany wynik: API z 3 modelami, porównanie predykcji
"""
from sklearn.datasets import load_breast_cancer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier

data = load_breast_cancer()
X, y = data.data, data.target

model_v1 = make_pipeline(StandardScaler(), LogisticRegression()).fit(X, y)
model_v2 = RandomForestClassifier(n_estimators=100, max_depth=10).fit(X, y)
model_v3 = GradientBoostingClassifier(n_estimators=100).fit(X, y)
