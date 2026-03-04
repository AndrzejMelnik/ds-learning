"""Przetestuj wartosci k od 1 do 20 na datasecie Iris z walidacja krzyzowa (cv=5).
    Wymagania:
Oblicz srednia accuracy dla kazdego k
Narysuj wykres accuracy vs k
Wskaż optymalna wartosc k

    Oczekiwany wynik:
Wykres z zaznaczonym optymalnym k"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)