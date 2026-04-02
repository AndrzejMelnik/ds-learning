"""Zadanie 3 -- SeparableConv2D vs Conv2D
Zbuduj dwa modele (Conv2D vs SeparableConv2D) o identycznej architekturze. Porownaj
liczbe parametrow. O ile SeparableConv2D jest mniejszy?
    Wymagania:
Identyczna architektura (3 bloki)
count_params() dla obu
Oblicz recznie parametry jednej warstwy"""

from tensorflow import keras
from tensorflow.keras import layers

def build_model(conv_type='standard'):
    model = keras.Sequential(name=f"Model_{conv_type}")
    model.add(layers.Input(shape=(32, 32, 3)))

    if conv_type == 'standard':
        conv_layer = layers.Conv2D
    else:
        conv_layer = layers.SeparableConv2D


    model.add(conv_layer(32, (3, 3), padding='same', activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))


    model.add(conv_layer(64, (3, 3), padding='same', activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(conv_layer(128, (3, 3), padding='same', activation='relu'))
    model.add(layers.GlobalAveragePooling2D())  # Redukcja parametrów klasyfikatora

    model.add(layers.Dense(10, activation='softmax'))
    return model

model_std = build_model(conv_type='standard')
model_sep = build_model(conv_type='separable')

