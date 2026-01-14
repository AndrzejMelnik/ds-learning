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

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def srednia(self):
        suma = 0
        for note in self.oceny:
            suma += note
        score = round(suma / len(self.oceny),2)
        return score