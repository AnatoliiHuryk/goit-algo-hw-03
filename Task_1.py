import os
import shutil
import sys
from pathlib import Path

def copy_files_recursively(src_dir, dest_dir="dist"):
    try:
        src_path = Path(src_dir)
        dest_path = Path(dest_dir)

        if not src_path.is_dir():
            print(f"Помилка: {src_dir} не є дійсною директорією.")
            return

        dest_path.mkdir(parents=True, exist_ok=True)

        for root, dirs, files in os.walk(src_path):
            for file in files:
                file_path = Path(root) / file
                file_ext = file_path.suffix[1:]

                if not file_ext:
                    continue

                ext_dir = dest_path / file_ext
                ext_dir.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.copy2(file_path, ext_dir / file)
                    print(f"Копіювання {file_path} до {ext_dir / file}")
                except Exception as e:
                    print(f"Помилка під час копіювання файлу {file_path}: {e}")

    except Exception as e:
        print(f"Сталася помилка під час роботи програми: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python script.py <вихідна_директорія> [директорія_призначення]")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"

    copy_files_recursively(source_directory, destination_directory)

#python script.py /path/to/source
