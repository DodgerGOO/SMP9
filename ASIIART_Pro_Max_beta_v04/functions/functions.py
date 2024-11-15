from ASIIART_Pro_Max_beta_v04.AppSettings.AppSettings import COLORS

def get_available_fonts():
    """Повертає список доступних шрифтів для ASCII-арту."""
    return ["basic", "block", "slant"]

def preview_font_example(font):
    """Показує приклад шрифту."""
    examples = {
    "basic": "Example:\n  ###  \n #   # \n ##### \n #   # \n #   # \n",
    "block": "Example:\n  ███  \n █   █ \n █████ \n █   █ \n █   █ \n",
    "slant": "Example:\n    /\\   \n   /  \\  \n  /____\\ \n /      \\ \n/        \\\n"
    }
    return examples.get(font, "Приклад не знайдено.")

def validate_latin_input(text):
    """Перевірка, чи містить введений текст тільки латинські символи."""
    for char in text:
        # Перевіряємо, чи символ є латинським символом або цифрою
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9') or char.isspace()):
            print("Помилка: Текст має містити тільки латинські символи та цифри.")
            return False
    return True

def font_selection(fonts):
    print("Доступні шрифти:")
    for i, font in enumerate(fonts):
        print(f"{i + 1}. {font}")
    while True:
        choice = input("Виберіть шрифт: ")
        try:
            selected_font = fonts[int(choice) - 1]
            print(f"Приклад шрифту:\n{preview_font_example(selected_font)}")
            return selected_font
        except (IndexError, ValueError):
            print("Помилка: Виберіть правильний номер шрифту.")

def get_validated_text():
    while True:
        text = input("Введіть слово або фразу для генерації ASCII-арту (латиницею): ")
        if validate_latin_input(text):
            return text
        
def validate_custom_char(char):
    """Перевірка, чи введений символ не містить кирилицю."""
    # Тут ми можемо перевірити, чи символ не є кириличним.
    if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
        print("Помилка: Символ не має містити кириличні символи.")
        return False
    return True

def get_validated_custom_char():
    """Отримує і перевіряє символ для ASCII-арту."""
    while True:
        custom_char = input("Введіть символ для ASCII-арту, або натисніть Enter для використання # (працює тільки з шрифтами basic та block): ")
        
        if not custom_char:  # Якщо нічого не введено, використати '#'
           
            return '#'
        
        if len(custom_char) != 1:  # Перевіряємо, що введено лише один символ
            print("Помилка: Ви повинні ввести рівно один символ.")
            continue
        
        if validate_custom_char(custom_char):  # Перевіряємо введений символ
            return custom_char

        
def get_width():
    """Отримує ширину для ASCII-арту, або повертає значення за замовчуванням."""
    default_width = 80  # Значення за замовчуванням
    while True:
        width_input = input(f"Введіть ширину ASCII-арту (за замовчуванням {default_width}): ")
        if not width_input:  # Якщо нічого не введено, використати значення за замовчуванням
            return default_width
        try:
            width = int(width_input)  # Спробуйте перетворити на число
            if width > 0:  # Переконайтесь, що ширина більше нуля
                return width
            else:
                print("Помилка: Введіть число більше нуля.")
        except ValueError:
            print("Помилка: Введіть число для ширини.")
            
def get_color_choice(colors):
    while True:
        print("Виберіть колір:")
        for num, color in colors.items():
            print(f"{num}: {color}")

        try:
            color_choice = int(input("Введіть номер кольору: "))
            if color_choice in colors:
                return colors[color_choice]
            else:
                print("Помилка: Виберіть номер кольору з наявних.")
        except ValueError:
            print("Помилка: Введіть число.")
            
def get_save_choice():
    """Запитує у користувача, чи хоче він зберегти ASCII-арт у файл."""
    while True:
        save_choice = input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").strip().lower()
        if save_choice in ["так", "ні"]:
            return save_choice
        print("Помилка: Введіть 'так' або 'ні'.")



