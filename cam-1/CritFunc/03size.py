#Name: Team Cam-1 (Evelyn)
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


#i2c = busio.I2C(board.SCL, board.SDA)
#sensor = adafruit_fxos8700.FXOS8700(i2c)
camera = PiCamera()

"""
Names files according to their resolution. 

Args:
    resw: the number of pixels in the width of the jpg
    resh: the number of pixels in the height of the jpg

Returns:
    String containing the name of the file

Raises:
    AssertionError: Raised when width or height are not integers
"""
def name(resw, resh):
    assert type(resw) is int and type(resh) is int
    filen = "/home/pi/cam-1/CritFunc/03Images/" + str(resw) + "by" + str(resh) + ".jpg"
    return filen

"""
Produces up to 10 images of varying sizes that are in increments
of an inputted factor. 

Args:
    widthfactor: The factor that the width is incremented by
    heightfactor: The factor that the height is incremented by

Returns:
    Either a string notifying that the program has finished or 
    a string notifying that the program was aborted

Raises:
    AssertionError: Raised when widthfactor and heightfactor are 
    not integers
"""
def size(widthfactor, heightfactor):
    #min res is 64x64, max res is 3280 x 2464 
    assert type(widthfactor) is int and type(heightfactor) is int
    maxfiles = 5 #for storage purposes
    initialw = 64
    initialh = 64
    yayornay = input("Ready to take a picture? Yes or No?\n")
    if yayornay == "Yes":
        for i in range(1, maxfiles+1):
            curw = 64 * widthfactor * i
            curh = 64 * heightfactor * i
            if curw <= 3280 and curh <= 2464:
                camera.resolution = (curw, curh)
                camera.capture(name(curw, curh))
                sleep(1)
        return "Finished"
    return "Did not take photos"
        
def main():
    print(size(1, 1))

if __name__ == "__main__":
    main()
