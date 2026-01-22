import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
batch_size = 100
total_processed = 0
for chunk in pd.read_csv(url, chunksize=batch_size):
    mean_age = chunk['Age'].mean()
    total_processed += 1
    print(f"Batch {total_processed}: średni wiek = {mean_age:.2f} lat")