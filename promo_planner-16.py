# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: PromoPlanner
def monthly_stats(data):
    """Расчёт месячной статистики по датам."""
    stats = {}
    for item in data:
        if 'date' not in item:
            continue
        date_str = item['date']
        if isinstance(date_str, datetime.date):
            month_key = date_str.strftime('%Y-%m')
        else:
            try:
                dt = datetime.datetime.strptime(str(date_str), '%Y-%m-%d').date()
                month_key = dt.strftime('%Y-%m')
            except (ValueError, TypeError):
                continue
        
        if month_key not in stats:
            stats[month_key] = {'count': 0, 'total_budget': 0.0}
        
        stats[month_key]['count'] += 1
        if 'budget' in item and isinstance(item['budget'], (int, float)):
            stats[month_key]['total_budget'] += float(item['budget'])
    
    return stats
