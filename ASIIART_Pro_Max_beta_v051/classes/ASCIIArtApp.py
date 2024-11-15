from ASIIART_Pro_Max_beta_v051.functions.functions import get_shape_type, get_color_choice, get_validated_custom_char, get_save_choice
# Словник з 2D та 3D ASCII фігурами
shapes = {
    'cube': {
        '3D': [
            "    +------+ ",
            "   /      /| ",
            "  /      / | ",
            " +------+  + ",
            " |      | /  ",
            " |      |/   ",
            " +------+    "
        ],
        '2D': [
            " +------+ ",
            " |      | ",
            " |      | ",
            " +------+ "
        ]
    },
    'pyramid': {
        '3D': [
            "     /\\     ",
            "    /  \\    ",
            "   /____\\   ",
            "  /|    |\\  ",
            " /_|____|_\\ "
        ],
        '2D': [
            "   /\\   ",
            "  /  \\  ",
            " /____\\ "
        ]
    }
}

class ASCIIArtApp:
    def __init__(self):
        self.colors = {
            1: 'Червоний',
            2: 'Синій',
            3: 'Зелений',
            4: 'Білий',
            5: 'Жовтий'
        }

    def get_user_input(self):
        shape_name = get_shape_type()  # Отримати тип фігури
       
        # Цикл для отримання розміру фігури (2D або 3D)
        while True:
            dimension_choice = input("Введіть '1' для 3D або '2' для 2D: ")
            if dimension_choice == '1':
                is_3d = True
                break
            elif dimension_choice == '2':
                is_3d = False
                break
            else:
                print("Невірний вибір. Будь ласка, спробуйте ще раз.")

        color_choice = get_color_choice(self.colors)  # Отримати вибір кольору
        symbol = get_validated_custom_char()  # Отримати символ

        return shape_name, is_3d, color_choice, symbol

    def get_ansi_color(self, color):
        color_codes = {
            "Червоний": "\033[91m",
            "Синій": "\033[94m",
            "Зелений": "\033[92m",
            "Білий": "\033[97m",
            "Жовтий": "\033[93m",
        }
        return color_codes.get(color, "\033[97m")  # За замовчуванням білий

    def display_shape(self, shape_name, is_3d, color, symbol):
        ansi_color = self.get_ansi_color(color)  # Отримуємо ANSI-код кольору
        reset_color = "\033[0m"  # Код для скидання кольору
        shape_type = '3D' if is_3d else '2D'
        shape = shapes[shape_name][shape_type]

        art_lines = []  # Список для зберігання рядків ASCII-арту

        for line in shape:
            # Заміна символу на вибраний символ
            colored_line = line.replace('+', symbol).replace('/', symbol).replace('\\', symbol).replace('|', symbol).replace('-', symbol).replace('_', symbol)
            art_lines.append(f"{ansi_color}{colored_line}{reset_color}")  # Додаємо кольоровий рядок до списку
            print(art_lines[-1])  # Виводимо останній рядок

        return art_lines  # Повертаємо список рядків ASCII-арту

    def save_to_file(self, file_path, shape_name, is_3d, symbol):
        shape_type = '3D' if is_3d else '2D'
        shape = shapes[shape_name][shape_type]

        with open(file_path, 'w', encoding='utf-8') as f:
            for line in shape:
                # Заміна символів у рядку на вибраний символ без кольору
                saved_line = line.replace('+', symbol).replace('/', symbol).replace('\\', symbol).replace('|', symbol).replace('-', symbol).replace('_', symbol)
                f.write(saved_line + '\n')  # Запис рядка без кольорових кодів

    def run(self):
        shape_name, is_3d, color_choice, symbol = self.get_user_input()

        # Відображення фігури
        art_lines = self.display_shape(shape_name, is_3d, color_choice, symbol)

        save_choice = get_save_choice()
        if save_choice.lower() == "так":
            file_path = r"C:\\Users\\Vlad\\Desktop\\унік\\пітоній\\ASIIART_Pro_Max_beta_v05.1\\art.txt"
            self.save_to_file(file_path, shape_name, is_3d, symbol)  # Зберігаємо файл
            print(f"ASCII-арт збережено у файл {file_path}")
