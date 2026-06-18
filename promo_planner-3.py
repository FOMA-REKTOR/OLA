# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: PromoPlanner
class PromoPlanner:
    def __init__(self):
        self.channels = {}
        self.budgets = {}
        self.tasks = []
        self.results = []

    def add_channel(self, name, platform, cost_per_post=0.0):
        if not name or not platform:
            raise ValueError("Имя канала и платформа обязательны")
        self.channels[name] = {"platform": platform, "cost_per_post": cost_per_post}
        return True

    def set_budget(self, channel_name, amount):
        if channel_name in self.channels:
            self.budgets[channel_name] = float(amount)
            return True
        raise ValueError(f"Канал {channel_name} не найден")

    def add_task(self, channel_name, content, date, status="planned"):
        if not all([channel_name, content, date]):
            raise ValueError("Не все поля задачи заполнены")
        task_id = len(self.tasks) + 1
        self.tasks.append({
            "id": task_id,
            "channel": channel_name,
            "content": content,
            "date": date,
            "status": status
        })
        return True

    def record_result(self, task_id, impressions=0, clicks=0):
        if not any(t["id"] == task_id for t in self.tasks):
            raise ValueError(f"Задача с ID {task_id} не найдена")
        result = {"task_id": task_id, "impressions": impressions, "clicks": clicks}
        self.results.append(result)
        return True

    def get_summary(self):
        summary = {
            "channels_count": len(self.channels),
            "tasks_count": len(self.tasks),
            "results_count": len(self.results)
        }
        for ch_name, budget in self.budgets.items():
            if ch_name in self.channels:
                summary[ch_name] = {"budget": budget}
        return summary

planner = PromoPlanner()
