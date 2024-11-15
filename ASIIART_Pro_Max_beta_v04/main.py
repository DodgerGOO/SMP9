from .classes.ASCIIArtApp import ASCIIArtApp

def main():
    """
    Точка входу для лабораторної роботи №4
    """
    print("Лабораторна робота 4: Розробка ASCII ART генератора для візуалізації 2D-фігур ")
    app = ASCIIArtApp()
    app.run()
    
if __name__ == "__main__":
    main()