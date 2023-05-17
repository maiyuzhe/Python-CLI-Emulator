from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from db.models import Base, FileSystem
from os import listdir
import touch

##Added model generation, will be able to assign file information through this stuff

def generate_file_system(location, file_name, file_size):
    engine = create_engine('sqlite:///file_system.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    file_system=FileSystem(location=location, file_name=file_name, file_size=file_size)

    session.add(file_system)
    session.commit()

x = input("Enter location, file_name, file_size: ")


if __name__ == "__main__":
    generate_file_system(x.split(" ")[0], x.split(" ")[1], x.split(" ")[2])


terminal_active = True

while terminal_active == True:
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
           # creates file within current directory (no quotes)
           touch.touch(x.split(" ")[1])
        #    os.utime(x.split(" ")[1])
