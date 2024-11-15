import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from .classes.ASCIIArtApp import ASCIIArtApp

def main():
    """
    Точка входу для лабораторної роботи №5
    """
    print("Лабораторна робота 5: Розробка ASCII ART генератора для візуалізації 2D-фігур")
    app = ASCIIArtApp()
    app.run()
    
if __name__ == "__main__":
     main()
