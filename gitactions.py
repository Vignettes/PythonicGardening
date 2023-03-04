from git import Repo
from config import *

#PATH_OF_GIT_REPO = r'/Users/georgewolf/Documents/PythonicGardening/'  # make sure .git folder is properly configured
#COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
        print("Push successful")
    except:
        print('Some error occured while pushing the code')    


##