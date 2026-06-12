from functions import display_config, choose_folder, moveFiles
import json
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def main():
    success = 0
    failed = 0
    filescount = 0
    print("\033[H\033[2J", end="")
    print("----| Pre-Config Organize |----")

    org_folder = choose_folder()
    config_data = display_config()
    confirm = input("[?] Organize with this current config? (Y/N) : ").lower()
    if confirm!='y':
        return
    print('\n')

    for file in org_folder.iterdir():
        if file.is_file():
            filescount+=1
            if moveFiles(file, org_folder, config_data):
                success+=1
            else:
                failed+=1
    if not filescount:
        print(f"\n[!] No files exists in {org_folder} to organize..")
        input("\n[i] Enter anthing..")
        return True
    print(f"\nTOTAL FILES : {filescount} | SUCCESS : {success} | FAILED : {failed}")
    input("\n[i] Enter anthing..")


