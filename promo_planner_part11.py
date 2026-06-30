# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: PromoPlanner
import json, os

def save_to_file(data: dict, filename: str = "promoplanner.json") -> None:
    """Сохраняет состояние приложения в JSON файл с проверкой и форматированием."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def load_from_file(filename: str = "promoplanner.json") -> dict | None:
    """Загружает данные из JSON файла, возвращает None если файл отсутствует или повреждён."""
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные успешно загружены из {filename}")
        return data
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return {}

if __name__ == "__main__":
    # Пример использования для тестирования сохранения и загрузки
    test_data = {"channels": [], "budget": 0, "tasks": []}
    save_to_file(test_data)
    loaded_data = load_from_file()
    print(f"Загруженные данные: {loaded_data}")
