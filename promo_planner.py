# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: PromoPlanner
import json, random
from dataclasses import asdict
from datetime import date, timedelta

def generate_demo_data():
    channels = ["email", "social_media", "sms"]
    tasks = []
    for i in range(5):
        tasks.append({
            "id": i + 1,
            "name": f"Задача {i+1}",
            "channel": random.choice(channels),
            "budget": round(random.uniform(1000, 5000), 2),
            "status": "planned",
            "start_date": (date.today() + timedelta(days=random.randint(0, 30))).isoformat(),
            "results": {}
        })
    return {
        "project_name": "PromoPlanner Demo",
        "total_budget": sum(t["budget"] for t in tasks),
        "channels": channels,
        "tasks": tasks
    }

if __name__ == "__main__":
    demo = generate_demo_data()
    print(json.dumps(demo, indent=2))
