from matplotlib import pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping

max_features = 5000
maxlen = 100

(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=max_features)
x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = keras.preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)

model_lstm = keras.Sequential([
    layers.Embedding(input_dim=max_features, output_dim=64),
    layers.LSTM(64, dropout=0.2),
    layers.Dense(1, activation='sigmoid')
], name="Model_LSTM")

model_lstm.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
history = model_lstm.fit(
    x_train, y_train,
    epochs=10,
    batch_size=128,
    validation_split=0.2,
    callbacks=[EarlyStopping(patience=3, restore_best_weights=True)],
    verbose=1
)
test_loss, test_acc = model_lstm.evaluate(x_test, y_test, verbose=0)
print(f"\nAccuracy modelu LSTM: {test_acc:.4f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(history.history['loss'], label='Train Loss')
ax1.plot(history.history['val_loss'], label='Val Loss')
ax1.set_title('Krzywa Straty (Loss)')
ax1.legend()

ax2.plot(history.history['accuracy'], label='Train Acc')
ax2.plot(history.history['val_accuracy'], label='Val Acc')
ax2.set_title('Krzywa Dokładności (Accuracy)')
ax2.legend()

plt.tight_layout()
plt.show()Wy