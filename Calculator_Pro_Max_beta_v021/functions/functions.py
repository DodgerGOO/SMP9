import math
from common.logger import Logger

logger = Logger()   
  
def validate_input(prompt, validation_fn, error_message):
    
    while True:
        user_input = input(prompt)
        if validation_fn(user_input):
            return user_input
        print(error_message)


def get_operator():
   
    return validate_input("Введіть оператор (+, -, *, /, %, ^, √): ",
                          lambda op: op in ['+', '-', '*', '/', '%', '^', '√'],
                          "Помилка: некоректний оператор.")

def calculate(self, num1, num2, operator):
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

        logger.log_info(f"Обчислення: {num1} {operator} {num2} = {result}")
        self.history.append({"num1": num1, "num2": num2, "operator": operator, "result": result})
        return result
    except Exception as e:
        logger.log_error(f"Помилка: {e}")
        raise