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

from tqdm import keras

class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()