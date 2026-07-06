# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: PromoPlanner
def weekly_stats_by_date(stats_list, date_format="%Y-%m-%d"):
    """Compute per-date weekly stats from a list of weekly records."""
    if not stats_list:
        return {}
    grouped = {}
    for rec in stats_list:
        d = rec.get("date", "")[:10]  # YYYY-MM-DD
        grouped.setdefault(d, {"week": rec["week"], "channel_count": rec["channel_count"]})
    result = {}
    for d, vals in sorted(grouped.items()):
        result[d] = {
            "date": d,
            "avg_weeks": sum(vals.get("week", 0) for _ in vals) / len(vals),
            "total_channels": sum(vals["channel_count"] for _ in vals),
        }
    return result


if __name__ == "__main__":
    sample = [
        {"date": "2025-10-01", "week": 4, "channel_count": 3},
        {"date": "2025-10-08", "week": 5, "channel_count": 4},
        {"date": "2025-10-01", "week": 4, "channel_count": 2},
    ]
    print(weekly_stats_by_date(sample))
