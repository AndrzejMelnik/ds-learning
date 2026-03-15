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

from sklearn.datasets import load_breast_cancer
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