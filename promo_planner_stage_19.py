# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: PromoPlanner
def archive_records(records, threshold_days=30):
    """Archive records older than threshold_days in-place and return list of archived IDs."""
    import datetime as dt
    cutoff = dt.datetime.now() - dt.timedelta(days=threshold_days)
    archived = []
    for i, rec in enumerate(records):
        if isinstance(rec.get('created_at'), dt.datetime):
            if rec['created_at'] < cutoff:
                records[i]['archived'] = True
                archived.append(i)
    return archived
