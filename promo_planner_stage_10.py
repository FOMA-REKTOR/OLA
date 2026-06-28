# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: PromoPlanner
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "channels": channels,
        "budgets": budgets,
        "tasks": tasks,
        "results": results,
        "exported_at": datetime.utcnow().isoformat() + "Z"
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
