""" Zadanie 3 – Klasa BankAccount
    Stwórz klasę BankAccount z atrybutami: wlasciciel , saldo .
    Metody:
    Stwórz kilka kont i przetestuj operacje:

    wplac(kwota) – zwiększa saldo
    wyplac(kwota) – zmniejsza saldo (tylko jeśli wystarczy środków)
    pokaz_saldo() – wyświetla saldo """

class BankAccount:

    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplac(self, kwota):
        self.saldo += kwota
        print(self.saldo)