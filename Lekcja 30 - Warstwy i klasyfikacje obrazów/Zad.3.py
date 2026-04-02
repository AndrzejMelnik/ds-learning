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