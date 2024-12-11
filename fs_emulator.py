import zipfile
from pathlib import Path

def load_file_system(zip_path):
    fs = {}
    with zipfile.ZipFile(zip_path, "r") as zf:
        for file in zf.namelist():
            parts = file.split("/")
            current = fs
            for part in parts[:-1]:
                current = current.setdefault(part, {})
            current[parts[-1]] = None  # Файлы храним как `None`
    return fs

def list_files(fs, current_dir):
    parts = current_dir.strip("/").split("/")
    current = fs
    for part in parts:
        if part:
            current = current.get(part, {})
    return "\n".join(current.keys())

def change_directory(fs, current_dir, path):
    if path == "/":
        return "/"
    parts = path.strip("/").split("/")
    current = fs
    for part in parts:
        if part not in current:
            raise ValueError("Directory not found")
        current = current[part]
    return "/" + "/".join(parts)
