# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: PromoPlanner
from typing import Callable, Optional
def filter_records(records: list[dict], status: Optional[str] = None, category: Optional[str] = None, tags: Optional[list[str]] = None) -> list[dict]:
    if not records: return []
    filtered = [r for r in records if (not status or r.get('status') == status) and (not category or r.get('category') == category)]
    if tags is not None:
        def has_all_tags(rec):
            rec_tags = set(r.get('tags', [])).union(*[set(t) for t in r.get('sub_tags', [])])
            return all(tag in rec_tags for tag in tags)
        filtered = [r for r in filtered if has_all_tags(r)]
    return filtered
