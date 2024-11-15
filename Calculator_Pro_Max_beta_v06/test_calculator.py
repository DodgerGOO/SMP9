import unittest
from Calculator_Pro_Max_beta_v06.classes.calculator import Calculator
from Calculator_Pro_Max_beta_v06.functions.functions import calculate
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestCalculatorOperations(unittest.TestCase):
    
    def setUp(self):
        # Ініціалізуємо калькулятор перед кожним тестом
        self.calculator = Calculator()

    # Завдання 1: Тестування Додавання
    def test_addition(self):
        result = calculate(5, 3, '+')
        self.assertEqual(result, 8, "Додавання не працює з позитивними числами")
        
        result = calculate(-5, -3, '+')
        self.assertEqual(result, -8, "Додавання не працює з від'ємними числами")

    # Завдання 2: Тестування Віднімання
    def test_subtraction(self):
        result = calculate(10, 5, '-')
        self.assertEqual(result, 5, "Віднімання не працює з позитивними числами")
        
        result = calculate(5, 10, '-')
        self.assertEqual(result, -5, "Віднімання не працює для отримання від'ємного результату")
        
        result = calculate(-5, -3, '-')
        self.assertEqual(result, -2, "Віднімання не працює з від'ємними числами")

    # Завдання 3: Тестування Множення
    def test_multiplication(self):
        result = calculate(0, 5, '*')
        self.assertEqual(result, 0, "Множення не працює з нулем")
        
        result = calculate(3, 3, '*')
        self.assertEqual(result, 9, "Множення не працює з позитивними числами")
        
        result = calculate(-3, 3, '*')
        self.assertEqual(result, -9, "Множення не працює з від'ємними числами")

    # Завдання 4: Тестування Ділення
    def test_division(self):
        result = calculate(10, 2, '/')
        self.assertEqual(result, 5, "Ділення не працює з позитивними числами")
        
        result = calculate(10, 0, '/')
        self.assertIsNone(result, "Ділення на нуль не обробляється правильно")

        result = calculate(-10, 2, '/')
        self.assertEqual(result, -5, "Ділення не працює з від'ємними числами")

    # Завдання 5: Тестування Обробки Помилок
    def test_error_handling(self):
        # Тест на неіснуючий оператор
        result = calculate(10, 2, '?')
        self.assertIsNone(result, "Некоректний оператор не обробляється правильно")
        
        # Тест ділення на нуль
        result = calculate(10, 0, '/')
        self.assertIsNone(result, "Помилка ділення на нуль не обробляється правильно")


if __name__ == '__main__':
    unittest.main()