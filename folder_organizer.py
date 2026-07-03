from pathlib import Path
import shutil
import re

def organize_folder(source):

    source = Path(source)

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff", ".raw", ".heic"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".3gp"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".opus"],
        "Documents": [".pdf", ".doc", ".docx", ".odt", ".rtf", ".txt", ".md", ".epub"],
        "Spreadsheets": [".xls", ".xlsx", ".ods", ".csv"],
        "Presentations": [".ppt", ".pptx", ".odp", ".key"],
        "Code": [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c",
                 ".h", ".cs", ".go", ".rs", ".php", ".rb", ".sh", ".bat", ".sql"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"],
        "Executables": [".exe", ".msi", ".dmg", ".deb", ".rpm", ".apk"],
        "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "Databases": [".db", ".sqlite", ".sqlite3", ".mdb"],
        "3D_and_CAD": [".obj", ".fbx", ".stl", ".blend", ".dae"]
    }

    def unique_name(path):

        if not path.exists():
            return path

        original_name = path.stem
        extension = path.suffix

        clean_name = re.sub(r" \(\d+\)$", "", original_name)

        counter = 1

        while True:

            new_path = path.with_name(f"{clean_name} ({counter}){extension}")

            if not new_path.exists():
                return new_path

            counter += 1

    if not source.is_dir():
        print("Folder does not exist!")
        return

    moved = 0

    for file in source.iterdir():

        if not file.is_file():
            continue

        ext = file.suffix.lower()

        folder = "Others"

        for category, extensions in categories.items():
            if ext in extensions:
                folder = category
                break

        target_folder = source / folder

        target_folder.mkdir(exist_ok=True)

        new_path = unique_name(target_folder / file.name)

        shutil.move(file, new_path)

        print(f"{file.name} → {folder}")

        moved += 1

    print(f"\nTotal files moved: {moved}")


folder = input("Enter folder path: ")

organize_folder(folder)
