# === Stage 43: Добавь пагинацию длинных списков ===
# Project: PromoPlanner
def paginate(items, page_size=20):
    """Return (current_page, total_pages, items_on_page) for a 1-indexed page."""
    if page_size <= 0:
        page_size = 20
    total_pages = max(1, -(-len(items) // page_size))
    page = max(1, min(page, total_pages))
    start = (page - 1) * page_size
    end = start + page_size
    return page, total_pages, items[start:end]
