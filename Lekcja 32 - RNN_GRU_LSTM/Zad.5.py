"""Zadanie 5 -- Padding i dlugosc sekwencji
    Zbadaj wplyw maxlen na accuracy: wytrenuj ten sam model LSTM
    z maxlen = 50, 100, 200,
    500. Jak dlugosc wplywa na wyniki i czas?
    Dataset: keras.datasets.imdb
    Wymagania:
4 eksperymenty z roznym maxlen
Tabela: maxlen, accuracy, czas treningu
Interpretacja"""

from tensorflow import keras

max_features = 10000
maxlen_values = [2-5]
results = []

(x_train_raw, y_train),(x_test_raw, y_test) = keras.datasets.imdb.load_data(num_words=max_features)
