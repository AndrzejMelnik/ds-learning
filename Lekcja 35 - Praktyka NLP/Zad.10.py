"""Zadanie 10 -- Pretrenowane embeddingi w LSTM
Porownaj LSTM z embeddingami:
Dataset: IMDB.
Oczekiwany wynik: porownanie 3 wariantow, analiza
(srednie)
Trenowanymi od zera
Pretrenowanymi GloVe (zamrozonymi, trainable=False)
Pretrenowanymi GloVe (odblokowanymi, trainable=True)"""

from tensorflow import keras

max_features = 10000
maxlen = 200

(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=max_features)
x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = keras.preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)

