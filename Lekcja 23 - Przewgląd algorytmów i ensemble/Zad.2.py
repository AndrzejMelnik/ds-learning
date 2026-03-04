"""Przetestuj wartosci k od 1 do 20 na datasecie Iris z walidacja krzyzowa (cv=5).
    Wymagania:
Oblicz srednia accuracy dla kazdego k
Narysuj wykres accuracy vs k
Wskaż optymalna wartosc k

    Oczekiwany wynik:
Wykres z zaznaczonym optymalnym k"""
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

k_range = range(1, 31)
cv_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train_scaled, y_train, cv=5,
    scoring='accuracy')
    cv_scores.append(scores.mean())

best_k = list(k_range)[np.argmax(cv_scores)]
print(f"Optymalna wartość k: {best_k}")

