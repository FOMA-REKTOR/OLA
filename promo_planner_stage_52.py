# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: PromoPlanner
def export_text_report(self):
    """Export a concise text report with channels, budget, tasks, and results."""
    lines = []
    lines.append("=== PromoPlanner Report ===")
    lines.append(f"Date: {self.report_date}")
    lines.append(f"Currency: {self.currency}")
    lines.append("")
    lines.append("--- Channels ---")
    for ch in self.channels:
        lines.append(f"  {ch.name} (type={ch.type}, status={ch.status})")
    lines.append("")
    lines.append("--- Budget ---")
    lines.append(f"  Budget: {self.budget} {self.currency}")
    lines.append(f"  Spent: {self.spent} {self.currency}")
    lines.append(f"  Remaining: {self.budget - self.spent} {self.currency}")
    lines.append("")
    lines.append("--- Tasks ---")
    for t in self.tasks:
        lines.append(f"  [{t.status}] {t.name} - cost={t.cost} {self.currency}")
    lines.append("")
    lines.append("--- Results ---")
    for r in self.results:
        lines.append(f"  {r.name}: {r.value} {self.currency} (channel={r.channel})")
    lines.append("")
    return "\n".join(lines)
