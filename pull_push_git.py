from git import Repo
from config import *


def git_Pull():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.pull("--set-upstream", "origin", "hugo")
        print("Pull successful or repo is up-to-date")
    except:
        print('Some error occured while pushing the code')    


def git_Push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add('.')
        repo.index.commit(COMMIT_MESSAGE)
        # repo.git.push() default argument assumes you are using Quartz 
        repo.git.push("--set-upstream", "origin", "hugo")
        print("Push successful")
    except:
        print('Some error occured while pushing the code')    
    

