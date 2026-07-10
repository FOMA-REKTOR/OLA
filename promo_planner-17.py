# === Stage 17: Добавь группировку записей по категориям ===
# Project: PromoPlanner
def group_records_by_category(records, category_field='category'):
    grouped = {}
    for rec in records:
        cat = rec.get(category_field, 'Uncategorized')
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(rec)
    return grouped

def summarize_by_category(grouped):
    summary = {}
    for cat, items in grouped.items():
        total_budget = sum(i.get('budget', 0) for i in items)
        avg_return = sum(i.get('return', 0) / i.get('spent', 1e-9) if i.get('spent') else 0 for i in items)
        summary[cat] = {
            'count': len(items),
            'total_budget': total_budget,
            'avg_roi': avg_return,
        }
    return summary

if __name__ == '__main__':
    sample = [
        {'id': 1, 'channel': 'email', 'category': 'retargeting'},
        {'id': 2, 'channel': 'social', 'category': 'awareness'},
        {'id': 3, 'channel': 'email', 'category': 'retargeting'},
    ]
    grouped = group_records_by_category(sample)
    print('Grouped:', grouped.keys())
    summary = summarize_by_category(grouped)
    print('Summary:', summary)
