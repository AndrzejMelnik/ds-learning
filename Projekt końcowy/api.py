from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI(title="Honey Purity API")
model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")

class HoneyRequest(BaseModel):
    features: list[float] #lista parametrów chemicznych

@app.post("/predict")
def predict(data: HoneyRequest):
    X = np.array([data.features])
    X_sc = scaler.transform(X) #ten sam scaler co w treningu
    prediction = int(model.predict(X_sc))
    return {"is_pure": prediction, "label": "Pure" if prediction == 1 else "Adulterated"}