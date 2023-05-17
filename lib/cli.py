import urllib.request
import os
from os import listdir
import touch
import subprocess
import time
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
        print("Done: Reality Simulated.")
        print("What did you lose?")
        # thanos everything gif 
        max_time = 10
        start_time = time.time()  
        while (time.time() - start_time) < max_time:
            thanos_input = subprocess.run(["viu", "Assets/thanos_everything.gif"])
            terminal_active = False
            # deletes all files and directories 
        print("Bury your poor little head in the sand now, my sweet prince.")
        
        
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
        # if inputed file_name does not exist, open rick roll 
        if "file_name" in x: 
            pass
        else:
            # Play rick roll in terminal... still trying to figure this one out lol
            # website = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            #mplayer(str(website))

            urllib.request.urlopen("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
