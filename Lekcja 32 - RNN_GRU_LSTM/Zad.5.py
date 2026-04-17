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
from tensorflow.keras import layers
import time
from tensorflow.keras.callbacks import EarlyStopping

max_features = 10000
maxlen_values = [2-5]
results = []

(x_train_raw, y_train),(x_test_raw, y_test) = keras.datasets.imdb.load_data(num_words=max_features)

for ml in maxlen_values:
    print(f"\n--- Testowanie maxlen = {ml} ---")
    x_train = keras.preprocessing.sequence.pad_sequences(x_train_raw, maxlen=ml)
    x_test = keras.preprocessing.sequence.pad_sequences(x_test_raw, maxlen=ml)
    model = keras.Sequential([
        layers.Embedding(max_features, 64),
        layers.LSTM(64, dropout=0.2),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

start_time = time.time()

history = model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=128,
    validation_split=0.2,
    callbacks=[EarlyStopping(patience=2, restore_best_weights=True)],
    verbose=0
)
elapsed_time = time.time() - start_time