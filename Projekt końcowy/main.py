from src.data_handler import HoneyDataHandler
from src.anomaly_detector import HoneyAnomalyDetector
from src.model_manager import HoneyModelManager
from src.visualizer import HoneyVisualizer
from sklearn.metrics import classification_report


def run_project():
    #Przygotowanie danych
    handler = HoneyDataHandler()
    (X_tr, X_te, y_tr, y_te), feats = handler.load_and_prepare()
    X_tr_sc, X_te_sc = handler.scale_data(X_tr, X_te)

    #Detekcja anomalii
    X_tr_cl, y_tr_cl = HoneyAnomalyDetector().clean_train_data(X_tr_sc, y_tr)

    #Model i optymalizacja regularyzacji
    manager = HoneyModelManager()
    manager.tune_regularization(X_tr_cl, y_tr_cl)

    #Ewaluacja i wizualizacja [32]
    y_pred = manager.best_model.predict(X_te_sc)
    y_prob = manager.best_model.predict_proba(X_te_sc)[:, 1]

    print("\nRAPORT KLASYFIKACJI:\n", classification_report(y_te, y_pred))
    HoneyVisualizer.plot_diagnostics(y_te, y_pred, y_prob, feats, manager.best_model)

    #Zapis artefaktów
    manager.save_assets(handler.scaler, feats)

if __name__ == "__main__":
    run_project()