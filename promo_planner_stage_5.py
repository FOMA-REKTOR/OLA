# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: PromoPlanner
def delete_record(table_name, id_value):
    if not table_name or not isinstance(id_value, int) or id_value <= 0:
        raise ValueError("Некорректные параметры для удаления")
    try:
        with open('promoplanner.db', 'r') as f_in, open('promoplanner_tmp.db', 'w+') as f_out:
            for line in f_in:
                parts = line.strip().split('|')
                if len(parts) < 2 or int(parts[1]) != id_value:
                    f_out.write(line)
        import os
        os.replace('promoplanner_tmp.db', 'promoplanner.db')
    except FileNotFoundError:
        pass

def handle_missing_id(table_name, missing_ids):
    if not table_name or not isinstance(missing_ids, list):
        return []
    valid_tables = ['channels', 'budgets', 'tasks', 'results']
    filtered = [id_ for id_ in missing_ids if isinstance(id_, int) and id_ > 0]
    invalid_msg = f"Ошибка: таблица '{table_name}' не найдена или ID некорректны." if table_name not in valid_tables else ""
    return filtered, invalid_msg
