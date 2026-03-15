"""Zadanie 8 -- Early stopping eksperyment
Porownaj trening z i bez early_stopping.
    Wymagania:
Dataset: Breast Cancer
Architektura: (64, 32), solver='adam', max_iter=1000
Wariant 1: early_stopping=False
Wariant 2: early_stopping=True, validation_fraction=0.15
Porownaj: epoki, czas, accuracy

    Oczekiwany wynik:
Tabela porownawcza i wykresy loss"""
import time

from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

cancer_data = load_breast_cancer()
X, y = cancer_data.data, cancer_data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

configs = {
    'without early stopping': MLPClassifier(
        hidden_layer_sizes=(64, 32),
        solver='adam',
        max_iter=1000,
        early_stopping=False,
        random_state=42
    ),
    'with early stopping': MLPClassifier(
        hidden_layer_sizes=(64, 32),
        solver='adam',
        max_iter=1000,
        early_stopping=True,
        validation_fraction=0.15,
        random_state=42
    )
}

results = {}
plt.figure(figsize=(10, 6))

for name, mlp in configs.items():
    start = time.time()
    mlp.fit(X_train_sc, y_train)
    elapsed = time.time() - start

    y_pred = mlp.predict(X_test_sc)
    acc = accuracy_score(y_test, y_pred)

    results[name] = {
        'Accuracy': acc,
        'Czas treningu [s]': round(elapsed, 4),
        'Liczba epok': mlp.n_iter_
    }
    plt.plot(mlp.loss_curve_, label=f'{name} (Epoki: {mlp.n_iter_})')

df_results = pd.DataFrame(results).T
print("\n=== TABELA PORÓWNAWCZA (Zadanie 8) ===")
print(df_results)