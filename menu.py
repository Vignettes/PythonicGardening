from push2gh import createFile 
from gitactions import git_push

def menu():
    usrSelect = input("Start or Finish? ").lower()
    if usrSelect == "start":
        createFile()
    elif usrSelect == "finish":
        git_push()
    else:
        print("Error")

