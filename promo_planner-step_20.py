# === Stage 20: Добавь восстановление записей из архива ===
# Project: PromoPlanner
import json, os

def load_archive(records_path='promo_records.json', archive_path='promo_archive.json'):
    records = []
    if not os.path.exists(records_path): return records
    with open(records_path) as f: records = json.load(f)
    if not os.path.exists(archive_path): return records
    with open(archive_path) as f: archived = json.load(f)
    for rec in archived:
        found = False
        for i, r in enumerate(records):
            if r.get('id') == rec['id']:
                records[i].update(rec)
                found = True
                break
        if not found: records.append(rec)
    return sorted(records, key=lambda x: x.get('date', ''))

def save_archive(records_path='promo_records.json', archive_path='promo_archive.json'):
    archived = [r for r in records if r.get('status') == 'archived']
    active = [r for r in records if r.get('status') != 'archived']
    with open(archive_path, 'w') as f: json.dump(active, f)
    with open(records_path, 'w') as f: json.dump(archived, f)
