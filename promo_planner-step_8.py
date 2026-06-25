# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: PromoPlanner
def main():
    print("=== PromoPlanner CLI ===")
    while True:
        cmd = input("\n1. Каналы | 2. Бюджет | 3. Задачи | 4. Результаты | 5. Выход > ").strip()
        if not cmd: continue
        try:
            action, *args = map(int, cmd.split())
        except ValueError:
            print("Неверный ввод.")
            continue
        
        actions = {1: "canal_menu", 2: "budget_menu", 3: "task_menu", 4: "result_menu"}
        
        if action in actions:
            menu_func = actions[action]
            print(f"\n--- Меню {menu_func} ---")
            
            # Имитация выбора действия в меню (заглушка для структуры)
            sub_cmd = input("Выберите действие из списка выше или 'q' для выхода: ").strip()
            if sub_cmd.lower() == 'q': break
            
        elif action in [5]:
            print("\nВыход из программы.")
            break
        
        else:
            print("Неизвестная команда меню.")

if __name__ == "__main__":
    main()
