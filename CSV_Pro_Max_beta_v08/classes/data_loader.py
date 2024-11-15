import pandas as pd
import os

class DataLoader:
    def __init__(self, filepath=None):
        # Абсолютний шлях до файлу за замовчуванням
        if filepath is None:
            filepath = r"C:\Users\Vlad\Desktop\унік\пітоній\All_Super_Ultra_Pro_Max_beta_v09\CSV_Pro_Max_beta_v08\data.csv"
        self.filepath = filepath

    def load_data(self):
        """
        Завантаження даних з CSV-файлу.
        """
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Файл не знайдено: {self.filepath}")

        try:
            data = pd.read_csv(self.filepath)
            print(f"Дані успішно завантажено з {self.filepath}.")
            return data
        except Exception as e:
            print(f"Помилка під час завантаження даних: {e}")
            raise
