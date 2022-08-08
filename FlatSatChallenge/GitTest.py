#NOTICE COMMENTS BEFORE TESTING

from git import Repo
import os

#function for uploading to Github
def git_push():
    try:
        repo = Repo('/home/pi/FlatSatChallenge')
        repo.git.add('/home/pi/FlatSatChallenge/Images/EvelynLi/')
        repo.index.commit('New Git Test')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes\n')
    except:
        print('couldn\'t upload to git\n')

#ADD YOUR NAME HERE
name = "EvelynLi"

#REPLACE 'yourfolder' with the name of your directory, then Run it!
f = open(r'/home/pi/FlatSatChallenge/Images/EvelynLi/%s.txt' % name,'w')
f.write('%s' % name)
f.close()

git_push()
