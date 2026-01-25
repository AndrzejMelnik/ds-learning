""" Stwórz nową kolumnę Family_Size w Titanic jako sumę SibSp + Parch + 1 (sam
pasażer).
Dataset: Titanic

Wymagania:
Oblicz Family_Size
Oblicz survival rate według rozmiaru rodziny
Zidentyfikuj, który rozmiar rodziny miał najwyższy survival rate

Oczekiwany rezultat:
Tabela z survival rate według Family_Size
Wykres słupkowy """

import pandas as pd
titanic_data = pd.read_csv('titanic.csv')

titanic_feat = titanic_data.copy()