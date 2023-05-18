from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from db.models import Base, FileSystem
import os
import touch
import random
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
