#ADCS Test
#this is basically a copy of plot.py with modifications
import time
import board
import numpy as np
import adafruit_fxas21002c
from yaw import *

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxas21002c.FXAS21002C(i2c)
mag_offset = calibrate_mag()
initial_angle = set_initial(mag_offset)
gyro_offset = calibrate_gyro()
yaw = []
xs = []

while True:
    if len(yaw) == 0:
        prev_angle = 0
    else:
        a = yaw[-1]
        prev_angle = a

    gyroX, gyroY, gyroZ = sensor.gyroscope
    gyroZ = gyroZ * (180/np.pi) - gyro_offset[2]
    xs.append(time.time())

    if len(xs) == 1:
        yaw.append(prev_angle)
    else: 
        delT = xs[-1] - xs[-2]
        yaw.append(yaw_gy(prev_angle, delT, gyroZ) % 360)

    yaw = yaw[-20:]

    print("Gyro (degrees): ({0:0.3f})".format(yaw[-1]))
    time.sleep(0.5)
