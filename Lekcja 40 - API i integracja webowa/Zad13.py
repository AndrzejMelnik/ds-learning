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

from fastapi import FastAPI,HTTPException
import joblib

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

@app.post("/predict/v1")
def predict_v1(input_data: PredictionInput):
    """Predykcja modelem LogisticRegression (v1)."""
    prediction = models["v1"].predict([input_data.features])
    return {"version": "v1", "model": "LogisticRegression", "prediction": int(prediction)}

@app.post("/predict/v2")
def predict_v2(input_data: PredictionInput):
    """Predykcja modelem RandomForest (v2)."""
    prediction = models["v2"].predict([input_data.features])
    return {"version": "v2", "model": "RandomForest", "prediction": int(prediction)}

@app.post("/predict/v3")
def predict_v3(input_data: PredictionInput):
    """Predykcja modelem GradientBoosting (v3)."""
    prediction = models["v3"].predict([input_data.features])
    return {"version": "v3", "model": "GradientBoosting", "prediction": int(prediction)}


@app.post("/predict/compare")
def compare_models(input_data: PredictionInput):
    """Zwraca predykcje ze wszystkich modeli naraz."""
    results = {}
    for version, model in models.items():
        pred = model.predict([input_data.features])
        results[version] = int(pred)

    return {
        "input_summary": "Breast Cancer Data",
        "predictions": results,
        "consistent": len(set(results.values())) == 1
    }


@app.get("/health")
def health_check():
    return {"status": "online", "models_loaded": list(models.keys())}

"""Uruchomienie w terminalu komendą uvicorn Zad13:app --reload
 w przeglądarce: http://127.0.0.1:8000/docs#/default/predict_v2_predict_v2_post"""
