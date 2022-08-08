#magneto
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
y1 = []
xs = []

while True:

    accelX, accelY, accelZ = sensor1.accelerometer
    magX, magY, magZ = sensor1.magnetometer
    magX = magX - mag_offset[0]
    magY = magY - mag_offset[1]
    magZ = magZ - mag_offset[2]
    xs.append(time.time())

    zeroCalib = 362 - initial_angle[2]
    y1.append(yaw_am(accelX, accelY, accelZ, magX, magY, magZ, zeroCalib))

    y1 = y1[-20:]
    print('Magneto Yaw (degrees): ({0:0.3f})'.format(y1[-1]))
    time.sleep(0.5)
