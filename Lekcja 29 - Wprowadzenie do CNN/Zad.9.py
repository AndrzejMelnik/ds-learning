"""Zadanie 9 -- CNN na Fashion MNIST z diagnostyka
Zbuduj CNN na Fashion MNIST z 3 blokami konwolucyjnymi, wytrenuj z callbacks, narysuj
krzywe uczenia i confusion matrix. Zidentyfikuj najczesciej mylone klasy.
   Dataset: keras.datasets.fashion_mnist
   Wymagania:
3 bloki Conv+Pool z BatchNorm i Dropout
EarlyStopping + ReduceLROnPlateau
Krzywe uczenia (loss, accuracy)
Confusion matrix z nazwami klas
Analiza bledow"""
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

x_val, y_val = x_train[-10000:], y_train[-10000:]
x_train, y_train = x_train[:-10000], y_train[:-10000]

model = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),

    # Blok 1: 32 filtry
    layers.Conv2D(32, (3, 3), padding='same', activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    # Blok 2: 64 filtry
    layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    # Blok 3: 128 filtrów + GAP [6, 7]
    layers.Conv2D(128, (3, 3), padding='same', activation='relu'),
    layers.BatchNormalization(),
    layers.GlobalAveragePooling2D(),

    # Klasyfikator Dense
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])
