# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: PromoPlanner
def calc_project_metrics():
    total_budget = sum(channel.budget for channel in channels) if channels else 0
    active_channels = len(channels) - any(
        (channel.status == "closed" or channel.status == "completed") for channel in channels
    ) if channels else 0
    total_tasks = sum(len(task_list) for task_list in [channel.tasks for channel in channels] if channel.tasks is not None) if channels else 0
    completed_tasks = sum(
        len([t for t in tl if (t.status == "done" or t.status == "completed")])
        for tl in [channel.tasks for channel in channels] if channel.tasks is not None
    ) if channels else 0
    task_completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0.0
    avg_budget_per_channel = total_budget / active_channels if active_channels > 0 else 0.0
    return {
        "total_budget": total_budget,
        "active_channels": active_channels,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "task_completion_rate": task_completion_rate,
        "avg_budget_per_channel": avg_budget_per_channel,
    }

print("Project metrics:", calc_project_metrics())
