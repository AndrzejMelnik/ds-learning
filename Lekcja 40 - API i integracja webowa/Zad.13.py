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
import joblib

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from typing import Dict
from typing import List, Annotated
from pydantic import BaseModel, Field

data = load_breast_cancer()
X, y = data.data, data.target

model_v1 = make_pipeline(StandardScaler(), LogisticRegression()).fit(X, y)
model_v2 = RandomForestClassifier(n_estimators=100, max_depth=10).fit(X, y)
model_v3 = GradientBoostingClassifier(n_estimators=100).fit(X, y)

joblib.dump(model_v1, "model_v1.pkl")
joblib.dump(model_v2, "model_v2.pkl")
joblib.dump(model_v3, "model_v3.pkl")

class PredictionInput(BaseModel):
    features: Annotated[List[float], Field(min_length=30, max_length=30)]

app = FastAPI(title="Multi-Model ML API")

try:
    models = {
        "v1": joblib.load("model_v1.pkl"),
        "v2": joblib.load("model_v2.pkl"),
        "v3": joblib.load("model_v3.pkl")
    }
except FileNotFoundError:
    print("Błąd: Pliki modeli nie istnieją. Uruchom najpierw skrypt trenujący.")
    models = {}
