from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate
import json
import textwrap

root = tk.Tk()
root.withdraw()

extension_data = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".pages", ".md", ".tex", ".wps", ".wpd"],
    "Data & Sheets": [".csv", ".xlsx", ".xls", ".xlsm", ".ods", ".numbers", ".json", ".xml", ".yaml", ".yml", ".tsv", ".ini", ".cfg", ".conf"],
    "Presentations": [".ppt", ".pptx", ".odp", ".key"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff", ".tif", ".ico", ".heic", ".heif", ".raw", ".cr2", ".nef", ".arw", ".dng", ".psd", ".ai", ".xcf"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mpeg", ".mpg", ".3gp", ".ts", ".mts"],
    "Audios": [".mp3", ".wav", ".flac", ".aac", ".m4a", ".ogg", ".opus", ".wma", ".aiff", ".mid", ".midi"],
    "Subtitles": [".srt", ".ass", ".ssa", ".sub", ".vtt"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tgz", ".iso", ".cab"],
    "Executables": [".exe", ".msi", ".apk", ".aab", ".app", ".dmg", ".pkg", ".deb", ".rpm", ".bin", ".run", ".jar"],
    "Programming": [".py", ".pyw", ".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".scss", ".java", ".c", ".h", ".cpp", ".hpp", ".cs", ".go", ".rs", ".rb", ".php", ".swift", ".kt", ".dart", ".lua", ".r"],
    "Scripts": [".sh", ".bash", ".zsh", ".bat", ".cmd", ".ps1"],
    "Databases": [".db", ".sqlite", ".sqlite3", ".mdb", ".accdb", ".sql"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "Ebooks": [".epub", ".mobi", ".azw", ".azw3", ".fb2"],
    "CAD & 3D": [".dwg", ".dxf", ".stl", ".obj", ".blend", ".fbx", ".3ds"],
    "Virtual Machines": [".ova", ".ovf", ".vdi", ".vmdk", ".qcow2"],
    "Logs": [".log"],
    "Certificates": [".pem", ".crt", ".cer", ".key", ".p12", ".pfx"],
    "Torrents": [".torrent"],
    "Disk Images": [".iso", ".img", ".vhd", ".vhdx"],
    "Miscellaneous": []
}

def check_config_exists():
    if not Path('config.json').exists():
        with open('config.json', 'w', encoding="utf-8") as file:
            json.dump(extension_data, file, indent=4)

def choose_folder():
    print("[+] Choose the Folder to organize")
    selected_folder = filedialog.askdirectory(title="Choose the folder to organize ")
    if selected_folder:
        org_folder = Path(selected_folder)
        print(f"[i] Selected folder - {org_folder}")
        return org_folder
    return False
def display_config(isFile=True, jsondata=False):
    if isFile:
        check_config_exists()
        with open('config.json', 'r') as file:
            config_data = json.load(file)
    else:
        config_data = json.loads(jsondata)
    config_rows = []
    for destination, extensions in config_data.items():
        formats_string = ", ".join(extensions) or "-"
        formats_string = "\n".join(
            textwrap.wrap(formats_string, width=60)
        )
        config_rows.append([destination, formats_string])
    print(tabulate(config_rows, tablefmt="rounded_outline"))
    return config_data

def checkFolder(folder):
        FolderDir = Path(folder)
        if not FolderDir.is_dir():
            print(f"[i] Folder doesnt exist, creating one..")
            try:
                FolderDir.mkdir(exist_ok=True)
            except Exception as e:
                print("[!] Error Occured\n ->",e)
                return 0
        return 1

def check_destination(fileExt, config_data):
        for destination, extensions in config_data.items():
            if fileExt in extensions:
                return destination
        return "Others"

def moveFiles(file, org_folder, config_data):
        destination = check_destination(file.suffix, config_data)
        if checkFolder(f"{org_folder}/{destination}"):
            try:
                file.rename(f"{org_folder}/{destination}/{file.name}")
                print(f" [✔] Moved {file.name} -> {destination}/{file.name}")
                return True
            except Exception as e:
                print("[!] Error Occured\n ->",e)
                return False
