from sklearn.ensemble import IsolationForest

class HoneyAnomalyDetector:
    def __init__(self, contamination=0.03):
        self.model = IsolationForest(contamination=contamination, random_state=42)

    def clean_train_data(self, X, y):
        # Wykrywanie anomalii w zbiorze treningowym
        preds = self.model.fit_predict(X)
        X_clean = X[preds == 1]
        y_clean = y[preds == 1]
        print(f"Usunięto {len(X) - len(X_clean)} anomalii.")
        return X_clean, y_clean