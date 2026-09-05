# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: PromoPlanner
import sys

class Color:
    """ANSI-кодовые цвета для терминала."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"

    # Форматирования текста
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Сброс цвета
    NO_COLOR = False

def enable_color():
    """Включает цветовую поддержку."""
    Color.NO_COLOR = False

def disable_color():
    """Отключает цветовую поддержку."""
    Color.NO_COLOR = True
    Color.RESET = ""
    Color.BOLD = ""
    Color.DIM = ""
    Color.UNDERLINE = ""
    Color.BLACK = ""
    Color.RED = ""
    Color.GREEN = ""
    Color.YELLOW = ""
    Color.BLUE = ""
    Color.MAGENTA = ""
    Color.CYAN = ""
    Color.WHITE = ""
