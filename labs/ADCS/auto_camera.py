import adafruit_fxos8700
import adafruit_fxas21002c
import time
import os
import board
import busio
from picamera import PiCamera
import numpy as np
import math
import sys
from sensor_calc import *

i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_fxos8700.FXOS8700(i2c)
sensor2 = adafruit_fxas21002c.FXAS21002C(i2c)
camera = PiCamera()

#Code to take a picture at a given offset angle
def capture(dir ='yaw', target_angle = 45):
    #Calibration lines should remain commented out until you implement calibration
    offset_mag = calibrate_mag()
    offset_gyro =calibrate_gyro()
    initial_angle = set_initial(offset_mag)
    prev_angle = initial_angle
    print("Begin moving camera.")
    while True:
        accelX, accelY, accelZ = sensor1.accelerometer #m/s^2
        magX, magY, magZ = sensor1.magnetometer #gauss
	#Calibrate magnetometer readings
        magX = magX - offset_mag[0]
        magY = magY - offset_mag[1]
        magZ = magZ - offset_mag[2]
        gyroX, gyroY, gyroZ = sensor2.gyroscope #rad/s
        #Convert to degrees and calibrate
        gyroX = gyroX *180/np.pi - offset_gyro[0]
        gyroY = gyroY *180/np.pi - offset_gyro[1]
        gyroZ = gyroZ *180/np.pi - offset_gyro[2]

        #TODO: Everything else! Be sure to not take a picture on exactly a
        #certain angle: give yourself some margin for error. 
        if dir == 'yaw':
            yaw_angle = yaw_am(accelX, accelY, accelZ, magX, magY, magZ)
            while abs(yaw_angle - initial_angle[2]) >  target_angle:
                yaw_angle = yaw_am(accelX, accelY, accelZ, magX, magY, magZ)
                print(yaw_angle - initial_angle)
                time.sleep(2)
            print("FOUND AND CAPTURING")
            camera.resolution = (1024, 768)
            camera.start_preview()
            time.sleep(2)
            print("taking pic") #take out
            imgname = dir + str(target_angle)
            camera.capture('/home/pi/Labs/ADCS/Images/' + imgname+ '.jpg')
            print("pic taken")
            break
    return "done"

if __name__ == '__main__':
    capture(*sys.argv[1:])
