import joblib
import json
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV


class HoneyModelManager:
    def __init__(self):
        # ROZWIĄZANIE: Ustawiamy domyślnie 'elasticnet', co pozwala modelowi
        # być zarówno Lasso, Ridge, jak i czymś pomiędzy, zależnie od l1_ratio.
        self.base_model = LogisticRegression(
            penalty='elasticnet',
            solver='saga',
            max_iter=5000,
            random_state=42
        )
        self.best_model = None

    def tune_regularization(self, X_train, y_train):
        #Zgodnie z ostrzeżeniem sklearn, przestajemy używać parametru 'penalty' w siatce.
        #Teraz sterujemy wszystkim przez 'l1_ratio' [Lekcja 22]:
        #l1_ratio=0.0 to odpowiednik penalty='l2' (Ridge)
        #l1_ratio=1.0 to odpowiednik penalty='l1' (Lasso)
        #l1_ratio=0.5 to mieszanka obu (ElasticNet)
        param_grid = {
            'l1_ratio': [0.0, 0.5, 1.0],  # Testujemy L2, ElasticNet i L1
            'C': [0.1, 1.0, 10.0]  # Siła regularyzacji (odwrotność)
        }

        #GridSearchCV dobierze teraz najlepszy balans między L1 a L2
        grid = GridSearchCV(self.base_model, param_grid, cv=5, scoring='f1', n_jobs=-1)
        grid.fit(X_train, y_train)

        self.best_model = grid.best_estimator_
        print(f"Najlepsze parametry (zoptymalizowane): {grid.best_params_}")

    def save_assets(self, scaler, features):
        joblib.dump(self.best_model, "models/best_model.pkl")
        joblib.dump(scaler, "models/scaler.pkl")
        metadata = {"features": features, "params": self.best_model.get_params()}
        with open("models/metadata.json", "w") as f:
            json.dump(metadata, f)