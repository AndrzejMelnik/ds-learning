
"""Zadanie 2 – Pierwszy model
Stwórz model Student z polami: id (Integer, primary key), name (String 100), age
(Integer), email (String 150, unique). Utwórz tabelę w bazie.
Wymagania:
(proste)
Definicja modelu
Base.metadata.create_all()
Sprawdzenie struktury tabeli"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import inspect

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    email = Column(String(150), unique=True)

engine = create_engine('sqlite:///products.db', echo=False)

Base.metadata.create_all(engine)
print("Tabela 'students' została utworzona")

inspector = inspect(engine)
print("Tabele w bazie:", inspector.get_table_names())
print("Kolumny w 'students':", [col['name'] for col in
inspector.get_columns('students')])

