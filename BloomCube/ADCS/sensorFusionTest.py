#sensor fusion test
import time
import board
import numpy as np
import adafruit_fxas21002c
import adafruit_fxos8700
from yaw import *

i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_fxos8700.FXOS8700(i2c)
sensor2 = adafruit_fxas21002c.FXAS21002C(i2c)

mag_offset = calibrate_mag()
initial_angle = set_initial(mag_offset)
gyro_offset = calibrate_gyro()
yawAM = []
trueYaw = []
xs = []

while True:
    
    accelX, accelY, accelZ = sensor1.accelerometer #m/s^2
    magX, magY, magZ = sensor1.magnetometer #gauss
    #Calibrate magnetometer readings
    magX = magX - mag_offset[0]
    magY = magY - mag_offset[1]
    magZ = magZ - mag_offset[2]
    gyroX, gyroY, gyroZ = sensor2.gyroscope #rad/s
    gyroX = gyroX * (180/np.pi)- gyro_offset[0]
    gyroY = gyroY * (180/np.pi)- gyro_offset[1]
    gyroZ = gyroZ * (180/np.pi)- gyro_offset[2]
    xs.append(time.time())

    zeroCalib = 365 - initial_angle[2]
    yawAM.append(yaw_am(accelX,accelY,accelZ,magX,magY,magZ, zeroCalib))

    if len(trueYaw) == 0:
        prev_angle = yawAM[0]
    else:
        prev_angle = trueYaw[-1]

    if len(xs) == 1:
        trueYaw.append(prev_angle)
    else: 
        delT = xs[-1] - xs[-2]
        trueYaw.append(0.8*(yaw_gy(prev_angle, delT, gyroZ) % 360) + 0.2*yawAM[-1])

    #Keep the plot from being too long
    xs = xs[-20:]
    yawAM = yawAM[-20:]
    trueYaw = trueYaw[-20:]

    print("Gyro and Magnetometer (degrees): ({0:0.3f})".format(trueYaw[-1]))
    time.sleep(0.5)