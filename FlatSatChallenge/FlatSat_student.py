#complete CAPITALIZED sections

#AUTHOR: Evelyn Li
#DATE: 07/12/2022

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
        repo = Repo('/home/pi/BWSI-CubeSat/FlatSatChallenge')
        repo.git.add('FlatSatChallenge/Images/EvelynLi') #PATH TO YOUR IMAGES FOLDER, SHOULD BE LOCATED IN FlatSatChallenge/Images/EvelynLi
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')

    
#SET THRESHOLD
threshold = 15

#read acceleration
while True:
    accelX, accelY, accelZ = sensor.accelerometer

    #CHECK IF READINGS ARE ABOVE THRESHOLD
        #PAUSE
    print(math.sqrt(accelX**2 + accelZ**2 + accelY**2)) #take out
    if math.sqrt(accelX**2 + accelZ**2 + accelY**2) > threshold:
        print("reached here") #take out

        sleep(1)

        #TAKE/SAVE/UPLOAD A PICTURE 
        name = "LiE"     #Last Name, First Initial  ex. FoxJ
        
        if name:
            t = time.strftime("_%H%M%S")      # current time string
            #change directory to your folder
            imgname = ('/home/pi/BWSI-CubeSat/FlatSatChallenge/Images/' + name + 'SEC' + t) 
    
            #<YOUR CODE GOES HERE>#
            camera.resolution = (1024, 768)
            camera.start_preview()
            sleep(2)
            print("taking pic") #take out
            camera.capture(imgname + '.jpg')
            #git_push() #in future pull before executing
    
    #PAUSE
    sleep(2)
