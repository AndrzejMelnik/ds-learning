""" Stwórz nową kolumnę Family_Size w Titanic jako sumę SibSp + Parch + 1 (sam
pasażer).
Dataset: Titanic

Wymagania:
Oblicz Family_Size
Oblicz survival rate według rozmiaru rodziny
Zidentyfikuj, który rozmiar rodziny miał najwyższy survival rate

Oczekiwany rezultat:
Tabela z survival rate według Family_Size
Wykres słupkowy """
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import legend

titanic_data = pd.read_csv('titanic.csv')

titanic_feat = titanic_data.copy()
titanic_feat['Family_Size'] = titanic_feat['SibSp'] + titanic_feat['Parch'] + 1

surv_rate = titanic_feat.groupby('Family_Size')['Survived'].mean()
print(surv_rate)

titanic_feat['Survived_Rating'] = (
    surv_rate
)

print(titanic_feat.head())

family_size_surv_rate = surv_rate.sort_values(ascending=False)
table = pd.DataFrame({"Family_Size": family_size_surv_rate.index,
                      "Survived_Rating": family_size_surv_rate.values
                      })

print(table.head(10))

count, ax = plt.subplots()
sns.barplot(data=table, x= 'Family_Size',y= 'Survived_Rating',
            palette='viridis',hue='Family_Size', legend=False, ax=ax)


plt.show()