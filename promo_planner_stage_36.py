# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: PromoPlanner
def repair_simple_issues(data):
    """Проверяет и чинит типичные мелкие проблемы:
    - пустой список каналов;
    - пустой список задач;
    - отсутствие бюджета;
    - отрицательные значения бюджета;
    - пустой список результатов;
    - отрицательные значения в результатах.
    """
    if not data.get('channels'):
        data['channels'] = []
    if not data.get('tasks'):
        data['tasks'] = []
    if not data.get('budget'):
        data['budget'] = 0
    if data.get('budget') < 0:
        data['budget'] = 0
    if not data.get('results'):
        data['results'] = []
    for result in data['results']:
        if isinstance(result, dict):
            for key in list(result.keys()):
                if key.startswith('_'):
                    continue
                if key not in ('name', 'channel_id', 'task_id', 'value'):
                    del result[key]
                if key == 'value' and isinstance(result[key], (int, float)) and result[key] < 0:
                    result[key] = 0
    return data
