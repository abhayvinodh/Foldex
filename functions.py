from enum import Flag
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate
import json
import textwrap

root = tk.Tk()
root.withdraw()

def choose_folder():
    print("[+] Choose the Folder to organize")
    org_folder = Path(filedialog.askdirectory(title="Choose the folder to organize "))
    print(f"[i] Selected folder - {org_folder}")
    return org_folder

def display_config(isFile=True, jsondata=False):
    if isFile:
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
    print(tabulate(config_rows, tablefmt="rounded_grid"))
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