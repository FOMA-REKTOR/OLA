# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: PromoPlanner
def find_duplicate_promo(promos, promo_id=None):
    if not promos:
        return None
    existing_ids = {p['id'] for p in promos}
    if promo_id in existing_ids:
        return next((p for p in promos if p['id'] == promo_id), None)
    for p in promos:
        if p.get('name') == promo_id:
            return p
    for p in promos:
        if p.get('channel') == promo_id:
            return p
    return None
