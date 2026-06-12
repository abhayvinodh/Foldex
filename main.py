#    ___________    .__       .___             
#    \_   _____/___ |  |    __| _/____ ___  ___
#     |    __)/  _ \|  |   / __ |/ __ \\  \/  /
#     |     \(  <_> )  |__/ /_/ \  ___/ >    < 
#     \___  / \____/|____/\____ |\___  >__/\_ \
#         \/                   \/    \/      \/
# GITHUB : https://github.com/abhayvinodh/Foldex.git | V1.0

import ai_organize as ao
import preconfig_org as po
from Functions import display_config
import time
import os

if os.name == 'nt':
    os.system('')

def display_op():
    print("\033[H\033[2J", end="")
    print(f"""
     /$$$$$$$$        /$$       /$$                    
    | $$_____/       | $$      | $$                    
    | $$     /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$   /$$
    | $$$$$ /$$__  $$| $$ /$$__  $$ /$$__  $$|  $$ /$$/
    | $$__/| $$  \ $$| $$| $$  | $$| $$$$$$$$ \  $$$$/ 
    | $$   | $$  | $$| $$| $$  | $$| $$_____/  >$$  $$ 
    | $$   |  $$$$$$/| $$|  $$$$$$$|  $$$$$$$ /$$/\  $$
    |__/    \______/ |__/ \_______/ \_______/|__/  \__/
                                                   
        https://github.com/abhayvinodh/Foldex | V1.0
{'-'*60}""")
    print("""
    [1] - AI Organize
    [2] - Pre-Config Organize
    [3] - View current Config
    [4] - Setup API key again
    [0] - EXIT
    """)

    try:
        op = int(input("Choose Operation > "))
    except ValueError:
        print("[!] Invalid option. Please enter a number.")
        time.sleep(2.4)
        return True

    if op==1:
        ao.main()
    elif op==2:
        po.main()
    elif op==3:
        display_config(isFile=True)
        input("\n[i] Enter to continue...")
    elif op==4:
        ao.setup_key()
    elif op==0:
        print("||| Thankyou for using <3 |||")
        return False
    else:
        print("[!] Invalid option.")
        time.sleep(2.4)
    return True

while True:
    if __name__ == "__main__":
        if not display_op():
            break
