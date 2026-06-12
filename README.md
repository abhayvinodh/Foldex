# FOLDEX

A Python-based utility to automatically organize files in a directory into categorized subfolders based on their file extensions. FOLDEX offers both a pre-configured rule-based organization and an intelligent, AI-powered organization using the Gemini API.

---

## 🛠️ Prerequisites & Installation

### 1. Requirements
- **Python 3.x** installed on your system.
- A **Google Gemini API Key** (Required only for the "AI Organize" feature). You can get one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).

   | 🔴 WARNING ⚠ |
   | :---: |
   | **NEVER SHARE YOUR API-KEY !!** |

### 2. Setup Steps
1. **Download/Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/abhayvinodh/Foldex.git
   cd Foldex
   ```

2. **Create a Virtual Environment** (Optional but highly recommended):
   ```bash
   python -m venv venv
   ```
   *Activate it:*
   - **Windows:** `venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`

3. **Install Dependencies**:
   ```bash
   pip install google-genai tabulate
   ```

---

## 🚀 How to Run and Use

Start the application by running the main script in your terminal:
```bash
python main.py
```

### The Interactive Menu
When you run the script, you'll see a styled ASCII command-line menu:

```
        /$$$$$$$$        /$$       /$$                    
       | $$_____/       | $$      | $$                    
       | $$     /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$   /$$
       | $$$$$ /$$__  $$| $$ /$$__  $$ /$$__  $$|  $$ /$$/
       | $$__/| $$  \ $$| $$| $$  | $$| $$$$$$$$ \  $$$$/ 
       | $$   | $$  | $$| $$| $$  | $$| $$_____/  >$$  $$ 
       | $$   |  $$$$$$/| $$|  $$$$$$$|  $$$$$$$ /$$/\  $$
       |__/    \______/ |__/ \_______/ \_______/|__/  \__/
                                                   
           https://github.com/abhayvinodh/Foldex | V1.0
   ------------------------------------------------------------
    [1] - AI Organize (gemini)
    [2] - Pre-Config Organize
    [3] - View current Config
    [4] - Setup API key again
    [0] - EXIT
```

#### Option 1: AI Organize (Smart Mode)
1. Select **[1]**.
2. **API Key Setup:** If this is your first time, the app will ask you to enter your Gemini API Key. Paste the key you got from Google AI Studio. It will be saved locally in a `.KEY` file for future use. (Make sure `.KEY` is kept private and never committed!)
3. **Select Folder:** A native file selection dialog will pop up. Choose the folder you want to organize. If you cancel, the program safely returns to the main menu.
4. **AI Analysis:** The tool scans all files in that folder and sends the list of file extensions to Gemini AI.
5. **Categorization:** The AI groups similar file extensions into logical categories. It displays the proposed structure.
6. **Confirmation:** Type `Y` to confirm. The files will then be moved into their respective new folders.

#### Option 2: Pre-Config Organize (Static Mode)
1. Select **[2]**.
2. **Select Folder:** Choose your target folder via the file dialog.
3. **Review Config:** The app will display your current static configuration (loaded from `config.json`).
4. **Confirmation:** Type `Y` to confirm. The files will be instantly moved based on the rules in `config.json`. Any unrecognized file types will be moved to an "Others" folder.

#### Option 3: View current Config
Select **[3]** to print a cleanly formatted table of your current `config.json` rules so you can see exactly which extensions go into which folders. It wraps long lists of extensions beautifully using a `rounded_outline` table grid.

#### Option 4: Setup API key again
Select **[4]** if you need to update or change your Gemini API key. This simply overwrites the local `.KEY` file.

---

## ⚙️ How It Works Under the Hood

### Automatic Configuration Generation
If `config.json` is missing from the directory, FOLDEX automatically generates one with a comprehensive set of 21 default categories:
*   **Documents**, **Data & Sheets**, **Presentations**, **Images**, **Videos**, **Audios**
*   **Subtitles**, **Archives**, **Executables**, **Programming**, **Scripts**, **Databases**
*   **Fonts**, **Ebooks**, **CAD & 3D**, **Virtual Machines**, **Logs**, **Certificates**
*   **Torrents**, **Disk Images**, and **Miscellaneous**.

You can manually edit this auto-generated `config.json` file in any text editor to customize how files are grouped.

### Moving Files
- The tool uses Python's built-in `pathlib` to handle files safely.
- It scans the target directory but **ignores sub-directories**.
- Files are physically **moved** (not copied) into newly created category folders inside the target directory.

---

## ⚠️ Troubleshooting & Common Errors

- **`google.genai.errors.ServerError: 503 UNAVAILABLE`**: 
  If you see this while using the *AI Organize* feature, it means Google's Gemini API is currently experiencing high demand or is temporarily overloaded. **Solution:** Wait a minute or two and try again.
- **Empty API Key**: Make sure you paste the exact string given by Google AI Studio. If you paste an empty string, the AI feature will not work.
- **`ModuleNotFoundError`**: Ensure you have activated your virtual environment and run `pip install google-genai tabulate`.

---

## 💡 Future Improvements
Here are some planned features and ideas for extending this project:
- **Undo Functionality:** Keep track of the last organization run to easily revert files back to their original locations if a mistake was made.
- **Filename/Content-Based Organization:** Future upgrades will prioritize grouping files by either their filenames or their internal content.
- **Duplicate Handling:** Automatically detect if a file with the same name exists in the target directory and rename it (e.g., `file(1).txt`) instead of crashing or overwriting.
- **Copy vs Move:** Add an option to duplicate/copy the files into the categorized folders instead of physically moving them.
- **Directory Monitoring (Watchdog):** Run the script in the background to automatically organize new files as soon as they are dropped into a specific folder (like your `Downloads` folder).
- **Full GUI:** Transition from a terminal-based interface to a fully standalone Graphical User Interface using a modern framework (like PyQt or CustomTkinter).
