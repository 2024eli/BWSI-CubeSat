#main code for orbiter (in testing phase)

import adafruit_fxos8700
import adafruit_fxas21002c
import time
import os
import board
import busio
from picamera import PiCamera
import numpy as np
import sys
from ADCS.yaw import *
from btcon import *
from Cam.scanner import *
from Cam.color_id import *
from multiprocessing import connection
from btcon import BTCon

#on start up, use btcon functions to send telemetry packet and confirm comms
connection = BTCon('raspberrypi3')
status = connection.connect_repeat_as_client(1, 5)

while status == False:
	connection = BTCon('raspberrypi3')
	status = connection.connect_repeat_as_client(1, 5)

connection.write_string('Shake satellite for 10 seconds')
connection.close_client()

#main code for imaging and sending data
#set initial 0 for IMU, calibrate mag
i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_fxos8700.FXOS8700(i2c)
sensor2 = adafruit_fxas21002c.FXAS21002C(i2c)

mag_offset = calibrate_mag()
time.sleep(5)
initial_angle = set_initial(mag_offset)

connection = BTCon('raspberrypi3')
status = connection.connect_repeat_as_client(1, 5)

while status == False:
	connection = BTCon('raspberrypi3')
	status = connection.connect_repeat_as_client(1, 5)

connection.write_string('Orbit begins')
connection.close_client()
#orbit begins

camTimer = 0.0
imaging = True
imageLoc = 0
imgLocSet = [] # experimental
while imaging:
	
	accelX, accelY, accelZ = sensor1.accelerometer
	magX, magY, magZ = sensor1.magnetometer
	magX = magX - mag_offset[0]
	magY = magY - mag_offset[1]
	magZ = magZ - mag_offset[2]
	zeroCalib = 360 - initial_angle[2]
	location = yaw_am(accelX, accelY, accelZ, magX, magY, magZ, zeroCalib)
	print(location)

	if len(imgLocSet) == 0:
		if camTimer == 1:
			camTimer = 0
		if camTimer == 0:
			test = image_processing()
			if test:
				imageLoc = location
				imaging = False
	if len(imgLocSet) > 0:
		if camTimer == 1:
			camTimer = 0
		if camTimer == 0:
			for i in imgLocSet:
				if i[0] < location and location < i[1]:
					imaging = True
				else:
					test = image_processing()
					if test:
						imageLoc = location
						imaging = False

	camTimer += 0.5
	time.sleep(0.5)
	
	if imaging == False:
		#send file
		#send location
		imgLocRange = (imageLoc - 7, imageLoc + 7) #experimental
		imgLocSet.append(imgLocRange) #experimental
		connection = BTCon('raspberrypi3')
		status = connection.connect_repeat_as_client(1, 5)

		while status == False:
			connection = BTCon('raspberrypi3')
			status = connection.connect_repeat_as_client(1, 5)
		connection.write_string(str(format(imageLoc, '.2f')))
		connection.write_string(str(time.ctime()))
		connection.write_image("/home/pi/BloomCube/satImage/red.jpg")
		connection.close_client()
		imaging = True
