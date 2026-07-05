# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: PromoPlanner
def generate_summary():
    if not channels: return print("Нет данных для сводки.")
    total_budget = sum(c.budget for c in channels.values())
    spent = sum(r.spent for r in results)
    remaining = total_budget - spent
    tasks_done = len([t for t in tasks if t.status == 'done'])
    print(f"Каналов: {len(channels)}, Завершено задач: {tasks_done}/{len(tasks)}")
    print(f"Бюджет: {total_budget:.2f}, Израсходовано: {spent:.2f}, Остаток: {remaining:.2f}")
