# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: PromoPlanner
def check_overdue_reminders():
    overdue = []
    for task in tasks:
        if task.reminder_date and task.reminder_date < datetime.now().date() and not task.is_done:
            overdue.append(task)
    return overdue
