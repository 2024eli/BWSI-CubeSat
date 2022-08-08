#Name: Team Cam-1 (Evelyn)
#Date: 07/13/2022

import time
from time import sleep
import os
import board
import math
import busio
import adafruit_fxos8700
from git import Repo
from picamera import PiCamera


i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)

"""
When shaken to an aceleration above 20, camera takes picture of
red cardstock from chest height

Args:
    threshold: The threshold for acceleration that has to be passed for
    picture to be taken.
    accel: The accelerometer that is being used. 
    
Returns:
    String message notifying that the picture has been
    taken. and saved as 'red.jpg'

Raises:
    AssertionError: Raised when threshold isn't an integer or when incorrect
    sensor is inputted.
    
"""
def cdstk(threshold, accel):
    assert type(threshold) is int and type(accel) is adafruit_fxos8700.FXOS8700
    #set up imu and camera
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.rotation = 0 #can be 0, 90, 180, or 270
    taken = False #so that the code stops after taking one picture
    while taken == False:
        #detect acceleration
        accelX, accelY, accelZ = accel.accelerometer
        total_accel = math.sqrt(accelX**2 + accelZ**2 + accelY**2)

        print(total_accel)
        if total_accel > threshold:
            print("Shaken")
            camera.start_preview()
            # Camera warm-up time
            sleep(2)
            print("Hold still. Taking picture")
            camera.capture('red.jpg')
            taken = True
            return "Picture taken."
        sleep(2)

def main():
    cdstk(20, sensor)

if __name__ == "__main__":
    main()
