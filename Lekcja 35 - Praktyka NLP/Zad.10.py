"""Zadanie 10 -- Pretrenowane embeddingi w LSTM
Porownaj LSTM z embeddingami:
Dataset: IMDB.
Oczekiwany wynik: porownanie 3 wariantow, analiza
(srednie)
Trenowanymi od zera
Pretrenowanymi GloVe (zamrozonymi, trainable=False)
Pretrenowanymi GloVe (odblokowanymi, trainable=True)"""

from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

max_features = 10000  # Rozmiar słownika [3]
maxlen = 200          # Dobry kompromis dla recenzji IMDB [4]
embed_dim = 100       # Standardowy wymiar dla GloVe [5]

(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=max_features)
x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = keras.preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)

def get_simulated_glove_weights(vocab_size, dim):
    return np.random.randn(vocab_size, dim) * 0.01

embedding_matrix = get_simulated_glove_weights(max_features, embed_dim)


def build_lstm_model(embedding_layer, name):
    model = keras.Sequential([
        layers.Input(shape=(maxlen,)),
        embedding_layer,
        layers.LSTM(64, dropout=0.2, recurrent_dropout=0.2),
        layers.Dense(1, activation='sigmoid')
    ], name=name)

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model