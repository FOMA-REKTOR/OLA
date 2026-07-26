# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: PromoPlanner
def reset_demo_data():
    """Сбрасывает все данные в дефолтные значения."""
    global channels, tasks, results, budget_used, promo_name
    channels = {i: ["Канал", i] for i in range(1, 3)}
    tasks = []
    results = []
    budget_used = 0.0
    promo_name = "Промо-акция"

def clear_state():
    """Полностью очищает все данные и сбрасывает в дефолт."""
    reset_demo_data()
