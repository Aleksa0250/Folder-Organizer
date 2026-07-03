from pathlib import Path
import shutil
import re

def organize_folder(source):

    source = Path(source)

    categories = {
        "Slike": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff", ".raw", ".heic"],
        "Video": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".3gp"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".opus"],
        "Dokumenti": [".pdf", ".doc", ".docx", ".odt", ".rtf", ".txt", ".md", ".epub"],
        "Tabele": [".xls", ".xlsx", ".ods", ".csv"],
        "Prezentacije": [".ppt", ".pptx", ".odp", ".key"],
        "Kod": [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c",
                ".h", ".cs", ".go", ".rs", ".php", ".rb", ".sh", ".bat", ".sql"],
        "Arhive": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"],
        "Izvrsni": [".exe", ".msi", ".dmg", ".deb", ".rpm", ".apk"],
        "Fontovi": [".ttf", ".otf", ".woff", ".woff2"],
        "Baze_podataka": [".db", ".sqlite", ".sqlite3", ".mdb"],
        "3D_i_CAD": [".obj", ".fbx", ".stl", ".blend", ".dae"]
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
        print("Folder ne postoji!")
        return

    moved = 0

    for file in source.iterdir():

        if not file.is_file():
            continue

        ext = file.suffix.lower()

        folder = "Ostalo"

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

    print(f"\nUkupno premešteno fajlova: {moved}")


folder = input("Unesi putanju foldera: ")

organize_folder(folder)