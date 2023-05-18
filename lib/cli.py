from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from db.models import Base, FileSystem
import os
import touch
import random
import subprocess
import time
from helpers import Colors

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
 _______ _______  ______ _______ _____ __   _ _______             _______ _______ _     _        _______ _______  _____   ______
    |    |______ |_____/ |  |  |   |   | \  | |_____| |           |______ |  |  | |     | |      |_____|    |    |     | |_____/
    |    |______ |    \_ |  |  | __|__ |  \_| |     | |_____      |______ |  |  | |_____| |_____ |     |    |    |_____| |    \_
                                                                                                                 
''')


terminal_active = True

while terminal_active == True:
    print(Colors.white, "=========================================================================================================================== [")
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
        else:
            # removes file, ex: remove file_name (no quotes)
            os.remove(x.split(" ")[1])
    elif x.split(" ")[0] == "touch":
        if len(x.split(" ")) > 2:
            print("Too many arguments given!")
        else: 
           location = os.getcwd()
           file_name = x.split(" ")[1].split(".")[0]
           file_size = random.randint(1, 10000)
           file_type = x.split(" ")[1].split(".")[1]
           # creates file within current directory (no quotes)
        #    touch.touch(x.split(" ")[1])
           if __name__ == "__main__":
             generate_file_system(location, file_name, file_size, file_type, file_ownership)
        #    os.utime(x.split(" ")[1])
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
        
