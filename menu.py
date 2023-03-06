from push2gh import createFile 
from gitactions import git_Push
from editmd import editMd
from config import *
import main

def menu():
    usrSelect = input("Start, Edit, Finish, or Quit? ").lower()
    if usrSelect == "start" or usrSelect == "s":
        createFile()
    elif usrSelect == "finish" or usrSelect == "f":
        git_Push()
    elif usrSelect == "edit" or usrSelect == "e":
        fileName = input("File Name? ") + ".md"
        editMd(contentDir, fileName)
    elif usrSelect == "quit" or usrSelect == "q":
        quit()
    else:
        print("Error")


menu()