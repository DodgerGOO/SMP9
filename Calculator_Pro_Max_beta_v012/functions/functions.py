from Calculator_Pro_Max_beta_v012.GlobalVariables.GlobalVariables import memory, history
from Calculator_Pro_Max_beta_v012.tools.tools import save_to_memory, get_from_memory, show_history, customize
from Calculator_Pro_Max_beta_v012.AppSettings.AppSettings import decimal_places

from common.logger import Logger
from common.validation import Validation

def get_numbers():
    choice = input("Використати значення з пам'яті? (так/ні): ").lower()
    if choice == 'так':
        num1 = get_from_memory()
        if num1 is None:  
            return get_numbers() 
        print(f"Використано значення з пам'яті: {num1}")
    else:
        try:
            num1 = Validation.validate_number(input("Введіть перше число: "))
        except ValueError:
            print("Помилка: потрібно ввести дійсне число.")
            return get_numbers()

    try:
        num2 = Validation.validate_number(input("Введіть друге число: "))
        return num1, num2
    except ValueError:
        print("Помилка: потрібно ввести дійсне число.")
        return get_numbers()

def get_operator():
    operator = input("Введіть оператор (+, -, *, /, %, ^, √): ")
    if operator in ['+', '-', '*', '/', '%', '^', '√']:
        return operator
    else:
        print("Помилка: некоректний оператор.")
        return get_operator()

logger = Logger()

def calculate(num1, num2, operator):
    """
    Виконує базові арифметичні операції між двома числами.

    :param num1: Перше число
    :param num2: Друге число
    :param operator: Оператор ('+', '-', '*', '/')
    :return: Результат обчислення
    """
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль.")
            result = num1 / num2
        else:
            raise ValueError("Некоректний оператор.")

        # Логування успішного обчислення
        logger.log_info(f"Обчислення: {num1} {operator} {num2} = {result}")
        return result
    except Exception as e:
        # Логування помилки
        logger.log_error(f"Помилка: {e}")
        raise

def run_calculator():
    global memory, history, decimal_places


    while True:
        operator = get_operator()
        if operator == '√':
            choice = input("Використати значення з пам'яті? (так/ні): ").lower()
            if choice == 'так':
                num1 = get_from_memory()            
                if num1 is None:
                    continue 
            else:
                num1 = float(input("Введіть число для операції √: "))
            num2 = 0 
        else:
            num1, num2 = get_numbers()

        result = calculate(num1, num2, operator)

        if result is not None:
            result = round(result, decimal_places)
            print(f"Результат: {result}")
            history.append(f"{num1} {operator} {num2} = {result}" if operator != '√' else f"√{num1} = {result}")

            save_choice = input("Зберегти результат у пам'ять? (так/ні): ").lower()
            if save_choice == 'так':
                save_to_memory(result)

        choice = input("Чи хочете виконати ще одне обчислення? (так/ні): ").lower()
        if choice != 'так':
            break

        history_choice = input("Бажаєте переглянути історію? (так/ні): ").lower()
        if history_choice == 'так':
            show_history()

        customize_choice = input("Бажаєте налаштувати калькулятор? (так/ні): ").lower()
        if customize_choice == 'так':
            customize()