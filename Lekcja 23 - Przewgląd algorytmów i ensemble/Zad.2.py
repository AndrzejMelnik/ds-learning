"""Przetestuj wartosci k od 1 do 20 na datasecie Iris z walidacja krzyzowa (cv=5).
    Wymagania:
Oblicz srednia accuracy dla kazdego k
Narysuj wykres accuracy vs k
Wskaż optymalna wartosc k

    Oczekiwany wynik:
Wykres z zaznaczonym optymalnym k"""
import numpy as np
from matplotlib import pyplot as plt
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

for k, score in zip(k_range, cv_scores):
    print(f"Średnie Accuracy dla k = {k} -> {score:.4f}")


fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(k_range, cv_scores, marker='o', linewidth=2, markersize=4)
ax.set_xlabel('Liczba sasiadow (k)', fontsize=12)
ax.set_ylabel('Accuracy (CV)', fontsize=12)
ax.set_title('Dobor optymalnego k dla kNN', fontsize=14)
ax.grid(True, alpha=0.3)

best_k = list(k_range)[np.argmax(cv_scores)]
best_score = max(cv_scores)
ax.axvline(x=best_k, color='red', linestyle='--', alpha=0.7)

ax.annotate(f'Najlepsze k={best_k}\naccuracy={best_score:.3f}',
xy=(best_k, best_score), xytext=(best_k + 3, best_score - 0.02),
arrowprops=dict(arrowstyle='->', color='red'),
fontsize=11, color='red')
plt.tight_layout()
plt.show()