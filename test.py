from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, FileSystem
import sqlalchemy
# import os
# import random
# import time
# from helpers import Colors, red_pill, blue_or_red, load
# import pyautogui
# import webbrowser

engine = create_engine('sqlite:///file_system.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

print(session.query(FileSystem).filter(FileSystem.file_name=="new_txt").first())