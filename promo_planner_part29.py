# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: PromoPlanner
APP_CONFIG = {
    "app_name": "PromoPlanner",
    "version": "0.29",
    "channels": ["social_media", "email", "offline"],
    "default_budget_usd": 500,
    "monitors_enabled": True,
    "monitor_interval_seconds": 3600,
    "max_tasks_per_promo": 10,
    "results_history_days": 90,
}

def get_config(key=None):
    if key is None:
        return APP_CONFIG.copy()
    return APP_CONFIG.get(key)
