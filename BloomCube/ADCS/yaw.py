#yaw calculations
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
    #TODO
    numerator = accelX
    denominator = np.sqrt(accelY**2 + accelZ**2)
    roll = np.arctan2(numerator, denominator)
    roll = roll * (180/np.pi)
    return roll

def pitch_am(accelX,accelY,accelZ):
    #TODO
    numerator = accelY
    denominator = np.sqrt(accelX**2 + accelZ**2)
    pitch = np.arctan2(numerator, denominator)
    pitch = pitch * (180/np.pi)
    return pitch

def yaw_am(accelX,accelY,accelZ,magX,magY,magZ, zeroCalib):
    #TODO
    pitch = pitch_am(accelX,accelY,accelZ)
    pitch = pitch * (180/np.pi)
    roll = roll_am(accelX,accelY,accelZ)
    roll = roll * (180/np.pi)
    degrees = (180/np.pi)*np.arctan2(magY, magX)
    degrees = (degrees + zeroCalib)%360
    return degrees

#Activity 2: RPY based on gyroscope
def roll_gy(prev_angle, delT, gyroX):
    #TODO
    roll = prev_angle + gyroX*delT
    return roll
def pitch_gy(prev_angle, delT, gyroY):
    #TODO
    pitch = prev_angle + gyroY*delT
    return pitch
def yaw_gy(prev_angle, delT, gyroZ):
    #TODO
    yaw = prev_angle + gyroZ*delT
    return yaw

def set_initial(mag_offset):
    #Sets the initial position for plotting and gyro calculations.
    print("Preparing to set initial angle. Please hold the IMU still.")
    time.sleep(7)
    print("Setting angle...")
    accelX, accelY, accelZ = sensor1.accelerometer #m/s^2
    magX, magY, magZ = sensor1.magnetometer #gauss
    #Calibrate magnetometer readings. Defaults to zero until you
    #write the code
    magX = magX - mag_offset[0]
    magY = magY - mag_offset[1]
    magZ = magZ - mag_offset[2]
    roll = roll_am(accelX, accelY,accelZ)
    pitch = pitch_am(accelX,accelY,accelZ)
    yaw = yaw_am(accelX,accelY,accelZ,magX,magY,magZ,0)
    print("Initial angle set.")
    return [roll,pitch,yaw]

def calibrate_mag():
    #TODO: Set up lists, time, etc
    print("Preparing to calibrate magnetometer. Please wave around.")
    time.sleep(3)
    print("Calibrating...")
    #TODO: Calculate calibration constants
    timeout = time.time () + 10
    offsetX = []
    offsetY = []
    offsetZ = []
    while True:
        test = 0
        magX, magY, magZ = sensor1.magnetometer
        offsetX.append(magX)
        offsetY.append(magY)
        offsetZ.append(magZ)
        if test == 5 or time.time() > timeout:
            break
        test = test -1
    mag_offset = [0, 0, 0]
    mag_offset[0] = (max(offsetX) + min(offsetX)) / 2
    mag_offset[1] = (max(offsetY) + min(offsetY)) / 2
    mag_offset[2] = (max(offsetZ) + min(offsetZ)) / 2
    print("Calibration complete.")
    return mag_offset

def calibrate_gyro():
    #TODO
    print("Preparing to calibrate gyroscope. Put down the board and do not touch it.")
    time.sleep(5)
    print('Setting angle...')
    #TODO
    timeout = time.time () + 10
    offsetX = []
    offsetY = []
    offsetZ = []
    while True:
        test = 0
        gyroX, gyroY, gyroZ = sensor2.gyroscope
        gyroX = gyroX * (180/np.pi)
        gyroY = gyroY * (180/np.pi)
        gyroZ = gyroZ * (180/np.pi)
        offsetX.append(gyroX)
        offsetY.append(gyroY)
        offsetZ.append(gyroZ)
        if test == 5 or time.time() > timeout:
            break
        test = test -1
    gyro_offset = [0, 0, 0]
    gyro_offset[0] = (max(offsetX) + min(offsetX)) / 2
    gyro_offset[1] = (max(offsetY) + min(offsetY)) / 2
    gyro_offset[2] = (max(offsetZ) + min(offsetZ)) / 2
    print("Calibration complete.")
    return gyro_offset
