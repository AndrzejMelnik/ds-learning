"""Zadanie 11 – System ocen uczniów
Stwórz klasy:

Uczen (imie, oceny=[])
Klasa (nazwa, uczniowie=[])

Metody Klasa :

dodaj_ucznia(uczen)
srednia_klasy() – średnia ocen wszystkich uczniów
najlepszy_uczen() – zwraca ucznia z najwyższą średnią """


from statistics import mean

class Uczen:
    def __init__(self, imie, oceny=[]):
        self.imie = imie
        self.oceny = oceny




class Klasa:
    def __init__(self, nazwa, uczniowie=[]):
        self.nazwa = nazwa
        self.uczniowie = uczniowie

    def dodaj_ucznia(self, uczen):
        self.uczniowie.append(uczen)


    def srednia_klasy(self):
        wszystkie_oceny = []
        for uczen in self.uczniowie:
            wszystkie_oceny.extend(uczen.oceny)
        return round(mean(wszystkie_oceny), 2)


    def najlepszy_uczen(self):
        best_uczen = self.uczniowie[0]
        best_ocena = sum(best_uczen.oceny)
        for uczen in self.uczniowie:
            if sum(uczen.oceny) > best_ocena:
                best_uczen = uczen
        avg = mean(best_uczen.oceny)
        print(best_uczen, avg)