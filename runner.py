import os
import subprocess
from Calculator_Pro_Max_beta_v012.main import main as run_lr1
from Calculator_Pro_Max_beta_v021.main import main as run_lr2
from ASIIART_Pro_Max_beta_v033.main import main as run_lr3
from ASIIART_Pro_Max_beta_v04.main import main as run_lr4
from ASIIART_Pro_Max_beta_v051.main import main as run_lr5
from Calculator_Pro_Max_beta_v06.main import main as run_lr6
from API_Pro_Max_beta_v07.main import main as run_lr7
from CSV_Pro_Max_beta_v08.main import main as run_lr8

class LabRunner:
    def __init__(self):
        self.labs = {
            1: run_lr1,
            2: run_lr2,
            3: run_lr3,
            4: run_lr4,
            5: run_lr5,
            6: run_lr6,
            7: run_lr7,
            8: run_lr8,
        }

    def run_lab(self, lab_number):
        try:
            if lab_number in self.labs:
                print(f"Запускаємо лабораторну роботу №{lab_number}...")
                self.labs[lab_number]()
            else:
                print("Некоректний номер лабораторної роботи.")
        except AttributeError:
            print(f"Помилка: лабораторна робота №{lab_number} не має коректної функції main.")

    def run_tests(self, lab_number):
        """
        Запуск юніт-тестів для вказаної лабораторної роботи.
        """
        test_files = {
            6: "Calculator_Pro_Max_beta_v06/test_calculator.py",
            7: "API_Pro_Max_beta_v07/tests.py",
        }
        test_file = test_files.get(lab_number)
        if not test_file:
            print(f"Для лабораторної роботи №{lab_number} тести не знайдено.")
            return

        if os.path.exists(test_file):
            print(f"Запускаємо тести для лабораторної роботи №{lab_number}...")
            subprocess.run(["python", "-m", "unittest", test_file])
        else:
            print(f"Файл з тестами не знайдено: {test_file}.")

if __name__ == "__main__":
    runner = LabRunner()
    while True:
        try:
            print("\nМеню:")
            print("1-8: Запуск лабораторної роботи")
            print("9: Запуск тестів для 6-ї лабораторної")
            print("10: Запуск тестів для 7-ї лабораторної")
            print("0: Вихід")
            choice = int(input("Введіть номер дії: "))

            if choice == 0:
                break
            elif choice == 9:
                runner.run_tests(6)
            elif choice == 10:
                runner.run_tests(7)
            elif 1 <= choice <= 8:
                runner.run_lab(choice)
            else:
                print("Некоректний вибір.")
        except ValueError:
            print("Помилка: введіть коректне число.")
