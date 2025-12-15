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