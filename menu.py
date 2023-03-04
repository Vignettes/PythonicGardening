from push2gh import createFile 
from gitactions import git_push
from editmd import editMd
from config import *
import main

def menu():
    usrSelect = input("Start, Edit, Finish, or Quit? ").lower()
    if usrSelect == "start":
        createFile()
    elif usrSelect == "finish":
        git_push()
    elif usrSelect == "edit":
        fileName = input("File Name? ") + ".md"
        editMd(contentDir, fileName)
    elif usrSelect == "quit":
        quit()
    else:
        print("Error")


menu()