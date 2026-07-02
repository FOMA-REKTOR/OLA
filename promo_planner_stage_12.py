# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: PromoPlanner
def load_promo_data(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив данных")
        return {
            "channels": [c for c in data if c.get("type")] or [],
            "budgets": [b for b in data if b.get("amount")],
            "tasks": [t for t in data if t.get("status")],
            "results": [r for r in data if r.get("metric")]
        }
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
        return {}
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных из {filepath}: {type(e).__name__}")
        return {}
