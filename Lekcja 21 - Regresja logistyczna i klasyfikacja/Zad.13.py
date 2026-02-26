"""Zadanie 13 – Precision-Recall tradeoff
    Zbadaj trade-off między Precision a Recall dla różnych progów.
Dataset:
    Niezbalansowany dataset (95:5)
Wymagania:
    Wygeneruj dane z make_classification (weights=[0.95, 0.05])
    Dla progów od 0.1 do 0.9 oblicz Precision i Recall
    Znajdź próg dający najlepszy balans (F1)
    Znajdź próg maksymalizujący Recall przy Precision > 0.5
Oczekiwany rezultat
    Wykres: Precision i Recall vs próg
    Analiza trade-offu"""

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
n_samples=1000,
n_features=20,
n_informative=10,
n_redundant=5,
n_classes=2,
weights=[0.95, 0.05],
random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
results = {}

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)