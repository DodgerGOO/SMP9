class Validation:
    """
    Клас для перевірки введених даних.
    """
    @staticmethod
    def validate_number(value):
        """
        Перевірка, чи є значення числом.
        """
        try:
            return float(value)
        except ValueError:
            print("Помилка: введене значення не є числом.")
            return None

    @staticmethod
    def validate_non_empty_string(value):
        """
        Перевірка, чи є значення непорожнім рядком.
        """
        if isinstance(value, str) and value.strip():
            return value
        print("Помилка: рядок порожній або некоректний.")
        return None
