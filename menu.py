from create_md import createFile 
from pull_push_git import git_Push, git_Pull
from edit_md import editMd
from config import *


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

git_Pull()

menu()