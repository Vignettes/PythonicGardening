from git import Repo
from config import *



def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add('.')
        repo.index.commit(COMMIT_MESSAGE)
        repo.git.push("--set-upstream", "origin", "hugo")
        # origin = repo.remote(name='origin')
        # origin.push()
        print("Push successful")
    except:
        print('Some error occured while pushing the code')    


