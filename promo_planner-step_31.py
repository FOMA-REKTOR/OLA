# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: PromoPlanner
def switch_profile(new_name=None):
    """Переключить активный профиль. Если new_name None, вернуть текущий."""
    if not profiles:
        print("Нет сохранённых профилей.")
        return "none"
    current = active_profile or "default"
    if new_name is None:
        return current
    if new_name not in profiles:
        print(f"Профиль '{new_name}' не найден. Список: {', '.join(profiles)}")
        return "unknown"
    old = active_profile
    active_profile = new_name
    print(f"Переключено с профиля '{old}' на '{new_name}'.")
    return new_name
