logs = [
    "2024-01-15 10:23:45 INFO Model training started",
    "2024-01-15 10:45:12 WARNING Low memory",
    "2024-01-15 11:02:33 ERROR Training failed",
    "2024-01-15 11:05:01 INFO Retrying with smaller batch"]

#Tworzymy zmodyfikowaną z naszymi słowami kluczowymi:

keywords_from_logs = []
for keyword in logs:
    keyword = keyword.split()[2]
    keywords_from_logs.append(keyword)

print(keywords_from_logs)

#Wyświetlenie liczby wystąpień poszczególnych wyrazów

TOTAL_NUM_OF_KEYW = 4
number_of_occur_inf = keywords_from_logs.count('INFO') 
info_word = (number_of_occur_inf / TOTAL_NUM_OF_KEYW) * 100
print(f"Procentowe wystąpienie wyrazu INFO: {info_word}%")

number_of_occur_warn = keywords_from_logs.count('WARNING')
warn_word = (number_of_occur_warn / TOTAL_NUM_OF_KEYW) * 100
print(f"Procentowe wystąpienie wyrazu WARNING: {warn_word}%")

number_of_occur_err = keywords_from_logs.count('ERROR')
err_word = (number_of_occur_err / TOTAL_NUM_OF_KEYW) * 100
print(f"Procentowe wystąpienie wyrazu ERROR: {err_word}%")

