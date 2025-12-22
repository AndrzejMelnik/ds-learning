state_sequence = ["A", "B", "A", "A", "C", "B", "C", "A", "B", "B"]

# stworzenie listy z eliminacją duplikatów
unique_list = []
for value in state_sequence:
    if value not in unique_list:
        unique_list.append(value)
print(unique_list)