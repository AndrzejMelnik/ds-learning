state_sequence = ["A", "B", "A", "A", "C", "B", "C", "A", "B", "B"]

# stworzenie listy z eliminacją duplikatów
unique_list = []
for value in state_sequence:
    if value not in unique_list:
        unique_list.append(value)
print(unique_list)

#tworzenie słownika sekwencji
sequences = {}

# wewnętrzny słownik dla każdego ze stanów
for starting_state in unique_list:
    sequences[starting_state] = {}
    # wszystkie przejścia ustwione z wartością zero
    for ending_state in unique_list:
        sequences[starting_state][ending_state] = 0