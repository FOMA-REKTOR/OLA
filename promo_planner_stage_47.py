# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: PromoPlanner
def demo():
    print("=" * 60)
    print("PromoPlanner — Демо-сценарий")
    print("=" * 60)

    channels = [
        {"id": 1, "name": "Instagram", "platform": "social"},
        {"id": 2, "name": "VK", "platform": "social"},
        {"id": 3, "name": "Email", "platform": "email"},
        {"id": 4, "name": "Telegram", "platform": "social"},
    ]
    print("\n📌 Добавлены каналы:")
    for ch in channels:
        print(f"   • {ch['name']} ({ch['platform']})")

    budget = Budget(100000, 10, 1)
    print(f"\n💰 Бюджет установлен: {budget}")

    tasks = [
        Task(1, 1, "Создать визуал", "Создать баннер для Instagram"),
        Task(1, 2, "Написать текст", "Подготовить описание акции"),
        Task(1, 3, "Запустить кампанию", "Опубликовать пост"),
        Task(1, 4, "Провести анализ", "Собрать статистику"),
        Task(2, 1, "Создать визуал", "Создать баннер для VK"),
        Task(2, 2, "Написать текст", "Подготовить описание акции"),
        Task(2, 3, "Запустить кампанию", "Опубликовать пост"),
        Task(2, 4, "Провести анализ", "Собрать статистику"),
    ]
    print(f"\n📋 Добавлено {len(tasks)} задач")

    results = [
        Result(1, 1, 450, 320, "high"),
        Result(1, 2, 80, 150, "medium"),
        Result(1, 3, 1200, 1100, "high"),
        Result(1, 4, 200, 250, "low"),
        Result(2, 1, 380, 290, "medium"),
        Result(2, 2, 60, 110, "low"),
        Result(2, 3, 950, 920, "high"),
        Result(2, 4, 180, 200, "low"),
    ]
    print(f"   📊 Получено {len(results)} результатов")

    planner = PromoPlanner(channels, budget, tasks, results)
    print(f"\n🚀 Инициализация планировщика...")
    planner.run()

    print("\n" + "=" * 60)
    print("✅ Демо-сценарий завершен")
    print("=" * 60)
