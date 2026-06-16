# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: PromoPlanner
class PromoPlannerData:
    def __init__(self):
        self.channels = {}
        self.budgets = {}
        self.tasks = []
        self.results = []

    def validate_channel_name(self, name: str) -> bool:
        return isinstance(name, str) and len(name.strip()) > 0

    def validate_budget(self, amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount >= 0

    def add_channel(self, name: str, budget_limit: float):
        if not self.validate_channel_name(name):
            raise ValueError("Некорректное имя канала")
        if not self.validate_budget(budget_limit):
            raise ValueError("Бюджет должен быть неотрицательным числом")
        self.channels[name] = {'limit': budget_limit, 'spent': 0}

    def add_task(self, channel: str, name: str, cost: float):
        if not self.validate_channel_name(channel) or channel not in self.channels:
            raise ValueError("Канал не существует")
        if not self.validate_budget(cost):
            raise ValueError("Стоимость задачи должна быть неотрицательной")
        remaining = self.channels[channel]['limit'] - self.channels[channel]['spent']
        if cost > remaining:
            raise ValueError(f"Недостаточно бюджета для канала {channel}")
        self.tasks.append({'channel': channel, 'name': name, 'cost': cost})
        self.channels[channel]['spent'] += cost

    def add_result(self, task_name: str, revenue: float):
        if not isinstance(task_name, str) or len(task_name.strip()) == 0:
            raise ValueError("Некорректное имя задачи")
        if not self.validate_budget(revenue):
            raise ValueError("Доход должен быть неотрицательным числом")
        self.results.append({'task': task_name, 'revenue': revenue})
