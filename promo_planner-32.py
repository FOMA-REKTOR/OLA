# === Stage 32: Добавь журнал действий пользователя ===
# Project: PromoPlanner
import json, os


class ActionLog:
    """Журнал действий пользователя."""

    def __init__(self):
        self._path = "action_log.json"
        self._entries = []

    @property
    def entries(self):
        if not os.path.exists(self._path) or os.path.getsize(self._path) == 0:
            return []
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        except Exception:
            return []

    def add(self, user_name: str, action_type: str, description: str):
        entry = {
            "id": len(self._entries) + 1,
            "user": user_name,
            "type": action_type,
            "description": description,
            "timestamp": __import__("datetime").now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self._entries.append(entry)
        try:
            with open(self._path, "w", encoding="utf-8") as f:
                json.dump(self._entries, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def get_user_actions(self, user_name: str):
        return [e for e in self._entries if e["user"] == user_name]

    def clear(self):
        self._entries.clear()
        try:
            with open(self._path, "w", encoding="utf-8") as f:
                f.write("[]")
        except Exception:
            pass
