"""Zadanie 8 -- Porownanie 3 algorytmow
Porownaj kNN, Decision Tree i Random Forest na datasecie Iris.
    Wymagania:
Walidacja krzyzowa (cv=5) dla kazdego
Narysuj bar chart ze srednia accuracy i odchyleniem standardowym
Wskaż najlepszy algorytm
    Oczekiwany wynik:
Wykres porownawczy z errorbar"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target


models = {
    'kNN (k=5)': make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
}
