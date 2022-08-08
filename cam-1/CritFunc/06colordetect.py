#Name: Team Cam-1 (Steve)
#Date: 07/14/2022

import time
from time import sleep
import os
import board
import math
import busio
import adafruit_fxos8700
from git import Repo
from picamera import PiCamera
from tkinter import *
from SimpleCV import Image

#i2c = busio.I2C(board.SCL, board.SDA)
#sensor = adafruit_fxos8700.FXOS8700(i2c)
camera = PiCamera()
camera.resolution = (1024, 768)

while True:
   image = camera.capture('test.jpg')
   img = Image('test.jpg')
   for x in range(0, 1024):
      for y in range(0, 768):
       # get the value of the current pixel
         print img.getPixel(50, 50)

       # check if the red intensity is greater than the green and blue
         if red > green and red > blue:
          # colour pixels which pass the test black
            print("there is red!")
