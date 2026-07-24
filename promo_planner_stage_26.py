# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: PromoPlanner
def demo_commands():
    print("=== PromoPlanner Demo ===")
    channels = {"social_media": "Социальные сети", "email_marketing": "Email маркетинг", "offline_ads": "Офлайн реклама"}
    for ch, name in channels.items():
        c = Channel(ch, name)
        c.budget.set_total(1000)
        c.budget.add_expense("setup_cost", 500)
        c.budget.add_expense("campaign_cost", 400)
        result = Result(campaign_id="d1", channel=c.id, name="Демо-кампания", status="active")
        result.kpi.set_target(10000)
        result.kpi.set_actual(7500)
        task = Task("Запуск кампании", "Создать лендинг", 3, c, result)
        task.status = "in_progress"
        print(f"\nКанал: {c.name}, Бюджет: {c.budget.remaining} руб., Результат: KPI {result.kpi.actual}/{result.kpi.target}")
        print(f"  Задача: {task.summary}")

demo_commands()
