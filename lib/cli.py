import os
from os import listdir
import os.path
import touch
import subprocess
import time
import random
import webbrowser
import pyautogui
from helpers import Colors

print(Colors.green, f'''
 _______ _______  ______ _______ _____ __   _ _______             _______ _______ _     _        _______ _______  _____   ______
    |    |______ |_____/ |  |  |   |   | \  | |_____| |           |______ |  |  | |     | |      |_____|    |    |     | |_____/
    |    |______ |    \_ |  |  | __|__ |  \_| |     | |_____      |______ |  |  | |_____| |_____ |     |    |    |_____| |    \_
                                                                                                                 
''')

terminal_active = True

while terminal_active == True:
    print(Colors.white, "=========================================================================================================================== [")
    directory = os.getcwd()
    x = input(
        f'[{os.getlogin()}@{os.uname().sysname}-{os.uname().machine}] {directory} $ ')
    if x == "exit":
        terminal_active = False
    elif x.split(" ")[0] == "cd":
        if len(x.split(" ")) > 2:
            print("Too many arguments given!")
        else:
            os.chdir(x.split(" ")[1])
    elif x.split(" ")[0] == "ls":
        print(*(os.listdir(directory)),sep="\n")
    elif x.split(" ")[0] == "mkdir":
        if len(x.split(" ")) > 2:
            print("Too many arguments given!")
        else:
            if os.mkdir(x.split(" ")[1]) == "/":
                os.mkdir(x.split(" "))
    elif x.split(" ")[0] == "remove":
        if len(x.split(" ")) > 2:
            print("Too many arguments given!")
        else:
            # removes file, ex: $remove file_name (no quotes)
            os.remove(x.split(" ")[1])
    elif x.split(" ")[0] == "touch":
        if len(x.split(" ")) > 2:
            print("Too many arguments given!")
        else: 
           # creates file within current directory (no quotes)
           touch.touch(x.split(" ")[1])
    elif x.lower()  == "blue pill":
        print(Colors.green,"Reality is often disapointing. Now, reality can be whatever you want.")
        print("=========================================================================")
        time.sleep(1)
        print("Exiting Reality...")
        print("=========================================================================")
        time.sleep(1)
        print("Done: Reality Suspended.")
        print("=========================================================================")
        time.sleep(1)
        print("Simulating...")
        print("=========================================================================")
        time.sleep(1)
        print("Done: New Reality Simulated.")
        print("=========================================================================")
        print("What did you lose?")
        time.sleep(.5)
        try:
            thanos_input = subprocess.run(["viu", "Assets/thanos.gif"], timeout=2)
            print("Bury your poor little head in the sand now, my sweet prince.")
            time.sleep(1.5)
            nums = [1,0]
            tm = 0
            while tm < 10:
                print(Colors.green,random.randrange(1,5)* "    ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),)
                tm = tm + 0.1
                time.sleep(0.01)
            time.sleep(.5)
            print("Simulation Loaded")
            terminal_active = False
        except: 
            print("Bury your poor little head in the sand now, my sweet prince.")
            os.system('color 0a')
            nums = [1,0]
            tm = 0
            while tm < 10:
                print(Colors.green,random.randrange(1,5)* "    ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),random.randrange(1,5)* " ",
                random.choice(nums),)
                tm = tm + 0.1
                time.sleep(0.01)
                terminal_active = False
        
    elif x.lower() == "red pill":
        print(Colors.green,"\nBold move, Cotton. Let's see if it pays off.")
        print("=========================================================================")
        time.sleep(1)
        print("Exiting Simulated Reality...")
        print("=========================================================================")
        time.sleep(1)
        print("Done: Simulated Reality Suspended.")
        print("=========================================================================")
        time.sleep(1)
        print("Reconfiguring...")
        print("=========================================================================")
        # os.system('256color 0a')
        nums = [1,0]
        tm = 0
        time.sleep(1)
        while tm < 10:
            print(Colors.green, random.randrange(1,5)* "    ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),)
            tm = tm + 0.1
            time.sleep(0.01)
        print("Done: Base Reality Configured.")
        terminal_active = False
        
    elif "open" in x.split(" ")[0]:
        file_name = x.split(" ")[1]
        if os.path.isfile("./" + x.split(" ")[1]): 
            # opens file, no quotes
            print(f"Searching for '{file_name}' in files...")
            print(f"Opening '{file_name}'")
            os.system(f"open {file_name}")
        else:
            print(f"File '{file_name}' does not exist. Perhaps this is the file you were looking for?")
            time.sleep(1.5)
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            time.sleep(5)
            pyautogui.moveTo(700, 450, 2)
            time.sleep(.05)
            pyautogui.click()

    # elif x == "test": 
    #     # Move mouse in a square.
    #     for i in range(10): 
    #         pyautogui.moveTo(100, 100, duration=0.25)
    #         pyautogui.moveTo(200, 100, duration=0.25)
    #         pyautogui.moveTo(200, 200, duration=0.25)
    #         pyautogui.moveTo(100, 200, duration=0.25)
    
    elif "display" in x.split(" ")[0]:
        display_input = x.split(" ")[1]
        if ".gif" in x.split(" ")[1]:
            print("control + c to exit")
            os.system(f"viu {display_input}")
        else: 
            os.system(f"viu {display_input}")
            