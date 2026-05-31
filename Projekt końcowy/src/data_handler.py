import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class HoneyDataHandler:
    def __init__(self, file_path="data/raw/honey_purity_dataset.csv"):
        self.file_path = file_path
        self.scaler = StandardScaler()

    def load_and_prepare(self):
        # 1. Wczytanie danych
        df = pd.read_csv(self.file_path)

        #Tworzenie celu (targetu)
        df['target'] = (df['Purity'] > 0.9).astype(int)

        #Separacja cech (usuwamy kolumny docelowe i Price)
        X = df.drop(columns=['Purity', 'Price', 'target'])
        y = df['target']

        #ROZWIĄZANIE BŁĘDU: One-Hot Encoding
        # Zamienia kolumny tekstowe (jak 'Blueberry') na kolumny numeryczne 0/1
        X = pd.get_dummies(X, drop_first=True)

        feature_names = X.columns.tolist()

        #Podział na zbiory
        X_train, X_test, y_train, y_test = train_test_split(
            X.values.astype('float32'),
            y.values.astype('float32'),
            test_size=0.2,
            random_state=42,
            stratify=y
        )
        return (X_train, X_test, y_train, y_test), feature_names

    def scale_data(self, X_train, X_test):
        #Standaryzacja tylko na danych treningowych
        X_train_sc = self.scaler.fit_transform(X_train)
        X_test_sc = self.scaler.transform(X_test)
        return X_train_sc, X_test_sc