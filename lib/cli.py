from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from db.models import Base, FileSystem
import os
import random
import time
from helpers import Colors, blue_pill, red_pill, blue_or_red
import pyautogui
import webbrowser
from pathlib import Path

valid_type = ("txt", "exe", "md", "py", "js", "jsx", "db", "json")

location = None
file_name = None
file_size = None
file_type = None
file_ownership = None


##Added model generation, will be able to assign file information through this stuff

def generate_file_system(location, file_name, file_size, file_type, file_ownership):
    engine = create_engine('sqlite:///file_system.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    file_system=FileSystem(location=location, file_name=file_name, file_size=file_size, file_type=file_type, file_ownership=file_ownership)

    session.add(file_system)
    session.commit()


print(Colors.green, f'''

 _______ _______  ______ _______ _____ __   _ _______             
    |    |______ |_____/ |  |  |   |   | \  | |_____| |           
    |    |______ |    \_ |  |  | __|__ |  \_| |     | |_____ 

 _______ _______ _     _        _______ _______  _____   ______
 |______ |  |  | |     | |      |_____|    |    |     | |_____/
 |______ |  |  | |_____| |_____ |     |    |    |_____| |    \_
                           


''')

blue_or_red()
terminal_active = True

while terminal_active == True:
    print(Colors.white)
    file_ownership=os.getlogin()
    directory = os.getcwd()
    x = input(
        f'[{os.getlogin()}@{os.uname().sysname}-{os.uname().machine}] {directory}$ ')
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
        elif os.path.isdir("./" + x.split(" ")[1]) == True:
            print("Cannot remove directory. Input type must be a file.")
        else:
            # removes file, ex: remove file_name (no quotes)
            os.remove(x.split(" ")[1])
    elif x.split(" ")[0] == "touch":
        if len(x.split(" ")) > 2:
            print("Too many arguments given!")
        elif x.split(" ")[1].split(".")[1] in valid_type: 
           new_file = os.getcwd()+"/"+x.split(" ")[1]
           Path(new_file).touch()
           location = os.getcwd()
           file_name = x.split(" ")[1].split(".")[0]
           file_size = random.randint(1, 10000)
           file_type = x.split(" ")[1].split(".")[1]
        else:
            print("File type invalid!")

        if __name__ == "__main__":
            generate_file_system(location, file_name, file_size, file_type, file_ownership)
    elif x.lower() == "red pill":
        red_pill()
    elif x.lower() == "blue pill":
        print("You've already taken the blue pill, silly!")
    elif "open" in x.split(" ")[0]:
        file_name = x.split(" ")[1]
        if os.path.isfile("./" + x.split(" ")[1]): 
            # opens file, no quotes
            print(f"Searching for '{file_name}' in files...")
            print(f"Opening '{file_name}'")
            os.system(f"open {file_name}")
            engine = create_engine('sqlite:///file_system.db')
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            print(session.query(FileSystem).filter(FileSystem.file_name==x.split(" ")[1].split(".")[0]).first())
        else:
            print(f"File '{file_name}' does not exist. Perhaps this is the file you were looking for?")
            time.sleep(1.5)
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            time.sleep(5)
            # moves cursor to center of (my) screen and clicks-- 
            # may not work on other devices bc of screen sizes 
            # (pyautogui.size() ==> size of screen)
            pyautogui.moveTo(700, 450, 2)
            time.sleep(.05)
            pyautogui.click()
    elif "display" in x.split(" ")[0]:
        display_input = x.split(" ")[1]
        if ".gif" in x.split(" ")[1]:
            print("control + c to exit")
            os.system(f"viu {display_input}")
        else: 
            os.system(f"viu {display_input}")
    elif x == "clear":
            os.system('clear')