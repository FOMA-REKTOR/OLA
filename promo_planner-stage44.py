# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: PromoPlanner
import shutil, os, datetime
from pathlib import Path

def backup_data_file(file_path: str, backup_dir: str = "backups") -> str:
    """Create a timestamped backup of the data file and return the backup path."""
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"{Path(file_path).name}_{timestamp}.bak"
    shutil.copy2(file_path, backup_path)
    return str(backup_path)
