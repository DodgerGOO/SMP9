import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)


from Calculator_Pro_Max_beta_v021.classes.calculator import Calculator

def main():
    """
    Точка входу для лабораторної роботи №2
    """
    print("Лабораторна робота 2: Основи побудови об’єктно-орієнтованих додатків на Python")    

    calculator = Calculator()
    calculator.run()

if __name__ == "__main__":
    main()