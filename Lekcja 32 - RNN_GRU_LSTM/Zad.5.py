"""Zadanie 5 -- Padding i dlugosc sekwencji
    Zbadaj wplyw maxlen na accuracy: wytrenuj ten sam model LSTM
    z maxlen = 50, 100, 200,
    500. Jak dlugosc wplywa na wyniki i czas?
    Dataset: keras.datasets.imdb
    Wymagania:
4 eksperymenty z roznym maxlen
Tabela: maxlen, accuracy, czas treningu
Interpretacja"""
import pandas as pd
from matplotlib import pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
import time
from tensorflow.keras.callbacks import EarlyStopping

max_features = 10000
maxlen_values = [2,3,4,5]
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

    _, test_acc = model.evaluate(x_test, y_test, verbose=0)

    results.append({
        'maxlen': ml,
        'accuracy': round(test_acc, 4),
        'czas_treningu_s': round(elapsed_time, 2)
    })
    print(f"Wynik dla {ml}: Accuracy = {test_acc:.4f}, Czas = {elapsed_time:.2f}s")

df_results = pd.DataFrame(results)
print(df_results)

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Długość sekwencji (maxlen)')
ax1.set_ylabel('Accuracy', color='tab:blue')
ax1.plot(df_results['maxlen'], df_results['accuracy'], color='tab:blue', marker='o', label='Accuracy')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Czas treningu (s)', color='tab:red')
ax2.plot(df_results['maxlen'], df_results['czas_treningu_s'], color='tab:red', marker='s', label='Czas')
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title('Wpływ maxlen na wyniki modelu LSTM')
plt.grid(True, alpha=0.3)
plt.show()