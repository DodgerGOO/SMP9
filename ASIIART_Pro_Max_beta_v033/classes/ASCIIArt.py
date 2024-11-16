import pyfiglet
from colorama import Fore

class ASCIIArt:
    def __init__(self, text, font="standard", color=Fore.WHITE, width=80, custom_char="#"):
        self.text = text
        self.font = font
        self.color = color
        self.width = width
        self.custom_char = custom_char
        self.ascii_art = ""

    def generate_art(self):
        self.ascii_art = pyfiglet.figlet_format(self.text, font=self.font, width=self.width)
        self._apply_custom_characters()
        return self.color + self.ascii_art + Fore.RESET

    def _apply_custom_characters(self):
        self.ascii_art = self.ascii_art.replace('@', self.custom_char)
        self.ascii_art = self.ascii_art.replace('#', self.custom_char)

    def preview(self):
        print("Попередній перегляд ASCII-арту:")
        print(self.generate_art())

    def save_to_file(self, file_path):
        with open(file_path, "w") as f:
            f.write(self.ascii_art)
        print(f"ASCII-арт збережено у файл {file_path}")