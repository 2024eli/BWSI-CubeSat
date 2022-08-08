#Evelyn Li
import time
from git import Repo
import os

def git_push():
    repo = Repo('/home/pi/BloomCube')
    repo.git.add('/home/pi/BloomCube/CritFunc/')
    repo.index.commit('New Boot Test')
    print('made the commit')
    origin = repo.remote('origin')
    print('added remote')
    origin.push()
    print('pushed changes\n')

good = time.ctime()
f = open("/home/pi/BloomCube/CritFunc/time.txt", "w")
f.write("Time created " + good)
f.close()
#git_push()
