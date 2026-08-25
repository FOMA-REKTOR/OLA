# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: PromoPlanner
def get_next_action_state(state):
    """Generates a recommended next action based on current promo state."""
    if state.get("budget_remaining", 0) <= 0 and not state.get("active_campaigns"):
        return {"action": "end", "message": "All budgets exhausted. Campaigns concluded."}
    if state.get("active_campaigns", 0) >= 3:
        return {"action": "pause", "message": "Too many active campaigns. Consider pausing some."}
    if not state.get("tasks_completed", 0):
        return {"action": "start", "message": "No tasks completed yet. Start a new campaign."}
    if state.get("tasks_completed", 0) < 5:
        return {"action": "continue", "message": "Keep working on current tasks."}
    return {"action": "review", "message": "Tasks completed. Review results and plan next steps."}
