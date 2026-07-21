# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: PromoPlanner
def print_record(record):
    if not record: return
    print("="*60)
    print(f"📌 ID: {record.get('id')}")
    print(f"   Канал:  {record.get('channel') or '—'}")
    print(f"   Статус: {record.get('status','?').upper()}")
    print(f"   Бюджет: {record.get('budget',0):,.0f} ₽ → потрачено {record.get('spent',0):,.0f}")
    print(f"   Задачи: {record.get('tasks_count',0)} завершено из {len(record.get('tasks',[]))}")
    print(f"   ROI:    {record.get('roi','—') or '—'}")
    print("="*60)

# Пример использования (раскомментируй при запуске):
# if __name__ == "__main__":
#     demo = {"id":"P2","channel":"vk","status":"done","budget":5000,"spent":3800,
#             "tasks":["пост1","пост2"],"roi":4.2}
#     print_record(demo)
