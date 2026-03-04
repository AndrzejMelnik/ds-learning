"""Zadanie 8 -- Porownanie 3 algorytmow
Porownaj kNN, Decision Tree i Random Forest na datasecie Iris.
    Wymagania:
Walidacja krzyzowa (cv=5) dla kazdego
Narysuj bar chart ze srednia accuracy i odchyleniem standardowym
Wskaż najlepszy algorytm
    Oczekiwany wynik:
Wykres porownawczy z errorbar"""
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import time

iris = load_iris()
X, y = iris.data, iris.target


models = {
    'kNN (k=5)': make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
}

results_comparison = {}
for name, model in models.items():
    start = time.time()
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    elapsed = time.time() - start
    results_comparison[name] = {
        'mean': scores.mean(),
        'std': scores.std(),
        'time': elapsed
    }
    print(f"{name:>25s}: Accuracy = {scores.mean():.4f} "
          f"(+/-{scores.std(): .4f}) | Czas: {elapsed: .3f}s")

names = list(results_comparison.keys())
means = [results_comparison[n]['mean'] for n in names]
stds = [results_comparison[n]['std'] for n in names]
best_idx = np.argmax(means)

plt.figure(figsize=(10, 6))
bars = plt.bar(names, means, yerr=stds, capsize=10, color=['#2196F3', '#FF9800', '#4CAF50'], alpha=0.8)
plt.ylabel('Accuracy (CV)')
plt.title('Porównanie kNN, Decision Tree i Random Forest (Iris Dataset)')
plt.ylim(0.9, 1.0)
plt.grid(True, axis='y', alpha=0.3)
for bar, mean in zip(bars, means):
    plt.text(bar.get_x() + bar.get_width()/2, mean + 0.005, f'{mean:.4f}', ha='center', va='bottom', fontweight='bold')
plt.tight_layout()
plt.show()