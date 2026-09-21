# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: PromoPlanner
class ChangeLog:
    def __init__(self):
        self.entries = []

    def add(self, event, who, what):
        self.entries.append({
            'timestamp': datetime.now().isoformat(),
            'who': who,
            'what': what,
        })

    def __str__(self):
        out = '=== Change Log ===\n'
        for i, entry in enumerate(self.entries, 1):
            out += f"#{i} [{entry['timestamp']}] {entry['who']}: {entry['what']}\n"
        return out
