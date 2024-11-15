import json
import csv

class DataStorage:
    @staticmethod
    def save_to_json(data, filepath):
        """
        Зберігає дані у JSON файл.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Дані збережено у файл: {filepath}")
        except Exception as e:
            print(f"Помилка збереження у JSON: {e}")

    @staticmethod
    def load_from_json(filepath):
        """
        Завантажує дані з JSON файлу.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Помилка завантаження з JSON: {e}")
            return None

    @staticmethod
    def save_to_csv(data, filepath, fieldnames):
        """
        Зберігає дані у CSV файл.
        """
        try:
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            print(f"Дані збережено у CSV файл: {filepath}")
        except Exception as e:
            print(f"Помилка збереження у CSV: {e}")

    @staticmethod
    def load_from_csv(filepath):
        """
        Завантажує дані з CSV файлу.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except Exception as e:
            print(f"Помилка завантаження з CSV: {e}")
            return None
