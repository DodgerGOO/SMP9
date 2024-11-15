import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)


from .classes.calculator import Calculator

def main():
    """
    Точка входу для лабораторної роботи №6
    """
    print("Лабораторна робота 6: Введення в Python")   
    calculator = Calculator()
    calculator.run()

if __name__ == "__main__":
    main()