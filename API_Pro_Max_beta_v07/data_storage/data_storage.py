import json

class DataStorage:
    def save(self, data):
        try:
            with open(r"C:\Users\Vlad\Desktop\унік\пітоній\All_Super_Ultra_Pro_Max_beta_v09\API_Pro_Max_beta_v07\data.json", 'w') as json_file:
                json.dump(data, json_file, indent=4)  # Записуємо дані у JSON форматі
            print("Дані успішно збережено у файл data.json.")
        except Exception as e:
            print(f"Помилка при збереженні даних: {e}")
