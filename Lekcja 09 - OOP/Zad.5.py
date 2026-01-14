"""Stwórz klasę Student z atrybutami: imie , numer_indeksu , oceny (lista ocen).

Metody:
Stwórz 3 studentów, dodaj im oceny i wyświetl średnie.

dodaj_ocene(ocena) – dodaje ocenę do listy
srednia() – zwraca średnią ocen
__str__() – reprezentacja tekstowa """

class Student:

    def __init__(self, imie, numer_indeksu,oceny):
        self.imie = imie
        self.numer_indeksu = numer_indeksu
        self.oceny = oceny