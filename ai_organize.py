from time import time
from Functions import display_config, moveFiles, choose_folder
import types
from pathlib import Path
SETUP_FLAG = Path('.KEY')


def setup_key():
    while True:
        key = input("[API] Enter API KEY : ")
        if key:
            SETUP_FLAG.write_text(key)
            print("A")
            return key
        print("[!} API Key shouldn't be empty")
    

def check_key():
    if not SETUP_FLAG.exists():
        print("[!] API KEY not found!", end='')
        choice = input(" SETUP NOW? (Y/N)").lower()
        if choice=='n':
            return False
        setup_key()
    return SETUP_FLAG.read_text()
    

def generate_response(files, key):
    # pyrefly: ignore [missing-import]
    from google import genai
    # pyrefly: ignore [missing-import]
    from google.genai import types
    client = genai.Client(api_key=key)

    instruction = """You are a file classification assistant.
The user will provide a list of filenames.

Your task:
1. Extract the file extensions.
2. Group similar extensions into categories.
3. Create meaningful category names.
4. Include ONLY extensions found in the input.
5. Do NOT add any additional extensions.
6. Each extension must appear exactly once.
7. Return ONLY valid JSON.

Example input:
["report.pdf", "script.py", "component.jsx"]

Example output:
{
    "Documents": [".pdf"],
    "Programming": [".py", ".jsx"]
}
    """
    print("[Ai] Analysing file extensions...")
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=instruction),
        contents=files
    )
    # print(response.text)
    filtered_responce = response.text.replace("```json", "").replace("```", "").strip()
    return filtered_responce

def main():
    success = 0
    failed = 0
    filescount = 0
    key = check_key()
    if not key:
        return
    files = []
    org_folder = choose_folder()
    if not org_folder:
        print("[!] No folder selected")
        time.sleep(2.5)
        return
    for file in org_folder.iterdir():
        if file.is_file():
            files.append(file.name)
    
    jsondata = generate_response(files, key)
    
    config_data = display_config(isFile=False, jsondata=jsondata)
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
        input("\n[↵] Enter to Continue...")
        return True
    print(f"\nTOTAL FILES : {filescount} | SUCCESS : {success} | FAILED : {failed}")
    input("\n[↵] Enter to Continue...")

