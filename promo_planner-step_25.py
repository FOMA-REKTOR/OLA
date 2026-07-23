# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: PromoPlanner
import re

_DATE_RE = re.compile(
    r'^(\d{4})-(\d{1,2})-(\d{1,2})$',
)


def parse_date(date_string: str):
    """Parse a date in YYYY-MM-DD format. Returns None if invalid."""
    match = _DATE_RE.match(date_string)
    if not match:
        return None
    year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month[month]:
        return None
    return (year, month, day)


def format_date(year, month, day):
    """Format a date tuple as YYYY-MM-DD."""
    return f'{year:04d}-{month:02d}-{day:02d}'
