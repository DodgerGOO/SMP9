from .ASCIIArt import ASCIIArt 
from ASIIART_Pro_Max_beta_v04.functions.functions import get_available_fonts, font_selection, get_validated_text, get_validated_custom_char, get_width, get_color_choice, get_save_choice

class ASCIIArtApp:
    def __init__(self):
        self.colors = {
            1: 'Червоний',
            2: 'Синій',
            3: 'Зелений',
            4: 'Білий',
            5: 'Жовтий'
        }

    def get_font_choice(self):
        fonts = get_available_fonts()
        return font_selection(fonts)

    def get_user_input(self):
        text = get_validated_text()

        print("Доступні шрифти:")
        selected_font = self.get_font_choice()

        custom_char = get_validated_custom_char()

        width = get_width()

        # Вибір кольору
        color = get_color_choice(self.colors)

        # Повертаємо об'єкт ASCIIArt
        return ASCIIArt(text, selected_font, color, width, custom_char)

    def run(self):
        # Виклик методу для отримання введених даних
        art = self.get_user_input()

        # Генерація та відображення арту
        print(art.generate_art())

        save_choice = get_save_choice()
        if save_choice == "так":
            file_path = r"C:\\Users\\Vlad\\Desktop\\унік\\пітоній\\All_Super_Ultra_Pro_Max_beta_v09\\ASIIART_Pro_Max_beta_v04\\art.txt"
            art.save_to_file(file_path)

        art.preview()
