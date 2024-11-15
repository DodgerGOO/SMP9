import pyfiglet
from colorama import Fore
from common.logger import Logger
from common.validation import Validation

logger = Logger()

class ASCIIArt:
    """
    Клас для створення ASCII-арту із заданого тексту.
    """
    def __init__(self, text, font="standard"):
        """
        Ініціалізує об'єкт ASCII-арту із текстом і шрифтом.

        :param text: Текст, який потрібно перетворити в ASCII-арт
        :param font: Шрифт для генерації ASCII-арту (за замовчуванням "standard")
        """
        # Валідація тексту для перевірки його непорожнього значення
        self.text = Validation.validate_non_empty_string(text)
        self.font = font  # Встановлення шрифту

    def generate_art(self):
        self.ascii_art = pyfiglet.figlet_format(self.text, font=self.font, width=self.width)
        self._apply_custom_characters()
        return self.color + self.ascii_art + Fore.RESET

    def _apply_custom_characters(self):
        self.ascii_art = self.ascii_art.replace('@', self.custom_char)
        self.ascii_art = self.ascii_art.replace('#', self.custom_char)
        
    def generate(self):
        """
        Генерує ASCII-арт із заданого тексту та шрифту.

        :return: ASCII-арт у вигляді рядка
        """
        try:
            import pyfiglet  # Бібліотека для генерації ASCII-арту
            # Форматування тексту у вигляді ASCII-арту
            ascii_art = pyfiglet.figlet_format(self.text, font=self.font)
            # Логування успішної генерації
            logger.log_info(f"ASCII-арт створено: '{self.text}' зі шрифтом '{self.font}'")
            return ascii_art  # Повертаємо результат
        except Exception as e:
            # Логування помилки генерації
            logger.log_error(f"Помилка генерації ASCII-арту: {e}")
            raise

    def preview(self):
        print("Попередній перегляд ASCII-арту:")
        print(self.generate_art())

    def save_to_file(self, file_path):
        with open(file_path, "w") as f:
            f.write(self.ascii_art)
        print(f"ASCII-арт збережено у файл {file_path}")