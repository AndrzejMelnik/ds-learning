"""Zbuduj model z bottleneck (Conv2D 1x1 do redukcji kanalow) i bez. Porownaj parametry.
Wymagania:
Wejscie: (14, 14, 128)
Bez bottleneck: Conv2D(256, 3x3)
Z bottleneck: Conv2D(32, 1x1) -- Conv2D(32, 3x3) -- Conv2D(256, 1x1)
Porownaj parametry"""

from tensorflow import keras
from tensorflow.keras import layers

input_shape = (14, 14, 128)

model_direct = keras.Sequential([
    layers.Input(shape=input_shape),
    layers.Conv2D(256, (3, 3), padding='same', activation='relu')
], name="Model_Bez_Bottleneck")

model_bottleneck = keras.Sequential([
    layers.Input(shape=input_shape),
    # Redukcja kanałów (bottleneck): 128 --> 32
    layers.Conv2D(32, (1, 1), activation='relu'),
    # Konwolucja na mniejszej liczbie kanałów
    layers.Conv2D(32, (3, 3), padding='same', activation='relu'),
    # Ekspansja kanałów: 32 --> 256
    layers.Conv2D(256, (1, 1), activation='relu')
], name="Model_Z_Bottleneck")