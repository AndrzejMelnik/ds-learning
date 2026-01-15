"""Zadanie 11 – System ocen uczniów
Stwórz klasy:

Uczen (imie, oceny=[])
Klasa (nazwa, uczniowie=[])

Metody Klasa :

dodaj_ucznia(uczen)
srednia_klasy() – średnia ocen wszystkich uczniów
najlepszy_uczen() – zwraca ucznia z najwyższą średnią """



class Uczen:
    def __init__(self, imie, oceny=[]):
        self.imie = imie
        self.oceny = oceny




class Klasa:
    def __init__(self, nazwa, uczniowie=[]):
        self.nazwa = nazwa
        self.uczniowie = uczniowie