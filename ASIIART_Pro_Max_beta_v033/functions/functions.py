import pyfiglet
import re
from colorama import Fore

def validate_latin_input(text):
    """Перевірка, чи містить введений текст тільки латинські символи."""
    if re.match("^[A-Za-z0-9 ]+$", text):
        return True
    print("Помилка: Текст має містити тільки латинські символи та цифри.")
    return False

def validate_custom_char(char):
    """Перевірка, чи введений символ не містить кирилицю."""
    if re.match("^[^\u0400-\u04FF]+$", char):  # Регулярний вираз, що виключає кирилицю
        return True
    print("Помилка: Символ не має містити кириличні символи.")
    return False

def font_selection(fonts):
    page_size = 10
    current_page = 0
    total_pages = len(fonts) // page_size + (1 if len(fonts) % page_size else 0)

    while True:
        print(f"\nСторінка {current_page + 1}/{total_pages}")
        start_index = current_page * page_size
        end_index = min(start_index + page_size, len(fonts))

        for index, font in enumerate(fonts[start_index:end_index], start=start_index + 1):
            print(f"{index}. {font}")

        user_action = input("\nВведіть номер шрифту (від 1 до 549), або '>' для наступної сторінки, '<' для попередньої, або 'приклад [номер]' для перегляду прикладу: ")

        if user_action == '>':
            if current_page < total_pages - 1:
                current_page += 1
            else:
                print("Ви на останній сторінці.")
        elif user_action == '<':
            if current_page > 0:
                current_page -= 1
            else:
                print("Ви на першій сторінці.")
        elif user_action.startswith("приклад"):
            try:
                font_index = int(user_action.split()[1]) - 1
                if 0 <= font_index < len(fonts):
                    print(f"\nПриклад шрифту '{fonts[font_index]}':")
                    print(pyfiglet.figlet_format("Example", font=fonts[font_index]))
                else:
                    print("Неправильний номер шрифту.")
            except (IndexError, ValueError):
                print("Неправильний формат команди.")
        else:
            try:
                font_choice = int(user_action) - 1
                if 0 <= font_choice < len(fonts):
                    return fonts[font_choice]
                else:
                    print("Помилка: Виберіть правильний номер шрифту.")
            except ValueError:
                print("Помилка: Введіть число або команду.")

def get_available_fonts():
    return pyfiglet.FigletFont.getFonts()

def get_validated_text():
    while True:
        text = input("Введіть слово або фразу для генерації ASCII-арту (латиницею): ")
        if validate_latin_input(text):
            return text

def get_validated_custom_char():
    while True:
        custom_char = input("Введіть символ для ASCII-арту (або натисніть Enter для використання '#'): ")
        if not custom_char:
            return '#'
        if validate_custom_char(custom_char):
            return custom_char

def get_width():
    default_width = 80
    while True:
        width_input = input(f"Введіть ширину ASCII-арту (за замовчуванням {default_width}): ")
        if not width_input:
            return default_width
        try:
            return int(width_input)
        except ValueError:
            print("Помилка: Введіть число для ширини.")

def get_color_choice(colors):
    print("Доступні кольори:")
    print("1. Червоний")
    print("2. Синій")
    print("3. Зелений")
    print("4. Білий")
    print("5. Жовтий")
    
    while True:
        try:
            color_choice = int(input("Виберіть номер кольору: "))
            if 1 <= color_choice <= 5:
                return colors.get(color_choice, Fore.WHITE)
            else:
                print("Помилка: Виберіть номер кольору від 1 до 5.")
        except ValueError:
            print("Помилка: Введіть число.")

def get_save_choice():
    while True:
        save_choice = input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").strip().lower()
        if save_choice in ["так", "ні"]:
            return save_choice
        print("Помилка: Введіть 'так' або 'ні'.")
