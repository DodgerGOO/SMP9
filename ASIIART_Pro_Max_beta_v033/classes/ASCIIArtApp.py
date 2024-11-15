from colorama import Fore

from .ASCIIArt import ASCIIArt
from ASIIART_Pro_Max_beta_v033.functions.functions import get_available_fonts, font_selection, get_validated_text, get_validated_custom_char, get_width, get_color_choice, get_save_choice


class ASCIIArtApp:
    def __init__(self):
        self.colors = {
            1: Fore.RED,
            2: Fore.BLUE,
            3: Fore.GREEN,
            4: Fore.WHITE,
            5: Fore.YELLOW
        }

    def get_font_choice(self):
        fonts = get_available_fonts()
        return font_selection(fonts)

    def get_user_input(self):
        # Завдання 1: Введення користувача
        text = get_validated_text()

        # Завдання 2: Вибір шрифту
        print("Доступні шрифти:")
        selected_font = self.get_font_choice()

        # Завдання 8: Вибір символів
        custom_char = get_validated_custom_char()

        # Завдання 7: Розмір ARTу
        width = get_width()

        # Завдання 4: Колір тексту
        color = get_color_choice(self.colors)

        return ASCIIArt(text, selected_font, color, width, custom_char)

    def run(self):
        art = self.get_user_input()

        # Завдання 5: Форматування виводу
        print(art.generate_art())

        # Завдання 6: Збереження у файл
        save_choice = get_save_choice()
        if save_choice == "так":
            file_path = r"C:\Users\Vlad\Desktop\унік\пітоній\All_Super_Ultra_Pro_Max_beta_v09\ASIIART_Pro_Max_beta_v033\art.txt"
            art.save_to_file(file_path)

        # Завдання 9: Попередній перегляд
        art.preview()
