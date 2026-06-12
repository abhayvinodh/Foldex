from time import time
from Functions import display_config, moveFiles, choose_folder
import types
from pathlib import Path
import time
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
    
def choose_model():
    while True:
        print(f"\n{'-' * 30}\n [1] Gemini-3.5-flash\n [2] Gemini-3.1-pro-preview\n [3] Gemini-3-flash-preview\n [4] Gemini-3.1-flash-lite\n [5] gemini-2.5-flash\n")
        ai_model = int(input("[?] Choose AI model to use > "))
        if ai_model==1:
            return "gemini-3.5-flash"
        elif ai_model==2:
            return "gemini-3.1-pro-preview"
        elif ai_model==3:
            return "gemini-3-flash-preview"
        elif ai_model==4:
            return "gemini-3.1-flash-lite"
        elif ai_model==5:
            return "gemini-2.5-flash"
        else:
            print("[!] INVALID SELECTION... Try Again")
        
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
    ai_model = choose_model()
    print("[Ai] Analysing file extensions...")
    try:
        response = client.models.generate_content(
            model=ai_model,
            config=types.GenerateContentConfig(
                system_instruction=instruction),
            contents=files
        )
    except Exception as e:
        print(e)
        return False
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
    print("\033[H\033[2J", end="")
    print("""
  ╭────────────────────────────╮
  │        AI ORGANIZE         │
  ╰────────────────────────────╯
""")
    files = []
    org_folder = choose_folder()
    if not org_folder:
        print("[!] No folder selected...")
        time.sleep(2.5)
        return
    for file in org_folder.iterdir():
        if file.is_file():
            files.append(file.name)
    
    jsondata = generate_response(files, key)
    if not jsondata:
        return
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

