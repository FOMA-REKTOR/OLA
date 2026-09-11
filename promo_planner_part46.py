# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: PromoPlanner
def migrate_promo_planner_to_v2():
    """Migrate PromoPlanner data structures to v2 schema."""
    try:
        from promo_planner import PromoPlanner
        planner = PromoPlanner()
        planner._version = 2
        planner._channels = {
            "email": {"name": "Email", "budget": 5000, "tasks": 0, "results": {}},
            "social": {"name": "Social Media", "budget": 8000, "tasks": 0, "results": {}},
            "web": {"name": "Web", "budget": 12000, "tasks": 0, "results": {}},
        }
        planner._budget_total = 25000
        planner._tasks = []
        planner._results = []
        planner._history = []
        planner._version_history = [(1, "initial", []), (2, "migrated", [])]
        print("PromoPlanner migrated to v2 successfully.")
    except Exception as e:
        print(f"Migration failed: {e}")
