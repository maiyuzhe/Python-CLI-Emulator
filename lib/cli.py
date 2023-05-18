import os
from os import listdir
import os.path
import touch
import subprocess
import time
import random
import webbrowser
terminal_active = True

while terminal_active == True:
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
            # removes file, ex: remove file_name (no quotes)
            os.remove(x.split(" ")[1])
    elif x.split(" ")[0] == "touch":
        if len(x.split(" ")) > 2:
            print("Too many arguments given!")
        else: 
           # creates file within current directory (no quotes)
           touch.touch(x.split(" ")[1])
    elif x.lower()  == "blue pill":
        print("Reality is often disapointing. Now, reality can be whatever you want.")
        #Thanos gif
        print("Exiting Reality............................")
        # matrix animation
        print("Done: Reality Suspended.")
        print("Simulating.................................")
        # matrix animation
        print("Done: New Reality Simulated.")
        print("What did you lose?")
        try:
            thanos_input = subprocess.run(["viu", "Assets/thanos_everything.gif"], timeout=2)
            # deletes all files and directories 
        except: 
            print("Bury your poor little head in the sand now, my sweet prince.")
            os.system('color 0a')
            nums = [1,0,0,1]
            tm = 0
            while tm < 2:
                print(random.randrange(1,5)* "    ",
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
                time.sleep(0.1)
                terminal_active = False
        
        # Quits emulated terminal and opens file displaying something indidating that life is OK
    elif x.lower() == "red pill":
        print("\nBold move, Cotton. Let's see if it pays off.")
        print("Exiting Simulated Reality...................")
        # matrix animation
        print("Done: Simulated Reality Suspended.")
        print("Reconfiguring...............................")
        # matrix animation
        print("Done: Base Reality Configured.")
        print(".")
        terminal_active = False
        # Quits emulated terminal and opens file displaying something indidating that life is shit

    elif "open" in x.split(" ")[0]:
        file_name = x.split(" ")[1]
        if os.path.isfile("./" + x.split(" ")[1]): 
            # opens file, no quotes
            os.system(f"open {file_name}")
        else: 
            print(f"File '{file_name}' does not exist. Perhaps this is the file you were looking for?")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
 
#  thanos_input = subprocess.run(["viu", "Assets/thanos_everything.gif"], timeout=2)
# "thanos_everything.gif"