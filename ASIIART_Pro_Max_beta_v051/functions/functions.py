from ASIIART_Pro_Max_beta_v051.AppSettings.AppSettings import COLORS

def get_shape_type():
    shapes = ["cube", "pyramid"]
    print("Доступні фігури:")
    for i, shape in enumerate(shapes, 1):
        print(f"{i}. {shape}")
    while True:
        choice = input("Виберіть фігуру: ")
        try:
            return shapes[int(choice) - 1]
        except (IndexError, ValueError):
            print("Помилка: Виберіть правильний номер фігури.")

def get_shape_dimension():
    while True:
        dimension = input("Якщо 3D - введіть 1, якщо 2D - введіть 2,: ").strip().lower()
        if dimension in ['1', '2']:
            return dimension
        print("Неправильний ввід. Спробуйте ще раз.")

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

def get_validated_custom_char():
    while True:
        custom_char = input("Введіть символ для ASCII-арту (Enter для використання #): ")
        if not custom_char:
            return '#'
        if len(custom_char) == 1:
            return custom_char
        print("Помилка: Ви повинні ввести рівно один символ.")

def get_save_choice():
    while True:
        save_choice = input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").strip().lower()
        if save_choice in ["так", "ні"]:
            return save_choice
        print("Помилка: Введіть 'так' або 'ні'.")
        
      



