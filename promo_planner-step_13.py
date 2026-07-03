# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: PromoPlanner
def search_promo_campaigns(query: str, channels=None, min_budget=0) -> list[dict]:
    query_lower = query.lower().strip()
    results = []
    for campaign in campaigns_db:
        if not any(keyword in campaign['name'].lower() or keyword in campaign['description'].lower() for keyword in [query_lower]):
            continue
        if channels and campaign['channel'] != channels:
            continue
        if campaign['budget'] < min_budget:
            continue
        results.append(campaign)
    return sorted(results, key=lambda x: x['created_at'], reverse=True)
