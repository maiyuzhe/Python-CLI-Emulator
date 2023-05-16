import os

terminal_active = True

while terminal_active == True:
    directory = os.getcwd()
    x = input(f'[{os.getlogin()}@{os.uname().sysname}-{os.uname().machine}] {directory}$ ')
    if x == "exit":
        terminal_active = False
    elif x.split(" ")[0] == "cd":
        if len(x.split(" ")) > 2:
            print("Too many arguments given!")
        else:
            os.chdir(x.split(" ")[1])
    elif x == "ls":
        pass