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
from tqdm import keras

class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

x_val, y_val = x_train[-10000:], y_train[-10000:]
x_train, y_train = x_train[:-10000], y_train[:-10000]