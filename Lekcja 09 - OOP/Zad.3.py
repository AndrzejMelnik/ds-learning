""" Zadanie 3 – Klasa BankAccount
    Stwórz klasę BankAccount z atrybutami: wlasciciel , saldo .
    Metody:
    Stwórz kilka kont i przetestuj operacje:

    wplac(kwota) – zwiększa saldo
    wyplac(kwota) – zmniejsza saldo (tylko jeśli wystarczy środków)
    pokaz_saldo() – wyświetla saldo """

import locale

class BankAccount:

    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplac(self, kwota):
        self.saldo += kwota
        print(self.saldo)

    def wyplac(self, kwota):
        if self.saldo - kwota >= 0:
            self.saldo -= kwota
            print(self.saldo)
        else:
            print("Kwota, którą chcesz wypłacić, przekracza twoje saldo.")
            print("Skoryguj kwotę.")

    def pokaz_saldo(self):
        amount = self.saldo

        #część kodu wyświetlająca saldo w odpowiednim formacie waluty PLN
        locale.setlocale(locale.LC_ALL, "pl_PL")
        print("Twoje saldo to: ", locale.currency(amount, grouping=True))