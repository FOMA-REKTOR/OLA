# === Stage 45: Добавь восстановление из резервной копии ===
# Project: PromoPlanner
import shutil
import os
from datetime import datetime

BACKUP_DIR = os.path.join(os.path.dirname(__file__), "backups")

def create_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"promo_backup_{timestamp}.py")
    if os.path.exists(backup_path):
        os.remove(backup_path)
    shutil.copy2(__file__, backup_path)
    print(f"Backup saved to {backup_path}")
    return backup_path

def restore_backup():
    if not os.path.exists(BACKUP_DIR):
        print("No backups directory found.")
        return False
    backups = [f for f in os.listdir(BACKUP_DIR) if f.endswith(".py")]
    if not backups:
        print("No backup files found.")
        return False
    latest = sorted(backups)[-1]
    backup_path = os.path.join(BACKUP_DIR, latest)
    if not os.path.isfile(backup_path):
        print("Backup file corrupted or missing.")
        return False
    # Restore by replacing current file with backup
    original_stat = os.stat(__file__)
    shutil.copy2(backup_path, __file__)
    print(f"Restored from {backup_path}")
    return True
