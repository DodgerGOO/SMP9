import pyfiglet

def get_available_fonts():
    """Повертає список доступних шрифтів для ASCII-арту."""
    return pyfiglet.FigletFont.getFonts()

def preview_font_example(font):
    """Показує приклад шрифту."""
    return pyfiglet.figlet_format("Example", font=font)