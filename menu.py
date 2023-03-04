from push2gh import createFile 
from gitactions import git_push
from editmd import editMd
from config import *

def menu():
    usrSelect = input("Start, Edit or Finish? ").lower()
    if usrSelect == "start":
        createFile()
    elif usrSelect == "finish":
        git_push()
    elif usrSelect == "edit":
        fileName = input("File Name? ") + ".md"
        editMd(contentDir, fileName)
    else:
        print("Error")

