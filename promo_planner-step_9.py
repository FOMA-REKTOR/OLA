# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: PromoPlanner
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация обязательных полей
        required_fields = ['channels', 'budgets', 'tasks']
        for field in required_fields:
            if field not in data:
                raise KeyError(f"Отсутствует поле {field}")
            
            # Проверка типов данных для каналов и бюджетов
            if not isinstance(data['channels'], list):
                raise TypeError("Поле channels должно быть списком")
            if not isinstance(data['budgets'], dict) or 'total' not in data['budgets']:
                raise ValueError("Некорректная структура budgets")
            
        return {
            "version": 1,
            "channels": data.get('channels', []),
            "budgets": data.get('budgets', {}),
            "tasks": data.get('tasks', [])
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    sample_json = '''
    {
        "channels": ["email", "social_media"],
        "budgets": {"total": 5000, "allocated": {}},
        "tasks": []
    }'''
    
    initial_data = load_initial_data(sample_json)
    print(f"Загружено каналов: {len(initial_data['channels'])}")
