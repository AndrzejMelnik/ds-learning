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
from tensorflow.keras.callbacks import EarlyStopping

max_features = 10000
maxlen = 200
embed_dim = 100
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

emb_scratch = layers.Embedding(max_features, embed_dim, trainable=True)
model_scratch = build_lstm_model(emb_scratch, "LSTM_Scratch")

emb_frozen = layers.Embedding(
    max_features, embed_dim,
    embeddings_initializer=keras.initializers.Constant(embedding_matrix),
    trainable=False
)
model_frozen = build_lstm_model(emb_frozen, "LSTM_GloVe_Frozen")

emb_unfrozen = layers.Embedding(
    max_features, embed_dim,
    embeddings_initializer=keras.initializers.Constant(embedding_matrix),
    trainable=True
)
model_unfrozen = build_lstm_model(emb_unfrozen, "LSTM_GloVe_Unfrozen")

callback = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

print(f"\nRozpoczynanie treningu modelu: {model_scratch.name}")
history = model_scratch.fit(
    x_train, y_train,
    epochs=10,
    batch_size=128,
    validation_split=0.2,
    callbacks=[callback],
    verbose=1
)

loss, acc = model_scratch.evaluate(x_test, y_test, verbose=0)
print(f"\nWynik {model_scratch.name} -> Accuracy: {acc:.4f}")