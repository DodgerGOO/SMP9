import math
     
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

def calculate(num1, num2, operator):
  
    try:
        operations = {
            '+': lambda: num1 + num2,
            '-': lambda: num1 - num2,
            '*': lambda: num1 * num2,
            '/': lambda: num1 / num2 if num2 != 0 else None,
            '%': lambda: num1 % num2,
            '^': lambda: num1 ** num2,
            '√': lambda: math.sqrt(num1) if num1 >= 0 else None,
            
        }
        return operations.get(operator, lambda: None)()
    except (ZeroDivisionError, ValueError) as e:
        print(f"Помилка: {e}")
        
    
         
    return None
