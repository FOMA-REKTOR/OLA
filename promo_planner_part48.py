# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: PromoPlanner
import json, os, random, datetime

def load_promo_data():
    data = {"channels": {"social": {"name": "Social Media", "cost_per_action": 5, "max_actions": 100}, "email": {"name": "Email", "cost_per_action": 0.5, "max_actions": 500}, "ads": {"name": "Paid Ads", "cost_per_action": 2, "max_actions": 200}}, "budget": 5000, "tasks": [], "results": []}
    if os.path.exists("promo_data.json"):
        with open("promo_data.json") as f:
            data.update(json.load(f))
    return data

def save_promo_data(data):
    with open("promo_data.json", "w") as f:
        json.dump(data, f, indent=2)

def suggest_task(data):
    budget_left = data["budget"] - sum(t.get("spent", 0) for t in data["tasks"])
    if budget_left <= 0:
        return {"task": "Pause campaigns", "channel": None, "cost": 0}
    channels = list(data["channels"].values())
    channel = random.choice(channels)
    max_actions = min(int(budget_left / channel["cost_per_action"]), channel["max_actions"])
    return {"task": f"Run {channel['name']} campaign", "channel": channel["name"], "cost": channel["cost_per_action"] * max_actions}

def simulate_result(data, task):
    return {"task": task["task"], "channel": task["channel"], "result": random.randint(5, 200), "roi": round(random.uniform(0.5, 5.0), 2)}

def run_promo_planner():
    data = load_promo_data()
    while data["budget"] > 0 and len(data["tasks"]) < 5:
        task = suggest_task(data)
        data["tasks"].append(task)
    results = [simulate_result(data, t) for t in data["tasks"]]
    data["results"] = results
    save_promo_data(data)
    return data
