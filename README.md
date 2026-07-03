# 📁 Folder Organizer (Python)

A simple Python script that automatically organizes files in a selected folder by sorting them into categorized subfolders based on file extensions.

---

## ⚙️ How it works

- User enters a folder path
- Script scans all files in that folder
- Files are sorted based on their extensions
- Appropriate folders are created automatically if they don’t exist
- Files are moved into their corresponding categories

---

## 📂 Categories

Files are organized into the following folders:

- Images (jpg, png, gif, etc.)
- Videos (mp4, mkv, avi, etc.)
- Audio (mp3, wav, flac, etc.)
- Documents (pdf, docx, txt, etc.)
- Spreadsheets (xlsx, csv, etc.)
- Presentations (pptx, ppt, etc.)
- Code (py, js, html, css, etc.)
- Archives (zip, rar, 7z, etc.)
- Executables (exe, msi, apk, etc.)
- Fonts (ttf, otf, etc.)
- Databases (db, sqlite, etc.)
- 3D/CAD files (obj, stl, blend, etc.)
- Others (uncategorized files)

---

## 🚀 Features

- Automatic file sorting by extension
- Auto-creates missing folders
- Prevents file overwriting with unique naming
- Supports a wide range of file types
- Simple command-line usage

---

## 🛠️ Technologies

- Python 3
- pathlib
- shutil
- re (regex)

---

## ▶️ Usage

```bash
python folder_organizer.py
