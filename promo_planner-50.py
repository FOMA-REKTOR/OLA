# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: PromoPlanner
def format_report(summary):
    """Оформление итогового отчёта в читаемом виде."""
    lines = [
        "=== PromoPlanner — Итоговый отчёт ===",
        f"Каналы:      {summary['channels']}",
        f"Задачи:      {summary['tasks']}",
        f"Бюджет:      {summary['budget']:.2f} руб.",
        f"Выполнено:   {summary['completed']}",
        f"ROI:         {summary['roi']:.1f}%",
    ]
    return "\n".join(lines)
