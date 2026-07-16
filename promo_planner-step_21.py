# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: PromoPlanner
class Reminders:
    def __init__(self):
        self.reminders = []
    
    def add_reminder(self, task_id, deadline, message="Напоминание"):
        reminder = {
            "task_id": task_id,
            "deadline": deadline,
            "message": message,
            "is_done": False,
            "created_at": datetime.now()
        }
        self.reminders.append(reminder)
        return reminder
    
    def get_pending_reminders(self):
        today = datetime.today().date()
        pending = [r for r in self.reminders if not r["is_done"] and r["deadline"].date() <= today]
        return sorted(pending, key=lambda x: x["deadline"])
    
    def mark_completed(self, reminder_id):
        for r in self.reminders:
            if r.get("id") == reminder_id:
                r["is_done"] = True
                return True
        return False
    
    def get_all_reminders(self):
        return list(self.reminders)
