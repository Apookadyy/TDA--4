# file_organizer/organizer.py

import os
import shutil
from collections import defaultdict

# Windows-safe Downloads path
SOURCE_DIR = os.path.join(os.path.expanduser("~"), "Downloads")

# Folder where organized files will go
ORGANIZED_DIR = os.path.join(SOURCE_DIR, "Organized_Files")

FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
}

def organize_files():
    print("\n📁 FILE ORGANIZER:")
    print(f"✅ Monitoring: {SOURCE_DIR}")

    if not os.path.exists(ORGANIZED_DIR):
        os.makedirs(ORGANIZED_DIR)

    stats = defaultdict(int)

    for file in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)

            moved = False
            for category, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    category_path = os.path.join(ORGANIZED_DIR, category)
                    os.makedirs(category_path, exist_ok=True)

                    shutil.move(file_path, os.path.join(category_path, file))
                    stats[category] += 1
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(ORGANIZED_DIR, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, file))
                stats["Others"] += 1

    print("📊 Statistics:")
    for k, v in stats.items():
        print(f"   • {k}: {v}")

    print("⏰ Last Run: Just now")
