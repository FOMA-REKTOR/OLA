# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: PromoPlanner
def dry_run_operation(op_name, **kwargs):
    print(f"[DRY-RUN] {op_name}:")
    for k, v in kwargs.items():
        print(f"  {k} = {v}")
    print("[DRY-RUN] Операция отменена, данные не изменены.\n")
