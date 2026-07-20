# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: PromoPlanner
def print_table(headers, rows):
    widths = [len(str(h)) for h in headers]
    for r in rows:
        for i, v in enumerate(r):
            if str(v) and len(str(v)) > widths[i]:
                widths[i] = len(str(v))
    lines = []
    sep = '  '.join('-' * w for w in widths)
    lines.append(sep)
    lines.append('  '.join(str(h).ljust(widths[i]) for i, h in enumerate(headers)))
    lines.append(sep)
    for r in rows:
        lines.append('  '.join((str(v) or '').ljust(widths[i]) for i, v in enumerate(r)))
    return '\n'.join(lines)

def print_report(channels, budget, tasks, results):
    ch = [(c.name, c.budget_left, c.campaigns_count()) for c in channels]
    ts = [(t.id, t.channel_name, t.status.value) for t in tasks]
    rs = [(r.id, r.channel_name, r.type.value, f"{r.amount:.1f} {r.currency}") for r in results]
    print("=== PromoPlanner Report ===")
    print()
    print(print_table(["Channel", "Budget Left", "# Campaigns"], ch))
    print()
    print(print_table(["Task ID", "Channel", "Status"], ts))
    print()
    print(print_table(["Result ID", "Channel", "Type", "Amount (Currency)"], rs))
