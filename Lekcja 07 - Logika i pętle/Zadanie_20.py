# lista wartosci
wartosci = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#sortowanie listy i z niej utworzenie nowej listy
new_list = sorted(wartosci)

# wyswietlenie nowej listy; utworzenie min i max
print(new_list)
min = new_list[0]
max = new_list[-1]

#utworzenie listy znormalizowanej; dokonanie obliczeń
znormalizowana_lista = []
for wartosc in wartosci:
    x_norm = (wartosc - min) / (max - min)
    znormalizowana_lista.append(round(x_norm, 2))

