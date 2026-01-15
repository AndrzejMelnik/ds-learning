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

    def __str__(self):
        return f"{self.imie} oceny: {self.oceny}"


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
        best_avg = mean(best_uczen.oceny)
        for uczen in self.uczniowie:
            avg = mean(uczen.oceny)
            if avg > best_avg:
                best_uczen = uczen
                best_avg = avg
        avg = mean(best_uczen.oceny)
        print(best_uczen, best_avg)

uczen_1 = Uczen("Andrzej", [3, 4, 5, 5,])
uczen_2 = Uczen("Gosia", [5, 5, 5, 4])
uczen_3 = Uczen("Franek", [3, 3, 4, 4])
uczen_4 = Uczen("Jola", [4, 4, 4, 6])
uczen_5 = Uczen("Maria", [3, 4, 4, 5])



moja_klasa = Klasa("7b", [uczen_1, uczen_2, uczen_3,
                          uczen_4,uczen_5])
moja_klasa.dodaj_ucznia(Uczen("Basia", [1, 1, 5, 5]))
moja_klasa.najlepszy_uczen()

print(moja_klasa.srednia_klasy())


