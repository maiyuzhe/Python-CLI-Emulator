from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import FileSystem
import os

def terminal():
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

def generate_file_system(location, file_name, file_size):
    engine = create_engine('sqlite:///file_system.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    file_system=FileSystem(location=location, file_name=file_name, file_size=file_size)

    session.add(file_system)
    session.commit()

x = input("Enter location, file_name, file_size: ")


if __name__ == "__main__":
    generate_file_system(x.split(" ")[0], x.split(" ")[1], x.split(" ")[2])