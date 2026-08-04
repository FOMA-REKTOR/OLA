# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: PromoPlanner
def undo_last_action(state: dict) -> None | tuple[dict, str]:
    """Откат последнего действия в истории. Возвращает (новое_состояние, сообщение)."""
    if not state.get("history") or not state["history"]:
        return state, "Нет действий для отката."

    last = state["history"][-1]
    action_type = last.get("type", "")
    new_state = {**state}
    del new_state["history"][-1]

    if action_type == "add_channel":
        channel_name = last["channel"]["name"]
        if channel_name in new_state.get("channels", {}):
            return state, f"Канал '{channel_name}' уже существует."
        new_state["channels"][channel_name] = {"budget": 0, "tasks": [], "results": []}

    elif action_type == "add_budget":
        budget_value = last["budget"]
        for ch in new_state.get("channels", {}).values():
            if isinstance(ch, dict):
                ch["budget"] = budget_value

    elif action_type == "add_task":
        channel_name = last["task"]["channel"]
        task_desc = last["task"]["description"]
        if channel_name not in new_state.get("channels", {}):
            return state, f"Канал '{channel_name}' не найден."
        ch_data = new_state["channels"][channel_name]
        ch_data.setdefault("tasks", []).append(task_desc)

    elif action_type == "set_result":
        channel_name = last["result"]["channel"]
        result_value = last["result"]["value"]
        if channel_name not in new_state.get("channels", {}):
            return state, f"Канал '{channel_name}' не найден."
        ch_data = new_state["channels"][channel_name]
        results_list = ch_data.get("results", [])
        # Удаляем последний результат по каналу
        while results_list and results_list[-1].get("channel") == channel_name:
            results_list.pop()
        if not isinstance(ch_data, dict):
            return state, "Ошибка структуры канала."
        ch_data["results"] = results_list

    elif action_type == "delete_channel":
        channel_name = last["channel"]["name"]
        if channel_name in new_state.get("channels", {}):
            del new_state["channels"][channel_name]

    else:
        return state, f"Неподдерживаемое действие для отката: {action_type}."

    # Восстанавливаем историю без последнего элемента
    history = state.get("history", [])[:-1] if len(state.get("history", [])) > 1 else []
    new_state["history"] = history
    return new_state, "Действие отменено."
