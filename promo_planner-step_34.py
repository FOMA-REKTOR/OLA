# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: PromoPlanner
TEMPLATES = {
    "email_newsletter": {
        "name": "Email Newsletter",
        "channel": "email",
        "duration_days": 7,
        "budget": 500,
        "target_audience": "all_subscribers",
        "priority": 5,
    },
    "social_promo": {
        "name": "Social Media Promo",
        "channel": "social",
        "duration_days": 3,
        "budget": 200,
        "target_audience": "followers",
        "priority": 4,
    },
    "blog_post": {
        "name": "Blog Post",
        "channel": "blog",
        "duration_days": 14,
        "budget": 100,
        "target_audience": "website_visitors",
        "priority": 3,
    },
    "offline_event": {
        "name": "Offline Event",
        "channel": "offline",
        "duration_days": 1,
        "budget": 2000,
        "target_audience": "local_audience",
        "priority": 5,
    },
}

def create_promo_from_template(template_name: str, **overrides) -> dict:
    if template_name not in TEMPLATES:
        raise ValueError(f"Unknown template: {template_name}")
    base = dict(TEMPLATES[template_name])
    base.update(overrides)
    return base
