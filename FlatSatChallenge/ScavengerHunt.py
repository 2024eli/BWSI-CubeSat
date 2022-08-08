#complete CAPITALIZED sections

<<<<<<< HEAD:ScavengerHunt.py
#AUTHOR: Evelyn Li
#DATE: 07/12/2022
=======
#AUTHOR:Fiona McSherry 
#DATE:07/12/2022
>>>>>>> 42c2369017a6f90e5205ca325b8fb66b5964a4b9:Images/Fiona/FlatSat_student.py

#import libraries
import time
from time import sleep
import os
import board
import math
import busio
import adafruit_fxos8700
from git import Repo
from picamera import PiCamera

#setup imu and camera
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)
camera = PiCamera()

#function for uploading image to Github
def git_push():
    try:
<<<<<<< HEAD:ScavengerHunt.py
        repo = Repo('/home/pi/FlatSatChallenge')
        repo.git.add('FlatSatChallenge/Images/EvelynLi') #PATH TO YOUR IMAGES FOLDER, SHOULD BE LOCATED IN FlatSatChallenge/Images/EvelynLi
=======
        repo = Repo('/home/pi/FlatSatChallenge/')
        repo.git.add('/home/pi/FlatSatChallenge/Images/Fiona') #PATH TO YOUR IMAGES FOLDER, SHOULD BE LOCATED IN FlatSatChallenge/Images/YOURFOLDER
>>>>>>> 42c2369017a6f90e5205ca325b8fb66b5964a4b9:Images/Fiona/FlatSat_student.py
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')
#SET THRESHOLD
<<<<<<< HEAD:ScavengerHunt.py
threshold = 17
=======
threshold = 10
>>>>>>> 42c2369017a6f90e5205ca325b8fb66b5964a4b9:Images/Fiona/FlatSat_student.py

#read acceleration
while True:
    accelX, accelY, accelZ = sensor.accelerometer

    #CHECK IF READINGS ARE ABOVE THRESHOLD
        #PAUSE
<<<<<<< HEAD:ScavengerHunt.py
    print(math.sqrt(accelX**2 + accelZ**2 + accelY**2)) #take out
    if math.sqrt(accelX**2 + accelZ**2 + accelY**2) > threshold:
        print("reached here") #take out

        sleep(1)

        #TAKE/SAVE/UPLOAD A PICTURE 
        name = "ScaHunt_COMPUTER"     #Last Name, First Initial  ex. FoxJ
        
        if name:
            t = time.strftime("_%H%M%S")      # current time string
            #change directory to your folder
            imgname = ('/home/pi/FlatSatChallenge/Images/EvelynLi/%s%s' % (name,t)) 
    
            #<YOUR CODE GOES HERE>#
            camera.resolution = (1024, 768)
            camera.start_preview()
            sleep(2)
            print("taking pic") #take out
            camera.capture(imgname + '.jpg')
            git_push() #in future pull before executing
    
=======
    
    if accelY > threshold or accelX  > threshold or accelZ > threshold:
        time.sleep(3)
        #TAKE/SAVE/UPLOAD A PICTURE 
        name = "McSherryF"     #Last Name, First Initial  ex. FoxJ
        
        if name:
            t = time.strftime("_%H%M%S")      # current time string
            imgname = ('/home/pi/FlatSatChallenge/Images/Fiona/%s%s.jpg' % (name,t)) #change directory to your folder
            camera.capture(imgname)
            git_push()
            #<YOUR CODE GOES HERE>#


>>>>>>> 42c2369017a6f90e5205ca325b8fb66b5964a4b9:Images/Fiona/FlatSat_student.py
    #PAUSE
    sleep(2)
