"Honey Purity Classification Project"

Opis projektu:
    Celem projektu jest automatyczna klasyfikacja czystości miodu na podstawie parametrów chemicznych i fizycznych. Projekt realizuje pełny proces Data Science Pipeline: od wczytania surowych danych, przez zaawansowany preprocessing i detekcję anomalii, aż po udostępnienie modelu przez interfejs API.

Kluczowe cechy:

    Detekcja anomalii: Wykorzystanie algorytmu Isolation Forest do usunięcia obserwacji odstających przed etapem trenowania.
    Optymalizacja modelu: Zastosowanie regresji logistycznej z regularyzacją ElasticNet (balans między L1 i L2), optymalizowaną za pomocą GridSearchCV.
    Reprodukowalność: Zastosowanie stałego ziarna losowości (random_state) oraz izolowanego środowiska wirtualnego

Instalacja i uruchomienie:

1. Przygotowanie środowiska
Zaleca się użycie środowiska wirtualnego .venv. Aby zainstalować wymagane biblioteki, wykonaj:
    
    pip install -r requirements.txt

2. Uruchomienie pipeline'u treningowego
Skrypt main.py wykonuje pełny cykl: wczytanie danych, czyszczenie, trening z walidacją krzyżową oraz zapis artefaktów.

    python main.py

3. Udostępnienie modelu przez API
Gdy model zostanie zapisany w folderze models/, możesz uruchomić serwer produkcyjny za pomocą uvicorn:

uvicorn api:app --reload

Po uruchomieniu interaktywna dokumentacja Swagger UI jest dostępna pod adresem: http://127.0.0.1:8000/docs.
Metryki i Ocena Modelu
Model jest oceniany za pomocą zestawu metryk klasyfikacji binarnej:

    Accuracy: Ogólna poprawność predykcji.
    F1-score: Równowaga między precyzją a czułością, kluczowa przy analizie jakości produktów spożywczych.
    ROC-AUC: Zdolność modelu do rozróżniania klas miodu.

Wszystkie wyniki oraz najważniejsze parametry modelu są automatycznie zapisywane w pliku models/metadata.json zgodnie z dobrą praktyką dokumentowania eksperymentów