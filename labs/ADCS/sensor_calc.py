#sensor_calc.py
#Evelyn Li
#07/19/2022

import time
import numpy as np
import adafruit_fxos8700
import adafruit_fxas21002c
import time
import os
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_fxos8700.FXOS8700(i2c)
sensor2 = adafruit_fxas21002c.FXAS21002C(i2c) 


#Activity 1: RPY based on accelerometer and magnetometer
def roll_am(accelX,accelY,accelZ):
    #DONE (degrees)
    roll = (180/np.pi)*np.arctan2(accelX, np.sqrt(accelY**2 + accelZ**2))
    return roll

def pitch_am(accelX,accelY,accelZ):
    #DONE (degrees)
    pitch = (180/np.pi)*np.arctan2(accelY, np.sqrt(accelX**2 + accelZ**2))
    return pitch

def yaw_am(accelX,accelY,accelZ,magX,magY,magZ):
    #DONE (degrees)
    roll = (np.pi/180)*roll_am(accelX, accelY, accelZ)
    pitch = (np.pi/180)*pitch_am(accelX, accelY, accelZ)
    mag_x = (magX*np.cos(pitch) + magY*np.sin(roll) + magZ*np.cos(roll)*np.sin(pitch))
    mag_y = (magY*np.cos(roll) - magY*np.sin(roll))
    return (180/np.pi)*np.arctan2(-mag_y, mag_x)

#Activity 2: RPY based on gyroscope
def roll_gy(prev_angle, delT, gyroX):
    #TODO
    roll = prev_angle + delT*gyroX
    return roll
def pitch_gy(prev_angle, delT, gyroY):
    #TODO
    pitch = prev_angle + delT*gyroY
    return pitch
def yaw_gy(prev_angle, delT, gyroZ):
    #TODO
    yaw = prev_angle + delT*gyroZ
    return yaw

def set_initial(mag_offset = [0,0,0]):
    #Sets the initial position for plotting and gyro calculations.
    print("Preparing to set initial angle. Please hold the IMU still.")
    time.sleep(3)
    print("Setting angle...")
    accelX, accelY, accelZ = sensor1.accelerometer #m/s^2
    magX, magY, magZ = sensor1.magnetometer #gauss
    #Calibrate magnetometer readings. Defaults to zero until you
    #write the code
    offset = mag_offset
    magX = magX - offset[0]
    magY = magY - offset[1]
    magZ = magZ - offset[2]
    roll = roll_am(accelX, accelY,accelZ)
    pitch = pitch_am(accelX,accelY,accelZ)
    yaw = yaw_am(accelX,accelY,accelZ,magX,magY,magZ)
    print("Initial angle set.")
    return [roll,pitch,yaw]

def calibrate_mag():
    #TODO: Set up lists, time, etc
    print("Preparing to calibrate magnetometer. Please wave around.")
    time.sleep(3)
    print("Calibrating...")
    #TODO: Calculate calibration constants
    timeelapse = 10 #seconds
    timestart = time.time()
    magX, magY, magZ = sensor1.magnetometer
    maxiX = magX
    miniX = magX
    maxiY = magY
    miniY = magY
    maxiZ = magZ
    miniZ = magZ
    while time.time() < timestart + timeelapse:
        magX, magY, magZ = sensor1.magnetometer
        time.sleep(1)
        if magX > maxiX:
            maxiX = magX
        if magX < miniX:
            miniX = magX 
        if magY > maxiY:
            maxiY = magY
        if magY < miniY:
            miniY = magY
        if magZ > maxiZ:
            maxiZ = magZ
        if magZ < miniZ:
            miniZ = magZ
    avgX = (miniX + maxiX)/2
    avgY = (miniY + maxiY)/2
    avgZ = (miniZ + maxiZ)/2
    print("Calibration complete.")
    return [avgX,avgY,avgZ]

def calibrate_gyro():
    #TODO
    print("Preparing to calibrate gyroscope. Put down the board and do not touch it.")
    time.sleep(3)
    print("Calibrating...")
    #TODO: Calculate calibration constants
    timeelapse = 10 #seconds
    timestart = time.time()
    gyroX, gyroY, gyroZ = sensor2.gyroscope
    maxiX = gyroX
    miniX = gyroX
    maxiY = gyroY
    miniY = gyroY
    maxiZ = gyroZ
    miniZ = gyroZ
    while time.time() < timestart + timeelapse:
        gyroX, gyroY, gyroZ = sensor2.gyroscope
        time.sleep(1)
        if gyroX > maxiX:
            maxiX = gyroX
        if gyroX < miniX:
            miniX = gyroX 
        if gyroY > maxiY:
            maxiY = gyroY
        if gyroY < miniY:
            miniY = gyroY
        if gyroZ > maxiZ:
            maxiZ = gyroZ
        if gyroZ < miniZ:
            miniZ = gyroZ
    #avg and convert to degrees!!
    avgX = (180/np.pi)*(miniX + maxiX)/2
    avgY = (180/np.pi)*(miniY + maxiY)/2
    avgZ = (180/np.pi)*(miniZ + maxiZ)/2
    print("Calibration complete.")
    return [avgX,avgY,avgZ]
