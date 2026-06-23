# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: PromoPlanner
def sort_promo_records(records, key='date'):
    if not records: return []
    reverse = {'priority': True, 'name': False}.get(key, False)
    order_map = {'date': lambda r: (r['end_date'] or datetime.min).timestamp(),
                 'priority': lambda r: -r.get('priority', 0),
                 'name': lambda r: r['name'].lower()}
    return sorted(records, key=order_map.get(key, lambda r: r), reverse=reverse)
