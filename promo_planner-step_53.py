# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: PromoPlanner
def import_from_text(path):
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(";")]
            if len(parts) < 3:
                continue
            rec = {
                "id": int(parts[0]),
                "name": parts[1],
                "channel": parts[2],
                "budget": float(parts[3]) if len(parts) > 3 else 0.0,
                "status": parts[4] if len(parts) > 4 else "planned",
            }
            records.append(rec)
    return records
